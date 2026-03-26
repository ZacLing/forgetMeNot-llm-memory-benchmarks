---
name: GraphRAG-Bench
slug: graphrag-bench
language: en
category: Retrieval, Embeddings, and RAG
subcategory: End-to-End RAG and Faithfulness
memory_type: Semantic / Retrieval-Augmented
year: "2025"
primary_source_kind: paper
primary_source_url: https://arxiv.org/abs/2506.02404
counterpart_zh: ../../zh/03_retrieval_rag/graphrag-bench.md
---

# GraphRAG-Bench

[English Knowledge Base Index](../README.md) | [中文卡片](../../zh/03_retrieval_rag/graphrag-bench.md)

## Structured Metadata

| Field | Content |
|---|---|
| Benchmark | GraphRAG-Bench |
| Category | Retrieval, Embeddings, and RAG |
| Subcategory | End-to-End RAG and Faithfulness |
| Memory Focus | Semantic / Retrieval-Augmented |
| First Year | 2025 |
| Primary Source Type | paper |
| Paper Title | GraphRAG-Bench: Challenging Domain-Specific Reasoning for Evaluating Graph Retrieval-Augmented Generation |
| Chinese Card | [GraphRAG-Bench](../../zh/03_retrieval_rag/graphrag-bench.md) |

## Overview

A full-pipeline GraphRAG benchmark over textbook corpora that evaluates construction, retrieval, generation, and reasoning coherence.

## Abstract
### Original Abstract
> Graph Retrieval Augmented Generation (GraphRAG) has garnered increasing recognition for its potential to enhance large language models (LLMs) by structurally organizing domain-specific corpora and facilitating complex reasoning. However, current evaluations of GraphRAG models predominantly rely on traditional question-answering datasets. Their limited scope in questions and evaluation metrics fails to comprehensively assess the reasoning capacity improvements enabled by GraphRAG models. To address this gap, we introduce GraphRAG-Bench, a large-scale, domain-specific benchmark designed to rigorously evaluate GraphRAG models. Our benchmark offers three key superiorities: \((i)\) Challenging question design. Featuring college-level, domain-specific questions that demand multi-hop reasoning, the benchmark ensures that simple content retrieval is insufficient for problem-solving. For example, some questions require mathematical reasoning or programming. \((ii)\) Diverse task coverage. The dataset includes a broad spectrum of reasoning tasks, multiple-choice, true/false, multi-select, open-ended, and fill-in-the-blank. It spans 16 disciplines in twenty core textbooks. \((iii)\) Holistic evaluation framework. GraphRAG-Bench provides comprehensive assessment across the entire GraphRAG pipeline, including graph construction, knowledge retrieval, and answer generation. Beyond final-answer correctness, it evaluates the logical coherence of the reasoning process. By applying nine contemporary GraphRAG methods to GraphRAG-Bench, we demonstrate its utility in quantifying how graph-based structuring improves model reasoning capabilities. Our analysis reveals critical insights about graph architectures, retrieval efficacy, and reasoning capabilities, offering actionable guidance for the research community.

### Curated Summary
A full-pipeline GraphRAG benchmark over textbook corpora that evaluates construction, retrieval, generation, and reasoning coherence.

## Links

| Type | Link |
|---|---|
| Paper | https://arxiv.org/abs/2506.02404 |
| GitHub | https://github.com/GraphRAG-Bench/GraphRAG-Benchmark |
| Dataset | https://huggingface.co/datasets/GraphRAG-Bench/GraphRAG-Bench |

## BibTeX

```bibtex
@misc{https://doi.org/10.48550/arxiv.2506.02404,
  doi = {10.48550/ARXIV.2506.02404},
  url = {https://arxiv.org/abs/2506.02404},
  author = {Xiao, Yilin and Dong, Junnan and Zhou, Chuang and Dong, Su and Zhang, Qian-wen and Yin, Di and Sun, Xing and Huang, Xiao},
  keywords = {Computation and Language (cs.CL), Artificial Intelligence (cs.AI), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {GraphRAG-Bench: Challenging Domain-Specific Reasoning for Evaluating Graph Retrieval-Augmented Generation},
  publisher = {arXiv},
  year = {2025},
  copyright = {arXiv.org perpetual, non-exclusive license}
}
```

## Remarks

- This card prioritizes official paper pages, project pages, and code repositories. When a link in the original report was incorrect, the corrected official link is used instead.
