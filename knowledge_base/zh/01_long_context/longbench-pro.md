---
        name: LongBench Pro
        slug: longbench-pro
        language: zh
        category: 长上下文理解与推理
        subcategory: 长上下文综合任务
        memory_type: Working / In-Context
        year: "2026"
        primary_source_kind: paper
        primary_source_url: https://arxiv.org/abs/2601.02872
        counterpart_en: ../../en/01_long_context/longbench-pro.md
        ---

        # LongBench Pro

        [中文知识库索引](../README.md) | [English Card](../../en/01_long_context/longbench-pro.md)

        ## 结构化信息

        | 字段 | 内容 |
        |---|---|
        | Benchmark | LongBench Pro |
        | 分类 | 长上下文理解与推理 |
        | 子类 | 长上下文综合任务 |
        | 记忆侧重 | Working / In-Context |
        | 首次年份 | 2026 |
        | 主要来源类型 | paper |
        | 论文标题 | LongBench Pro: A More Realistic and Comprehensive Bilingual Long-Context Evaluation Benchmark |
        | 英文卡片 | [LongBench Pro](../../en/01_long_context/longbench-pro.md) |

        ## 基础介绍

        年份与规模：2026；1,500 条“自然出现”的长样本，中英双语；8k–256k tokens；11 主任务 25 子任务，并提出多维 taxonomy（依赖范围/长度/难度）。
构造：提出 human‑model 协作构造管线以降低专家标注成本，同时保持可核验性。
用途：适合做更接近真实“长上下文理解”回归测试与细粒度诊断（跨语对齐、有效上下文长度与 claimed length 的差距等）。

        ## Abstract
### 原始摘要
> The rapid expansion of context length in large language models (LLMs) has outpaced existing evaluation benchmarks. Current long-context benchmarks often trade off scalability and realism: synthetic tasks underrepresent real-world complexity, while fully manual annotation is costly to scale to extreme lengths and diverse scenarios. We present LongBench Pro, a more realistic and comprehensive bilingual benchmark of 1,500 naturally occurring long-context samples in English and Chinese spanning 11 primary tasks and 25 secondary tasks, with input lengths from 8k to 256k tokens. LongBench Pro supports fine-grained analysis with task-specific metrics and a multi-dimensional taxonomy of context requirement (full vs. partial dependency), length (six levels), and difficulty (four levels calibrated by model performance). To balance quality with scalability, we propose a Human-Model Collaborative Construction pipeline: frontier LLMs draft challenging questions and reference answers, along with design rationales and solution processes, to reduce the cost of expert verification. Experts then rigorously validate correctness and refine problematic cases. Evaluating 46 widely used long-context LLMs on LongBench Pro yields three findings: (1) long-context optimization contributes more to long-context comprehension than parameter scaling; (2) effective context length is typically shorter than the claimed context length, with pronounced cross-lingual misalignment; and (3) the "thinking" paradigm helps primarily models trained with native reasoning, while mixed-thinking designs offer a promising Pareto trade-off. In summary, LongBench Pro provides a robust testbed for advancing long-context understanding.

### 中文抽取
年份与规模：2026；1,500 条“自然出现”的长样本，中英双语；8k–256k tokens；11 主任务 25 子任务，并提出多维 taxonomy（依赖范围/长度/难度）。
构造：提出 human‑model 协作构造管线以降低专家标注成本，同时保持可核验性。
用途：适合做更接近真实“长上下文理解”回归测试与细粒度诊断（跨语对齐、有效上下文长度与 claimed length 的差距等）。

## URL 汇总

| 类型 | 链接 |
|---|---|
| 论文页 | https://arxiv.org/abs/2601.02872 |
| 数据集页 | https://huggingface.co/datasets/caskcsg/LongBench-Pro |

## BibTeX

```bibtex
@misc{https://doi.org/10.48550/arxiv.2601.02872,
  doi = {10.48550/ARXIV.2601.02872},
  url = {https://arxiv.org/abs/2601.02872},
  author = {Chen, Ziyang and Wu, Xing and Jia, Junlong and Gao, Chaochen and Fu, Qi and Zhang, Debing and Hu, Songlin},
  keywords = {Computation and Language (cs.CL), Artificial Intelligence (cs.AI), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {LongBench Pro: A More Realistic and Comprehensive Bilingual Long-Context Evaluation Benchmark},
  publisher = {arXiv},
  year = {2026},
  copyright = {arXiv.org perpetual, non-exclusive license}
}
```

## 备注

- 本卡片优先使用论文页、项目页与代码仓库等官方来源；若原报告中的链接存在错误，则以标题匹配后的官方链接为准。
