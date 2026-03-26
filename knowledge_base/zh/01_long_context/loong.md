---
name: Loong
slug: loong
language: zh
category: 长上下文理解与推理
subcategory: 长上下文综合任务
memory_type: Working / In-Context
year: "2024"
primary_source_kind: paper
primary_source_url: https://arxiv.org/abs/2406.17419
counterpart_en: ../../en/01_long_context/loong.md
---

# Loong

[中文知识库索引](../README.md) | [English Card](../../en/01_long_context/loong.md)

## 结构化信息

| 字段 | 内容 |
|---|---|
| Benchmark | Loong |
| 分类 | 长上下文理解与推理 |
| 子类 | 长上下文综合任务 |
| 记忆侧重 | Working / In-Context |
| 首次年份 | 2024 |
| 主要来源类型 | paper |
| 论文标题 | Leave No Document Behind: Benchmarking Long-Context LLMs with Extended Multi-Doc QA |
| 英文卡片 | [Loong](../../en/01_long_context/loong.md) |

## 基础介绍

核心设计：不同于“用无关噪声补长度”，Loong 让每份文档都与答案相关，“漏掉任何文档会失败”；任务类型包括 Spotlight Locating、Comparison、Clustering、Chain of Reasoning；并提供中英场景（金融报告、法律案例、论文）。

## Abstract
### 原始摘要
> Long-context modeling capabilities have garnered widespread attention, leading to the emergence of Large Language Models (LLMs) with ultra-context windows. Meanwhile, benchmarks for evaluating long-context LLMs are gradually catching up. However, existing benchmarks employ irrelevant noise texts to artificially extend the length of test cases, diverging from the real-world scenarios of long-context applications. To bridge this gap, we propose a novel long-context benchmark, Loong, aligning with realistic scenarios through extended multi-document question answering (QA). Unlike typical document QA, in Loong's test cases, each document is relevant to the final answer, ignoring any document will lead to the failure of the answer. Furthermore, Loong introduces four types of tasks with a range of context lengths: Spotlight Locating, Comparison, Clustering, and Chain of Reasoning, to facilitate a more realistic and comprehensive evaluation of long-context understanding. Extensive experiments indicate that existing long-context language models still exhibit considerable potential for enhancement. Retrieval augmented generation (RAG) achieves poor performance, demonstrating that Loong can reliably assess the model's long-context modeling capabilities.

### 中文抽取
核心设计：不同于“用无关噪声补长度”，Loong 让每份文档都与答案相关，“漏掉任何文档会失败”；任务类型包括 Spotlight Locating、Comparison、Clustering、Chain of Reasoning；并提供中英场景（金融报告、法律案例、论文）。

## URL 汇总

| 类型 | 链接 |
|---|---|
| 论文页 | https://arxiv.org/abs/2406.17419 |
| GitHub | https://github.com/MozerWang/Loong |
| other_emnlp-pdf_url | https://aclanthology.org/2024.emnlp-main.322.pdf |

## BibTeX

```bibtex
@misc{https://doi.org/10.48550/arxiv.2406.17419,
  doi = {10.48550/ARXIV.2406.17419},
  url = {https://arxiv.org/abs/2406.17419},
  author = {Wang, Minzheng and Chen, Longze and Fu, Cheng and Liao, Shengyi and Zhang, Xinghua and Wu, Bingli and Yu, Haiyang and Xu, Nan and Zhang, Lei and Luo, Run and Li, Yunshui and Yang, Min and Huang, Fei and Li, Yongbin},
  keywords = {Computation and Language (cs.CL), Artificial Intelligence (cs.AI), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {Leave No Document Behind: Benchmarking Long-Context LLMs with Extended Multi-Doc QA},
  publisher = {arXiv},
  year = {2024},
  copyright = {arXiv.org perpetual, non-exclusive license}
}
```

## 备注

- 本卡片优先使用论文页、项目页与代码仓库等官方来源；若原报告中的链接存在错误，则以标题匹配后的官方链接为准。
