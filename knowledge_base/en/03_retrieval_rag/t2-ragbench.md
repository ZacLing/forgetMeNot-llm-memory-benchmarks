---
name: T2-RAGBench
slug: t2-ragbench
language: en
category: Retrieval, Embeddings, and RAG
subcategory: End-to-End RAG and Faithfulness
memory_type: Semantic / Retrieval-Augmented
year: "2026"
primary_source_kind: paper
primary_source_url: https://arxiv.org/abs/2506.12071
counterpart_zh: ../../zh/03_retrieval_rag/t2-ragbench.md
---

# T2-RAGBench

[English Knowledge Base Index](../README.md) | [中文卡片](../../zh/03_retrieval_rag/t2-ragbench.md)

## Structured Metadata

| Field | Content |
|---|---|
| Benchmark | T2-RAGBench |
| Category | Retrieval, Embeddings, and RAG |
| Subcategory | End-to-End RAG and Faithfulness |
| Memory Focus | Semantic / Retrieval-Augmented |
| First Year | 2026 |
| Primary Source Type | paper |
| Paper Title | T$^2$-RAGBench: Text-and-Table Benchmark for Evaluating Retrieval-Augmented Generation |
| Chinese Card | [T2-RAGBench](../../zh/03_retrieval_rag/t2-ragbench.md) |

## Overview

A text-and-table RAG benchmark with 23,088 context-independent triples for retrieval plus numerical reasoning.

## Abstract
### Original Abstract
> Since many real-world documents combine textual and tabular data, robust Retrieval Augmented Generation (RAG) systems are essential for effectively accessing and analyzing such content to support complex reasoning tasks. Therefore, this paper introduces $\textbf{$T^2$-RAGBench}$, a benchmark comprising $\textbf{23,088}$ question-context-answer triples, designed to evaluate RAG methods on real-world text-and-table data. Unlike typical QA datasets that operate under $\textit{Oracle Context}$ settings, $\textbf{$T^2$-RAGBench}$ challenges models to first retrieve the correct context before conducting numerical reasoning. Existing QA datasets containing text-and-table data typically contain context-dependent questions, which may yield multiple correct answers depending on the provided context. To address this, we transform SOTA datasets into a context-independent format, validated by experts as 91.3% context-independent questions, enabling reliable RAG evaluation. Our comprehensive evaluation identifies $\textit{Hybrid BM25}$ , a technique that combines dense and sparse vectors, as the most effective approach for text-and-table data. However, results demonstrate that $\textbf{$T^2$-RAGBench}$ remains challenging even for SOTA LLMs and RAG methods. Further ablation studies examine the impact of embedding models and corpus size on retrieval performance. $\textbf{$T^2$-RAGBench}$ provides a realistic and rigorous benchmark for existing RAG methods on text-and-table data. Code and dataset are available online: https://github.com/uhh-hcds/g4kmu-paper

### Curated Summary
A text-and-table RAG benchmark with 23,088 context-independent triples for retrieval plus numerical reasoning.

## Links

| Type | Link |
|---|---|
| Paper | https://arxiv.org/abs/2506.12071 |

## BibTeX

```bibtex
@misc{https://doi.org/10.48550/arxiv.2506.12071,
  doi = {10.48550/ARXIV.2506.12071},
  url = {https://arxiv.org/abs/2506.12071},
  author = {Strich, Jan and Isgorur, Enes Kutay and Trescher, Maximilian and Biemann, Chris and Semmann, Martin},
  keywords = {Information Retrieval (cs.IR), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {T$^2$-RAGBench: Text-and-Table Benchmark for Evaluating Retrieval-Augmented Generation},
  publisher = {arXiv},
  year = {2025},
  copyright = {Creative Commons Attribution 4.0 International}
}
```

## Remarks

- This card prioritizes official paper pages, project pages, and code repositories. When a link in the original report was incorrect, the corrected official link is used instead.
