---
name: Visual Haystacks
slug: visual-haystacks
category: 多模态长程记忆与检索推理
subcategory: 多图 / 多模态检索推理
memory_type: Multimodal Long-Horizon
year: "2025"
primary_source_kind: paper
primary_source_url: https://arxiv.org/abs/2407.13766
---

# Visual Haystacks

## 结构化信息

| 字段 | 内容 |
|---|---|
| Benchmark | Visual Haystacks |
| 分类 | 多模态长程记忆与检索推理 |
| 子类 | 多图 / 多模态检索推理 |
| 记忆侧重 | Multimodal Long-Horizon |
| 首次年份 | 2025 |
| 主要来源类型 | paper |
| 论文标题 | Visual Haystacks: A Vision-Centric Needle-In-A-Haystack Benchmark |

## 基础介绍

定位：评测 LMM 在大量“可能不相关”的图像集合中检索并推理；并提供 MIRAGE 作为视觉 RAG baseline；项目页与 paper 给出。

## Abstract
### 原始摘要
> Large Multimodal Models (LMMs) have made significant strides in visual question-answering for single images. Recent advancements like long-context LMMs have allowed them to ingest larger, or even multiple, images. However, the ability to process a large number of visual tokens does not guarantee effective retrieval and reasoning for multi-image question answering (MIQA), especially in real-world applications like photo album searches or satellite imagery analysis. In this work, we first assess the limitations of current benchmarks for long-context LMMs. We address these limitations by introducing a new vision-centric, long-context benchmark, "Visual Haystacks (VHs)". We comprehensively evaluate both open-source and proprietary models on VHs, and demonstrate that these models struggle when reasoning across potentially unrelated images, perform poorly on cross-image reasoning, as well as exhibit biases based on the placement of key information within the context window. Towards a solution, we introduce MIRAGE (Multi-Image Retrieval Augmented Generation), an open-source, lightweight visual-RAG framework that processes up to 10k images on a single 40G A100 GPU -- far surpassing the 1k-image limit of contemporary models. MIRAGE demonstrates up to 13% performance improvement over existing open-source LMMs on VHs, sets a new state-of-the-art on the RetVQA multi-image QA benchmark, and achieves competitive performance on single-image QA with state-of-the-art LMMs. Our dataset, model, and code are available at: https://visual-haystacks.github.io.

### 中文抽取
定位：评测 LMM 在大量“可能不相关”的图像集合中检索并推理；并提供 MIRAGE 作为视觉 RAG baseline；项目页与 paper 给出。

## URL 汇总

| 类型 | 链接 |
|---|---|
| 论文页 | https://arxiv.org/abs/2407.13766 |
| 项目主页 | https://visual-haystacks.github.io/ |

## BibTeX

```bibtex
@misc{https://doi.org/10.48550/arxiv.2407.13766,
  doi = {10.48550/ARXIV.2407.13766},
  url = {https://arxiv.org/abs/2407.13766},
  author = {Wu, Tsung-Han and Biamby, Giscard and Quenum, Jerome and Gupta, Ritwik and Gonzalez, Joseph E. and Darrell, Trevor and Chan, David M.},
  keywords = {Computer Vision and Pattern Recognition (cs.CV), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {Visual Haystacks: A Vision-Centric Needle-In-A-Haystack Benchmark},
  publisher = {arXiv},
  year = {2024},
  copyright = {arXiv.org perpetual, non-exclusive license}
}
```

## 备注

- 本卡片优先使用论文页、项目页与代码仓库等官方来源；若原报告中的链接存在错误，则以标题匹配后的官方链接为准。
