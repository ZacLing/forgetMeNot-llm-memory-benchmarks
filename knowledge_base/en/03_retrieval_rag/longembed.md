---
name: LongEmbed
slug: longembed
language: en
category: Retrieval, Embeddings, and RAG
subcategory: 检索与表示学习
memory_type: Semantic / Retrieval-Augmented
year: "2024"
primary_source_kind: paper
primary_source_url: https://arxiv.org/abs/2404.12096
counterpart_zh: ../../zh/03_retrieval_rag/longembed.md
---

# LongEmbed

[English Knowledge Base Index](../README.md) | [中文卡片](../../zh/03_retrieval_rag/longembed.md)

## Structured Metadata

| Field | Content |
|---|---|
| Benchmark | LongEmbed |
| Category | Retrieval, Embeddings, and RAG |
| Subcategory | 检索与表示学习 |
| Memory Focus | Semantic / Retrieval-Augmented |
| First Year | 2024 |
| Primary Source Type | paper |
| Paper Title | LongEmbed: Extending Embedding Models for Long Context Retrieval |
| Chinese Card | [LongEmbed](../../zh/03_retrieval_rag/longembed.md) |

## Overview

A benchmark for extending embedding models from short contexts to long-context retrieval up to 32k tokens.

## Abstract
### Original Abstract
> Embedding models play a pivot role in modern NLP applications such as IR and RAG. While the context limit of LLMs has been pushed beyond 1 million tokens, embedding models are still confined to a narrow context window not exceeding 8k tokens, refrained from application scenarios requiring long inputs such as legal contracts. This paper explores context window extension of existing embedding models, pushing the limit to 32k without requiring additional training. First, we examine the performance of current embedding models for long context retrieval on our newly constructed LongEmbed benchmark. LongEmbed comprises two synthetic tasks and four carefully chosen real-world tasks, featuring documents of varying length and dispersed target information. Benchmarking results underscore huge room for improvement in these models. Based on this, comprehensive experiments show that training-free context window extension strategies like position interpolation can effectively extend the context window of existing embedding models by several folds, regardless of their original context being 512 or beyond 4k. Furthermore, for models employing absolute position encoding (APE), we show the possibility of further fine-tuning to harvest notable performance gains while strictly preserving original behavior for short inputs. For models using rotary position embedding (RoPE), significant enhancements are observed when employing RoPE-specific methods, such as NTK and SelfExtend, indicating RoPE's superiority over APE for context window extension. To facilitate future research, we release E5-Base-4k and E5-RoPE-Base, along with the LongEmbed benchmark.

### Curated Summary
A benchmark for extending embedding models from short contexts to long-context retrieval up to 32k tokens.

## Links

| Type | Link |
|---|---|
| Paper | https://arxiv.org/abs/2404.12096 |
| GitHub | https://github.com/dwzhu-pku/LongEmbed |
| other_emnlp-pdf_url | https://aclanthology.org/2024.emnlp-main.47.pdf |

## BibTeX

```bibtex
@misc{https://doi.org/10.48550/arxiv.2404.12096,
  doi = {10.48550/ARXIV.2404.12096},
  url = {https://arxiv.org/abs/2404.12096},
  author = {Zhu, Dawei and Wang, Liang and Yang, Nan and Song, Yifan and Wu, Wenhao and Wei, Furu and Li, Sujian},
  keywords = {Computation and Language (cs.CL), Machine Learning (cs.LG), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {LongEmbed: Extending Embedding Models for Long Context Retrieval},
  publisher = {arXiv},
  year = {2024},
  copyright = {Creative Commons Attribution 4.0 International}
}
```

## Remarks

- This card prioritizes official paper pages, project pages, and code repositories. When a link in the original report was incorrect, the corrected official link is used instead.
