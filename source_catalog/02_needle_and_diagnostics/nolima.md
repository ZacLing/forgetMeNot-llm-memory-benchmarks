---
name: NoLiMa
slug: nolima
category: 长上下文针类诊断
subcategory: Needle / Passkey / 合成诊断
memory_type: Working / In-Context
year: "2025"
primary_source_kind: paper
primary_source_url: https://arxiv.org/abs/2502.05167
---

# NoLiMa

## 结构化信息

| 字段 | 内容 |
|---|---|
| Benchmark | NoLiMa |
| 分类 | 长上下文针类诊断 |
| 子类 | Needle / Passkey / 合成诊断 |
| 记忆侧重 | Working / In-Context |
| 首次年份 | 2025 |
| 主要来源类型 | paper |
| 论文标题 | NoLiMa: Long-Context Evaluation Beyond Literal Matching |

## 基础介绍

动机：传统 NIAH 风格 benchmark 往往允许模型利用 question 与 needle 之间的字面重叠做“近似字符串匹配”，从而高估真实的长上下文检索能力。
设计：NoLiMa 刻意最小化 question 与 needle 的 lexical overlap，迫使模型通过 latent associations 而非字面匹配来定位关键信息。
用途：它适合与标准 NIAH 搭配使用，用来区分“能做 literal retrieval”与“能在长上下文中完成更抽象的语义定位”这两类能力。
结论：论文显示许多在短上下文表现很强、甚至在标准 NIAH 上接近满分的模型，在 NoLiMa 的长上下文设置下会明显退化。

## Abstract
### 原始摘要
> Recent large language models (LLMs) support long contexts ranging from 128K to 1M tokens. A popular method for evaluating these capabilities is the needle-in-a-haystack (NIAH) test, which involves retrieving a "needle" (relevant information) from a "haystack" (long irrelevant context). Extensions of this approach include increasing distractors, fact chaining, and in-context reasoning. However, in these benchmarks, models can exploit existing literal matches between the needle and haystack to simplify the task. To address this, we introduce NoLiMa, a benchmark extending NIAH with a carefully designed needle set, where questions and needles have minimal lexical overlap, requiring models to infer latent associations to locate the needle within the haystack. We evaluate 13 popular LLMs that claim to support contexts of at least 128K tokens. While they perform well in short contexts (<1K), performance degrades significantly as context length increases. At 32K, for instance, 11 models drop below 50% of their strong short-length baselines. Even GPT-4o, one of the top-performing exceptions, experiences a reduction from an almost-perfect baseline of 99.3% to 69.7%. Our analysis suggests these declines stem from the increased difficulty the attention mechanism faces in longer contexts when literal matches are absent, making it harder to retrieve relevant information. Even models enhanced with reasoning capabilities or CoT prompting struggle to maintain performance in long contexts. We publicly release the dataset and evaluation code at https://github.com/adobe-research/NoLiMa.

### 中文抽取
NoLiMa 可以看作一种“去字面匹配捷径”的 NIAH 扩展。它更严厉地测试模型是否真的具备长上下文语义定位能力，而不仅仅是依靠表面词重合完成检索。

## URL 汇总

| 类型 | 链接 |
|---|---|
| 论文页 | https://arxiv.org/abs/2502.05167 |
| GitHub | https://github.com/adobe-research/NoLiMa |
| 项目主页 | https://research.adobe.com/publication/nolima-long-context-evaluation-beyond-literal-matching/ |

## BibTeX

```bibtex
@misc{modarressi2025nolima,
  title = {NoLiMa: Long-Context Evaluation Beyond Literal Matching},
  author = {Modarressi, Ali and Deilamsalehy, Hanieh and Dernoncourt, Franck and Bui, Trung and Rossi, Ryan A. and Yoon, Seunghyun and Sch{\"u}tze, Hinrich},
  year = {2025},
  eprint = {2502.05167},
  archivePrefix = {arXiv},
  primaryClass = {cs.CL},
  url = {https://arxiv.org/abs/2502.05167},
  note = {Accepted at ICML 2025}
}
```

## 备注

- 本卡片将 NoLiMa 归入“长上下文针类诊断”，因为它仍然继承自 NIAH 范式，但核心贡献在于消除 literal matching shortcut。
