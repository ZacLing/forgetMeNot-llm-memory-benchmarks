---
name: NoLiMa
slug: nolima
language: en
category: Needle Retrieval and Diagnostic Probes
subcategory: Needle / Passkey / Synthetic Diagnostics
memory_type: Working / In-Context
year: "2025"
primary_source_kind: paper
primary_source_url: https://arxiv.org/abs/2502.05167
counterpart_zh: ../../zh/02_needle_and_diagnostics/nolima.md
---

# NoLiMa

[English Knowledge Base Index](../README.md) | [中文卡片](../../zh/02_needle_and_diagnostics/nolima.md)

## Structured Metadata

| Field | Content |
|---|---|
| Benchmark | NoLiMa |
| Category | Needle Retrieval and Diagnostic Probes |
| Subcategory | Needle / Passkey / Synthetic Diagnostics |
| Memory Focus | Working / In-Context |
| First Year | 2025 |
| Primary Source Type | paper |
| Paper Title | NoLiMa: Long-Context Evaluation Beyond Literal Matching |
| Chinese Card | [NoLiMa](../../zh/02_needle_and_diagnostics/nolima.md) |

## Overview

A NIAH-style benchmark that removes lexical-overlap shortcuts and forces models to retrieve needles through latent semantic association rather than literal matching.

## Abstract
### Original Abstract
> Recent large language models (LLMs) support long contexts ranging from 128K to 1M tokens. A popular method for evaluating these capabilities is the needle-in-a-haystack (NIAH) test, which involves retrieving a "needle" (relevant information) from a "haystack" (long irrelevant context). Extensions of this approach include increasing distractors, fact chaining, and in-context reasoning. However, in these benchmarks, models can exploit existing literal matches between the needle and haystack to simplify the task. To address this, we introduce NoLiMa, a benchmark extending NIAH with a carefully designed needle set, where questions and needles have minimal lexical overlap, requiring models to infer latent associations to locate the needle within the haystack. We evaluate 13 popular LLMs that claim to support contexts of at least 128K tokens. While they perform well in short contexts (<1K), performance degrades significantly as context length increases. At 32K, for instance, 11 models drop below 50% of their strong short-length baselines. Even GPT-4o, one of the top-performing exceptions, experiences a reduction from an almost-perfect baseline of 99.3% to 69.7%. Our analysis suggests these declines stem from the increased difficulty the attention mechanism faces in longer contexts when literal matches are absent, making it harder to retrieve relevant information. Even models enhanced with reasoning capabilities or CoT prompting struggle to maintain performance in long contexts. We publicly release the dataset and evaluation code at https://github.com/adobe-research/NoLiMa.

### Curated Summary

A NIAH-style benchmark that removes lexical-overlap shortcuts and forces models to retrieve needles through latent semantic association rather than literal matching.

## Links

| Type | Link |
|---|---|
| Paper | https://arxiv.org/abs/2502.05167 |
| GitHub | https://github.com/adobe-research/NoLiMa |
| Project Page | https://research.adobe.com/publication/nolima-long-context-evaluation-beyond-literal-matching/ |

## BibTeX

```bibtex
@misc{modarressi2025nolima,
  title = {NoLiMa: Long-Context Evaluation Beyond Literal Matching},
  author = {Modarressi, Ali and Deilamsalehy, Hanieh and Dernoncourt, Franck and Bui, Trung and Rossi, Ryan A. and Yoon, Seunghyun and Sch{\"u}tze, Hinrich},
  year = {2025},
  eprint = {2502.05167},
  archivePrefix = {arXiv},
  primaryClass = {cs.CL},
  url = {https://arxiv.org/abs/2502.05167},
  note = {Accepted at ICML 2025}
}
```

## Remarks

- NoLiMa is best read as a harder semantic variant of NIAH rather than a completely different evaluation paradigm.
