---
name: Mem-Gallery
slug: mem-gallery
language: en
category: Multi-Session Dialogue Memory and Personalization
subcategory: Long-Term Dialogue Memory
memory_type: Episodic / Multi-Session
year: "2026"
primary_source_kind: paper
primary_source_url: https://arxiv.org/abs/2601.03515
counterpart_zh: ../../zh/04_dialogue_memory/mem-gallery.md
---

# Mem-Gallery

[English Knowledge Base Index](../README.md) | [中文卡片](../../zh/04_dialogue_memory/mem-gallery.md)

## Structured Metadata

| Field | Content |
|---|---|
| Benchmark | Mem-Gallery |
| Category | Multi-Session Dialogue Memory and Personalization |
| Subcategory | Long-Term Dialogue Memory |
| Memory Focus | Episodic / Multi-Session |
| First Year | 2026 |
| Primary Source Type | paper |
| Paper Title | Mem-Gallery: Benchmarking Multimodal Long-Term Conversational Memory for MLLM Agents |
| Chinese Card | [Mem-Gallery](../../zh/04_dialogue_memory/mem-gallery.md) |

## Overview

A multimodal long-term conversational memory benchmark for MLLM agents across multi-session interactions.

## Abstract
### Original Abstract
> Long-term memory is a critical capability for multimodal large language model (MLLM) agents, particularly in conversational settings where information accumulates and evolves over time. However, existing benchmarks either evaluate multi-session memory in text-only conversations or assess multimodal understanding within localized contexts, failing to evaluate how multimodal memory is preserved, organized, and evolved across long-term conversational trajectories. Thus, we introduce Mem-Gallery, a new benchmark for evaluating multimodal long-term conversational memory in MLLM agents. Mem-Gallery features high-quality multi-session conversations grounded in both visual and textual information, with long interaction horizons and rich multimodal dependencies. Building on this dataset, we propose a systematic evaluation framework that assesses key memory capabilities along three functional dimensions: memory extraction and test-time adaptation, memory reasoning, and memory knowledge management. Extensive benchmarking across thirteen memory systems reveals several key findings, highlighting the necessity of explicit multimodal information retention and memory organization, the persistent limitations in memory reasoning and knowledge management, as well as the efficiency bottleneck of current models.

### Curated Summary
A multimodal long-term conversational memory benchmark for MLLM agents across multi-session interactions.

## Links

| Type | Link |
|---|---|
| Paper | https://arxiv.org/abs/2601.03515 |
| Project Page | https://mem-gallery.github.io/ |
| GitHub | https://github.com/YuanchenBei/Mem-Gallery |

## BibTeX

```bibtex
@misc{https://doi.org/10.48550/arxiv.2601.03515,
  doi = {10.48550/ARXIV.2601.03515},
  url = {https://arxiv.org/abs/2601.03515},
  author = {Bei, Yuanchen and Wei, Tianxin and Ning, Xuying and Zhao, Yanjun and Liu, Zhining and Lin, Xiao and Zhu, Yada and Hamann, Hendrik and He, Jingrui and Tong, Hanghang},
  keywords = {Computation and Language (cs.CL), Artificial Intelligence (cs.AI), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {Mem-Gallery: Benchmarking Multimodal Long-Term Conversational Memory for MLLM Agents},
  publisher = {arXiv},
  year = {2026},
  copyright = {arXiv.org perpetual, non-exclusive license}
}
```

## Remarks

- The original arXiv link was incorrect. This card replaces it with the official Mem-Gallery paper.
