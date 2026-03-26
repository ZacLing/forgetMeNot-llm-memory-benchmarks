---
name: Video-MME
slug: video-mme
category: 多模态长程记忆与检索推理
subcategory: 视频长上下文
memory_type: Multimodal Long-Horizon
year: "2025"
primary_source_kind: paper
primary_source_url: https://arxiv.org/abs/2405.21075
---

# Video-MME

## 结构化信息

| 字段 | 内容 |
|---|---|
| Benchmark | Video-MME |
| 分类 | 多模态长程记忆与检索推理 |
| 子类 | 视频长上下文 |
| 记忆侧重 | Multimodal Long-Horizon |
| 首次年份 | 2025 |
| 主要来源类型 | paper |
| 论文标题 | Video-MME: The First-Ever Comprehensive Evaluation Benchmark of Multi-modal LLMs in Video Analysis |

## 基础介绍

数据：900 视频（约 254 小时）与 2,700 人工标注 QA；多域多时长。

## Abstract
### 原始摘要
> In the quest for artificial general intelligence, Multi-modal Large Language Models (MLLMs) have emerged as a focal point in recent advancements. However, the predominant focus remains on developing their capabilities in static image understanding. The potential of MLLMs in processing sequential visual data is still insufficiently explored, highlighting the absence of a comprehensive, high-quality assessment of their performance. In this paper, we introduce Video-MME, the first-ever full-spectrum, Multi-Modal Evaluation benchmark of MLLMs in Video analysis. Our work distinguishes from existing benchmarks through four key features: 1) Diversity in video types, spanning 6 primary visual domains with 30 subfields to ensure broad scenario generalizability; 2) Duration in temporal dimension, encompassing both short-, medium-, and long-term videos, ranging from 11 seconds to 1 hour, for robust contextual dynamics; 3) Breadth in data modalities, integrating multi-modal inputs besides video frames, including subtitles and audios, to unveil the all-round capabilities of MLLMs; 4) Quality in annotations, utilizing rigorous manual labeling by expert annotators to facilitate precise and reliable model assessment. 900 videos with a total of 254 hours are manually selected and annotated by repeatedly viewing all the video content, resulting in 2,700 question-answer pairs. With Video-MME, we extensively evaluate various state-of-the-art MLLMs, including GPT-4 series and Gemini 1.5 Pro, as well as open-source image models like InternVL-Chat-V1.5 and video models like LLaVA-NeXT-Video. Our experiments reveal that Gemini 1.5 Pro is the best-performing commercial model, significantly outperforming the open-source models. Our dataset along with these findings underscores the need for further improvements in handling longer sequences and multi-modal data. Project Page: https://video-mme.github.io

### 中文抽取
数据：900 视频（约 254 小时）与 2,700 人工标注 QA；多域多时长。

## URL 汇总

| 类型 | 链接 |
|---|---|
| 论文页 | https://arxiv.org/abs/2405.21075 |
| 项目主页 | https://video-mme.github.io/home_page.html |
| GitHub | https://github.com/MME-Benchmarks/Video-MME |

## BibTeX

```bibtex
@misc{https://doi.org/10.48550/arxiv.2405.21075,
  doi = {10.48550/ARXIV.2405.21075},
  url = {https://arxiv.org/abs/2405.21075},
  author = {Fu, Chaoyou and Dai, Yuhan and Luo, Yongdong and Li, Lei and Ren, Shuhuai and Zhang, Renrui and Wang, Zihan and Zhou, Chenyu and Shen, Yunhang and Zhang, Mengdan and Chen, Peixian and Li, Yanwei and Lin, Shaohui and Zhao, Sirui and Li, Ke and Xu, Tong and Zheng, Xiawu and Chen, Enhong and Shan, Caifeng and He, Ran and Sun, Xing},
  keywords = {Computer Vision and Pattern Recognition (cs.CV), Computation and Language (cs.CL), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {Video-MME: The First-Ever Comprehensive Evaluation Benchmark of Multi-modal LLMs in Video Analysis},
  publisher = {arXiv},
  year = {2024},
  copyright = {arXiv.org perpetual, non-exclusive license}
}
```

## 备注

- 本卡片优先使用论文页、项目页与代码仓库等官方来源；若原报告中的链接存在错误，则以标题匹配后的官方链接为准。
