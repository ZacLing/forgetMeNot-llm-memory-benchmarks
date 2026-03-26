---
name: MemoryAgentBench
slug: memoryagentbench
language: en
category: Agent Memory and Continual Learning
subcategory: Agentic memory benchmark
memory_type: Agentic / Procedural / Continual
year: "2026"
primary_source_kind: paper
primary_source_url: https://arxiv.org/abs/2507.05257
counterpart_zh: ../../zh/05_agent_memory/memoryagentbench.md
---

# MemoryAgentBench

[English Knowledge Base Index](../README.md) | [中文卡片](../../zh/05_agent_memory/memoryagentbench.md)

## Structured Metadata

| Field | Content |
|---|---|
| Benchmark | MemoryAgentBench |
| Category | Agent Memory and Continual Learning |
| Subcategory | Agentic memory benchmark |
| Memory Focus | Agentic / Procedural / Continual |
| First Year | 2026 |
| Primary Source Type | paper |
| Paper Title | Evaluating Memory in LLM Agents via Incremental Multi-Turn Interactions |
| Chinese Card | [MemoryAgentBench](../../zh/05_agent_memory/memoryagentbench.md) |

## Overview

A benchmark that reformats memory-agent evaluation into incremental multi-turn interactions.

## Abstract
### Original Abstract
> Recent benchmarks for Large Language Model (LLM) agents primarily focus on evaluating reasoning, planning, and execution capabilities, while another critical component-memory, encompassing how agents memorize, update, and retrieve long-term information-is under-evaluated due to the lack of benchmarks. We term agents with memory mechanisms as memory agents. In this paper, based on classic theories from memory science and cognitive science, we identify four core competencies essential for memory agents: accurate retrieval, test-time learning, long-range understanding, and selective forgetting. Existing benchmarks either rely on limited context lengths or are tailored for static, long-context settings like book-based QA, which do not reflect the interactive, multi-turn nature of memory agents that incrementally accumulate information. Moreover, no existing benchmarks cover all four competencies. We introduce MemoryAgentBench, a new benchmark specifically designed for memory agents. Our benchmark transforms existing long-context datasets and incorporates newly constructed datasets into a multi-turn format, effectively simulating the incremental information processing characteristic of memory agents. By carefully selecting and curating datasets, our benchmark provides comprehensive coverage of the four core memory competencies outlined above, thereby offering a systematic and challenging testbed for assessing memory quality. We evaluate a diverse set of memory agents, ranging from simple context-based and retrieval-augmented generation (RAG) systems to advanced agents with external memory modules and tool integration. Empirical results reveal that current methods fall short of mastering all four competencies, underscoring the need for further research into comprehensive memory mechanisms for LLM agents.

### Curated Summary
A benchmark that reformats memory-agent evaluation into incremental multi-turn interactions.

## Links

| Type | Link |
|---|---|
| Paper | https://arxiv.org/abs/2507.05257 |
| GitHub | https://github.com/HUST-AI-HYZ/MemoryAgentBench |
| Dataset | https://huggingface.co/datasets/ai-hyz/MemoryAgentBench |

## BibTeX

```bibtex
@misc{https://doi.org/10.48550/arxiv.2507.05257,
  doi = {10.48550/ARXIV.2507.05257},
  url = {https://arxiv.org/abs/2507.05257},
  author = {Hu, Yuanzhe and Wang, Yu and McAuley, Julian},
  keywords = {Computation and Language (cs.CL), Artificial Intelligence (cs.AI), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {Evaluating Memory in LLM Agents via Incremental Multi-Turn Interactions},
  publisher = {arXiv},
  year = {2025},
  copyright = {arXiv.org perpetual, non-exclusive license}
}
```

## Remarks

- This card prioritizes official paper pages, project pages, and code repositories. When a link in the original report was incorrect, the corrected official link is used instead.
