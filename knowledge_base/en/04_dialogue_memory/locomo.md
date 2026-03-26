---
name: LoCoMo
slug: locomo
language: en
category: Multi-Session Dialogue Memory and Personalization
subcategory: Long-Term Dialogue Memory
memory_type: Episodic / Multi-Session
year: "2024"
primary_source_kind: paper
primary_source_url: https://arxiv.org/abs/2402.17753
counterpart_zh: ../../zh/04_dialogue_memory/locomo.md
---

# LoCoMo

[English Knowledge Base Index](../README.md) | [中文卡片](../../zh/04_dialogue_memory/locomo.md)

## Structured Metadata

| Field | Content |
|---|---|
| Benchmark | LoCoMo |
| Category | Multi-Session Dialogue Memory and Personalization |
| Subcategory | Long-Term Dialogue Memory |
| Memory Focus | Episodic / Multi-Session |
| First Year | 2024 |
| Primary Source Type | paper |
| Paper Title | Evaluating Very Long-Term Conversational Memory of LLM Agents |
| Chinese Card | [LoCoMo](../../zh/04_dialogue_memory/locomo.md) |

## Overview

A benchmark of very long-term conversational memory with event-grounded multi-session dialogues.

## Abstract
### Original Abstract
> Existing works on long-term open-domain dialogues focus on evaluating model responses within contexts spanning no more than five chat sessions. Despite advancements in long-context large language models (LLMs) and retrieval augmented generation (RAG) techniques, their efficacy in very long-term dialogues remains unexplored. To address this research gap, we introduce a machine-human pipeline to generate high-quality, very long-term dialogues by leveraging LLM-based agent architectures and grounding their dialogues on personas and temporal event graphs. Moreover, we equip each agent with the capability of sharing and reacting to images. The generated conversations are verified and edited by human annotators for long-range consistency and grounding to the event graphs. Using this pipeline, we collect LoCoMo, a dataset of very long-term conversations, each encompassing 300 turns and 9K tokens on avg., over up to 35 sessions. Based on LoCoMo, we present a comprehensive evaluation benchmark to measure long-term memory in models, encompassing question answering, event summarization, and multi-modal dialogue generation tasks. Our experimental results indicate that LLMs exhibit challenges in understanding lengthy conversations and comprehending long-range temporal and causal dynamics within dialogues. Employing strategies like long-context LLMs or RAG can offer improvements but these models still substantially lag behind human performance.

### Curated Summary
A benchmark of very long-term conversational memory with event-grounded multi-session dialogues.

## Links

| Type | Link |
|---|---|
| Paper | https://arxiv.org/abs/2402.17753 |
| Paper PDF | https://aclanthology.org/2024.acl-long.747.pdf |
| Project Page | https://snap-research.github.io/locomo/ |
| GitHub | https://github.com/snap-research/LoCoMo |

## BibTeX

```bibtex
@misc{https://doi.org/10.48550/arxiv.2402.17753,
  doi = {10.48550/ARXIV.2402.17753},
  url = {https://arxiv.org/abs/2402.17753},
  author = {Maharana, Adyasha and Lee, Dong-Ho and Tulyakov, Sergey and Bansal, Mohit and Barbieri, Francesco and Fang, Yuwei},
  keywords = {Computation and Language (cs.CL), Artificial Intelligence (cs.AI), Machine Learning (cs.LG), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {Evaluating Very Long-Term Conversational Memory of LLM Agents},
  publisher = {arXiv},
  year = {2024},
  copyright = {Creative Commons Attribution Non Commercial Share Alike 4.0 International}
}
```

## Remarks

- The original report pointed to an unrelated arXiv page. This card corrects it to the official LoCoMo paper.
