# -*- coding: utf-8 -*-
"""数据读取与校验测试。"""

from __future__ import annotations

import json

import pytest

from src.load import load_all
from src.load_csv import load_from_csv


def _write_dataset(root, missing: bool = False):
    items = {"1": "a", "2": "b", "3": "c"}
    with open(root / "items.jsonl", "w", encoding="utf-8") as f:
        for iid, text in items.items():
            f.write(json.dumps({"id": iid, "text": text}) + "\n")

    (root / "labels.json").write_text(json.dumps({"labels": ["A", "B"]}), encoding="utf-8")

    votes = {
        "a": {"1": "A", "2": "A", "3": "B"},
        "b": {"1": "A", "2": "B", "3": "B"},
        "c": {"1": "A", "2": "A", "3": "B"},
    }
    if missing:
        del votes["c"]["3"]
    for name, rows in votes.items():
        with open(root / f"ann_{name}.jsonl", "w", encoding="utf-8") as f:
            for iid, label in rows.items():
                f.write(json.dumps({"id": iid, "label": label}) + "\n")


def test_strict_rejects_missing(tmp_path):
    _write_dataset(tmp_path, missing=True)
    with pytest.raises(ValueError, match="缺"):
        load_all(tmp_path)


def test_allow_missing_loads(tmp_path):
    _write_dataset(tmp_path, missing=True)
    items, labels, anns = load_all(tmp_path, allow_missing=True)
    assert len(items) == 3
    assert labels == ["A", "B"]
    assert "3" not in anns["c"]


def test_empty_items_rejected(tmp_path):
    (tmp_path / "items.jsonl").write_text("", encoding="utf-8")
    (tmp_path / "labels.json").write_text('{"labels": ["A"]}', encoding="utf-8")
    for name in ("a", "b"):
        (tmp_path / f"ann_{name}.jsonl").write_text(
            '{"id": "1", "label": "A"}\n', encoding="utf-8"
        )
    with pytest.raises(ValueError, match="为空"):
        load_all(tmp_path, allow_missing=True)


def test_duplicate_annotation_id_rejected(tmp_path):
    _write_dataset(tmp_path)
    with open(tmp_path / "ann_a.jsonl", "a", encoding="utf-8") as f:
        f.write(json.dumps({"id": "1", "label": "B"}) + "\n")
    with pytest.raises(ValueError, match="重复"):
        load_all(tmp_path)


def test_item_with_one_annotation_rejected(tmp_path):
    _write_dataset(tmp_path, missing=True)
    # 再删掉 b 的 3，让 3 号样本只剩 a 一个人
    lines = (tmp_path / "ann_b.jsonl").read_text(encoding="utf-8").splitlines()
    (tmp_path / "ann_b.jsonl").write_text("\n".join(lines[:2]) + "\n", encoding="utf-8")
    with pytest.raises(ValueError, match="不足 2 个标注"):
        load_all(tmp_path, allow_missing=True)


def test_csv_strict_and_missing(tmp_path):
    path = tmp_path / "sample.csv"
    path.write_text(
        "id,text,annotator,label\n"
        "1,a,a,A\n1,a,b,A\n1,a,c,A\n"
        "2,b,a,B\n2,b,b,B\n",
        encoding="utf-8",
    )
    with pytest.raises(ValueError, match="漏标"):
        load_from_csv(path)

    items, anns = load_from_csv(path, allow_missing=True)
    assert items == {"1": "a", "2": "b"}
    assert "2" not in anns["c"]


def test_csv_duplicate_row_rejected(tmp_path):
    path = tmp_path / "sample.csv"
    path.write_text(
        "id,text,annotator,label\n"
        "1,a,a,A\n1,a,a,B\n1,a,b,A\n",
        encoding="utf-8",
    )
    with pytest.raises(ValueError, match="重复标注"):
        load_from_csv(path)
