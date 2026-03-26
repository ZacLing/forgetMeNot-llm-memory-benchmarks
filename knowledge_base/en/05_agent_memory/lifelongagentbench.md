---
name: LifelongAgentBench
slug: lifelongagentbench
language: en
category: Agent Memory and Continual Learning
subcategory: Agentic memory benchmark
memory_type: Agentic / Procedural / Continual
year: "2025"
primary_source_kind: paper
primary_source_url: https://arxiv.org/abs/2505.11942
counterpart_zh: ../../zh/05_agent_memory/lifelongagentbench.md
---

# LifelongAgentBench

[English Knowledge Base Index](../README.md) | [中文卡片](../../zh/05_agent_memory/lifelongagentbench.md)

## Structured Metadata

| Field | Content |
|---|---|
| Benchmark | LifelongAgentBench |
| Category | Agent Memory and Continual Learning |
| Subcategory | Agentic memory benchmark |
| Memory Focus | Agentic / Procedural / Continual |
| First Year | 2025 |
| Primary Source Type | paper |
| Paper Title | LifelongAgentBench: Evaluating LLM Agents as Lifelong Learners |
| Chinese Card | [LifelongAgentBench](../../zh/05_agent_memory/lifelongagentbench.md) |

## Overview

A unified benchmark that evaluates LLM agents as lifelong learners across evolving tasks.

## Abstract
### Original Abstract
> Lifelong learning is essential for intelligent agents operating in dynamic environments. Current large language model (LLM)-based agents, however, remain stateless and unable to accumulate or transfer knowledge over time. Existing benchmarks treat agents as static systems and fail to evaluate lifelong learning capabilities. We present LifelongAgentBench, the first unified benchmark designed to systematically assess the lifelong learning ability of LLM agents. It provides skill-grounded, interdependent tasks across three interactive environments, Database, Operating System, and Knowledge Graph, with automatic label verification, reproducibility, and modular extensibility. Extensive experiments reveal that conventional experience replay has limited effectiveness for LLM agents due to irrelevant information and context length constraints. We further introduce a group self-consistency mechanism that significantly improves lifelong learning performance. We hope LifelongAgentBench will advance the development of adaptive, memory-capable LLM agents.

### Curated Summary
A unified benchmark that evaluates LLM agents as lifelong learners across evolving tasks.

## Links

| Type | Link |
|---|---|
| Paper | https://arxiv.org/abs/2505.11942 |
| Project Page | https://caixd-220529.github.io/LifelongAgentBench/ |

## BibTeX

```bibtex
@misc{https://doi.org/10.48550/arxiv.2505.11942,
  doi = {10.48550/ARXIV.2505.11942},
  url = {https://arxiv.org/abs/2505.11942},
  author = {Zheng, Junhao and Cai, Xidi and Li, Qiuke and Zhang, Duzhen and Li, ZhongZhi and Zhang, Yingying and Song, Le and Ma, Qianli},
  keywords = {Artificial Intelligence (cs.AI), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {LifelongAgentBench: Evaluating LLM Agents as Lifelong Learners},
  publisher = {arXiv},
  year = {2025},
  copyright = {Creative Commons Attribution 4.0 International}
}
```

## Remarks

- This card prioritizes official paper pages, project pages, and code repositories. When a link in the original report was incorrect, the corrected official link is used instead.
