---
name: BEIR
slug: beir
language: zh
category: 检索、Embedding 与 RAG
subcategory: 检索与表示学习
memory_type: Semantic / Retrieval-Augmented
year: "2021"
primary_source_kind: paper
primary_source_url: https://arxiv.org/abs/2104.08663
counterpart_en: ../../en/03_retrieval_rag/beir.md
---

# BEIR

[中文知识库索引](../README.md) | [English Card](../../en/03_retrieval_rag/beir.md)

## 结构化信息

| 字段 | 内容 |
|---|---|
| Benchmark | BEIR |
| 分类 | 检索、Embedding 与 RAG |
| 子类 | 检索与表示学习 |
| 记忆侧重 | Semantic / Retrieval-Augmented |
| 首次年份 | 2021 |
| 主要来源类型 | paper |
| 论文标题 | BEIR: A Heterogenous Benchmark for Zero-shot Evaluation of Information Retrieval Models |
| 英文卡片 | [BEIR](../../en/03_retrieval_rag/beir.md) |

## 基础介绍

BEIR：18 个数据集构成异质检索 benchmark，强调 zero-shot / OOD 泛化评测。

## Abstract
### 原始摘要
> Existing neural information retrieval (IR) models have often been studied in homogeneous and narrow settings, which has considerably limited insights into their out-of-distribution (OOD) generalization capabilities. To address this, and to facilitate researchers to broadly evaluate the effectiveness of their models, we introduce Benchmarking-IR (BEIR), a robust and heterogeneous evaluation benchmark for information retrieval. We leverage a careful selection of 18 publicly available datasets from diverse text retrieval tasks and domains and evaluate 10 state-of-the-art retrieval systems including lexical, sparse, dense, late-interaction and re-ranking architectures on the BEIR benchmark. Our results show BM25 is a robust baseline and re-ranking and late-interaction-based models on average achieve the best zero-shot performances, however, at high computational costs. In contrast, dense and sparse-retrieval models are computationally more efficient but often underperform other approaches, highlighting the considerable room for improvement in their generalization capabilities. We hope this framework allows us to better evaluate and understand existing retrieval systems, and contributes to accelerating progress towards better robust and generalizable systems in the future. BEIR is publicly available at https://github.com/UKPLab/beir.

### 中文抽取
BEIR：18 个数据集构成异质检索 benchmark，强调 zero-shot / OOD 泛化评测。

## URL 汇总

| 类型 | 链接 |
|---|---|
| 论文页 | https://arxiv.org/abs/2104.08663 |
| GitHub | https://github.com/UKPLab/beir |

## BibTeX

```bibtex
@misc{https://doi.org/10.48550/arxiv.2104.08663,
  doi = {10.48550/ARXIV.2104.08663},
  url = {https://arxiv.org/abs/2104.08663},
  author = {Thakur, Nandan and Reimers, Nils and Rücklé, Andreas and Srivastava, Abhishek and Gurevych, Iryna},
  keywords = {Information Retrieval (cs.IR), Artificial Intelligence (cs.AI), Computation and Language (cs.CL), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {BEIR: A Heterogenous Benchmark for Zero-shot Evaluation of Information Retrieval Models},
  publisher = {arXiv},
  year = {2021},
  copyright = {Creative Commons Attribution Share Alike 4.0 International}
}
```

## 备注

- 本卡片优先使用论文页、项目页与代码仓库等官方来源；若原报告中的链接存在错误，则以标题匹配后的官方链接为准。
