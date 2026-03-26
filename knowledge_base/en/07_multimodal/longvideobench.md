---
name: LongVideoBench
slug: longvideobench
language: en
category: Multimodal Long-Horizon Memory and Retrieval-Reasoning
subcategory: 视频长上下文
memory_type: Multimodal Long-Horizon
year: "2024"
primary_source_kind: paper
primary_source_url: https://arxiv.org/abs/2407.15754
counterpart_zh: ../../zh/07_multimodal/longvideobench.md
---

# LongVideoBench

[English Knowledge Base Index](../README.md) | [中文卡片](../../zh/07_multimodal/longvideobench.md)

## Structured Metadata

| Field | Content |
|---|---|
| Benchmark | LongVideoBench |
| Category | Multimodal Long-Horizon Memory and Retrieval-Reasoning |
| Subcategory | 视频长上下文 |
| Memory Focus | Multimodal Long-Horizon |
| First Year | 2024 |
| Primary Source Type | paper |
| Paper Title | LongVideoBench: A Benchmark for Long-context Interleaved Video-Language Understanding |
| Chinese Card | [LongVideoBench](../../zh/07_multimodal/longvideobench.md) |

## Overview

An interleaved video-language long-context benchmark with videos up to around one hour.

## Abstract
### Original Abstract
> Large multimodal models (LMMs) are processing increasingly longer and richer inputs. Albeit the progress, few public benchmark is available to measure such development. To mitigate this gap, we introduce LongVideoBench, a question-answering benchmark that features video-language interleaved inputs up to an hour long. Our benchmark includes 3,763 varying-length web-collected videos with their subtitles across diverse themes, designed to comprehensively evaluate LMMs on long-term multimodal understanding. To achieve this, we interpret the primary challenge as to accurately retrieve and reason over detailed multimodal information from long inputs. As such, we formulate a novel video question-answering task termed referring reasoning. Specifically, as part of the question, it contains a referring query that references related video contexts, called referred context. The model is then required to reason over relevant video details from the referred context. Following the paradigm of referring reasoning, we curate 6,678 human-annotated multiple-choice questions in 17 fine-grained categories, establishing one of the most comprehensive benchmarks for long-form video understanding. Evaluations suggest that the LongVideoBench presents significant challenges even for the most advanced proprietary models (e.g. GPT-4o, Gemini-1.5-Pro, GPT-4-Turbo), while their open-source counterparts show an even larger performance gap. In addition, our results indicate that model performance on the benchmark improves only when they are capable of processing more frames, positioning LongVideoBench as a valuable benchmark for evaluating future-generation long-context LMMs.

### Curated Summary
An interleaved video-language long-context benchmark with videos up to around one hour.

## Links

| Type | Link |
|---|---|
| Paper | https://arxiv.org/abs/2407.15754 |
| GitHub | https://github.com/longvideobench/LongVideoBench |
| Dataset | https://huggingface.co/datasets/longvideobench/LongVideoBench |

## BibTeX

```bibtex
@misc{https://doi.org/10.48550/arxiv.2407.15754,
  doi = {10.48550/ARXIV.2407.15754},
  url = {https://arxiv.org/abs/2407.15754},
  author = {Wu, Haoning and Li, Dongxu and Chen, Bei and Li, Junnan},
  keywords = {Computer Vision and Pattern Recognition (cs.CV), Computation and Language (cs.CL), Machine Learning (cs.LG), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {LongVideoBench: A Benchmark for Long-context Interleaved Video-Language Understanding},
  publisher = {arXiv},
  year = {2024},
  copyright = {Creative Commons Attribution Non Commercial Share Alike 4.0 International}
}
```

## Remarks

- This card prioritizes official paper pages, project pages, and code repositories. When a link in the original report was incorrect, the corrected official link is used instead.
