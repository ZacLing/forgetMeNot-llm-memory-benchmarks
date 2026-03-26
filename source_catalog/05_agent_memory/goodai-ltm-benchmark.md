---
name: GoodAI LTM Benchmark
slug: goodai-ltm-benchmark
category: 智能体记忆与持续学习
subcategory: Agentic memory benchmark
memory_type: Agentic / Procedural / Continual
year: "2024"
primary_source_kind: paper
primary_source_url: https://arxiv.org/abs/2409.20222
---

# GoodAI LTM Benchmark

## 结构化信息

| 字段 | 内容 |
|---|---|
| Benchmark | GoodAI LTM Benchmark |
| 分类 | 智能体记忆与持续学习 |
| 子类 | Agentic memory benchmark |
| 记忆侧重 | Agentic / Procedural / Continual |
| 首次年份 | 2024 |
| 主要来源类型 | paper |
| 论文标题 | Beyond Prompts: Dynamic Conversational Benchmarking of Large Language Models |

## 基础介绍

系列：官方博客与 GitHub 提供 benchmark 介绍、更新与 v3 标准化版本，强调评测“可持续与终身学习的 agent”。

## Abstract
### 原始摘要
> We introduce a dynamic benchmarking system for conversational agents that evaluates their performance through a single, simulated, and lengthy user$\leftrightarrow$agent interaction. The interaction is a conversation between the user and agent, where multiple tasks are introduced and then undertaken concurrently. We context switch regularly to interleave the tasks, which constructs a realistic testing scenario in which we assess the Long-Term Memory, Continual Learning, and Information Integration capabilities of the agents. Results from both proprietary and open-source Large-Language Models show that LLMs in general perform well on single-task interactions, but they struggle on the same tasks when they are interleaved. Notably, short-context LLMs supplemented with an LTM system perform as well as or better than those with larger contexts. Our benchmark suggests that there are other challenges for LLMs responding to more natural interactions that contemporary benchmarks have heretofore not been able to capture.

### 中文抽取
系列：官方博客与 GitHub 提供 benchmark 介绍、更新与 v3 标准化版本，强调评测“可持续与终身学习的 agent”。

## URL 汇总

| 类型 | 链接 |
|---|---|
| 论文页 | https://arxiv.org/abs/2409.20222 |
| 论文 PDF | https://papers.neurips.cc/paper_files/paper/2024/file/4aedf0cba303537fcb6cf948bb41b2df-Paper-Datasets_and_Benchmarks_Track.pdf |
| 项目主页 | https://www.goodai.com/introducing-goodai-ltm-benchmark/ |
| 版本发布页 | https://www.goodai.com/ltm-benchmark-3/ |
| GitHub | https://github.com/GoodAI/goodai-ltm-benchmark |

## BibTeX

```bibtex
@misc{https://doi.org/10.48550/arxiv.2409.20222,
  doi = {10.48550/ARXIV.2409.20222},
  url = {https://arxiv.org/abs/2409.20222},
  author = {Castillo-Bolado, David and Davidson, Joseph and Gray, Finlay and Rosa, Marek},
  keywords = {Computation and Language (cs.CL), Artificial Intelligence (cs.AI), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {Beyond Prompts: Dynamic Conversational Benchmarking of Large Language Models},
  publisher = {arXiv},
  year = {2024},
  copyright = {arXiv.org perpetual, non-exclusive license}
}
```

## 备注

- 本卡片优先使用论文页、项目页与代码仓库等官方来源；若原报告中的链接存在错误，则以标题匹配后的官方链接为准。
