---
name: MemoryBench
slug: memorybench
language: zh
category: 智能体记忆与持续学习
subcategory: 持续学习与反馈记忆
memory_type: Agentic / Procedural / Continual
year: "2025"
primary_source_kind: paper
primary_source_url: https://arxiv.org/abs/2510.17281
counterpart_en: ../../en/05_agent_memory/memorybench.md
---

# MemoryBench

[中文知识库索引](../README.md) | [English Card](../../en/05_agent_memory/memorybench.md)

## 结构化信息

| 字段 | 内容 |
|---|---|
| Benchmark | MemoryBench |
| 分类 | 智能体记忆与持续学习 |
| 子类 | 持续学习与反馈记忆 |
| 记忆侧重 | Agentic / Procedural / Continual |
| 首次年份 | 2025 |
| 主要来源类型 | paper |
| 论文标题 | MemoryBench: A Benchmark for Memory and Continual Learning in LLM Systems |
| 英文卡片 | [MemoryBench](../../en/05_agent_memory/memorybench.md) |

## 基础介绍

定义：指出既有“LLM memory benchmark”偏阅读理解长输入，缺少“服务期从用户反馈中持续学习”的评测；提出用户反馈模拟框架与多域多语言 benchmark。

## Abstract
### 原始摘要
> Scaling up data, parameters, and test-time computation has been the mainstream methods to improve LLM systems (LLMsys), but their upper bounds are almost reached due to the gradual depletion of high-quality data and marginal gains obtained from larger computational resource consumption. Inspired by the abilities of human and traditional AI systems in learning from practice, constructing memory and continual learning frameworks for LLMsys has become an important and popular research direction in recent literature. Yet, existing benchmarks for LLM memory often focus on evaluating the system on homogeneous reading comprehension tasks with long-form inputs rather than testing their abilities to learn from accumulated user feedback in service time. Therefore, we propose a user feedback simulation framework and a comprehensive benchmark covering multiple domains, languages, and types of tasks to evaluate the continual learning abilities of LLMsys. Experiments show that the effectiveness and efficiency of state-of-the-art baselines are far from satisfying, and we hope this benchmark could pave the way for future studies on LLM memory and optimization algorithms.

### 中文抽取
定义：指出既有“LLM memory benchmark”偏阅读理解长输入，缺少“服务期从用户反馈中持续学习”的评测；提出用户反馈模拟框架与多域多语言 benchmark。

## URL 汇总

| 类型 | 链接 |
|---|---|
| 论文页 | https://arxiv.org/abs/2510.17281 |
| 论文 HTML | https://arxiv.org/html/2510.17281v4 |

## BibTeX

```bibtex
@misc{https://doi.org/10.48550/arxiv.2510.17281,
  doi = {10.48550/ARXIV.2510.17281},
  url = {https://arxiv.org/abs/2510.17281},
  author = {Ai, Qingyao and Tang, Yichen and Wang, Changyue and Long, Jianming and Su, Weihang and Liu, Yiqun},
  keywords = {Machine Learning (cs.LG), Artificial Intelligence (cs.AI), Information Retrieval (cs.IR), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {MemoryBench: A Benchmark for Memory and Continual Learning in LLM Systems},
  publisher = {arXiv},
  year = {2025},
  copyright = {arXiv.org perpetual, non-exclusive license}
}
```

## 备注

- 本卡片优先使用论文页、项目页与代码仓库等官方来源；若原报告中的链接存在错误，则以标题匹配后的官方链接为准。
