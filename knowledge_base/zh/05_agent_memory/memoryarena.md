---
name: MemoryArena
slug: memoryarena
language: zh
category: 智能体记忆与持续学习
subcategory: Agentic memory benchmark
memory_type: Agentic / Procedural / Continual
year: "2026"
primary_source_kind: paper
primary_source_url: https://arxiv.org/abs/2602.16313
counterpart_en: ../../en/05_agent_memory/memoryarena.md
---

# MemoryArena

[中文知识库索引](../README.md) | [English Card](../../en/05_agent_memory/memoryarena.md)

## 结构化信息

| 字段 | 内容 |
|---|---|
| Benchmark | MemoryArena |
| 分类 | 智能体记忆与持续学习 |
| 子类 | Agentic memory benchmark |
| 记忆侧重 | Agentic / Procedural / Continual |
| 首次年份 | 2026 |
| 主要来源类型 | paper |
| 论文标题 | MemoryArena: Benchmarking Agent Memory in Interdependent Multi-Session Agentic Tasks |
| 英文卡片 | [MemoryArena](../../en/05_agent_memory/memoryarena.md) |

## 基础介绍

定位：面向“相互依赖的多 session agentic 任务”评测 agent memory；该名称在集中清单与论文条目中出现。

## Abstract
### 原始摘要
> Existing evaluations of agents with memory typically assess memorization and action in isolation. One class of benchmarks evaluates memorization by testing recall of past conversations or text but fails to capture how memory is used to guide future decisions. Another class focuses on agents acting in single-session tasks without the need for long-term memory. However, in realistic settings, memorization and action are tightly coupled: agents acquire memory while interacting with the environment, and subsequently rely on that memory to solve future tasks. To capture this setting, we introduce MemoryArena, a unified evaluation gym for benchmarking agent memory in multi-session Memory-Agent-Environment loops. The benchmark consists of human-crafted agentic tasks with explicitly interdependent subtasks, where agents must learn from earlier actions and feedback by distilling experiences into memory, and subsequently use that memory to guide later actions to solve the overall task. MemoryArena supports evaluation across web navigation, preference-constrained planning, progressive information search, and sequential formal reasoning, and reveals that agents with near-saturated performance on existing long-context memory benchmarks like LoCoMo perform poorly in our agentic setting, exposing a gap in current evaluations for agents with memory.

### 中文抽取
定位：面向“相互依赖的多 session agentic 任务”评测 agent memory；该名称在集中清单与论文条目中出现。

## URL 汇总

| 类型 | 链接 |
|---|---|
| 论文页 | https://arxiv.org/abs/2602.16313 |
| 项目主页 | https://memoryarena.github.io/ |

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

## 备注

- 原报告中的 arXiv 链接有误，已替换为 MemoryArena 官方论文。
