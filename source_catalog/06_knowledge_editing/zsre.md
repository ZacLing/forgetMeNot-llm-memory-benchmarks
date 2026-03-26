---
name: ZsRE
slug: zsre
category: 知识编辑与语义记忆更新
subcategory: 知识编辑评测
memory_type: Semantic Memory Update
year: "2017"
primary_source_kind: paper
primary_source_url: https://arxiv.org/abs/1706.04115
---

# ZsRE

## 结构化信息

| 字段 | 内容 |
|---|---|
| Benchmark | ZsRE |
| 分类 | 知识编辑与语义记忆更新 |
| 子类 | 知识编辑评测 |
| 记忆侧重 | Semantic Memory Update |
| 首次年份 | 2017 |
| 主要来源类型 | paper |
| 论文标题 | Zero-Shot Relation Extraction via Reading Comprehension |

## 基础介绍

来源：Levy 等 2017 提出，把关系抽取转为 QA；并提供公开数据集页面；在模型编辑文献中被广泛用作“context‑free QA 编辑”基准。

## Abstract
### 原始摘要
> We show that relation extraction can be reduced to answering simple reading comprehension questions, by associating one or more natural-language questions with each relation slot. This reduction has several advantages: we can (1) learn relation-extraction models by extending recent neural reading-comprehension techniques, (2) build very large training sets for those models by combining relation-specific crowd-sourced questions with distant supervision, and even (3) do zero-shot learning by extracting new relation types that are only specified at test-time, for which we have no labeled training examples. Experiments on a Wikipedia slot-filling task demonstrate that the approach can generalize to new questions for known relation types with high accuracy, and that zero-shot generalization to unseen relation types is possible, at lower accuracy levels, setting the bar for future work on this task.

### 中文抽取
来源：Levy 等 2017 提出，把关系抽取转为 QA；并提供公开数据集页面；在模型编辑文献中被广泛用作“context‑free QA 编辑”基准。

## URL 汇总

| 类型 | 链接 |
|---|---|
| 论文页 | https://arxiv.org/abs/1706.04115 |
| 数据集页 | https://nlp.cs.washington.edu/zeroshot/ |

## BibTeX

```bibtex
@misc{https://doi.org/10.48550/arxiv.1706.04115,
  doi = {10.48550/ARXIV.1706.04115},
  url = {https://arxiv.org/abs/1706.04115},
  author = {Levy, Omer and Seo, Minjoon and Choi, Eunsol and Zettlemoyer, Luke},
  keywords = {Computation and Language (cs.CL), Artificial Intelligence (cs.AI), Machine Learning (cs.LG), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {Zero-Shot Relation Extraction via Reading Comprehension},
  publisher = {arXiv},
  year = {2017},
  copyright = {arXiv.org perpetual, non-exclusive license}
}
```

## 备注

- 本卡片优先使用论文页、项目页与代码仓库等官方来源；若原报告中的链接存在错误，则以标题匹配后的官方链接为准。
