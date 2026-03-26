---
name: ZsRE
slug: zsre
language: en
category: Knowledge Editing and Semantic Memory Updates
subcategory: 知识编辑评测
memory_type: Semantic Memory Update
year: "2017"
primary_source_kind: paper
primary_source_url: https://arxiv.org/abs/1706.04115
counterpart_zh: ../../zh/06_knowledge_editing/zsre.md
---

# ZsRE

[English Knowledge Base Index](../README.md) | [中文卡片](../../zh/06_knowledge_editing/zsre.md)

## Structured Metadata

| Field | Content |
|---|---|
| Benchmark | ZsRE |
| Category | Knowledge Editing and Semantic Memory Updates |
| Subcategory | 知识编辑评测 |
| Memory Focus | Semantic Memory Update |
| First Year | 2017 |
| Primary Source Type | paper |
| Paper Title | Zero-Shot Relation Extraction via Reading Comprehension |
| Chinese Card | [ZsRE](../../zh/06_knowledge_editing/zsre.md) |

## Overview

A zero-shot relation extraction dataset often repurposed as a context-free QA editing benchmark.

## Abstract
### Original Abstract
> We show that relation extraction can be reduced to answering simple reading comprehension questions, by associating one or more natural-language questions with each relation slot. This reduction has several advantages: we can (1) learn relation-extraction models by extending recent neural reading-comprehension techniques, (2) build very large training sets for those models by combining relation-specific crowd-sourced questions with distant supervision, and even (3) do zero-shot learning by extracting new relation types that are only specified at test-time, for which we have no labeled training examples. Experiments on a Wikipedia slot-filling task demonstrate that the approach can generalize to new questions for known relation types with high accuracy, and that zero-shot generalization to unseen relation types is possible, at lower accuracy levels, setting the bar for future work on this task.

### Curated Summary
A zero-shot relation extraction dataset often repurposed as a context-free QA editing benchmark.

## Links

| Type | Link |
|---|---|
| Paper | https://arxiv.org/abs/1706.04115 |
| Dataset | https://nlp.cs.washington.edu/zeroshot/ |

## BibTeX

```bibtex
@misc{https://doi.org/10.48550/arxiv.1706.04115,
  doi = {10.48550/ARXIV.1706.04115},
  url = {https://arxiv.org/abs/1706.04115},
  author = {Levy, Omer and Seo, Minjoon and Choi, Eunsol and Zettlemoyer, Luke},
  keywords = {Computation and Language (cs.CL), Artificial Intelligence (cs.AI), Machine Learning (cs.LG), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {Zero-Shot Relation Extraction via Reading Comprehension},
  publisher = {arXiv},
  year = {2017},
  copyright = {arXiv.org perpetual, non-exclusive license}
}
```

## Remarks

- This card prioritizes official paper pages, project pages, and code repositories. When a link in the original report was incorrect, the corrected official link is used instead.
