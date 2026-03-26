---
name: KILT
slug: kilt
language: en
category: Retrieval, Embeddings, and RAG
subcategory: Retrieval and Representation Learning
memory_type: Semantic / Retrieval-Augmented
year: "2021"
primary_source_kind: paper
primary_source_url: https://arxiv.org/abs/2009.02252
counterpart_zh: ../../zh/03_retrieval_rag/kilt.md
---

# KILT

[English Knowledge Base Index](../README.md) | [中文卡片](../../zh/03_retrieval_rag/kilt.md)

## Structured Metadata

| Field | Content |
|---|---|
| Benchmark | KILT |
| Category | Retrieval, Embeddings, and RAG |
| Subcategory | Retrieval and Representation Learning |
| Memory Focus | Semantic / Retrieval-Augmented |
| First Year | 2021 |
| Primary Source Type | paper |
| Paper Title | KILT: a Benchmark for Knowledge Intensive Language Tasks |
| Chinese Card | [KILT](../../zh/03_retrieval_rag/kilt.md) |

## Overview

A knowledge-intensive benchmark that unifies multiple tasks over a shared Wikipedia snapshot and provenance evaluation.

## Abstract
### Original Abstract
> Challenging problems such as open-domain question answering, fact checking, slot filling and entity linking require access to large, external knowledge sources. While some models do well on individual tasks, developing general models is difficult as each task might require computationally expensive indexing of custom knowledge sources, in addition to dedicated infrastructure. To catalyze research on models that condition on specific information in large textual resources, we present a benchmark for knowledge-intensive language tasks (KILT). All tasks in KILT are grounded in the same snapshot of Wikipedia, reducing engineering turnaround through the re-use of components, as well as accelerating research into task-agnostic memory architectures. We test both task-specific and general baselines, evaluating downstream performance in addition to the ability of the models to provide provenance. We find that a shared dense vector index coupled with a seq2seq model is a strong baseline, outperforming more tailor-made approaches for fact checking, open-domain question answering and dialogue, and yielding competitive results on entity linking and slot filling, by generating disambiguated text. KILT data and code are available at https://github.com/facebookresearch/KILT.

### Curated Summary
A knowledge-intensive benchmark that unifies multiple tasks over a shared Wikipedia snapshot and provenance evaluation.

## Links

| Type | Link |
|---|---|
| Paper | https://arxiv.org/abs/2009.02252 |
| GitHub | https://github.com/facebookresearch/KILT |

## BibTeX

```bibtex
@misc{https://doi.org/10.48550/arxiv.2009.02252,
  doi = {10.48550/ARXIV.2009.02252},
  url = {https://arxiv.org/abs/2009.02252},
  author = {Petroni, Fabio and Piktus, Aleksandra and Fan, Angela and Lewis, Patrick and Yazdani, Majid and De Cao, Nicola and Thorne, James and Jernite, Yacine and Karpukhin, Vladimir and Maillard, Jean and Plachouras, Vassilis and Rocktäschel, Tim and Riedel, Sebastian},
  keywords = {Computation and Language (cs.CL), Artificial Intelligence (cs.AI), Information Retrieval (cs.IR), Machine Learning (cs.LG), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {KILT: a Benchmark for Knowledge Intensive Language Tasks},
  publisher = {arXiv},
  year = {2020},
  copyright = {arXiv.org perpetual, non-exclusive license}
}
```

## Remarks

- This card prioritizes official paper pages, project pages, and code repositories. When a link in the original report was incorrect, the corrected official link is used instead.
