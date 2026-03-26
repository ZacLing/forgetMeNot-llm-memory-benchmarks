---
name: LaRA
slug: lara
category: 检索、Embedding 与 RAG
subcategory: 端到端 RAG 与忠实性
memory_type: Semantic / Retrieval-Augmented
year: "2025"
primary_source_kind: paper
primary_source_url: https://arxiv.org/abs/2502.09977
---

# LaRA

## 结构化信息

| 字段 | 内容 |
|---|---|
| Benchmark | LaRA |
| 分类 | 检索、Embedding 与 RAG |
| 子类 | 端到端 RAG 与忠实性 |
| 记忆侧重 | Semantic / Retrieval-Augmented |
| 首次年份 | 2025 |
| 主要来源类型 | paper |
| 论文标题 | LaRA: Benchmarking Retrieval-Augmented Generation and Long-Context LLMs -- No Silver Bullet for LC or RAG Routing |

## 基础介绍

动机：指出既有研究对 “RAG vs 长上下文” 得出不一致结论，提出 LaRA 用于更严格比较；规模 2,326 test cases，覆盖四类实用 QA 任务与三类自然长文本。

## Abstract
### 原始摘要
> Effectively incorporating external knowledge into Large Language Models (LLMs) is crucial for enhancing their capabilities and addressing real-world needs. Retrieval-Augmented Generation (RAG) offers an effective method for achieving this by retrieving the most relevant fragments into LLMs. However, the advancements in context window size for LLMs offer an alternative approach, raising the question of whether RAG remains necessary for effectively handling external knowledge. Several existing studies provide inconclusive comparisons between RAG and long-context (LC) LLMs, largely due to limitations in the benchmark designs. In this paper, we present LaRA, a novel benchmark specifically designed to rigorously compare RAG and LC LLMs. LaRA encompasses 2326 test cases across four practical QA task categories and three types of naturally occurring long texts. Through systematic evaluation of seven open-source and four proprietary LLMs, we find that the optimal choice between RAG and LC depends on a complex interplay of factors, including the model's parameter size, long-text capabilities, context length, task type, and the characteristics of the retrieved chunks. Our findings provide actionable guidelines for practitioners to effectively leverage both RAG and LC approaches in developing and deploying LLM applications. Our code and dataset is provided at: \href{https://github.com/Alibaba-NLP/LaRA}{\textbf{https://github.com/Alibaba-NLP/LaRA}}.

### 中文抽取
动机：指出既有研究对 “RAG vs 长上下文” 得出不一致结论，提出 LaRA 用于更严格比较；规模 2,326 test cases，覆盖四类实用 QA 任务与三类自然长文本。

## URL 汇总

| 类型 | 链接 |
|---|---|
| 论文页 | https://arxiv.org/abs/2502.09977 |
| GitHub | https://github.com/Alibaba-NLP/LaRA |

## BibTeX

```bibtex
@misc{https://doi.org/10.48550/arxiv.2502.09977,
  doi = {10.48550/ARXIV.2502.09977},
  url = {https://arxiv.org/abs/2502.09977},
  author = {Li, Kuan and Zhang, Liwen and Jiang, Yong and Xie, Pengjun and Huang, Fei and Wang, Shuai and Cheng, Minhao},
  keywords = {Computation and Language (cs.CL), Artificial Intelligence (cs.AI), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {LaRA: Benchmarking Retrieval-Augmented Generation and Long-Context LLMs -- No Silver Bullet for LC or RAG Routing},
  publisher = {arXiv},
  year = {2025},
  copyright = {Creative Commons Attribution Non Commercial Share Alike 4.0 International}
}
```

## 备注

- 本卡片优先使用论文页、项目页与代码仓库等官方来源；若原报告中的链接存在错误，则以标题匹配后的官方链接为准。
