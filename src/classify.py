# -*- coding: utf-8 -*-
"""把「争议样本」分成三类：规范未覆盖 / 系统性偏差 / 个别错误。

分类思路：

1. 先看这条样本有没有「多数派」。
   - 三个人各标一种 → 没有多数派，多半是规范没写清。
   - 两个人一样、一个人不同 → 有少数派，继续往下看。

2. 再看这个少数派是不是「惯犯」。
   - 统计每个人在所有争议里当少数派的次数，以及他偏的是哪一类。
   - 如果某个人当少数派的次数够多，而且高度集中在同一个标签上，
     先看主导标签占比是否 >= 60%，再做二项检验并用 BH 校正多重比较。
   - 标注者一多，只按次数判断会把随机波动误报成系统性偏差。

3. 合起来判断。
   - 少数派的标签，正好是他平时的偏差标签 → 系统性偏差
   - 少数派没有这种习惯 → 个别错误（可能是疏忽，也可能是规范歧义）
"""

import math
from collections import Counter

# 一个人至少当几次少数派，才值得怀疑他有系统性偏差
MIN_MINORITY = 3
# 他的少数派标注里，同一个标签至少占多少比例，才算「集中」
DOMINANT_RATIO = 0.6
# 二项检验的显著性水平（再做 BH 多重校正）
ALPHA = 0.05


def minority_profile(anns: dict[str, dict[str, str]],
                     ids: list[str]) -> dict[str, dict]:
    """统计每个标注者「当少数派」的情况。

    返回
        {
          "b": {"count": 5, "labels": {"商品咨询": 4, "物流查询": 1}},
          "c": {"count": 7, "labels": {"其他": 2, "投诉建议": 2, ...}},
        }

    什么叫「当少数派」
        一条样本里，大多数人都标 A，只有他标了 B —— 他就是少数派。
        如果三个人标得各不相同（比如 A/B/C），就没有多数派，这条不计入。
    """
    names = sorted(anns)
    profile = {x: {"count": 0, "labels": Counter(), "opportunities": 0} for x in names}

    for i in ids:
        votes = {x: anns[x][i] for x in names if i in anns[x]}
        if len(votes) < 2:
            continue
        counts = Counter(votes.values())

        if len(counts) == 1:            # 全员一致：每个人都有「不偏离」的机会
            for x in votes:
                profile[x]["opportunities"] += 1
            continue
        top = counts.most_common()
        if len(top) >= 2 and top[0][1] == top[1][1]:   # 平票：每个人各标一种
            continue

        majority = top[0][0]
        for x, label in votes.items():
            profile[x]["opportunities"] += 1
            if label != majority:
                profile[x]["count"] += 1
                profile[x]["labels"][label] += 1

    return profile


def systematic_details(profile: dict[str, dict],
                       min_minority: int = MIN_MINORITY,
                       dominant_ratio: float = DOMINANT_RATIO,
                       alpha: float = ALPHA,
                       labels: list[str] | None = None) -> list[dict]:
    """给每个标注者算「当少数派」的统计显著性。

    零假设：这个人的少数派标签分布和全体标注者一样随机。
    用留一平滑估计目标标签在全体少数派里的占比 p0，再做单侧二项正态近似检验，
    最后用 Benjamini-Hochberg 控制多重比较的假阳性。

    为什么不能只看次数
        HateXplain 有 157 个标注者，只偏离两三次的人一大把；
        固定阈值会把「随机波动」全部报成系统性偏差。
    为什么不能只比整体偏离率
        b 只在「商品咨询」这一类上偏，整体偏离率可能只有 8%，和平均水平差不多；
        真正的信号是「他每次偏都偏向同一个标签」，所以检验的是标签集中度。
    """
    label_totals: Counter[str] = Counter()
    for p in profile.values():
        label_totals.update(p["labels"])
    total_minority = sum(label_totals.values())
    num_labels = max(1, len(labels) if labels else len(label_totals))

    rows = []
    for name, p in profile.items():
        n = p.get("opportunities", 0)
        k = p["count"]
        if n == 0 or not p["labels"]:
            continue
        label, times = p["labels"].most_common(1)[0]
        dominance = times / k if k else 0.0
        rate = k / n

        # 留一平滑：去掉本人后，这个标签在全体少数派里的占比
        p0 = (label_totals[label] - times + 1) / (total_minority - k + num_labels)
        p0 = min(max(p0, 1e-9), 1 - 1e-9)

        mean = k * p0
        sd = math.sqrt(k * p0 * (1 - p0))
        z = (times - mean - 0.5) / sd if sd > 0 else 0.0
        p_value = 0.5 * math.erfc(z / math.sqrt(2))

        rows.append({
            "name": name,
            "label": label,
            "count": k,
            "opportunities": n,
            "rate": rate,
            "dominance": dominance,
            "expected_share": p0,
            "p_value": p_value,
            "q_value": 1.0,
            "systematic": False,
        })

    m = len(rows)
    ordered = sorted(range(m), key=lambda idx: rows[idx]["p_value"])
    previous = 1.0
    for rank_idx in range(m - 1, -1, -1):
        idx = ordered[rank_idx]
        q = min(previous, rows[idx]["p_value"] * m / (rank_idx + 1))
        rows[idx]["q_value"] = min(q, 1.0)
        previous = rows[idx]["q_value"]

    for row in rows:
        row["systematic"] = (
            row["q_value"] < alpha
            and row["count"] >= min_minority
            and row["dominance"] >= dominant_ratio
        )
    return rows


def find_systematic(profile: dict[str, dict],
                    min_minority: int = MIN_MINORITY,
                    dominant_ratio: float = DOMINANT_RATIO,
                    alpha: float = ALPHA,
                    use_stats: bool = True,
                    labels: list[str] | None = None) -> dict[str, str]:
    """找出有系统性偏差的人，返回 {人: 他偏的那个标签}。

    判定条件（三个都要满足）：
      1. 当少数派次数 >= min_minority
      2. 他偏的标签里，最多的那个占比 >= dominant_ratio
      3. 相对整体少数派比例显著偏高（BH 校正后 q < alpha）

    没有 opportunities 字段的旧 profile 会退回只按前两条判断。
    """
    if use_stats and all("opportunities" in p for p in profile.values()):
        return {
            row["name"]: row["label"]
            for row in systematic_details(
                profile, min_minority, dominant_ratio, alpha, labels
            )
            if row["systematic"]
        }

    result = {}
    for name, p in profile.items():
        if p["count"] < min_minority or not p["labels"]:
            continue
        label, times = p["labels"].most_common(1)[0]
        if times / p["count"] >= dominant_ratio:
            result[name] = label
    return result


def classify_disputes(anns: dict[str, dict[str, str]],
                      ids: list[str],
                      min_minority: int = MIN_MINORITY,
                      dominant_ratio: float = DOMINANT_RATIO,
                      labels: list[str] | None = None) -> list[dict]:
    """给每条争议样本打上原因标签。

    返回
        [
          {"id": "T14", "votes": {...}, "category": "规范未覆盖", "reason": "..."},
          ...
        ]
    """
    names = sorted(anns)
    profile = minority_profile(anns, ids)
    systematic = find_systematic(
        profile, min_minority, dominant_ratio, labels=labels
    )

    out = []
    for i in ids:
        votes = {x: anns[x][i] for x in names if i in anns[x]}
        if len(votes) < 2:
            continue
        counts = Counter(votes.values())

        if len(counts) == 1:
            continue

        top = counts.most_common()

        # 情况一：没有多数派（每个人各标一种）
        if len(top) >= 2 and top[0][1] == top[1][1]:
            out.append({
                "id": i,
                "votes": votes,
                "category": "规范未覆盖",
                "reason": f"{len(votes)} 人各标一种，没有多数派——多半是规范没写清这种情况怎么处理",
            })
            continue

        # 情况二：有 2:1 的多数派
        majority = top[0][0]
        minority_people = [x for x in votes if votes[x] != majority]

        # 少数派里，有没有人的标签正好撞上他自己的「老毛病」
        hit = [x for x in minority_people if systematic.get(x) == votes[x]]

        if hit:
            who = "、".join(hit)
            bad = votes[hit[0]]
            out.append({
                "id": i,
                "votes": votes,
                "category": "系统性偏差",
                "reason": f"{who} 反复把这一类标成「{bad}」，是固定的理解偏差",
            })
        else:
            who = "、".join(minority_people)
            out.append({
                "id": i,
                "votes": votes,
                "category": "个别错误",
                "reason": f"{who} 的标注偏离多数派，但本人没有固定倾向——可能是疏忽，也可能是规范有歧义",
            })

    return out


def apply_third_opinion(classified: list[dict], items: dict, spec: str,
                        cache_path, log=print) -> list[dict]:
    """让模型盲判一遍，再和人类多数派对照。

    三种结果：
        模型说「无法确定」         → 改判为「规范未覆盖」
        模型和多数派一致           → 维持原判（少数派确实错了）
        模型和多数派不一致         → 标记「可疑」，可能是共同错误
    """
    import json
    from pathlib import Path

    from . import llm

    cache_path = Path(cache_path)
    cache = {}
    if cache_path.exists():
        cache = json.loads(cache_path.read_text(encoding="utf-8"))

    for d in classified:
        iid = d["id"]
        d["rule_category"] = d["category"]   # 先留一份规则的原判，后面可能被推翻
        if iid not in cache:
            log(f"  询问模型：{iid} …")
            cache[iid] = llm.judge(spec, items[iid])
            cache_path.parent.mkdir(parents=True, exist_ok=True)
            cache_path.write_text(
                json.dumps(cache, ensure_ascii=False, indent=2), encoding="utf-8"
            )

        third = cache[iid]
        d["third"] = third

        counts = Counter(d["votes"].values())
        top = counts.most_common()
        # 平票时没有多数派，不能拿 Counter 的第一个当多数
        has_majority = not (len(top) >= 2 and top[0][1] == top[1][1])
        majority = top[0][0] if has_majority else None

        if third["label"] == llm.UNDECIDED:
            d["verdict"] = "规范未覆盖"
            d["category"] = "规范未覆盖"
        elif not has_majority:
            d["verdict"] = "无多数派"
            d["third_note"] = f"模型独立判定为「{third['label']}」"
        elif third["label"] == majority:
            d["verdict"] = "维持"
        else:
            d["verdict"] = "可疑"
            d["third_note"] = f"模型认为是「{third['label']}」，多数派是「{majority}」"
            # 规则想归因到某个人，但第三方不同意——这条不该硬判
            d["category"] = "待人工复核"
            d["reason"] = (
                f"规则判为「{d.get('rule_category', '个体问题')}」，"
                f"但模型独立判断为「{third['label']}」——两种解释都成立，需人工裁决"
            )

    return classified


def summarize(classified: list[dict]) -> dict[str, int]:
    """数一数每类各有几条。"""
    c = Counter(d["category"] for d in classified)
    return {
        "规范未覆盖": c.get("规范未覆盖", 0),
        "系统性偏差": c.get("系统性偏差", 0),
        "个别错误": c.get("个别错误", 0),
        "待人工复核": c.get("待人工复核", 0),
    }


def confusion_pairs(anns: dict[str, dict[str, str]], ids: list[str]) -> dict:
    """统计「多数派本该是 A，却有人标成 B」的次数。

    返回
        {("退款退货", "商品咨询"): {"count": 2, "who": {"b": 2}}, ...}
        key 是 (多数派标签, 少数派标签)
    """
    names = sorted(anns)
    pairs: dict = {}

    for i in ids:
        votes = {x: anns[x][i] for x in names if i in anns[x]}
        if len(votes) < 2:
            continue
        counts = Counter(votes.values())
        if len(counts) == 1:
            continue
        top = counts.most_common()
        if len(top) >= 2 and top[0][1] == top[1][1]:
            continue                        # 平票，没有多数派

        majority = top[0][0]
        for x, label in votes.items():
            if label == majority:
                continue
            item = pairs.setdefault(
                (majority, label), {"count": 0, "who": Counter()}
            )
            item["count"] += 1
            item["who"][x] += 1

    return pairs


def action_items(classified: list[dict], anns: dict, ids: list[str],
                 items: dict, labels: list[str] | None = None) -> list[dict]:
    """把判定结果翻译成「人今天该干什么」。

    输出顺序 = 处理优先级：
        补规范 → 培训 → 人工裁决 → 加抽检
    """
    profile = minority_profile(anns, ids)
    systematic = find_systematic(profile, labels=labels)
    actions = []

    # 1. 补规范
    for d in classified:
        if d["category"] != "规范未覆盖":
            continue
        text = items.get(d["id"], "")
        actions.append({
            "type": "补规范",
            "text": f'{d["id"]}「{text}」—— 没有多数派，确认归哪类后写进规范',
        })

    # 2. 培训（按人合并成一条）
    for name, label in sorted(systematic.items()):
        p = profile[name]
        times = p["labels"].get(label, 0)
        actions.append({
            "type": "培训",
            "text": (
                f"{name}：{p['count']} 次偏离中有 {times} 次选了「{label}」，"
                f"方向高度集中 —— 安排一次定义对齐，不是让他重标"
            ),
        })

    # 3. 人工裁决
    for d in classified:
        if d["category"] != "待人工复核":
            continue
        text = items.get(d["id"], "")
        note = d.get("third_note", "")
        actions.append({
            "type": "人工裁决",
            "text": f'{d["id"]}「{text}」—— 规则与第三方结论冲突（{note}），主管拍板',
        })

    # 4. 加抽检
    for name, p in sorted(profile.items()):
        if name in systematic or p["count"] < MIN_MINORITY:
            continue
        actions.append({
            "type": "加抽检",
            "text": f"{name}：{p['count']} 次偏离但方向分散 —— 提高抽检比例，不必培训",
        })

    return actions
