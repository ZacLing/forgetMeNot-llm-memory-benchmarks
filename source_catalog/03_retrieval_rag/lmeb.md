---
name: LMEB
slug: lmeb
category: 检索、Embedding 与 RAG
subcategory: 检索与表示学习
memory_type: Semantic / Retrieval-Augmented
year: "2026"
primary_source_kind: paper
primary_source_url: https://arxiv.org/abs/2603.12572
---

# LMEB

## 结构化信息

| 字段 | 内容 |
|---|---|
| Benchmark | LMEB |
| 分类 | 检索、Embedding 与 RAG |
| 子类 | 检索与表示学习 |
| 记忆侧重 | Semantic / Retrieval-Augmented |
| 首次年份 | 2026 |
| 主要来源类型 | paper |
| 论文标题 | LMEB: Long-horizon Memory Embedding Benchmark |

## 基础介绍

定位：明确指出传统 embedding 基准（如 MTEB）主要覆盖“passage retrieval”，不足以衡量“碎片化、上下文依赖、时间跨度远”的记忆检索；因此提出 LMEB，覆盖 22 datasets、193 zero‑shot retrieval tasks、4 种记忆类型（episodic/dialogue/semantic/procedural），并指出与 MTEB 存在“正交性”。

## Abstract
### 原始摘要
> Memory embeddings are crucial for memory-augmented systems, such as OpenClaw, but their evaluation is underexplored in current text embedding benchmarks, which narrowly focus on traditional passage retrieval and fail to assess models' ability to handle long-horizon memory retrieval tasks involving fragmented, context-dependent, and temporally distant information. To address this, we introduce the Long-horizon Memory Embedding Benchmark (LMEB), a comprehensive framework that evaluates embedding models' capabilities in handling complex, long-horizon memory retrieval tasks. LMEB spans 22 datasets and 193 zero-shot retrieval tasks across 4 memory types: episodic, dialogue, semantic, and procedural, with both AI-generated and human-annotated data. These memory types differ in terms of level of abstraction and temporal dependency, capturing distinct aspects of memory retrieval that reflect the diverse challenges of the real world. We evaluate 15 widely used embedding models, ranging from hundreds of millions to ten billion parameters. The results reveal that (1) LMEB provides a reasonable level of difficulty; (2) Larger models do not always perform better; (3) LMEB and MTEB exhibit orthogonality. This suggests that the field has yet to converge on a universal model capable of excelling across all memory retrieval tasks, and that performance in traditional passage retrieval may not generalize to long-horizon memory retrieval. In summary, by providing a standardized and reproducible evaluation framework, LMEB fills a crucial gap in memory embedding evaluation, driving further advancements in text embedding for handling long-term, context-dependent memory retrieval. LMEB is available at https://github.com/KaLM-Embedding/LMEB.

### 中文抽取
定位：明确指出传统 embedding 基准（如 MTEB）主要覆盖“passage retrieval”，不足以衡量“碎片化、上下文依赖、时间跨度远”的记忆检索；因此提出 LMEB，覆盖 22 datasets、193 zero‑shot retrieval tasks、4 种记忆类型（episodic/dialogue/semantic/procedural），并指出与 MTEB 存在“正交性”。

## URL 汇总

| 类型 | 链接 |
|---|---|
| 论文页 | https://arxiv.org/abs/2603.12572 |
| GitHub | https://github.com/KaLM-Embedding/LMEB |

## BibTeX

```bibtex
@misc{https://doi.org/10.48550/arxiv.2603.12572,
  doi = {10.48550/ARXIV.2603.12572},
  url = {https://arxiv.org/abs/2603.12572},
  author = {Zhao, Xinping and Hu, Xinshuo and Xu, Jiaxin and Tang, Danyu and Zhang, Xin and Zhou, Mengjia and Zhong, Yan and Zhou, Yao and Shan, Zifei and Zhang, Meishan and Hu, Baotian and Zhang, Min},
  keywords = {Computation and Language (cs.CL), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {LMEB: Long-horizon Memory Embedding Benchmark},
  publisher = {arXiv},
  year = {2026},
  copyright = {arXiv.org perpetual, non-exclusive license}
}
```

## 备注

- 本卡片优先使用论文页、项目页与代码仓库等官方来源；若原报告中的链接存在错误，则以标题匹配后的官方链接为准。
