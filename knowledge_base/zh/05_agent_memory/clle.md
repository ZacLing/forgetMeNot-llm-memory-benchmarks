---
name: CLLE
slug: clle
language: zh
category: 智能体记忆与持续学习
subcategory: 持续学习与反馈记忆
memory_type: Agentic / Procedural / Continual
year: "2022"
primary_source_kind: paper
primary_source_url: https://aclanthology.org/2022.findings-emnlp.30/
counterpart_en: ../../en/05_agent_memory/clle.md
---

# CLLE

[中文知识库索引](../README.md) | [English Card](../../en/05_agent_memory/clle.md)

## 结构化信息

| 字段 | 内容 |
|---|---|
| Benchmark | CLLE |
| 分类 | 智能体记忆与持续学习 |
| 子类 | 持续学习与反馈记忆 |
| 记忆侧重 | Agentic / Procedural / Continual |
| 首次年份 | 2022 |
| 主要来源类型 | paper |
| 论文标题 | CLLE: A Benchmark for Continual Language Learning Evaluation in Multilingual Machine Translation |
| 英文卡片 | [CLLE](../../en/05_agent_memory/clle.md) |

## 基础介绍

定义：提出 Continual Language Learning Evaluation（CLLE）用于多语翻译持续学习评测。

## Abstract
### 原始摘要
> Continual Language Learning (CLL) in multilingual translation is inevitable when new languages are required to be translated. Due to the lack of unified and generalized benchmarks, the evaluation of existing methods is greatly influenced by experimental design which usually has a big gap from the industrial demands. In this work, we propose the first Continual Language Learning Evaluation benchmark CLLE in multilingual translation. CLLE consists of a Chinese-centric corpus — CN-25 and two CLL tasks — the close-distance language continual learning task and the language family continual learning task designed for real and disparate demands. Different from existing translation benchmarks, CLLE considers several restrictions for CLL, including domain distribution alignment, content overlap, language diversity, and the balance of corpus. Furthermore, we propose a novel framework COMETA based on Constrained Optimization and META-learning to alleviate catastrophic forgetting and dependency on history training data by using a meta-model to retain the important parameters for old languages. Our experiments prove that CLLE is a challenging CLL benchmark and that our proposed method is effective when compared with other strong baselines. Due to the construction of the corpus, the task designing and the evaluation method are independent of the centric language, we also construct and release the English-centric corpus EN-25 to facilitate academic research.

### 中文抽取
定义：提出 Continual Language Learning Evaluation（CLLE）用于多语翻译持续学习评测。

## URL 汇总

| 类型 | 链接 |
|---|---|
| 论文页 | https://aclanthology.org/2022.findings-emnlp.30/ |
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

## 备注

- 主论文链接通过检索补齐：CLLE: A Benchmark for Continual Language Learning Evaluation in ...
