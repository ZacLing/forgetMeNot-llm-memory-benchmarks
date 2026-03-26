---
name: RAGBench
slug: ragbench
language: zh
category: 检索、Embedding 与 RAG
subcategory: 端到端 RAG 与忠实性
memory_type: Semantic / Retrieval-Augmented
year: "2025"
primary_source_kind: paper
primary_source_url: https://arxiv.org/abs/2407.11005
counterpart_en: ../../en/03_retrieval_rag/ragbench.md
---

# RAGBench

[中文知识库索引](../README.md) | [English Card](../../en/03_retrieval_rag/ragbench.md)

## 结构化信息

| 字段 | 内容 |
|---|---|
| Benchmark | RAGBench |
| 分类 | 检索、Embedding 与 RAG |
| 子类 | 端到端 RAG 与忠实性 |
| 记忆侧重 | Semantic / Retrieval-Augmented |
| 首次年份 | 2025 |
| 主要来源类型 | paper |
| 论文标题 | RAGBench: Explainable Benchmark for Retrieval-Augmented Generation Systems |
| 英文卡片 | [RAGBench](../../en/03_retrieval_rag/ragbench.md) |

## 基础介绍

规模：100k 样本，覆盖 5 个行业域与多种 RAG 任务类型；特点之一是“来自工业语料（如用户手册）”。

## Abstract
### 原始摘要
> Retrieval-Augmented Generation (RAG) has become a standard architectural pattern for incorporating domain-specific knowledge into user-facing chat applications powered by Large Language Models (LLMs). RAG systems are characterized by (1) a document retriever that queries a domain-specific corpus for context information relevant to an input query, and (2) an LLM that generates a response based on the provided query and context. However, comprehensive evaluation of RAG systems remains a challenge due to the lack of unified evaluation criteria and annotated datasets. In response, we introduce RAGBench: the first comprehensive, large-scale RAG benchmark dataset of 100k examples. It covers five unique industry-specific domains and various RAG task types. RAGBench examples are sourced from industry corpora such as user manuals, making it particularly relevant for industry applications. Further, we formalize the TRACe evaluation framework: a set of explainable and actionable RAG evaluation metrics applicable across all RAG domains. We release the labeled dataset at https://huggingface.co/datasets/rungalileo/ragbench. RAGBench explainable labels facilitate holistic evaluation of RAG systems, enabling actionable feedback for continuous improvement of production applications. Thorough extensive benchmarking, we find that LLM-based RAG evaluation methods struggle to compete with a finetuned RoBERTa model on the RAG evaluation task. We identify areas where existing approaches fall short and propose the adoption of RAGBench with TRACe towards advancing the state of RAG evaluation systems.

### 中文抽取
规模：100k 样本，覆盖 5 个行业域与多种 RAG 任务类型；特点之一是“来自工业语料（如用户手册）”。

## URL 汇总

| 类型 | 链接 |
|---|---|
| 论文页 | https://arxiv.org/abs/2407.11005 |
| paper_url_2 | https://arxiv.org/html/2407.11005v1 |

## BibTeX

```bibtex
@misc{https://doi.org/10.48550/arxiv.2407.11005,
  doi = {10.48550/ARXIV.2407.11005},
  url = {https://arxiv.org/abs/2407.11005},
  author = {Friel, Robert and Belyi, Masha and Sanyal, Atindriyo},
  keywords = {Computation and Language (cs.CL), Artificial Intelligence (cs.AI), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {RAGBench: Explainable Benchmark for Retrieval-Augmented Generation Systems},
  publisher = {arXiv},
  year = {2024},
  copyright = {Creative Commons Attribution 4.0 International}
}
```

## 备注

- 本卡片优先使用论文页、项目页与代码仓库等官方来源；若原报告中的链接存在错误，则以标题匹配后的官方链接为准。
