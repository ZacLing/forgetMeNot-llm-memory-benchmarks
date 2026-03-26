---
name: LongBench v2
slug: longbench-v2
category: 长上下文理解与推理
subcategory: 长上下文综合任务
memory_type: Working / In-Context
year: "2025"
primary_source_kind: paper
primary_source_url: https://arxiv.org/abs/2412.15204
---

# LongBench v2

## 结构化信息

| 字段 | 内容 |
|---|---|
| Benchmark | LongBench v2 |
| 分类 | 长上下文理解与推理 |
| 子类 | 长上下文综合任务 |
| 记忆侧重 | Working / In-Context |
| 首次年份 | 2025 |
| 主要来源类型 | paper |
| 论文标题 | LongBench v2: Towards Deeper Understanding and Reasoning on Realistic Long-context Multitasks |

## 基础介绍

目标：强调“真实多任务场景下的深度理解与推理”，长度可到 2M words；并声称即便人类专家也难以快速完成。
覆盖：官方项目页与 repo 描述其长度范围、困难度与应用覆盖。

## Abstract
### 原始摘要
> This paper introduces LongBench v2, a benchmark designed to assess the ability of LLMs to handle long-context problems requiring deep understanding and reasoning across real-world multitasks. LongBench v2 consists of 503 challenging multiple-choice questions, with contexts ranging from 8k to 2M words, across six major task categories: single-document QA, multi-document QA, long in-context learning, long-dialogue history understanding, code repository understanding, and long structured data understanding. To ensure the breadth and the practicality, we collect data from nearly 100 highly educated individuals with diverse professional backgrounds. We employ both automated and manual review processes to maintain high quality and difficulty, resulting in human experts achieving only 53.7% accuracy under a 15-minute time constraint. Our evaluation reveals that the best-performing model, when directly answers the questions, achieves only 50.1% accuracy. In contrast, the o1-preview model, which includes longer reasoning, achieves 57.7%, surpassing the human baseline by 4%. These results highlight the importance of enhanced reasoning ability and scaling inference-time compute to tackle the long-context challenges in LongBench v2. The project is available at https://longbench2.github.io.

### 中文抽取
目标：强调“真实多任务场景下的深度理解与推理”，长度可到 2M words；并声称即便人类专家也难以快速完成。
覆盖：官方项目页与 repo 描述其长度范围、困难度与应用覆盖。

## URL 汇总

| 类型 | 链接 |
|---|---|
| 论文页 | https://arxiv.org/abs/2412.15204 |
| 项目主页 | https://longbench2.github.io/ |
| GitHub | https://github.com/THUDM/LongBench |
| 数据集页 | https://huggingface.co/datasets/zai-org/LongBench-v2 |

## BibTeX

```bibtex
@misc{https://doi.org/10.48550/arxiv.2412.15204,
  doi = {10.48550/ARXIV.2412.15204},
  url = {https://arxiv.org/abs/2412.15204},
  author = {Bai, Yushi and Tu, Shangqing and Zhang, Jiajie and Peng, Hao and Wang, Xiaozhi and Lv, Xin and Cao, Shulin and Xu, Jiazheng and Hou, Lei and Dong, Yuxiao and Tang, Jie and Li, Juanzi},
  keywords = {Computation and Language (cs.CL), Artificial Intelligence (cs.AI), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {LongBench v2: Towards Deeper Understanding and Reasoning on Realistic Long-context Multitasks},
  publisher = {arXiv},
  year = {2024},
  copyright = {arXiv.org perpetual, non-exclusive license}
}
```

## 备注

- 本卡片优先使用论文页、项目页与代码仓库等官方来源；若原报告中的链接存在错误，则以标题匹配后的官方链接为准。
