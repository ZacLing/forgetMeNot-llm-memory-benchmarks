---
name: LongBioBench
slug: longbiobench
category: 长上下文理解与推理
subcategory: 长上下文综合任务
memory_type: Working / In-Context
year: "2025"
primary_source_kind: paper
primary_source_url: https://arxiv.org/abs/2506.02921
---

# LongBioBench

## 结构化信息

| 字段 | 内容 |
|---|---|
| Benchmark | LongBioBench |
| 分类 | 长上下文理解与推理 |
| 子类 | 长上下文综合任务 |
| 记忆侧重 | Working / In-Context |
| 首次年份 | 2025 |
| 主要来源类型 | paper |
| 论文标题 | A Controllable Examination for Long-Context Language Models |

## 基础介绍

动机：指出传统 NIAH 的“上下文不连贯、数字针、无干扰项”等设计可能被模型投机；以连贯传记文本构造可控环境，从理解/推理/可信维度评估。

## Abstract
### 原始摘要
> Existing frameworks for evaluating long-context language models (LCLM) can be broadly categorized into real-world applications (e.g, document summarization) and synthetic tasks (e.g, needle-in-a-haystack). Despite their utility, both approaches are accompanied by certain intrinsic limitations. Real-world tasks often involve complexity that makes interpretation challenging and suffer from data contamination, whereas synthetic tasks frequently lack meaningful coherence between the target information (needle) and its surrounding context (haystack), undermining their validity as proxies for realistic applications. In response to these challenges, we posit that an ideal long-context evaluation framework should be characterized by three essential features: 1) seamless context 2) controllable setting and 3) sound evaluation. This study introduces $\textbf{LongBioBench}$, a benchmark that utilizes artificially generated biographies as a controlled environment for assessing LCLMs across dimensions of understanding, reasoning, and trustworthiness. Our experimental evaluation, which includes 18 LCLMs in total, demonstrates that most models still exhibit deficiencies in semantic understanding and elementary reasoning over retrieved results and are less trustworthy as context length increases. Our further analysis indicates some design choices employed by existing synthetic benchmarks, such as contextual non-coherence, numerical needles, and the absence of distractors, rendering them vulnerable to test the model's long-context capabilities. To sum up, compared to previous synthetic benchmarks, LongBioBench achieves a better trade-off between mirroring authentic language tasks and maintaining controllability, and is highly interpretable and configurable.

### 中文抽取
动机：指出传统 NIAH 的“上下文不连贯、数字针、无干扰项”等设计可能被模型投机；以连贯传记文本构造可控环境，从理解/推理/可信维度评估。

## URL 汇总

| 类型 | 链接 |
|---|---|
| 论文页 | https://arxiv.org/abs/2506.02921 |
| GitHub | https://github.com/Thomasyyj/LongBio-Benchmark |

## BibTeX

```bibtex
@misc{https://doi.org/10.48550/arxiv.2506.02921,
  doi = {10.48550/ARXIV.2506.02921},
  url = {https://arxiv.org/abs/2506.02921},
  author = {Yang, Yijun and Huang, Zeyu and Zhu, Wenhao and Qiu, Zihan and Yuan, Fei and Pan, Jeff Z. and Titov, Ivan},
  keywords = {Computation and Language (cs.CL), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {A Controllable Examination for Long-Context Language Models},
  publisher = {arXiv},
  year = {2025},
  copyright = {Creative Commons Attribution 4.0 International}
}
```

## 备注

- 本卡片优先使用论文页、项目页与代码仓库等官方来源；若原报告中的链接存在错误，则以标题匹配后的官方链接为准。
