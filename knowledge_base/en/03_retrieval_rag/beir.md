---
name: BEIR
slug: beir
language: en
category: Retrieval, Embeddings, and RAG
subcategory: 检索与表示学习
memory_type: Semantic / Retrieval-Augmented
year: "2021"
primary_source_kind: paper
primary_source_url: https://arxiv.org/abs/2104.08663
counterpart_zh: ../../zh/03_retrieval_rag/beir.md
---

# BEIR

[English Knowledge Base Index](../README.md) | [中文卡片](../../zh/03_retrieval_rag/beir.md)

## Structured Metadata

| Field | Content |
|---|---|
| Benchmark | BEIR |
| Category | Retrieval, Embeddings, and RAG |
| Subcategory | 检索与表示学习 |
| Memory Focus | Semantic / Retrieval-Augmented |
| First Year | 2021 |
| Primary Source Type | paper |
| Paper Title | BEIR: A Heterogenous Benchmark for Zero-shot Evaluation of Information Retrieval Models |
| Chinese Card | [BEIR](../../zh/03_retrieval_rag/beir.md) |

## Overview

A heterogeneous zero-shot retrieval benchmark for evaluating generalization across 18 IR datasets.

## Abstract
### Original Abstract
> Existing neural information retrieval (IR) models have often been studied in homogeneous and narrow settings, which has considerably limited insights into their out-of-distribution (OOD) generalization capabilities. To address this, and to facilitate researchers to broadly evaluate the effectiveness of their models, we introduce Benchmarking-IR (BEIR), a robust and heterogeneous evaluation benchmark for information retrieval. We leverage a careful selection of 18 publicly available datasets from diverse text retrieval tasks and domains and evaluate 10 state-of-the-art retrieval systems including lexical, sparse, dense, late-interaction and re-ranking architectures on the BEIR benchmark. Our results show BM25 is a robust baseline and re-ranking and late-interaction-based models on average achieve the best zero-shot performances, however, at high computational costs. In contrast, dense and sparse-retrieval models are computationally more efficient but often underperform other approaches, highlighting the considerable room for improvement in their generalization capabilities. We hope this framework allows us to better evaluate and understand existing retrieval systems, and contributes to accelerating progress towards better robust and generalizable systems in the future. BEIR is publicly available at https://github.com/UKPLab/beir.

### Curated Summary
A heterogeneous zero-shot retrieval benchmark for evaluating generalization across 18 IR datasets.

## Links

| Type | Link |
|---|---|
| Paper | https://arxiv.org/abs/2104.08663 |
| GitHub | https://github.com/UKPLab/beir |

## BibTeX

```bibtex
@misc{https://doi.org/10.48550/arxiv.2104.08663,
  doi = {10.48550/ARXIV.2104.08663},
  url = {https://arxiv.org/abs/2104.08663},
  author = {Thakur, Nandan and Reimers, Nils and Rücklé, Andreas and Srivastava, Abhishek and Gurevych, Iryna},
  keywords = {Information Retrieval (cs.IR), Artificial Intelligence (cs.AI), Computation and Language (cs.CL), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {BEIR: A Heterogenous Benchmark for Zero-shot Evaluation of Information Retrieval Models},
  publisher = {arXiv},
  year = {2021},
  copyright = {Creative Commons Attribution Share Alike 4.0 International}
}
```

## Remarks

- This card prioritizes official paper pages, project pages, and code repositories. When a link in the original report was incorrect, the corrected official link is used instead.
