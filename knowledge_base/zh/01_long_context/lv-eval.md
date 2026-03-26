---
name: LV-Eval
slug: lv-eval
language: zh
category: 长上下文理解与推理
subcategory: 长上下文综合任务
memory_type: Working / In-Context
year: "2024"
primary_source_kind: paper
primary_source_url: https://arxiv.org/abs/2402.05136
counterpart_en: ../../en/01_long_context/lv-eval.md
---

# LV-Eval

[中文知识库索引](../README.md) | [English Card](../../en/01_long_context/lv-eval.md)

## 结构化信息

| 字段 | 内容 |
|---|---|
| Benchmark | LV-Eval |
| 分类 | 长上下文理解与推理 |
| 子类 | 长上下文综合任务 |
| 记忆侧重 | Working / In-Context |
| 首次年份 | 2024 |
| 主要来源类型 | paper |
| 论文标题 | LV-Eval: A Balanced Long-Context Benchmark with 5 Length Levels Up to 256K |
| 英文卡片 | [LV-Eval](../../en/01_long_context/lv-eval.md) |

## 基础介绍

定位：LV-Eval 是一个强调“长度分层 + 数据平衡 + 泄漏控制”的长上下文 benchmark。
任务：以 single-hop QA 和 multi-hop QA 为核心，覆盖 11 个中英双语数据子集，并提供从 16K 到 256K 的 5 档长度。
关键技术：其构造中特别加入 confusing facts insertion、keyword and phrase replacement，以及基于关键词召回的评测指标，以降低字面匹配和数据泄漏带来的偏差。
用途：适合分析模型在不同上下文长度上的退化曲线，也适合比较模型在干扰事实存在时的鲁棒性。

## Abstract
### 原始摘要
> State-of-the-art large language models (LLMs) are now claiming remarkable supported context lengths of 256k or even more. In contrast, the average context lengths of mainstream benchmarks are insufficient (5k-21k), and they suffer from potential knowledge leakage and inaccurate metrics, resulting in biased evaluation. This paper introduces LV-Eval, a challenging long-context benchmark with five length levels (16k, 32k, 64k, 128k, and 256k) reaching up to 256k words. LV-Eval features two main tasks, single-hop QA and multi-hop QA, comprising 11 bilingual datasets. The design of LV-Eval has incorporated three key techniques, namely confusing facts insertion, keyword and phrase replacement, and keyword-recall-based metric design. The advantages of LV-Eval include controllable evaluation across different context lengths, challenging test instances with confusing facts, mitigated knowledge leakage, and more objective evaluations. We evaluate 15 LLMs on LV-Eval and conduct ablation studies on the benchmarking techniques. The results reveal that: (i) Moonshot-v1 and recent large-scale open-source models, such as Qwen-2.5-72B and Llama-3.1-70B, achieve the highest performance on LV-Eval, particularly at lengths below 64k. (ii) Models exhibit distinct score trends. For example, GLM-4-9B-128k, Yi-6B-200k, and Llama3-8B-1M exhibit a relatively gentle degradation of performance, but their absolute performances may not necessarily be higher than those of LLMs with shorter context lengths. (iii) LLMs' performances can significantly degrade in the presence of confusing information, especially in the pressure test of "needle in a haystack". (iv) Issues related to knowledge leakage and inaccurate metrics introduce bias in evaluation, and these concerns are alleviated in LV-Eval. All datasets and evaluation codes are released at: https://github.com/infinigence/LVEval.

### 中文抽取
LV-Eval 的核心特点是 5 档长度、双语 QA、多种泄漏缓解设计和可控的干扰信息插入。它特别适合比较模型在 16K 到 256K 区间中的性能衰减，以及在混淆事实干扰下的稳健性。

## URL 汇总

| 类型 | 链接 |
|---|---|
| 论文页 | https://arxiv.org/abs/2402.05136 |
| GitHub | https://github.com/infinigence/LVEval |
| 数据集页 | https://huggingface.co/datasets/Infinigence/LVEval |

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

## 备注

- 如果希望在统一 QA 框架下观察 16K 到 256K 的长度效应，LV-Eval 是非常直接的一组基线。
