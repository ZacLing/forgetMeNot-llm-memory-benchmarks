---
name: LoCoV1
slug: locov1
category: 检索、Embedding 与 RAG
subcategory: 检索与表示学习
memory_type: Semantic / Retrieval-Augmented
year: "2024"
primary_source_kind: paper
primary_source_url: https://arxiv.org/abs/2402.07440
---

# LoCoV1

## 结构化信息

| 字段 | 内容 |
|---|---|
| Benchmark | LoCoV1 |
| 分类 | 检索、Embedding 与 RAG |
| 子类 | 检索与表示学习 |
| 记忆侧重 | Semantic / Retrieval-Augmented |
| 首次年份 | 2024 |
| 主要来源类型 | paper |
| 论文标题 | Benchmarking and Building Long-Context Retrieval Models with LoCo and M2-BERT |

## 基础介绍

问题：长文档检索场景中“chunking 不可行/无效”，需要真正对长文整体建模；提出 LoCoV1（12 项任务）来评测 long-context retrieval。

## Abstract
### 原始摘要
> Retrieval pipelines-an integral component of many machine learning systems-perform poorly in domains where documents are long (e.g., 10K tokens or more) and where identifying the relevant document requires synthesizing information across the entire text. Developing long-context retrieval encoders suitable for these domains raises three challenges: (1) how to evaluate long-context retrieval performance, (2) how to pretrain a base language model to represent both short contexts (corresponding to queries) and long contexts (corresponding to documents), and (3) how to fine-tune this model for retrieval under the batch size limitations imposed by GPU memory constraints. To address these challenges, we first introduce LoCoV1, a novel 12 task benchmark constructed to measure long-context retrieval where chunking is not possible or not effective. We next present the M2-BERT retrieval encoder, an 80M parameter state-space encoder model built from the Monarch Mixer architecture, capable of scaling to documents up to 32K tokens long. We describe a pretraining data mixture which allows this encoder to process both short and long context sequences, and a finetuning approach that adapts this base model to retrieval with only single-sample batches. Finally, we validate the M2-BERT retrieval encoder on LoCoV1, finding that it outperforms competitive Transformer-based models by at least 23.3 points, despite containing upwards of 90x fewer parameters.

### 中文抽取
问题：长文档检索场景中“chunking 不可行/无效”，需要真正对长文整体建模；提出 LoCoV1（12 项任务）来评测 long-context retrieval。

## URL 汇总

| 类型 | 链接 |
|---|---|
| 论文页 | https://arxiv.org/abs/2402.07440 |
| paper_url_2 | https://proceedings.mlr.press/v235/saad-falcon24a.html |

## BibTeX

```bibtex
@misc{https://doi.org/10.48550/arxiv.2402.07440,
  doi = {10.48550/ARXIV.2402.07440},
  url = {https://arxiv.org/abs/2402.07440},
  author = {Saad-Falcon, Jon and Fu, Daniel Y. and Arora, Simran and Guha, Neel and Ré, Christopher},
  keywords = {Information Retrieval (cs.IR), Machine Learning (cs.LG), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {Benchmarking and Building Long-Context Retrieval Models with LoCo and M2-BERT},
  publisher = {arXiv},
  year = {2024},
  copyright = {Creative Commons Attribution 4.0 International}
}
```

## 备注

- 本卡片优先使用论文页、项目页与代码仓库等官方来源；若原报告中的链接存在错误，则以标题匹配后的官方链接为准。
