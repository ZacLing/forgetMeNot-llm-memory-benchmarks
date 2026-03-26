---
name: MMNeedle
slug: mmneedle
language: en
category: Multimodal Long-Horizon Memory and Retrieval-Reasoning
subcategory: 多图 / 多模态检索推理
memory_type: Multimodal Long-Horizon
year: "2025"
primary_source_kind: paper
primary_source_url: https://arxiv.org/abs/2406.11230
counterpart_zh: ../../zh/07_multimodal/mmneedle.md
---

# MMNeedle

[English Knowledge Base Index](../README.md) | [中文卡片](../../zh/07_multimodal/mmneedle.md)

## Structured Metadata

| Field | Content |
|---|---|
| Benchmark | MMNeedle |
| Category | Multimodal Long-Horizon Memory and Retrieval-Reasoning |
| Subcategory | 多图 / 多模态检索推理 |
| Memory Focus | Multimodal Long-Horizon |
| First Year | 2025 |
| Primary Source Type | paper |
| Paper Title | Multimodal Needle in a Haystack: Benchmarking Long-Context Capability of Multimodal Large Language Models |
| Chinese Card | [MMNeedle](../../zh/07_multimodal/mmneedle.md) |

## Overview

A multi-image needle benchmark that stresses sub-image localization and negative-sample hallucination.

## Abstract
### Original Abstract
> Multimodal Large Language Models (MLLMs) have shown significant promise in various applications, leading to broad interest from researchers and practitioners alike. However, a comprehensive evaluation of their long-context capabilities remains underexplored. To address these gaps, we introduce the MultiModal Needle-in-a-haystack (MMNeedle) benchmark, specifically designed to assess the long-context capabilities of MLLMs. Besides multi-image input, we employ image stitching to further increase the input context length, and develop a protocol to automatically generate labels for sub-image level retrieval. Essentially, MMNeedle evaluates MLLMs by stress-testing their capability to locate a target sub-image (needle) within a set of images (haystack) based on textual instructions and descriptions of image contents. This setup necessitates an advanced understanding of extensive visual contexts and effective information retrieval within long-context image inputs. With this benchmark, we evaluate state-of-the-art MLLMs, encompassing both API-based and open-source models. The findings reveal that GPT-4o consistently surpasses other models in long-context scenarios, but suffers from hallucination problems in negative samples, i.e., when needles are not in the haystacks. Our comprehensive long-context evaluation of MLLMs also sheds lights on the considerable performance gap between API-based and open-source models. All the code, data, and instructions required to reproduce the main results are available at https://github.com/Wang-ML-Lab/multimodal-needle-in-a-haystack.

### Curated Summary
A multi-image needle benchmark that stresses sub-image localization and negative-sample hallucination.

## Links

| Type | Link |
|---|---|
| Paper | https://arxiv.org/abs/2406.11230 |
| Project Page | https://mmneedle.github.io/ |
| GitHub | https://github.com/Wang-ML-Lab/multimodal-needle-in-a-haystack |

## BibTeX

```bibtex
@misc{https://doi.org/10.48550/arxiv.2406.11230,
  doi = {10.48550/ARXIV.2406.11230},
  url = {https://arxiv.org/abs/2406.11230},
  author = {Wang, Hengyi and Shi, Haizhou and Tan, Shiwei and Qin, Weiyi and Wang, Wenyuan and Zhang, Tunyu and Nambi, Akshay and Ganu, Tanuja and Wang, Hao},
  keywords = {Machine Learning (cs.LG), Artificial Intelligence (cs.AI), Computation and Language (cs.CL), Computer Vision and Pattern Recognition (cs.CV), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {Multimodal Needle in a Haystack: Benchmarking Long-Context Capability of Multimodal Large Language Models},
  publisher = {arXiv},
  year = {2024},
  copyright = {Creative Commons Attribution 4.0 International}
}
```

## Remarks

- This card prioritizes official paper pages, project pages, and code repositories. When a link in the original report was incorrect, the corrected official link is used instead.
