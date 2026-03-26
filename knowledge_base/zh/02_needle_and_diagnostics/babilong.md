---
name: BABILong
slug: babilong
language: zh
category: 长上下文针类诊断
subcategory: Needle / Passkey / 合成诊断
memory_type: Working / In-Context
year: "2024"
primary_source_kind: paper
primary_source_url: https://arxiv.org/abs/2406.10149
counterpart_en: ../../en/02_needle_and_diagnostics/babilong.md
---

# BABILong

[中文知识库索引](../README.md) | [English Card](../../en/02_needle_and_diagnostics/babilong.md)

## 结构化信息

| 字段 | 内容 |
|---|---|
| Benchmark | BABILong |
| 分类 | 长上下文针类诊断 |
| 子类 | Needle / Passkey / 合成诊断 |
| 记忆侧重 | Working / In-Context |
| 首次年份 | 2024 |
| 主要来源类型 | paper |
| 论文标题 | BABILong: Testing the Limits of LLMs with Long Context Reasoning-in-a-Haystack |
| 英文卡片 | [BABILong](../../en/02_needle_and_diagnostics/babilong.md) |

## 基础介绍

设计：把 bAbI 风格推理任务嵌入超长文档（“推理在干草堆里”），包含 20 推理任务。

## Abstract
### 原始摘要
> In recent years, the input context sizes of large language models (LLMs) have increased dramatically. However, existing evaluation methods have not kept pace, failing to comprehensively assess the efficiency of models in handling long contexts. To bridge this gap, we introduce the BABILong benchmark, designed to test language models' ability to reason across facts distributed in extremely long documents. BABILong includes a diverse set of 20 reasoning tasks, including fact chaining, simple induction, deduction, counting, and handling lists/sets. These tasks are challenging on their own, and even more demanding when the required facts are scattered across long natural text. Our evaluations show that popular LLMs effectively utilize only 10-20\% of the context and their performance declines sharply with increased reasoning complexity. Among alternatives to in-context reasoning, Retrieval-Augmented Generation methods achieve a modest 60\% accuracy on single-fact question answering, independent of context length. Among context extension methods, the highest performance is demonstrated by recurrent memory transformers after fine-tuning, enabling the processing of lengths up to 50 million tokens. The BABILong benchmark is extendable to any length to support the evaluation of new upcoming models with increased capabilities, and we provide splits up to 10 million token lengths.

### 中文抽取
设计：把 bAbI 风格推理任务嵌入超长文档（“推理在干草堆里”），包含 20 推理任务。

## URL 汇总

| 类型 | 链接 |
|---|---|
| 论文页 | https://arxiv.org/abs/2406.10149 |
| GitHub | https://github.com/booydar/babilong |

## BibTeX

```bibtex
@misc{https://doi.org/10.48550/arxiv.2406.10149,
  doi = {10.48550/ARXIV.2406.10149},
  url = {https://arxiv.org/abs/2406.10149},
  author = {Kuratov, Yuri and Bulatov, Aydar and Anokhin, Petr and Rodkin, Ivan and Sorokin, Dmitry and Sorokin, Artyom and Burtsev, Mikhail},
  keywords = {Computation and Language (cs.CL), Artificial Intelligence (cs.AI), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {BABILong: Testing the Limits of LLMs with Long Context Reasoning-in-a-Haystack},
  publisher = {arXiv},
  year = {2024},
  copyright = {arXiv.org perpetual, non-exclusive license}
}
```

## 备注

- 本卡片优先使用论文页、项目页与代码仓库等官方来源；若原报告中的链接存在错误，则以标题匹配后的官方链接为准。
