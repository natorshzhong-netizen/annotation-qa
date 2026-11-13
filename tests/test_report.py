# -*- coding: utf-8 -*-
"""报告生成的冒烟与稀疏数据测试。"""

from __future__ import annotations

from eval.generate import generate
from src.report import build_report


def test_complete_report_uses_fleiss():
    items, labels, anns, _ = generate(n_items=100, seed=1)
    md = build_report(items, labels, anns)
    assert "Fleiss' kappa" in md
    assert "两两一致性" in md
    assert "分歧原因分析" in md
    assert "本周行动" in md


def test_sparse_report_uses_krippendorff_and_coverage():
    items, labels, anns, _ = generate(n_items=100, seed=2)
    # 每个标注者删掉 5 条，但仍然保证每条样本至少 2 人
    for name in sorted(anns):
        for iid in sorted(anns[name])[:5]:
            del anns[name][iid]
    md = build_report(items, labels, anns)
    assert "Krippendorff's alpha" in md
    assert "标注覆盖" in md
    assert "| Fleiss' kappa" not in md


def test_all_agree_does_not_crash():
    items = {"1": "x", "2": "y"}
    labels = ["A"]
    anns = {"a": {"1": "A", "2": "A"}, "b": {"1": "A", "2": "A"}}
    md = build_report(items, labels, anns)
    assert "无需处理" in md
    assert "没有需要处理的项" in md
