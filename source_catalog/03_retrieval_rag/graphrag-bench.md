---
name: GraphRAG-Bench
slug: graphrag-bench
category: 检索、Embedding 与 RAG
subcategory: 端到端 RAG 与忠实性
memory_type: Semantic / Retrieval-Augmented
year: "2025"
primary_source_kind: paper
primary_source_url: https://arxiv.org/abs/2506.02404
---

# GraphRAG-Bench

## 结构化信息

| 字段 | 内容 |
|---|---|
| Benchmark | GraphRAG-Bench |
| 分类 | 检索、Embedding 与 RAG |
| 子类 | 端到端 RAG 与忠实性 |
| 记忆侧重 | Semantic / Retrieval-Augmented |
| 首次年份 | 2025 |
| 主要来源类型 | paper |
| 论文标题 | GraphRAG-Bench: Challenging Domain-Specific Reasoning for Evaluating Graph Retrieval-Augmented Generation |

## 基础介绍

内容：16 学科、20 本核心教材构成域内语料；题型多样（选择/判断/多选/填空/开放式等），并不仅看最终答案正确性，也企图覆盖 graph construction、retrieval、generation、reasoning coherence 等维度。

## Abstract
### 原始摘要
> Graph Retrieval Augmented Generation (GraphRAG) has garnered increasing recognition for its potential to enhance large language models (LLMs) by structurally organizing domain-specific corpora and facilitating complex reasoning. However, current evaluations of GraphRAG models predominantly rely on traditional question-answering datasets. Their limited scope in questions and evaluation metrics fails to comprehensively assess the reasoning capacity improvements enabled by GraphRAG models. To address this gap, we introduce GraphRAG-Bench, a large-scale, domain-specific benchmark designed to rigorously evaluate GraphRAG models. Our benchmark offers three key superiorities: \((i)\) Challenging question design. Featuring college-level, domain-specific questions that demand multi-hop reasoning, the benchmark ensures that simple content retrieval is insufficient for problem-solving. For example, some questions require mathematical reasoning or programming. \((ii)\) Diverse task coverage. The dataset includes a broad spectrum of reasoning tasks, multiple-choice, true/false, multi-select, open-ended, and fill-in-the-blank. It spans 16 disciplines in twenty core textbooks. \((iii)\) Holistic evaluation framework. GraphRAG-Bench provides comprehensive assessment across the entire GraphRAG pipeline, including graph construction, knowledge retrieval, and answer generation. Beyond final-answer correctness, it evaluates the logical coherence of the reasoning process. By applying nine contemporary GraphRAG methods to GraphRAG-Bench, we demonstrate its utility in quantifying how graph-based structuring improves model reasoning capabilities. Our analysis reveals critical insights about graph architectures, retrieval efficacy, and reasoning capabilities, offering actionable guidance for the research community.

### 中文抽取
内容：16 学科、20 本核心教材构成域内语料；题型多样（选择/判断/多选/填空/开放式等），并不仅看最终答案正确性，也企图覆盖 graph construction、retrieval、generation、reasoning coherence 等维度。

## URL 汇总

| 类型 | 链接 |
|---|---|
| 论文页 | https://arxiv.org/abs/2506.02404 |
| GitHub | https://github.com/GraphRAG-Bench/GraphRAG-Benchmark |
| 数据集页 | https://huggingface.co/datasets/GraphRAG-Bench/GraphRAG-Bench |

## BibTeX

```bibtex
@misc{https://doi.org/10.48550/arxiv.2506.02404,
  doi = {10.48550/ARXIV.2506.02404},
  url = {https://arxiv.org/abs/2506.02404},
  author = {Xiao, Yilin and Dong, Junnan and Zhou, Chuang and Dong, Su and Zhang, Qian-wen and Yin, Di and Sun, Xing and Huang, Xiao},
  keywords = {Computation and Language (cs.CL), Artificial Intelligence (cs.AI), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {GraphRAG-Bench: Challenging Domain-Specific Reasoning for Evaluating Graph Retrieval-Augmented Generation},
  publisher = {arXiv},
  year = {2025},
  copyright = {arXiv.org perpetual, non-exclusive license}
}
```

## 备注

- 本卡片优先使用论文页、项目页与代码仓库等官方来源；若原报告中的链接存在错误，则以标题匹配后的官方链接为准。
