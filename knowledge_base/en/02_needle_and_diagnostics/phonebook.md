---
name: Phonebook
slug: phonebook
language: en
category: Needle Retrieval and Diagnostic Probes
subcategory: Multi-Needle / Structured Retrieval
memory_type: Working / In-Context
year: "2024"
primary_source_kind: task-family
primary_source_url: https://arxiv.org/abs/2406.07887
counterpart_zh: ../../zh/02_needle_and_diagnostics/phonebook.md
---

# Phonebook

[English Knowledge Base Index](../README.md) | [中文卡片](../../zh/02_needle_and_diagnostics/phonebook.md)

## Structured Metadata

| Field | Content |
|---|---|
| Benchmark | Phonebook |
| Category | Needle Retrieval and Diagnostic Probes |
| Subcategory | Multi-Needle / Structured Retrieval |
| Memory Focus | Working / In-Context |
| First Year | 2024 |
| Primary Source Type | task-family |
| Paper Title | An Empirical Study of Mamba-based Language Models |
| Chinese Card | [Phonebook](../../zh/02_needle_and_diagnostics/phonebook.md) |

## Overview

A task family that measures long-context retrieval by querying names and phone numbers from large lookup tables.

## Abstract
### Original Abstract
> Selective state-space models (SSMs) like Mamba overcome some of the shortcomings of Transformers, such as quadratic computational complexity with sequence length and large inference-time memory requirements from the key-value cache. Moreover, recent studies have shown that SSMs can match or exceed the language modeling capabilities of Transformers, making them an attractive alternative. In a controlled setting (e.g., same data), however, studies so far have only presented small scale experiments comparing SSMs to Transformers. To understand the strengths and weaknesses of these architectures at larger scales, we present a direct comparison between 8B-parameter Mamba, Mamba-2, and Transformer models trained on the same datasets of up to 3.5T tokens. We also compare these models to a hybrid architecture consisting of 43% Mamba-2, 7% attention, and 50% MLP layers (Mamba-2-Hybrid). Using a diverse set of tasks, we answer the question of whether Mamba models can match Transformers at larger training budgets. Our results show that while pure SSMs match or exceed Transformers on many tasks, they lag behind Transformers on tasks which require strong copying or in-context learning abilities (e.g., 5-shot MMLU, Phonebook) or long-context reasoning. In contrast, we find that the 8B Mamba-2-Hybrid exceeds the 8B Transformer on all 12 standard tasks we evaluated (+2.65 points on average) and is predicted to be up to 8x faster when generating tokens at inference time. To validate long-context capabilities, we provide additional experiments evaluating variants of the Mamba-2-Hybrid and Transformer extended to support 16K, 32K, and 128K sequences. On an additional 23 long-context tasks, the hybrid model continues to closely match or exceed the Transformer on average. To enable further study, we release the checkpoints as well as the code used to train our models as part of NVIDIA's Megatron-LM project.

### Curated Summary
A task family that measures long-context retrieval by querying names and phone numbers from large lookup tables.

## Links

| Type | Link |
|---|---|
| Paper | https://arxiv.org/abs/2406.07887 |
| Dataset | https://huggingface.co/collections/booydar/phonebook-datasets |
| dataset_url_2 | https://huggingface.co/datasets/booydar/phonebook_N16 |

## BibTeX

```bibtex
@misc{https://doi.org/10.48550/arxiv.2406.07887,
  doi = {10.48550/ARXIV.2406.07887},
  url = {https://arxiv.org/abs/2406.07887},
  author = {Waleffe, Roger and Byeon, Wonmin and Riach, Duncan and Norick, Brandon and Korthikanti, Vijay and Dao, Tri and Gu, Albert and Hatamizadeh, Ali and Singh, Sudhakar and Narayanan, Deepak and Kulshreshtha, Garvit and Singh, Vartika and Casper, Jared and Kautz, Jan and Shoeybi, Mohammad and Catanzaro, Bryan},
  keywords = {Machine Learning (cs.LG), Computation and Language (cs.CL), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {An Empirical Study of Mamba-based Language Models},
  publisher = {arXiv},
  year = {2024},
  copyright = {arXiv.org perpetual, non-exclusive license}
}
```

## Remarks

- Phonebook is better viewed as a task family reused across multiple long-context papers than as a standalone benchmark paper. This card therefore follows the representative paper and dataset collection cited in the report.
