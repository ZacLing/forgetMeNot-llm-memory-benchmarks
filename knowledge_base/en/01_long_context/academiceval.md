---
name: AcademicEval
slug: academiceval
language: en
category: Long-Context Understanding and Reasoning
subcategory: Comprehensive Long-Context Tasks
memory_type: Working / In-Context
year: "2025"
primary_source_kind: paper
primary_source_url: https://arxiv.org/abs/2510.17725
counterpart_zh: ../../zh/01_long_context/academiceval.md
---

# AcademicEval

[English Knowledge Base Index](../README.md) | [中文卡片](../../zh/01_long_context/academiceval.md)

## Structured Metadata

| Field | Content |
|---|---|
| Benchmark | AcademicEval |
| Category | Long-Context Understanding and Reasoning |
| Subcategory | Comprehensive Long-Context Tasks |
| Memory Focus | Working / In-Context |
| First Year | 2025 |
| Primary Source Type | paper |
| Paper Title | AcademicEval: Live Long-Context LLM Benchmark |
| Chinese Card | [AcademicEval](../../zh/01_long_context/academiceval.md) |

## Overview

A live long-context generation benchmark built from recent arXiv papers for title, abstract, introduction, and related-work writing tasks.

## Abstract
### Original Abstract
> Large Language Models (LLMs) have recently achieved remarkable performance in long-context understanding. However, current long-context LLM benchmarks are limited by rigid context length, labor-intensive annotation, and the pressing challenge of label leakage issues during LLM training. Therefore, we propose \textsc{AcademicEval}, a live benchmark for evaluating LLMs over long-context generation tasks. \textsc{AcademicEval} adopts papers on arXiv to introduce several academic writing tasks with long-context inputs, \textit{i.e.}, \textsc{Title}, \textsc{Abstract}, \textsc{Introduction}, and \textsc{Related Work}, which cover a wide range of abstraction levels and require no manual labeling. Moreover, \textsc{AcademicEval} integrates high-quality and expert-curated few-shot demonstrations from a collected co-author graph to enable flexible context length. Especially, \textsc{AcademicEval} features an efficient live evaluation, ensuring no label leakage. We conduct a holistic evaluation on \textsc{AcademicEval}, and the results illustrate that LLMs perform poorly on tasks with hierarchical abstraction levels and tend to struggle with long few-shot demonstrations, highlighting the challenge of our benchmark. Through experimental analysis, we also reveal some insights for enhancing LLMs' long-context modeling capabilities. Code is available at https://github.com/ulab-uiuc/AcademicEval

### Curated Summary
A live long-context generation benchmark built from recent arXiv papers for title, abstract, introduction, and related-work writing tasks.

## Links

| Type | Link |
|---|---|
| Paper | https://arxiv.org/abs/2510.17725 |
| GitHub | https://github.com/ulab-uiuc/AcademicEval |

## BibTeX

```bibtex
@misc{https://doi.org/10.48550/arxiv.2510.17725,
  doi = {10.48550/ARXIV.2510.17725},
  url = {https://arxiv.org/abs/2510.17725},
  author = {Zhang, Haozhen and Feng, Tao and Han, Pengrui and You, Jiaxuan},
  keywords = {Computation and Language (cs.CL), Artificial Intelligence (cs.AI), Machine Learning (cs.LG), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {AcademicEval: Live Long-Context LLM Benchmark},
  publisher = {arXiv},
  year = {2025},
  copyright = {Creative Commons Attribution 4.0 International}
}
```

## Remarks

- This card prioritizes official paper pages, project pages, and code repositories. When a link in the original report was incorrect, the corrected official link is used instead.
