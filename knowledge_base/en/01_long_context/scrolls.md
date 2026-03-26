---
name: SCROLLS
slug: scrolls
language: en
category: Long-Context Understanding and Reasoning
subcategory: Comprehensive Long-Context Tasks
memory_type: Working / In-Context
year: "2022"
primary_source_kind: paper
primary_source_url: https://aclanthology.org/2022.emnlp-main.823.pdf
counterpart_zh: ../../zh/01_long_context/scrolls.md
---

# SCROLLS

[English Knowledge Base Index](../README.md) | [中文卡片](../../zh/01_long_context/scrolls.md)

## Structured Metadata

| Field | Content |
|---|---|
| Benchmark | SCROLLS |
| Category | Long-Context Understanding and Reasoning |
| Subcategory | Comprehensive Long-Context Tasks |
| Memory Focus | Working / In-Context |
| First Year | 2022 |
| Primary Source Type | paper |
| Paper Title | SCROLLS: Standardized CompaRison Over Long Language Sequences |
| Chinese Card | [SCROLLS](../../zh/01_long_context/scrolls.md) |

## Overview

A standardized long-text benchmark spanning summarization, QA, NLI, and other long-sequence tasks.

## Abstract
### Original Abstract
> NLP benchmarks have largely focused on short texts, such as sentences and paragraphs, even though long texts comprise a considerable amount of natural language in the wild. We introduce SCROLLS, a suite of tasks that require reasoning over long texts. We examine existing long-text datasets, and handpick ones where the text is naturally long, while prioritizing tasks that involve synthesizing information across the input. SCROLLS contains summarization, question answering, and natural language inference tasks, covering multiple domains, including literature, science, business, and entertainment. Initial baselines, including Longformer Encoder-Decoder, indicate that there is ample room for improvement on SCROLLS. We make all datasets available in a unified text-to-text format and host a live leaderboard to facilitate research on model architecture and pretraining methods.

### Curated Summary
A standardized long-text benchmark spanning summarization, QA, NLI, and other long-sequence tasks.

## Links

| Type | Link |
|---|---|
| Paper | https://aclanthology.org/2022.emnlp-main.823.pdf |
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

## Remarks

- This card prioritizes official paper pages, project pages, and code repositories. When a link in the original report was incorrect, the corrected official link is used instead.
