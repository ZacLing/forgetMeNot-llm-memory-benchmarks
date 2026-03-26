---
        name: LongBench-E
        slug: longbench-e
        language: zh
        category: 长上下文理解与推理
        subcategory: 长上下文综合任务
        memory_type: Working / In-Context
        year: "2025"
        primary_source_kind: variant-doc
        primary_source_url: https://github.com/EleutherAI/lm-evaluation-harness/blob/main/lm_eval/tasks/longbench/README.md
        counterpart_en: ../../en/01_long_context/longbench-e.md
        ---

        # LongBench-E

        [中文知识库索引](../README.md) | [English Card](../../en/01_long_context/longbench-e.md)

        ## 结构化信息

        | 字段 | 内容 |
        |---|---|
        | Benchmark | LongBench-E |
        | 分类 | 长上下文理解与推理 |
        | 子类 | 长上下文综合任务 |
        | 记忆侧重 | Working / In-Context |
        | 首次年份 | 2025 |
        | 主要来源类型 | variant-doc |
        | 论文标题 | LongBench-E: Uniform-Length Variant for LongBench in lm-evaluation-harness |
        | 英文卡片 | [LongBench-E](../../en/01_long_context/longbench-e.md) |

        ## 基础介绍

        提出方：作为分析不同输入长度下性能退化的变体，被 lm‑evaluation‑harness 文档明确描述为“均匀长度分布”版本。
目的：把“基准知识/短输入强项”与“真正长上下文能力”在统计上更多解耦（但仍需结合其它无泄漏/可控基准验证）。

        ## Abstract
### 原始摘要
> A framework for few-shot evaluation of language models. - EleutherAI/lm-evaluation-harness

### 中文抽取
提出方：作为分析不同输入长度下性能退化的变体，被 lm‑evaluation‑harness 文档明确描述为“均匀长度分布”版本。
目的：把“基准知识/短输入强项”与“真正长上下文能力”在统计上更多解耦（但仍需结合其它无泄漏/可控基准验证）。

## URL 汇总

| 类型 | 链接 |
|---|---|
| 项目主页 | https://github.com/EleutherAI/lm-evaluation-harness/blob/main/lm_eval/tasks/longbench/README.md |

## BibTeX

```bibtex
@misc{longbench_e_lm_eval,
  title = {LongBench-E: Uniform-Length Variant for LongBench in lm-evaluation-harness},
  author = {{EleutherAI}},
  howpublished = {GitHub documentation},
  year = {2025},
  url = {https://github.com/EleutherAI/lm-evaluation-harness/blob/main/lm_eval/tasks/longbench/README.md},
  note = {LongBench-E is documented as the uniform-length evaluation variant of LongBench in lm-evaluation-harness.}
}
```

## 备注

- LongBench-E 更像 LongBench 的长度分布变体说明，而不是单独发表的 benchmark 论文；因此这里以 lm-evaluation-harness 官方任务文档作为可引用来源。
