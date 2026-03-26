---
name: AMA-Bench
slug: ama-bench
language: zh
category: 智能体记忆与持续学习
subcategory: Agentic memory benchmark
memory_type: Agentic / Procedural / Continual
year: "2026"
primary_source_kind: paper
primary_source_url: https://arxiv.org/abs/2602.22769
counterpart_en: ../../en/05_agent_memory/ama-bench.md
---

# AMA-Bench

[中文知识库索引](../README.md) | [English Card](../../en/05_agent_memory/ama-bench.md)

## 结构化信息

| 字段 | 内容 |
|---|---|
| Benchmark | AMA-Bench |
| 分类 | 智能体记忆与持续学习 |
| 子类 | Agentic memory benchmark |
| 记忆侧重 | Agentic / Procedural / Continual |
| 首次年份 | 2026 |
| 主要来源类型 | paper |
| 论文标题 | AMA-Bench: Evaluating Long-Horizon Memory for Agentic Applications |
| 英文卡片 | [AMA-Bench](../../en/05_agent_memory/ama-bench.md) |

## 基础介绍

动机：指出现有记忆评测偏“对话中心”，而真实 agent memory 更多是 agent‑environment 交互流；AMA‑Bench 提供真实轨迹 QA + 可扩展合成轨迹 QA，并提出 AMA‑Agent。

## Abstract
### 原始摘要
> Large Language Models (LLMs) are deployed as autonomous agents in increasingly complex applications, where enabling long-horizon memory is critical for achieving strong performance. However, a significant gap exists between practical applications and current evaluation standards for agent memory: existing benchmarks primarily focus on dialogue-centric, human-agent interactions. In reality, agent memory consists of a continuous stream of agent-environment interactions that are primarily composed of machine-generated representations. To bridge this gap, we introduce AMA-Bench (Agent Memory with Any length), which evaluates long-horizon memory for LLMs in real agentic applications. It features two key components: (1) a set of real-world agentic trajectories across representative agentic applications, paired with expert-curated QA, and (2) a set of synthetic agentic trajectories that scale to arbitrary horizons, paired with rule-based QA. Our comprehensive study shows that existing memory systems underperform on AMA-Bench primarily because they lack causality and objective information and are constrained by the lossy nature of similarity-based retrieval employed by many memory systems. To address these limitations, we propose AMA-Agent, an effective memory system featuring a causality graph and tool-augmented retrieval. Our results demonstrate that AMA-Agent achieves 57.22% average accuracy on AMA-Bench, surpassing the strongest memory system baselines by 11.16%.

### 中文抽取
动机：指出现有记忆评测偏“对话中心”，而真实 agent memory 更多是 agent‑environment 交互流；AMA‑Bench 提供真实轨迹 QA + 可扩展合成轨迹 QA，并提出 AMA‑Agent。

## URL 汇总

| 类型 | 链接 |
|---|---|
| 论文页 | https://arxiv.org/abs/2602.22769 |
| 论文 PDF | https://openreview.net/pdf/5705a80026ee66192e9c660b3ecb2c73254e4707.pdf |

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

## 备注

- 本卡片优先使用论文页、项目页与代码仓库等官方来源；若原报告中的链接存在错误，则以标题匹配后的官方链接为准。
