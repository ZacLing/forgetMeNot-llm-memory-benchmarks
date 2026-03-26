---
name: AcademicEval
slug: academiceval
language: zh
category: 长上下文理解与推理
subcategory: 长上下文综合任务
memory_type: Working / In-Context
year: "2025"
primary_source_kind: paper
primary_source_url: https://arxiv.org/abs/2510.17725
counterpart_en: ../../en/01_long_context/academiceval.md
---

# AcademicEval

[中文知识库索引](../README.md) | [English Card](../../en/01_long_context/academiceval.md)

## 结构化信息

| 字段 | 内容 |
|---|---|
| Benchmark | AcademicEval |
| 分类 | 长上下文理解与推理 |
| 子类 | 长上下文综合任务 |
| 记忆侧重 | Working / In-Context |
| 首次年份 | 2025 |
| 主要来源类型 | paper |
| 论文标题 | AcademicEval: Live Long-Context LLM Benchmark |
| 英文卡片 | [AcademicEval](../../en/01_long_context/academiceval.md) |

## 基础介绍

设计：以 arXiv 论文构造学术写作任务（Title/Abstract/Introduction/Related Work），强调 live evaluation 与减少标签泄漏。

## Abstract
### 原始摘要
> Large Language Models (LLMs) have recently achieved remarkable performance in long-context understanding. However, current long-context LLM benchmarks are limited by rigid context length, labor-intensive annotation, and the pressing challenge of label leakage issues during LLM training. Therefore, we propose \textsc{AcademicEval}, a live benchmark for evaluating LLMs over long-context generation tasks. \textsc{AcademicEval} adopts papers on arXiv to introduce several academic writing tasks with long-context inputs, \textit{i.e.}, \textsc{Title}, \textsc{Abstract}, \textsc{Introduction}, and \textsc{Related Work}, which cover a wide range of abstraction levels and require no manual labeling. Moreover, \textsc{AcademicEval} integrates high-quality and expert-curated few-shot demonstrations from a collected co-author graph to enable flexible context length. Especially, \textsc{AcademicEval} features an efficient live evaluation, ensuring no label leakage. We conduct a holistic evaluation on \textsc{AcademicEval}, and the results illustrate that LLMs perform poorly on tasks with hierarchical abstraction levels and tend to struggle with long few-shot demonstrations, highlighting the challenge of our benchmark. Through experimental analysis, we also reveal some insights for enhancing LLMs' long-context modeling capabilities. Code is available at https://github.com/ulab-uiuc/AcademicEval

### 中文抽取
设计：以 arXiv 论文构造学术写作任务（Title/Abstract/Introduction/Related Work），强调 live evaluation 与减少标签泄漏。

## URL 汇总

| 类型 | 链接 |
|---|---|
| 论文页 | https://arxiv.org/abs/2510.17725 |
| GitHub | https://github.com/ulab-uiuc/AcademicEval |

## BibTeX

```bibtex
@misc{https://doi.org/10.48550/arxiv.2510.17725,
  doi = {10.48550/ARXIV.2510.17725},
  url = {https://arxiv.org/abs/2510.17725},
  author = {Zhang, Haozhen and Feng, Tao and Han, Pengrui and You, Jiaxuan},
  keywords = {Computation and Language (cs.CL), Artificial Intelligence (cs.AI), Machine Learning (cs.LG), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {AcademicEval: Live Long-Context LLM Benchmark},
  publisher = {arXiv},
  year = {2025},
  copyright = {Creative Commons Attribution 4.0 International}
}
```

## 备注

- 本卡片优先使用论文页、项目页与代码仓库等官方来源；若原报告中的链接存在错误，则以标题匹配后的官方链接为准。
