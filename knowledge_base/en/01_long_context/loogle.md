---
name: LooGLE
slug: loogle
language: en
category: Long-Context Understanding and Reasoning
subcategory: 长上下文综合任务
memory_type: Working / In-Context
year: "2024"
primary_source_kind: paper
primary_source_url: https://arxiv.org/abs/2311.04939
counterpart_zh: ../../zh/01_long_context/loogle.md
---

# LooGLE

[English Knowledge Base Index](../README.md) | [中文卡片](../../zh/01_long_context/loogle.md)

## Structured Metadata

| Field | Content |
|---|---|
| Benchmark | LooGLE |
| Category | Long-Context Understanding and Reasoning |
| Subcategory | 长上下文综合任务 |
| Memory Focus | Working / In-Context |
| First Year | 2024 |
| Primary Source Type | paper |
| Paper Title | LooGLE: Can Long-Context Language Models Understand Long Contexts? |
| Chinese Card | [LooGLE](../../zh/01_long_context/loogle.md) |

## Overview

A long-document benchmark built from recent real-world documents with both automatic and human-written QA.

## Abstract
### Original Abstract
> Large language models (LLMs), despite their impressive performance in various language tasks, are typically limited to processing texts within context-window size. This limitation has spurred significant research efforts to enhance LLMs' long-context understanding with high-quality long-sequence benchmarks. However, prior datasets in this regard suffer from shortcomings, such as short context length compared to the context window of modern LLMs; outdated documents that have data leakage problems; and an emphasis on short dependency tasks rather than long dependency tasks. In this paper, we present LooGLE, a Long Context Generic Language Evaluation benchmark for LLMs' long context understanding. LooGLE features relatively new documents post-2022, with over 24,000 tokens per document and 6,000 newly generated questions spanning diverse domains. Human annotators meticulously crafted more than 1,100 high-quality question-answer pairs to meet the long dependency requirements. These pairs underwent thorough cross-validation, yielding the most precise assessment of LLMs' long dependency capabilities. The evaluation of eight state-of-the-art LLMs on LooGLE revealed key findings: (i) commercial models outperformed open-sourced models; (ii) LLMs excelled in short dependency tasks like short question-answering and cloze tasks but struggled with more intricate long dependency tasks; (iii) in-context learning and chaining thoughts offered only marginal improvements; (iv) retrieval-based techniques demonstrated substantial benefits for short question-answering, while strategies for extending context window length had limited impact on long context understanding. As such, LooGLE not only provides a systematic and comprehensive evaluation schema on long-context LLMs, but also sheds light on future development of enhanced models towards "true long-context understanding".

### Curated Summary
A long-document benchmark built from recent real-world documents with both automatic and human-written QA.

## Links

| Type | Link |
|---|---|
| Paper | https://arxiv.org/abs/2311.04939 |
| Project Page | https://github.com/bigai-nlco/LooGLE |
| other_acl-version_url | https://aclanthology.org/2024.acl-long.859/ |

## BibTeX

```bibtex
@misc{https://doi.org/10.48550/arxiv.2311.04939,
  doi = {10.48550/ARXIV.2311.04939},
  url = {https://arxiv.org/abs/2311.04939},
  author = {Li, Jiaqi and Wang, Mengmeng and Zheng, Zilong and Zhang, Muhan},
  keywords = {Computation and Language (cs.CL), Artificial Intelligence (cs.AI), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {LooGLE: Can Long-Context Language Models Understand Long Contexts?},
  publisher = {arXiv},
  year = {2023},
  copyright = {arXiv.org perpetual, non-exclusive license}
}
```

## Remarks

- This card prioritizes official paper pages, project pages, and code repositories. When a link in the original report was incorrect, the corrected official link is used instead.
