# -*- coding: utf-8 -*-
"""把公开多标注者数据集转换成 annotation-qa 的数据目录格式。

原始文件放在 benchmarks/raw/，转换结果放到 benchmarks/data/<name>/。
原始文件不提交（体积大、许可证各不相同），转换脚本和抽样后的样本提交。

用法
    python benchmarks/prepare.py --dataset all
    python benchmarks/prepare.py --dataset go_emotions --limit 1000
"""

from __future__ import annotations

import argparse
import json
import random
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "benchmarks" / "raw"
DATA = ROOT / "benchmarks" / "data"

GO_EMOTIONS_RAW = RAW / "go_emotions" / "train.parquet"
HATEXPLAIN_RAW = RAW / "hatexplain" / "dataset.json"
CHAOSNLI_RAW = RAW / "chaosnli" / "train.parquet"

META_FIELDS = {
    "go_emotions",
    "hatexplain",
    "chaosnli",
    "entailment",
    "neutral",
    "contradiction",
}


def _write(out: Path, items: dict[str, str], labels: list[str],
           anns: dict[str, dict[str, str]], meta: dict) -> None:
    out.mkdir(parents=True, exist_ok=True)
    with open(out / "items.jsonl", "w", encoding="utf-8", newline="\n") as f:
        for iid in sorted(items):
            f.write(json.dumps({"id": iid, "text": items[iid]}, ensure_ascii=False) + "\n")

    (out / "labels.json").write_text(
        json.dumps({"labels": labels}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    for name in sorted(anns):
        with open(out / f"ann_{name}.jsonl", "w", encoding="utf-8", newline="\n") as f:
            for iid in sorted(anns[name]):
                f.write(
                    json.dumps({"id": iid, "label": anns[name][iid]}, ensure_ascii=False) + "\n"
                )

    counts = Counter({name: len(v) for name, v in anns.items()})
    meta = {
        **meta,
        "items": len(items),
        "annotators": len(anns),
        "annotations": sum(counts.values()),
        "annotations_per_item": round(sum(counts.values()) / max(1, len(items)), 2),
        "annotator_annotation_counts": {
            "min": min(counts.values()) if counts else 0,
            "median": sorted(counts.values())[len(counts) // 2] if counts else 0,
            "max": max(counts.values()) if counts else 0,
        },
    }
    (out / "meta.json").write_text(
        json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(f"[{out.name}] {len(items)} items, {len(anns)} annotators, "
          f"{sum(counts.values())} annotations")


def _sample(ids: list[str], limit: int | None, seed: int) -> set[str]:
    ids = sorted(ids)
    if limit is None or limit >= len(ids):
        return set(ids)
    return set(random.Random(seed).sample(ids, limit))


def prepare_go_emotions(out: Path, limit: int | None, min_annotations: int, seed: int) -> None:
    import pyarrow.parquet as pq

    table = pq.read_table(GO_EMOTIONS_RAW).to_pydict()
    emotions = [
        k for k in table
        if k not in {
            "text", "id", "author", "subreddit", "link_id", "parent_id",
            "created_utc", "rater_id", "example_very_unclear",
        }
    ]

    rows: dict[str, list[tuple[int, str, str]]] = defaultdict(list)
    skipped_multi = 0
    for n in range(len(table["text"])):
        if table["example_very_unclear"][n]:
            continue
        positive = [e for e in emotions if table[e][n] == 1]
        if len(positive) != 1:
            skipped_multi += 1
            continue
        rows[table["id"][n]].append((table["rater_id"][n], positive[0], table["text"][n]))

    annotator_counts = Counter()
    for values in rows.values():
        annotator_counts.update(r[0] for r in values)
    kept = {r for r, c in annotator_counts.items() if c >= min_annotations}

    candidates = [
        iid for iid, values in rows.items()
        if sum(r[0] in kept for r in values) >= 2
    ]
    chosen = _sample(candidates, limit, seed)

    items: dict[str, str] = {}
    anns: dict[str, dict[str, str]] = defaultdict(dict)
    for iid in chosen:
        values = [r for r in rows[iid] if r[0] in kept]
        items[iid] = values[0][2]
        for rater, label, _text in values:
            anns[f"r{rater}"][iid] = label

    labels = sorted({label for a in anns.values() for label in a.values()})
    _write(out, items, labels, dict(anns), {
        "dataset": "GoEmotions (raw, single-label subset)",
        "source": "https://huggingface.co/datasets/google-research-datasets/go_emotions",
        "license": "Apache-2.0",
        "citation": "Demszky et al., 2020, arXiv:2005.00547",
        "conversion": (
            "只保留恰好一个情绪标签为 1 的评分（多标签与全 0 丢弃）；"
            f"丢弃多标签/空标签行 {skipped_multi} 条；"
            f"保留标注数 >= {min_annotations} 的标注者；"
            "每条样本至少 2 个评分。"
        ),
        "labels_origin": "28 个 Reddit 情绪类别（含 neutral）",
        "identity_tracking": True,
        "note": "标注者 ID 来自原始 rater_id，跨样本保持一致。",
    })


def prepare_hatexplain(out: Path, limit: int | None, min_annotations: int, seed: int) -> None:
    raw = json.loads(HATEXPLAIN_RAW.read_text(encoding="utf-8"))

    annotator_counts = Counter()
    for post in raw.values():
        annotator_counts.update(a["annotator_id"] for a in post["annotators"])
    kept = {r for r, c in annotator_counts.items() if c >= min_annotations}

    candidates = [
        pid for pid, post in raw.items()
        if sum(a["annotator_id"] in kept for a in post["annotators"]) >= 2
    ]
    chosen = _sample(candidates, limit, seed)

    items: dict[str, str] = {}
    anns: dict[str, dict[str, str]] = defaultdict(dict)
    for pid in chosen:
        post = raw[pid]
        items[pid] = " ".join(post["post_tokens"])
        for a in post["annotators"]:
            if a["annotator_id"] in kept:
                anns[f"a{a['annotator_id']}"][pid] = a["label"]

    labels = sorted({label for a in anns.values() for label in a.values()})
    _write(out, items, labels, dict(anns), {
        "dataset": "HateXplain",
        "source": "https://github.com/hate-alert/HateXplain",
        "license": "MIT",
        "citation": "Mathew et al., 2020, arXiv:2012.10289",
        "conversion": (
            f"每条帖子取 3 位标注者的标签；保留标注数 >= {min_annotations} 的标注者；"
            "每条帖子至少保留 2 位标注者。"
        ),
        "labels_origin": "normal / offensive / hatespeech",
        "identity_tracking": True,
        "note": "标注者 ID 来自原始 annotator_id，跨帖子保持一致。",
    })


def prepare_chaosnli(out: Path, limit: int | None, slots: int, seed: int) -> None:
    import pyarrow.parquet as pq

    table = pq.read_table(CHAOSNLI_RAW).to_pylist()
    rng = random.Random(seed)
    ids = _sample([row["uid"] for row in table], limit, seed)
    order = ["entailment", "neutral", "contradiction"]

    items: dict[str, str] = {}
    anns: dict[str, dict[str, str]] = defaultdict(dict)
    for row in table:
        if row["uid"] not in ids:
            continue
        items[row["uid"]] = f"{row['premise']} [SEP] {row['hypothesis']}"
        pool = []
        for label, count in zip(order, row["label_count"]):
            pool.extend([label] * int(count))
        for n, label in enumerate(rng.sample(pool, min(slots, len(pool))), start=1):
            anns[f"s{n}"][row["uid"]] = label

    labels = sorted({label for a in anns.values() for label in a.values()})
    _write(out, items, labels, dict(anns), {
        "dataset": "ChaosNLI (MNLI portion, 5-slot subsample)",
        "source": "https://huggingface.co/datasets/tasksource/chaos-mnli-ambiguity",
        "upstream": "https://github.com/easonnie/ChaosNLI",
        "license": "CC BY-NC 4.0",
        "citation": "Nie et al., 2020, arXiv:2010.03532",
        "conversion": (
            "原始每条有 100 位标注者的标签分布；这里每条随机抽 "
            f"{slots} 个标签，作为 {slots} 个标注槽。"
        ),
        "labels_origin": "entailment / neutral / contradiction",
        "identity_tracking": False,
        "note": (
            "槽位 s1..sN 不是固定的真人，跨样本没有身份连续性。"
            "因此这组数据只用于一致性指标，不用于「谁有系统性偏差」的归因。"
        ),
    })


def main() -> None:
    parser = argparse.ArgumentParser(description="公开数据集转换")
    parser.add_argument("--dataset", default="all",
                        choices=["all", "go_emotions", "hatexplain", "chaosnli"])
    parser.add_argument("--limit", type=int, default=None,
                        help="每个数据集最多保留多少条；0 表示不限制")
    parser.add_argument("--min-annotations", type=int, default=20,
                        help="标注者至少标注多少条才保留（GoEmotions/HateXplain）")
    parser.add_argument("--slots", type=int, default=5, help="ChaosNLI 每条抽几个槽")
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--out-root", default=str(DATA), help="输出根目录")
    args = parser.parse_args()

    limit = None if args.limit in (None, 0) else args.limit
    out_root = Path(args.out_root)

    if args.dataset in ("all", "go_emotions"):
        prepare_go_emotions(out_root / "go_emotions", limit, args.min_annotations, args.seed)
    if args.dataset in ("all", "hatexplain"):
        prepare_hatexplain(out_root / "hatexplain", limit, args.min_annotations, args.seed)
    if args.dataset in ("all", "chaosnli"):
        prepare_chaosnli(out_root / "chaosnli", limit, args.slots, args.seed)


if __name__ == "__main__":
    main()
