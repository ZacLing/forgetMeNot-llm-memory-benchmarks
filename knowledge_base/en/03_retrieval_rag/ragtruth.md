---
name: RAGTruth
slug: ragtruth
language: en
category: Retrieval, Embeddings, and RAG
subcategory: 端到端 RAG 与忠实性
memory_type: Semantic / Retrieval-Augmented
year: "2024"
primary_source_kind: paper
primary_source_url: https://arxiv.org/abs/2401.00396
counterpart_zh: ../../zh/03_retrieval_rag/ragtruth.md
---

# RAGTruth

[English Knowledge Base Index](../README.md) | [中文卡片](../../zh/03_retrieval_rag/ragtruth.md)

## Structured Metadata

| Field | Content |
|---|---|
| Benchmark | RAGTruth |
| Category | Retrieval, Embeddings, and RAG |
| Subcategory | 端到端 RAG 与忠实性 |
| Memory Focus | Semantic / Retrieval-Augmented |
| First Year | 2024 |
| Primary Source Type | paper |
| Paper Title | RAGTruth: A Hallucination Corpus for Developing Trustworthy Retrieval-Augmented Language Models |
| Chinese Card | [RAGTruth](../../zh/03_retrieval_rag/ragtruth.md) |

## Overview

A hallucination corpus for RAG that provides case-level and word-level faithfulness annotations.

## Abstract
### Original Abstract
> Retrieval-augmented generation (RAG) has become a main technique for alleviating hallucinations in large language models (LLMs). Despite the integration of RAG, LLMs may still present unsupported or contradictory claims to the retrieved contents. In order to develop effective hallucination prevention strategies under RAG, it is important to create benchmark datasets that can measure the extent of hallucination. This paper presents RAGTruth, a corpus tailored for analyzing word-level hallucinations in various domains and tasks within the standard RAG frameworks for LLM applications. RAGTruth comprises nearly 18,000 naturally generated responses from diverse LLMs using RAG. These responses have undergone meticulous manual annotations at both the individual cases and word levels, incorporating evaluations of hallucination intensity. We not only benchmark hallucination frequencies across different LLMs, but also critically assess the effectiveness of several existing hallucination detection methodologies. Furthermore, we show that using a high-quality dataset such as RAGTruth, it is possible to finetune a relatively small LLM and achieve a competitive level of performance in hallucination detection when compared to the existing prompt-based approaches using state-of-the-art large language models such as GPT-4.

### Curated Summary
A hallucination corpus for RAG that provides case-level and word-level faithfulness annotations.

## Links

| Type | Link |
|---|---|
| Paper | https://arxiv.org/abs/2401.00396 |
| GitHub | https://github.com/ParticleMedia/RAGTruth |
| paper_url_2 | https://aclanthology.org/2024.acl-long.585/ |

## BibTeX

```bibtex
@misc{https://doi.org/10.48550/arxiv.2401.00396,
  doi = {10.48550/ARXIV.2401.00396},
  url = {https://arxiv.org/abs/2401.00396},
  author = {Niu, Cheng and Wu, Yuanhao and Zhu, Juno and Xu, Siliang and Shum, Kashun and Zhong, Randy and Song, Juntong and Zhang, Tong},
  keywords = {Computation and Language (cs.CL), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {RAGTruth: A Hallucination Corpus for Developing Trustworthy Retrieval-Augmented Language Models},
  publisher = {arXiv},
  year = {2024},
  copyright = {arXiv.org perpetual, non-exclusive license}
}
```

## Remarks

- This card prioritizes official paper pages, project pages, and code repositories. When a link in the original report was incorrect, the corrected official link is used instead.
