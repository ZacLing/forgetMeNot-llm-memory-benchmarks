---
name: L-CiteEval
slug: l-citeeval
language: en
category: Long-Context Understanding and Reasoning
subcategory: 引用定位与忠实性
memory_type: Working / In-Context
year: "2024"
primary_source_kind: paper
primary_source_url: https://arxiv.org/abs/2410.02115
counterpart_zh: ../../zh/01_long_context/l-citeeval.md
---

# L-CiteEval

[English Knowledge Base Index](../README.md) | [中文卡片](../../zh/01_long_context/l-citeeval.md)

## Structured Metadata

| Field | Content |
|---|---|
| Benchmark | L-CiteEval |
| Category | Long-Context Understanding and Reasoning |
| Subcategory | 引用定位与忠实性 |
| Memory Focus | Working / In-Context |
| First Year | 2024 |
| Primary Source Type | paper |
| Paper Title | L-CiteEval: Do Long-Context Models Truly Leverage Context for Responding? |
| Chinese Card | [L-CiteEval](../../zh/01_long_context/l-citeeval.md) |

## Overview

A citation-grounded long-context benchmark that scores both answer quality and citation precision and recall.

## Abstract
### Original Abstract
> Long-context models (LCMs) have made remarkable strides in recent years, offering users great convenience for handling tasks that involve long context, such as document summarization. As the community increasingly prioritizes the faithfulness of generated results, merely ensuring the accuracy of LCM outputs is insufficient, as it is quite challenging for humans to verify the results from the extremely lengthy context. Yet, although some efforts have been made to assess whether LCMs respond truly based on the context, these works either are limited to specific tasks or heavily rely on external evaluation resources like GPT4.In this work, we introduce L-CiteEval, a comprehensive multi-task benchmark for long-context understanding with citations, aiming to evaluate both the understanding capability and faithfulness of LCMs. L-CiteEval covers 11 tasks from diverse domains, spanning context lengths from 8K to 48K, and provides a fully automated evaluation suite. Through testing with 11 cutting-edge closed-source and open-source LCMs, we find that although these models show minor differences in their generated results, open-source models substantially trail behind their closed-source counterparts in terms of citation accuracy and recall. This suggests that current open-source LCMs are prone to responding based on their inherent knowledge rather than the given context, posing a significant risk to the user experience in practical applications. We also evaluate the RAG approach and observe that RAG can significantly improve the faithfulness of LCMs, albeit with a slight decrease in the generation quality. Furthermore, we discover a correlation between the attention mechanisms of LCMs and the citation generation process.

### Curated Summary
A citation-grounded long-context benchmark that scores both answer quality and citation precision and recall.

## Links

| Type | Link |
|---|---|
| Paper | https://arxiv.org/abs/2410.02115 |
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

## Remarks

- This card prioritizes official paper pages, project pages, and code repositories. When a link in the original report was incorrect, the corrected official link is used instead.
