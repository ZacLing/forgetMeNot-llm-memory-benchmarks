---
name: LifelongAgentBench
slug: lifelongagentbench
language: zh
category: 智能体记忆与持续学习
subcategory: Agentic memory benchmark
memory_type: Agentic / Procedural / Continual
year: "2025"
primary_source_kind: paper
primary_source_url: https://arxiv.org/abs/2505.11942
counterpart_en: ../../en/05_agent_memory/lifelongagentbench.md
---

# LifelongAgentBench

[中文知识库索引](../README.md) | [English Card](../../en/05_agent_memory/lifelongagentbench.md)

## 结构化信息

| 字段 | 内容 |
|---|---|
| Benchmark | LifelongAgentBench |
| 分类 | 智能体记忆与持续学习 |
| 子类 | Agentic memory benchmark |
| 记忆侧重 | Agentic / Procedural / Continual |
| 首次年份 | 2025 |
| 主要来源类型 | paper |
| 论文标题 | LifelongAgentBench: Evaluating LLM Agents as Lifelong Learners |
| 英文卡片 | [LifelongAgentBench](../../en/05_agent_memory/lifelongagentbench.md) |

## 基础介绍

定义：将 LLM agents 视为“终身学习系统”，提供统一 benchmark 与框架。

## Abstract
### 原始摘要
> Lifelong learning is essential for intelligent agents operating in dynamic environments. Current large language model (LLM)-based agents, however, remain stateless and unable to accumulate or transfer knowledge over time. Existing benchmarks treat agents as static systems and fail to evaluate lifelong learning capabilities. We present LifelongAgentBench, the first unified benchmark designed to systematically assess the lifelong learning ability of LLM agents. It provides skill-grounded, interdependent tasks across three interactive environments, Database, Operating System, and Knowledge Graph, with automatic label verification, reproducibility, and modular extensibility. Extensive experiments reveal that conventional experience replay has limited effectiveness for LLM agents due to irrelevant information and context length constraints. We further introduce a group self-consistency mechanism that significantly improves lifelong learning performance. We hope LifelongAgentBench will advance the development of adaptive, memory-capable LLM agents.

### 中文抽取
定义：将 LLM agents 视为“终身学习系统”，提供统一 benchmark 与框架。

## URL 汇总

| 类型 | 链接 |
|---|---|
| 论文页 | https://arxiv.org/abs/2505.11942 |
| 项目主页 | https://caixd-220529.github.io/LifelongAgentBench/ |

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

## 备注

- 本卡片优先使用论文页、项目页与代码仓库等官方来源；若原报告中的链接存在错误，则以标题匹配后的官方链接为准。
