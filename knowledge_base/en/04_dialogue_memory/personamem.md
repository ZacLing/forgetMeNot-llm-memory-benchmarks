---
name: PersonaMem
slug: personamem
language: en
category: Multi-Session Dialogue Memory and Personalization
subcategory: 个性化与真实多会话
memory_type: Episodic / Multi-Session
year: "2025"
primary_source_kind: paper
primary_source_url: https://arxiv.org/abs/2504.14225
counterpart_zh: ../../zh/04_dialogue_memory/personamem.md
---

# PersonaMem

[English Knowledge Base Index](../README.md) | [中文卡片](../../zh/04_dialogue_memory/personamem.md)

## Structured Metadata

| Field | Content |
|---|---|
| Benchmark | PersonaMem |
| Category | Multi-Session Dialogue Memory and Personalization |
| Subcategory | 个性化与真实多会话 |
| Memory Focus | Episodic / Multi-Session |
| First Year | 2025 |
| Primary Source Type | paper |
| Paper Title | Know Me, Respond to Me: Benchmarking LLMs for Dynamic User Profiling and Personalized Responses at Scale |
| Chinese Card | [PersonaMem](../../zh/04_dialogue_memory/personamem.md) |

## Overview

A dynamic personalization benchmark that evaluates whether LLMs track evolving user traits and preferences over time.

## Abstract
### Original Abstract
> Large Language Models (LLMs) have emerged as personalized assistants for users across a wide range of tasks -- from offering writing support to delivering tailored recommendations or consultations. Over time, the interaction history between a user and an LLM can provide extensive information about an individual's traits and preferences. However, open questions remain on how well LLMs today can effectively leverage such history to (1) internalize the user's inherent traits and preferences, (2) track how the user profiling and preferences evolve over time, and (3) generate personalized responses accordingly in new scenarios. In this work, we introduce the PERSONAMEM benchmark. PERSONAMEM features curated user profiles with over 180 simulated user-LLM interaction histories, each containing up to 60 sessions of multi-turn conversations across 15 real-world tasks that require personalization. Given an in-situ user query, i.e. query issued by the user from the first-person perspective, we evaluate LLM chatbots' ability to identify the most suitable response according to the current state of the user's profile. We observe that current LLMs still struggle to recognize the dynamic evolution in users' profiles over time through direct prompting approaches. As a consequence, LLMs often fail to deliver responses that align with users' current situations and preferences, with frontier models such as GPT-4.1, o4-mini, GPT-4.5, o1, or Gemini-2.0 achieving only around 50% overall accuracy, suggesting room for improvement. We hope that PERSONAMEM, along with the user profile and conversation simulation pipeline, can facilitate future research in the development of truly user-aware chatbots. Code and data are available at github.com/bowen-upenn/PersonaMem.

### Curated Summary
A dynamic personalization benchmark that evaluates whether LLMs track evolving user traits and preferences over time.

## Links

| Type | Link |
|---|---|
| Paper | https://arxiv.org/abs/2504.14225 |
| Project Page | https://zhuoqunhao.github.io/PersonaMem.github.io/ |
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

## Remarks

- The original report only included an OpenReview link. This card additionally provides the arXiv version and official code page so that the abstract and BibTeX can be accessed directly.
