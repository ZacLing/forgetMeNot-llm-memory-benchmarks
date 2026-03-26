---
name: SCROLLS
slug: scrolls
language: zh
category: 长上下文理解与推理
subcategory: 长上下文综合任务
memory_type: Working / In-Context
year: "2022"
primary_source_kind: paper
primary_source_url: https://aclanthology.org/2022.emnlp-main.823.pdf
counterpart_en: ../../en/01_long_context/scrolls.md
---

# SCROLLS

[中文知识库索引](../README.md) | [English Card](../../en/01_long_context/scrolls.md)

## 结构化信息

| 字段 | 内容 |
|---|---|
| Benchmark | SCROLLS |
| 分类 | 长上下文理解与推理 |
| 子类 | 长上下文综合任务 |
| 记忆侧重 | Working / In-Context |
| 首次年份 | 2022 |
| 主要来源类型 | paper |
| 论文标题 | SCROLLS: Standardized CompaRison Over Long Language Sequences |
| 英文卡片 | [SCROLLS](../../en/01_long_context/scrolls.md) |

## 基础介绍

SCROLLS：7 个长文本任务/多域（摘要、QA、NLI 等），目标是“需要在长文本中综合信息”。

## Abstract
### 原始摘要
> NLP benchmarks have largely focused on short texts, such as sentences and paragraphs, even though long texts comprise a considerable amount of natural language in the wild. We introduce SCROLLS, a suite of tasks that require reasoning over long texts. We examine existing long-text datasets, and handpick ones where the text is naturally long, while prioritizing tasks that involve synthesizing information across the input. SCROLLS contains summarization, question answering, and natural language inference tasks, covering multiple domains, including literature, science, business, and entertainment. Initial baselines, including Longformer Encoder-Decoder, indicate that there is ample room for improvement on SCROLLS. We make all datasets available in a unified text-to-text format and host a live leaderboard to facilitate research on model architecture and pretraining methods.

### 中文抽取
SCROLLS：7 个长文本任务/多域（摘要、QA、NLI 等），目标是“需要在长文本中综合信息”。

## URL 汇总

| 类型 | 链接 |
|---|---|
| 论文页 | https://aclanthology.org/2022.emnlp-main.823.pdf |
| other_scrolls-site_url | https://www.scrolls-benchmark.com/ |

## BibTeX

```bibtex
@inproceedings{shaham-etal-2022-scrolls,
    title = "{SCROLLS}: Standardized {C}ompa{R}ison Over Long Language Sequences",
    author = "Shaham, Uri  and
      Segal, Elad  and
      Ivgi, Maor  and
      Efrat, Avia  and
      Yoran, Ori  and
      Haviv, Adi  and
      Gupta, Ankit  and
      Xiong, Wenhan  and
      Geva, Mor  and
      Berant, Jonathan  and
      Levy, Omer",
    editor = "Goldberg, Yoav  and
      Kozareva, Zornitsa  and
      Zhang, Yue",
    booktitle = "Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing",
    month = dec,
    year = "2022",
    address = "Abu Dhabi, United Arab Emirates",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2022.emnlp-main.823/",
    doi = "10.18653/v1/2022.emnlp-main.823",
    pages = "12007--12021",
    abstract = "NLP benchmarks have largely focused on short texts, such as sentences and paragraphs, even though long texts comprise a considerable amount of natural language in the wild. We introduce SCROLLS, a suite of tasks that require reasoning over long texts. We examine existing long-text datasets, and handpick ones where the text is naturally long, while prioritizing tasks that involve synthesizing information across the input. SCROLLS contains summarization, question answering, and natural language inference tasks, covering multiple domains, including literature, science, business, and entertainment. Initial baselines, including Longformer Encoder-Decoder, indicate that there is ample room for improvement on SCROLLS. We make all datasets available in a unified text-to-text format and host a live leaderboard to facilitate research on model architecture and pretraining methods."
}
```

## 备注

- 本卡片优先使用论文页、项目页与代码仓库等官方来源；若原报告中的链接存在错误，则以标题匹配后的官方链接为准。
