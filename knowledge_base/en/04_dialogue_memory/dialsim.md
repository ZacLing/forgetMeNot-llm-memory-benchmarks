---
name: DialSim
slug: dialsim
language: en
category: Multi-Session Dialogue Memory and Personalization
subcategory: Long-Term Dialogue Memory
memory_type: Episodic / Multi-Session
year: "2025"
primary_source_kind: paper
primary_source_url: https://arxiv.org/abs/2406.13144
counterpart_zh: ../../zh/04_dialogue_memory/dialsim.md
---

# DialSim

[English Knowledge Base Index](../README.md) | [中文卡片](../../zh/04_dialogue_memory/dialsim.md)

## Structured Metadata

| Field | Content |
|---|---|
| Benchmark | DialSim |
| Category | Multi-Session Dialogue Memory and Personalization |
| Subcategory | Long-Term Dialogue Memory |
| Memory Focus | Episodic / Multi-Session |
| First Year | 2025 |
| Primary Source Type | paper |
| Paper Title | DialSim: A Dialogue Simulator for Evaluating Long-Term Multi-Party Dialogue Understanding of Conversational Agents |
| Chinese Card | [DialSim](../../zh/04_dialogue_memory/dialsim.md) |

## Overview

A dialogue simulator for long multi-party conversations, including very long contexts and unanswerable cases.

## Abstract
### Original Abstract
> Recent advancements in Large Language Models (LLMs) have significantly enhanced conversational agents, making them applicable to various fields (e.g., education, entertainment). Despite their progress, the evaluation of the agents often overlooks the complexities of real-world conversations, such as multi-party dialogues and extended contextual dependencies. To bridge this gap, we introduce DialSim, a dialogue simulation-based evaluation framework. In DialSim, an agent assumes the role of a character in a scripted conversation and is evaluated on their ability to answer spontaneous questions using only the dialogue history, while recognizing when they lack sufficient information. To support this framework, we introduce LongDialQA, a new QA dataset constructed from long-running TV shows, comprising over 1,300 dialogue sessions, each paired with more than 1,000 carefully curated questions, totaling over 352,000 tokens. To minimize reliance on prior knowledge, all character names are anonymized or swapped. Our evaluation of state-of-the-art LLM-based conversational agents using DialSim reveals that even models with large context windows or RAG capabilities struggle to maintain accurate comprehension over long-term, multi-party interactions-underscoring the need for more realistic and challenging benchmarks in conversational AI.

### Curated Summary
A dialogue simulator for long multi-party conversations, including very long contexts and unanswerable cases.

## Links

| Type | Link |
|---|---|
| Paper | https://arxiv.org/abs/2406.13144 |

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

## Remarks

- This card prioritizes official paper pages, project pages, and code repositories. When a link in the original report was incorrect, the corrected official link is used instead.
