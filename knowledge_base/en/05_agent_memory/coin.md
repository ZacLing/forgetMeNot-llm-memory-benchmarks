---
name: CoIN
slug: coin
language: en
category: Agent Memory and Continual Learning
subcategory: 持续学习与反馈记忆
memory_type: Agentic / Procedural / Continual
year: "2024"
primary_source_kind: paper
primary_source_url: https://arxiv.org/abs/2403.08350
counterpart_zh: ../../zh/05_agent_memory/coin.md
---

# CoIN

[English Knowledge Base Index](../README.md) | [中文卡片](../../zh/05_agent_memory/coin.md)

## Structured Metadata

| Field | Content |
|---|---|
| Benchmark | CoIN |
| Category | Agent Memory and Continual Learning |
| Subcategory | 持续学习与反馈记忆 |
| Memory Focus | Agentic / Procedural / Continual |
| First Year | 2024 |
| Primary Source Type | paper |
| Paper Title | CoIN: A Benchmark of Continual Instruction tuNing for Multimodel Large Language Model |
| Chinese Card | [CoIN](../../zh/05_agent_memory/coin.md) |

## Overview

A multimodal continual instruction-tuning benchmark that measures instruction following and retained knowledge under drift.

## Abstract
### Original Abstract
> Instruction tuning represents a prevalent strategy employed by Multimodal Large Language Models (MLLMs) to align with human instructions and adapt to new tasks. Nevertheless, MLLMs encounter the challenge of adapting to users' evolving knowledge and demands. Therefore, how to retain existing skills while acquiring new knowledge needs to be investigated. In this paper, we present a comprehensive benchmark, namely Continual Instruction tuNing (CoIN), to assess existing MLLMs in the sequential instruction tuning paradigm. CoIN comprises 10 commonly used datasets spanning 8 task categories, ensuring a diverse range of instructions and tasks. Besides, the trained model is evaluated from two aspects: Instruction Following and General Knowledge, which assess the alignment with human intention and knowledge preserved for reasoning, respectively. Experiments on CoIN demonstrate that current powerful MLLMs still suffer catastrophic forgetting, and the failure in intention alignment assumes the main responsibility, instead of the knowledge forgetting. To this end, we introduce MoELoRA to MLLMs which is effective to retain the previous instruction alignment. Experimental results consistently illustrate the forgetting decreased from this method on CoIN.

### Curated Summary
A multimodal continual instruction-tuning benchmark that measures instruction following and retained knowledge under drift.

## Links

| Type | Link |
|---|---|
| Paper | https://arxiv.org/abs/2403.08350 |
| GitHub | https://github.com/zackschen/CoIN |
| other_neurips-entry_url | https://proceedings.neurips.cc/paper_files/paper/2024/hash/6a45500d9eda640deed90d8a62742be5-Abstract-Datasets_and_Benchmarks_Track.html |

## BibTeX

```bibtex
@misc{https://doi.org/10.48550/arxiv.2403.08350,
  doi = {10.48550/ARXIV.2403.08350},
  url = {https://arxiv.org/abs/2403.08350},
  author = {Chen, Cheng and Zhu, Junchen and Luo, Xu and Shen, Hengtao and Gao, Lianli and Song, Jingkuan},
  keywords = {Computer Vision and Pattern Recognition (cs.CV), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {CoIN: A Benchmark of Continual Instruction tuNing for Multimodel Large Language Model},
  publisher = {arXiv},
  year = {2024},
  copyright = {Creative Commons Attribution 4.0 International}
}
```

## Remarks

- This card prioritizes official paper pages, project pages, and code repositories. When a link in the original report was incorrect, the corrected official link is used instead.
