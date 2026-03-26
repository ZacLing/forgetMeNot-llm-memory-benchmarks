# LLM Memory Benchmark 结构化目录

本目录汇总了用于构建双语知识库的结构化 benchmark 源卡片，并补充了论文 abstract、官方链接、BibTeX 与分类说明。若早期研究素材中的链接与 benchmark 名称不一致，本目录会在对应卡片中显式说明并给出校正后的链接。

## 分类原则

- 长上下文理解与推理：评估模型在单轮超长输入中的定位、综合、推理与长生成能力。
- 长上下文针类诊断：用可控合成任务压测 retrieval、needle 定位和注意力覆盖。
- 检索、Embedding 与 RAG：把外部知识库与 retriever 视为语义记忆，评估检索质量与 RAG 忠实性。
- 多会话对话记忆与个性化：关注跨会话用户事实、偏好、项目历史与个性化响应。
- 智能体记忆与持续学习：关注 agent 在环境交互、任务迁移和反馈累积中的长期记忆能力。
- 知识编辑与语义记忆更新：关注“写入新事实后是否能正确回忆并保持局部一致性”。
- 多模态长程记忆与检索推理：关注 PDF、图像池与长视频中的跨模态长程证据定位与推理。

## 总量统计

- Benchmark 卡片数：69
- 主类别数：7

## 长上下文理解与推理

这组 benchmark 关注模型在超长文本、代码仓库、长对话历史或结构化长输入中的定位、综合、推理与生成能力，强调“给定长上下文内的工作记忆”。

- [AcademicEval](01_long_context/academiceval.md)：长上下文综合任务；主要论文题目为 `AcademicEval: Live Long-Context LLM Benchmark`；首次年份 `2025`。
- [Ada-LEval](01_long_context/ada-leval.md)：诊断套件与标准化评测；主要论文题目为 `Ada-LEval: Evaluating long-context LLMs with length-adaptable benchmarks`；首次年份 `2024`。
- [BAMBOO](01_long_context/bamboo.md)：长上下文综合任务；主要论文题目为 `BAMBOO: A Comprehensive Benchmark for Evaluating Long Text Modeling Capacities of Large Language Models`；首次年份 `2024`。
- [L-CiteEval](01_long_context/l-citeeval.md)：引用定位与忠实性；主要论文题目为 `L-CiteEval: Do Long-Context Models Truly Leverage Context for Responding?`；首次年份 `2024`。
- [L-Eval](01_long_context/l-eval.md)：诊断套件与标准化评测；主要论文题目为 `L-Eval: Instituting Standardized Evaluation for Long Context Language Models`；首次年份 `2023`。
- [LongBench](01_long_context/longbench.md)：长上下文综合任务；主要论文题目为 `LongBench: A Bilingual, Multitask Benchmark for Long Context Understanding`；首次年份 `2024`。
- [LongBench Pro](01_long_context/longbench-pro.md)：长上下文综合任务；主要论文题目为 `LongBench Pro: A More Realistic and Comprehensive Bilingual Long-Context Evaluation Benchmark`；首次年份 `2026`。
- [LongBench v2](01_long_context/longbench-v2.md)：长上下文综合任务；主要论文题目为 `LongBench v2: Towards Deeper Understanding and Reasoning on Realistic Long-context Multitasks`；首次年份 `2025`。
- [LongBench-E](01_long_context/longbench-e.md)：长上下文综合任务；主要论文题目为 `LongBench-E: Uniform-Length Variant for LongBench in lm-evaluation-harness`；首次年份 `2025`。
- [LongBioBench](01_long_context/longbiobench.md)：长上下文综合任务；主要论文题目为 `A Controllable Examination for Long-Context Language Models`；首次年份 `2025`。
- [LooGLE](01_long_context/loogle.md)：长上下文综合任务；主要论文题目为 `LooGLE: Can Long-Context Language Models Understand Long Contexts?`；首次年份 `2024`。
- [LooGLE v2](01_long_context/loogle-v2.md)：长上下文综合任务；主要论文题目为 `NeurIPS Poster LooGLE v2: Are LLMs Ready for Real World Long Dependency Challenges?`；首次年份 `2025`。
- [Loong](01_long_context/loong.md)：长上下文综合任务；主要论文题目为 `Leave No Document Behind: Benchmarking Long-Context LLMs with Extended Multi-Doc QA`；首次年份 `2024`。
- [Ref-Long](01_long_context/ref-long.md)：引用定位与忠实性；主要论文题目为 `Ref-Long: Benchmarking the Long-context Referencing Capability of Long-context Language Models`；首次年份 `2025`。
- [RULER](01_long_context/ruler.md)：诊断套件与标准化评测；主要论文题目为 `RULER: What's the Real Context Size of Your Long-Context Language Models?`；首次年份 `2024`。
- [SCROLLS](01_long_context/scrolls.md)：长上下文综合任务；主要论文题目为 `SCROLLS: Standardized CompaRison Over Long Language Sequences`；首次年份 `2022`。
- [ZeroSCROLLS](01_long_context/zeroscrolls.md)：长上下文综合任务；主要论文题目为 `ZeroSCROLLS: A Zero-Shot Benchmark for Long Text Understanding`；首次年份 `2023`。
- [∞Bench](01_long_context/infinitebench.md)：长上下文综合任务；主要论文题目为 `$\infty$Bench: Extending Long Context Evaluation Beyond 100K Tokens`；首次年份 `2024`。

## 长上下文针类诊断

这组 benchmark 倾向于用可控合成任务诊断“是否真的找到了长上下文中的关键信息”，适合做最低层的长上下文检索与注意力压力测试。

- [BABILong](02_needle_and_diagnostics/babilong.md)：Needle / Passkey / 合成诊断；主要论文题目为 `BABILong: Testing the Limits of LLMs with Long Context Reasoning-in-a-Haystack`；首次年份 `2024`。
- [GraphWalks](02_needle_and_diagnostics/graphwalks.md)：多针 / 结构化检索；主要论文题目为 `GraphWalks: Long-Context Graph Reasoning Dataset`；首次年份 `2025`。
- [MRCR](02_needle_and_diagnostics/mrcr.md)：多针 / 结构化检索；主要论文题目为 `openai/mrcr · Datasets at Hugging Face`；首次年份 `未注明`。
- [Needle-in-a-Haystack](02_needle_and_diagnostics/niah.md)：Needle / Passkey / 合成诊断；主要论文题目为 `Needle In A Haystack - Pressure Testing LLMs`；首次年份 `2024`。
- [NeedleBench](02_needle_and_diagnostics/needlebench.md)：Needle / Passkey / 合成诊断；主要论文题目为 `NeedleBench: Evaluating LLM Retrieval and Reasoning Across Varying Information Densities`；首次年份 `2025`。
- [Passkey Retrieval](02_needle_and_diagnostics/passkey-retrieval.md)：Needle / Passkey / 合成诊断；主要论文题目为 `Landmark Attention: Random-Access Infinite Context Length for Transformers`；首次年份 `2023`。
- [Phonebook](02_needle_and_diagnostics/phonebook.md)：多针 / 结构化检索；主要论文题目为 `An Empirical Study of Mamba-based Language Models`；首次年份 `2024`。

## 检索、Embedding 与 RAG

这组 benchmark 将外部知识库、索引或 retriever 视为可写可读的语义记忆，重点评价检索质量、生成忠实性以及长文档表示学习能力。

- [BEIR](03_retrieval_rag/beir.md)：检索与表示学习；主要论文题目为 `BEIR: A Heterogenous Benchmark for Zero-shot Evaluation of Information Retrieval Models`；首次年份 `2021`。
- [GraphRAG-Bench](03_retrieval_rag/graphrag-bench.md)：端到端 RAG 与忠实性；主要论文题目为 `GraphRAG-Bench: Challenging Domain-Specific Reasoning for Evaluating Graph Retrieval-Augmented Generation`；首次年份 `2025`。
- [KILT](03_retrieval_rag/kilt.md)：检索与表示学习；主要论文题目为 `KILT: a Benchmark for Knowledge Intensive Language Tasks`；首次年份 `2021`。
- [LaRA](03_retrieval_rag/lara.md)：端到端 RAG 与忠实性；主要论文题目为 `LaRA: Benchmarking Retrieval-Augmented Generation and Long-Context LLMs -- No Silver Bullet for LC or RAG Routing`；首次年份 `2025`。
- [LMEB](03_retrieval_rag/lmeb.md)：检索与表示学习；主要论文题目为 `LMEB: Long-horizon Memory Embedding Benchmark`；首次年份 `2026`。
- [LoCoV1](03_retrieval_rag/locov1.md)：检索与表示学习；主要论文题目为 `Benchmarking and Building Long-Context Retrieval Models with LoCo and M2-BERT`；首次年份 `2024`。
- [LongEmbed](03_retrieval_rag/longembed.md)：检索与表示学习；主要论文题目为 `LongEmbed: Extending Embedding Models for Long Context Retrieval`；首次年份 `2024`。
- [MTEB](03_retrieval_rag/mteb.md)：检索与表示学习；主要论文题目为 `MTEB: Massive Text Embedding Benchmark`；首次年份 `2023`。
- [RAGBench](03_retrieval_rag/ragbench.md)：端到端 RAG 与忠实性；主要论文题目为 `RAGBench: Explainable Benchmark for Retrieval-Augmented Generation Systems`；首次年份 `2025`。
- [RAGTruth](03_retrieval_rag/ragtruth.md)：端到端 RAG 与忠实性；主要论文题目为 `RAGTruth: A Hallucination Corpus for Developing Trustworthy Retrieval-Augmented Language Models`；首次年份 `2024`。
- [T2-RAGBench](03_retrieval_rag/t2-ragbench.md)：端到端 RAG 与忠实性；主要论文题目为 `T$^2$-RAGBench: Text-and-Table Benchmark for Evaluating Retrieval-Augmented Generation`；首次年份 `2026`。

## 多会话对话记忆与个性化

这组 benchmark 关注跨会话对话、长期用户画像和真实交互轨迹中的情景记忆，核心问题是“模型能否在时间维度上保留并正确调用过往信息”。

- [DialSim](04_dialogue_memory/dialsim.md)：长期对话记忆；主要论文题目为 `DialSim: A Dialogue Simulator for Evaluating Long-Term Multi-Party Dialogue Understanding of Conversational Agents`；首次年份 `2025`。
- [LoCoMo](04_dialogue_memory/locomo.md)：长期对话记忆；主要论文题目为 `Evaluating Very Long-Term Conversational Memory of LLM Agents`；首次年份 `2024`。
- [LongMemEval](04_dialogue_memory/longmemeval.md)：长期对话记忆；主要论文题目为 `LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory`；首次年份 `2025`。
- [Mem-Gallery](04_dialogue_memory/mem-gallery.md)：长期对话记忆；主要论文题目为 `Mem-Gallery: Benchmarking Multimodal Long-Term Conversational Memory for MLLM Agents`；首次年份 `2026`。
- [PersonaMem](04_dialogue_memory/personamem.md)：个性化与真实多会话；主要论文题目为 `Know Me, Respond to Me: Benchmarking LLMs for Dynamic User Profiling and Personalized Responses at Scale`；首次年份 `2025`。
- [RealMem](04_dialogue_memory/realmem.md)：个性化与真实多会话；主要论文题目为 `RealMem: Benchmarking LLMs in Real-World Memory-Driven Interaction`；首次年份 `2026`。
- [RealTalk](04_dialogue_memory/realtalk.md)：长期对话记忆；主要论文题目为 `REALTALK: A 21-Day Real-World Dataset for Long-Term Conversation`；首次年份 `2025`。

## 智能体记忆与持续学习

这组 benchmark 将 memory 放到 agent 任务、环境交互和持续学习场景里考察，不只看检索命中，还看行动成功率、效率与长期行为适配。

- [AMA-Bench](05_agent_memory/ama-bench.md)：Agentic memory benchmark；主要论文题目为 `AMA-Bench: Evaluating Long-Horizon Memory for Agentic Applications`；首次年份 `2026`。
- [CLLE](05_agent_memory/clle.md)：持续学习与反馈记忆；主要论文题目为 `CLLE: A Benchmark for Continual Language Learning Evaluation in Multilingual Machine Translation`；首次年份 `2022`。
- [CoIN](05_agent_memory/coin.md)：持续学习与反馈记忆；主要论文题目为 `CoIN: A Benchmark of Continual Instruction tuNing for Multimodel Large Language Model`；首次年份 `2024`。
- [GoodAI LTM Benchmark](05_agent_memory/goodai-ltm-benchmark.md)：Agentic memory benchmark；主要论文题目为 `Beyond Prompts: Dynamic Conversational Benchmarking of Large Language Models`；首次年份 `2024`。
- [LifelongAgentBench](05_agent_memory/lifelongagentbench.md)：Agentic memory benchmark；主要论文题目为 `LifelongAgentBench: Evaluating LLM Agents as Lifelong Learners`；首次年份 `2025`。
- [LOCA-bench](05_agent_memory/loca-bench.md)：Agentic memory benchmark；主要论文题目为 `LOCA-bench: Benchmarking Language Agents Under Controllable and Extreme Context Growth`；首次年份 `2026`。
- [MemBench](05_agent_memory/membench.md)：Agentic memory benchmark；主要论文题目为 `MemBench: Towards More Comprehensive Evaluation on the Memory of LLM-based Agents`；首次年份 `2025`。
- [MemoryAgentBench](05_agent_memory/memoryagentbench.md)：Agentic memory benchmark；主要论文题目为 `Evaluating Memory in LLM Agents via Incremental Multi-Turn Interactions`；首次年份 `2026`。
- [MemoryArena](05_agent_memory/memoryarena.md)：Agentic memory benchmark；主要论文题目为 `MemoryArena: Benchmarking Agent Memory in Interdependent Multi-Session Agentic Tasks`；首次年份 `2026`。
- [MemoryBench](05_agent_memory/memorybench.md)：持续学习与反馈记忆；主要论文题目为 `MemoryBench: A Benchmark for Memory and Continual Learning in LLM Systems`；首次年份 `2025`。
- [MemoryCD](05_agent_memory/memorycd.md)：Agentic memory benchmark；主要论文题目为 `MemoryCD: Benchmarking Long-Context User Memory of LLM Agents for Lifelong Cross-Domain Personalization`；首次年份 `2026`。
- [Rubric Feedback Bench](05_agent_memory/rubric-feedback-bench.md)：持续学习与反馈记忆；主要论文题目为 `Distilling Feedback into Memory-as-a-Tool`；首次年份 `2026`。

## 知识编辑与语义记忆更新

这组 benchmark 用于测试模型或外部记忆在写入新事实之后，是否能实现正确回忆、局部更新、泛化传播与一致性保持。

- [CounterFact](06_knowledge_editing/counterfact.md)：知识编辑评测；主要论文题目为 `Locating and Editing Factual Associations in GPT`；首次年份 `2023`。
- [MQuAKE](06_knowledge_editing/mquake.md)：知识编辑评测；主要论文题目为 `MQuAKE: Assessing Knowledge Editing in Language Models via Multi-Hop Questions`；首次年份 `2024`。
- [QAEdit + WILD](06_knowledge_editing/qaeedit-wild.md)：知识编辑评测；主要论文题目为 `The Mirage of Model Editing: Revisiting Evaluation in the Wild`；首次年份 `2025`。
- [ZsRE](06_knowledge_editing/zsre.md)：知识编辑评测；主要论文题目为 `Zero-Shot Relation Extraction via Reading Comprehension`；首次年份 `2017`。

## 多模态长程记忆与检索推理

这组 benchmark 将长程记忆问题扩展到 PDF、图像池和长视频，重点挑战通常不在单步推理，而在大规模跨模态证据池中的定位与整合。

- [DocHaystack](07_multimodal/dochaystack.md)：长文档与视觉文档；主要论文题目为 `Document Haystacks: Vision-Language Reasoning Over Piles of 1000+ Documents`；首次年份 `2024`。
- [Ego4D Episodic Memory](07_multimodal/ego4d-episodic-memory.md)：视频长上下文；主要论文题目为 `Ego4D Episodic Memory Benchmark`；首次年份 `2021`。
- [InfoHaystack](07_multimodal/infohaystack.md)：长文档与视觉文档；主要论文题目为 `Document Haystacks: Vision-Language Reasoning Over Piles of 1000+ Documents`；首次年份 `2024`。
- [LongVideoBench](07_multimodal/longvideobench.md)：视频长上下文；主要论文题目为 `LongVideoBench: A Benchmark for Long-context Interleaved Video-Language Understanding`；首次年份 `2024`。
- [MM-NIAH](07_multimodal/mm-niah.md)：多图 / 多模态检索推理；主要论文题目为 `Needle In A Multimodal Haystack`；首次年份 `2024`。
- [MMLongBench-Doc](07_multimodal/mmlongbench-doc.md)：长文档与视觉文档；主要论文题目为 `MMLongBench-Doc: Benchmarking Long-context Document Understanding with Visualizations`；首次年份 `2024`。
- [MMNeedle](07_multimodal/mmneedle.md)：多图 / 多模态检索推理；主要论文题目为 `Multimodal Needle in a Haystack: Benchmarking Long-Context Capability of Multimodal Large Language Models`；首次年份 `2025`。
- [MultiHaystack](07_multimodal/multihaystack.md)：多图 / 多模态检索推理；主要论文题目为 `MultiHaystack: Benchmarking Multimodal Retrieval and Reasoning over 40K Images, Videos, and Documents`；首次年份 `2026`。
- [Video-MME](07_multimodal/video-mme.md)：视频长上下文；主要论文题目为 `Video-MME: The First-Ever Comprehensive Evaluation Benchmark of Multi-modal LLMs in Video Analysis`；首次年份 `2025`。
- [Visual Haystacks](07_multimodal/visual-haystacks.md)：多图 / 多模态检索推理；主要论文题目为 `Visual Haystacks: A Vision-Centric Needle-In-A-Haystack Benchmark`；首次年份 `2025`。
