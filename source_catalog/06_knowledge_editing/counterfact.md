---
name: CounterFact
slug: counterfact
category: 知识编辑与语义记忆更新
subcategory: 知识编辑评测
memory_type: Semantic Memory Update
year: "2023"
primary_source_kind: paper
primary_source_url: https://arxiv.org/abs/2202.05262
---

# CounterFact

## 结构化信息

| 字段 | 内容 |
|---|---|
| Benchmark | CounterFact |
| 分类 | 知识编辑与语义记忆更新 |
| 子类 | 知识编辑评测 |
| 记忆侧重 | Semantic Memory Update |
| 首次年份 | 2023 |
| 主要来源类型 | paper |
| 论文标题 | Locating and Editing Factual Associations in GPT |

## 基础介绍

来源：ROME 论文明确提出“COUNTERFACT”作为更敏感的编辑评测数据集；并提供项目页与代码。

## Abstract
### 原始摘要
> We analyze the storage and recall of factual associations in autoregressive transformer language models, finding evidence that these associations correspond to localized, directly-editable computations. We first develop a causal intervention for identifying neuron activations that are decisive in a model's factual predictions. This reveals a distinct set of steps in middle-layer feed-forward modules that mediate factual predictions while processing subject tokens. To test our hypothesis that these computations correspond to factual association recall, we modify feed-forward weights to update specific factual associations using Rank-One Model Editing (ROME). We find that ROME is effective on a standard zero-shot relation extraction (zsRE) model-editing task, comparable to existing methods. To perform a more sensitive evaluation, we also evaluate ROME on a new dataset of counterfactual assertions, on which it simultaneously maintains both specificity and generalization, whereas other methods sacrifice one or another. Our results confirm an important role for mid-layer feed-forward modules in storing factual associations and suggest that direct manipulation of computational mechanisms may be a feasible approach for model editing. The code, dataset, visualizations, and an interactive demo notebook are available at https://rome.baulab.info/

### 中文抽取
来源：ROME 论文明确提出“COUNTERFACT”作为更敏感的编辑评测数据集；并提供项目页与代码。

## URL 汇总

| 类型 | 链接 |
|---|---|
| 论文页 | https://arxiv.org/abs/2202.05262 |
| 项目主页 | https://rome.baulab.info/ |
| GitHub | https://github.com/kmeng01/rome |

## BibTeX

```bibtex
@misc{https://doi.org/10.48550/arxiv.2202.05262,
  doi = {10.48550/ARXIV.2202.05262},
  url = {https://arxiv.org/abs/2202.05262},
  author = {Meng, Kevin and Bau, David and Andonian, Alex and Belinkov, Yonatan},
  keywords = {Computation and Language (cs.CL), Machine Learning (cs.LG), FOS: Computer and information sciences, FOS: Computer and information sciences, I.2.7},
  title = {Locating and Editing Factual Associations in GPT},
  publisher = {arXiv},
  year = {2022},
  copyright = {arXiv.org perpetual, non-exclusive license}
}
```

## 备注

- 本卡片优先使用论文页、项目页与代码仓库等官方来源；若原报告中的链接存在错误，则以标题匹配后的官方链接为准。
