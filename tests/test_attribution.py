# -*- coding: utf-8 -*-
"""归因规则的单元测试 + 合成真值回归。"""

from __future__ import annotations

from eval.generate import generate
from eval.run_attribution_eval import evaluate_seed
from src import classify


def test_no_majority_is_spec_gap():
    anns = {
        "a": {"1": "A"},
        "b": {"1": "B"},
        "c": {"1": "C"},
    }
    result = classify.classify_disputes(anns, ["1"])
    assert result[0]["category"] == "规范未覆盖"


def test_concentrated_minority_is_systematic():
    anns = {
        "a": {"1": "A", "2": "A", "3": "A", "4": "B"},
        "b": {"1": "C", "2": "C", "3": "C", "4": "B"},
        "c": {"1": "A", "2": "A", "3": "A", "4": "B"},
    }
    profile = classify.minority_profile(anns, ["1", "2", "3", "4"])
    assert profile["b"]["count"] == 3
    assert classify.find_systematic(profile, labels=["A", "B", "C"]) == {"b": "C"}
    result = classify.classify_disputes(anns, ["1", "2", "3", "4"], labels=["A", "B", "C"])
    assert all(d["category"] == "系统性偏差" for d in result)


def test_dispersed_minority_is_random_error():
    anns = {
        "a": {"1": "A", "2": "A", "3": "A", "4": "A", "5": "A", "6": "A"},
        "b": {"1": "B", "2": "C", "3": "B", "4": "C", "5": "B", "6": "C"},
        "c": {"1": "A", "2": "A", "3": "A", "4": "A", "5": "A", "6": "A"},
    }
    profile = classify.minority_profile(anns, ["1", "2", "3", "4", "5", "6"])
    assert classify.find_systematic(profile) == {}
    result = classify.classify_disputes(anns, ["1", "2", "3", "4", "5", "6"])
    assert all(d["category"] == "个别错误" for d in result)


def test_sparse_data_does_not_crash():
    anns = {
        "a": {"1": "A", "2": "A", "3": "A"},
        "b": {"1": "B", "2": "A"},
        "c": {"1": "A", "2": "C"},
    }
    result = classify.classify_disputes(anns, ["1", "2", "3"])
    by_id = {d["id"]: d["category"] for d in result}
    assert by_id["1"] == "个别错误"
    assert by_id["2"] == "个别错误"
    assert "3" not in by_id      # 只有 1 个人标过，不构成分歧


def test_synthetic_clean_scenario_is_recovered():
    for seed in range(5):
        run = evaluate_seed(seed, n_items=300, noise_rate=0.0)
        assert run["unlabeled_disputes"] == 0
        assert run["macro_f1"] >= 0.99, run["tool"]


def test_synthetic_noise_is_separated_from_labeled_disputes():
    run = evaluate_seed(0, n_items=300, noise_rate=0.05)
    assert run["unlabeled_disputes"] > 0
    assert run["macro_f1"] >= 0.95, run["tool"]


def test_generated_ground_truth_matches_known_causes():
    _, _, anns, truth = generate(n_items=200, seed=3)
    assert set(truth.values()) == {"规范未覆盖", "系统性偏差", "个别错误"}
    result = {d["id"]: d["category"] for d in classify.classify_disputes(
        anns, sorted(truth)
    )}
    assert result == truth
