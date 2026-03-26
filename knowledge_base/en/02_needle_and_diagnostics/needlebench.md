---
name: NeedleBench
slug: needlebench
language: en
category: Needle Retrieval and Diagnostic Probes
subcategory: Needle / Passkey / 合成诊断
memory_type: Working / In-Context
year: "2025"
primary_source_kind: paper
primary_source_url: https://arxiv.org/abs/2407.11963
counterpart_zh: ../../zh/02_needle_and_diagnostics/needlebench.md
---

# NeedleBench

[English Knowledge Base Index](../README.md) | [中文卡片](../../zh/02_needle_and_diagnostics/needlebench.md)

## Structured Metadata

| Field | Content |
|---|---|
| Benchmark | NeedleBench |
| Category | Needle Retrieval and Diagnostic Probes |
| Subcategory | Needle / Passkey / 合成诊断 |
| Memory Focus | Working / In-Context |
| First Year | 2025 |
| Primary Source Type | paper |
| Paper Title | NeedleBench: Evaluating LLM Retrieval and Reasoning Across Varying Information Densities |
| Chinese Card | [NeedleBench](../../zh/02_needle_and_diagnostics/needlebench.md) |

## Overview

A synthetic bilingual benchmark that systematically varies needle depth, density, and reasoning difficulty.

## Abstract
### Original Abstract
> The capability of large language models to handle long-context information is crucial across various real-world applications. Existing evaluation methods often rely either on real-world long texts, making it difficult to exclude the influence of models' inherent knowledge, or introduce irrelevant filler content to artificially achieve target lengths, reducing assessment effectiveness. To address these limitations, we introduce NeedleBench, a synthetic framework for assessing retrieval and reasoning performance in bilingual long-context tasks with adaptive context lengths. NeedleBench systematically embeds key data points at varying depths to rigorously test model capabilities. Tasks are categorized into two scenarios: information-sparse, featuring minimal relevant details within extensive irrelevant text to simulate simple retrieval tasks; and information-dense (the Ancestral Trace Challenge), where relevant information is continuously distributed throughout the context to simulate complex reasoning tasks. Our experiments reveal that although recent reasoning models like Deepseek-R1 and OpenAI's o3 excel in mathematical reasoning, they struggle with continuous retrieval and reasoning in information-dense scenarios, even at shorter context lengths. We also characterize a phenomenon termed 'under-thinking', where models prematurely conclude reasoning despite available information. NeedleBench thus provides critical insights and targeted tools essential for evaluating and improving LLMs' long-context capabilities. All resources are available at OpenCompass: https://github.com/open-compass/opencompass.

### Curated Summary
A synthetic bilingual benchmark that systematically varies needle depth, density, and reasoning difficulty.

## Links

| Type | Link |
|---|---|
| Paper | https://arxiv.org/abs/2407.11963 |
| paper_url_2 | https://openreview.net/forum?id=cEvmIKsRw0 |

## BibTeX

```bibtex
@misc{https://doi.org/10.48550/arxiv.2407.11963,
  doi = {10.48550/ARXIV.2407.11963},
  url = {https://arxiv.org/abs/2407.11963},
  author = {Li, Mo and Zhang, Songyang and Zhang, Taolin and Duan, Haodong and Liu, Yunxin and Chen, Kai},
  keywords = {Computation and Language (cs.CL), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {NeedleBench: Evaluating LLM Retrieval and Reasoning Across Varying Information Densities},
  publisher = {arXiv},
  year = {2024},
  copyright = {Creative Commons Attribution 4.0 International}
}
```

## Remarks

- This card prioritizes official paper pages, project pages, and code repositories. When a link in the original report was incorrect, the corrected official link is used instead.
