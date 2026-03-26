---
name: MQuAKE
slug: mquake
language: en
category: Knowledge Editing and Semantic Memory Updates
subcategory: 知识编辑评测
memory_type: Semantic Memory Update
year: "2024"
primary_source_kind: paper
primary_source_url: https://arxiv.org/abs/2305.14795
counterpart_zh: ../../zh/06_knowledge_editing/mquake.md
---

# MQuAKE

[English Knowledge Base Index](../README.md) | [中文卡片](../../zh/06_knowledge_editing/mquake.md)

## Structured Metadata

| Field | Content |
|---|---|
| Benchmark | MQuAKE |
| Category | Knowledge Editing and Semantic Memory Updates |
| Subcategory | 知识编辑评测 |
| Memory Focus | Semantic Memory Update |
| First Year | 2024 |
| Primary Source Type | paper |
| Paper Title | MQuAKE: Assessing Knowledge Editing in Language Models via Multi-Hop Questions |
| Chinese Card | [MQuAKE](../../zh/06_knowledge_editing/mquake.md) |

## Overview

A multi-hop benchmark that tests whether factual edits propagate correctly through related reasoning chains.

## Abstract
### Original Abstract
> The information stored in large language models (LLMs) falls out of date quickly, and retraining from scratch is often not an option. This has recently given rise to a range of techniques for injecting new facts through updating model weights. Current evaluation paradigms are extremely limited, mainly validating the recall of edited facts, but changing one fact should cause rippling changes to the model's related beliefs. If we edit the UK Prime Minister to now be Rishi Sunak, then we should get a different answer to Who is married to the British Prime Minister? In this work, we present a benchmark, MQuAKE (Multi-hop Question Answering for Knowledge Editing), comprising multi-hop questions that assess whether edited models correctly answer questions where the answer should change as an entailed consequence of edited facts. While we find that current knowledge-editing approaches can recall edited facts accurately, they fail catastrophically on the constructed multi-hop questions. We thus propose a simple memory-based approach, MeLLo, which stores all edited facts externally while prompting the language model iteratively to generate answers that are consistent with the edited facts. While MQuAKE remains challenging, we show that MeLLo scales well with LLMs (e.g., OpenAI GPT-3.5-turbo) and outperforms previous model editors by a large margin.

### Curated Summary
A multi-hop benchmark that tests whether factual edits propagate correctly through related reasoning chains.

## Links

| Type | Link |
|---|---|
| Paper | https://arxiv.org/abs/2305.14795 |
| GitHub | https://github.com/princeton-nlp/MQuAKE |

## BibTeX

```bibtex
@misc{https://doi.org/10.48550/arxiv.2305.14795,
  doi = {10.48550/ARXIV.2305.14795},
  url = {https://arxiv.org/abs/2305.14795},
  author = {Zhong, Zexuan and Wu, Zhengxuan and Manning, Christopher D. and Potts, Christopher and Chen, Danqi},
  keywords = {Computation and Language (cs.CL), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {MQuAKE: Assessing Knowledge Editing in Language Models via Multi-Hop Questions},
  publisher = {arXiv},
  year = {2023},
  copyright = {arXiv.org perpetual, non-exclusive license}
}
```

## Remarks

- This card prioritizes official paper pages, project pages, and code repositories. When a link in the original report was incorrect, the corrected official link is used instead.
