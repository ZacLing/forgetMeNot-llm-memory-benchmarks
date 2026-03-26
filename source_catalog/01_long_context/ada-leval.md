---
name: Ada-LEval
slug: ada-leval
category: 长上下文理解与推理
subcategory: 诊断套件与标准化评测
memory_type: Working / In-Context
year: "2024"
primary_source_kind: paper
primary_source_url: https://aclanthology.org/2024.naacl-long.205/
---

# Ada-LEval

## 结构化信息

| 字段 | 内容 |
|---|---|
| Benchmark | Ada-LEval |
| 分类 | 长上下文理解与推理 |
| 子类 | 诊断套件与标准化评测 |
| 记忆侧重 | Working / In-Context |
| 首次年份 | 2024 |
| 主要来源类型 | paper |
| 论文标题 | Ada-LEval: Evaluating long-context LLMs with length-adaptable benchmarks |

## 基础介绍

任务：TSort（片段排序）与 BestAnswer（多候选选择），以“长度可调”方式评测长上下文理解。

## Abstract
### 原始摘要
> Recently, the large language model (LLM) community has shown increasing interest in enhancing LLMs’ capability to handle extremely long documents. As various long-text techniques and model architectures emerge, the precise and detailed evaluation of models’ long-text capabilities has become increasingly important. Existing long-text evaluation benchmarks, such as L-Eval and LongBench, construct long-text test sets based on open-source datasets, focusing mainly on QA and summarization tasks. These datasets include test samples of varying lengths (from 2k to 32k+) entangled together, making it challenging to assess model capabilities across different length ranges. Moreover, they do not cover the ultralong settings (100k+ tokens) that the latest LLMs claim to achieve. In this paper, we introduce Ada-LEval, a length-adaptable benchmark for evaluating the long-context understanding of LLMs. Ada-LEval includes two challenging subsets, TSort and BestAnswer, which enable a more reliable evaluation of LLMs’ long context capabilities. These benchmarks support intricate manipulation of the length of test cases, and can easily produce text samples up to 128k tokens. We evaluate 4 state-of-the-art closed-source API models and 6 open-source models with Ada-LEval. The evaluation results demonstrate the limitations of current LLMs, especially in ultra-long-context settings. Our code is available at https://github.com/open-compass/Ada-LEval.

### 中文抽取
任务：TSort（片段排序）与 BestAnswer（多候选选择），以“长度可调”方式评测长上下文理解。

## URL 汇总

| 类型 | 链接 |
|---|---|
| 论文页 | https://aclanthology.org/2024.naacl-long.205/ |
| GitHub | https://github.com/open-compass/Ada-LEval |

## BibTeX

```bibtex
@inproceedings{wang-etal-2024-ada,
    title = "{A}da-{LE}val: Evaluating long-context {LLM}s with length-adaptable benchmarks",
    author = "Wang, Chonghua  and
      Duan, Haodong  and
      Zhang, Songyang  and
      Lin, Dahua  and
      Chen, Kai",
    editor = "Duh, Kevin  and
      Gomez, Helena  and
      Bethard, Steven",
    booktitle = "Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers)",
    month = jun,
    year = "2024",
    address = "Mexico City, Mexico",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2024.naacl-long.205/",
    doi = "10.18653/v1/2024.naacl-long.205",
    pages = "3712--3724",
    abstract = "Recently, the large language model (LLM) community has shown increasing interest in enhancing LLMs' capability to handle extremely long documents. As various long-text techniques and model architectures emerge, the precise and detailed evaluation of models' long-text capabilities has become increasingly important. Existing long-text evaluation benchmarks, such as L-Eval and LongBench, construct long-text test sets based on open-source datasets, focusing mainly on QA and summarization tasks. These datasets include test samples of varying lengths (from 2k to 32k+) entangled together, making it challenging to assess model capabilities across different length ranges. Moreover, they do not cover the ultralong settings (100k+ tokens) that the latest LLMs claim to achieve. In this paper, we introduce Ada-LEval, a length-adaptable benchmark for evaluating the long-context understanding of LLMs. Ada-LEval includes two challenging subsets, TSort and BestAnswer, which enable a more reliable evaluation of LLMs' long context capabilities. These benchmarks support intricate manipulation of the length of test cases, and can easily produce text samples up to 128k tokens. We evaluate 4 state-of-the-art closed-source API models and 6 open-source models with Ada-LEval. The evaluation results demonstrate the limitations of current LLMs, especially in ultra-long-context settings. Our code is available at https://github.com/open-compass/Ada-LEval."
}
```

## 备注

- 本卡片优先使用论文页、项目页与代码仓库等官方来源；若原报告中的链接存在错误，则以标题匹配后的官方链接为准。
