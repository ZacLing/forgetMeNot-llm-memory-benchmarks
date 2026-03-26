---
name: MemoryArena
slug: memoryarena
language: en
category: Agent Memory and Continual Learning
subcategory: Agentic memory benchmark
memory_type: Agentic / Procedural / Continual
year: "2026"
primary_source_kind: paper
primary_source_url: https://arxiv.org/abs/2602.16313
counterpart_zh: ../../zh/05_agent_memory/memoryarena.md
---

# MemoryArena

[English Knowledge Base Index](../README.md) | [中文卡片](../../zh/05_agent_memory/memoryarena.md)

## Structured Metadata

| Field | Content |
|---|---|
| Benchmark | MemoryArena |
| Category | Agent Memory and Continual Learning |
| Subcategory | Agentic memory benchmark |
| Memory Focus | Agentic / Procedural / Continual |
| First Year | 2026 |
| Primary Source Type | paper |
| Paper Title | MemoryArena: Benchmarking Agent Memory in Interdependent Multi-Session Agentic Tasks |
| Chinese Card | [MemoryArena](../../zh/05_agent_memory/memoryarena.md) |

## Overview

A benchmark for agent memory in interdependent multi-session agentic tasks.

## Abstract
### Original Abstract
> Existing evaluations of agents with memory typically assess memorization and action in isolation. One class of benchmarks evaluates memorization by testing recall of past conversations or text but fails to capture how memory is used to guide future decisions. Another class focuses on agents acting in single-session tasks without the need for long-term memory. However, in realistic settings, memorization and action are tightly coupled: agents acquire memory while interacting with the environment, and subsequently rely on that memory to solve future tasks. To capture this setting, we introduce MemoryArena, a unified evaluation gym for benchmarking agent memory in multi-session Memory-Agent-Environment loops. The benchmark consists of human-crafted agentic tasks with explicitly interdependent subtasks, where agents must learn from earlier actions and feedback by distilling experiences into memory, and subsequently use that memory to guide later actions to solve the overall task. MemoryArena supports evaluation across web navigation, preference-constrained planning, progressive information search, and sequential formal reasoning, and reveals that agents with near-saturated performance on existing long-context memory benchmarks like LoCoMo perform poorly in our agentic setting, exposing a gap in current evaluations for agents with memory.

### Curated Summary
A benchmark for agent memory in interdependent multi-session agentic tasks.

## Links

| Type | Link |
|---|---|
| Paper | https://arxiv.org/abs/2602.16313 |
| Project Page | https://memoryarena.github.io/ |

## BibTeX

```bibtex
@misc{https://doi.org/10.48550/arxiv.2602.16313,
  doi = {10.48550/ARXIV.2602.16313},
  url = {https://arxiv.org/abs/2602.16313},
  author = {He, Zexue and Wang, Yu and Zhi, Churan and Hu, Yuanzhe and Chen, Tzu-Ping and Yin, Lang and Chen, Ze and Wu, Tong Arthur and Ouyang, Siru and Wang, Zihan and Pei, Jiaxin and McAuley, Julian and Choi, Yejin and Pentland, Alex},
  keywords = {Computation and Language (cs.CL), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {MemoryArena: Benchmarking Agent Memory in Interdependent Multi-Session Agentic Tasks},
  publisher = {arXiv},
  year = {2026},
  copyright = {arXiv.org perpetual, non-exclusive license}
}
```

## Remarks

- The original arXiv link was incorrect. This card replaces it with the official MemoryArena paper.
