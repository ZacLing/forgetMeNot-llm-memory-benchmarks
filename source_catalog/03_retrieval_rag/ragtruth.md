---
name: RAGTruth
slug: ragtruth
category: 检索、Embedding 与 RAG
subcategory: 端到端 RAG 与忠实性
memory_type: Semantic / Retrieval-Augmented
year: "2024"
primary_source_kind: paper
primary_source_url: https://arxiv.org/abs/2401.00396
---

# RAGTruth

## 结构化信息

| 字段 | 内容 |
|---|---|
| Benchmark | RAGTruth |
| 分类 | 检索、Embedding 与 RAG |
| 子类 | 端到端 RAG 与忠实性 |
| 记忆侧重 | Semantic / Retrieval-Augmented |
| 首次年份 | 2024 |
| 主要来源类型 | paper |
| 论文标题 | RAGTruth: A Hallucination Corpus for Developing Trustworthy Retrieval-Augmented Language Models |

## 基础介绍

内容：近 18,000 条在 RAG setting 下由多模型产生的响应，进行 case 与 word-level 的幻觉标注（含幻觉强度）。

## Abstract
### 原始摘要
> Retrieval-augmented generation (RAG) has become a main technique for alleviating hallucinations in large language models (LLMs). Despite the integration of RAG, LLMs may still present unsupported or contradictory claims to the retrieved contents. In order to develop effective hallucination prevention strategies under RAG, it is important to create benchmark datasets that can measure the extent of hallucination. This paper presents RAGTruth, a corpus tailored for analyzing word-level hallucinations in various domains and tasks within the standard RAG frameworks for LLM applications. RAGTruth comprises nearly 18,000 naturally generated responses from diverse LLMs using RAG. These responses have undergone meticulous manual annotations at both the individual cases and word levels, incorporating evaluations of hallucination intensity. We not only benchmark hallucination frequencies across different LLMs, but also critically assess the effectiveness of several existing hallucination detection methodologies. Furthermore, we show that using a high-quality dataset such as RAGTruth, it is possible to finetune a relatively small LLM and achieve a competitive level of performance in hallucination detection when compared to the existing prompt-based approaches using state-of-the-art large language models such as GPT-4.

### 中文抽取
内容：近 18,000 条在 RAG setting 下由多模型产生的响应，进行 case 与 word-level 的幻觉标注（含幻觉强度）。

## URL 汇总

| 类型 | 链接 |
|---|---|
| 论文页 | https://arxiv.org/abs/2401.00396 |
| GitHub | https://github.com/ParticleMedia/RAGTruth |
| paper_url_2 | https://aclanthology.org/2024.acl-long.585/ |

## BibTeX

```bibtex
@misc{https://doi.org/10.48550/arxiv.2401.00396,
  doi = {10.48550/ARXIV.2401.00396},
  url = {https://arxiv.org/abs/2401.00396},
  author = {Niu, Cheng and Wu, Yuanhao and Zhu, Juno and Xu, Siliang and Shum, Kashun and Zhong, Randy and Song, Juntong and Zhang, Tong},
  keywords = {Computation and Language (cs.CL), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {RAGTruth: A Hallucination Corpus for Developing Trustworthy Retrieval-Augmented Language Models},
  publisher = {arXiv},
  year = {2024},
  copyright = {arXiv.org perpetual, non-exclusive license}
}
```

## 备注

- 本卡片优先使用论文页、项目页与代码仓库等官方来源；若原报告中的链接存在错误，则以标题匹配后的官方链接为准。
