---
name: ∞Bench
slug: infinitebench
category: 长上下文理解与推理
subcategory: 长上下文综合任务
memory_type: Working / In-Context
year: "2024"
primary_source_kind: paper
primary_source_url: https://arxiv.org/abs/2402.13718
---

# ∞Bench

## 结构化信息

| 字段 | 内容 |
|---|---|
| Benchmark | ∞Bench |
| 分类 | 长上下文理解与推理 |
| 子类 | 长上下文综合任务 |
| 记忆侧重 | Working / In-Context |
| 首次年份 | 2024 |
| 主要来源类型 | paper |
| 论文标题 | $\infty$Bench: Extending Long Context Evaluation Beyond 100K Tokens |

## 基础介绍

定位：宣称“首个平均长度超过 100k tokens 的 LLM benchmark”，含合成与现实任务，中英双语。

## Abstract
### 原始摘要
> Processing and reasoning over long contexts is crucial for many practical applications of Large Language Models (LLMs), such as document comprehension and agent construction. Despite recent strides in making LLMs process contexts with more than 100K tokens, there is currently a lack of a standardized benchmark to evaluate this long-context capability. Existing public benchmarks typically focus on contexts around 10K tokens, limiting the assessment and comparison of LLMs in processing longer contexts. In this paper, we propose $\infty$Bench, the first LLM benchmark featuring an average data length surpassing 100K tokens. $\infty$Bench comprises synthetic and realistic tasks spanning diverse domains, presented in both English and Chinese. The tasks in $\infty$Bench are designed to require well understanding of long dependencies in contexts, and make simply retrieving a limited number of passages from contexts not sufficient for these tasks. In our experiments, based on $\infty$Bench, we evaluate the state-of-the-art proprietary and open-source LLMs tailored for processing long contexts. The results indicate that existing long context LLMs still require significant advancements to effectively process 100K+ context. We further present three intriguing analyses regarding the behavior of LLMs processing long context.

### 中文抽取
定位：宣称“首个平均长度超过 100k tokens 的 LLM benchmark”，含合成与现实任务，中英双语。

## URL 汇总

| 类型 | 链接 |
|---|---|
| 论文页 | https://arxiv.org/abs/2402.13718 |
| 论文 PDF | https://aclanthology.org/2024.acl-long.814.pdf |
| GitHub | https://github.com/OpenBMB/InfiniteBench |

## BibTeX

```bibtex
@article{https://doi.org/10.48550/arxiv.2402.13718,
  doi = {10.48550/ARXIV.2402.13718},
  url = {https://arxiv.org/abs/2402.13718},
  author = {Zhang, Xinrong and Chen, Yingfa and Hu, Shengding and Xu, Zihang and Chen, Junhao and Hao, Moo Khai and Han, Xu and Thai, Zhen Leng and Wang, Shuo and Liu, Zhiyuan and Sun, Maosong},
  keywords = {Computation and Language (cs.CL), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {$\infty$Bench: Extending Long Context Evaluation Beyond 100K Tokens},
  publisher = {arXiv},
  year = {2024},
  copyright = {arXiv.org perpetual, non-exclusive license}
}
```

## 备注

- 本卡片优先使用论文页、项目页与代码仓库等官方来源；若原报告中的链接存在错误，则以标题匹配后的官方链接为准。
