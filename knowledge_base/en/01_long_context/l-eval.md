---
name: L-Eval
slug: l-eval
language: en
category: Long-Context Understanding and Reasoning
subcategory: 诊断套件与标准化评测
memory_type: Working / In-Context
year: "2023"
primary_source_kind: paper
primary_source_url: https://arxiv.org/abs/2307.11088
counterpart_zh: ../../zh/01_long_context/l-eval.md
---

# L-Eval

[English Knowledge Base Index](../README.md) | [中文卡片](../../zh/01_long_context/l-eval.md)

## Structured Metadata

| Field | Content |
|---|---|
| Benchmark | L-Eval |
| Category | Long-Context Understanding and Reasoning |
| Subcategory | 诊断套件与标准化评测 |
| Memory Focus | Working / In-Context |
| First Year | 2023 |
| Primary Source Type | paper |
| Paper Title | L-Eval: Instituting Standardized Evaluation for Long Context Language Models |
| Chinese Card | [L-Eval](../../zh/01_long_context/l-eval.md) |

## Overview

A standardized long-context suite with 20 tasks, 508 long documents, and 2,000+ human-labeled query-response pairs.

## Abstract
### Original Abstract
> Recently, there has been growing interest in extending the context length of large language models (LLMs), aiming to effectively process long inputs of one turn or conversations with more extensive histories. While proprietary models such as GPT-4 and Claude can largely preserve the reasoning ability in an extended context, open-source models are still progressing through the early stages of development. To bridge this gap, we propose L-Eval to institute a more standardized evaluation for long context language models (LCLMs) addressing two key aspects: dataset construction and evaluation metrics. On the one hand, we build a new evaluation suite containing 20 sub-tasks, 508 long documents, and over 2,000 human-labeled query-response pairs encompassing diverse question styles, domains, and input length (3k$\sim$200k tokens). On the other hand, we investigate the effectiveness in evalution metrics for LCLMs. Results show that popular n-gram matching metrics generally can not correlate well with human judgment, and thus we strongly advocate for length-instruction-enhanced (LIE) evaluation and employing LLM judges. We conducted a comprehensive study of 4 popular commercial LLMs and 12 open-source counterparts using the L-Eval benchmark. Our empirical findings offer useful insights into the study of LCLMs and lay the groundwork for the development of more principled evaluation of these models.

### Curated Summary
A standardized long-context suite with 20 tasks, 508 long documents, and 2,000+ human-labeled query-response pairs.

## Links

| Type | Link |
|---|---|
| Paper | https://arxiv.org/abs/2307.11088 |
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

## Remarks

- This card prioritizes official paper pages, project pages, and code repositories. When a link in the original report was incorrect, the corrected official link is used instead.
