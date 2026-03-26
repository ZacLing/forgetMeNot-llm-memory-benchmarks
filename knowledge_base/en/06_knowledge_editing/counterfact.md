---
name: CounterFact
slug: counterfact
language: en
category: Knowledge Editing and Semantic Memory Updates
subcategory: Knowledge Editing Evaluation
memory_type: Semantic Memory Update
year: "2023"
primary_source_kind: paper
primary_source_url: https://arxiv.org/abs/2202.05262
counterpart_zh: ../../zh/06_knowledge_editing/counterfact.md
---

# CounterFact

[English Knowledge Base Index](../README.md) | [中文卡片](../../zh/06_knowledge_editing/counterfact.md)

## Structured Metadata

| Field | Content |
|---|---|
| Benchmark | CounterFact |
| Category | Knowledge Editing and Semantic Memory Updates |
| Subcategory | Knowledge Editing Evaluation |
| Memory Focus | Semantic Memory Update |
| First Year | 2023 |
| Primary Source Type | paper |
| Paper Title | Locating and Editing Factual Associations in GPT |
| Chinese Card | [CounterFact](../../zh/06_knowledge_editing/counterfact.md) |

## Overview

A classic counterfactual dataset introduced by ROME for evaluating factual editing efficacy, specificity, and generalization.

## Abstract
### Original Abstract
> We analyze the storage and recall of factual associations in autoregressive transformer language models, finding evidence that these associations correspond to localized, directly-editable computations. We first develop a causal intervention for identifying neuron activations that are decisive in a model's factual predictions. This reveals a distinct set of steps in middle-layer feed-forward modules that mediate factual predictions while processing subject tokens. To test our hypothesis that these computations correspond to factual association recall, we modify feed-forward weights to update specific factual associations using Rank-One Model Editing (ROME). We find that ROME is effective on a standard zero-shot relation extraction (zsRE) model-editing task, comparable to existing methods. To perform a more sensitive evaluation, we also evaluate ROME on a new dataset of counterfactual assertions, on which it simultaneously maintains both specificity and generalization, whereas other methods sacrifice one or another. Our results confirm an important role for mid-layer feed-forward modules in storing factual associations and suggest that direct manipulation of computational mechanisms may be a feasible approach for model editing. The code, dataset, visualizations, and an interactive demo notebook are available at https://rome.baulab.info/

### Curated Summary
A classic counterfactual dataset introduced by ROME for evaluating factual editing efficacy, specificity, and generalization.

## Links

| Type | Link |
|---|---|
| Paper | https://arxiv.org/abs/2202.05262 |
| Project Page | https://rome.baulab.info/ |
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

## Remarks

- This card prioritizes official paper pages, project pages, and code repositories. When a link in the original report was incorrect, the corrected official link is used instead.
