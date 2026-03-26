---
name: ZeroSCROLLS
slug: zeroscrolls
language: en
category: Long-Context Understanding and Reasoning
subcategory: Comprehensive Long-Context Tasks
memory_type: Working / In-Context
year: "2023"
primary_source_kind: paper
primary_source_url: https://arxiv.org/abs/2305.14196
counterpart_zh: ../../zh/01_long_context/zeroscrolls.md
---

# ZeroSCROLLS

[English Knowledge Base Index](../README.md) | [中文卡片](../../zh/01_long_context/zeroscrolls.md)

## Structured Metadata

| Field | Content |
|---|---|
| Benchmark | ZeroSCROLLS |
| Category | Long-Context Understanding and Reasoning |
| Subcategory | Comprehensive Long-Context Tasks |
| Memory Focus | Working / In-Context |
| First Year | 2023 |
| Primary Source Type | paper |
| Paper Title | ZeroSCROLLS: A Zero-Shot Benchmark for Long Text Understanding |
| Chinese Card | [ZeroSCROLLS](../../zh/01_long_context/zeroscrolls.md) |

## Overview

A zero-shot long-text benchmark derived from SCROLLS and additional datasets with tiny validation sets and no training split.

## Abstract
### Original Abstract
> We introduce ZeroSCROLLS, a zero-shot benchmark for natural language understanding over long texts, which contains only test and small validation sets, without training data. We adapt six tasks from the SCROLLS benchmark, and add four new datasets, including two novel information fusing tasks, such as aggregating the percentage of positive reviews. Using ZeroSCROLLS, we conduct a comprehensive evaluation of both open-source and closed large language models, finding that Claude outperforms ChatGPT, and that GPT-4 achieves the highest average score. However, there is still room for improvement on multiple open challenges in ZeroSCROLLS, such as aggregation tasks, where models struggle to pass the naive baseline. As the state of the art is a moving target, we invite researchers to evaluate their ideas on the live ZeroSCROLLS leaderboard.

### Curated Summary
A zero-shot long-text benchmark derived from SCROLLS and additional datasets with tiny validation sets and no training split.

## Links

| Type | Link |
|---|---|
| Paper | https://arxiv.org/abs/2305.14196 |
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

## Remarks

- This card prioritizes official paper pages, project pages, and code repositories. When a link in the original report was incorrect, the corrected official link is used instead.
