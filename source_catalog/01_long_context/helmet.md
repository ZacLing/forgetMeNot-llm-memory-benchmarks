---
name: HELMET
slug: helmet
category: 长上下文理解与推理
subcategory: 长上下文综合任务
memory_type: Working / In-Context
year: "2024"
primary_source_kind: paper
primary_source_url: https://arxiv.org/abs/2410.02694
---

# HELMET

## 结构化信息

| 字段 | 内容 |
|---|---|
| Benchmark | HELMET |
| 分类 | 长上下文理解与推理 |
| 子类 | 长上下文综合任务 |
| 记忆侧重 | Working / In-Context |
| 首次年份 | 2024 |
| 主要来源类型 | paper |
| 论文标题 | HELMET: How to Evaluate Long-Context Language Models Effectively and Thoroughly |

## 基础介绍

动机：作者指出常见长上下文 benchmark 往往覆盖面不足、长度不够、指标不稳，且对 base model 不友好，导致排行榜信号噪声较大。
设计：HELMET 将评测组织成 7 个面向应用的类别，并把上下文长度控制到最高 128K tokens，同时引入 model-based evaluation 与 few-shot prompting。
用途：适合做“综合型长上下文能力”评测，尤其适合比较不同模型在真实下游任务、复杂指令遵循与 full-context reasoning 上的表现差异。
结论：论文明确指出 NIAH 一类合成测试并不能稳定预测真实下游表现，因此 HELMET 更强调跨任务、跨长度、跨指标的整体评测。

## Abstract
### 原始摘要
> Many benchmarks exist for evaluating long-context language models (LCLMs), yet developers often rely on synthetic tasks such as needle-in-a-haystack (NIAH) or an arbitrary subset of tasks. However, it remains unclear whether these benchmarks reflect the diverse downstream applications of LCLMs, and such inconsistencies further complicate model comparison. We investigate the underlying reasons behind these practices and find that existing benchmarks often provide noisy signals due to limited coverage of applications, insufficient context lengths, unreliable metrics, and incompatibility with base models. In this work, we introduce HELMET (How to Evaluate Long-context Models Effectively and Thoroughly), a comprehensive benchmark encompassing seven diverse, application-centric categories. We also address several issues in previous benchmarks by adding controllable lengths up to 128K tokens, model-based evaluation for reliable metrics, and few-shot prompting for robustly evaluating base models. Consequently, we demonstrate that HELMET offers more reliable and consistent rankings of frontier LCLMs. Through a comprehensive study of 59 LCLMs, we find that (1) synthetic tasks like NIAH do not reliably predict downstream performance; (2) the diverse categories in HELMET exhibit distinct trends and low correlations with each other; and (3) while most LCLMs achieve perfect NIAH scores, open-source models significantly lag behind closed ones when tasks require full-context reasoning or following complex instructions -- the gap widens as length increases. Finally, we recommend using our RAG tasks for fast model development, as they are easy to run and better predict other downstream performance; ultimately, we advocate for a holistic evaluation across diverse tasks.

### 中文抽取
HELMET 是一个覆盖 7 个 application-centric 类别的综合型长上下文 benchmark，强调可控长度、多任务覆盖、稳定指标和对 base model 友好的评测设置。它的核心贡献之一是证明 NIAH 分数并不能可靠预测真实下游性能。

## URL 汇总

| 类型 | 链接 |
|---|---|
| 论文页 | https://arxiv.org/abs/2410.02694 |
| GitHub | https://github.com/princeton-nlp/HELMET |
| 项目主页 | https://princeton-nlp.github.io/HELMET/ |

## BibTeX

```bibtex
@misc{yen2024helmet,
  title = {HELMET: How to Evaluate Long-Context Language Models Effectively and Thoroughly},
  author = {Yen, Howard and Gao, Tianyu and Hou, Minmin and Ding, Ke and Fleischer, Daniel and Izsak, Peter and Wasserblat, Moshe and Chen, Danqi},
  year = {2024},
  eprint = {2410.02694},
  archivePrefix = {arXiv},
  primaryClass = {cs.CL},
  url = {https://arxiv.org/abs/2410.02694},
  note = {ICLR 2025}
}
```

## 备注

- 本卡片优先使用 arXiv、官方 GitHub 与项目主页；项目页明确给出了 benchmark 结构与推荐使用方式。
