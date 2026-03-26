---
name: RealTalk
slug: realtalk
language: zh
category: 多会话对话记忆与个性化
subcategory: 长期对话记忆
memory_type: Episodic / Multi-Session
year: "2025"
primary_source_kind: paper
primary_source_url: https://arxiv.org/abs/2502.13270
counterpart_en: ../../en/04_dialogue_memory/realtalk.md
---

# RealTalk

[中文知识库索引](../README.md) | [English Card](../../en/04_dialogue_memory/realtalk.md)

## 结构化信息

| 字段 | 内容 |
|---|---|
| Benchmark | RealTalk |
| 分类 | 多会话对话记忆与个性化 |
| 子类 | 长期对话记忆 |
| 记忆侧重 | Episodic / Multi-Session |
| 首次年份 | 2025 |
| 主要来源类型 | paper |
| 论文标题 | REALTALK: A 21-Day Real-World Dataset for Long-Term Conversation |
| 英文卡片 | [RealTalk](../../en/04_dialogue_memory/realtalk.md) |

## 基础介绍

定义：21 天语料，用于评测长期会话记忆。

## Abstract
### 原始摘要
> Long-term, open-domain dialogue capabilities are essential for chatbots aiming to recall past interactions and demonstrate emotional intelligence (EI). Yet, most existing research relies on synthetic, LLM-generated data, leaving open questions about real-world conversational patterns. To address this gap, we introduce REALTALK, a 21-day corpus of authentic messaging app dialogues, providing a direct benchmark against genuine human interactions. We first conduct a dataset analysis, focusing on EI attributes and persona consistency to understand the unique challenges posed by real-world dialogues. By comparing with LLM-generated conversations, we highlight key differences, including diverse emotional expressions and variations in persona stability that synthetic dialogues often fail to capture. Building on these insights, we introduce two benchmark tasks: (1) persona simulation where a model continues a conversation on behalf of a specific user given prior dialogue context; and (2) memory probing where a model answers targeted questions requiring long-term memory of past interactions. Our findings reveal that models struggle to simulate a user solely from dialogue history, while fine-tuning on specific user chats improves persona emulation. Additionally, existing models face significant challenges in recalling and leveraging long-term context within real-world conversations.

### 中文抽取
定义：21 天语料，用于评测长期会话记忆。

## URL 汇总

| 类型 | 链接 |
|---|---|
| 论文页 | https://arxiv.org/abs/2502.13270 |
| GitHub | https://github.com/danny911kr/REALTALK |

## BibTeX

```bibtex
@misc{https://doi.org/10.48550/arxiv.2502.13270,
  doi = {10.48550/ARXIV.2502.13270},
  url = {https://arxiv.org/abs/2502.13270},
  author = {Lee, Dong-Ho and Maharana, Adyasha and Pujara, Jay and Ren, Xiang and Barbieri, Francesco},
  keywords = {Computation and Language (cs.CL), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {REALTALK: A 21-Day Real-World Dataset for Long-Term Conversation},
  publisher = {arXiv},
  year = {2025},
  copyright = {Creative Commons Attribution 4.0 International}
}
```

## 备注

- 原报告中的 arXiv 与 GitHub 链接均与 benchmark 不一致，这里改为与 REALTALK 论文标题一致的官方资源。
