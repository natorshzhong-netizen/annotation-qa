# -*- coding: utf-8 -*-
"""把 metrics 的计算结果拼成一份 Markdown 报告。

这个文件已经写好了，Day 1 不用改。
等你 metrics.py 的四个函数全部实现，`python -m src` 就能跑出报告。
"""
from itertools import combinations
from pathlib import Path

from . import classify, metrics

ROOT = Path(__file__).resolve().parent.parent


def _bar(kappa: float) -> str:
    """给 kappa 一个人类可读的档位。Landis & Koch 的经典分档。"""
    if kappa < 0.2:
        return "差"
    if kappa < 0.4:
        return "一般"
    if kappa < 0.6:
        return "中等"
    if kappa < 0.8:
        return "较好"
    return "很好"


def build_report(items: dict, labels: list[str], anns: dict,
                 use_llm: bool = False, spec: str = "",
                 cache_path=None) -> str:
    ids = sorted(items)
    names = sorted(anns)
    n_items = len(ids)

    out = []
    out.append("# 标注一致性报告")
    out.append("")
    out.append(f"- 样本数：**{n_items}**")
    out.append(f"- 标注者：{', '.join(names)}（共 {len(names)} 人）")
    out.append(f"- 类别数：{len(labels)}")
    out.append("")

    # ---- 总体 ----
    fk = metrics.fleiss_kappa(anns, labels, ids)
    lo, hi = metrics.bootstrap_kappa(anns, labels, ids)
    out.append("## 一、总体一致性")
    out.append("")
    out.append("| 指标 | 数值 | 档位 |")
    out.append("|---|---|---|")
    out.append(f"| Fleiss' kappa（{len(names)} 人） | {fk:.4f} | {_bar(fk)} |")
    out.append(f"| 95% 置信区间 | [{lo:.3f}, {hi:.3f}] | 1000 次 bootstrap |")
    out.append("")
    out.append(
        f"> {n_items} 条样本，区间宽度 {hi - lo:.2f}。"
        "**方向可信（明显高于随机水平），但具体数值需谨慎看待。**"
    )
    out.append("")

    # ---- 两两 ----
    out.append("## 二、两两一致性")
    out.append("")
    out.append("| 标注者 A | 标注者 B | 一致条数 | 一致率 | Cohen's kappa | 档位 |")
    out.append("|---|---|---|---|---|---|")
    for x, y in combinations(names, 2):
        agr = metrics.pairwise_agreement(anns[x], anns[y], ids)
        ck = metrics.cohen_kappa(anns[x], anns[y], labels, ids)
        out.append(
            f"| {x} | {y} | {round(agr * n_items)} / {n_items} | "
            f"{agr:.2%} | {ck:.4f} | {_bar(ck)} |"
        )
    out.append("")

    # ---- 争议样本 ----
    dis = metrics.disputed_items(anns, ids)
    out.append(f"## 三、争议样本清单（{len(dis)} 条）")
    out.append("")
    if not dis:
        out.append("> 全部样本一致，无需处理。")
    else:
        header = ["样本 ID", "文本"] + names + ["分歧度"]
        out.append("| " + " | ".join(header) + " |")
        out.append("|" + "---|" * len(header))
        for d in dis:
            text = items[d["id"]]
            text = text if len(text) <= 24 else text[:24] + "…"
            votes = [d["votes"].get(n, "-") for n in names]
            out.append(
                f"| {d['id']} | {text} | " + " | ".join(votes) +
                f" | {d.get('n_distinct', '')} 种 |"
            )
    out.append("")

    # ---- 分歧原因分析 ----
    classified = classify.classify_disputes(anns, ids)

    if use_llm:
        spec_text = spec or (ROOT / "data" / "spec.md").read_text(encoding="utf-8")
        classify.apply_third_opinion(
            classified, items, spec_text,
            cache_path or (ROOT / "out" / "llm_cache.json"),
        )

    stats = classify.summarize(classified)
    profile = classify.minority_profile(anns, ids)
    systematic = classify.find_systematic(profile)

    out.append("## 四、分歧原因分析")
    out.append("")
    out.append("| 原因 | 条数 | 该谁处理 |")
    out.append("|---|---|---|")
    out.append(f"| 规范未覆盖 | {stats['规范未覆盖']} | 补规范，跟标注员无关 |")
    out.append(f"| 系统性偏差 | {stats['系统性偏差']} | 找当事人培训 |")
    out.append(f"| 个别错误 | {stats['个别错误']} | 加抽检，不必培训 |")
    out.append(f"| 待人工复核 | {stats['待人工复核']} | 规则和第三方冲突，人工裁决 |")
    out.append("")

    # 每个人的「少数派画像」——这是分类的证据
    out.append("### 谁的标注习惯有问题")
    out.append("")
    out.append("| 标注者 | 当少数派次数 | 偏得最多的标签 | 判定 |")
    out.append("|---|---|---|---|")
    for name in names:
        p = profile[name]
        if p["count"] == 0:
            out.append(f"| {name} | 0 | — | 无偏离 |")
            continue
        top_label, top_times = p["labels"].most_common(1)[0]
        verdict = f"系统性偏差（{systematic[name]}）" if name in systematic else "无明显规律"
        out.append(f"| {name} | {p['count']} | {top_label}（{top_times} 次） | {verdict} |")
    out.append("")

    # 逐条判定
    out.append("### 逐条判定")
    out.append("")
    if use_llm:
        out.append("| 样本 | 判定 | 第三方复核 | 依据 |")
        out.append("|---|---|---|---|")
    else:
        out.append("| 样本 | 判定 | 依据 |")
        out.append("|---|---|---|")
    for d in classified:
        votes = " / ".join(f"{n}={d['votes'][n]}" for n in names)
        if use_llm and "verdict" in d:
            v = d["verdict"]
            if v == "维持":
                third = f"✓ 支持多数派（{d['third']['label']}）"
            elif v == "可疑":
                third = f"⚠ 模型认为是「{d['third']['label']}」"
            elif v == "无多数派":
                third = f"模型独立判定「{d['third']['label']}」（本条三人各不同）"
            else:
                third = "模型判「无法确定」"
            out.append(
                f"| {d['id']}<br>{votes} | **{d['category']}** | {third} | {d['reason']} |"
            )
        else:
            out.append(f"| {d['id']}<br>{votes} | **{d['category']}** | {d['reason']} |")
    out.append("")

    if use_llm:
        suspicious = [d for d in classified if d.get("verdict") == "可疑"]
        out.append(
            f"> 第三方复核：{len(classified) - len(suspicious)} 条与多数派一致，"
            f"**{len(suspicious)} 条可疑**（可能是共同错误，建议人工复核）。"
        )
        out.append("")

    # ---- 混淆矩阵 ----
    pairs = classify.confusion_pairs(anns, ids)
    if pairs:
        rows = sorted({k[0] for k in pairs})
        cols = sorted({k[1] for k in pairs})

        out.append("## 五、哪两类最容易混")
        out.append("")
        out.append("行 = 多数派本该选的类别，列 = 少数派实际选的类别。")
        out.append("")
        out.append("| 多数派 ＼ 少数派 | " + " | ".join(cols) + " |")
        out.append("|" + "---|" * (len(cols) + 1))
        for r in rows:
            cells = []
            for c in cols:
                v = pairs.get((r, c))
                cells.append(str(v["count"]) if v else "")
            out.append(f"| **{r}** | " + " | ".join(cells) + " |")
        out.append("")

        max_count = max(v["count"] for v in pairs.values())
        tops = [(k, v) for k, v in pairs.items() if v["count"] == max_count]
        parts = []
        for (src, dst), info in sorted(tops):
            who = "、".join(f"{k}×{v}" for k, v in info["who"].most_common())
            parts.append(f"「{src}」→「{dst}」{max_count} 次（{who}）")
        out.append("> 最集中的混淆：" + "；".join(parts) + "。")
        out.append("")
        out.append(
            "> 若同一格里全是同一个人，更像**个人理解偏差**（培训）；"
            "若分散在多人身上，更像**两类定义本身模糊**（补规范）。"
        )
        out.append("")

    # ---- 行动清单 ----
    actions = classify.action_items(classified, anns, ids, items)
    out.append("## 六、本周行动")
    out.append("")
    if not actions:
        out.append("> 没有需要处理的项。")
    else:
        order = {"补规范": 1, "培训": 2, "人工裁决": 3, "加抽检": 4}
        actions.sort(key=lambda a: order.get(a["type"], 9))
        for i, a in enumerate(actions, 1):
            out.append(f"{i}. **【{a['type']}】** {a['text']}")
    out.append("")

    return "\n".join(out)
