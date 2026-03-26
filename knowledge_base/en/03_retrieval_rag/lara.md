---
name: LaRA
slug: lara
language: en
category: Retrieval, Embeddings, and RAG
subcategory: End-to-End RAG and Faithfulness
memory_type: Semantic / Retrieval-Augmented
year: "2025"
primary_source_kind: paper
primary_source_url: https://arxiv.org/abs/2502.09977
counterpart_zh: ../../zh/03_retrieval_rag/lara.md
---

# LaRA

[English Knowledge Base Index](../README.md) | [中文卡片](../../zh/03_retrieval_rag/lara.md)

## Structured Metadata

| Field | Content |
|---|---|
| Benchmark | LaRA |
| Category | Retrieval, Embeddings, and RAG |
| Subcategory | End-to-End RAG and Faithfulness |
| Memory Focus | Semantic / Retrieval-Augmented |
| First Year | 2025 |
| Primary Source Type | paper |
| Paper Title | LaRA: Benchmarking Retrieval-Augmented Generation and Long-Context LLMs -- No Silver Bullet for LC or RAG Routing |
| Chinese Card | [LaRA](../../zh/03_retrieval_rag/lara.md) |

## Overview

A benchmark for comparing long-context LLMs and RAG systems under the same realistic QA settings.

## Abstract
### Original Abstract
> Effectively incorporating external knowledge into Large Language Models (LLMs) is crucial for enhancing their capabilities and addressing real-world needs. Retrieval-Augmented Generation (RAG) offers an effective method for achieving this by retrieving the most relevant fragments into LLMs. However, the advancements in context window size for LLMs offer an alternative approach, raising the question of whether RAG remains necessary for effectively handling external knowledge. Several existing studies provide inconclusive comparisons between RAG and long-context (LC) LLMs, largely due to limitations in the benchmark designs. In this paper, we present LaRA, a novel benchmark specifically designed to rigorously compare RAG and LC LLMs. LaRA encompasses 2326 test cases across four practical QA task categories and three types of naturally occurring long texts. Through systematic evaluation of seven open-source and four proprietary LLMs, we find that the optimal choice between RAG and LC depends on a complex interplay of factors, including the model's parameter size, long-text capabilities, context length, task type, and the characteristics of the retrieved chunks. Our findings provide actionable guidelines for practitioners to effectively leverage both RAG and LC approaches in developing and deploying LLM applications. Our code and dataset is provided at: \href{https://github.com/Alibaba-NLP/LaRA}{\textbf{https://github.com/Alibaba-NLP/LaRA}}.

### Curated Summary
A benchmark for comparing long-context LLMs and RAG systems under the same realistic QA settings.

## Links

| Type | Link |
|---|---|
| Paper | https://arxiv.org/abs/2502.09977 |
| GitHub | https://github.com/Alibaba-NLP/LaRA |

## BibTeX

```bibtex
@misc{https://doi.org/10.48550/arxiv.2502.09977,
  doi = {10.48550/ARXIV.2502.09977},
  url = {https://arxiv.org/abs/2502.09977},
  author = {Li, Kuan and Zhang, Liwen and Jiang, Yong and Xie, Pengjun and Huang, Fei and Wang, Shuai and Cheng, Minhao},
  keywords = {Computation and Language (cs.CL), Artificial Intelligence (cs.AI), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {LaRA: Benchmarking Retrieval-Augmented Generation and Long-Context LLMs -- No Silver Bullet for LC or RAG Routing},
  publisher = {arXiv},
  year = {2025},
  copyright = {Creative Commons Attribution Non Commercial Share Alike 4.0 International}
}
```

## Remarks

- This card prioritizes official paper pages, project pages, and code repositories. When a link in the original report was incorrect, the corrected official link is used instead.
