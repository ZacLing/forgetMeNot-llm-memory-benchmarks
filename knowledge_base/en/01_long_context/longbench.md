---
name: LongBench
slug: longbench
language: en
category: Long-Context Understanding and Reasoning
subcategory: Comprehensive Long-Context Tasks
memory_type: Working / In-Context
year: "2024"
primary_source_kind: paper
primary_source_url: https://arxiv.org/abs/2308.14508
counterpart_zh: ../../zh/01_long_context/longbench.md
---

# LongBench

[English Knowledge Base Index](../README.md) | [中文卡片](../../zh/01_long_context/longbench.md)

## Structured Metadata

| Field | Content |
|---|---|
| Benchmark | LongBench |
| Category | Long-Context Understanding and Reasoning |
| Subcategory | Comprehensive Long-Context Tasks |
| Memory Focus | Working / In-Context |
| First Year | 2024 |
| Primary Source Type | paper |
| Paper Title | LongBench: A Bilingual, Multitask Benchmark for Long Context Understanding |
| Chinese Card | [LongBench](../../zh/01_long_context/longbench.md) |

## Overview

The first bilingual multitask long-context benchmark covering QA, summarization, few-shot learning, synthetic tasks, and code completion.

## Abstract
### Original Abstract
> Although large language models (LLMs) demonstrate impressive performance for many language tasks, most of them can only handle texts a few thousand tokens long, limiting their applications on longer sequence inputs, such as books, reports, and codebases. Recent works have proposed methods to improve LLMs' long context capabilities by extending context windows and more sophisticated memory mechanisms. However, comprehensive benchmarks tailored for evaluating long context understanding are lacking. In this paper, we introduce LongBench, the first bilingual, multi-task benchmark for long context understanding, enabling a more rigorous evaluation of long context understanding. LongBench comprises 21 datasets across 6 task categories in both English and Chinese, with an average length of 6,711 words (English) and 13,386 characters (Chinese). These tasks cover key long-text application areas including single-doc QA, multi-doc QA, summarization, few-shot learning, synthetic tasks, and code completion. All datasets in LongBench are standardized into a unified format, allowing for effortless automatic evaluation of LLMs. Upon comprehensive evaluation of 8 LLMs on LongBench, we find that: (1) Commercial model (GPT-3.5-Turbo-16k) outperforms other open-sourced models, but still struggles on longer contexts. (2) Scaled position embedding and fine-tuning on longer sequences lead to substantial improvement on long context understanding. (3) Context compression technique such as retrieval brings improvement for model with weak ability on long contexts, but the performance still lags behind models that have strong long context understanding capability. The code and datasets are available at https://github.com/THUDM/LongBench.

### Curated Summary
The first bilingual multitask long-context benchmark covering QA, summarization, few-shot learning, synthetic tasks, and code completion.

## Links

| Type | Link |
|---|---|
| Paper | https://arxiv.org/abs/2308.14508 |
| Paper PDF | https://aclanthology.org/2024.acl-long.172.pdf |
| Project Page | https://github.com/EleutherAI/lm-evaluation-harness/blob/main/lm_eval/tasks/longbench/README.md |
| GitHub | https://github.com/THUDM/LongBench |
| Dataset | https://huggingface.co/datasets/zai-org/LongBench |

## BibTeX

```bibtex
@misc{https://doi.org/10.48550/arxiv.2308.14508,
  doi = {10.48550/ARXIV.2308.14508},
  url = {https://arxiv.org/abs/2308.14508},
  author = {Bai, Yushi and Lv, Xin and Zhang, Jiajie and Lyu, Hongchang and Tang, Jiankai and Huang, Zhidian and Du, Zhengxiao and Liu, Xiao and Zeng, Aohan and Hou, Lei and Dong, Yuxiao and Tang, Jie and Li, Juanzi},
  keywords = {Computation and Language (cs.CL), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {LongBench: A Bilingual, Multitask Benchmark for Long Context Understanding},
  publisher = {arXiv},
  year = {2023},
  copyright = {arXiv.org perpetual, non-exclusive license}
}
```

## Remarks

- This card prioritizes official paper pages, project pages, and code repositories. When a link in the original report was incorrect, the corrected official link is used instead.
