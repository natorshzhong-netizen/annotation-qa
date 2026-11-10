# -*- coding: utf-8 -*-
"""数据读取与校验。

这个模块已经写好了，不用改。你只需要用它的返回值。
"""
import json
from pathlib import Path


def _read_jsonl(path: Path) -> list[dict]:
    rows = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def load_items(data_dir) -> dict[str, str]:
    """返回 {样本id: 文本}"""
    rows = _read_jsonl(Path(data_dir) / "items.jsonl")
    return {r["id"]: r["text"] for r in rows}


def load_labels(data_dir) -> list[str]:
    """返回类别列表（顺序和 labels.json 一致）"""
    with open(Path(data_dir) / "labels.json", encoding="utf-8") as f:
        return json.load(f)["labels"]


def load_annotations(data_dir) -> dict[str, dict[str, str]]:
    """返回 {标注者名: {样本id: 标签}}

    文件名 ann_a.jsonl / ann_b.jsonl / ann_c.jsonl，
    标注者名取文件名里的 a / b / c。
    """
    anns = {}
    for p in sorted(Path(data_dir).glob("ann_*.jsonl")):
        name = p.stem.replace("ann_", "")
        anns[name] = {r["id"]: r["label"] for r in _read_jsonl(p)}
    return anns


def load_all(data_dir):
    items = load_items(data_dir)
    labels = load_labels(data_dir)
    anns = load_annotations(data_dir)
    validate(items, labels, anns)
    return items, labels, anns


def validate(items: dict, labels: list[str], anns: dict):
    """保证三份标注覆盖同样的样本、且标签都在类别表里。"""
    if not anns:
        raise ValueError("没找到任何标注文件（ann_*.jsonl）")
    ids = set(items)
    for name, a in anns.items():
        missing = ids - set(a)
        extra = set(a) - ids
        if missing:
            raise ValueError(f"标注者 {name} 缺 {len(missing)} 条：{sorted(missing)[:5]}")
        if extra:
            raise ValueError(f"标注者 {name} 多了不存在的样本：{sorted(extra)[:5]}")
        bad = {v for v in a.values() if v not in labels}
        if bad:
            raise ValueError(f"标注者 {name} 用了未定义的标签：{sorted(bad)}")
