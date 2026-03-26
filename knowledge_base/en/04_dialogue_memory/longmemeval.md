---
name: LongMemEval
slug: longmemeval
language: en
category: Multi-Session Dialogue Memory and Personalization
subcategory: 长期对话记忆
memory_type: Episodic / Multi-Session
year: "2025"
primary_source_kind: paper
primary_source_url: https://arxiv.org/abs/2410.10813
counterpart_zh: ../../zh/04_dialogue_memory/longmemeval.md
---

# LongMemEval

[English Knowledge Base Index](../README.md) | [中文卡片](../../zh/04_dialogue_memory/longmemeval.md)

## Structured Metadata

| Field | Content |
|---|---|
| Benchmark | LongMemEval |
| Category | Multi-Session Dialogue Memory and Personalization |
| Subcategory | 长期对话记忆 |
| Memory Focus | Episodic / Multi-Session |
| First Year | 2025 |
| Primary Source Type | paper |
| Paper Title | LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory |
| Chinese Card | [LongMemEval](../../zh/04_dialogue_memory/longmemeval.md) |

## Overview

An interactive benchmark that embeds 500 questions into expandable chat histories for long-term assistant memory.

## Abstract
### Original Abstract
> Recent large language model (LLM)-driven chat assistant systems have integrated memory components to track user-assistant chat histories, enabling more accurate and personalized responses. However, their long-term memory capabilities in sustained interactions remain underexplored. We introduce LongMemEval, a comprehensive benchmark designed to evaluate five core long-term memory abilities of chat assistants: information extraction, multi-session reasoning, temporal reasoning, knowledge updates, and abstention. With 500 meticulously curated questions embedded within freely scalable user-assistant chat histories, LongMemEval presents a significant challenge to existing long-term memory systems, with commercial chat assistants and long-context LLMs showing a 30% accuracy drop on memorizing information across sustained interactions. We then present a unified framework that breaks down the long-term memory design into three stages: indexing, retrieval, and reading. Built upon key experimental insights, we propose several memory design optimizations including session decomposition for value granularity, fact-augmented key expansion for indexing, and time-aware query expansion for refining the search scope. Extensive experiments show that these optimizations greatly improve both memory recall and downstream question answering on LongMemEval. Overall, our study provides valuable resources and guidance for advancing the long-term memory capabilities of LLM-based chat assistants, paving the way toward more personalized and reliable conversational AI. Our benchmark and code are publicly available at https://github.com/xiaowu0162/LongMemEval.

### Curated Summary
An interactive benchmark that embeds 500 questions into expandable chat histories for long-term assistant memory.

## Links

| Type | Link |
|---|---|
| Paper | https://arxiv.org/abs/2410.10813 |
| GitHub | https://github.com/google-deepmind/long-mem-eval |

## BibTeX

```bibtex
@misc{https://doi.org/10.48550/arxiv.2410.10813,
  doi = {10.48550/ARXIV.2410.10813},
  url = {https://arxiv.org/abs/2410.10813},
  author = {Wu, Di and Wang, Hongwei and Yu, Wenhao and Zhang, Yuwei and Chang, Kai-Wei and Yu, Dong},
  keywords = {Computation and Language (cs.CL), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory},
  publisher = {arXiv},
  year = {2024},
  copyright = {Creative Commons Attribution 4.0 International}
}
```

## Remarks

- This card prioritizes official paper pages, project pages, and code repositories. When a link in the original report was incorrect, the corrected official link is used instead.
