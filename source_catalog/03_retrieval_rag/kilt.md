---
name: KILT
slug: kilt
category: 检索、Embedding 与 RAG
subcategory: 检索与表示学习
memory_type: Semantic / Retrieval-Augmented
year: "2021"
primary_source_kind: paper
primary_source_url: https://arxiv.org/abs/2009.02252
---

# KILT

## 结构化信息

| 字段 | 内容 |
|---|---|
| Benchmark | KILT |
| 分类 | 检索、Embedding 与 RAG |
| 子类 | 检索与表示学习 |
| 记忆侧重 | Semantic / Retrieval-Augmented |
| 首次年份 | 2021 |
| 主要来源类型 | paper |
| 论文标题 | KILT: a Benchmark for Knowledge Intensive Language Tasks |

## 基础介绍

KILT：把多个知识密集任务统一到同一份 Wikipedia 快照，并联合评估答案质量与 provenance。

## Abstract
### 原始摘要
> Challenging problems such as open-domain question answering, fact checking, slot filling and entity linking require access to large, external knowledge sources. While some models do well on individual tasks, developing general models is difficult as each task might require computationally expensive indexing of custom knowledge sources, in addition to dedicated infrastructure. To catalyze research on models that condition on specific information in large textual resources, we present a benchmark for knowledge-intensive language tasks (KILT). All tasks in KILT are grounded in the same snapshot of Wikipedia, reducing engineering turnaround through the re-use of components, as well as accelerating research into task-agnostic memory architectures. We test both task-specific and general baselines, evaluating downstream performance in addition to the ability of the models to provide provenance. We find that a shared dense vector index coupled with a seq2seq model is a strong baseline, outperforming more tailor-made approaches for fact checking, open-domain question answering and dialogue, and yielding competitive results on entity linking and slot filling, by generating disambiguated text. KILT data and code are available at https://github.com/facebookresearch/KILT.

### 中文抽取
KILT：把多个知识密集任务统一到同一份 Wikipedia 快照，并联合评估答案质量与 provenance。

## URL 汇总

| 类型 | 链接 |
|---|---|
| 论文页 | https://arxiv.org/abs/2009.02252 |
| GitHub | https://github.com/facebookresearch/KILT |

## BibTeX

```bibtex
@misc{https://doi.org/10.48550/arxiv.2009.02252,
  doi = {10.48550/ARXIV.2009.02252},
  url = {https://arxiv.org/abs/2009.02252},
  author = {Petroni, Fabio and Piktus, Aleksandra and Fan, Angela and Lewis, Patrick and Yazdani, Majid and De Cao, Nicola and Thorne, James and Jernite, Yacine and Karpukhin, Vladimir and Maillard, Jean and Plachouras, Vassilis and Rocktäschel, Tim and Riedel, Sebastian},
  keywords = {Computation and Language (cs.CL), Artificial Intelligence (cs.AI), Information Retrieval (cs.IR), Machine Learning (cs.LG), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {KILT: a Benchmark for Knowledge Intensive Language Tasks},
  publisher = {arXiv},
  year = {2020},
  copyright = {arXiv.org perpetual, non-exclusive license}
}
```

## 备注

- 本卡片优先使用论文页、项目页与代码仓库等官方来源；若原报告中的链接存在错误，则以标题匹配后的官方链接为准。
