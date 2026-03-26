---
name: MQuAKE
slug: mquake
language: zh
category: 知识编辑与语义记忆更新
subcategory: 知识编辑评测
memory_type: Semantic Memory Update
year: "2024"
primary_source_kind: paper
primary_source_url: https://arxiv.org/abs/2305.14795
counterpart_en: ../../en/06_knowledge_editing/mquake.md
---

# MQuAKE

[中文知识库索引](../README.md) | [English Card](../../en/06_knowledge_editing/mquake.md)

## 结构化信息

| 字段 | 内容 |
|---|---|
| Benchmark | MQuAKE |
| 分类 | 知识编辑与语义记忆更新 |
| 子类 | 知识编辑评测 |
| 记忆侧重 | Semantic Memory Update |
| 首次年份 | 2024 |
| 主要来源类型 | paper |
| 论文标题 | MQuAKE: Assessing Knowledge Editing in Language Models via Multi-Hop Questions |
| 英文卡片 | [MQuAKE](../../en/06_knowledge_editing/mquake.md) |

## 基础介绍

动机：编辑一个事实应导致相关推论答案改变；MQuAKE 用多跳问题检验“涟漪效应”。

## Abstract
### 原始摘要
> The information stored in large language models (LLMs) falls out of date quickly, and retraining from scratch is often not an option. This has recently given rise to a range of techniques for injecting new facts through updating model weights. Current evaluation paradigms are extremely limited, mainly validating the recall of edited facts, but changing one fact should cause rippling changes to the model's related beliefs. If we edit the UK Prime Minister to now be Rishi Sunak, then we should get a different answer to Who is married to the British Prime Minister? In this work, we present a benchmark, MQuAKE (Multi-hop Question Answering for Knowledge Editing), comprising multi-hop questions that assess whether edited models correctly answer questions where the answer should change as an entailed consequence of edited facts. While we find that current knowledge-editing approaches can recall edited facts accurately, they fail catastrophically on the constructed multi-hop questions. We thus propose a simple memory-based approach, MeLLo, which stores all edited facts externally while prompting the language model iteratively to generate answers that are consistent with the edited facts. While MQuAKE remains challenging, we show that MeLLo scales well with LLMs (e.g., OpenAI GPT-3.5-turbo) and outperforms previous model editors by a large margin.

### 中文抽取
动机：编辑一个事实应导致相关推论答案改变；MQuAKE 用多跳问题检验“涟漪效应”。

## URL 汇总

| 类型 | 链接 |
|---|---|
| 论文页 | https://arxiv.org/abs/2305.14795 |
| GitHub | https://github.com/princeton-nlp/MQuAKE |

## BibTeX

```bibtex
@misc{https://doi.org/10.48550/arxiv.2305.14795,
  doi = {10.48550/ARXIV.2305.14795},
  url = {https://arxiv.org/abs/2305.14795},
  author = {Zhong, Zexuan and Wu, Zhengxuan and Manning, Christopher D. and Potts, Christopher and Chen, Danqi},
  keywords = {Computation and Language (cs.CL), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {MQuAKE: Assessing Knowledge Editing in Language Models via Multi-Hop Questions},
  publisher = {arXiv},
  year = {2023},
  copyright = {arXiv.org perpetual, non-exclusive license}
}
```

## 备注

- 本卡片优先使用论文页、项目页与代码仓库等官方来源；若原报告中的链接存在错误，则以标题匹配后的官方链接为准。
