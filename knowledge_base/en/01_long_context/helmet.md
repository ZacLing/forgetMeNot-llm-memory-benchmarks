---
name: HELMET
slug: helmet
language: en
category: Long-Context Understanding and Reasoning
subcategory: Comprehensive Long-Context Tasks
memory_type: Working / In-Context
year: "2024"
primary_source_kind: paper
primary_source_url: https://arxiv.org/abs/2410.02694
counterpart_zh: ../../zh/01_long_context/helmet.md
---

# HELMET

[English Knowledge Base Index](../README.md) | [中文卡片](../../zh/01_long_context/helmet.md)

## Structured Metadata

| Field | Content |
|---|---|
| Benchmark | HELMET |
| Category | Long-Context Understanding and Reasoning |
| Subcategory | Comprehensive Long-Context Tasks |
| Memory Focus | Working / In-Context |
| First Year | 2024 |
| Primary Source Type | paper |
| Paper Title | HELMET: How to Evaluate Long-Context Language Models Effectively and Thoroughly |
| Chinese Card | [HELMET](../../zh/01_long_context/helmet.md) |

## Overview

A comprehensive long-context benchmark spanning seven application-centric categories, controllable lengths up to 128K, and more reliable evaluation protocols.

## Abstract
### Original Abstract
> Many benchmarks exist for evaluating long-context language models (LCLMs), yet developers often rely on synthetic tasks such as needle-in-a-haystack (NIAH) or an arbitrary subset of tasks. However, it remains unclear whether these benchmarks reflect the diverse downstream applications of LCLMs, and such inconsistencies further complicate model comparison. We investigate the underlying reasons behind these practices and find that existing benchmarks often provide noisy signals due to limited coverage of applications, insufficient context lengths, unreliable metrics, and incompatibility with base models. In this work, we introduce HELMET (How to Evaluate Long-context Models Effectively and Thoroughly), a comprehensive benchmark encompassing seven diverse, application-centric categories. We also address several issues in previous benchmarks by adding controllable lengths up to 128K tokens, model-based evaluation for reliable metrics, and few-shot prompting for robustly evaluating base models. Consequently, we demonstrate that HELMET offers more reliable and consistent rankings of frontier LCLMs. Through a comprehensive study of 59 LCLMs, we find that (1) synthetic tasks like NIAH do not reliably predict downstream performance; (2) the diverse categories in HELMET exhibit distinct trends and low correlations with each other; and (3) while most LCLMs achieve perfect NIAH scores, open-source models significantly lag behind closed ones when tasks require full-context reasoning or following complex instructions -- the gap widens as length increases. Finally, we recommend using our RAG tasks for fast model development, as they are easy to run and better predict other downstream performance; ultimately, we advocate for a holistic evaluation across diverse tasks.

### Curated Summary

A comprehensive long-context benchmark spanning seven application-centric categories, controllable lengths up to 128K, and more reliable evaluation protocols.

## Links

| Type | Link |
|---|---|
| Paper | https://arxiv.org/abs/2410.02694 |
| GitHub | https://github.com/princeton-nlp/HELMET |
| Project Page | https://princeton-nlp.github.io/HELMET/ |

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

## Remarks

- HELMET is especially useful when NIAH-style results are too narrow and you want rankings over broader downstream task families.
