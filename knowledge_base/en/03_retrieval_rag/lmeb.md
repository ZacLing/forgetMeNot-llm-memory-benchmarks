---
name: LMEB
slug: lmeb
language: en
category: Retrieval, Embeddings, and RAG
subcategory: 检索与表示学习
memory_type: Semantic / Retrieval-Augmented
year: "2026"
primary_source_kind: paper
primary_source_url: https://arxiv.org/abs/2603.12572
counterpart_zh: ../../zh/03_retrieval_rag/lmeb.md
---

# LMEB

[English Knowledge Base Index](../README.md) | [中文卡片](../../zh/03_retrieval_rag/lmeb.md)

## Structured Metadata

| Field | Content |
|---|---|
| Benchmark | LMEB |
| Category | Retrieval, Embeddings, and RAG |
| Subcategory | 检索与表示学习 |
| Memory Focus | Semantic / Retrieval-Augmented |
| First Year | 2026 |
| Primary Source Type | paper |
| Paper Title | LMEB: Long-horizon Memory Embedding Benchmark |
| Chinese Card | [LMEB](../../zh/03_retrieval_rag/lmeb.md) |

## Overview

A long-horizon memory embedding benchmark covering episodic, dialogue, semantic, and procedural retrieval.

## Abstract
### Original Abstract
> Memory embeddings are crucial for memory-augmented systems, such as OpenClaw, but their evaluation is underexplored in current text embedding benchmarks, which narrowly focus on traditional passage retrieval and fail to assess models' ability to handle long-horizon memory retrieval tasks involving fragmented, context-dependent, and temporally distant information. To address this, we introduce the Long-horizon Memory Embedding Benchmark (LMEB), a comprehensive framework that evaluates embedding models' capabilities in handling complex, long-horizon memory retrieval tasks. LMEB spans 22 datasets and 193 zero-shot retrieval tasks across 4 memory types: episodic, dialogue, semantic, and procedural, with both AI-generated and human-annotated data. These memory types differ in terms of level of abstraction and temporal dependency, capturing distinct aspects of memory retrieval that reflect the diverse challenges of the real world. We evaluate 15 widely used embedding models, ranging from hundreds of millions to ten billion parameters. The results reveal that (1) LMEB provides a reasonable level of difficulty; (2) Larger models do not always perform better; (3) LMEB and MTEB exhibit orthogonality. This suggests that the field has yet to converge on a universal model capable of excelling across all memory retrieval tasks, and that performance in traditional passage retrieval may not generalize to long-horizon memory retrieval. In summary, by providing a standardized and reproducible evaluation framework, LMEB fills a crucial gap in memory embedding evaluation, driving further advancements in text embedding for handling long-term, context-dependent memory retrieval. LMEB is available at https://github.com/KaLM-Embedding/LMEB.

### Curated Summary
A long-horizon memory embedding benchmark covering episodic, dialogue, semantic, and procedural retrieval.

## Links

| Type | Link |
|---|---|
| Paper | https://arxiv.org/abs/2603.12572 |
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

## Remarks

- This card prioritizes official paper pages, project pages, and code repositories. When a link in the original report was incorrect, the corrected official link is used instead.
