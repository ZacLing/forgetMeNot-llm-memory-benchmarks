---
name: LongEmbed
slug: longembed
language: zh
category: 检索、Embedding 与 RAG
subcategory: 检索与表示学习
memory_type: Semantic / Retrieval-Augmented
year: "2024"
primary_source_kind: paper
primary_source_url: https://arxiv.org/abs/2404.12096
counterpart_en: ../../en/03_retrieval_rag/longembed.md
---

# LongEmbed

[中文知识库索引](../README.md) | [English Card](../../en/03_retrieval_rag/longembed.md)

## 结构化信息

| 字段 | 内容 |
|---|---|
| Benchmark | LongEmbed |
| 分类 | 检索、Embedding 与 RAG |
| 子类 | 检索与表示学习 |
| 记忆侧重 | Semantic / Retrieval-Augmented |
| 首次年份 | 2024 |
| 主要来源类型 | paper |
| 论文标题 | LongEmbed: Extending Embedding Models for Long Context Retrieval |
| 英文卡片 | [LongEmbed](../../en/03_retrieval_rag/longembed.md) |

## 基础介绍

内容：构造 LongEmbed benchmark（2 合成 + 4 真实任务），评测 embedding 模型从 512/4k 等上下文扩展到 32k 的检索能力；合成任务包括 Personalized Passkey Retrieval 等设置。

## Abstract
### 原始摘要
> Embedding models play a pivot role in modern NLP applications such as IR and RAG. While the context limit of LLMs has been pushed beyond 1 million tokens, embedding models are still confined to a narrow context window not exceeding 8k tokens, refrained from application scenarios requiring long inputs such as legal contracts. This paper explores context window extension of existing embedding models, pushing the limit to 32k without requiring additional training. First, we examine the performance of current embedding models for long context retrieval on our newly constructed LongEmbed benchmark. LongEmbed comprises two synthetic tasks and four carefully chosen real-world tasks, featuring documents of varying length and dispersed target information. Benchmarking results underscore huge room for improvement in these models. Based on this, comprehensive experiments show that training-free context window extension strategies like position interpolation can effectively extend the context window of existing embedding models by several folds, regardless of their original context being 512 or beyond 4k. Furthermore, for models employing absolute position encoding (APE), we show the possibility of further fine-tuning to harvest notable performance gains while strictly preserving original behavior for short inputs. For models using rotary position embedding (RoPE), significant enhancements are observed when employing RoPE-specific methods, such as NTK and SelfExtend, indicating RoPE's superiority over APE for context window extension. To facilitate future research, we release E5-Base-4k and E5-RoPE-Base, along with the LongEmbed benchmark.

### 中文抽取
内容：构造 LongEmbed benchmark（2 合成 + 4 真实任务），评测 embedding 模型从 512/4k 等上下文扩展到 32k 的检索能力；合成任务包括 Personalized Passkey Retrieval 等设置。

## URL 汇总

| 类型 | 链接 |
|---|---|
| 论文页 | https://arxiv.org/abs/2404.12096 |
| GitHub | https://github.com/dwzhu-pku/LongEmbed |
| other_emnlp-pdf_url | https://aclanthology.org/2024.emnlp-main.47.pdf |

## BibTeX

```bibtex
@misc{https://doi.org/10.48550/arxiv.2404.12096,
  doi = {10.48550/ARXIV.2404.12096},
  url = {https://arxiv.org/abs/2404.12096},
  author = {Zhu, Dawei and Wang, Liang and Yang, Nan and Song, Yifan and Wu, Wenhao and Wei, Furu and Li, Sujian},
  keywords = {Computation and Language (cs.CL), Machine Learning (cs.LG), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {LongEmbed: Extending Embedding Models for Long Context Retrieval},
  publisher = {arXiv},
  year = {2024},
  copyright = {Creative Commons Attribution 4.0 International}
}
```

## 备注

- 本卡片优先使用论文页、项目页与代码仓库等官方来源；若原报告中的链接存在错误，则以标题匹配后的官方链接为准。
