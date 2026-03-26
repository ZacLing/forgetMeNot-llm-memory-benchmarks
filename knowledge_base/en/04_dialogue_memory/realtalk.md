---
name: RealTalk
slug: realtalk
language: en
category: Multi-Session Dialogue Memory and Personalization
subcategory: Long-Term Dialogue Memory
memory_type: Episodic / Multi-Session
year: "2025"
primary_source_kind: paper
primary_source_url: https://arxiv.org/abs/2502.13270
counterpart_zh: ../../zh/04_dialogue_memory/realtalk.md
---

# RealTalk

[English Knowledge Base Index](../README.md) | [中文卡片](../../zh/04_dialogue_memory/realtalk.md)

## Structured Metadata

| Field | Content |
|---|---|
| Benchmark | RealTalk |
| Category | Multi-Session Dialogue Memory and Personalization |
| Subcategory | Long-Term Dialogue Memory |
| Memory Focus | Episodic / Multi-Session |
| First Year | 2025 |
| Primary Source Type | paper |
| Paper Title | REALTALK: A 21-Day Real-World Dataset for Long-Term Conversation |
| Chinese Card | [RealTalk](../../zh/04_dialogue_memory/realtalk.md) |

## Overview

A 21-day real-world conversation dataset and benchmark for long-term open-domain dialogue memory.

## Abstract
### Original Abstract
> Long-term, open-domain dialogue capabilities are essential for chatbots aiming to recall past interactions and demonstrate emotional intelligence (EI). Yet, most existing research relies on synthetic, LLM-generated data, leaving open questions about real-world conversational patterns. To address this gap, we introduce REALTALK, a 21-day corpus of authentic messaging app dialogues, providing a direct benchmark against genuine human interactions. We first conduct a dataset analysis, focusing on EI attributes and persona consistency to understand the unique challenges posed by real-world dialogues. By comparing with LLM-generated conversations, we highlight key differences, including diverse emotional expressions and variations in persona stability that synthetic dialogues often fail to capture. Building on these insights, we introduce two benchmark tasks: (1) persona simulation where a model continues a conversation on behalf of a specific user given prior dialogue context; and (2) memory probing where a model answers targeted questions requiring long-term memory of past interactions. Our findings reveal that models struggle to simulate a user solely from dialogue history, while fine-tuning on specific user chats improves persona emulation. Additionally, existing models face significant challenges in recalling and leveraging long-term context within real-world conversations.

### Curated Summary
A 21-day real-world conversation dataset and benchmark for long-term open-domain dialogue memory.

## Links

| Type | Link |
|---|---|
| Paper | https://arxiv.org/abs/2502.13270 |
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

## Remarks

- Both the arXiv and GitHub links in the original report were mismatched. This card replaces them with official REALTALK resources.
