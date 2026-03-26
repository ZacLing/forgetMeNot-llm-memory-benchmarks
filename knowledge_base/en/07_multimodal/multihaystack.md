---
name: MultiHaystack
slug: multihaystack
language: en
category: Multimodal Long-Horizon Memory and Retrieval-Reasoning
subcategory: 多图 / 多模态检索推理
memory_type: Multimodal Long-Horizon
year: "2026"
primary_source_kind: paper
primary_source_url: https://arxiv.org/abs/2603.05697
counterpart_zh: ../../zh/07_multimodal/multihaystack.md
---

# MultiHaystack

[English Knowledge Base Index](../README.md) | [中文卡片](../../zh/07_multimodal/multihaystack.md)

## Structured Metadata

| Field | Content |
|---|---|
| Benchmark | MultiHaystack |
| Category | Multimodal Long-Horizon Memory and Retrieval-Reasoning |
| Subcategory | 多图 / 多模态检索推理 |
| Memory Focus | Multimodal Long-Horizon |
| First Year | 2026 |
| Primary Source Type | paper |
| Paper Title | MultiHaystack: Benchmarking Multimodal Retrieval and Reasoning over 40K Images, Videos, and Documents |
| Chinese Card | [MultiHaystack](../../zh/07_multimodal/multihaystack.md) |

## Overview

A multimodal retrieval-and-reasoning benchmark over 46k images, videos, and documents.

## Abstract
### Original Abstract
> Multimodal large language models (MLLMs) achieve strong performance on benchmarks that evaluate text, image, or video understanding separately. However, these settings do not assess a critical real-world requirement, which involves retrieving relevant evidence from large, heterogeneous multimodal corpora prior to reasoning. Most existing benchmarks restrict retrieval to small, single-modality candidate sets, substantially simplifying the search space and overstating end-to-end reliability. To address this gap, we introduce MultiHaystack, the first benchmark designed to evaluate both retrieval and reasoning under large-scale, cross-modal conditions. MultiHaystack comprises over 46,000 multimodal retrieval candidates across documents, images, and videos, along with 747 open yet verifiable questions. Each question is grounded in a unique validated evidence item within the retrieval pool, requiring evidence localization across modalities and fine-grained reasoning. In our study, we find that models perform competitively when provided with the corresponding evidence, but their performance drops sharply when required to retrieve that evidence from the full corpus. Additionally, even the strongest retriever, E5-V, achieves only 40.8% Recall@1, while state-of-the-art MLLMs such as GPT-5 experience a significant drop in reasoning accuracy from 80.86% when provided with the corresponding evidence to 51.4% under top-5 retrieval. These results indicate that multimodal retrieval over heterogeneous pools remains a primary bottleneck for MLLMs, positioning MultiHaystack as a valuable testbed that highlights underlying limitations obscured by small-scale evaluations and promotes retrieval-centric advances in multimodal systems.

### Curated Summary
A multimodal retrieval-and-reasoning benchmark over 46k images, videos, and documents.

## Links

| Type | Link |
|---|---|
| Paper | https://arxiv.org/abs/2603.05697 |
| paper_url_2 | https://openreview.net/forum?id=aiZG7mRi43 |

## BibTeX

```bibtex
@misc{https://doi.org/10.48550/arxiv.2603.05697,
  doi = {10.48550/ARXIV.2603.05697},
  url = {https://arxiv.org/abs/2603.05697},
  author = {Xu, Dannong and Yang, Zhongyu and Chen, Jun and Yuan, Yingfang and Hu, Ming and Sun, Lei and Van Gool, Luc and Paudel, Danda Pani and Feng, Chun-Mei},
  keywords = {Computer Vision and Pattern Recognition (cs.CV), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {MultiHaystack: Benchmarking Multimodal Retrieval and Reasoning over 40K Images, Videos, and Documents},
  publisher = {arXiv},
  year = {2026},
  copyright = {Creative Commons Attribution 4.0 International}
}
```

## Remarks

- This card prioritizes official paper pages, project pages, and code repositories. When a link in the original report was incorrect, the corrected official link is used instead.
