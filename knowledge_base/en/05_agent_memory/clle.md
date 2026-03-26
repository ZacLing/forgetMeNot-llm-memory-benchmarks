---
name: CLLE
slug: clle
language: en
category: Agent Memory and Continual Learning
subcategory: Continual Learning and Feedback Memory
memory_type: Agentic / Procedural / Continual
year: "2022"
primary_source_kind: paper
primary_source_url: https://aclanthology.org/2022.findings-emnlp.30/
counterpart_zh: ../../zh/05_agent_memory/clle.md
---

# CLLE

[English Knowledge Base Index](../README.md) | [中文卡片](../../zh/05_agent_memory/clle.md)

## Structured Metadata

| Field | Content |
|---|---|
| Benchmark | CLLE |
| Category | Agent Memory and Continual Learning |
| Subcategory | Continual Learning and Feedback Memory |
| Memory Focus | Agentic / Procedural / Continual |
| First Year | 2022 |
| Primary Source Type | paper |
| Paper Title | CLLE: A Benchmark for Continual Language Learning Evaluation in Multilingual Machine Translation |
| Chinese Card | [CLLE](../../zh/05_agent_memory/clle.md) |

## Overview

A benchmark for continual language learning in multilingual machine translation.

## Abstract
### Original Abstract
> Continual Language Learning (CLL) in multilingual translation is inevitable when new languages are required to be translated. Due to the lack of unified and generalized benchmarks, the evaluation of existing methods is greatly influenced by experimental design which usually has a big gap from the industrial demands. In this work, we propose the first Continual Language Learning Evaluation benchmark CLLE in multilingual translation. CLLE consists of a Chinese-centric corpus — CN-25 and two CLL tasks — the close-distance language continual learning task and the language family continual learning task designed for real and disparate demands. Different from existing translation benchmarks, CLLE considers several restrictions for CLL, including domain distribution alignment, content overlap, language diversity, and the balance of corpus. Furthermore, we propose a novel framework COMETA based on Constrained Optimization and META-learning to alleviate catastrophic forgetting and dependency on history training data by using a meta-model to retain the important parameters for old languages. Our experiments prove that CLLE is a challenging CLL benchmark and that our proposed method is effective when compared with other strong baselines. Due to the construction of the corpus, the task designing and the evaluation method are independent of the centric language, we also construct and release the English-centric corpus EN-25 to facilitate academic research.

### Curated Summary
A benchmark for continual language learning in multilingual machine translation.

## Links

| Type | Link |
|---|---|
| Paper | https://aclanthology.org/2022.findings-emnlp.30/ |
| other_acl-anthology_url | https://aclanthology.org/2022.findings-emnlp.30/ |
| other_pdf_url | https://aclanthology.org/2022.findings-emnlp.30.pdf |

## BibTeX

```bibtex
@inproceedings{zhang-etal-2022-clle,
    title = "{CLLE}: A Benchmark for Continual Language Learning Evaluation in Multilingual Machine Translation",
    author = "Zhang, Han  and
      Zhang, Sheng  and
      Xiang, Yang  and
      Liang, Bin  and
      Su, Jinsong  and
      Miao, Zhongjian  and
      Wang, Hui  and
      Xu, Ruifeng",
    editor = "Goldberg, Yoav  and
      Kozareva, Zornitsa  and
      Zhang, Yue",
    booktitle = "Findings of the Association for Computational Linguistics: EMNLP 2022",
    month = dec,
    year = "2022",
    address = "Abu Dhabi, United Arab Emirates",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2022.findings-emnlp.30/",
    doi = "10.18653/v1/2022.findings-emnlp.30",
    pages = "428--443",
    abstract = "Continual Language Learning (CLL) in multilingual translation is inevitable when new languages are required to be translated. Due to the lack of unified and generalized benchmarks, the evaluation of existing methods is greatly influenced by experimental design which usually has a big gap from the industrial demands. In this work, we propose the first Continual Language Learning Evaluation benchmark CLLE in multilingual translation. CLLE consists of a Chinese-centric corpus {---} CN-25 and two CLL tasks {---} the close-distance language continual learning task and the language family continual learning task designed for real and disparate demands. Different from existing translation benchmarks, CLLE considers several restrictions for CLL, including domain distribution alignment, content overlap, language diversity, and the balance of corpus. Furthermore, we propose a novel framework COMETA based on Constrained Optimization and META-learning to alleviate catastrophic forgetting and dependency on history training data by using a meta-model to retain the important parameters for old languages. Our experiments prove that CLLE is a challenging CLL benchmark and that our proposed method is effective when compared with other strong baselines. Due to the construction of the corpus, the task designing and the evaluation method are independent of the centric language, we also construct and release the English-centric corpus EN-25 to facilitate academic research."
}
```

## Remarks

- The main paper link was completed through search because the source report only listed the ACL PDF.
