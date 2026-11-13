# -*- coding: utf-8 -*-
"""归因准确率评测：合成真值 vs 工具的判定。

用法
    python eval/run_attribution_eval.py --seeds 20 --items 300
    python eval/run_attribution_eval.py --seeds 10 --noise 0.05   # 带未知原因的噪声

判定口径
    每条样本都要么是「无争议」，要么是三类原因之一。
    工具没输出、但真值也不是争议的样本，记为「无争议」。
    noise 造成的争议原因不明，真值里没有，评测时从分母里剔除，单独报告数量。
"""

from __future__ import annotations

import argparse
import json
import statistics
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

from eval.generate import generate  # noqa: E402
from src import classify  # noqa: E402

CLASSES = ["规范未覆盖", "系统性偏差", "个别错误", "无争议"]


def baseline_predict(anns: dict[str, dict[str, str]], ids: list[str]) -> dict[str, str]:
    """只用「有没有多数派」的简单基线。"""
    pred = {}
    for i in ids:
        votes = [anns[x][i] for x in anns if i in anns[x]]
        if len(votes) < 2:
            continue
        counts = Counter(votes)
        top = counts.most_common()
        if len(counts) == 1:
            continue
        if len(top) >= 2 and top[0][1] == top[1][1]:
            pred[i] = "规范未覆盖"
        else:
            pred[i] = "个别错误"
    return pred


def prf(truth: dict[str, str], pred: dict[str, str]) -> dict[str, dict[str, float]]:
    """按类别算 precision / recall / F1，返回 {类别: {...}}。"""
    matrix = {t: {p: 0 for p in CLASSES} for t in CLASSES}
    for i, expected in truth.items():
        matrix[expected][pred.get(i, "无争议")] += 1

    out = {}
    for cls in CLASSES:
        tp = matrix[cls][cls]
        predicted = sum(matrix[t][cls] for t in CLASSES)
        actual = sum(matrix[cls].values())
        precision = tp / predicted if predicted else 0.0
        recall = tp / actual if actual else 0.0
        f1 = 2 * precision * recall / (precision + recall) if precision + recall else 0.0
        out[cls] = {
            "precision": precision,
            "recall": recall,
            "f1": f1,
            "support": actual,
            "predicted": predicted,
        }
    out["macro_f1"] = {
        "precision": 0.0,
        "recall": 0.0,
        "f1": sum(out[c]["f1"] for c in CLASSES) / len(CLASSES),
        "support": 0,
        "predicted": 0,
    }
    return out


def evaluate_seed(seed: int, n_items: int, noise_rate: float) -> dict:
    _, labels, anns, truth = generate(n_items=n_items, seed=seed, noise_rate=noise_rate)
    ids = sorted(truth.keys() | {i for a in anns.values() for i in a})

    predicted = classify.classify_disputes(anns, ids, labels=labels)
    pred = {d["id"]: d["category"] for d in predicted}

    # 原因不明的争议：工具报了，但真值里没有 → 不参与准确率
    unlabeled = sorted(i for i in pred if i not in truth and pred[i] != "无争议")
    skip = set(unlabeled)

    labeled_truth = {}
    for i in ids:
        if i in skip:
            continue
        labeled_truth[i] = truth.get(i, "无争议")

    labeled_pred = {i: pred.get(i, "无争议") for i in labeled_truth}
    base_pred = {i: baseline_predict(anns, ids).get(i, "无争议") for i in labeled_truth}

    result = prf(labeled_truth, labeled_pred)
    base = prf(labeled_truth, base_pred)
    return {
        "seed": seed,
        "items": n_items,
        "labeled_items": len(labeled_truth),
        "unlabeled_disputes": len(unlabeled),
        "confusion": {
            t: {p: sum(1 for i, exp in labeled_truth.items()
                       if exp == t and labeled_pred[i] == p) for p in CLASSES}
            for t in CLASSES
        },
        "tool": result,
        "baseline": base,
        "macro_f1": result["macro_f1"]["f1"],
        "baseline_macro_f1": base["macro_f1"]["f1"],
    }


def aggregate(runs: list[dict]) -> dict:
    def mean_std(values: list[float]) -> tuple[float, float]:
        return statistics.mean(values), statistics.stdev(values) if len(values) > 1 else 0.0

    per_class = {}
    for cls in CLASSES:
        p = mean_std([r["tool"][cls]["precision"] for r in runs])
        rec = mean_std([r["tool"][cls]["recall"] for r in runs])
        f1 = mean_std([r["tool"][cls]["f1"] for r in runs])
        support = sum(r["tool"][cls]["support"] for r in runs)
        per_class[cls] = {
            "precision": p, "recall": rec, "f1": f1, "support_total": support
        }
    macro = mean_std([r["macro_f1"] for r in runs])
    base = mean_std([r["baseline_macro_f1"] for r in runs])
    return {"per_class": per_class, "macro_f1": macro, "baseline_macro_f1": base}


def render_markdown(runs: list[dict], agg: dict, noise_rate: float) -> str:
    def fmt(pair: tuple[float, float]) -> str:
        mean, std = pair
        return f"{mean:.3f} ± {std:.3f}"

    out = [
        "# 归因评测报告",
        "",
        f"- 随机种子：{len(runs)} 组（seed 0–{len(runs) - 1}）",
        f"- 每组样本：{runs[0]['items']} 条",
        f"- 未知原因噪声比例：{noise_rate:.0%}",
        f"- 参与评测样本：平均 {statistics.mean(r['labeled_items'] for r in runs):.0f} 条/组",
        "",
        "## 归因准确率（工具 vs 真值）",
        "",
        "| 类别 | 支持数合计 | Precision | Recall | F1 |",
        "|---|---|---|---|---|",
    ]
    for cls in CLASSES:
        m = agg["per_class"][cls]
        out.append(
            f"| {cls} | {m['support_total']} | {fmt(m['precision'])} | "
            f"{fmt(m['recall'])} | {fmt(m['f1'])} |"
        )
    out += [
        "",
        f"**Macro-F1：{fmt(agg['macro_f1'])}**",
        f"基线（只按有无多数派）：{fmt(agg['baseline_macro_f1'])}",
        "",
        "## 混淆矩阵（合并所有种子）",
        "",
    ]
    merged = {t: {p: 0 for p in CLASSES} for t in CLASSES}
    for run in runs:
        for t in CLASSES:
            for p in CLASSES:
                merged[t][p] += run["confusion"][t][p]
    out.append("| 真值 ＼ 预测 | " + " | ".join(CLASSES) + " |")
    out.append("|" + "---|" * (len(CLASSES) + 1))
    for t in CLASSES:
        out.append(f"| {t} | " + " | ".join(str(merged[t][p]) for p in CLASSES) + " |")

    out += [
        "",
        "## 说明",
        "",
        "- 「无争议」也参与计算：工具把一致样本误报成争议，会拉低这一类的 precision。",
        "- 真值来自生成器的注入原因，不是人工标注；它验证的是规则实现是否符合设计。",
        "- 未知原因的噪声争议不参与准确率，数量见下方 JSON 明细。",
        "",
    ]
    return "\n".join(out)


def main() -> int:
    parser = argparse.ArgumentParser(description="归因准确率评测")
    parser.add_argument("--seeds", type=int, default=20)
    parser.add_argument("--items", type=int, default=300)
    parser.add_argument("--noise", type=float, default=0.0)
    parser.add_argument("--min-macro-f1", type=float, default=0.9)
    parser.add_argument("--out", default=str(ROOT / "eval" / "report.md"),
                        help="Markdown 输出路径")
    parser.add_argument("--json-out", default=None,
                        help="JSON 输出路径；默认与 --out 同名")
    args = parser.parse_args()

    runs = [evaluate_seed(seed, args.items, args.noise) for seed in range(args.seeds)]
    agg = aggregate(runs)
    md = render_markdown(runs, agg, args.noise)

    print(md)
    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(md, encoding="utf-8")

    json_path = Path(args.json_out) if args.json_out else out_path.with_suffix(".json")
    json_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(
        json.dumps({"aggregate": agg, "runs": runs}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"\n[已写入] {out_path} / {json_path}")

    macro = agg["macro_f1"][0]
    if macro < args.min_macro_f1:
        print(f"\n[FAIL] macro-F1 {macro:.3f} < {args.min_macro_f1:.3f}")
        return 1
    print(f"\n[PASS] macro-F1 {macro:.3f} >= {args.min_macro_f1:.3f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
