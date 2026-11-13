# -*- coding: utf-8 -*-
"""把各数据集的评测结果汇总成 JSON，供仪表盘和 README 使用。"""

from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from src import classify, metrics  # noqa: E402
from src.load import load_all  # noqa: E402

DATASETS = {
    "go_emotions": {"path": "benchmarks/data_full/go_emotions", "allow_missing": True},
    "hatexplain": {"path": "benchmarks/data_full/hatexplain", "allow_missing": True},
    "chaosnli": {"path": "benchmarks/data_full/chaosnli", "allow_missing": False},
}


def summarize(name: str, path: Path, allow_missing: bool) -> dict:
    items, labels, anns = load_all(path, allow_missing=allow_missing)
    ids = sorted(items)
    complete = metrics.is_complete(anns, ids)

    if complete:
        value = metrics.fleiss_kappa(anns, labels, ids)
        lo, hi = metrics.bootstrap_kappa(anns, labels, ids, n_boot=200)
        metric = "Fleiss' kappa"
    else:
        value = metrics.krippendorff_alpha(anns, labels, ids)
        lo, hi = metrics.bootstrap_alpha(anns, labels, ids, n_boot=200)
        metric = "Krippendorff's α"

    classified = classify.classify_disputes(anns, ids, labels=labels)
    counts = Counter(d["category"] for d in classified)
    profile = classify.minority_profile(anns, ids)
    details = classify.systematic_details(profile, labels=labels)
    flagged = sorted(
        [row for row in details if row["systematic"]],
        key=lambda row: (-row["count"], row["name"]),
    )

    meta = json.loads((path / "meta.json").read_text(encoding="utf-8")) if (path / "meta.json").exists() else {}
    return {
        "name": name,
        "dataset": meta.get("dataset", name),
        "source": meta.get("source", ""),
        "license": meta.get("license", ""),
        "items": len(items),
        "annotators": len(anns),
        "annotations": sum(len(a) for a in anns.values()),
        "labels": len(labels),
        "identity_tracking": meta.get("identity_tracking", True),
        "metric": metric,
        "agreement": round(value, 4),
        "ci": [round(lo, 4), round(hi, 4)],
        "disputes": len(classified),
        "dispute_counts": {
            "规范未覆盖": counts.get("规范未覆盖", 0),
            "系统性偏差": counts.get("系统性偏差", 0),
            "个别错误": counts.get("个别错误", 0),
        },
        "flagged_annotators": [
            {
                "name": row["name"],
                "label": row["label"],
                "count": row["count"],
                "opportunities": row["opportunities"],
                "dominance": round(row["dominance"], 3),
                "q_value": row["q_value"],
            }
            for row in flagged[:10]
        ],
        "flagged_total": len(flagged),
    }


def main() -> None:
    missing = [
        name for name, config in DATASETS.items()
        if not (ROOT / config["path"]).exists()
    ]
    if missing:
        raise SystemExit(
            "缺少数据集目录："
            + ", ".join(missing)
            + "。先运行 benchmarks/prepare.py --limit 10000 --out-root benchmarks/data_full"
        )

    results = []
    for name, config in DATASETS.items():
        path = ROOT / config["path"]
        print(f"[summarize] {name}")
        results.append(summarize(name, path, config["allow_missing"]))

    out = ROOT / "benchmarks" / "results.json"
    out.write_text(
        json.dumps(results, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"[written] {out}")


if __name__ == "__main__":
    main()
