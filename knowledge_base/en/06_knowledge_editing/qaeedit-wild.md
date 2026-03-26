---
name: QAEdit + WILD
slug: qaeedit-wild
language: en
category: Knowledge Editing and Semantic Memory Updates
subcategory: 知识编辑评测
memory_type: Semantic Memory Update
year: "2025"
primary_source_kind: paper
primary_source_url: https://aclanthology.org/2025.acl-long.745/
counterpart_zh: ../../zh/06_knowledge_editing/qaeedit-wild.md
---

# QAEdit + WILD

[English Knowledge Base Index](../README.md) | [中文卡片](../../zh/06_knowledge_editing/qaeedit-wild.md)

## Structured Metadata

| Field | Content |
|---|---|
| Benchmark | QAEdit + WILD |
| Category | Knowledge Editing and Semantic Memory Updates |
| Subcategory | 知识编辑评测 |
| Memory Focus | Semantic Memory Update |
| First Year | 2025 |
| Primary Source Type | paper |
| Paper Title | The Mirage of Model Editing: Revisiting Evaluation in the Wild |
| Chinese Card | [QAEdit + WILD](../../zh/06_knowledge_editing/qaeedit-wild.md) |

## Overview

A realistic editing benchmark and evaluation framework that revisits model editing in the wild.

## Abstract
### Original Abstract
> Despite near-perfect results reported in the literature, the effectiveness of model editing in real-world applications remains unclear. To bridge this gap, we introduce QAEdit, a new benchmark aligned with widely used question answering (QA) datasets, and WILD, a task-agnostic evaluation framework designed to better reflect real-world usage of model editing. Our single editing experiments show that current editing methods perform substantially worse than previously reported (38.5% vs. 96.8%). We demonstrate that it stems from issues in the synthetic evaluation practices of prior work. Among them, the most severe is the use of teacher forcing during testing, which leaks both content and length of the ground truth, leading to overestimated performance. Furthermore, we simulate practical deployment by sequential editing, revealing that current approaches fail drastically with only 1000 edits. This work calls for a shift in model editing research toward rigorous evaluation and the development of robust, scalable methods that can reliably update knowledge in LLMs for real-world use.

### Curated Summary
A realistic editing benchmark and evaluation framework that revisits model editing in the wild.

## Links

| Type | Link |
|---|---|
| Paper | https://aclanthology.org/2025.acl-long.745/ |
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

## Remarks

- This card prioritizes official paper pages, project pages, and code repositories. When a link in the original report was incorrect, the corrected official link is used instead.
