---
name: MMNeedle
slug: mmneedle
language: zh
category: 多模态长程记忆与检索推理
subcategory: 多图 / 多模态检索推理
memory_type: Multimodal Long-Horizon
year: "2025"
primary_source_kind: paper
primary_source_url: https://arxiv.org/abs/2406.11230
counterpart_en: ../../en/07_multimodal/mmneedle.md
---

# MMNeedle

[中文知识库索引](../README.md) | [English Card](../../en/07_multimodal/mmneedle.md)

## 结构化信息

| 字段 | 内容 |
|---|---|
| Benchmark | MMNeedle |
| 分类 | 多模态长程记忆与检索推理 |
| 子类 | 多图 / 多模态检索推理 |
| 记忆侧重 | Multimodal Long-Horizon |
| 首次年份 | 2025 |
| 主要来源类型 | paper |
| 论文标题 | Multimodal Needle in a Haystack: Benchmarking Long-Context Capability of Multimodal Large Language Models |
| 英文卡片 | [MMNeedle](../../en/07_multimodal/mmneedle.md) |

## 基础介绍

特点：通过 multi-image 与 image stitching 增大上下文，评测模型按文本描述定位子图；并观察负样本幻觉。

## Abstract
### 原始摘要
> Multimodal Large Language Models (MLLMs) have shown significant promise in various applications, leading to broad interest from researchers and practitioners alike. However, a comprehensive evaluation of their long-context capabilities remains underexplored. To address these gaps, we introduce the MultiModal Needle-in-a-haystack (MMNeedle) benchmark, specifically designed to assess the long-context capabilities of MLLMs. Besides multi-image input, we employ image stitching to further increase the input context length, and develop a protocol to automatically generate labels for sub-image level retrieval. Essentially, MMNeedle evaluates MLLMs by stress-testing their capability to locate a target sub-image (needle) within a set of images (haystack) based on textual instructions and descriptions of image contents. This setup necessitates an advanced understanding of extensive visual contexts and effective information retrieval within long-context image inputs. With this benchmark, we evaluate state-of-the-art MLLMs, encompassing both API-based and open-source models. The findings reveal that GPT-4o consistently surpasses other models in long-context scenarios, but suffers from hallucination problems in negative samples, i.e., when needles are not in the haystacks. Our comprehensive long-context evaluation of MLLMs also sheds lights on the considerable performance gap between API-based and open-source models. All the code, data, and instructions required to reproduce the main results are available at https://github.com/Wang-ML-Lab/multimodal-needle-in-a-haystack.

### 中文抽取
特点：通过 multi-image 与 image stitching 增大上下文，评测模型按文本描述定位子图；并观察负样本幻觉。

## URL 汇总

| 类型 | 链接 |
|---|---|
| 论文页 | https://arxiv.org/abs/2406.11230 |
| 项目主页 | https://mmneedle.github.io/ |
| GitHub | https://github.com/Wang-ML-Lab/multimodal-needle-in-a-haystack |

## BibTeX

```bibtex
@misc{https://doi.org/10.48550/arxiv.2406.11230,
  doi = {10.48550/ARXIV.2406.11230},
  url = {https://arxiv.org/abs/2406.11230},
  author = {Wang, Hengyi and Shi, Haizhou and Tan, Shiwei and Qin, Weiyi and Wang, Wenyuan and Zhang, Tunyu and Nambi, Akshay and Ganu, Tanuja and Wang, Hao},
  keywords = {Machine Learning (cs.LG), Artificial Intelligence (cs.AI), Computation and Language (cs.CL), Computer Vision and Pattern Recognition (cs.CV), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {Multimodal Needle in a Haystack: Benchmarking Long-Context Capability of Multimodal Large Language Models},
  publisher = {arXiv},
  year = {2024},
  copyright = {Creative Commons Attribution 4.0 International}
}
```

## 备注

- 本卡片优先使用论文页、项目页与代码仓库等官方来源；若原报告中的链接存在错误，则以标题匹配后的官方链接为准。
