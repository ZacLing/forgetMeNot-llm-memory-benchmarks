---
name: LoCoV1
slug: locov1
language: en
category: Retrieval, Embeddings, and RAG
subcategory: 检索与表示学习
memory_type: Semantic / Retrieval-Augmented
year: "2024"
primary_source_kind: paper
primary_source_url: https://arxiv.org/abs/2402.07440
counterpart_zh: ../../zh/03_retrieval_rag/locov1.md
---

# LoCoV1

[English Knowledge Base Index](../README.md) | [中文卡片](../../zh/03_retrieval_rag/locov1.md)

## Structured Metadata

| Field | Content |
|---|---|
| Benchmark | LoCoV1 |
| Category | Retrieval, Embeddings, and RAG |
| Subcategory | 检索与表示学习 |
| Memory Focus | Semantic / Retrieval-Augmented |
| First Year | 2024 |
| Primary Source Type | paper |
| Paper Title | Benchmarking and Building Long-Context Retrieval Models with LoCo and M2-BERT |
| Chinese Card | [LoCoV1](../../zh/03_retrieval_rag/locov1.md) |

## Overview

A long-document retrieval benchmark for encoders where chunking is often ineffective or impossible.

## Abstract
### Original Abstract
> Retrieval pipelines-an integral component of many machine learning systems-perform poorly in domains where documents are long (e.g., 10K tokens or more) and where identifying the relevant document requires synthesizing information across the entire text. Developing long-context retrieval encoders suitable for these domains raises three challenges: (1) how to evaluate long-context retrieval performance, (2) how to pretrain a base language model to represent both short contexts (corresponding to queries) and long contexts (corresponding to documents), and (3) how to fine-tune this model for retrieval under the batch size limitations imposed by GPU memory constraints. To address these challenges, we first introduce LoCoV1, a novel 12 task benchmark constructed to measure long-context retrieval where chunking is not possible or not effective. We next present the M2-BERT retrieval encoder, an 80M parameter state-space encoder model built from the Monarch Mixer architecture, capable of scaling to documents up to 32K tokens long. We describe a pretraining data mixture which allows this encoder to process both short and long context sequences, and a finetuning approach that adapts this base model to retrieval with only single-sample batches. Finally, we validate the M2-BERT retrieval encoder on LoCoV1, finding that it outperforms competitive Transformer-based models by at least 23.3 points, despite containing upwards of 90x fewer parameters.

### Curated Summary
A long-document retrieval benchmark for encoders where chunking is often ineffective or impossible.

## Links

| Type | Link |
|---|---|
| Paper | https://arxiv.org/abs/2402.07440 |
| paper_url_2 | https://proceedings.mlr.press/v235/saad-falcon24a.html |

## BibTeX

```bibtex
@misc{https://doi.org/10.48550/arxiv.2402.07440,
  doi = {10.48550/ARXIV.2402.07440},
  url = {https://arxiv.org/abs/2402.07440},
  author = {Saad-Falcon, Jon and Fu, Daniel Y. and Arora, Simran and Guha, Neel and Ré, Christopher},
  keywords = {Information Retrieval (cs.IR), Machine Learning (cs.LG), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {Benchmarking and Building Long-Context Retrieval Models with LoCo and M2-BERT},
  publisher = {arXiv},
  year = {2024},
  copyright = {Creative Commons Attribution 4.0 International}
}
```

## Remarks

- This card prioritizes official paper pages, project pages, and code repositories. When a link in the original report was incorrect, the corrected official link is used instead.
