---
        name: Phonebook
        slug: phonebook
        language: zh
        category: 长上下文针类诊断
        subcategory: 多针 / 结构化检索
        memory_type: Working / In-Context
        year: "2024"
        primary_source_kind: task-family
        primary_source_url: https://arxiv.org/abs/2406.07887
        counterpart_en: ../../en/02_needle_and_diagnostics/phonebook.md
        ---

        # Phonebook

        [中文知识库索引](../README.md) | [English Card](../../en/02_needle_and_diagnostics/phonebook.md)

        ## 结构化信息

        | 字段 | 内容 |
        |---|---|
        | Benchmark | Phonebook |
        | 分类 | 长上下文针类诊断 |
        | 子类 | 多针 / 结构化检索 |
        | 记忆侧重 | Working / In-Context |
        | 首次年份 | 2024 |
        | 主要来源类型 | task-family |
        | 论文标题 | An Empirical Study of Mamba-based Language Models |
        | 英文卡片 | [Phonebook](../../en/02_needle_and_diagnostics/phonebook.md) |

        ## 基础介绍

        典型定义：给定若干姓名-电话号码条目，few-shot 询问某人号码；在 Mamba‑based LM 实证研究中用于长上下文检索能力评估。
数据集：社区在 HuggingFace 上整理 phonebook 数据集集合（如 booydar/phonebook_N16，百万行规模在卡片中可见）。

        ## Abstract
### 原始摘要
> Selective state-space models (SSMs) like Mamba overcome some of the shortcomings of Transformers, such as quadratic computational complexity with sequence length and large inference-time memory requirements from the key-value cache. Moreover, recent studies have shown that SSMs can match or exceed the language modeling capabilities of Transformers, making them an attractive alternative. In a controlled setting (e.g., same data), however, studies so far have only presented small scale experiments comparing SSMs to Transformers. To understand the strengths and weaknesses of these architectures at larger scales, we present a direct comparison between 8B-parameter Mamba, Mamba-2, and Transformer models trained on the same datasets of up to 3.5T tokens. We also compare these models to a hybrid architecture consisting of 43% Mamba-2, 7% attention, and 50% MLP layers (Mamba-2-Hybrid). Using a diverse set of tasks, we answer the question of whether Mamba models can match Transformers at larger training budgets. Our results show that while pure SSMs match or exceed Transformers on many tasks, they lag behind Transformers on tasks which require strong copying or in-context learning abilities (e.g., 5-shot MMLU, Phonebook) or long-context reasoning. In contrast, we find that the 8B Mamba-2-Hybrid exceeds the 8B Transformer on all 12 standard tasks we evaluated (+2.65 points on average) and is predicted to be up to 8x faster when generating tokens at inference time. To validate long-context capabilities, we provide additional experiments evaluating variants of the Mamba-2-Hybrid and Transformer extended to support 16K, 32K, and 128K sequences. On an additional 23 long-context tasks, the hybrid model continues to closely match or exceed the Transformer on average. To enable further study, we release the checkpoints as well as the code used to train our models as part of NVIDIA's Megatron-LM project.

### 中文抽取
典型定义：给定若干姓名-电话号码条目，few-shot 询问某人号码；在 Mamba‑based LM 实证研究中用于长上下文检索能力评估。
数据集：社区在 HuggingFace 上整理 phonebook 数据集集合（如 booydar/phonebook_N16，百万行规模在卡片中可见）。

## URL 汇总

| 类型 | 链接 |
|---|---|
| 论文页 | https://arxiv.org/abs/2406.07887 |
| 数据集页 | https://huggingface.co/collections/booydar/phonebook-datasets |
| dataset_url_2 | https://huggingface.co/datasets/booydar/phonebook_N16 |

## BibTeX

```bibtex
@misc{https://doi.org/10.48550/arxiv.2406.07887,
  doi = {10.48550/ARXIV.2406.07887},
  url = {https://arxiv.org/abs/2406.07887},
  author = {Waleffe, Roger and Byeon, Wonmin and Riach, Duncan and Norick, Brandon and Korthikanti, Vijay and Dao, Tri and Gu, Albert and Hatamizadeh, Ali and Singh, Sudhakar and Narayanan, Deepak and Kulshreshtha, Garvit and Singh, Vartika and Casper, Jared and Kautz, Jan and Shoeybi, Mohammad and Catanzaro, Bryan},
  keywords = {Machine Learning (cs.LG), Computation and Language (cs.CL), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {An Empirical Study of Mamba-based Language Models},
  publisher = {arXiv},
  year = {2024},
  copyright = {arXiv.org perpetual, non-exclusive license}
}
```

## 备注

- Phonebook 更接近一类被多篇长上下文论文复用的任务家族，而不是单独命名发表的 benchmark 论文。这里沿用报告中的代表性论文与数据集集合来说明其标准设定。
