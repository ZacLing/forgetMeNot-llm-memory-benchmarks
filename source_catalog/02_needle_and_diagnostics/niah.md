---
name: Needle-in-a-Haystack
slug: niah
category: 长上下文针类诊断
subcategory: Needle / Passkey / 合成诊断
memory_type: Working / In-Context
year: "2024"
primary_source_kind: repo-only
primary_source_url: https://github.com/gkamradt/LLMTest_NeedleInAHaystack
---

# Needle-in-a-Haystack

## 结构化信息

| 字段 | 内容 |
|---|---|
| Benchmark | Needle-in-a-Haystack |
| 分类 | 长上下文针类诊断 |
| 子类 | Needle / Passkey / 合成诊断 |
| 记忆侧重 | Working / In-Context |
| 首次年份 | 2024 |
| 主要来源类型 | repo-only |
| 论文标题 | Needle In A Haystack - Pressure Testing LLMs |

## 基础介绍

定义：把关键事实随机插入长文本中，询问模型是否能找回；常用于压测“注意力是否能覆盖长上下文”。

## Abstract
### 原始摘要
> Doing simple retrieval from LLM models at various context lengths to measure accuracy - gkamradt/LLMTest_NeedleInAHaystack

### 中文抽取
定义：把关键事实随机插入长文本中，询问模型是否能找回；常用于压测“注意力是否能覆盖长上下文”。

## URL 汇总

| 类型 | 链接 |
|---|---|
| 项目主页 | https://github.com/open-compass/opencompass/blob/main/docs/en/advanced_guides/needleinahaystack_eval.md |
| GitHub | https://github.com/gkamradt/LLMTest_NeedleInAHaystack |

## BibTeX

```bibtex
@misc{kamradt2024needlehaystack,
  title = {Needle In A Haystack - Pressure Testing LLMs},
  author = {Greg Kamradt},
  howpublished = {GitHub repository},
  year = {2024},
  url = {https://github.com/gkamradt/LLMTest_NeedleInAHaystack},
  note = {Reference implementation widely used for long-context needle-in-a-haystack evaluation.}
}
```

## 备注

- NIAH 在当前文献里更多是一套测试方法与实现范式，而非单一正式论文 benchmark；因此这里采用官方 GitHub 实现作为主引用。
