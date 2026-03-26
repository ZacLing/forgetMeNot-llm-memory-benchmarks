---
name: Passkey Retrieval
slug: passkey-retrieval
category: 长上下文针类诊断
subcategory: Needle / Passkey / 合成诊断
memory_type: Working / In-Context
year: "2023"
primary_source_kind: paper
primary_source_url: https://arxiv.org/abs/2305.16300
---

# Passkey Retrieval

## 结构化信息

| 字段 | 内容 |
|---|---|
| Benchmark | Passkey Retrieval |
| 分类 | 长上下文针类诊断 |
| 子类 | Needle / Passkey / 合成诊断 |
| 记忆侧重 | Working / In-Context |
| 首次年份 | 2023 |
| 主要来源类型 | paper |
| 论文标题 | Landmark Attention: Random-Access Infinite Context Length for Transformers |

## 基础介绍

来源：Landmark Attention 论文提出并用于评测“长文本中找回随机 passkey 数字”；后续大量长上下文工作复用其设置。

## Abstract
### 原始摘要
> While Transformers have shown remarkable success in natural language processing, their attention mechanism's large memory requirements have limited their ability to handle longer contexts. Prior approaches, such as recurrent memory or retrieval-based augmentation, have either compromised the random-access flexibility of attention (i.e., the capability to select any token in the entire context) or relied on separate mechanisms for relevant context retrieval, which may not be compatible with the model's attention. In this paper, we present a novel approach that allows access to the complete context while retaining random-access flexibility, closely resembling running attention on the entire context. Our method uses a landmark token to represent each block of the input and trains the attention to use it for selecting relevant blocks, enabling retrieval of blocks directly through the attention mechanism instead of by relying on a separate mechanism. Our approach seamlessly integrates with specialized data structures and the system's memory hierarchy, enabling processing of arbitrarily long context lengths. We demonstrate that our method can obtain comparable performance with Transformer-XL while significantly reducing the number of retrieved tokens in each step. Finally, we show that fine-tuning LLaMA 7B with our method successfully extends its context length capacity to over 32k tokens, allowing for inference at the context lengths of GPT-4. We release the implementation of landmark attention and the code to reproduce our experiments at https://github.com/epfml/landmark-attention/.

### 中文抽取
来源：Landmark Attention 论文提出并用于评测“长文本中找回随机 passkey 数字”；后续大量长上下文工作复用其设置。

## URL 汇总

| 类型 | 链接 |
|---|---|
| 论文页 | https://arxiv.org/abs/2305.16300 |
| GitHub | https://github.com/epfml/landmark-attention/ |

## BibTeX

```bibtex
@misc{https://doi.org/10.48550/arxiv.2305.16300,
  doi = {10.48550/ARXIV.2305.16300},
  url = {https://arxiv.org/abs/2305.16300},
  author = {Mohtashami, Amirkeivan and Jaggi, Martin},
  keywords = {Computation and Language (cs.CL), Machine Learning (cs.LG), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {Landmark Attention: Random-Access Infinite Context Length for Transformers},
  publisher = {arXiv},
  year = {2023},
  copyright = {arXiv.org perpetual, non-exclusive license}
}
```

## 备注

- 本卡片优先使用论文页、项目页与代码仓库等官方来源；若原报告中的链接存在错误，则以标题匹配后的官方链接为准。
