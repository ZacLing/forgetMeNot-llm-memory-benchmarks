---
name: BABILong
slug: babilong
language: en
category: Needle Retrieval and Diagnostic Probes
subcategory: Needle / Passkey / 合成诊断
memory_type: Working / In-Context
year: "2024"
primary_source_kind: paper
primary_source_url: https://arxiv.org/abs/2406.10149
counterpart_zh: ../../zh/02_needle_and_diagnostics/babilong.md
---

# BABILong

[English Knowledge Base Index](../README.md) | [中文卡片](../../zh/02_needle_and_diagnostics/babilong.md)

## Structured Metadata

| Field | Content |
|---|---|
| Benchmark | BABILong |
| Category | Needle Retrieval and Diagnostic Probes |
| Subcategory | Needle / Passkey / 合成诊断 |
| Memory Focus | Working / In-Context |
| First Year | 2024 |
| Primary Source Type | paper |
| Paper Title | BABILong: Testing the Limits of LLMs with Long Context Reasoning-in-a-Haystack |
| Chinese Card | [BABILong](../../zh/02_needle_and_diagnostics/babilong.md) |

## Overview

A reasoning-in-a-haystack benchmark that embeds bAbI-style reasoning tasks inside ultra-long documents.

## Abstract
### Original Abstract
> In recent years, the input context sizes of large language models (LLMs) have increased dramatically. However, existing evaluation methods have not kept pace, failing to comprehensively assess the efficiency of models in handling long contexts. To bridge this gap, we introduce the BABILong benchmark, designed to test language models' ability to reason across facts distributed in extremely long documents. BABILong includes a diverse set of 20 reasoning tasks, including fact chaining, simple induction, deduction, counting, and handling lists/sets. These tasks are challenging on their own, and even more demanding when the required facts are scattered across long natural text. Our evaluations show that popular LLMs effectively utilize only 10-20\% of the context and their performance declines sharply with increased reasoning complexity. Among alternatives to in-context reasoning, Retrieval-Augmented Generation methods achieve a modest 60\% accuracy on single-fact question answering, independent of context length. Among context extension methods, the highest performance is demonstrated by recurrent memory transformers after fine-tuning, enabling the processing of lengths up to 50 million tokens. The BABILong benchmark is extendable to any length to support the evaluation of new upcoming models with increased capabilities, and we provide splits up to 10 million token lengths.

### Curated Summary
A reasoning-in-a-haystack benchmark that embeds bAbI-style reasoning tasks inside ultra-long documents.

## Links

| Type | Link |
|---|---|
| Paper | https://arxiv.org/abs/2406.10149 |
| GitHub | https://github.com/booydar/babilong |

## BibTeX

```bibtex
@misc{https://doi.org/10.48550/arxiv.2406.10149,
  doi = {10.48550/ARXIV.2406.10149},
  url = {https://arxiv.org/abs/2406.10149},
  author = {Kuratov, Yuri and Bulatov, Aydar and Anokhin, Petr and Rodkin, Ivan and Sorokin, Dmitry and Sorokin, Artyom and Burtsev, Mikhail},
  keywords = {Computation and Language (cs.CL), Artificial Intelligence (cs.AI), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {BABILong: Testing the Limits of LLMs with Long Context Reasoning-in-a-Haystack},
  publisher = {arXiv},
  year = {2024},
  copyright = {arXiv.org perpetual, non-exclusive license}
}
```

## Remarks

- This card prioritizes official paper pages, project pages, and code repositories. When a link in the original report was incorrect, the corrected official link is used instead.
