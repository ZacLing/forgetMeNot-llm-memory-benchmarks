---
name: Ref-Long
slug: ref-long
language: en
category: Long-Context Understanding and Reasoning
subcategory: 引用定位与忠实性
memory_type: Working / In-Context
year: "2025"
primary_source_kind: paper
primary_source_url: https://arxiv.org/abs/2507.09506
counterpart_zh: ../../zh/01_long_context/ref-long.md
---

# Ref-Long

[English Knowledge Base Index](../README.md) | [中文卡片](../../zh/01_long_context/ref-long.md)

## Structured Metadata

| Field | Content |
|---|---|
| Benchmark | Ref-Long |
| Category | Long-Context Understanding and Reasoning |
| Subcategory | 引用定位与忠实性 |
| Memory Focus | Working / In-Context |
| First Year | 2025 |
| Primary Source Type | paper |
| Paper Title | Ref-Long: Benchmarking the Long-context Referencing Capability of Long-context Language Models |
| Chinese Card | [Ref-Long](../../zh/01_long_context/ref-long.md) |

## Overview

A referencing-oriented long-context benchmark that asks models to identify which documents point to a target key.

## Abstract
### Original Abstract
> Long-context language models (LCLMs) have exhibited impressive capabilities in long-context understanding tasks. Among these, long-context referencing -- a crucial task that requires LCLMs to attribute items of interest to specific parts of long-context data -- remains underexplored. To bridge this gap, this paper proposes Referencing Evaluation for Long-context Language Models (Ref-Long), a novel benchmark designed to assess the long-context referencing capability of LCLMs. Specifically, Ref-Long requires LCLMs to identify the indexes of documents that reference a specific key, emphasizing contextual relationships between the key and the documents over simple retrieval. Based on the task design, we construct three subsets ranging from synthetic to realistic scenarios to form the Ref-Long benchmark. Experimental results of 13 LCLMs reveal significant shortcomings in long-context referencing, even among advanced models like GPT-4o. To further investigate these challenges, we conduct comprehensive analyses, including human evaluations, task format adjustments, fine-tuning experiments, and error analyses, leading to several key insights. Our data and code can be found in https://github. com/wujunjie1998/Ref-Long.

### Curated Summary
A referencing-oriented long-context benchmark that asks models to identify which documents point to a target key.

## Links

| Type | Link |
|---|---|
| Paper | https://arxiv.org/abs/2507.09506 |
| Project Page | https://wujunjie1998.github.io/Ref-Long-website/ |
| paper_url_2 | https://github.com/wujunjie1998/Ref-Long |

## BibTeX

```bibtex
@misc{https://doi.org/10.48550/arxiv.2507.09506,
  doi = {10.48550/ARXIV.2507.09506},
  url = {https://arxiv.org/abs/2507.09506},
  author = {Wu, Junjie and Gu, Gefei and Zheng, Yanan and Yeung, Dit-Yan and Cohan, Arman},
  keywords = {Computation and Language (cs.CL), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {Ref-Long: Benchmarking the Long-context Referencing Capability of Long-context Language Models},
  publisher = {arXiv},
  year = {2025},
  copyright = {Creative Commons Attribution 4.0 International}
}
```

## Remarks

- This card prioritizes official paper pages, project pages, and code repositories. When a link in the original report was incorrect, the corrected official link is used instead.
