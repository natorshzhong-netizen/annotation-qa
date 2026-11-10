# -*- coding: utf-8 -*-
"""一致性度量 —— Day 1 你要写的就这四个函数。

别去 pip install 任何统计库。这四个函数都用标准库实现，
面试官问「kappa 怎么算的」时，你要能当场在纸上写出来。
"""

import random
from collections import Counter


def pairwise_agreement(a: dict[str, str], b: dict[str, str], ids: list[str]) -> float:
    """两个标注者的一致率（简单百分比）。

    参数
        a, b  : {样本id: 标签}
        ids   : 要统计的样本 id 列表（顺序无所谓）

    返回
        0.0 ~ 1.0 之间的小数。比如 30 条里 25 条一致 → 0.8333...

    注意
        分母是 len(ids)，不是交集大小。缺样本请让 load.validate 先拦住。
    """
    same = 0
    for i in ids:
        if a[i] == b[i]:
            same += 1
    return same / len(ids)


def cohen_kappa(a: dict[str, str], b: dict[str, str],
                labels: list[str], ids: list[str]) -> float:
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
    n = len(ids)
    if n == 0:
        return 0.0

    po = sum(1 for i in ids if a[i] == b[i]) / n

    pe = 0.0
    for label in labels:
        pa = sum(1 for i in ids if a[i] == label) / n
        pb = sum(1 for i in ids if b[i] == label) / n
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
        按「分歧严重程度」排序：三人全不同 > 2:1 分裂。
        同一档内按 id 排。

    用途
        这份清单是给质检员看的——他要拿这个去问标注员「你为什么这么标」。
    """
    names = sorted(anns)
    out = []
    for i in ids:
        votes = {x: anns[x][i] for x in names}
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
