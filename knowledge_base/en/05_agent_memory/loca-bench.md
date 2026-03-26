---
name: LOCA-bench
slug: loca-bench
language: en
category: Agent Memory and Continual Learning
subcategory: Agentic memory benchmark
memory_type: Agentic / Procedural / Continual
year: "2026"
primary_source_kind: paper
primary_source_url: https://arxiv.org/abs/2602.07962
counterpart_zh: ../../zh/05_agent_memory/loca-bench.md
---

# LOCA-bench

[English Knowledge Base Index](../README.md) | [中文卡片](../../zh/05_agent_memory/loca-bench.md)

## Structured Metadata

| Field | Content |
|---|---|
| Benchmark | LOCA-bench |
| Category | Agent Memory and Continual Learning |
| Subcategory | Agentic memory benchmark |
| Memory Focus | Agentic / Procedural / Continual |
| First Year | 2026 |
| Primary Source Type | paper |
| Paper Title | LOCA-bench: Benchmarking Language Agents Under Controllable and Extreme Context Growth |
| Chinese Card | [LOCA-bench](../../zh/05_agent_memory/loca-bench.md) |

## Overview

A controllable benchmark for language agents under extreme context growth in interactive environments.

## Abstract
### Original Abstract
> Large language models (LLMs) are increasingly capable of carrying out long-running, real-world tasks. However, as the amount of context grows, their reliability often deteriorates, a phenomenon known as "context rot". Existing long-context benchmarks primarily focus on single-step settings that evaluate a model's ability to retrieve information from a long snippet. In realistic scenarios, however, LLMs often need to act as agents that explore environments, follow instructions and plans, extract useful information, and predict correct actions under a dynamically growing context. To assess language agents in such settings, we introduce LOCA-bench (a benchmark for LOng-Context Agents). Given a task prompt, LOCA-bench leverages automated and scalable control of environment states to regulate the agent's context length. This design enables LOCA-bench to extend the context length potentially to infinity in a controlled way while keeping the underlying task semantics fixed. LOCA-bench evaluates language agents as a combination of models and scaffolds, including various context management strategies. While agent performance generally degrades as the environment states grow more complex, advanced context management techniques can substantially improve the overall success rate. We open-source LOCA-bench to provide a platform for evaluating models and scaffolds in long-context, agentic scenarios: https://github.com/hkust-nlp/LOCA-bench

### Curated Summary
A controllable benchmark for language agents under extreme context growth in interactive environments.

## Links

| Type | Link |
|---|---|
| Paper | https://arxiv.org/abs/2602.07962 |
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

## Remarks

- This card prioritizes official paper pages, project pages, and code repositories. When a link in the original report was incorrect, the corrected official link is used instead.
