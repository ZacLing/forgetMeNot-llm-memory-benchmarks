---
name: NeedleBench
slug: needlebench
category: 长上下文针类诊断
subcategory: Needle / Passkey / 合成诊断
memory_type: Working / In-Context
year: "2025"
primary_source_kind: paper
primary_source_url: https://arxiv.org/abs/2407.11963
---

# NeedleBench

## 结构化信息

| 字段 | 内容 |
|---|---|
| Benchmark | NeedleBench |
| 分类 | 长上下文针类诊断 |
| 子类 | Needle / Passkey / 合成诊断 |
| 记忆侧重 | Working / In-Context |
| 首次年份 | 2025 |
| 主要来源类型 | paper |
| 论文标题 | NeedleBench: Evaluating LLM Retrieval and Reasoning Across Varying Information Densities |

## 基础介绍

动机：批评已有基准难以系统控制 needle 深度/数量/推理复杂度，提出合成框架评测双语长上下文的检索与推理。

## Abstract
### 原始摘要
> The capability of large language models to handle long-context information is crucial across various real-world applications. Existing evaluation methods often rely either on real-world long texts, making it difficult to exclude the influence of models' inherent knowledge, or introduce irrelevant filler content to artificially achieve target lengths, reducing assessment effectiveness. To address these limitations, we introduce NeedleBench, a synthetic framework for assessing retrieval and reasoning performance in bilingual long-context tasks with adaptive context lengths. NeedleBench systematically embeds key data points at varying depths to rigorously test model capabilities. Tasks are categorized into two scenarios: information-sparse, featuring minimal relevant details within extensive irrelevant text to simulate simple retrieval tasks; and information-dense (the Ancestral Trace Challenge), where relevant information is continuously distributed throughout the context to simulate complex reasoning tasks. Our experiments reveal that although recent reasoning models like Deepseek-R1 and OpenAI's o3 excel in mathematical reasoning, they struggle with continuous retrieval and reasoning in information-dense scenarios, even at shorter context lengths. We also characterize a phenomenon termed 'under-thinking', where models prematurely conclude reasoning despite available information. NeedleBench thus provides critical insights and targeted tools essential for evaluating and improving LLMs' long-context capabilities. All resources are available at OpenCompass: https://github.com/open-compass/opencompass.

### 中文抽取
动机：批评已有基准难以系统控制 needle 深度/数量/推理复杂度，提出合成框架评测双语长上下文的检索与推理。

## URL 汇总

| 类型 | 链接 |
|---|---|
| 论文页 | https://arxiv.org/abs/2407.11963 |
| paper_url_2 | https://openreview.net/forum?id=cEvmIKsRw0 |

## BibTeX

```bibtex
@misc{https://doi.org/10.48550/arxiv.2407.11963,
  doi = {10.48550/ARXIV.2407.11963},
  url = {https://arxiv.org/abs/2407.11963},
  author = {Li, Mo and Zhang, Songyang and Zhang, Taolin and Duan, Haodong and Liu, Yunxin and Chen, Kai},
  keywords = {Computation and Language (cs.CL), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {NeedleBench: Evaluating LLM Retrieval and Reasoning Across Varying Information Densities},
  publisher = {arXiv},
  year = {2024},
  copyright = {Creative Commons Attribution 4.0 International}
}
```

## 备注

- 本卡片优先使用论文页、项目页与代码仓库等官方来源；若原报告中的链接存在错误，则以标题匹配后的官方链接为准。
