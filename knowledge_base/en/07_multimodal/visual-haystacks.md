---
name: Visual Haystacks
slug: visual-haystacks
language: en
category: Multimodal Long-Horizon Memory and Retrieval-Reasoning
subcategory: Multi-Image / Multimodal Retrieval and Reasoning
memory_type: Multimodal Long-Horizon
year: "2025"
primary_source_kind: paper
primary_source_url: https://arxiv.org/abs/2407.13766
counterpart_zh: ../../zh/07_multimodal/visual-haystacks.md
---

# Visual Haystacks

[English Knowledge Base Index](../README.md) | [中文卡片](../../zh/07_multimodal/visual-haystacks.md)

## Structured Metadata

| Field | Content |
|---|---|
| Benchmark | Visual Haystacks |
| Category | Multimodal Long-Horizon Memory and Retrieval-Reasoning |
| Subcategory | Multi-Image / Multimodal Retrieval and Reasoning |
| Memory Focus | Multimodal Long-Horizon |
| First Year | 2025 |
| Primary Source Type | paper |
| Paper Title | Visual Haystacks: A Vision-Centric Needle-In-A-Haystack Benchmark |
| Chinese Card | [Visual Haystacks](../../zh/07_multimodal/visual-haystacks.md) |

## Overview

A vision-centric needle-in-a-haystack benchmark for retrieval and reasoning over large image sets.

## Abstract
### Original Abstract
> Large Multimodal Models (LMMs) have made significant strides in visual question-answering for single images. Recent advancements like long-context LMMs have allowed them to ingest larger, or even multiple, images. However, the ability to process a large number of visual tokens does not guarantee effective retrieval and reasoning for multi-image question answering (MIQA), especially in real-world applications like photo album searches or satellite imagery analysis. In this work, we first assess the limitations of current benchmarks for long-context LMMs. We address these limitations by introducing a new vision-centric, long-context benchmark, "Visual Haystacks (VHs)". We comprehensively evaluate both open-source and proprietary models on VHs, and demonstrate that these models struggle when reasoning across potentially unrelated images, perform poorly on cross-image reasoning, as well as exhibit biases based on the placement of key information within the context window. Towards a solution, we introduce MIRAGE (Multi-Image Retrieval Augmented Generation), an open-source, lightweight visual-RAG framework that processes up to 10k images on a single 40G A100 GPU -- far surpassing the 1k-image limit of contemporary models. MIRAGE demonstrates up to 13% performance improvement over existing open-source LMMs on VHs, sets a new state-of-the-art on the RetVQA multi-image QA benchmark, and achieves competitive performance on single-image QA with state-of-the-art LMMs. Our dataset, model, and code are available at: https://visual-haystacks.github.io.

### Curated Summary
A vision-centric needle-in-a-haystack benchmark for retrieval and reasoning over large image sets.

## Links

| Type | Link |
|---|---|
| Paper | https://arxiv.org/abs/2407.13766 |
| Project Page | https://visual-haystacks.github.io/ |

## BibTeX

```bibtex
@misc{https://doi.org/10.48550/arxiv.2407.13766,
  doi = {10.48550/ARXIV.2407.13766},
  url = {https://arxiv.org/abs/2407.13766},
  author = {Wu, Tsung-Han and Biamby, Giscard and Quenum, Jerome and Gupta, Ritwik and Gonzalez, Joseph E. and Darrell, Trevor and Chan, David M.},
  keywords = {Computer Vision and Pattern Recognition (cs.CV), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {Visual Haystacks: A Vision-Centric Needle-In-A-Haystack Benchmark},
  publisher = {arXiv},
  year = {2024},
  copyright = {arXiv.org perpetual, non-exclusive license}
}
```

## Remarks

- This card prioritizes official paper pages, project pages, and code repositories. When a link in the original report was incorrect, the corrected official link is used instead.
