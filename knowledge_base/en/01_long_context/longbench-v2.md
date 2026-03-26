---
name: LongBench v2
slug: longbench-v2
language: en
category: Long-Context Understanding and Reasoning
subcategory: 长上下文综合任务
memory_type: Working / In-Context
year: "2025"
primary_source_kind: paper
primary_source_url: https://arxiv.org/abs/2412.15204
counterpart_zh: ../../zh/01_long_context/longbench-v2.md
---

# LongBench v2

[English Knowledge Base Index](../README.md) | [中文卡片](../../zh/01_long_context/longbench-v2.md)

## Structured Metadata

| Field | Content |
|---|---|
| Benchmark | LongBench v2 |
| Category | Long-Context Understanding and Reasoning |
| Subcategory | 长上下文综合任务 |
| Memory Focus | Working / In-Context |
| First Year | 2025 |
| Primary Source Type | paper |
| Paper Title | LongBench v2: Towards Deeper Understanding and Reasoning on Realistic Long-context Multitasks |
| Chinese Card | [LongBench v2](../../zh/01_long_context/longbench-v2.md) |

## Overview

A realistic multitask benchmark with 8k-to-2M-word contexts targeting deep understanding and reasoning.

## Abstract
### Original Abstract
> This paper introduces LongBench v2, a benchmark designed to assess the ability of LLMs to handle long-context problems requiring deep understanding and reasoning across real-world multitasks. LongBench v2 consists of 503 challenging multiple-choice questions, with contexts ranging from 8k to 2M words, across six major task categories: single-document QA, multi-document QA, long in-context learning, long-dialogue history understanding, code repository understanding, and long structured data understanding. To ensure the breadth and the practicality, we collect data from nearly 100 highly educated individuals with diverse professional backgrounds. We employ both automated and manual review processes to maintain high quality and difficulty, resulting in human experts achieving only 53.7% accuracy under a 15-minute time constraint. Our evaluation reveals that the best-performing model, when directly answers the questions, achieves only 50.1% accuracy. In contrast, the o1-preview model, which includes longer reasoning, achieves 57.7%, surpassing the human baseline by 4%. These results highlight the importance of enhanced reasoning ability and scaling inference-time compute to tackle the long-context challenges in LongBench v2. The project is available at https://longbench2.github.io.

### Curated Summary
A realistic multitask benchmark with 8k-to-2M-word contexts targeting deep understanding and reasoning.

## Links

| Type | Link |
|---|---|
| Paper | https://arxiv.org/abs/2412.15204 |
| Project Page | https://longbench2.github.io/ |
| GitHub | https://github.com/THUDM/LongBench |
| Dataset | https://huggingface.co/datasets/zai-org/LongBench-v2 |

## BibTeX

```bibtex
@misc{https://doi.org/10.48550/arxiv.2412.15204,
  doi = {10.48550/ARXIV.2412.15204},
  url = {https://arxiv.org/abs/2412.15204},
  author = {Bai, Yushi and Tu, Shangqing and Zhang, Jiajie and Peng, Hao and Wang, Xiaozhi and Lv, Xin and Cao, Shulin and Xu, Jiazheng and Hou, Lei and Dong, Yuxiao and Tang, Jie and Li, Juanzi},
  keywords = {Computation and Language (cs.CL), Artificial Intelligence (cs.AI), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {LongBench v2: Towards Deeper Understanding and Reasoning on Realistic Long-context Multitasks},
  publisher = {arXiv},
  year = {2024},
  copyright = {arXiv.org perpetual, non-exclusive license}
}
```

## Remarks

- This card prioritizes official paper pages, project pages, and code repositories. When a link in the original report was incorrect, the corrected official link is used instead.
