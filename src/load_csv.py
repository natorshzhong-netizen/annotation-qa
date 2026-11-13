# -*- coding: utf-8 -*-
"""从 CSV 读标注结果，让别人的数据也能跑。

CSV 格式（一行 = 一个人对一条样本的标注）：

    id,text,annotator,label
    T01,我买的鞋尺码不对想退掉,a,退款退货
    T01,我买的鞋尺码不对想退掉,b,退款退货
    T01,我买的鞋尺码不对想退掉,c,商品咨询

同一 id 的 text 重复出现是正常的（为了好导出）。
"""

import csv
from pathlib import Path


def load_from_csv(path, allow_missing: bool = False) -> tuple[dict[str, str], dict[str, dict[str, str]]]:
    """返回 (items, anns)，和 load.py 里的结构一致。

    allow_missing=True 时允许标注者漏标（真实众包数据常见）；
    每条样本仍然至少要有 2 个人标过。
    """
    path = Path(path)
    items: dict[str, str] = {}
    anns: dict[str, dict[str, str]] = {}

    with open(path, encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        required = {"id", "text", "annotator", "label"}
        if not required.issubset(set(reader.fieldnames or [])):
            raise ValueError(
                f"CSV 表头必须包含 {sorted(required)}，实际是 {reader.fieldnames}"
            )

        for n, row in enumerate(reader, start=2):
            iid = (row["id"] or "").strip()
            text = (row["text"] or "").strip()
            who = (row["annotator"] or "").strip()
            label = (row["label"] or "").strip()

            if not (iid and who and label):
                raise ValueError(f"第 {n} 行有空值：{row}")

            # 同一条样本的文本必须一致，否则说明数据出错
            if iid in items and items[iid] != text:
                raise ValueError(f"第 {n} 行：{iid} 的文本和前面不一致")

            items[iid] = text
            target = anns.setdefault(who, {})
            if iid in target:
                raise ValueError(f"第 {n} 行：标注者 {who} 对 {iid} 重复标注")
            target[iid] = label

    if not items:
        raise ValueError("CSV 里没有数据")
    if len(anns) < 2:
        raise ValueError("至少需要 2 个标注者才能算一致性")

    ids = set(items)
    if not allow_missing:
        for who, a in anns.items():
            if set(a) != ids:
                missing = sorted(ids - set(a))[:5]
                raise ValueError(
                    f"标注者 {who} 漏标了 {len(ids - set(a))} 条，例如 {missing}。"
                    "真实漏标数据请传 allow_missing=True。"
                )

    thin = [i for i in sorted(ids) if sum(i in a for a in anns.values()) < 2]
    if thin:
        raise ValueError(f"{len(thin)} 条样本不足 2 个标注：{thin[:5]}")

    return items, anns


def labels_of(anns: dict[str, dict[str, str]]) -> list[str]:
    """从数据里收集出现过的标签。"""
    return sorted({lab for a in anns.values() for lab in a.values()})
