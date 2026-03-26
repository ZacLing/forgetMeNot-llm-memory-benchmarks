---
name: CLongEval
slug: clongeval
category: 长上下文理解与推理
subcategory: 长上下文综合任务
memory_type: Working / In-Context
year: "2024"
primary_source_kind: paper
primary_source_url: https://aclanthology.org/2024.findings-emnlp.230/
---

# CLongEval

## 结构化信息

| 字段 | 内容 |
|---|---|
| Benchmark | CLongEval |
| 分类 | 长上下文理解与推理 |
| 子类 | 长上下文综合任务 |
| 记忆侧重 | Working / In-Context |
| 首次年份 | 2024 |
| 主要来源类型 | paper |
| 论文标题 | CLongEval: A Chinese Benchmark for Evaluating Long-Context Large Language Models |

## 基础介绍

定位：CLongEval 是一个专门面向中文长上下文模型的 benchmark。
规模：包含 7 类任务、7,267 个样本，并覆盖从 1K 到 100K 的上下文窗口范围。
质量：除自动构造标签外，还包含 2,000+ 手工标注的问答对，因此适合用来分析中文 long-context LLM 在不同任务和长度区间上的能力差异。
用途：如果研究重点是中文环境、中文长文档理解，或者希望避免直接套用英文 benchmark，CLongEval 是非常直接的基线集合。

## Abstract
### 原始摘要
> Developing Large Language Models (LLMs) with robust long-context capabilities has been the recent research focus, resulting in the emergence of long-context LLMs proficient in Chinese. However, the evaluation of these models remains underdeveloped due to a lack of benchmarks. To address this gap, we present CLongEval, a comprehensive Chinese benchmark for evaluating long-context LLMs. CLongEval is characterized by three key features: (1) Sufficient data volume, comprising 7 distinct tasks and 7,267 examples; (2) Broad applicability, accommodating to models with context windows size from 1K to 100K; (3) High quality, with over 2,000 manually annotated question-answer pairs in addition to the automatically constructed labels. With CLongEval, we undertake a comprehensive assessment of 6 open-source long-context LLMs and 2 leading commercial counterparts that feature both long-context abilities and proficiency in Chinese. We also provide in-depth analysis based on the empirical results, trying to shed light on the critical capabilities that present challenges in long-context settings. The dataset, evaluation scripts, and model outputs are released.

### 中文抽取
CLongEval 以中文为中心，强调任务覆盖、长度跨度和标注质量三方面的平衡。它适合做中文 long-context 模型的标准化评测，也适合补足现有英文 benchmark 在中文场景下的空缺。

## URL 汇总

| 类型 | 链接 |
|---|---|
| 论文页 | https://arxiv.org/abs/2403.03514 |
| 发表页 | https://aclanthology.org/2024.findings-emnlp.230/ |
| GitHub | https://github.com/zexuanqiu/CLongEval |

## BibTeX

```bibtex
@inproceedings{qiu-etal-2024-clongeval,
  title = "{CL}ong{E}val: A {C}hinese Benchmark for Evaluating Long-Context Large Language Models",
  author = "Qiu, Zexuan and Li, Jingjing and Huang, Shijue and Jiao, Xiaoqi and Zhong, Wanjun and King, Irwin",
  editor = "Al-Onaizan, Yaser and Bansal, Mohit and Chen, Yun-Nung",
  booktitle = "Findings of the Association for Computational Linguistics: EMNLP 2024",
  month = nov,
  year = "2024",
  address = "Miami, Florida, USA",
  publisher = "Association for Computational Linguistics",
  url = "https://aclanthology.org/2024.findings-emnlp.230/",
  doi = "10.18653/v1/2024.findings-emnlp.230",
  pages = "3985--4004"
}
```

## 备注

- 本卡片以 ACL Anthology 正式发表页作为主引用来源，同时保留 arXiv 预印本与 GitHub 实现入口。
