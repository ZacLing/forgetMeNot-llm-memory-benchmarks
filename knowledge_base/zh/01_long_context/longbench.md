---
        name: LongBench
        slug: longbench
        language: zh
        category: 长上下文理解与推理
        subcategory: 长上下文综合任务
        memory_type: Working / In-Context
        year: "2024"
        primary_source_kind: paper
        primary_source_url: https://arxiv.org/abs/2308.14508
        counterpart_en: ../../en/01_long_context/longbench.md
        ---

        # LongBench

        [中文知识库索引](../README.md) | [English Card](../../en/01_long_context/longbench.md)

        ## 结构化信息

        | 字段 | 内容 |
        |---|---|
        | Benchmark | LongBench |
        | 分类 | 长上下文理解与推理 |
        | 子类 | 长上下文综合任务 |
        | 记忆侧重 | Working / In-Context |
        | 首次年份 | 2024 |
        | 主要来源类型 | paper |
        | 论文标题 | LongBench: A Bilingual, Multitask Benchmark for Long Context Understanding |
        | 英文卡片 | [LongBench](../../en/01_long_context/longbench.md) |

        ## 基础介绍

        年份与提出方：2023 arXiv / 2024 ACL 发表；由清华相关团队（THUDM）提出与维护。
任务：单文档 QA、多文档 QA、摘要、Few-shot、合成任务、代码补全等 6 类；覆盖中文与英文。
规模与格式：标准化 21 个数据集为统一格式；论文提供平均长度统计，并强调自动化评测。
指标：按子任务采用 EM/F1/ROUGE/准确率等；以统一脚本汇总。
优势：多任务、双语、自动化统一格式；局限：典型样本长度仍以万级为主，面对百万上下文需要更“超长”基准补充。
典型用法：比较长上下文改造方法（RoPE scaling、长序列 SFT、检索压缩等）的整体收益。
许可：官方 repo/dataset card 未在摘要层明确统一说明（需以具体发布页为准）。
实现与榜单：官方 GitHub；也有 HuggingFace dataset 镜像；常见接入 lm‑evaluation‑harness。

        ## Abstract
### 原始摘要
> Although large language models (LLMs) demonstrate impressive performance for many language tasks, most of them can only handle texts a few thousand tokens long, limiting their applications on longer sequence inputs, such as books, reports, and codebases. Recent works have proposed methods to improve LLMs' long context capabilities by extending context windows and more sophisticated memory mechanisms. However, comprehensive benchmarks tailored for evaluating long context understanding are lacking. In this paper, we introduce LongBench, the first bilingual, multi-task benchmark for long context understanding, enabling a more rigorous evaluation of long context understanding. LongBench comprises 21 datasets across 6 task categories in both English and Chinese, with an average length of 6,711 words (English) and 13,386 characters (Chinese). These tasks cover key long-text application areas including single-doc QA, multi-doc QA, summarization, few-shot learning, synthetic tasks, and code completion. All datasets in LongBench are standardized into a unified format, allowing for effortless automatic evaluation of LLMs. Upon comprehensive evaluation of 8 LLMs on LongBench, we find that: (1) Commercial model (GPT-3.5-Turbo-16k) outperforms other open-sourced models, but still struggles on longer contexts. (2) Scaled position embedding and fine-tuning on longer sequences lead to substantial improvement on long context understanding. (3) Context compression technique such as retrieval brings improvement for model with weak ability on long contexts, but the performance still lags behind models that have strong long context understanding capability. The code and datasets are available at https://github.com/THUDM/LongBench.

### 中文抽取
年份与提出方：2023 arXiv / 2024 ACL 发表；由清华相关团队（THUDM）提出与维护。
任务：单文档 QA、多文档 QA、摘要、Few-shot、合成任务、代码补全等 6 类；覆盖中文与英文。
规模与格式：标准化 21 个数据集为统一格式；论文提供平均长度统计，并强调自动化评测。
指标：按子任务采用 EM/F1/ROUGE/准确率等；以统一脚本汇总。
优势：多任务、双语、自动化统一格式；局限：典型样本长度仍以万级为主，面对百万上下文需要更“超长”基准补充。
典型用法：比较长上下文改造方法（RoPE scaling、长序列 SFT、检索压缩等）的整体收益。
许可：官方 repo/dataset card 未在摘要层明确统一说明（需以具体发布页为准）。
实现与榜单：官方 GitHub；也有 HuggingFace dataset 镜像；常见接入 lm‑evaluation‑harness。

## URL 汇总

| 类型 | 链接 |
|---|---|
| 论文页 | https://arxiv.org/abs/2308.14508 |
| 论文 PDF | https://aclanthology.org/2024.acl-long.172.pdf |
| 项目主页 | https://github.com/EleutherAI/lm-evaluation-harness/blob/main/lm_eval/tasks/longbench/README.md |
| GitHub | https://github.com/THUDM/LongBench |
| 数据集页 | https://huggingface.co/datasets/zai-org/LongBench |

## BibTeX

```bibtex
@misc{https://doi.org/10.48550/arxiv.2308.14508,
  doi = {10.48550/ARXIV.2308.14508},
  url = {https://arxiv.org/abs/2308.14508},
  author = {Bai, Yushi and Lv, Xin and Zhang, Jiajie and Lyu, Hongchang and Tang, Jiankai and Huang, Zhidian and Du, Zhengxiao and Liu, Xiao and Zeng, Aohan and Hou, Lei and Dong, Yuxiao and Tang, Jie and Li, Juanzi},
  keywords = {Computation and Language (cs.CL), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {LongBench: A Bilingual, Multitask Benchmark for Long Context Understanding},
  publisher = {arXiv},
  year = {2023},
  copyright = {arXiv.org perpetual, non-exclusive license}
}
```

## 备注

- 本卡片优先使用论文页、项目页与代码仓库等官方来源；若原报告中的链接存在错误，则以标题匹配后的官方链接为准。
