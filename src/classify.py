# -*- coding: utf-8 -*-
"""把「争议样本」分成三类：规范未覆盖 / 系统性偏差 / 个别错误。

分类思路（也是你面试要讲的那套）：

1. 先看这条样本有没有「多数派」。
   - 三个人各标一种 → 没有多数派，多半是规范没写清。
   - 两个人一样、一个人不同 → 有少数派，继续往下看。

2. 再看这个少数派是不是「惯犯」。
   - 统计每个人在所有争议里当少数派的次数，以及他偏的是哪一类。
   - 如果某个人当少数派的次数够多，而且高度集中在同一个标签上，
     说明他不是随机错，而是对那一类有固定的理解偏差。

3. 合起来判断。
   - 少数派的标签，正好是他平时的偏差标签 → 系统性偏差
   - 少数派没有这种习惯 → 个别错误（可能是疏忽，也可能是规范歧义）
"""

from collections import Counter

# 一个人至少当几次少数派，才值得怀疑他有系统性偏差
MIN_MINORITY = 2
# 他的少数派标注里，同一个标签至少占多少比例，才算「集中」
DOMINANT_RATIO = 0.6


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
    profile = {x: {"count": 0, "labels": Counter()} for x in names}

    for i in ids:
        votes = {x: anns[x][i] for x in names}
        counts = Counter(votes.values())

        if len(counts) == 1:            # 全员一致，不是争议
            continue
        top = counts.most_common()
        if len(top) >= 2 and top[0][1] == top[1][1]:   # 平票（三人各一种）
            continue

        majority = top[0][0]
        for x, label in votes.items():
            if label != majority:
                profile[x]["count"] += 1
                profile[x]["labels"][label] += 1

    return profile


def find_systematic(profile: dict[str, dict]) -> dict[str, str]:
    """找出有系统性偏差的人，返回 {人: 他偏的那个标签}。

    判定条件（两个都要满足）：
      1. 当少数派的次数 >= MIN_MINORITY
      2. 他偏的标签里，最多的那个占比 >= DOMINANT_RATIO
    """
    result = {}
    for name, p in profile.items():
        if p["count"] < MIN_MINORITY or not p["labels"]:
            continue
        label, times = p["labels"].most_common(1)[0]
        if times / p["count"] >= DOMINANT_RATIO:
            result[name] = label
    return result


def classify_disputes(anns: dict[str, dict[str, str]],
                      ids: list[str]) -> list[dict]:
    """给每条争议样本打上原因标签。

    返回
        [
          {"id": "T14", "votes": {...}, "category": "规范未覆盖", "reason": "..."},
          ...
        ]
    """
    names = sorted(anns)
    profile = minority_profile(anns, ids)
    systematic = find_systematic(profile)

    out = []
    for i in ids:
        votes = {x: anns[x][i] for x in names}
        counts = Counter(votes.values())

        if len(counts) == 1:
            continue

        top = counts.most_common()

        # 情况一：没有多数派（三人各标一种）
        if len(top) >= 2 and top[0][1] == top[1][1]:
            out.append({
                "id": i,
                "votes": votes,
                "category": "规范未覆盖",
                "reason": "三人各标一种，没有多数派——多半是规范没写清这种情况怎么处理",
            })
            continue

        # 情况二：有 2:1 的多数派
        majority = top[0][0]
        minority_people = [x for x in names if votes[x] != majority]

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
        # 三人各标一种时没有多数派，不能拿 Counter 的第一个当多数
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
        votes = {x: anns[x][i] for x in names}
        counts = Counter(votes.values())
        if len(counts) == 1:
            continue
        top = counts.most_common()
        if len(top) >= 2 and top[0][1] == top[1][1]:
            continue                        # 三人各一种，没有多数派

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
                 items: dict) -> list[dict]:
    """把判定结果翻译成「人今天该干什么」。

    输出顺序 = 处理优先级：
        补规范 → 培训 → 人工裁决 → 加抽检
    """
    profile = minority_profile(anns, ids)
    systematic = find_systematic(profile)
    actions = []

    # 1. 补规范
    for d in classified:
        if d["category"] != "规范未覆盖":
            continue
        text = items.get(d["id"], "")
        actions.append({
            "type": "补规范",
            "text": f'{d["id"]}「{text}」—— 三人各持一说，确认归哪类后写进规范',
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
