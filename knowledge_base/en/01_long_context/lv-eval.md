---
name: LV-Eval
slug: lv-eval
language: en
category: Long-Context Understanding and Reasoning
subcategory: Comprehensive Long-Context Tasks
memory_type: Working / In-Context
year: "2024"
primary_source_kind: paper
primary_source_url: https://arxiv.org/abs/2402.05136
counterpart_zh: ../../zh/01_long_context/lv-eval.md
---

# LV-Eval

[English Knowledge Base Index](../README.md) | [中文卡片](../../zh/01_long_context/lv-eval.md)

## Structured Metadata

| Field | Content |
|---|---|
| Benchmark | LV-Eval |
| Category | Long-Context Understanding and Reasoning |
| Subcategory | Comprehensive Long-Context Tasks |
| Memory Focus | Working / In-Context |
| First Year | 2024 |
| Primary Source Type | paper |
| Paper Title | LV-Eval: A Balanced Long-Context Benchmark with 5 Length Levels Up to 256K |
| Chinese Card | [LV-Eval](../../zh/01_long_context/lv-eval.md) |

## Overview

A balanced bilingual long-context QA benchmark with five length levels up to 256K and explicit mitigation of leakage and literal-matching shortcuts.

## Abstract
### Original Abstract
> State-of-the-art large language models (LLMs) are now claiming remarkable supported context lengths of 256k or even more. In contrast, the average context lengths of mainstream benchmarks are insufficient (5k-21k), and they suffer from potential knowledge leakage and inaccurate metrics, resulting in biased evaluation. This paper introduces LV-Eval, a challenging long-context benchmark with five length levels (16k, 32k, 64k, 128k, and 256k) reaching up to 256k words. LV-Eval features two main tasks, single-hop QA and multi-hop QA, comprising 11 bilingual datasets. The design of LV-Eval has incorporated three key techniques, namely confusing facts insertion, keyword and phrase replacement, and keyword-recall-based metric design. The advantages of LV-Eval include controllable evaluation across different context lengths, challenging test instances with confusing facts, mitigated knowledge leakage, and more objective evaluations. We evaluate 15 LLMs on LV-Eval and conduct ablation studies on the benchmarking techniques. The results reveal that: (i) Moonshot-v1 and recent large-scale open-source models, such as Qwen-2.5-72B and Llama-3.1-70B, achieve the highest performance on LV-Eval, particularly at lengths below 64k. (ii) Models exhibit distinct score trends. For example, GLM-4-9B-128k, Yi-6B-200k, and Llama3-8B-1M exhibit a relatively gentle degradation of performance, but their absolute performances may not necessarily be higher than those of LLMs with shorter context lengths. (iii) LLMs' performances can significantly degrade in the presence of confusing information, especially in the pressure test of "needle in a haystack". (iv) Issues related to knowledge leakage and inaccurate metrics introduce bias in evaluation, and these concerns are alleviated in LV-Eval. All datasets and evaluation codes are released at: https://github.com/infinigence/LVEval.

### Curated Summary

A balanced bilingual long-context QA benchmark with five length levels up to 256K and explicit mitigation of leakage and literal-matching shortcuts.

## Links

| Type | Link |
|---|---|
| Paper | https://arxiv.org/abs/2402.05136 |
| GitHub | https://github.com/infinigence/LVEval |
| Dataset | https://huggingface.co/datasets/Infinigence/LVEval |

## BibTeX

```bibtex
@misc{yuan2024lveval,
  title = {LV-Eval: A Balanced Long-Context Benchmark with 5 Length Levels Up to 256K},
  author = {Yuan, Tao and Ning, Xuefei and Zhou, Dong and Yang, Zhijie and Li, Shiyao and Zhuang, Minghui and Tan, Zheyue and Yao, Zhuyu and Lin, Dahua and Li, Boxun and Dai, Guohao and Yan, Shengen and Wang, Yu},
  year = {2024},
  eprint = {2402.05136},
  archivePrefix = {arXiv},
  primaryClass = {cs.CL},
  url = {https://arxiv.org/abs/2402.05136}
}
```

## Remarks

- LV-Eval is a strong choice when you want explicit length stratification from 16K through 256K under a unified QA-oriented setup.
