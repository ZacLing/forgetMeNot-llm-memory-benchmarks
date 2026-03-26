---
name: LongBioBench
slug: longbiobench
language: en
category: Long-Context Understanding and Reasoning
subcategory: 长上下文综合任务
memory_type: Working / In-Context
year: "2025"
primary_source_kind: paper
primary_source_url: https://arxiv.org/abs/2506.02921
counterpart_zh: ../../zh/01_long_context/longbiobench.md
---

# LongBioBench

[English Knowledge Base Index](../README.md) | [中文卡片](../../zh/01_long_context/longbiobench.md)

## Structured Metadata

| Field | Content |
|---|---|
| Benchmark | LongBioBench |
| Category | Long-Context Understanding and Reasoning |
| Subcategory | 长上下文综合任务 |
| Memory Focus | Working / In-Context |
| First Year | 2025 |
| Primary Source Type | paper |
| Paper Title | A Controllable Examination for Long-Context Language Models |
| Chinese Card | [LongBioBench](../../zh/01_long_context/longbiobench.md) |

## Overview

A controllable long-context benchmark built from coherent biographical narratives to avoid shortcut-prone needle-style setups.

## Abstract
### Original Abstract
> Existing frameworks for evaluating long-context language models (LCLM) can be broadly categorized into real-world applications (e.g, document summarization) and synthetic tasks (e.g, needle-in-a-haystack). Despite their utility, both approaches are accompanied by certain intrinsic limitations. Real-world tasks often involve complexity that makes interpretation challenging and suffer from data contamination, whereas synthetic tasks frequently lack meaningful coherence between the target information (needle) and its surrounding context (haystack), undermining their validity as proxies for realistic applications. In response to these challenges, we posit that an ideal long-context evaluation framework should be characterized by three essential features: 1) seamless context 2) controllable setting and 3) sound evaluation. This study introduces $\textbf{LongBioBench}$, a benchmark that utilizes artificially generated biographies as a controlled environment for assessing LCLMs across dimensions of understanding, reasoning, and trustworthiness. Our experimental evaluation, which includes 18 LCLMs in total, demonstrates that most models still exhibit deficiencies in semantic understanding and elementary reasoning over retrieved results and are less trustworthy as context length increases. Our further analysis indicates some design choices employed by existing synthetic benchmarks, such as contextual non-coherence, numerical needles, and the absence of distractors, rendering them vulnerable to test the model's long-context capabilities. To sum up, compared to previous synthetic benchmarks, LongBioBench achieves a better trade-off between mirroring authentic language tasks and maintaining controllability, and is highly interpretable and configurable.

### Curated Summary
A controllable long-context benchmark built from coherent biographical narratives to avoid shortcut-prone needle-style setups.

## Links

| Type | Link |
|---|---|
| Paper | https://arxiv.org/abs/2506.02921 |
| GitHub | https://github.com/Thomasyyj/LongBio-Benchmark |

## BibTeX

```bibtex
@misc{https://doi.org/10.48550/arxiv.2506.02921,
  doi = {10.48550/ARXIV.2506.02921},
  url = {https://arxiv.org/abs/2506.02921},
  author = {Yang, Yijun and Huang, Zeyu and Zhu, Wenhao and Qiu, Zihan and Yuan, Fei and Pan, Jeff Z. and Titov, Ivan},
  keywords = {Computation and Language (cs.CL), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {A Controllable Examination for Long-Context Language Models},
  publisher = {arXiv},
  year = {2025},
  copyright = {Creative Commons Attribution 4.0 International}
}
```

## Remarks

- This card prioritizes official paper pages, project pages, and code repositories. When a link in the original report was incorrect, the corrected official link is used instead.
