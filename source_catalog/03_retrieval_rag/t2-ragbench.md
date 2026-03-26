---
name: T2-RAGBench
slug: t2-ragbench
category: 检索、Embedding 与 RAG
subcategory: 端到端 RAG 与忠实性
memory_type: Semantic / Retrieval-Augmented
year: "2026"
primary_source_kind: paper
primary_source_url: https://arxiv.org/abs/2506.12071
---

# T2-RAGBench

## 结构化信息

| 字段 | 内容 |
|---|---|
| Benchmark | T2-RAGBench |
| 分类 | 检索、Embedding 与 RAG |
| 子类 | 端到端 RAG 与忠实性 |
| 记忆侧重 | Semantic / Retrieval-Augmented |
| 首次年份 | 2026 |
| 主要来源类型 | paper |
| 论文标题 | T$^2$-RAGBench: Text-and-Table Benchmark for Evaluating Retrieval-Augmented Generation |

## 基础介绍

目的：评测真实文档常见的“文本+表格”场景；规模为 23,088 question‑context‑answer triples。

## Abstract
### 原始摘要
> Since many real-world documents combine textual and tabular data, robust Retrieval Augmented Generation (RAG) systems are essential for effectively accessing and analyzing such content to support complex reasoning tasks. Therefore, this paper introduces $\textbf{$T^2$-RAGBench}$, a benchmark comprising $\textbf{23,088}$ question-context-answer triples, designed to evaluate RAG methods on real-world text-and-table data. Unlike typical QA datasets that operate under $\textit{Oracle Context}$ settings, $\textbf{$T^2$-RAGBench}$ challenges models to first retrieve the correct context before conducting numerical reasoning. Existing QA datasets containing text-and-table data typically contain context-dependent questions, which may yield multiple correct answers depending on the provided context. To address this, we transform SOTA datasets into a context-independent format, validated by experts as 91.3% context-independent questions, enabling reliable RAG evaluation. Our comprehensive evaluation identifies $\textit{Hybrid BM25}$ , a technique that combines dense and sparse vectors, as the most effective approach for text-and-table data. However, results demonstrate that $\textbf{$T^2$-RAGBench}$ remains challenging even for SOTA LLMs and RAG methods. Further ablation studies examine the impact of embedding models and corpus size on retrieval performance. $\textbf{$T^2$-RAGBench}$ provides a realistic and rigorous benchmark for existing RAG methods on text-and-table data. Code and dataset are available online: https://github.com/uhh-hcds/g4kmu-paper

### 中文抽取
目的：评测真实文档常见的“文本+表格”场景；规模为 23,088 question‑context‑answer triples。

## URL 汇总

| 类型 | 链接 |
|---|---|
| 论文页 | https://arxiv.org/abs/2506.12071 |

## BibTeX

```bibtex
@misc{https://doi.org/10.48550/arxiv.2506.12071,
  doi = {10.48550/ARXIV.2506.12071},
  url = {https://arxiv.org/abs/2506.12071},
  author = {Strich, Jan and Isgorur, Enes Kutay and Trescher, Maximilian and Biemann, Chris and Semmann, Martin},
  keywords = {Information Retrieval (cs.IR), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {T$^2$-RAGBench: Text-and-Table Benchmark for Evaluating Retrieval-Augmented Generation},
  publisher = {arXiv},
  year = {2025},
  copyright = {Creative Commons Attribution 4.0 International}
}
```

## 备注

- 本卡片优先使用论文页、项目页与代码仓库等官方来源；若原报告中的链接存在错误，则以标题匹配后的官方链接为准。
