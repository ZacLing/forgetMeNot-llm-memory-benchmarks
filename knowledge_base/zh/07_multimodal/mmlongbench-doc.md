---
name: MMLongBench-Doc
slug: mmlongbench-doc
language: zh
category: 多模态长程记忆与检索推理
subcategory: 长文档与视觉文档
memory_type: Multimodal Long-Horizon
year: "2024"
primary_source_kind: paper
primary_source_url: https://arxiv.org/abs/2407.01523
counterpart_en: ../../en/07_multimodal/mmlongbench-doc.md
---

# MMLongBench-Doc

[中文知识库索引](../README.md) | [English Card](../../en/07_multimodal/mmlongbench-doc.md)

## 结构化信息

| 字段 | 内容 |
|---|---|
| Benchmark | MMLongBench-Doc |
| 分类 | 多模态长程记忆与检索推理 |
| 子类 | 长文档与视觉文档 |
| 记忆侧重 | Multimodal Long-Horizon |
| 首次年份 | 2024 |
| 主要来源类型 | paper |
| 论文标题 | MMLongBench-Doc: Benchmarking Long-context Document Understanding with Visualizations |
| 英文卡片 | [MMLongBench-Doc](../../en/07_multimodal/mmlongbench-doc.md) |

## 基础介绍

内容：基于多页 PDF（平均约 47.5 页、~21k tokens），含跨页与不可答问题；在多 LVLM 上评测，显示长文档多模态理解仍具挑战。

## Abstract
### 原始摘要
> Understanding documents with rich layouts and multi-modal components is a long-standing and practical task. Recent Large Vision-Language Models (LVLMs) have made remarkable strides in various tasks, particularly in single-page document understanding (DU). However, their abilities on long-context DU remain an open problem. This work presents MMLongBench-Doc, a long-context, multi-modal benchmark comprising 1,062 expert-annotated questions. Distinct from previous datasets, it is constructed upon 130 lengthy PDF-formatted documents with an average of 49.4 pages and 20,971 textual tokens. Towards comprehensive evaluation, answers to these questions rely on pieces of evidence from (1) different sources (text, image, chart, table, and layout structure) and (2) various locations (i.e. page number). Moreover, 33.2% of the questions are cross-page questions requiring evidence across multiple pages. 22.8% of the questions are designed to be unanswerable for detecting potential hallucinations. Experiments on 14 LVLMs demonstrate that long-context DU greatly challenges current models. Notably, the best-performing model, GPT-4o, achieves an F1 score of only 42.7%, while the second-best, GPT-4V, scores 31.4%. Furthermore, 12 LVLMs (all except GPT-4o and GPT-4V) even present worse performance than their LLM counterparts which are fed with lossy-parsed OCR documents. These results validate the necessity of future research toward more capable long-context LVLMs. Project Page: https://mayubo2333.github.io/MMLongBench-Doc

### 中文抽取
内容：基于多页 PDF（平均约 47.5 页、~21k tokens），含跨页与不可答问题；在多 LVLM 上评测，显示长文档多模态理解仍具挑战。

## URL 汇总

| 类型 | 链接 |
|---|---|
| 论文页 | https://arxiv.org/abs/2407.01523 |
| 项目主页 | https://mayubo2333.github.io/MMLongBench-Doc |
| GitHub | https://github.com/mayubo2333/MMLongBench-Doc |

## BibTeX

```bibtex
@misc{https://doi.org/10.48550/arxiv.2407.01523,
  doi = {10.48550/ARXIV.2407.01523},
  url = {https://arxiv.org/abs/2407.01523},
  author = {Ma, Yubo and Zang, Yuhang and Chen, Liangyu and Chen, Meiqi and Jiao, Yizhu and Li, Xinze and Lu, Xinyuan and Liu, Ziyu and Ma, Yan and Dong, Xiaoyi and Zhang, Pan and Pan, Liangming and Jiang, Yu-Gang and Wang, Jiaqi and Cao, Yixin and Sun, Aixin},
  keywords = {Computer Vision and Pattern Recognition (cs.CV), Computation and Language (cs.CL), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {MMLongBench-Doc: Benchmarking Long-context Document Understanding with Visualizations},
  publisher = {arXiv},
  year = {2024},
  copyright = {Creative Commons Attribution Non Commercial No Derivatives 4.0 International}
}
```

## 备注

- 本卡片优先使用论文页、项目页与代码仓库等官方来源；若原报告中的链接存在错误，则以标题匹配后的官方链接为准。
