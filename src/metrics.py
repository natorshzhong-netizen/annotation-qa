# -*- coding: utf-8 -*-
"""一致性度量：一致率、Cohen's / Fleiss' kappa、Krippendorff's alpha、bootstrap 区间。

全部用标准库实现，不引入运行时依赖；测试里再用 scipy / scikit-learn 的
参考实现做数值对拍，保证公式没有写偏。
"""

import random
from collections import Counter


def co_rated_ids(a: dict[str, str], b: dict[str, str], ids: list[str] | None = None) -> list[str]:
    """两个人共同标注过的样本 id，按字典序返回。"""
    if ids is None:
        return sorted(set(a) & set(b))
    return [i for i in sorted(ids) if i in a and i in b]


def is_complete(anns: dict[str, dict[str, str]], ids: list[str]) -> bool:
    """是否所有标注者都标了全部样本（Fleiss' kappa 的前提）。"""
    if not anns or not ids:
        return False
    target = set(ids)
    return all(set(a) >= target for a in anns.values())


def pairwise_agreement(a: dict[str, str], b: dict[str, str], ids: list[str] | None = None) -> float:
    """两个标注者的一致率（简单百分比）。

    参数
        a, b  : {样本id: 标签}
        ids   : 要统计的样本 id 列表；None 表示取两人共同标注过的样本

    返回
        0.0 ~ 1.0 之间的小数。比如 30 条里 25 条一致 → 0.8333...

    注意
        分母是共同标注的样本数。两人没有共同标注时返回 0.0。
    """
    common = co_rated_ids(a, b, ids)
    if not common:
        return 0.0
    same = 0
    for i in common:
        if a[i] == b[i]:
            same += 1
    return same / len(common)


def cohen_kappa(a: dict[str, str], b: dict[str, str],
                labels: list[str], ids: list[str] | None = None) -> float:
    """两个标注者的 Cohen's kappa。

    公式
        po = 一致率（就是上面那个函数）
        pe = Σ_over_labels  p_a(L) * p_b(L)
             其中 p_a(L) = a 把多少比例的样本标成了 L
        kappa = (po - pe) / (1 - pe)

    为什么要减去 pe
        两个人就算完全瞎猜，也会因为类别分布而碰巧对上一些。
        pe 就是「碰巧对上」的期望比例，减掉它才是真本事。

    返回
        -1.0 ~ 1.0。常见解读：<0.2 差，0.2~0.4 一般，
        0.4~0.6 中等，0.6~0.8 较好，>0.8 很好。

    边界情况
        如果 pe == 1.0（比如两人都只标了一个类），分母为 0，
        这时直接返回 1.0 并写一行注释说明——别让程序崩。
    """
    common = co_rated_ids(a, b, ids)
    n = len(common)
    if n == 0:
        return 0.0

    po = sum(1 for i in common if a[i] == b[i]) / n

    pe = 0.0
    for label in labels:
        pa = sum(1 for i in common if a[i] == label) / n
        pb = sum(1 for i in common if b[i] == label) / n
        pe += pa * pb

    if pe >= 1.0:          # 两人分布完全相同且退化成单一类别，避免除零
        return 1.0
    return (po - pe) / (1 - pe)


def fleiss_kappa(anns: dict[str, dict[str, str]],
                 labels: list[str], ids: list[str]) -> float:
    """多个标注者的 Fleiss' kappa（3 人及以上用这个）。

    公式
        对每条样本 i：
            n_ij = 第 j 个类别被多少人标了
            n    = 标注者总数
            P_i  = (Σ_j n_ij² - n) / (n * (n - 1))
            ↑ 直观理解：所有人都一致时 P_i = 1，完全分裂时接近 0

        P_bar = 所有 P_i 的平均
        p_j   = 类别 j 被标注的总次数 / (样本数 * n)
        P_e   = Σ_j p_j²
        kappa = (P_bar - P_e) / (1 - P_e)

    返回
        同 Cohen's kappa 的取值范围。
    """
    names = list(anns)
    n = len(names)
    if n < 2 or not ids:
        return 0.0
    if not is_complete(anns, ids):
        raise ValueError(
            "Fleiss' kappa 要求每个标注者都标全；"
            "有缺失值时请改用 krippendorff_alpha（它支持缺标）。"
        )

    # 每条样本的「一致程度」P_i
    P = []
    for i in ids:
        counts = Counter(anns[x][i] for x in names)
        s = sum(v * v for v in counts.values())
        P.append((s - n) / (n * (n - 1)))
    P_bar = sum(P) / len(P)

    # 每个类别被标注的总次数
    total = Counter()
    for x in names:
        for i in ids:
            total[anns[x][i]] += 1

    denom = len(ids) * n
    P_e = sum((total[label] / denom) ** 2 for label in labels)

    if P_e >= 1.0:
        return 1.0
    return (P_bar - P_e) / (1 - P_e)


def disputed_items(anns: dict[str, dict[str, str]],
                   ids: list[str]) -> list[dict]:
    """找出所有「不是全员一致」的样本。

    返回
        [
          {"id": "T14", "votes": {"a": "退款退货", "b": "商品咨询", "c": "投诉建议"},
           "split": "3:0:0" 之类可以不要，但建议带上 n_distinct},
          ...
        ]
        按「分歧严重程度」排序：全员各不同 > 2:1 分裂。
        同一档内按 id 排。

    用途
        这份清单是给质检员看的——他要拿这个去问标注员「你为什么这么标」。
    """
    names = sorted(anns)
    out = []
    for i in ids:
        votes = {x: anns[x][i] for x in names if i in anns[x]}
        n_distinct = len(set(votes.values()))
        if n_distinct > 1:
            out.append({"id": i, "votes": votes, "n_distinct": n_distinct})

    # 分歧越大排越前；同档按 id 排，保证每次结果一样
    out.sort(key=lambda d: (-d["n_distinct"], d["id"]))
    return out


def bootstrap_kappa(anns: dict[str, dict[str, str]],
                    labels: list[str], ids: list[str],
                    n_boot: int = 1000, seed: int = 42) -> tuple[float, float]:
    """用 bootstrap 给 Fleiss kappa 算一个 95% 置信区间。

    为什么要它
        30 条样本算出来的 0.6978，换一批数据可能是 0.55，也可能是 0.82。
        只报一个数，等于假装自己很确定。

    怎么做
        把样本有放回地重抽 n_boot 次（每次还是 30 条，但可能重复），
        每次都重算一次 kappa，得到 n_boot 个值，
        取第 2.5% 和第 97.5% 分位，就是 95% 区间。

    seed 固定
        保证每次跑出来一样，报告可复现。
    """
    if not ids:
        return 0.0, 0.0

    rng = random.Random(seed)
    n = len(ids)
    vals = []
    for _ in range(n_boot):
        sample = [rng.choice(ids) for _ in range(n)]   # 有放回抽样
        vals.append(fleiss_kappa(anns, labels, sample))

    vals.sort()
    lo = vals[int(0.025 * n_boot)]
    hi = vals[int(0.975 * n_boot) - 1]
    return lo, hi


def krippendorff_alpha(anns: dict[str, dict[str, str]],
                       labels: list[str],
                       ids: list[str] | None = None) -> float:
    """Krippendorff's alpha（名义尺度，支持缺标）。

    为什么不用 Fleiss
        Fleiss 要求「每个人都标了每一条」。真实众包数据里几乎做不到：
        有人请假、有人漏标、不同人负责不同批次。Krippendorff 按
        「可配对的标注值」计算，缺标不影响，是行业里更通用的选择。

    公式
        对每条样本 u，m_u 个标注值两两配对，构成重合矩阵 o：
            o_ck += n_c * n_k / (m_u - 1)      （c ≠ k）
            o_cc += n_c * (n_c - 1) / (m_u - 1)
        n    = 重合矩阵总和（可配对标注值数）
        D_o  = Σ_{c≠k} o_ck / n                      观察到的分歧
        D_e  = Σ_{c≠k} n_c n_k / (n(n-1))            随机期望的分歧
        alpha = 1 - D_o / D_e

        名义尺度下 δ²(c,k) = 1（c≠k），所以上面直接数不同值。
    """
    names = sorted(anns)
    if len(names) < 2:
        return 0.0
    if ids is None:
        ids = sorted({i for a in anns.values() for i in a})

    coincidence: dict[tuple[str, str], float] = {}
    for i in ids:
        values = [anns[x][i] for x in names if i in anns[x]]
        m = len(values)
        if m < 2:
            continue
        counts = Counter(values)
        for c, nc in counts.items():
            for k, nk in counts.items():
                weight = nc * (nc - 1) if c == k else nc * nk
                key = (c, k)
                coincidence[key] = coincidence.get(key, 0.0) + weight / (m - 1)

    n = sum(coincidence.values())
    if n < 2:
        return 0.0

    d_o = sum(v for (c, k), v in coincidence.items() if c != k) / n

    marginals: dict[str, float] = {}
    for (c, _k), v in coincidence.items():
        marginals[c] = marginals.get(c, 0.0) + v

    d_e = sum(
        marginals[c] * marginals[k]
        for c in marginals
        for k in marginals
        if c != k
    ) / (n * (n - 1))

    if d_e == 0:          # 所有标注值都相同，没有可解释的随机分歧
        return 1.0
    return 1.0 - d_o / d_e


def bootstrap_alpha(anns: dict[str, dict[str, str]],
                    labels: list[str], ids: list[str],
                    n_boot: int = 1000, seed: int = 42) -> tuple[float, float]:
    """给 Krippendorff's alpha 算 95% bootstrap 区间（样本有放回重抽）。"""
    ids = sorted(ids)
    if not ids:
        return 0.0, 0.0

    rng = random.Random(seed)
    n = len(ids)
    vals = []
    for _ in range(n_boot):
        sample = [rng.choice(ids) for _ in range(n)]
        vals.append(krippendorff_alpha(anns, labels, sample))

    vals.sort()
    return vals[int(0.025 * n_boot)], vals[int(0.975 * n_boot) - 1]
