---
name: MemBench
slug: membench
category: 智能体记忆与持续学习
subcategory: Agentic memory benchmark
memory_type: Agentic / Procedural / Continual
year: "2025"
primary_source_kind: paper
primary_source_url: https://arxiv.org/abs/2506.21605
---

# MemBench

## 结构化信息

| 字段 | 内容 |
|---|---|
| Benchmark | MemBench |
| 分类 | 智能体记忆与持续学习 |
| 子类 | Agentic memory benchmark |
| 记忆侧重 | Agentic / Procedural / Continual |
| 首次年份 | 2025 |
| 主要来源类型 | paper |
| 论文标题 | MemBench: Towards More Comprehensive Evaluation on the Memory of LLM-based Agents |

## 基础介绍

定义：将记忆拆成 factual memory 与 reflective memory 两层，并区分参与/观察等交互场景；强调从 effectiveness、efficiency、capacity 多方面评估 agent memory。

## Abstract
### 原始摘要
> Recent works have highlighted the significance of memory mechanisms in LLM-based agents, which enable them to store observed information and adapt to dynamic environments. However, evaluating their memory capabilities still remains challenges. Previous evaluations are commonly limited by the diversity of memory levels and interactive scenarios. They also lack comprehensive metrics to reflect the memory capabilities from multiple aspects. To address these problems, in this paper, we construct a more comprehensive dataset and benchmark to evaluate the memory capability of LLM-based agents. Our dataset incorporates factual memory and reflective memory as different levels, and proposes participation and observation as various interactive scenarios. Based on our dataset, we present a benchmark, named MemBench, to evaluate the memory capability of LLM-based agents from multiple aspects, including their effectiveness, efficiency, and capacity. To benefit the research community, we release our dataset and project at https://github.com/import-myself/Membench.

### 中文抽取
定义：将记忆拆成 factual memory 与 reflective memory 两层，并区分参与/观察等交互场景；强调从 effectiveness、efficiency、capacity 多方面评估 agent memory。

## URL 汇总

| 类型 | 链接 |
|---|---|
| 论文页 | https://arxiv.org/abs/2506.21605 |

## BibTeX

```bibtex
@misc{https://doi.org/10.48550/arxiv.2506.21605,
  doi = {10.48550/ARXIV.2506.21605},
  url = {https://arxiv.org/abs/2506.21605},
  author = {Tan, Haoran and Zhang, Zeyu and Ma, Chen and Chen, Xu and Dai, Quanyu and Dong, Zhenhua},
  keywords = {Computation and Language (cs.CL), Artificial Intelligence (cs.AI), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {MemBench: Towards More Comprehensive Evaluation on the Memory of LLM-based Agents},
  publisher = {arXiv},
  year = {2025},
  copyright = {arXiv.org perpetual, non-exclusive license}
}
```

## 备注

- 本卡片优先使用论文页、项目页与代码仓库等官方来源；若原报告中的链接存在错误，则以标题匹配后的官方链接为准。
