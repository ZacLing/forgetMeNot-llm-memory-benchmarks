---
name: CLongEval
slug: clongeval
language: en
category: Long-Context Understanding and Reasoning
subcategory: Comprehensive Long-Context Tasks
memory_type: Working / In-Context
year: "2024"
primary_source_kind: paper
primary_source_url: https://aclanthology.org/2024.findings-emnlp.230/
counterpart_zh: ../../zh/01_long_context/clongeval.md
---

# CLongEval

[English Knowledge Base Index](../README.md) | [中文卡片](../../zh/01_long_context/clongeval.md)

## Structured Metadata

| Field | Content |
|---|---|
| Benchmark | CLongEval |
| Category | Long-Context Understanding and Reasoning |
| Subcategory | Comprehensive Long-Context Tasks |
| Memory Focus | Working / In-Context |
| First Year | 2024 |
| Primary Source Type | paper |
| Paper Title | CLongEval: A Chinese Benchmark for Evaluating Long-Context Large Language Models |
| Chinese Card | [CLongEval](../../zh/01_long_context/clongeval.md) |

## Overview

A dedicated Chinese long-context benchmark with 7 tasks, 7,267 examples, and coverage from 1K to 100K context windows.

## Abstract
### Original Abstract
> Developing Large Language Models (LLMs) with robust long-context capabilities has been the recent research focus, resulting in the emergence of long-context LLMs proficient in Chinese. However, the evaluation of these models remains underdeveloped due to a lack of benchmarks. To address this gap, we present CLongEval, a comprehensive Chinese benchmark for evaluating long-context LLMs. CLongEval is characterized by three key features: (1) Sufficient data volume, comprising 7 distinct tasks and 7,267 examples; (2) Broad applicability, accommodating to models with context windows size from 1K to 100K; (3) High quality, with over 2,000 manually annotated question-answer pairs in addition to the automatically constructed labels. With CLongEval, we undertake a comprehensive assessment of 6 open-source long-context LLMs and 2 leading commercial counterparts that feature both long-context abilities and proficiency in Chinese. We also provide in-depth analysis based on the empirical results, trying to shed light on the critical capabilities that present challenges in long-context settings. The dataset, evaluation scripts, and model outputs are released.

### Curated Summary

A dedicated Chinese long-context benchmark with 7 tasks, 7,267 examples, and coverage from 1K to 100K context windows.

## Links

| Type | Link |
|---|---|
| Paper | https://arxiv.org/abs/2403.03514 |
| Publication Page | https://aclanthology.org/2024.findings-emnlp.230/ |
| GitHub | https://github.com/zexuanqiu/CLongEval |

## BibTeX

```bibtex
@inproceedings{qiu-etal-2024-clongeval,
  title = "{CL}ong{E}val: A {C}hinese Benchmark for Evaluating Long-Context Large Language Models",
  author = "Qiu, Zexuan and Li, Jingjing and Huang, Shijue and Jiao, Xiaoqi and Zhong, Wanjun and King, Irwin",
  editor = "Al-Onaizan, Yaser and Bansal, Mohit and Chen, Yun-Nung",
  booktitle = "Findings of the Association for Computational Linguistics: EMNLP 2024",
  month = nov,
  year = "2024",
  address = "Miami, Florida, USA",
  publisher = "Association for Computational Linguistics",
  url = "https://aclanthology.org/2024.findings-emnlp.230/",
  doi = "10.18653/v1/2024.findings-emnlp.230",
  pages = "3985--4004"
}
```

## Remarks

- CLongEval is the most direct fit when your evaluation target is Chinese long-context capability rather than English or bilingual generality.
