---
name: DocHaystack
slug: dochaystack
language: en
category: Multimodal Long-Horizon Memory and Retrieval-Reasoning
subcategory: 长文档与视觉文档
memory_type: Multimodal Long-Horizon
year: "2024"
primary_source_kind: paper
primary_source_url: https://arxiv.org/abs/2411.16740
counterpart_zh: ../../zh/07_multimodal/dochaystack.md
---

# DocHaystack

[English Knowledge Base Index](../README.md) | [中文卡片](../../zh/07_multimodal/dochaystack.md)

## Structured Metadata

| Field | Content |
|---|---|
| Benchmark | DocHaystack |
| Category | Multimodal Long-Horizon Memory and Retrieval-Reasoning |
| Subcategory | 长文档与视觉文档 |
| Memory Focus | Multimodal Long-Horizon |
| First Year | 2024 |
| Primary Source Type | paper |
| Paper Title | Document Haystacks: Vision-Language Reasoning Over Piles of 1000+ Documents |
| Chinese Card | [DocHaystack](../../zh/07_multimodal/dochaystack.md) |

## Overview

A visual document reasoning benchmark over piles of up to 1,000 documents.

## Abstract
### Original Abstract
> Large multimodal models (LMMs) have achieved impressive progress in vision-language understanding, yet they face limitations in real-world applications requiring complex reasoning over a large number of images. Existing benchmarks for multi-image question-answering are limited in scope, each question is paired with only up to 30 images, which does not fully capture the demands of large-scale retrieval tasks encountered in the real-world usages. To reduce these gaps, we introduce two document haystack benchmarks, dubbed DocHaystack and InfoHaystack, designed to evaluate LMM performance on large-scale visual document retrieval and understanding. Additionally, we propose V-RAG, a novel, vision-centric retrieval-augmented generation (RAG) framework that leverages a suite of multimodal vision encoders, each optimized for specific strengths, and a dedicated question-document relevance module. V-RAG sets a new standard, with a 9% and 11% improvement in Recall@1 on the challenging DocHaystack-1000 and InfoHaystack-1000 benchmarks, respectively, compared to the previous best baseline models. Additionally, integrating V-RAG with LMMs enables them to efficiently operate across thousands of images, yielding significant improvements on our DocHaystack and InfoHaystack benchmarks. Our code and datasets are available at https://github.com/Vision-CAIR/dochaystacks

### Curated Summary
A visual document reasoning benchmark over piles of up to 1,000 documents.

## Links

| Type | Link |
|---|---|
| Paper | https://arxiv.org/abs/2411.16740 |
| GitHub | https://github.com/Vision-CAIR/dochaystacks |

## BibTeX

```bibtex
@misc{https://doi.org/10.48550/arxiv.2411.16740,
  doi = {10.48550/ARXIV.2411.16740},
  url = {https://arxiv.org/abs/2411.16740},
  author = {Chen, Jun and Xu, Dannong and Fei, Junjie and Feng, Chun-Mei and Elhoseiny, Mohamed},
  keywords = {Computer Vision and Pattern Recognition (cs.CV), Artificial Intelligence (cs.AI), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {Document Haystacks: Vision-Language Reasoning Over Piles of 1000+ Documents},
  publisher = {arXiv},
  year = {2024},
  copyright = {Creative Commons Attribution 4.0 International}
}
```

## Remarks

- This card prioritizes official paper pages, project pages, and code repositories. When a link in the original report was incorrect, the corrected official link is used instead.
