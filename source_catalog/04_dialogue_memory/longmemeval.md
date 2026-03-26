---
name: LongMemEval
slug: longmemeval
category: 多会话对话记忆与个性化
subcategory: 长期对话记忆
memory_type: Episodic / Multi-Session
year: "2025"
primary_source_kind: paper
primary_source_url: https://arxiv.org/abs/2410.10813
---

# LongMemEval

## 结构化信息

| 字段 | 内容 |
|---|---|
| Benchmark | LongMemEval |
| 分类 | 多会话对话记忆与个性化 |
| 子类 | 长期对话记忆 |
| 记忆侧重 | Episodic / Multi-Session |
| 首次年份 | 2025 |
| 主要来源类型 | paper |
| 论文标题 | LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory |

## 基础介绍

设置：把 500 个问题嵌入可扩展对话历史，对聊天助手的“长期交互记忆”做 benchmark；强调有统一环境与可扩展对话历史。

## Abstract
### 原始摘要
> Recent large language model (LLM)-driven chat assistant systems have integrated memory components to track user-assistant chat histories, enabling more accurate and personalized responses. However, their long-term memory capabilities in sustained interactions remain underexplored. We introduce LongMemEval, a comprehensive benchmark designed to evaluate five core long-term memory abilities of chat assistants: information extraction, multi-session reasoning, temporal reasoning, knowledge updates, and abstention. With 500 meticulously curated questions embedded within freely scalable user-assistant chat histories, LongMemEval presents a significant challenge to existing long-term memory systems, with commercial chat assistants and long-context LLMs showing a 30% accuracy drop on memorizing information across sustained interactions. We then present a unified framework that breaks down the long-term memory design into three stages: indexing, retrieval, and reading. Built upon key experimental insights, we propose several memory design optimizations including session decomposition for value granularity, fact-augmented key expansion for indexing, and time-aware query expansion for refining the search scope. Extensive experiments show that these optimizations greatly improve both memory recall and downstream question answering on LongMemEval. Overall, our study provides valuable resources and guidance for advancing the long-term memory capabilities of LLM-based chat assistants, paving the way toward more personalized and reliable conversational AI. Our benchmark and code are publicly available at https://github.com/xiaowu0162/LongMemEval.

### 中文抽取
设置：把 500 个问题嵌入可扩展对话历史，对聊天助手的“长期交互记忆”做 benchmark；强调有统一环境与可扩展对话历史。

## URL 汇总

| 类型 | 链接 |
|---|---|
| 论文页 | https://arxiv.org/abs/2410.10813 |
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

## 备注

- 本卡片优先使用论文页、项目页与代码仓库等官方来源；若原报告中的链接存在错误，则以标题匹配后的官方链接为准。
