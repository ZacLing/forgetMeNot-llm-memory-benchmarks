---
name: MTEB
slug: mteb
language: en
category: Retrieval, Embeddings, and RAG
subcategory: Retrieval and Representation Learning
memory_type: Semantic / Retrieval-Augmented
year: "2023"
primary_source_kind: paper
primary_source_url: https://arxiv.org/abs/2210.07316
counterpart_zh: ../../zh/03_retrieval_rag/mteb.md
---

# MTEB

[English Knowledge Base Index](../README.md) | [中文卡片](../../zh/03_retrieval_rag/mteb.md)

## Structured Metadata

| Field | Content |
|---|---|
| Benchmark | MTEB |
| Category | Retrieval, Embeddings, and RAG |
| Subcategory | Retrieval and Representation Learning |
| Memory Focus | Semantic / Retrieval-Augmented |
| First Year | 2023 |
| Primary Source Type | paper |
| Paper Title | MTEB: Massive Text Embedding Benchmark |
| Chinese Card | [MTEB](../../zh/03_retrieval_rag/mteb.md) |

## Overview

A large-scale general text-embedding benchmark covering multiple tasks, datasets, and languages.

## Abstract
### Original Abstract
> Text embeddings are commonly evaluated on a small set of datasets from a single task not covering their possible applications to other tasks. It is unclear whether state-of-the-art embeddings on semantic textual similarity (STS) can be equally well applied to other tasks like clustering or reranking. This makes progress in the field difficult to track, as various models are constantly being proposed without proper evaluation. To solve this problem, we introduce the Massive Text Embedding Benchmark (MTEB). MTEB spans 8 embedding tasks covering a total of 58 datasets and 112 languages. Through the benchmarking of 33 models on MTEB, we establish the most comprehensive benchmark of text embeddings to date. We find that no particular text embedding method dominates across all tasks. This suggests that the field has yet to converge on a universal text embedding method and scale it up sufficiently to provide state-of-the-art results on all embedding tasks. MTEB comes with open-source code and a public leaderboard at https://github.com/embeddings-benchmark/mteb.

### Curated Summary
A large-scale general text-embedding benchmark covering multiple tasks, datasets, and languages.

## Links

| Type | Link |
|---|---|
| Paper | https://arxiv.org/abs/2210.07316 |
| GitHub | https://github.com/embeddings-benchmark/mteb |

## BibTeX

```bibtex
@misc{https://doi.org/10.48550/arxiv.2210.07316,
  doi = {10.48550/ARXIV.2210.07316},
  url = {https://arxiv.org/abs/2210.07316},
  author = {Muennighoff, Niklas and Tazi, Nouamane and Magne, Loïc and Reimers, Nils},
  keywords = {Computation and Language (cs.CL), Information Retrieval (cs.IR), Machine Learning (cs.LG), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {MTEB: Massive Text Embedding Benchmark},
  publisher = {arXiv},
  year = {2022},
  copyright = {arXiv.org perpetual, non-exclusive license}
}
```

## Remarks

- This card prioritizes official paper pages, project pages, and code repositories. When a link in the original report was incorrect, the corrected official link is used instead.
