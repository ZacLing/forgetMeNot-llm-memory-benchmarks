---
name: LoCoMo
slug: locomo
category: 多会话对话记忆与个性化
subcategory: 长期对话记忆
memory_type: Episodic / Multi-Session
year: "2024"
primary_source_kind: paper
primary_source_url: https://arxiv.org/abs/2402.17753
---

# LoCoMo

## 结构化信息

| 字段 | 内容 |
|---|---|
| Benchmark | LoCoMo |
| 分类 | 多会话对话记忆与个性化 |
| 子类 | 长期对话记忆 |
| 记忆侧重 | Episodic / Multi-Session |
| 首次年份 | 2024 |
| 主要来源类型 | paper |
| 论文标题 | Evaluating Very Long-Term Conversational Memory of LLM Agents |

## 基础介绍

语境：多论文与项目把 LoCoMo 作为长对话/长期记忆评测基准；其作为 “long-term memory” 场景常被方法论文引用（例如 2026 的 SimpleMem 在 LoCoMo 上报告显著提升）。

## Abstract
### 原始摘要
> Existing works on long-term open-domain dialogues focus on evaluating model responses within contexts spanning no more than five chat sessions. Despite advancements in long-context large language models (LLMs) and retrieval augmented generation (RAG) techniques, their efficacy in very long-term dialogues remains unexplored. To address this research gap, we introduce a machine-human pipeline to generate high-quality, very long-term dialogues by leveraging LLM-based agent architectures and grounding their dialogues on personas and temporal event graphs. Moreover, we equip each agent with the capability of sharing and reacting to images. The generated conversations are verified and edited by human annotators for long-range consistency and grounding to the event graphs. Using this pipeline, we collect LoCoMo, a dataset of very long-term conversations, each encompassing 300 turns and 9K tokens on avg., over up to 35 sessions. Based on LoCoMo, we present a comprehensive evaluation benchmark to measure long-term memory in models, encompassing question answering, event summarization, and multi-modal dialogue generation tasks. Our experimental results indicate that LLMs exhibit challenges in understanding lengthy conversations and comprehending long-range temporal and causal dynamics within dialogues. Employing strategies like long-context LLMs or RAG can offer improvements but these models still substantially lag behind human performance.

### 中文抽取
语境：多论文与项目把 LoCoMo 作为长对话/长期记忆评测基准；其作为 “long-term memory” 场景常被方法论文引用（例如 2026 的 SimpleMem 在 LoCoMo 上报告显著提升）。

## URL 汇总

| 类型 | 链接 |
|---|---|
| 论文页 | https://arxiv.org/abs/2402.17753 |
| 论文 PDF | https://aclanthology.org/2024.acl-long.747.pdf |
| 项目主页 | https://snap-research.github.io/locomo/ |
| GitHub | https://github.com/snap-research/LoCoMo |

## BibTeX

```bibtex
@misc{https://doi.org/10.48550/arxiv.2402.17753,
  doi = {10.48550/ARXIV.2402.17753},
  url = {https://arxiv.org/abs/2402.17753},
  author = {Maharana, Adyasha and Lee, Dong-Ho and Tulyakov, Sergey and Bansal, Mohit and Barbieri, Francesco and Fang, Yuwei},
  keywords = {Computation and Language (cs.CL), Artificial Intelligence (cs.AI), Machine Learning (cs.LG), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {Evaluating Very Long-Term Conversational Memory of LLM Agents},
  publisher = {arXiv},
  year = {2024},
  copyright = {Creative Commons Attribution Non Commercial Share Alike 4.0 International}
}
```

## 备注

- 原报告中的 arXiv 链接指向了无关论文，已按 benchmark 标题校正为 LoCoMo 官方论文。
