---
name: DialSim
slug: dialsim
language: zh
category: 多会话对话记忆与个性化
subcategory: 长期对话记忆
memory_type: Episodic / Multi-Session
year: "2025"
primary_source_kind: paper
primary_source_url: https://arxiv.org/abs/2406.13144
counterpart_en: ../../en/04_dialogue_memory/dialsim.md
---

# DialSim

[中文知识库索引](../README.md) | [English Card](../../en/04_dialogue_memory/dialsim.md)

## 结构化信息

| 字段 | 内容 |
|---|---|
| Benchmark | DialSim |
| 分类 | 多会话对话记忆与个性化 |
| 子类 | 长期对话记忆 |
| 记忆侧重 | Episodic / Multi-Session |
| 首次年份 | 2025 |
| 主要来源类型 | paper |
| 论文标题 | DialSim: A Dialogue Simulator for Evaluating Long-Term Multi-Party Dialogue Understanding of Conversational Agents |
| 英文卡片 | [DialSim](../../en/04_dialogue_memory/dialsim.md) |

## 基础介绍

定义：为评估“长期多方对话理解”而提出对话模拟器；论文/摘要提到平均对话长度可达 350k tokens，并含不可回答问题。

## Abstract
### 原始摘要
> Recent advancements in Large Language Models (LLMs) have significantly enhanced conversational agents, making them applicable to various fields (e.g., education, entertainment). Despite their progress, the evaluation of the agents often overlooks the complexities of real-world conversations, such as multi-party dialogues and extended contextual dependencies. To bridge this gap, we introduce DialSim, a dialogue simulation-based evaluation framework. In DialSim, an agent assumes the role of a character in a scripted conversation and is evaluated on their ability to answer spontaneous questions using only the dialogue history, while recognizing when they lack sufficient information. To support this framework, we introduce LongDialQA, a new QA dataset constructed from long-running TV shows, comprising over 1,300 dialogue sessions, each paired with more than 1,000 carefully curated questions, totaling over 352,000 tokens. To minimize reliance on prior knowledge, all character names are anonymized or swapped. Our evaluation of state-of-the-art LLM-based conversational agents using DialSim reveals that even models with large context windows or RAG capabilities struggle to maintain accurate comprehension over long-term, multi-party interactions-underscoring the need for more realistic and challenging benchmarks in conversational AI.

### 中文抽取
定义：为评估“长期多方对话理解”而提出对话模拟器；论文/摘要提到平均对话长度可达 350k tokens，并含不可回答问题。

## URL 汇总

| 类型 | 链接 |
|---|---|
| 论文页 | https://arxiv.org/abs/2406.13144 |

## BibTeX

```bibtex
@misc{https://doi.org/10.48550/arxiv.2406.13144,
  doi = {10.48550/ARXIV.2406.13144},
  url = {https://arxiv.org/abs/2406.13144},
  author = {Kim, Jiho and Chay, Woosog and Hwang, Hyeonji and Kyung, Daeun and Chung, Hyunseung and Cho, Eunbyeol and Kwon, Yeonsu and Jo, Yohan and Choi, Edward},
  keywords = {Computation and Language (cs.CL), Artificial Intelligence (cs.AI), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {DialSim: A Dialogue Simulator for Evaluating Long-Term Multi-Party Dialogue Understanding of Conversational Agents},
  publisher = {arXiv},
  year = {2024},
  copyright = {arXiv.org perpetual, non-exclusive license}
}
```

## 备注

- 本卡片优先使用论文页、项目页与代码仓库等官方来源；若原报告中的链接存在错误，则以标题匹配后的官方链接为准。
