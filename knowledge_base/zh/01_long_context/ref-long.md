---
name: Ref-Long
slug: ref-long
language: zh
category: 长上下文理解与推理
subcategory: 引用定位与忠实性
memory_type: Working / In-Context
year: "2025"
primary_source_kind: paper
primary_source_url: https://arxiv.org/abs/2507.09506
counterpart_en: ../../en/01_long_context/ref-long.md
---

# Ref-Long

[中文知识库索引](../README.md) | [English Card](../../en/01_long_context/ref-long.md)

## 结构化信息

| 字段 | 内容 |
|---|---|
| Benchmark | Ref-Long |
| 分类 | 长上下文理解与推理 |
| 子类 | 引用定位与忠实性 |
| 记忆侧重 | Working / In-Context |
| 首次年份 | 2025 |
| 主要来源类型 | paper |
| 论文标题 | Ref-Long: Benchmarking the Long-context Referencing Capability of Long-context Language Models |
| 英文卡片 | [Ref-Long](../../en/01_long_context/ref-long.md) |

## 基础介绍

定义：要求模型识别“哪些文档引用/指向某 key”，更强调上下文关系而非直接检索；构造三个子集（从合成到真实）。

## Abstract
### 原始摘要
> Long-context language models (LCLMs) have exhibited impressive capabilities in long-context understanding tasks. Among these, long-context referencing -- a crucial task that requires LCLMs to attribute items of interest to specific parts of long-context data -- remains underexplored. To bridge this gap, this paper proposes Referencing Evaluation for Long-context Language Models (Ref-Long), a novel benchmark designed to assess the long-context referencing capability of LCLMs. Specifically, Ref-Long requires LCLMs to identify the indexes of documents that reference a specific key, emphasizing contextual relationships between the key and the documents over simple retrieval. Based on the task design, we construct three subsets ranging from synthetic to realistic scenarios to form the Ref-Long benchmark. Experimental results of 13 LCLMs reveal significant shortcomings in long-context referencing, even among advanced models like GPT-4o. To further investigate these challenges, we conduct comprehensive analyses, including human evaluations, task format adjustments, fine-tuning experiments, and error analyses, leading to several key insights. Our data and code can be found in https://github. com/wujunjie1998/Ref-Long.

### 中文抽取
定义：要求模型识别“哪些文档引用/指向某 key”，更强调上下文关系而非直接检索；构造三个子集（从合成到真实）。

## URL 汇总

| 类型 | 链接 |
|---|---|
| 论文页 | https://arxiv.org/abs/2507.09506 |
| 项目主页 | https://wujunjie1998.github.io/Ref-Long-website/ |
| paper_url_2 | https://github.com/wujunjie1998/Ref-Long |

## BibTeX

```bibtex
@misc{https://doi.org/10.48550/arxiv.2507.09506,
  doi = {10.48550/ARXIV.2507.09506},
  url = {https://arxiv.org/abs/2507.09506},
  author = {Wu, Junjie and Gu, Gefei and Zheng, Yanan and Yeung, Dit-Yan and Cohan, Arman},
  keywords = {Computation and Language (cs.CL), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {Ref-Long: Benchmarking the Long-context Referencing Capability of Long-context Language Models},
  publisher = {arXiv},
  year = {2025},
  copyright = {Creative Commons Attribution 4.0 International}
}
```

## 备注

- 本卡片优先使用论文页、项目页与代码仓库等官方来源；若原报告中的链接存在错误，则以标题匹配后的官方链接为准。
