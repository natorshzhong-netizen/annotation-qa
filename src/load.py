# -*- coding: utf-8 -*-
"""数据读取与校验。

支持两种数据：三份对齐的 JSONL（ann_*.jsonl），或允许漏标的稀疏数据。
校验会拦住重复 id、未定义标签、不存在的样本，以及不足 2 人标注的条目。
"""
import json
from pathlib import Path


def _read_jsonl(path: Path, key: str | None = None) -> list[dict]:
    rows = []
    seen: set[str] = set()
    with open(path, encoding="utf-8") as f:
        for n, line in enumerate(f, start=1):
            line = line.strip()
            if not line:
                continue
            row = json.loads(line)
            if key is not None:
                value = str(row.get(key, ""))
                if value in seen:
                    raise ValueError(f"{path.name} 第 {n} 行：{key} 重复（{value}）")
                seen.add(value)
            rows.append(row)
    return rows


def load_items(data_dir) -> dict[str, str]:
    """返回 {样本id: 文本}"""
    rows = _read_jsonl(Path(data_dir) / "items.jsonl", key="id")
    return {r["id"]: r["text"] for r in rows}


def load_labels(data_dir) -> list[str]:
    """返回类别列表（顺序和 labels.json 一致）"""
    with open(Path(data_dir) / "labels.json", encoding="utf-8") as f:
        return json.load(f)["labels"]


def load_annotations(data_dir) -> dict[str, dict[str, str]]:
    """返回 {标注者名: {样本id: 标签}}

    文件名 ann_a.jsonl / ann_b.jsonl / ann_c.jsonl，
    标注者名取文件名里的 a / b / c。同一文件里 id 重复会直接报错，
    避免后一行悄悄覆盖前一行。
    """
    anns = {}
    for p in sorted(Path(data_dir).glob("ann_*.jsonl")):
        name = p.stem.replace("ann_", "")
        if name in anns:
            raise ValueError(f"标注者名重复：{name}（检查 ann_*.jsonl 文件名）")
        anns[name] = {r["id"]: r["label"] for r in _read_jsonl(p, key="id")}
    return anns


def load_all(data_dir, allow_missing: bool = False):
    """读完整数据集；allow_missing=True 时允许标注者漏标。"""
    items = load_items(data_dir)
    labels = load_labels(data_dir)
    anns = load_annotations(data_dir)
    validate(items, labels, anns, allow_missing=allow_missing)
    return items, labels, anns


def validate(items: dict, labels: list[str], anns: dict,
             allow_missing: bool = False):
    """校验数据完整性、标签合法性，以及每条样本是否有足够的人标过。"""
    if not anns:
        raise ValueError("没找到任何标注文件（ann_*.jsonl）")
    if not items:
        raise ValueError("items.jsonl 为空，没有可分析的样本")
    if len(anns) < 2:
        raise ValueError("至少需要 2 个标注者才能算一致性")

    ids = set(items)
    for name, a in anns.items():
        missing = ids - set(a)
        extra = set(a) - ids
        if missing and not allow_missing:
            raise ValueError(
                f"标注者 {name} 缺 {len(missing)} 条：{sorted(missing)[:5]}。"
                "如果是真实的漏标数据，请用 allow_missing=True（CLI 加 --allow-missing）。"
            )
        if extra:
            raise ValueError(f"标注者 {name} 多了不存在的样本：{sorted(extra)[:5]}")
        bad = {v for v in a.values() if v not in labels}
        if bad:
            raise ValueError(f"标注者 {name} 用了未定义的标签：{sorted(bad)}")

    # 无论是否允许漏标，一条样本至少要有 2 个人标过，否则一致性无从谈起
    thin = [i for i in sorted(ids) if sum(i in a for a in anns.values()) < 2]
    if thin:
        raise ValueError(
            f"{len(thin)} 条样本不足 2 个标注：{thin[:5]}。"
            "请检查数据或用 prepare 脚本过滤。"
        )
