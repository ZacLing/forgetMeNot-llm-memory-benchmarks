---
name: CoIN
slug: coin
language: zh
category: 智能体记忆与持续学习
subcategory: 持续学习与反馈记忆
memory_type: Agentic / Procedural / Continual
year: "2024"
primary_source_kind: paper
primary_source_url: https://arxiv.org/abs/2403.08350
counterpart_en: ../../en/05_agent_memory/coin.md
---

# CoIN

[中文知识库索引](../README.md) | [English Card](../../en/05_agent_memory/coin.md)

## 结构化信息

| 字段 | 内容 |
|---|---|
| Benchmark | CoIN |
| 分类 | 智能体记忆与持续学习 |
| 子类 | 持续学习与反馈记忆 |
| 记忆侧重 | Agentic / Procedural / Continual |
| 首次年份 | 2024 |
| 主要来源类型 | paper |
| 论文标题 | CoIN: A Benchmark of Continual Instruction tuNing for Multimodel Large Language Model |
| 英文卡片 | [CoIN](../../en/05_agent_memory/coin.md) |

## 基础介绍

定义：10 数据集、8 任务，评测持续指令学习下的“指令跟随”与“常识保留”，并观察灾难性遗忘。

## Abstract
### 原始摘要
> Instruction tuning represents a prevalent strategy employed by Multimodal Large Language Models (MLLMs) to align with human instructions and adapt to new tasks. Nevertheless, MLLMs encounter the challenge of adapting to users' evolving knowledge and demands. Therefore, how to retain existing skills while acquiring new knowledge needs to be investigated. In this paper, we present a comprehensive benchmark, namely Continual Instruction tuNing (CoIN), to assess existing MLLMs in the sequential instruction tuning paradigm. CoIN comprises 10 commonly used datasets spanning 8 task categories, ensuring a diverse range of instructions and tasks. Besides, the trained model is evaluated from two aspects: Instruction Following and General Knowledge, which assess the alignment with human intention and knowledge preserved for reasoning, respectively. Experiments on CoIN demonstrate that current powerful MLLMs still suffer catastrophic forgetting, and the failure in intention alignment assumes the main responsibility, instead of the knowledge forgetting. To this end, we introduce MoELoRA to MLLMs which is effective to retain the previous instruction alignment. Experimental results consistently illustrate the forgetting decreased from this method on CoIN.

### 中文抽取
定义：10 数据集、8 任务，评测持续指令学习下的“指令跟随”与“常识保留”，并观察灾难性遗忘。

## URL 汇总

| 类型 | 链接 |
|---|---|
| 论文页 | https://arxiv.org/abs/2403.08350 |
| GitHub | https://github.com/zackschen/CoIN |
| other_neurips-entry_url | https://proceedings.neurips.cc/paper_files/paper/2024/hash/6a45500d9eda640deed90d8a62742be5-Abstract-Datasets_and_Benchmarks_Track.html |

## BibTeX

```bibtex
@misc{https://doi.org/10.48550/arxiv.2403.08350,
  doi = {10.48550/ARXIV.2403.08350},
  url = {https://arxiv.org/abs/2403.08350},
  author = {Chen, Cheng and Zhu, Junchen and Luo, Xu and Shen, Hengtao and Gao, Lianli and Song, Jingkuan},
  keywords = {Computer Vision and Pattern Recognition (cs.CV), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {CoIN: A Benchmark of Continual Instruction tuNing for Multimodel Large Language Model},
  publisher = {arXiv},
  year = {2024},
  copyright = {Creative Commons Attribution 4.0 International}
}
```

## 备注

- 本卡片优先使用论文页、项目页与代码仓库等官方来源；若原报告中的链接存在错误，则以标题匹配后的官方链接为准。
