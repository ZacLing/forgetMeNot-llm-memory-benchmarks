---
name: AMA-Bench
slug: ama-bench
language: en
category: Agent Memory and Continual Learning
subcategory: Agentic memory benchmark
memory_type: Agentic / Procedural / Continual
year: "2026"
primary_source_kind: paper
primary_source_url: https://arxiv.org/abs/2602.22769
counterpart_zh: ../../zh/05_agent_memory/ama-bench.md
---

# AMA-Bench

[English Knowledge Base Index](../README.md) | [中文卡片](../../zh/05_agent_memory/ama-bench.md)

## Structured Metadata

| Field | Content |
|---|---|
| Benchmark | AMA-Bench |
| Category | Agent Memory and Continual Learning |
| Subcategory | Agentic memory benchmark |
| Memory Focus | Agentic / Procedural / Continual |
| First Year | 2026 |
| Primary Source Type | paper |
| Paper Title | AMA-Bench: Evaluating Long-Horizon Memory for Agentic Applications |
| Chinese Card | [AMA-Bench](../../zh/05_agent_memory/ama-bench.md) |

## Overview

A long-horizon agent-memory benchmark built from real trajectories and scalable synthetic traces.

## Abstract
### Original Abstract
> Large Language Models (LLMs) are deployed as autonomous agents in increasingly complex applications, where enabling long-horizon memory is critical for achieving strong performance. However, a significant gap exists between practical applications and current evaluation standards for agent memory: existing benchmarks primarily focus on dialogue-centric, human-agent interactions. In reality, agent memory consists of a continuous stream of agent-environment interactions that are primarily composed of machine-generated representations. To bridge this gap, we introduce AMA-Bench (Agent Memory with Any length), which evaluates long-horizon memory for LLMs in real agentic applications. It features two key components: (1) a set of real-world agentic trajectories across representative agentic applications, paired with expert-curated QA, and (2) a set of synthetic agentic trajectories that scale to arbitrary horizons, paired with rule-based QA. Our comprehensive study shows that existing memory systems underperform on AMA-Bench primarily because they lack causality and objective information and are constrained by the lossy nature of similarity-based retrieval employed by many memory systems. To address these limitations, we propose AMA-Agent, an effective memory system featuring a causality graph and tool-augmented retrieval. Our results demonstrate that AMA-Agent achieves 57.22% average accuracy on AMA-Bench, surpassing the strongest memory system baselines by 11.16%.

### Curated Summary
A long-horizon agent-memory benchmark built from real trajectories and scalable synthetic traces.

## Links

| Type | Link |
|---|---|
| Paper | https://arxiv.org/abs/2602.22769 |
| Paper PDF | https://openreview.net/pdf/5705a80026ee66192e9c660b3ecb2c73254e4707.pdf |

## BibTeX

```bibtex
@misc{https://doi.org/10.48550/arxiv.2602.22769,
  doi = {10.48550/ARXIV.2602.22769},
  url = {https://arxiv.org/abs/2602.22769},
  author = {Zhao, Yujie and Yuan, Boqin and Huang, Junbo and Yuan, Haocheng and Yu, Zhongming and Xu, Haozhou and Hu, Lanxiang and Shankarampeta, Abhilash and Huang, Zimeng and Ni, Wentao and Tian, Yuandong and Zhao, Jishen},
  keywords = {Artificial Intelligence (cs.AI), Machine Learning (cs.LG), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {AMA-Bench: Evaluating Long-Horizon Memory for Agentic Applications},
  publisher = {arXiv},
  year = {2026},
  copyright = {Creative Commons Attribution 4.0 International}
}
```

## Remarks

- This card prioritizes official paper pages, project pages, and code repositories. When a link in the original report was incorrect, the corrected official link is used instead.
