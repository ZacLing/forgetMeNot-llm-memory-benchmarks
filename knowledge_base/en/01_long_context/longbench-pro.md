---
name: LongBench Pro
slug: longbench-pro
language: en
category: Long-Context Understanding and Reasoning
subcategory: Comprehensive Long-Context Tasks
memory_type: Working / In-Context
year: "2026"
primary_source_kind: paper
primary_source_url: https://arxiv.org/abs/2601.02872
counterpart_zh: ../../zh/01_long_context/longbench-pro.md
---

# LongBench Pro

[English Knowledge Base Index](../README.md) | [中文卡片](../../zh/01_long_context/longbench-pro.md)

## Structured Metadata

| Field | Content |
|---|---|
| Benchmark | LongBench Pro |
| Category | Long-Context Understanding and Reasoning |
| Subcategory | Comprehensive Long-Context Tasks |
| Memory Focus | Working / In-Context |
| First Year | 2026 |
| Primary Source Type | paper |
| Paper Title | LongBench Pro: A More Realistic and Comprehensive Bilingual Long-Context Evaluation Benchmark |
| Chinese Card | [LongBench Pro](../../zh/01_long_context/longbench-pro.md) |

## Overview

A more realistic bilingual long-context benchmark with 1,500 naturally occurring long samples and a fine-grained taxonomy.

## Abstract
### Original Abstract
> The rapid expansion of context length in large language models (LLMs) has outpaced existing evaluation benchmarks. Current long-context benchmarks often trade off scalability and realism: synthetic tasks underrepresent real-world complexity, while fully manual annotation is costly to scale to extreme lengths and diverse scenarios. We present LongBench Pro, a more realistic and comprehensive bilingual benchmark of 1,500 naturally occurring long-context samples in English and Chinese spanning 11 primary tasks and 25 secondary tasks, with input lengths from 8k to 256k tokens. LongBench Pro supports fine-grained analysis with task-specific metrics and a multi-dimensional taxonomy of context requirement (full vs. partial dependency), length (six levels), and difficulty (four levels calibrated by model performance). To balance quality with scalability, we propose a Human-Model Collaborative Construction pipeline: frontier LLMs draft challenging questions and reference answers, along with design rationales and solution processes, to reduce the cost of expert verification. Experts then rigorously validate correctness and refine problematic cases. Evaluating 46 widely used long-context LLMs on LongBench Pro yields three findings: (1) long-context optimization contributes more to long-context comprehension than parameter scaling; (2) effective context length is typically shorter than the claimed context length, with pronounced cross-lingual misalignment; and (3) the "thinking" paradigm helps primarily models trained with native reasoning, while mixed-thinking designs offer a promising Pareto trade-off. In summary, LongBench Pro provides a robust testbed for advancing long-context understanding.

### Curated Summary
A more realistic bilingual long-context benchmark with 1,500 naturally occurring long samples and a fine-grained taxonomy.

## Links

| Type | Link |
|---|---|
| Paper | https://arxiv.org/abs/2601.02872 |
| Dataset | https://huggingface.co/datasets/caskcsg/LongBench-Pro |

## BibTeX

```bibtex
@misc{https://doi.org/10.48550/arxiv.2601.02872,
  doi = {10.48550/ARXIV.2601.02872},
  url = {https://arxiv.org/abs/2601.02872},
  author = {Chen, Ziyang and Wu, Xing and Jia, Junlong and Gao, Chaochen and Fu, Qi and Zhang, Debing and Hu, Songlin},
  keywords = {Computation and Language (cs.CL), Artificial Intelligence (cs.AI), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {LongBench Pro: A More Realistic and Comprehensive Bilingual Long-Context Evaluation Benchmark},
  publisher = {arXiv},
  year = {2026},
  copyright = {arXiv.org perpetual, non-exclusive license}
}
```

## Remarks

- This card prioritizes official paper pages, project pages, and code repositories. When a link in the original report was incorrect, the corrected official link is used instead.
