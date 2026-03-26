---
name: ZeroSCROLLS
slug: zeroscrolls
category: 长上下文理解与推理
subcategory: 长上下文综合任务
memory_type: Working / In-Context
year: "2023"
primary_source_kind: paper
primary_source_url: https://arxiv.org/abs/2305.14196
---

# ZeroSCROLLS

## 结构化信息

| 字段 | 内容 |
|---|---|
| Benchmark | ZeroSCROLLS |
| 分类 | 长上下文理解与推理 |
| 子类 | 长上下文综合任务 |
| 记忆侧重 | Working / In-Context |
| 首次年份 | 2023 |
| 主要来源类型 | paper |
| 论文标题 | ZeroSCROLLS: A Zero-Shot Benchmark for Long Text Understanding |

## 基础介绍

ZeroSCROLLS：从 SCROLLS 选 6 个任务并新增 4 个数据集，仅保留 test 与极小验证集，主要面向 zero-shot 长文本评测。

## Abstract
### 原始摘要
> We introduce ZeroSCROLLS, a zero-shot benchmark for natural language understanding over long texts, which contains only test and small validation sets, without training data. We adapt six tasks from the SCROLLS benchmark, and add four new datasets, including two novel information fusing tasks, such as aggregating the percentage of positive reviews. Using ZeroSCROLLS, we conduct a comprehensive evaluation of both open-source and closed large language models, finding that Claude outperforms ChatGPT, and that GPT-4 achieves the highest average score. However, there is still room for improvement on multiple open challenges in ZeroSCROLLS, such as aggregation tasks, where models struggle to pass the naive baseline. As the state of the art is a moving target, we invite researchers to evaluate their ideas on the live ZeroSCROLLS leaderboard.

### 中文抽取
ZeroSCROLLS：从 SCROLLS 选 6 个任务并新增 4 个数据集，仅保留 test 与极小验证集，主要面向 zero-shot 长文本评测。

## URL 汇总

| 类型 | 链接 |
|---|---|
| 论文页 | https://arxiv.org/abs/2305.14196 |
| other_zeroscrolls-hf_url | https://huggingface.co/datasets/tau/zero_scrolls |

## BibTeX

```bibtex
@misc{https://doi.org/10.48550/arxiv.2305.14196,
  doi = {10.48550/ARXIV.2305.14196},
  url = {https://arxiv.org/abs/2305.14196},
  author = {Shaham, Uri and Ivgi, Maor and Efrat, Avia and Berant, Jonathan and Levy, Omer},
  keywords = {Computation and Language (cs.CL), Artificial Intelligence (cs.AI), Machine Learning (cs.LG), Machine Learning (stat.ML), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {ZeroSCROLLS: A Zero-Shot Benchmark for Long Text Understanding},
  publisher = {arXiv},
  year = {2023},
  copyright = {Creative Commons Attribution 4.0 International}
}
```

## 备注

- 本卡片优先使用论文页、项目页与代码仓库等官方来源；若原报告中的链接存在错误，则以标题匹配后的官方链接为准。
