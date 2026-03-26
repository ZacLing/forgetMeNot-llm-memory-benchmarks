---
name: InfoHaystack
slug: infohaystack
category: 多模态长程记忆与检索推理
subcategory: 长文档与视觉文档
memory_type: Multimodal Long-Horizon
year: "2024"
primary_source_kind: paper
primary_source_url: https://arxiv.org/abs/2411.16740
---

# InfoHaystack

## 结构化信息

| 字段 | 内容 |
|---|---|
| Benchmark | InfoHaystack |
| 分类 | 多模态长程记忆与检索推理 |
| 子类 | 长文档与视觉文档 |
| 记忆侧重 | Multimodal Long-Horizon |
| 首次年份 | 2024 |
| 主要来源类型 | paper |
| 论文标题 | Document Haystacks: Vision-Language Reasoning Over Piles of 1000+ Documents |

## 基础介绍

既有多图 QA 候选集合过小，不足以代表真实检索，因此该工作提出可扩展到 1,000 视觉文档的检索与理解基准，并报告 recall@1 等检索指标。

## Abstract
### 原始摘要
> Large multimodal models (LMMs) have achieved impressive progress in vision-language understanding, yet they face limitations in real-world applications requiring complex reasoning over a large number of images. Existing benchmarks for multi-image question-answering are limited in scope, each question is paired with only up to 30 images, which does not fully capture the demands of large-scale retrieval tasks encountered in the real-world usages. To reduce these gaps, we introduce two document haystack benchmarks, dubbed DocHaystack and InfoHaystack, designed to evaluate LMM performance on large-scale visual document retrieval and understanding. Additionally, we propose V-RAG, a novel, vision-centric retrieval-augmented generation (RAG) framework that leverages a suite of multimodal vision encoders, each optimized for specific strengths, and a dedicated question-document relevance module. V-RAG sets a new standard, with a 9% and 11% improvement in Recall@1 on the challenging DocHaystack-1000 and InfoHaystack-1000 benchmarks, respectively, compared to the previous best baseline models. Additionally, integrating V-RAG with LMMs enables them to efficiently operate across thousands of images, yielding significant improvements on our DocHaystack and InfoHaystack benchmarks. Our code and datasets are available at https://github.com/Vision-CAIR/dochaystacks

### 中文抽取
既有多图 QA 候选集合过小，不足以代表真实检索，因此该工作提出可扩展到 1,000 视觉文档的检索与理解基准，并报告 recall@1 等检索指标。

## URL 汇总

| 类型 | 链接 |
|---|---|
| 论文页 | https://arxiv.org/abs/2411.16740 |
| GitHub | https://github.com/Vision-CAIR/dochaystacks |

## BibTeX

```bibtex
@misc{https://doi.org/10.48550/arxiv.2411.16740,
  doi = {10.48550/ARXIV.2411.16740},
  url = {https://arxiv.org/abs/2411.16740},
  author = {Chen, Jun and Xu, Dannong and Fei, Junjie and Feng, Chun-Mei and Elhoseiny, Mohamed},
  keywords = {Computer Vision and Pattern Recognition (cs.CV), Artificial Intelligence (cs.AI), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {Document Haystacks: Vision-Language Reasoning Over Piles of 1000+ Documents},
  publisher = {arXiv},
  year = {2024},
  copyright = {Creative Commons Attribution 4.0 International}
}
```

## 备注

- 本卡片优先使用论文页、项目页与代码仓库等官方来源；若原报告中的链接存在错误，则以标题匹配后的官方链接为准。
