---
name: MTEB
slug: mteb
language: zh
category: 检索、Embedding 与 RAG
subcategory: 检索与表示学习
memory_type: Semantic / Retrieval-Augmented
year: "2023"
primary_source_kind: paper
primary_source_url: https://arxiv.org/abs/2210.07316
counterpart_en: ../../en/03_retrieval_rag/mteb.md
---

# MTEB

[中文知识库索引](../README.md) | [English Card](../../en/03_retrieval_rag/mteb.md)

## 结构化信息

| 字段 | 内容 |
|---|---|
| Benchmark | MTEB |
| 分类 | 检索、Embedding 与 RAG |
| 子类 | 检索与表示学习 |
| 记忆侧重 | Semantic / Retrieval-Augmented |
| 首次年份 | 2023 |
| 主要来源类型 | paper |
| 论文标题 | MTEB: Massive Text Embedding Benchmark |
| 英文卡片 | [MTEB](../../en/03_retrieval_rag/mteb.md) |

## 基础介绍

MTEB：大规模 embedding benchmark，覆盖 58 个数据集、8 类任务和 112 种语言，常被用作通用检索与表征能力对照。

## Abstract
### 原始摘要
> Text embeddings are commonly evaluated on a small set of datasets from a single task not covering their possible applications to other tasks. It is unclear whether state-of-the-art embeddings on semantic textual similarity (STS) can be equally well applied to other tasks like clustering or reranking. This makes progress in the field difficult to track, as various models are constantly being proposed without proper evaluation. To solve this problem, we introduce the Massive Text Embedding Benchmark (MTEB). MTEB spans 8 embedding tasks covering a total of 58 datasets and 112 languages. Through the benchmarking of 33 models on MTEB, we establish the most comprehensive benchmark of text embeddings to date. We find that no particular text embedding method dominates across all tasks. This suggests that the field has yet to converge on a universal text embedding method and scale it up sufficiently to provide state-of-the-art results on all embedding tasks. MTEB comes with open-source code and a public leaderboard at https://github.com/embeddings-benchmark/mteb.

### 中文抽取
MTEB：大规模 embedding benchmark，覆盖 58 个数据集、8 类任务和 112 种语言，常被用作通用检索与表征能力对照。

## URL 汇总

| 类型 | 链接 |
|---|---|
| 论文页 | https://arxiv.org/abs/2210.07316 |
| GitHub | https://github.com/embeddings-benchmark/mteb |

## BibTeX

```bibtex
@misc{https://doi.org/10.48550/arxiv.2210.07316,
  doi = {10.48550/ARXIV.2210.07316},
  url = {https://arxiv.org/abs/2210.07316},
  author = {Muennighoff, Niklas and Tazi, Nouamane and Magne, Loïc and Reimers, Nils},
  keywords = {Computation and Language (cs.CL), Information Retrieval (cs.IR), Machine Learning (cs.LG), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {MTEB: Massive Text Embedding Benchmark},
  publisher = {arXiv},
  year = {2022},
  copyright = {arXiv.org perpetual, non-exclusive license}
}
```

## 备注

- 本卡片优先使用论文页、项目页与代码仓库等官方来源；若原报告中的链接存在错误，则以标题匹配后的官方链接为准。
