---
name: MM-NIAH
slug: mm-niah
category: 多模态长程记忆与检索推理
subcategory: 多图 / 多模态检索推理
memory_type: Multimodal Long-Horizon
year: "2024"
primary_source_kind: paper
primary_source_url: https://arxiv.org/abs/2406.07230
---

# MM-NIAH

## 结构化信息

| 字段 | 内容 |
|---|---|
| Benchmark | MM-NIAH |
| 分类 | 多模态长程记忆与检索推理 |
| 子类 | 多图 / 多模态检索推理 |
| 记忆侧重 | Multimodal Long-Horizon |
| 首次年份 | 2024 |
| 主要来源类型 | paper |
| 论文标题 | Needle In A Multimodal Haystack |

## 基础介绍

设计：把多段图文文档拼接成超长图文“干草堆”，任务含 retrieval/counting/reasoning。

## Abstract
### 原始摘要
> With the rapid advancement of multimodal large language models (MLLMs), their evaluation has become increasingly comprehensive. However, understanding long multimodal content, as a foundational ability for real-world applications, remains underexplored. In this work, we present Needle In A Multimodal Haystack (MM-NIAH), the first benchmark specifically designed to systematically evaluate the capability of existing MLLMs to comprehend long multimodal documents. Our benchmark includes three types of evaluation tasks: multimodal retrieval, counting, and reasoning. In each task, the model is required to answer the questions according to different key information scattered throughout the given multimodal document. Evaluating the leading MLLMs on MM-NIAH, we observe that existing models still have significant room for improvement on these tasks, especially on vision-centric evaluation. We hope this work can provide a platform for further research on long multimodal document comprehension and contribute to the advancement of MLLMs. Code and benchmark are released at https://github.com/OpenGVLab/MM-NIAH.

### 中文抽取
设计：把多段图文文档拼接成超长图文“干草堆”，任务含 retrieval/counting/reasoning。

## URL 汇总

| 类型 | 链接 |
|---|---|
| 论文页 | https://arxiv.org/abs/2406.07230 |
| 项目主页 | https://mm-niah.github.io/ |
| GitHub | https://github.com/OpenGVLab/MM-NIAH |
| 数据集页 | https://huggingface.co/datasets/OpenGVLab/MM-NIAH |

## BibTeX

```bibtex
@misc{https://doi.org/10.48550/arxiv.2406.07230,
  doi = {10.48550/ARXIV.2406.07230},
  url = {https://arxiv.org/abs/2406.07230},
  author = {Wang, Weiyun and Zhang, Shuibo and Ren, Yiming and Duan, Yuchen and Li, Tiantong and Liu, Shuo and Hu, Mengkang and Chen, Zhe and Zhang, Kaipeng and Lu, Lewei and Zhu, Xizhou and Luo, Ping and Qiao, Yu and Dai, Jifeng and Shao, Wenqi and Wang, Wenhai},
  keywords = {Computer Vision and Pattern Recognition (cs.CV), Artificial Intelligence (cs.AI), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {Needle In A Multimodal Haystack},
  publisher = {arXiv},
  year = {2024},
  copyright = {Creative Commons Attribution 4.0 International}
}
```

## 备注

- 本卡片优先使用论文页、项目页与代码仓库等官方来源；若原报告中的链接存在错误，则以标题匹配后的官方链接为准。
