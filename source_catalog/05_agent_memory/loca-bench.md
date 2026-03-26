---
name: LOCA-bench
slug: loca-bench
category: 智能体记忆与持续学习
subcategory: Agentic memory benchmark
memory_type: Agentic / Procedural / Continual
year: "2026"
primary_source_kind: paper
primary_source_url: https://arxiv.org/abs/2602.07962
---

# LOCA-bench

## 结构化信息

| 字段 | 内容 |
|---|---|
| Benchmark | LOCA-bench |
| 分类 | 智能体记忆与持续学习 |
| 子类 | Agentic memory benchmark |
| 记忆侧重 | Agentic / Procedural / Continual |
| 首次年份 | 2026 |
| 主要来源类型 | paper |
| 论文标题 | LOCA-bench: Benchmarking Language Agents Under Controllable and Extreme Context Growth |

## 基础介绍

特点：把评测从“单步长片段检索”扩展到“代理在环境中探索/计划/行动”的场景；环境状态可控增长，context 可潜在趋于无限，并可评估不同 context‑management scaffold。

## Abstract
### 原始摘要
> Large language models (LLMs) are increasingly capable of carrying out long-running, real-world tasks. However, as the amount of context grows, their reliability often deteriorates, a phenomenon known as "context rot". Existing long-context benchmarks primarily focus on single-step settings that evaluate a model's ability to retrieve information from a long snippet. In realistic scenarios, however, LLMs often need to act as agents that explore environments, follow instructions and plans, extract useful information, and predict correct actions under a dynamically growing context. To assess language agents in such settings, we introduce LOCA-bench (a benchmark for LOng-Context Agents). Given a task prompt, LOCA-bench leverages automated and scalable control of environment states to regulate the agent's context length. This design enables LOCA-bench to extend the context length potentially to infinity in a controlled way while keeping the underlying task semantics fixed. LOCA-bench evaluates language agents as a combination of models and scaffolds, including various context management strategies. While agent performance generally degrades as the environment states grow more complex, advanced context management techniques can substantially improve the overall success rate. We open-source LOCA-bench to provide a platform for evaluating models and scaffolds in long-context, agentic scenarios: https://github.com/hkust-nlp/LOCA-bench

### 中文抽取
特点：把评测从“单步长片段检索”扩展到“代理在环境中探索/计划/行动”的场景；环境状态可控增长，context 可潜在趋于无限，并可评估不同 context‑management scaffold。

## URL 汇总

| 类型 | 链接 |
|---|---|
| 论文页 | https://arxiv.org/abs/2602.07962 |
| GitHub | https://github.com/hkust-nlp/LOCA-bench |

## BibTeX

```bibtex
@misc{https://doi.org/10.48550/arxiv.2602.07962,
  doi = {10.48550/ARXIV.2602.07962},
  url = {https://arxiv.org/abs/2602.07962},
  author = {Zeng, Weihao and Huang, Yuzhen and He, Junxian},
  keywords = {Artificial Intelligence (cs.AI), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {LOCA-bench: Benchmarking Language Agents Under Controllable and Extreme Context Growth},
  publisher = {arXiv},
  year = {2026},
  copyright = {arXiv.org perpetual, non-exclusive license}
}
```

## 备注

- 本卡片优先使用论文页、项目页与代码仓库等官方来源；若原报告中的链接存在错误，则以标题匹配后的官方链接为准。
