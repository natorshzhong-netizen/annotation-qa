# -*- coding: utf-8 -*-
"""生成「原因已知」的合成标注数据，用来验证归因规则。

真实数据里没人知道某条分歧到底是规范问题还是人的问题，所以归因没法直接
算准确率。这里反过来：先定好每条争议的原因，再按原因造标注，最后看工具
能不能把原因认回来。

场景
    spec_gap       三个人各标一种，没有多数派 → 规范未覆盖
    systematic      b 对「商品咨询」固定标成「物流查询」 → 系统性偏差
    random_slip     c 偶尔标错，方向分散 → 个别错误
    noise          额外随机改动，原因不明，评测时排除（用来测误报）

输出与 data/ 目录同构，另加真值：
    items.jsonl / labels.json / ann_*.jsonl / ground_truth.json
"""

from __future__ import annotations

import json
import random
from pathlib import Path

LABELS = [
    "退款退货",
    "物流查询",
    "商品咨询",
    "账号问题",
    "发票报销",
    "投诉建议",
    "优惠券活动",
    "其他",
]

ANNOTATORS = ["a", "b", "c"]
BIAS_FROM = "商品咨询"
BIAS_TO = "物流查询"

TEXT_TEMPLATES = {
    "退款退货": [
        "买的鞋尺码不对，想退掉",
        "收到货有划痕，申请退款",
        "下单后不想要了，能退吗",
        "衣服洗过一次缩水，要求退货",
    ],
    "物流查询": [
        "快递三天没动了，到哪了",
        "显示已签收但没收到",
        "能改一下收货地址吗",
        "为什么物流一直停在转运中心",
    ],
    "商品咨询": [
        "这个型号支持无线充电吗",
        "包装里带不带数据线",
        "尺码偏大还是偏小",
        "和图片颜色一样吗",
    ],
    "账号问题": [
        "手机号换了，登录不上",
        "验证码一直收不到",
        "账号被冻结了怎么解",
        "能改绑邮箱吗",
    ],
    "发票报销": [
        "发票抬头开错了，能重开吗",
        "电子发票在哪里下载",
        "公司报销需要专票",
        "订单能补开发票吗",
    ],
    "投诉建议": [
        "客服态度很差，我要投诉",
        "快递员直接放门口没通知",
        "希望增加夜间配送",
        "包装太简陋，建议改进",
    ],
    "优惠券活动": [
        "满减券为什么用不了",
        "活动页面价格和结算不一致",
        "新人券过期了能补吗",
        "两件折扣能叠加吗",
    ],
    "其他": [
        "想问问有没有线下门店",
        "能不能开发票",
        "会员积分怎么用",
        "这个品牌还有别的系列吗",
    ],
}


def generate(
    n_items: int = 300,
    seed: int = 0,
    spec_gap_rate: float = 0.10,
    bias_rate: float = 0.80,
    slip_rate: float = 0.06,
    noise_rate: float = 0.0,
) -> tuple[dict[str, str], list[str], dict[str, dict[str, str]], dict[str, str]]:
    """返回 (items, labels, anns, ground_truth)。

    ground_truth 只包含原因明确的争议样本：{id: 规范未覆盖 / 系统性偏差 / 个别错误}。
    noise 造成的争议不在真值里，评测时应排除。
    """
    rng = random.Random(seed)
    ids = [f"T{i:03d}" for i in range(1, n_items + 1)]
    true_label = {i: rng.choice(LABELS) for i in ids}

    # 1. 规范空白：三人各标一种，保证没有多数派
    n_gap = max(1, round(n_items * spec_gap_rate))
    gap_ids = set(rng.sample(ids, n_gap))

    # 2. 系统性偏差：b 把「商品咨询」固定标成「物流查询」
    bias_pool = [i for i in ids if i not in gap_ids and true_label[i] == BIAS_FROM]
    n_bias = min(len(bias_pool), max(1, round(len(bias_pool) * bias_rate)))
    bias_ids = set(rng.sample(bias_pool, n_bias))

    # 3. 随机错误：c 偶尔标错，且不碰「商品咨询」，避免和 b 的偏差重叠
    slip_pool = [
        i for i in ids
        if i not in gap_ids and i not in bias_ids and true_label[i] != BIAS_FROM
    ]
    n_slip = max(1, round(n_items * slip_rate))
    n_slip = min(len(slip_pool), n_slip)
    slip_ids = set(rng.sample(slip_pool, n_slip))

    # 4. 原因不明的随机噪声：a 偶尔标错，不写进真值
    noise_ids: set[str] = set()
    if noise_rate > 0:
        noise_pool = [
            i for i in ids
            if i not in gap_ids and i not in bias_ids and i not in slip_ids
        ]
        noise_ids = set(rng.sample(noise_pool, min(len(noise_pool), round(n_items * noise_rate))))

    items: dict[str, str] = {}
    anns: dict[str, dict[str, str]] = {x: {} for x in ANNOTATORS}
    ground_truth: dict[str, str] = {}

    slip_seq = 0
    for i in ids:
        base = true_label[i]
        items[i] = rng.choice(TEXT_TEMPLATES[base])

        if i in gap_ids:
            picks = rng.sample(LABELS, len(ANNOTATORS))
            for who, label in zip(ANNOTATORS, picks):
                anns[who][i] = label
            ground_truth[i] = "规范未覆盖"
            continue

        for who in ANNOTATORS:
            label = base
            if who == "b" and i in bias_ids:
                label = BIAS_TO
            elif who == "c" and i in slip_ids:
                options = sorted(set(LABELS) - {base})
                label = options[slip_seq % len(options)]
                slip_seq += 1
            elif who == "a" and i in noise_ids:
                options = sorted(set(LABELS) - {base})
                label = rng.choice(options)
            anns[who][i] = label

        if i in bias_ids:
            ground_truth[i] = "系统性偏差"
        elif i in slip_ids:
            ground_truth[i] = "个别错误"

    return items, list(LABELS), anns, ground_truth


def write_dataset(
    out_dir: Path,
    n_items: int = 300,
    seed: int = 0,
    **kwargs,
) -> dict[str, str]:
    """把生成的数据写到磁盘，返回真值。"""
    items, labels, anns, truth = generate(n_items=n_items, seed=seed, **kwargs)
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    with open(out_dir / "items.jsonl", "w", encoding="utf-8", newline="\n") as f:
        for iid in sorted(items):
            f.write(json.dumps({"id": iid, "text": items[iid]}, ensure_ascii=False) + "\n")

    (out_dir / "labels.json").write_text(
        json.dumps({"labels": labels}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    for who in sorted(anns):
        with open(out_dir / f"ann_{who}.jsonl", "w", encoding="utf-8", newline="\n") as f:
            for iid in sorted(anns[who]):
                f.write(
                    json.dumps({"id": iid, "label": anns[who][iid]}, ensure_ascii=False) + "\n"
                )

    (out_dir / "ground_truth.json").write_text(
        json.dumps(truth, ensure_ascii=False, indent=2, sort_keys=True),
        encoding="utf-8",
    )
    return truth


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="生成带真值的合成标注数据")
    parser.add_argument("--out", default="eval/generated", help="输出目录")
    parser.add_argument("--items", type=int, default=300)
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument("--noise", type=float, default=0.0)
    args = parser.parse_args()

    write_dataset(Path(args.out), n_items=args.items, seed=args.seed, noise_rate=args.noise)
    print(f"已写入 {args.out}")
