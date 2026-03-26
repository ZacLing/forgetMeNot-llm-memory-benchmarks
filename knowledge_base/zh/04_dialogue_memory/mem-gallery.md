---
name: Mem-Gallery
slug: mem-gallery
language: zh
category: 多会话对话记忆与个性化
subcategory: 长期对话记忆
memory_type: Episodic / Multi-Session
year: "2026"
primary_source_kind: paper
primary_source_url: https://arxiv.org/abs/2601.03515
counterpart_en: ../../en/04_dialogue_memory/mem-gallery.md
---

# Mem-Gallery

[中文知识库索引](../README.md) | [English Card](../../en/04_dialogue_memory/mem-gallery.md)

## 结构化信息

| 字段 | 内容 |
|---|---|
| Benchmark | Mem-Gallery |
| 分类 | 多会话对话记忆与个性化 |
| 子类 | 长期对话记忆 |
| 记忆侧重 | Episodic / Multi-Session |
| 首次年份 | 2026 |
| 主要来源类型 | paper |
| 论文标题 | Mem-Gallery: Benchmarking Multimodal Long-Term Conversational Memory for MLLM Agents |
| 英文卡片 | [Mem-Gallery](../../en/04_dialogue_memory/mem-gallery.md) |

## 基础介绍

定位：评测多模态 agent 的长期会话记忆（综述页给出）。

## Abstract
### 原始摘要
> Long-term memory is a critical capability for multimodal large language model (MLLM) agents, particularly in conversational settings where information accumulates and evolves over time. However, existing benchmarks either evaluate multi-session memory in text-only conversations or assess multimodal understanding within localized contexts, failing to evaluate how multimodal memory is preserved, organized, and evolved across long-term conversational trajectories. Thus, we introduce Mem-Gallery, a new benchmark for evaluating multimodal long-term conversational memory in MLLM agents. Mem-Gallery features high-quality multi-session conversations grounded in both visual and textual information, with long interaction horizons and rich multimodal dependencies. Building on this dataset, we propose a systematic evaluation framework that assesses key memory capabilities along three functional dimensions: memory extraction and test-time adaptation, memory reasoning, and memory knowledge management. Extensive benchmarking across thirteen memory systems reveals several key findings, highlighting the necessity of explicit multimodal information retention and memory organization, the persistent limitations in memory reasoning and knowledge management, as well as the efficiency bottleneck of current models.

### 中文抽取
定位：评测多模态 agent 的长期会话记忆（综述页给出）。

## URL 汇总

| 类型 | 链接 |
|---|---|
| 论文页 | https://arxiv.org/abs/2601.03515 |
| 项目主页 | https://mem-gallery.github.io/ |
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

## 备注

- 原报告中的 arXiv 链接有误，已替换为 Mem-Gallery 官方论文。
