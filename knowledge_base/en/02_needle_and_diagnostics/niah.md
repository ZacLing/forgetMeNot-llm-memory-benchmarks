---
name: Needle-in-a-Haystack
slug: niah
language: en
category: Needle Retrieval and Diagnostic Probes
subcategory: Needle / Passkey / Synthetic Diagnostics
memory_type: Working / In-Context
year: "2024"
primary_source_kind: repo-only
primary_source_url: https://github.com/gkamradt/LLMTest_NeedleInAHaystack
counterpart_zh: ../../zh/02_needle_and_diagnostics/niah.md
---

# Needle-in-a-Haystack

[English Knowledge Base Index](../README.md) | [中文卡片](../../zh/02_needle_and_diagnostics/niah.md)

## Structured Metadata

| Field | Content |
|---|---|
| Benchmark | Needle-in-a-Haystack |
| Category | Needle Retrieval and Diagnostic Probes |
| Subcategory | Needle / Passkey / Synthetic Diagnostics |
| Memory Focus | Working / In-Context |
| First Year | 2024 |
| Primary Source Type | repo-only |
| Paper Title | Needle In A Haystack - Pressure Testing LLMs |
| Chinese Card | [Needle-in-a-Haystack](../../zh/02_needle_and_diagnostics/niah.md) |

## Overview

The canonical needle-in-a-haystack stress test that inserts key facts into long contexts and asks models to recover them.

## Abstract
### Original Abstract
> Doing simple retrieval from LLM models at various context lengths to measure accuracy - gkamradt/LLMTest_NeedleInAHaystack

### Curated Summary
The canonical needle-in-a-haystack stress test that inserts key facts into long contexts and asks models to recover them.

## Links

| Type | Link |
|---|---|
| Project Page | https://github.com/open-compass/opencompass/blob/main/docs/en/advanced_guides/needleinahaystack_eval.md |
| GitHub | https://github.com/gkamradt/LLMTest_NeedleInAHaystack |

## BibTeX

```bibtex
@misc{kamradt2024needlehaystack,
  title = {Needle In A Haystack - Pressure Testing LLMs},
  author = {Greg Kamradt},
  howpublished = {GitHub repository},
  year = {2024},
  url = {https://github.com/gkamradt/LLMTest_NeedleInAHaystack},
  note = {Reference implementation widely used for long-context needle-in-a-haystack evaluation.}
}
```

## Remarks

- In the current literature, NIAH is better treated as a testing protocol and implementation pattern than as a single formally published benchmark paper. This card therefore uses the official GitHub implementation as the primary source.
