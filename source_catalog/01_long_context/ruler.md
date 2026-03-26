---
name: RULER
slug: ruler
category: 长上下文理解与推理
subcategory: 诊断套件与标准化评测
memory_type: Working / In-Context
year: "2024"
primary_source_kind: paper
primary_source_url: https://arxiv.org/abs/2404.06654
---

# RULER

## 结构化信息

| 字段 | 内容 |
|---|---|
| Benchmark | RULER |
| 分类 | 长上下文理解与推理 |
| 子类 | 诊断套件与标准化评测 |
| 记忆侧重 | Working / In-Context |
| 首次年份 | 2024 |
| 主要来源类型 | paper |
| 论文标题 | RULER: What's the Real Context Size of Your Long-Context Language Models? |

## 基础介绍

构成：13 个“代表性任务”，类别含检索、多跳 tracing、聚合、QA；强调“vanilla NIAH 近满分并不代表真实长上下文能力”。
工具支持：被 lm‑evaluation‑harness 明确集成（README）。

## Abstract
### 原始摘要
> The needle-in-a-haystack (NIAH) test, which examines the ability to retrieve a piece of information (the "needle") from long distractor texts (the "haystack"), has been widely adopted to evaluate long-context language models (LMs). However, this simple retrieval-based test is indicative of only a superficial form of long-context understanding. To provide a more comprehensive evaluation of long-context LMs, we create a new synthetic benchmark RULER with flexible configurations for customized sequence length and task complexity. RULER expands upon the vanilla NIAH test to encompass variations with diverse types and quantities of needles. Moreover, RULER introduces new task categories multi-hop tracing and aggregation to test behaviors beyond searching from context. We evaluate 17 long-context LMs with 13 representative tasks in RULER. Despite achieving nearly perfect accuracy in the vanilla NIAH test, almost all models exhibit large performance drops as the context length increases. While these models all claim context sizes of 32K tokens or greater, only half of them can maintain satisfactory performance at the length of 32K. Our analysis of Yi-34B, which supports context length of 200K, reveals large room for improvement as we increase input length and task complexity. We open source RULER to spur comprehensive evaluation of long-context LMs.

### 中文抽取
构成：13 个“代表性任务”，类别含检索、多跳 tracing、聚合、QA；强调“vanilla NIAH 近满分并不代表真实长上下文能力”。
工具支持：被 lm‑evaluation‑harness 明确集成（README）。

## URL 汇总

| 类型 | 链接 |
|---|---|
| 论文页 | https://arxiv.org/abs/2404.06654 |
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

## 备注

- 本卡片优先使用论文页、项目页与代码仓库等官方来源；若原报告中的链接存在错误，则以标题匹配后的官方链接为准。
