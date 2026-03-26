---
name: PersonaMem
slug: personamem
language: zh
category: 多会话对话记忆与个性化
subcategory: 个性化与真实多会话
memory_type: Episodic / Multi-Session
year: "2025"
primary_source_kind: paper
primary_source_url: https://arxiv.org/abs/2504.14225
counterpart_en: ../../en/04_dialogue_memory/personamem.md
---

# PersonaMem

[中文知识库索引](../README.md) | [English Card](../../en/04_dialogue_memory/personamem.md)

## 结构化信息

| 字段 | 内容 |
|---|---|
| Benchmark | PersonaMem |
| 分类 | 多会话对话记忆与个性化 |
| 子类 | 个性化与真实多会话 |
| 记忆侧重 | Episodic / Multi-Session |
| 首次年份 | 2025 |
| 主要来源类型 | paper |
| 论文标题 | Know Me, Respond to Me: Benchmarking LLMs for Dynamic User Profiling and Personalized Responses at Scale |
| 英文卡片 | [PersonaMem](../../en/04_dialogue_memory/personamem.md) |

## 基础介绍

定位：OpenReview 条目明确其为用于评估“动态用户交互中的个性化能力”的大规模 benchmark。

## Abstract
### 原始摘要
> Large Language Models (LLMs) have emerged as personalized assistants for users across a wide range of tasks -- from offering writing support to delivering tailored recommendations or consultations. Over time, the interaction history between a user and an LLM can provide extensive information about an individual's traits and preferences. However, open questions remain on how well LLMs today can effectively leverage such history to (1) internalize the user's inherent traits and preferences, (2) track how the user profiling and preferences evolve over time, and (3) generate personalized responses accordingly in new scenarios. In this work, we introduce the PERSONAMEM benchmark. PERSONAMEM features curated user profiles with over 180 simulated user-LLM interaction histories, each containing up to 60 sessions of multi-turn conversations across 15 real-world tasks that require personalization. Given an in-situ user query, i.e. query issued by the user from the first-person perspective, we evaluate LLM chatbots' ability to identify the most suitable response according to the current state of the user's profile. We observe that current LLMs still struggle to recognize the dynamic evolution in users' profiles over time through direct prompting approaches. As a consequence, LLMs often fail to deliver responses that align with users' current situations and preferences, with frontier models such as GPT-4.1, o4-mini, GPT-4.5, o1, or Gemini-2.0 achieving only around 50% overall accuracy, suggesting room for improvement. We hope that PERSONAMEM, along with the user profile and conversation simulation pipeline, can facilitate future research in the development of truly user-aware chatbots. Code and data are available at github.com/bowen-upenn/PersonaMem.

### 中文抽取
定位：OpenReview 条目明确其为用于评估“动态用户交互中的个性化能力”的大规模 benchmark。

## URL 汇总

| 类型 | 链接 |
|---|---|
| 论文页 | https://arxiv.org/abs/2504.14225 |
| 项目主页 | https://zhuoqunhao.github.io/PersonaMem.github.io/ |
| GitHub | https://github.com/bowen-upenn/PersonaMem |

## BibTeX

```bibtex
@misc{https://doi.org/10.48550/arxiv.2504.14225,
  doi = {10.48550/ARXIV.2504.14225},
  url = {https://arxiv.org/abs/2504.14225},
  author = {Jiang, Bowen and Hao, Zhuoqun and Cho, Young-Min and Li, Bryan and Yuan, Yuan and Chen, Sihao and Ungar, Lyle and Taylor, Camillo J. and Roth, Dan},
  keywords = {Computation and Language (cs.CL), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {Know Me, Respond to Me: Benchmarking LLMs for Dynamic User Profiling and Personalized Responses at Scale},
  publisher = {arXiv},
  year = {2025},
  copyright = {Creative Commons Attribution Share Alike 4.0 International}
}
```

## 备注

- 原报告仅给出 OpenReview 链接；这里补充了可直接抓取 abstract 与 BibTeX 的 arXiv 版本及官方代码页。
