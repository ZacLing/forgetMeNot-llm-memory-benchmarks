---
name: ∞Bench
slug: infinitebench
language: en
category: Long-Context Understanding and Reasoning
subcategory: 长上下文综合任务
memory_type: Working / In-Context
year: "2024"
primary_source_kind: paper
primary_source_url: https://arxiv.org/abs/2402.13718
counterpart_zh: ../../zh/01_long_context/infinitebench.md
---

# ∞Bench

[English Knowledge Base Index](../README.md) | [中文卡片](../../zh/01_long_context/infinitebench.md)

## Structured Metadata

| Field | Content |
|---|---|
| Benchmark | ∞Bench |
| Category | Long-Context Understanding and Reasoning |
| Subcategory | 长上下文综合任务 |
| Memory Focus | Working / In-Context |
| First Year | 2024 |
| Primary Source Type | paper |
| Paper Title | $\infty$Bench: Extending Long Context Evaluation Beyond 100K Tokens |
| Chinese Card | [∞Bench](../../zh/01_long_context/infinitebench.md) |

## Overview

A bilingual benchmark that mixes synthetic and realistic tasks with average context length beyond 100k tokens.

## Abstract
### Original Abstract
> Processing and reasoning over long contexts is crucial for many practical applications of Large Language Models (LLMs), such as document comprehension and agent construction. Despite recent strides in making LLMs process contexts with more than 100K tokens, there is currently a lack of a standardized benchmark to evaluate this long-context capability. Existing public benchmarks typically focus on contexts around 10K tokens, limiting the assessment and comparison of LLMs in processing longer contexts. In this paper, we propose $\infty$Bench, the first LLM benchmark featuring an average data length surpassing 100K tokens. $\infty$Bench comprises synthetic and realistic tasks spanning diverse domains, presented in both English and Chinese. The tasks in $\infty$Bench are designed to require well understanding of long dependencies in contexts, and make simply retrieving a limited number of passages from contexts not sufficient for these tasks. In our experiments, based on $\infty$Bench, we evaluate the state-of-the-art proprietary and open-source LLMs tailored for processing long contexts. The results indicate that existing long context LLMs still require significant advancements to effectively process 100K+ context. We further present three intriguing analyses regarding the behavior of LLMs processing long context.

### Curated Summary
A bilingual benchmark that mixes synthetic and realistic tasks with average context length beyond 100k tokens.

## Links

| Type | Link |
|---|---|
| Paper | https://arxiv.org/abs/2402.13718 |
| Paper PDF | https://aclanthology.org/2024.acl-long.814.pdf |
| GitHub | https://github.com/OpenBMB/InfiniteBench |

## BibTeX

```bibtex
@article{https://doi.org/10.48550/arxiv.2402.13718,
  doi = {10.48550/ARXIV.2402.13718},
  url = {https://arxiv.org/abs/2402.13718},
  author = {Zhang, Xinrong and Chen, Yingfa and Hu, Shengding and Xu, Zihang and Chen, Junhao and Hao, Moo Khai and Han, Xu and Thai, Zhen Leng and Wang, Shuo and Liu, Zhiyuan and Sun, Maosong},
  keywords = {Computation and Language (cs.CL), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {$\infty$Bench: Extending Long Context Evaluation Beyond 100K Tokens},
  publisher = {arXiv},
  year = {2024},
  copyright = {arXiv.org perpetual, non-exclusive license}
}
```

## Remarks

- This card prioritizes official paper pages, project pages, and code repositories. When a link in the original report was incorrect, the corrected official link is used instead.
