---
name: Passkey Retrieval
slug: passkey-retrieval
language: en
category: Needle Retrieval and Diagnostic Probes
subcategory: Needle / Passkey / Synthetic Diagnostics
memory_type: Working / In-Context
year: "2023"
primary_source_kind: paper
primary_source_url: https://arxiv.org/abs/2305.16300
counterpart_zh: ../../zh/02_needle_and_diagnostics/passkey-retrieval.md
---

# Passkey Retrieval

[English Knowledge Base Index](../README.md) | [中文卡片](../../zh/02_needle_and_diagnostics/passkey-retrieval.md)

## Structured Metadata

| Field | Content |
|---|---|
| Benchmark | Passkey Retrieval |
| Category | Needle Retrieval and Diagnostic Probes |
| Subcategory | Needle / Passkey / Synthetic Diagnostics |
| Memory Focus | Working / In-Context |
| First Year | 2023 |
| Primary Source Type | paper |
| Paper Title | Landmark Attention: Random-Access Infinite Context Length for Transformers |
| Chinese Card | [Passkey Retrieval](../../zh/02_needle_and_diagnostics/passkey-retrieval.md) |

## Overview

A classic passkey recall setup, originating from Landmark Attention, for testing retrieval of a hidden random key.

## Abstract
### Original Abstract
> While Transformers have shown remarkable success in natural language processing, their attention mechanism's large memory requirements have limited their ability to handle longer contexts. Prior approaches, such as recurrent memory or retrieval-based augmentation, have either compromised the random-access flexibility of attention (i.e., the capability to select any token in the entire context) or relied on separate mechanisms for relevant context retrieval, which may not be compatible with the model's attention. In this paper, we present a novel approach that allows access to the complete context while retaining random-access flexibility, closely resembling running attention on the entire context. Our method uses a landmark token to represent each block of the input and trains the attention to use it for selecting relevant blocks, enabling retrieval of blocks directly through the attention mechanism instead of by relying on a separate mechanism. Our approach seamlessly integrates with specialized data structures and the system's memory hierarchy, enabling processing of arbitrarily long context lengths. We demonstrate that our method can obtain comparable performance with Transformer-XL while significantly reducing the number of retrieved tokens in each step. Finally, we show that fine-tuning LLaMA 7B with our method successfully extends its context length capacity to over 32k tokens, allowing for inference at the context lengths of GPT-4. We release the implementation of landmark attention and the code to reproduce our experiments at https://github.com/epfml/landmark-attention/.

### Curated Summary
A classic passkey recall setup, originating from Landmark Attention, for testing retrieval of a hidden random key.

## Links

| Type | Link |
|---|---|
| Paper | https://arxiv.org/abs/2305.16300 |
| GitHub | https://github.com/epfml/landmark-attention/ |

## BibTeX

```bibtex
@misc{https://doi.org/10.48550/arxiv.2305.16300,
  doi = {10.48550/ARXIV.2305.16300},
  url = {https://arxiv.org/abs/2305.16300},
  author = {Mohtashami, Amirkeivan and Jaggi, Martin},
  keywords = {Computation and Language (cs.CL), Machine Learning (cs.LG), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {Landmark Attention: Random-Access Infinite Context Length for Transformers},
  publisher = {arXiv},
  year = {2023},
  copyright = {arXiv.org perpetual, non-exclusive license}
}
```

## Remarks

- This card prioritizes official paper pages, project pages, and code repositories. When a link in the original report was incorrect, the corrected official link is used instead.
