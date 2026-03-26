---
name: QAEdit + WILD
slug: qaeedit-wild
category: 知识编辑与语义记忆更新
subcategory: 知识编辑评测
memory_type: Semantic Memory Update
year: "2025"
primary_source_kind: paper
primary_source_url: https://aclanthology.org/2025.acl-long.745/
---

# QAEdit + WILD

## 结构化信息

| 字段 | 内容 |
|---|---|
| Benchmark | QAEdit + WILD |
| 分类 | 知识编辑与语义记忆更新 |
| 子类 | 知识编辑评测 |
| 记忆侧重 | Semantic Memory Update |
| 首次年份 | 2025 |
| 主要来源类型 | paper |
| 论文标题 | The Mirage of Model Editing: Revisiting Evaluation in the Wild |

## 基础介绍

内容：指出既有编辑指标可能高估实用效果；提出 QAEdit benchmark 与 WILD 框架。

## Abstract
### 原始摘要
> Despite near-perfect results reported in the literature, the effectiveness of model editing in real-world applications remains unclear. To bridge this gap, we introduce QAEdit, a new benchmark aligned with widely used question answering (QA) datasets, and WILD, a task-agnostic evaluation framework designed to better reflect real-world usage of model editing. Our single editing experiments show that current editing methods perform substantially worse than previously reported (38.5% vs. 96.8%). We demonstrate that it stems from issues in the synthetic evaluation practices of prior work. Among them, the most severe is the use of teacher forcing during testing, which leaks both content and length of the ground truth, leading to overestimated performance. Furthermore, we simulate practical deployment by sequential editing, revealing that current approaches fail drastically with only 1000 edits. This work calls for a shift in model editing research toward rigorous evaluation and the development of robust, scalable methods that can reliably update knowledge in LLMs for real-world use.

### 中文抽取
内容：指出既有编辑指标可能高估实用效果；提出 QAEdit benchmark 与 WILD 框架。

## URL 汇总

| 类型 | 链接 |
|---|---|
| 论文页 | https://aclanthology.org/2025.acl-long.745/ |
| GitHub | https://github.com/WanliYoung/Revisit-Editing-Evaluation |
| other_pdf_url | https://aclanthology.org/2025.acl-long.745.pdf |

## BibTeX

```bibtex
@inproceedings{yang-etal-2025-mirage,
    title = "The Mirage of Model Editing: Revisiting Evaluation in the Wild",
    author = "Yang, Wanli  and
      Sun, Fei  and
      Tan, Jiajun  and
      Ma, Xinyu  and
      Cao, Qi  and
      Yin, Dawei  and
      Shen, Huawei  and
      Cheng, Xueqi",
    editor = "Che, Wanxiang  and
      Nabende, Joyce  and
      Shutova, Ekaterina  and
      Pilehvar, Mohammad Taher",
    booktitle = "Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)",
    month = jul,
    year = "2025",
    address = "Vienna, Austria",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2025.acl-long.745/",
    doi = "10.18653/v1/2025.acl-long.745",
    pages = "15336--15354",
    ISBN = "979-8-89176-251-0",
    abstract = "Despite near-perfect results reported in the literature, the effectiveness of model editing in real-world applications remains unclear. To bridge this gap, we introduce QAEdit, a new benchmark aligned with widely used question answering (QA) datasets, and WILD, a task-agnostic evaluation framework designed to better reflect real-world usage of model editing. Our single editing experiments show that current editing methods perform substantially worse than previously reported (38.5{\%} vs. 96.8{\%}). We demonstrate that it stems from issues in the synthetic evaluation practices of prior work. Among them, the most severe is the use of teacher forcing during testing, which leaks both content and length of the ground truth, leading to overestimated performance. Furthermore, we simulate practical deployment by sequential editing, revealing that current approaches fail drastically with only 1000 edits. This work calls for a shift in model editing research toward rigorous evaluation and the development of robust, scalable methods that can reliably update knowledge in LLMs for real-world use."
}
```

## 备注

- 本卡片优先使用论文页、项目页与代码仓库等官方来源；若原报告中的链接存在错误，则以标题匹配后的官方链接为准。
