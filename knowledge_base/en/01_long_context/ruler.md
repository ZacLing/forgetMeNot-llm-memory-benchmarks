---
name: RULER
slug: ruler
language: en
category: Long-Context Understanding and Reasoning
subcategory: Diagnostic Suites and Standardized Evaluation
memory_type: Working / In-Context
year: "2024"
primary_source_kind: paper
primary_source_url: https://arxiv.org/abs/2404.06654
counterpart_zh: ../../zh/01_long_context/ruler.md
---

# RULER

[English Knowledge Base Index](../README.md) | [中文卡片](../../zh/01_long_context/ruler.md)

## Structured Metadata

| Field | Content |
|---|---|
| Benchmark | RULER |
| Category | Long-Context Understanding and Reasoning |
| Subcategory | Diagnostic Suites and Standardized Evaluation |
| Memory Focus | Working / In-Context |
| First Year | 2024 |
| Primary Source Type | paper |
| Paper Title | RULER: What's the Real Context Size of Your Long-Context Language Models? |
| Chinese Card | [RULER](../../zh/01_long_context/ruler.md) |

## Overview

A controllable long-context diagnostic suite covering retrieval, aggregation, multi-hop tracing, and QA.

## Abstract
### Original Abstract
> The needle-in-a-haystack (NIAH) test, which examines the ability to retrieve a piece of information (the "needle") from long distractor texts (the "haystack"), has been widely adopted to evaluate long-context language models (LMs). However, this simple retrieval-based test is indicative of only a superficial form of long-context understanding. To provide a more comprehensive evaluation of long-context LMs, we create a new synthetic benchmark RULER with flexible configurations for customized sequence length and task complexity. RULER expands upon the vanilla NIAH test to encompass variations with diverse types and quantities of needles. Moreover, RULER introduces new task categories multi-hop tracing and aggregation to test behaviors beyond searching from context. We evaluate 17 long-context LMs with 13 representative tasks in RULER. Despite achieving nearly perfect accuracy in the vanilla NIAH test, almost all models exhibit large performance drops as the context length increases. While these models all claim context sizes of 32K tokens or greater, only half of them can maintain satisfactory performance at the length of 32K. Our analysis of Yi-34B, which supports context length of 200K, reveals large room for improvement as we increase input length and task complexity. We open source RULER to spur comprehensive evaluation of long-context LMs.

### Curated Summary
A controllable long-context diagnostic suite covering retrieval, aggregation, multi-hop tracing, and QA.

## Links

| Type | Link |
|---|---|
| Paper | https://arxiv.org/abs/2404.06654 |
| other_lm-eval-task_url | https://github.com/EleutherAI/lm-evaluation-harness/blob/main/lm_eval/tasks/ruler/README.md |

## BibTeX

```bibtex
@misc{https://doi.org/10.48550/arxiv.2404.06654,
  doi = {10.48550/ARXIV.2404.06654},
  url = {https://arxiv.org/abs/2404.06654},
  author = {Hsieh, Cheng-Ping and Sun, Simeng and Kriman, Samuel and Acharya, Shantanu and Rekesh, Dima and Jia, Fei and Zhang, Yang and Ginsburg, Boris},
  keywords = {Computation and Language (cs.CL), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {RULER: What's the Real Context Size of Your Long-Context Language Models?},
  publisher = {arXiv},
  year = {2024},
  copyright = {Creative Commons Attribution 4.0 International}
}
```

## Remarks

- This card prioritizes official paper pages, project pages, and code repositories. When a link in the original report was incorrect, the corrected official link is used instead.
