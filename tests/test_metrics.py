# -*- coding: utf-8 -*-
"""指标函数的数值对拍与边界测试。"""

from __future__ import annotations

import random

import pytest

from src import metrics

LABELS = ["A", "B", "C"]


def _random_complete(seed: int, n_items: int = 40, n_anns: int = 3):
    rng = random.Random(seed)
    ids = [f"i{n}" for n in range(n_items)]
    anns = {
        f"x{k}": {i: rng.choice(LABELS) for i in ids}
        for k in range(n_anns)
    }
    return ids, anns


def test_pairwise_perfect_and_none():
    a = {"1": "A", "2": "B", "3": "C"}
    assert metrics.pairwise_agreement(a, a, ["1", "2", "3"]) == 1.0
    assert metrics.cohen_kappa(a, a, LABELS, ["1", "2", "3"]) == 1.0
    assert metrics.pairwise_agreement({"1": "A"}, {"2": "B"}, None) == 0.0
    assert metrics.cohen_kappa({"1": "A"}, {"2": "B"}, LABELS, None) == 0.0


def test_pairwise_uses_common_items_when_sparse():
    a = {"1": "A", "2": "B", "3": "A"}
    b = {"2": "B", "3": "B", "4": "C"}
    assert metrics.co_rated_ids(a, b) == ["2", "3"]
    assert metrics.pairwise_agreement(a, b, None) == 0.5


def test_cohen_matches_sklearn():
    sklearn_metrics = pytest.importorskip("sklearn.metrics")
    for seed in range(20):
        ids, anns = _random_complete(seed)
        a = [anns["x0"][i] for i in ids]
        b = [anns["x1"][i] for i in ids]
        expected = sklearn_metrics.cohen_kappa_score(a, b, labels=LABELS)
        got = metrics.cohen_kappa(anns["x0"], anns["x1"], LABELS, ids)
        assert got == pytest.approx(expected, abs=1e-9)


def test_fleiss_matches_statsmodels():
    inter_rater = pytest.importorskip("statsmodels.stats.inter_rater")
    for seed in range(10):
        ids, anns = _random_complete(seed, n_items=30, n_anns=4)
        ratings = [[anns[x][i] for x in sorted(anns)] for i in ids]
        table, _ = inter_rater.aggregate_raters(ratings)
        expected = inter_rater.fleiss_kappa(table, method="fleiss")
        got = metrics.fleiss_kappa(anns, LABELS, ids)
        assert got == pytest.approx(expected, abs=1e-9)


def test_fleiss_known_value():
    """4 条样本、3 个标注者、2 个类别，手算 kappa = 1/3。"""
    ids = ["1", "2", "3", "4"]
    anns = {
        "a": {"1": "A", "2": "A", "3": "A", "4": "B"},
        "b": {"1": "A", "2": "A", "3": "B", "4": "B"},
        "c": {"1": "A", "2": "B", "3": "B", "4": "B"},
    }
    assert metrics.fleiss_kappa(anns, ["A", "B"], ids) == pytest.approx(1 / 3, abs=1e-12)


def test_fleiss_rejects_missing():
    ids = ["1", "2", "3"]
    anns = {"a": {"1": "A", "2": "A", "3": "B"}, "b": {"2": "A", "3": "B"}}
    with pytest.raises(ValueError, match="缺失"):
        metrics.fleiss_kappa(anns, LABELS, ids)


def test_krippendorff_perfect_and_single_label():
    ids = ["1", "2", "3"]
    anns = {"a": {"1": "A", "2": "A", "3": "B"}, "b": {"1": "A", "2": "A", "3": "B"}}
    assert metrics.krippendorff_alpha(anns, LABELS, ids) == pytest.approx(1.0)

    same = {"a": {i: "A" for i in ids}, "b": {i: "A" for i in ids}}
    assert metrics.krippendorff_alpha(same, LABELS, ids) == pytest.approx(1.0)


def test_krippendorff_matches_reference_with_missing():
    krippendorff = pytest.importorskip("krippendorff")
    np = pytest.importorskip("numpy")

    # 4 个标注者 × 8 条样本，故意留 3 个缺失
    ids = [str(n) for n in range(8)]
    anns = {
        "a": {i: "A" for i in ids},
        "b": {"0": "A", "1": "B", "2": "A", "3": "B", "4": "A", "5": "B", "6": "A", "7": "B"},
        "c": {"0": "A", "1": "A", "2": "B", "3": "B", "4": "A", "5": "A", "6": "B", "7": "B"},
        "d": {"0": "A", "1": "A", "2": "B", "3": "A", "4": "B", "5": "A", "6": "B", "7": "A"},
    }
    names = sorted(anns)
    matrix = np.full((len(names), len(ids)), np.nan)
    for r, name in enumerate(names):
        for c, iid in enumerate(ids):
            if iid in anns[name]:
                matrix[r, c] = LABELS.index(anns[name][iid])

    expected = krippendorff.alpha(
        reliability_data=matrix, level_of_measurement="nominal", value_domain=[0, 1, 2]
    )
    got = metrics.krippendorff_alpha(anns, LABELS, ids)
    assert got == pytest.approx(expected, abs=1e-9)


def test_krippendorff_random_matches_reference():
    krippendorff = pytest.importorskip("krippendorff")
    np = pytest.importorskip("numpy")
    for seed in range(10):
        ids, anns = _random_complete(seed, n_items=25, n_anns=4)
        names = sorted(anns)
        matrix = np.array([
            [LABELS.index(anns[name][i]) for i in ids]
            for name in names
        ], dtype=float)
        expected = krippendorff.alpha(
            reliability_data=matrix, level_of_measurement="nominal", value_domain=[0, 1, 2]
        )
        got = metrics.krippendorff_alpha(anns, LABELS, ids)
        assert got == pytest.approx(expected, abs=1e-9)


def test_bootstrap_is_deterministic_and_brackets_point_estimate():
    ids, anns = _random_complete(0, n_items=60, n_anns=3)
    lo1, hi1 = metrics.bootstrap_alpha(anns, LABELS, ids, n_boot=200, seed=7)
    lo2, hi2 = metrics.bootstrap_alpha(anns, LABELS, ids, n_boot=200, seed=7)
    assert (lo1, hi1) == (lo2, hi2)
    assert lo1 <= hi1
    assert -1.0 <= lo1 <= 1.0 and -1.0 <= hi1 <= 1.0


def test_disputed_items_sparse_no_keyerror():
    anns = {"a": {"1": "A", "2": "A"}, "b": {"1": "B"}, "c": {"2": "A"}}
    out = metrics.disputed_items(anns, ["1", "2"])
    assert [d["id"] for d in out] == ["1"]
    assert out[0]["votes"] == {"a": "A", "b": "B"}
