---
name: LongVideoBench
slug: longvideobench
category: 多模态长程记忆与检索推理
subcategory: 视频长上下文
memory_type: Multimodal Long-Horizon
year: "2024"
primary_source_kind: paper
primary_source_url: https://arxiv.org/abs/2407.15754
---

# LongVideoBench

## 结构化信息

| 字段 | 内容 |
|---|---|
| Benchmark | LongVideoBench |
| 分类 | 多模态长程记忆与检索推理 |
| 子类 | 视频长上下文 |
| 记忆侧重 | Multimodal Long-Horizon |
| 首次年份 | 2024 |
| 主要来源类型 | paper |
| 论文标题 | LongVideoBench: A Benchmark for Long-context Interleaved Video-Language Understanding |

## 基础介绍

数据：3,763 视频与字幕；6,678 多选题；强调“referring reasoning”。

## Abstract
### 原始摘要
> Large multimodal models (LMMs) are processing increasingly longer and richer inputs. Albeit the progress, few public benchmark is available to measure such development. To mitigate this gap, we introduce LongVideoBench, a question-answering benchmark that features video-language interleaved inputs up to an hour long. Our benchmark includes 3,763 varying-length web-collected videos with their subtitles across diverse themes, designed to comprehensively evaluate LMMs on long-term multimodal understanding. To achieve this, we interpret the primary challenge as to accurately retrieve and reason over detailed multimodal information from long inputs. As such, we formulate a novel video question-answering task termed referring reasoning. Specifically, as part of the question, it contains a referring query that references related video contexts, called referred context. The model is then required to reason over relevant video details from the referred context. Following the paradigm of referring reasoning, we curate 6,678 human-annotated multiple-choice questions in 17 fine-grained categories, establishing one of the most comprehensive benchmarks for long-form video understanding. Evaluations suggest that the LongVideoBench presents significant challenges even for the most advanced proprietary models (e.g. GPT-4o, Gemini-1.5-Pro, GPT-4-Turbo), while their open-source counterparts show an even larger performance gap. In addition, our results indicate that model performance on the benchmark improves only when they are capable of processing more frames, positioning LongVideoBench as a valuable benchmark for evaluating future-generation long-context LMMs.

### 中文抽取
数据：3,763 视频与字幕；6,678 多选题；强调“referring reasoning”。

## URL 汇总

| 类型 | 链接 |
|---|---|
| 论文页 | https://arxiv.org/abs/2407.15754 |
| GitHub | https://github.com/longvideobench/LongVideoBench |
| 数据集页 | https://huggingface.co/datasets/longvideobench/LongVideoBench |

## BibTeX

```bibtex
@misc{https://doi.org/10.48550/arxiv.2407.15754,
  doi = {10.48550/ARXIV.2407.15754},
  url = {https://arxiv.org/abs/2407.15754},
  author = {Wu, Haoning and Li, Dongxu and Chen, Bei and Li, Junnan},
  keywords = {Computer Vision and Pattern Recognition (cs.CV), Computation and Language (cs.CL), Machine Learning (cs.LG), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {LongVideoBench: A Benchmark for Long-context Interleaved Video-Language Understanding},
  publisher = {arXiv},
  year = {2024},
  copyright = {Creative Commons Attribution Non Commercial Share Alike 4.0 International}
}
```

## 备注

- 本卡片优先使用论文页、项目页与代码仓库等官方来源；若原报告中的链接存在错误，则以标题匹配后的官方链接为准。
