---
name: BAMBOO
slug: bamboo
language: zh
category: 长上下文理解与推理
subcategory: 长上下文综合任务
memory_type: Working / In-Context
year: "2024"
primary_source_kind: paper
primary_source_url: https://arxiv.org/abs/2309.13345
counterpart_en: ../../en/01_long_context/bamboo.md
---

# BAMBOO

[中文知识库索引](../README.md) | [English Card](../../en/01_long_context/bamboo.md)

## 结构化信息

| 字段 | 内容 |
|---|---|
| Benchmark | BAMBOO |
| 分类 | 长上下文理解与推理 |
| 子类 | 长上下文综合任务 |
| 记忆侧重 | Working / In-Context |
| 首次年份 | 2024 |
| 主要来源类型 | paper |
| 论文标题 | BAMBOO: A Comprehensive Benchmark for Evaluating Long Text Modeling Capacities of Large Language Models |
| 英文卡片 | [BAMBOO](../../en/01_long_context/bamboo.md) |

## 基础介绍

组成：10 数据集、5 任务（QA、幻觉检测、文本排序、语言建模、代码补全），强调抗污染与更准确自动评测。

## Abstract
### 原始摘要
> Large language models (LLMs) have achieved dramatic proficiency over NLP tasks with normal length. Recently, multiple studies have committed to extending the context length and enhancing the long text modeling capabilities of LLMs. To comprehensively evaluate the long context ability of LLMs, we propose BAMBOO, a multi-task long context benchmark. BAMBOO has been designed with four principles: comprehensive capacity evaluation, avoidance of data contamination, accurate automatic evaluation, and different length levels. It consists of 10 datasets from 5 different long text understanding tasks, i.e. question answering, hallucination detection, text sorting, language modeling, and code completion, to cover core capacities and various domains of LLMs. We conduct experiments with five long context models on BAMBOO and further discuss four key research questions of long text. We also qualitatively analyze current long context models and point out future directions for enhancing long text modeling capacities. We release our data, prompts, and code at https://github.com/RUCAIBox/BAMBOO.

### 中文抽取
组成：10 数据集、5 任务（QA、幻觉检测、文本排序、语言建模、代码补全），强调抗污染与更准确自动评测。

## URL 汇总

| 类型 | 链接 |
|---|---|
| 论文页 | https://arxiv.org/abs/2309.13345 |
| GitHub | https://github.com/RUCAIBox/BAMBOO |

## BibTeX

```bibtex
@misc{https://doi.org/10.48550/arxiv.2309.13345,
  doi = {10.48550/ARXIV.2309.13345},
  url = {https://arxiv.org/abs/2309.13345},
  author = {Dong, Zican and Tang, Tianyi and Li, Junyi and Zhao, Wayne Xin and Wen, Ji-Rong},
  keywords = {Computation and Language (cs.CL), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {BAMBOO: A Comprehensive Benchmark for Evaluating Long Text Modeling Capacities of Large Language Models},
  publisher = {arXiv},
  year = {2023},
  copyright = {arXiv.org perpetual, non-exclusive license}
}
```

## 备注

- 本卡片优先使用论文页、项目页与代码仓库等官方来源；若原报告中的链接存在错误，则以标题匹配后的官方链接为准。
