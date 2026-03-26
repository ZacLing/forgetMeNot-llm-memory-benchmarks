---
name: Loong
slug: loong
language: en
category: Long-Context Understanding and Reasoning
subcategory: 长上下文综合任务
memory_type: Working / In-Context
year: "2024"
primary_source_kind: paper
primary_source_url: https://arxiv.org/abs/2406.17419
counterpart_zh: ../../zh/01_long_context/loong.md
---

# Loong

[English Knowledge Base Index](../README.md) | [中文卡片](../../zh/01_long_context/loong.md)

## Structured Metadata

| Field | Content |
|---|---|
| Benchmark | Loong |
| Category | Long-Context Understanding and Reasoning |
| Subcategory | 长上下文综合任务 |
| Memory Focus | Working / In-Context |
| First Year | 2024 |
| Primary Source Type | paper |
| Paper Title | Leave No Document Behind: Benchmarking Long-Context LLMs with Extended Multi-Doc QA |
| Chinese Card | [Loong](../../zh/01_long_context/loong.md) |

## Overview

An extended multi-document QA benchmark where every document is relevant, so missing any document hurts performance.

## Abstract
### Original Abstract
> Long-context modeling capabilities have garnered widespread attention, leading to the emergence of Large Language Models (LLMs) with ultra-context windows. Meanwhile, benchmarks for evaluating long-context LLMs are gradually catching up. However, existing benchmarks employ irrelevant noise texts to artificially extend the length of test cases, diverging from the real-world scenarios of long-context applications. To bridge this gap, we propose a novel long-context benchmark, Loong, aligning with realistic scenarios through extended multi-document question answering (QA). Unlike typical document QA, in Loong's test cases, each document is relevant to the final answer, ignoring any document will lead to the failure of the answer. Furthermore, Loong introduces four types of tasks with a range of context lengths: Spotlight Locating, Comparison, Clustering, and Chain of Reasoning, to facilitate a more realistic and comprehensive evaluation of long-context understanding. Extensive experiments indicate that existing long-context language models still exhibit considerable potential for enhancement. Retrieval augmented generation (RAG) achieves poor performance, demonstrating that Loong can reliably assess the model's long-context modeling capabilities.

### Curated Summary
An extended multi-document QA benchmark where every document is relevant, so missing any document hurts performance.

## Links

| Type | Link |
|---|---|
| Paper | https://arxiv.org/abs/2406.17419 |
| GitHub | https://github.com/MozerWang/Loong |
| other_emnlp-pdf_url | https://aclanthology.org/2024.emnlp-main.322.pdf |

## BibTeX

```bibtex
@misc{https://doi.org/10.48550/arxiv.2406.17419,
  doi = {10.48550/ARXIV.2406.17419},
  url = {https://arxiv.org/abs/2406.17419},
  author = {Wang, Minzheng and Chen, Longze and Fu, Cheng and Liao, Shengyi and Zhang, Xinghua and Wu, Bingli and Yu, Haiyang and Xu, Nan and Zhang, Lei and Luo, Run and Li, Yunshui and Yang, Min and Huang, Fei and Li, Yongbin},
  keywords = {Computation and Language (cs.CL), Artificial Intelligence (cs.AI), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {Leave No Document Behind: Benchmarking Long-Context LLMs with Extended Multi-Doc QA},
  publisher = {arXiv},
  year = {2024},
  copyright = {arXiv.org perpetual, non-exclusive license}
}
```

## Remarks

- This card prioritizes official paper pages, project pages, and code repositories. When a link in the original report was incorrect, the corrected official link is used instead.
