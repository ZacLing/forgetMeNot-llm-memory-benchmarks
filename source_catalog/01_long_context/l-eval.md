---
name: L-Eval
slug: l-eval
category: 长上下文理解与推理
subcategory: 诊断套件与标准化评测
memory_type: Working / In-Context
year: "2023"
primary_source_kind: paper
primary_source_url: https://arxiv.org/abs/2307.11088
---

# L-Eval

## 结构化信息

| 字段 | 内容 |
|---|---|
| Benchmark | L-Eval |
| 分类 | 长上下文理解与推理 |
| 子类 | 诊断套件与标准化评测 |
| 记忆侧重 | Working / In-Context |
| 首次年份 | 2023 |
| 主要来源类型 | paper |
| 论文标题 | L-Eval: Instituting Standardized Evaluation for Long Context Language Models |

## 基础介绍

构成：20 子任务、508 长文档、2,000+人工标注 query‑response；输入跨度 3k–200k tokens；并讨论评测指标有效性。
任务形态：包含闭集与开放式任务（repo 列出分组与评测方式）。

## Abstract
### 原始摘要
> Recently, there has been growing interest in extending the context length of large language models (LLMs), aiming to effectively process long inputs of one turn or conversations with more extensive histories. While proprietary models such as GPT-4 and Claude can largely preserve the reasoning ability in an extended context, open-source models are still progressing through the early stages of development. To bridge this gap, we propose L-Eval to institute a more standardized evaluation for long context language models (LCLMs) addressing two key aspects: dataset construction and evaluation metrics. On the one hand, we build a new evaluation suite containing 20 sub-tasks, 508 long documents, and over 2,000 human-labeled query-response pairs encompassing diverse question styles, domains, and input length (3k$\sim$200k tokens). On the other hand, we investigate the effectiveness in evalution metrics for LCLMs. Results show that popular n-gram matching metrics generally can not correlate well with human judgment, and thus we strongly advocate for length-instruction-enhanced (LIE) evaluation and employing LLM judges. We conducted a comprehensive study of 4 popular commercial LLMs and 12 open-source counterparts using the L-Eval benchmark. Our empirical findings offer useful insights into the study of LCLMs and lay the groundwork for the development of more principled evaluation of these models.

### 中文抽取
构成：20 子任务、508 长文档、2,000+人工标注 query‑response；输入跨度 3k–200k tokens；并讨论评测指标有效性。
任务形态：包含闭集与开放式任务（repo 列出分组与评测方式）。

## URL 汇总

| 类型 | 链接 |
|---|---|
| 论文页 | https://arxiv.org/abs/2307.11088 |
| GitHub | https://github.com/OpenLMLab/LEval |

## BibTeX

```bibtex
@misc{https://doi.org/10.48550/arxiv.2307.11088,
  doi = {10.48550/ARXIV.2307.11088},
  url = {https://arxiv.org/abs/2307.11088},
  author = {An, Chenxin and Gong, Shansan and Zhong, Ming and Zhao, Xingjian and Li, Mukai and Zhang, Jun and Kong, Lingpeng and Qiu, Xipeng},
  keywords = {Computation and Language (cs.CL), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {L-Eval: Instituting Standardized Evaluation for Long Context Language Models},
  publisher = {arXiv},
  year = {2023},
  copyright = {arXiv.org perpetual, non-exclusive license}
}
```

## 备注

- 本卡片优先使用论文页、项目页与代码仓库等官方来源；若原报告中的链接存在错误，则以标题匹配后的官方链接为准。
