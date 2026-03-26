---
name: RAGBench
slug: ragbench
language: en
category: Retrieval, Embeddings, and RAG
subcategory: End-to-End RAG and Faithfulness
memory_type: Semantic / Retrieval-Augmented
year: "2025"
primary_source_kind: paper
primary_source_url: https://arxiv.org/abs/2407.11005
counterpart_zh: ../../zh/03_retrieval_rag/ragbench.md
---

# RAGBench

[English Knowledge Base Index](../README.md) | [中文卡片](../../zh/03_retrieval_rag/ragbench.md)

## Structured Metadata

| Field | Content |
|---|---|
| Benchmark | RAGBench |
| Category | Retrieval, Embeddings, and RAG |
| Subcategory | End-to-End RAG and Faithfulness |
| Memory Focus | Semantic / Retrieval-Augmented |
| First Year | 2025 |
| Primary Source Type | paper |
| Paper Title | RAGBench: Explainable Benchmark for Retrieval-Augmented Generation Systems |
| Chinese Card | [RAGBench](../../zh/03_retrieval_rag/ragbench.md) |

## Overview

An explainable end-to-end RAG benchmark with large-scale industrial-style data and annotated failure modes.

## Abstract
### Original Abstract
> Retrieval-Augmented Generation (RAG) has become a standard architectural pattern for incorporating domain-specific knowledge into user-facing chat applications powered by Large Language Models (LLMs). RAG systems are characterized by (1) a document retriever that queries a domain-specific corpus for context information relevant to an input query, and (2) an LLM that generates a response based on the provided query and context. However, comprehensive evaluation of RAG systems remains a challenge due to the lack of unified evaluation criteria and annotated datasets. In response, we introduce RAGBench: the first comprehensive, large-scale RAG benchmark dataset of 100k examples. It covers five unique industry-specific domains and various RAG task types. RAGBench examples are sourced from industry corpora such as user manuals, making it particularly relevant for industry applications. Further, we formalize the TRACe evaluation framework: a set of explainable and actionable RAG evaluation metrics applicable across all RAG domains. We release the labeled dataset at https://huggingface.co/datasets/rungalileo/ragbench. RAGBench explainable labels facilitate holistic evaluation of RAG systems, enabling actionable feedback for continuous improvement of production applications. Thorough extensive benchmarking, we find that LLM-based RAG evaluation methods struggle to compete with a finetuned RoBERTa model on the RAG evaluation task. We identify areas where existing approaches fall short and propose the adoption of RAGBench with TRACe towards advancing the state of RAG evaluation systems.

### Curated Summary
An explainable end-to-end RAG benchmark with large-scale industrial-style data and annotated failure modes.

## Links

| Type | Link |
|---|---|
| Paper | https://arxiv.org/abs/2407.11005 |
| paper_url_2 | https://arxiv.org/html/2407.11005v1 |

## BibTeX

```bibtex
@misc{https://doi.org/10.48550/arxiv.2407.11005,
  doi = {10.48550/ARXIV.2407.11005},
  url = {https://arxiv.org/abs/2407.11005},
  author = {Friel, Robert and Belyi, Masha and Sanyal, Atindriyo},
  keywords = {Computation and Language (cs.CL), Artificial Intelligence (cs.AI), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {RAGBench: Explainable Benchmark for Retrieval-Augmented Generation Systems},
  publisher = {arXiv},
  year = {2024},
  copyright = {Creative Commons Attribution 4.0 International}
}
```

## Remarks

- This card prioritizes official paper pages, project pages, and code repositories. When a link in the original report was incorrect, the corrected official link is used instead.
