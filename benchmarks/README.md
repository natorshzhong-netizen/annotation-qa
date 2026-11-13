# 公开数据集实测

这里放三份公开多标注者数据集的转换脚本和 1,000 条抽样结果。原始文件不提交，
用 `prepare.py` 重新下载转换即可复现。

| 数据集 | 来源 | 许可证 | 标注结构 | 用途 |
|---|---|---|---|---|
| **GoEmotions** | [HF: google-research-datasets/go_emotions](https://huggingface.co/datasets/google-research-datasets/go_emotions) | Apache-2.0 | 82 位标注者，跨样本保持 ID，存在漏标 | 稀疏数据 + 真实情绪类别 |
| **HateXplain** | [GitHub: hate-alert/HateXplain](https://github.com/hate-alert/HateXplain) | MIT | 166 位标注者，每条 3 人，存在漏标 | 完整评审小组 + 归因 |
| **ChaosNLI** | [HF: tasksource/chaos-mnli-ambiguity](https://huggingface.co/datasets/tasksource/chaos-mnli-ambiguity) | CC BY-NC 4.0 | 每条 100 人分布 | 高分歧数据的一致性指标 |

> ChaosNLI 的 100 个标签没有跨样本身份。这里每条随机抽 5 个标签当作「标注槽」，
> **只用于一致性指标，不用于「谁有系统性偏差」的归因**。
>
> **内容警告：** GoEmotions 与 HateXplain 的原始文本包含冒犯性/仇恨言论，
> 抽样仅用于评测，不代表本项目立场。

## 目录

```
benchmarks/
├── prepare.py          原始数据 → 本项目格式
├── data/               1,000 条抽样（提交）
│   ├── go_emotions/
│   ├── hatexplain/
│   └── chaosnli/
├── raw/                原始下载文件（.gitignore）
├── data_full/          10,000 条全量转换（.gitignore）
├── results.json        汇总结果（仪表盘使用）
└── reports/            各数据集生成的 Markdown 报告
```

## 复现

```bash
# 1. 下载原始数据（见下方链接），放到 benchmarks/raw/ 对应目录
# 2. 转成项目格式
.venv/Scripts/python.exe benchmarks/prepare.py --dataset all --limit 1000
.venv/Scripts/python.exe benchmarks/prepare.py --dataset all --limit 10000 --out-root benchmarks/data_full

# 3. 跑报告
python -m src --data-dir benchmarks/data_full/go_emotions --allow-missing --out benchmarks/reports/go_emotions_full.md
python -m src --data-dir benchmarks/data_full/hatexplain --allow-missing --out benchmarks/reports/hatexplain_full.md
python -m src --data-dir benchmarks/data_full/chaosnli --out benchmarks/reports/chaosnli_full.md

# 4. 汇总
python eval/summarize_benchmarks.py
```

原始文件地址：

```bash
mkdir -p benchmarks/raw/{go_emotions,multi_nli,ocnli,hatexplain,chaosnli}

curl -L "https://hf-mirror.com/datasets/google-research-datasets/go_emotions/resolve/main/raw/train-00000-of-00001.parquet" \
  -o benchmarks/raw/go_emotions/train.parquet

curl -L "https://cdn.jsdelivr.net/gh/hate-alert/HateXplain@master/Data/dataset.json" \
  -o benchmarks/raw/hatexplain/dataset.json

curl -L "https://hf-mirror.com/datasets/tasksource/chaos-mnli-ambiguity/resolve/main/data/train-00000-of-00001.parquet" \
  -o benchmarks/raw/chaosnli/train.parquet
```

## 转换规则

| 数据集 | 规则 |
|---|---|
| GoEmotions | 只保留恰好一个情绪标签为 1 的评分；丢弃多标签/全 0；保留标注数 ≥ 20 的标注者 |
| HateXplain | 每条帖子取 3 位标注者的标签；保留标注数 ≥ 20 的标注者；每条至少保留 2 人 |
| ChaosNLI | 每条从 100 个标签里随机抽 5 个作为标注槽 |

## 实测结果（10,000 条抽样）

| 数据集 | 样本 | 标注者 | 一致性 | 95% CI | 争议 | 系统性偏差者 |
|---|---|---|---|---|---|---|
| GoEmotions | 10,000 | 80 | Krippendorff's α 0.272 | [0.265, 0.279] | 7,484 | 3 |
| HateXplain | 10,000 | 166 | Krippendorff's α 0.460 | [0.449, 0.469] | 5,040 | 41 |
| ChaosNLI | 1,599 | 5 槽 | Fleiss' κ 0.303 | [0.284, 0.320] | 1,307 | 0 |

数字来自 `benchmarks/results.json`，跑法见上。不同抽样会带来小幅波动。

> GoEmotions 与 ChaosNLI 是开放域标注，没有业务规范；它们的「规范未覆盖」计数只验证规则能否运行，
> 不应解读为真实质检结论。HateXplain 的标签体系更接近一个有明确类别的标注任务，归因结果更有解释力。

## 引用

- Demszky et al. 2020. *GoEmotions: A Dataset of Fine-Grained Emotions*. arXiv:2005.00547.
- Mathew et al. 2020. *HateXplain: A Benchmark Dataset for Explainable Hate Speech Detection*. arXiv:2012.10289.
- Nie et al. 2020. *What Can We Learn from Collective Human Opinions on Natural Language Inference Data?* arXiv:2010.03532.
