# -*- coding: utf-8 -*-
"""把一致性指标和归因结果拼成一份 Markdown 报告。

报告分六节：总体一致性、两两一致性、争议清单、原因分析、混淆矩阵、行动清单。
大数据集会自动切换为汇总视图，并用 max_rows 限制单表行数。
"""
import statistics
from itertools import combinations
from pathlib import Path

from . import classify, metrics

ROOT = Path(__file__).resolve().parent.parent
MAX_TABLE_ROWS = 30


def _cell(text: str) -> str:
    """转义 Markdown 表格里会破坏结构的字符。"""
    return str(text).replace("|", "\\|").replace("\r", " ").replace("\n", " ")


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
                 cache_path=None, max_rows: int = MAX_TABLE_ROWS) -> str:
    if not items:
        raise ValueError("没有样本，无法生成报告")
    ids = sorted(items)
    names = sorted(anns)
    n_items = len(ids)

    out = []
    out.append("# 标注一致性报告")
    out.append("")
    out.append(f"- 样本数：**{n_items}**")
    shown = ", ".join(names[:12])
    if len(names) > 12:
        shown += f" …（共 {len(names)} 人）"
    else:
        shown += f"（共 {len(names)} 人）"
    out.append(f"- 标注者：{shown}")
    out.append(f"- 类别数：{len(labels)}")
    out.append("")

    # ---- 总体 ----
    complete = metrics.is_complete(anns, ids)
    if complete:
        value = metrics.fleiss_kappa(anns, labels, ids)
        lo, hi = metrics.bootstrap_kappa(anns, labels, ids)
        metric_name = f"Fleiss' kappa（{len(names)} 人）"
    else:
        value = metrics.krippendorff_alpha(anns, labels, ids)
        lo, hi = metrics.bootstrap_alpha(anns, labels, ids)
        metric_name = "Krippendorff's alpha（名义尺度，支持缺标）"

    out.append("## 一、总体一致性")
    out.append("")
    out.append("| 指标 | 数值 | 档位 |")
    out.append("|---|---|---|")
    out.append(f"| {metric_name} | {value:.4f} | {_bar(value)} |")
    out.append(f"| 95% 置信区间 | [{lo:.3f}, {hi:.3f}] | 1000 次 bootstrap |")
    out.append("")
    out.append(
        f"> {n_items} 条样本，区间宽度 {hi - lo:.2f}。"
        "**方向可信（明显高于随机水平），但具体数值需谨慎看待。**"
    )
    out.append("")

    if not complete:
        out.append("### 标注覆盖")
        out.append("")
        out.append("| 标注者 | 标注条数 | 覆盖率 |")
        out.append("|---|---|---|")
        coverage = sorted(
            ((name, len(set(anns[name]) & set(ids))) for name in names),
            key=lambda item: (-item[1], item[0]),
        )
        for name, count in coverage[:max_rows]:
            out.append(f"| {_cell(name)} | {count} / {n_items} | {count / n_items:.0%} |")
        if len(coverage) > max_rows:
            out.append("")
            out.append(f"> 按标注条数排序，仅显示前 {max_rows} 人（共 {len(coverage)} 人）。")
        out.append("")
        out.append(
            "> 有人漏标，Fleiss' kappa 不适用，改用 Krippendorff's alpha；"
            "两两一致性只统计双方共同标注过的样本。"
        )
        out.append("")

    # ---- 两两 ----
    out.append("## 二、两两一致性")
    out.append("")
    pairs = []
    for x, y in combinations(names, 2):
        common = metrics.co_rated_ids(anns[x], anns[y], ids)
        if not common:
            continue
        pairs.append({
            "a": x,
            "b": y,
            "n": len(common),
            "agr": metrics.pairwise_agreement(anns[x], anns[y], common),
            "kappa": metrics.cohen_kappa(anns[x], anns[y], labels, common),
        })

    if len(pairs) <= 20:
        out.append("| 标注者 A | 标注者 B | 共同标注 | 一致率 | Cohen's kappa | 档位 |")
        out.append("|---|---|---|---|---|---|")
        for p in pairs:
            out.append(
                f"| {_cell(p['a'])} | {_cell(p['b'])} | {p['n']} | "
                f"{p['agr']:.2%} | {p['kappa']:.4f} | {_bar(p['kappa'])} |"
            )
    else:
        agrs = [p["agr"] for p in pairs]
        kappas = [p["kappa"] for p in pairs]
        out.append(f"标注者较多（{len(names)} 人，{len(pairs)} 对组合），这里只给汇总；")
        out.append("")
        out.append("| 指标 | 均值 | 中位数 | 最小 | 最大 |")
        out.append("|---|---|---|---|---|")
        out.append(
            f"| 一致率 | {statistics.mean(agrs):.2%} | {statistics.median(agrs):.2%} | "
            f"{min(agrs):.2%} | {max(agrs):.2%} |"
        )
        out.append(
            f"| Cohen's kappa | {statistics.mean(kappas):.4f} | {statistics.median(kappas):.4f} | "
            f"{min(kappas):.4f} | {max(kappas):.4f} |"
        )
        out.append("")
        out.append(f"共同标注最多的 {min(10, max_rows)} 对（样本量越大越可靠）：")
        out.append("")
        out.append("| 标注者 A | 标注者 B | 共同标注 | 一致率 | Cohen's kappa | 档位 |")
        out.append("|---|---|---|---|---|---|")
        for p in sorted(pairs, key=lambda item: (-item["n"], item["a"], item["b"]))[:min(10, max_rows)]:
            out.append(
                f"| {_cell(p['a'])} | {_cell(p['b'])} | {p['n']} | "
                f"{p['agr']:.2%} | {p['kappa']:.4f} | {_bar(p['kappa'])} |"
            )
    out.append("")

    # ---- 争议样本 ----
    dis = metrics.disputed_items(anns, ids)
    out.append(f"## 三、争议样本清单（{len(dis)} 条）")
    out.append("")
    if not dis:
        out.append("> 全部样本一致，无需处理。")
    else:
        out.append("| 样本 ID | 文本 | 投票 | 分歧度 |")
        out.append("|---|---|---|---|")
        for d in dis[:max_rows]:
            text = _cell(items[d["id"]])
            text = text if len(text) <= 24 else text[:24] + "…"
            votes = "；".join(f"{n}={_cell(d['votes'][n])}" for n in sorted(d["votes"]))
            out.append(
                f"| {_cell(d['id'])} | {text} | {votes} | {d.get('n_distinct', '')} 种 |"
            )
        if len(dis) > max_rows:
            out.append("")
            out.append(f"> 仅显示分歧度最高的 {max_rows} 条，共 {len(dis)} 条。")
    out.append("")

    # ---- 分歧原因分析 ----
    classified = classify.classify_disputes(anns, ids, labels=labels)

    if use_llm:
        spec_text = spec or (ROOT / "data" / "spec.md").read_text(encoding="utf-8")
        classify.apply_third_opinion(
            classified, items, spec_text,
            cache_path or (ROOT / "out" / "llm_cache.json"),
        )

    stats = classify.summarize(classified)
    profile = classify.minority_profile(anns, ids)
    details = classify.systematic_details(profile, labels=labels)
    detail_map = {row["name"]: row for row in details}

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
    out.append("| 标注者 | 少数派次数 / 机会 | 主导标签 | 主导占比 | q 值 | 判定 |")
    out.append("|---|---|---|---|---|---|")
    ranked = sorted(names, key=lambda n: (-profile[n]["count"], n))
    for name in ranked[:max_rows]:
        p = profile[name]
        if p["count"] == 0:
            out.append(f"| {_cell(name)} | 0 / {p.get('opportunities', 0)} | — | — | — | 无偏离 |")
            continue
        row = detail_map.get(name)
        if not row:
            out.append(f"| {_cell(name)} | {p['count']} / {p.get('opportunities', 0)} | — | — | — | — |")
            continue
        q = "<0.001" if row["q_value"] < 0.001 else f"{row['q_value']:.3f}"
        if row["systematic"]:
            verdict = "系统性偏差"
        elif row["q_value"] < classify.ALPHA:
            verdict = "显著但分散"
        else:
            verdict = "无明显规律"
        out.append(
            f"| {_cell(name)} | {row['count']} / {row['opportunities']} | {_cell(row['label'])} | "
            f"{row['dominance']:.0%} | {q} | **{verdict}** |"
        )
    if len(ranked) > max_rows:
        out.append("")
        out.append(f"> 按少数派次数排序，仅显示前 {max_rows} 人（共 {len(ranked)} 人）。")
    out.append("")
    out.append(
        "> q 值 = 二项检验 p 值经 Benjamini-Hochberg 校正后的结果。"
        "只按次数判断时，标注者一多，随机波动就会被误报成系统性偏差。"
        "「显著但分散」表示集中度显著、但主导标签占比低于 60%，不归为系统性偏差。"
    )
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
    for d in classified[:max_rows]:
        votes = " / ".join(
            f"{n}={_cell(d['votes'][n])}" for n in names if n in d["votes"]
        )
        if use_llm and "verdict" in d:
            v = d["verdict"]
            if v == "维持":
                third = f"✓ 支持多数派（{d['third']['label']}）"
            elif v == "可疑":
                third = f"⚠ 模型认为是「{d['third']['label']}」"
            elif v == "无多数派":
                third = f"模型独立判定「{d['third']['label']}」（本条 {len(d['votes'])} 人各不同）"
            else:
                third = "模型判「无法确定」"
            out.append(
                f"| {_cell(d['id'])}<br>{votes} | **{d['category']}** | {_cell(third)} | {_cell(d['reason'])} |"
            )
        else:
            out.append(
                f"| {_cell(d['id'])}<br>{votes} | **{d['category']}** | {_cell(d['reason'])} |"
            )
    if len(classified) > max_rows:
        out.append("")
        out.append(f"> 仅显示前 {max_rows} 条，共 {len(classified)} 条争议。")
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
        out.append("| 多数派 ＼ 少数派 | " + " | ".join(_cell(c) for c in cols) + " |")
        out.append("|" + "---|" * (len(cols) + 1))
        for r in rows:
            cells = []
            for c in cols:
                v = pairs.get((r, c))
                cells.append(str(v["count"]) if v else "")
            out.append(f"| **{_cell(r)}** | " + " | ".join(cells) + " |")
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
    actions = classify.action_items(classified, anns, ids, items, labels=labels)
    out.append("## 六、本周行动")
    out.append("")
    if not actions:
        out.append("> 没有需要处理的项。")
    else:
        order = {"补规范": 1, "培训": 2, "人工裁决": 3, "加抽检": 4}
        actions.sort(key=lambda a: order.get(a["type"], 9))
        for i, a in enumerate(actions[:max_rows], 1):
            out.append(f"{i}. **【{a['type']}】** {_cell(a['text'])}")
        if len(actions) > max_rows:
            out.append("")
            out.append(f"> 仅显示前 {max_rows} 项，共 {len(actions)} 项。")
    out.append("")

    return "\n".join(out)
