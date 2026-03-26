---
name: L-CiteEval
slug: l-citeeval
language: zh
category: 长上下文理解与推理
subcategory: 引用定位与忠实性
memory_type: Working / In-Context
year: "2024"
primary_source_kind: paper
primary_source_url: https://arxiv.org/abs/2410.02115
counterpart_en: ../../en/01_long_context/l-citeeval.md
---

# L-CiteEval

[中文知识库索引](../README.md) | [English Card](../../en/01_long_context/l-citeeval.md)

## 结构化信息

| 字段 | 内容 |
|---|---|
| Benchmark | L-CiteEval |
| 分类 | 长上下文理解与推理 |
| 子类 | 引用定位与忠实性 |
| 记忆侧重 | Working / In-Context |
| 首次年份 | 2024 |
| 主要来源类型 | paper |
| 论文标题 | L-CiteEval: Do Long-Context Models Truly Leverage Context for Responding? |
| 英文卡片 | [L-CiteEval](../../en/01_long_context/l-citeeval.md) |

## 基础介绍

特征：多任务长上下文 + 必须产出 citations；自动评测引用准确与召回，旨在检测“模型是否真正利用上下文而非靠固有知识”。

## Abstract
### 原始摘要
> Long-context models (LCMs) have made remarkable strides in recent years, offering users great convenience for handling tasks that involve long context, such as document summarization. As the community increasingly prioritizes the faithfulness of generated results, merely ensuring the accuracy of LCM outputs is insufficient, as it is quite challenging for humans to verify the results from the extremely lengthy context. Yet, although some efforts have been made to assess whether LCMs respond truly based on the context, these works either are limited to specific tasks or heavily rely on external evaluation resources like GPT4.In this work, we introduce L-CiteEval, a comprehensive multi-task benchmark for long-context understanding with citations, aiming to evaluate both the understanding capability and faithfulness of LCMs. L-CiteEval covers 11 tasks from diverse domains, spanning context lengths from 8K to 48K, and provides a fully automated evaluation suite. Through testing with 11 cutting-edge closed-source and open-source LCMs, we find that although these models show minor differences in their generated results, open-source models substantially trail behind their closed-source counterparts in terms of citation accuracy and recall. This suggests that current open-source LCMs are prone to responding based on their inherent knowledge rather than the given context, posing a significant risk to the user experience in practical applications. We also evaluate the RAG approach and observe that RAG can significantly improve the faithfulness of LCMs, albeit with a slight decrease in the generation quality. Furthermore, we discover a correlation between the attention mechanisms of LCMs and the citation generation process.

### 中文抽取
特征：多任务长上下文 + 必须产出 citations；自动评测引用准确与召回，旨在检测“模型是否真正利用上下文而非靠固有知识”。

## URL 汇总

| 类型 | 链接 |
|---|---|
| 论文页 | https://arxiv.org/abs/2410.02115 |
| GitHub | https://github.com/ZetangForward/L-CITEEVAL |

## BibTeX

```bibtex
@misc{https://doi.org/10.48550/arxiv.2410.02115,
  doi = {10.48550/ARXIV.2410.02115},
  url = {https://arxiv.org/abs/2410.02115},
  author = {Tang, Zecheng and Zhou, Keyan and Li, Juntao and Ji, Baibei and Hou, Jianye and Zhang, Min},
  keywords = {Computation and Language (cs.CL), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {L-CiteEval: Do Long-Context Models Truly Leverage Context for Responding?},
  publisher = {arXiv},
  year = {2024},
  copyright = {Creative Commons Attribution 4.0 International}
}
```

## 备注

- 本卡片优先使用论文页、项目页与代码仓库等官方来源；若原报告中的链接存在错误，则以标题匹配后的官方链接为准。
