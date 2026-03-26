# LLM Memory Benchmark Structured Source Catalog

This directory collects the structured source cards used to build the bilingual benchmark knowledge base. It augments each benchmark with abstracts, official links, BibTeX, and explicit category assignments. When earlier research materials contained mismatched links or names, the corresponding source card documents the correction explicitly.

## Classification Principles

- Long-Context Understanding and Reasoning: evaluates localization, synthesis, reasoning, and long-form generation inside single-turn long inputs.
- Needle Retrieval and Diagnostic Probes: uses controllable synthetic tasks to stress-test retrieval, needle localization, and attention coverage.
- Retrieval, Embeddings, and RAG: treats external knowledge stores and retrievers as semantic memory, focusing on retrieval quality and RAG faithfulness.
- Multi-Session Dialogue Memory and Personalization: focuses on cross-session user facts, preferences, project history, and personalized responses.
- Agent Memory and Continual Learning: focuses on long-term memory in agent-environment interaction, task transfer, and accumulated feedback.
- Knowledge Editing and Semantic Memory Updates: evaluates whether newly written facts are recalled correctly while preserving locality and consistency.
- Multimodal Long-Horizon Memory and Retrieval-Reasoning: focuses on evidence localization and reasoning across PDFs, image pools, and long videos.

## Statistics

- Benchmark cards: 73
- Top-level categories: 7

## Long-Context Understanding and Reasoning

This family focuses on localization, synthesis, reasoning, and generation over long documents, code repositories, dialogue histories, and other structured long-context inputs.

- [AcademicEval](01_long_context/academiceval.md): Comprehensive Long-Context Tasks; primary paper title: `AcademicEval: Live Long-Context LLM Benchmark`; first year: `2025`.
- [Ada-LEval](01_long_context/ada-leval.md): Diagnostic Suites and Standardized Evaluation; primary paper title: `Ada-LEval: Evaluating long-context LLMs with length-adaptable benchmarks`; first year: `2024`.
- [BAMBOO](01_long_context/bamboo.md): Comprehensive Long-Context Tasks; primary paper title: `BAMBOO: A Comprehensive Benchmark for Evaluating Long Text Modeling Capacities of Large Language Models`; first year: `2024`.
- [CLongEval](01_long_context/clongeval.md): Comprehensive Long-Context Tasks; primary paper title: `CLongEval: A Chinese Benchmark for Evaluating Long-Context Large Language Models`; first year: `2024`.
- [HELMET](01_long_context/helmet.md): Comprehensive Long-Context Tasks; primary paper title: `HELMET: How to Evaluate Long-Context Language Models Effectively and Thoroughly`; first year: `2024`.
- [L-CiteEval](01_long_context/l-citeeval.md): Citation Grounding and Faithfulness; primary paper title: `L-CiteEval: Do Long-Context Models Truly Leverage Context for Responding?`; first year: `2024`.
- [L-Eval](01_long_context/l-eval.md): Diagnostic Suites and Standardized Evaluation; primary paper title: `L-Eval: Instituting Standardized Evaluation for Long Context Language Models`; first year: `2023`.
- [LV-Eval](01_long_context/lv-eval.md): Comprehensive Long-Context Tasks; primary paper title: `LV-Eval: A Balanced Long-Context Benchmark with 5 Length Levels Up to 256K`; first year: `2024`.
- [LongBench](01_long_context/longbench.md): Comprehensive Long-Context Tasks; primary paper title: `LongBench: A Bilingual, Multitask Benchmark for Long Context Understanding`; first year: `2024`.
- [LongBench Pro](01_long_context/longbench-pro.md): Comprehensive Long-Context Tasks; primary paper title: `LongBench Pro: A More Realistic and Comprehensive Bilingual Long-Context Evaluation Benchmark`; first year: `2026`.
- [LongBench v2](01_long_context/longbench-v2.md): Comprehensive Long-Context Tasks; primary paper title: `LongBench v2: Towards Deeper Understanding and Reasoning on Realistic Long-context Multitasks`; first year: `2025`.
- [LongBench-E](01_long_context/longbench-e.md): Comprehensive Long-Context Tasks; primary paper title: `LongBench-E: Uniform-Length Variant for LongBench in lm-evaluation-harness`; first year: `2025`.
- [LongBioBench](01_long_context/longbiobench.md): Comprehensive Long-Context Tasks; primary paper title: `A Controllable Examination for Long-Context Language Models`; first year: `2025`.
- [LooGLE](01_long_context/loogle.md): Comprehensive Long-Context Tasks; primary paper title: `LooGLE: Can Long-Context Language Models Understand Long Contexts?`; first year: `2024`.
- [LooGLE v2](01_long_context/loogle-v2.md): Comprehensive Long-Context Tasks; primary paper title: `NeurIPS Poster LooGLE v2: Are LLMs Ready for Real World Long Dependency Challenges?`; first year: `2025`.
- [Loong](01_long_context/loong.md): Comprehensive Long-Context Tasks; primary paper title: `Leave No Document Behind: Benchmarking Long-Context LLMs with Extended Multi-Doc QA`; first year: `2024`.
- [Ref-Long](01_long_context/ref-long.md): Citation Grounding and Faithfulness; primary paper title: `Ref-Long: Benchmarking the Long-context Referencing Capability of Long-context Language Models`; first year: `2025`.
- [RULER](01_long_context/ruler.md): Diagnostic Suites and Standardized Evaluation; primary paper title: `RULER: What's the Real Context Size of Your Long-Context Language Models?`; first year: `2024`.
- [SCROLLS](01_long_context/scrolls.md): Comprehensive Long-Context Tasks; primary paper title: `SCROLLS: Standardized CompaRison Over Long Language Sequences`; first year: `2022`.
- [ZeroSCROLLS](01_long_context/zeroscrolls.md): Comprehensive Long-Context Tasks; primary paper title: `ZeroSCROLLS: A Zero-Shot Benchmark for Long Text Understanding`; first year: `2023`.
- [∞Bench](01_long_context/infinitebench.md): Comprehensive Long-Context Tasks; primary paper title: `$\infty$Bench: Extending Long Context Evaluation Beyond 100K Tokens`; first year: `2024`.

## Needle Retrieval and Diagnostic Probes

This family uses controllable synthetic setups to diagnose whether a model truly finds the key information inside long contexts, making it suitable for retrieval and attention stress tests.

- [BABILong](02_needle_and_diagnostics/babilong.md): Needle / Passkey / Synthetic Diagnostics; primary paper title: `BABILong: Testing the Limits of LLMs with Long Context Reasoning-in-a-Haystack`; first year: `2024`.
- [GraphWalks](02_needle_and_diagnostics/graphwalks.md): Multi-Needle / Structured Retrieval; primary paper title: `GraphWalks: Long-Context Graph Reasoning Dataset`; first year: `2025`.
- [MRCR](02_needle_and_diagnostics/mrcr.md): Multi-Needle / Structured Retrieval; primary paper title: `openai/mrcr · Datasets at Hugging Face`; first year: `not specified`.
- [Needle-in-a-Haystack](02_needle_and_diagnostics/niah.md): Needle / Passkey / Synthetic Diagnostics; primary paper title: `Needle In A Haystack - Pressure Testing LLMs`; first year: `2024`.
- [NeedleBench](02_needle_and_diagnostics/needlebench.md): Needle / Passkey / Synthetic Diagnostics; primary paper title: `NeedleBench: Evaluating LLM Retrieval and Reasoning Across Varying Information Densities`; first year: `2025`.
- [Passkey Retrieval](02_needle_and_diagnostics/passkey-retrieval.md): Needle / Passkey / Synthetic Diagnostics; primary paper title: `Landmark Attention: Random-Access Infinite Context Length for Transformers`; first year: `2023`.
- [NoLiMa](02_needle_and_diagnostics/nolima.md): Needle / Passkey / Synthetic Diagnostics; primary paper title: `NoLiMa: Long-Context Evaluation Beyond Literal Matching`; first year: `2025`.
- [Phonebook](02_needle_and_diagnostics/phonebook.md): Multi-Needle / Structured Retrieval; primary paper title: `An Empirical Study of Mamba-based Language Models`; first year: `2024`.

## Retrieval, Embeddings, and RAG

This family treats external knowledge stores, indices, and retrievers as semantic memory, focusing on retrieval quality, faithfulness, and long-document representation learning.

- [BEIR](03_retrieval_rag/beir.md): Retrieval and Representation Learning; primary paper title: `BEIR: A Heterogenous Benchmark for Zero-shot Evaluation of Information Retrieval Models`; first year: `2021`.
- [GraphRAG-Bench](03_retrieval_rag/graphrag-bench.md): End-to-End RAG and Faithfulness; primary paper title: `GraphRAG-Bench: Challenging Domain-Specific Reasoning for Evaluating Graph Retrieval-Augmented Generation`; first year: `2025`.
- [KILT](03_retrieval_rag/kilt.md): Retrieval and Representation Learning; primary paper title: `KILT: a Benchmark for Knowledge Intensive Language Tasks`; first year: `2021`.
- [LaRA](03_retrieval_rag/lara.md): End-to-End RAG and Faithfulness; primary paper title: `LaRA: Benchmarking Retrieval-Augmented Generation and Long-Context LLMs -- No Silver Bullet for LC or RAG Routing`; first year: `2025`.
- [LMEB](03_retrieval_rag/lmeb.md): Retrieval and Representation Learning; primary paper title: `LMEB: Long-horizon Memory Embedding Benchmark`; first year: `2026`.
- [LoCoV1](03_retrieval_rag/locov1.md): Retrieval and Representation Learning; primary paper title: `Benchmarking and Building Long-Context Retrieval Models with LoCo and M2-BERT`; first year: `2024`.
- [LongEmbed](03_retrieval_rag/longembed.md): Retrieval and Representation Learning; primary paper title: `LongEmbed: Extending Embedding Models for Long Context Retrieval`; first year: `2024`.
- [MTEB](03_retrieval_rag/mteb.md): Retrieval and Representation Learning; primary paper title: `MTEB: Massive Text Embedding Benchmark`; first year: `2023`.
- [RAGBench](03_retrieval_rag/ragbench.md): End-to-End RAG and Faithfulness; primary paper title: `RAGBench: Explainable Benchmark for Retrieval-Augmented Generation Systems`; first year: `2025`.
- [RAGTruth](03_retrieval_rag/ragtruth.md): End-to-End RAG and Faithfulness; primary paper title: `RAGTruth: A Hallucination Corpus for Developing Trustworthy Retrieval-Augmented Language Models`; first year: `2024`.
- [T2-RAGBench](03_retrieval_rag/t2-ragbench.md): End-to-End RAG and Faithfulness; primary paper title: `T$^2$-RAGBench: Text-and-Table Benchmark for Evaluating Retrieval-Augmented Generation`; first year: `2026`.

## Multi-Session Dialogue Memory and Personalization

This family focuses on episodic memory over cross-session dialogue, long-term user profiles, and real interaction traces.

- [DialSim](04_dialogue_memory/dialsim.md): Long-Term Dialogue Memory; primary paper title: `DialSim: A Dialogue Simulator for Evaluating Long-Term Multi-Party Dialogue Understanding of Conversational Agents`; first year: `2025`.
- [LoCoMo](04_dialogue_memory/locomo.md): Long-Term Dialogue Memory; primary paper title: `Evaluating Very Long-Term Conversational Memory of LLM Agents`; first year: `2024`.
- [LongMemEval](04_dialogue_memory/longmemeval.md): Long-Term Dialogue Memory; primary paper title: `LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory`; first year: `2025`.
- [Mem-Gallery](04_dialogue_memory/mem-gallery.md): Long-Term Dialogue Memory; primary paper title: `Mem-Gallery: Benchmarking Multimodal Long-Term Conversational Memory for MLLM Agents`; first year: `2026`.
- [PersonaMem](04_dialogue_memory/personamem.md): Personalization and Real-World Multi-Session Dialogue; primary paper title: `Know Me, Respond to Me: Benchmarking LLMs for Dynamic User Profiling and Personalized Responses at Scale`; first year: `2025`.
- [RealMem](04_dialogue_memory/realmem.md): Personalization and Real-World Multi-Session Dialogue; primary paper title: `RealMem: Benchmarking LLMs in Real-World Memory-Driven Interaction`; first year: `2026`.
- [RealTalk](04_dialogue_memory/realtalk.md): Long-Term Dialogue Memory; primary paper title: `REALTALK: A 21-Day Real-World Dataset for Long-Term Conversation`; first year: `2025`.

## Agent Memory and Continual Learning

This family places memory inside agent tasks, environment interaction, and continual learning, measuring not only recall but also long-term behavioral adaptation.

- [AMA-Bench](05_agent_memory/ama-bench.md): Agentic memory benchmark; primary paper title: `AMA-Bench: Evaluating Long-Horizon Memory for Agentic Applications`; first year: `2026`.
- [CLLE](05_agent_memory/clle.md): Continual Learning and Feedback Memory; primary paper title: `CLLE: A Benchmark for Continual Language Learning Evaluation in Multilingual Machine Translation`; first year: `2022`.
- [CoIN](05_agent_memory/coin.md): Continual Learning and Feedback Memory; primary paper title: `CoIN: A Benchmark of Continual Instruction tuNing for Multimodel Large Language Model`; first year: `2024`.
- [GoodAI LTM Benchmark](05_agent_memory/goodai-ltm-benchmark.md): Agentic memory benchmark; primary paper title: `Beyond Prompts: Dynamic Conversational Benchmarking of Large Language Models`; first year: `2024`.
- [LifelongAgentBench](05_agent_memory/lifelongagentbench.md): Agentic memory benchmark; primary paper title: `LifelongAgentBench: Evaluating LLM Agents as Lifelong Learners`; first year: `2025`.
- [LOCA-bench](05_agent_memory/loca-bench.md): Agentic memory benchmark; primary paper title: `LOCA-bench: Benchmarking Language Agents Under Controllable and Extreme Context Growth`; first year: `2026`.
- [MemBench](05_agent_memory/membench.md): Agentic memory benchmark; primary paper title: `MemBench: Towards More Comprehensive Evaluation on the Memory of LLM-based Agents`; first year: `2025`.
- [MemoryAgentBench](05_agent_memory/memoryagentbench.md): Agentic memory benchmark; primary paper title: `Evaluating Memory in LLM Agents via Incremental Multi-Turn Interactions`; first year: `2026`.
- [MemoryArena](05_agent_memory/memoryarena.md): Agentic memory benchmark; primary paper title: `MemoryArena: Benchmarking Agent Memory in Interdependent Multi-Session Agentic Tasks`; first year: `2026`.
- [MemoryBench](05_agent_memory/memorybench.md): Continual Learning and Feedback Memory; primary paper title: `MemoryBench: A Benchmark for Memory and Continual Learning in LLM Systems`; first year: `2025`.
- [MemoryCD](05_agent_memory/memorycd.md): Agentic memory benchmark; primary paper title: `MemoryCD: Benchmarking Long-Context User Memory of LLM Agents for Lifelong Cross-Domain Personalization`; first year: `2026`.
- [Rubric Feedback Bench](05_agent_memory/rubric-feedback-bench.md): Continual Learning and Feedback Memory; primary paper title: `Distilling Feedback into Memory-as-a-Tool`; first year: `2026`.

## Knowledge Editing and Semantic Memory Updates

This family evaluates whether a model or external memory can support correct recall, local updates, generalization, and consistency after new facts are written.

- [CounterFact](06_knowledge_editing/counterfact.md): Knowledge Editing Evaluation; primary paper title: `Locating and Editing Factual Associations in GPT`; first year: `2023`.
- [MQuAKE](06_knowledge_editing/mquake.md): Knowledge Editing Evaluation; primary paper title: `MQuAKE: Assessing Knowledge Editing in Language Models via Multi-Hop Questions`; first year: `2024`.
- [QAEdit + WILD](06_knowledge_editing/qaeedit-wild.md): Knowledge Editing Evaluation; primary paper title: `The Mirage of Model Editing: Revisiting Evaluation in the Wild`; first year: `2025`.
- [ZsRE](06_knowledge_editing/zsre.md): Knowledge Editing Evaluation; primary paper title: `Zero-Shot Relation Extraction via Reading Comprehension`; first year: `2017`.

## Multimodal Long-Horizon Memory and Retrieval-Reasoning

This family extends long-horizon memory to PDFs, image pools, and long videos, emphasizing large-scale cross-modal evidence localization and integration.

- [DocHaystack](07_multimodal/dochaystack.md): Long Documents and Visual Documents; primary paper title: `Document Haystacks: Vision-Language Reasoning Over Piles of 1000+ Documents`; first year: `2024`.
- [Ego4D Episodic Memory](07_multimodal/ego4d-episodic-memory.md): Long-Context Video; primary paper title: `Ego4D Episodic Memory Benchmark`; first year: `2021`.
- [InfoHaystack](07_multimodal/infohaystack.md): Long Documents and Visual Documents; primary paper title: `Document Haystacks: Vision-Language Reasoning Over Piles of 1000+ Documents`; first year: `2024`.
- [LongVideoBench](07_multimodal/longvideobench.md): Long-Context Video; primary paper title: `LongVideoBench: A Benchmark for Long-context Interleaved Video-Language Understanding`; first year: `2024`.
- [MM-NIAH](07_multimodal/mm-niah.md): Multi-Image / Multimodal Retrieval and Reasoning; primary paper title: `Needle In A Multimodal Haystack`; first year: `2024`.
- [MMLongBench-Doc](07_multimodal/mmlongbench-doc.md): Long Documents and Visual Documents; primary paper title: `MMLongBench-Doc: Benchmarking Long-context Document Understanding with Visualizations`; first year: `2024`.
- [MMNeedle](07_multimodal/mmneedle.md): Multi-Image / Multimodal Retrieval and Reasoning; primary paper title: `Multimodal Needle in a Haystack: Benchmarking Long-Context Capability of Multimodal Large Language Models`; first year: `2025`.
- [MultiHaystack](07_multimodal/multihaystack.md): Multi-Image / Multimodal Retrieval and Reasoning; primary paper title: `MultiHaystack: Benchmarking Multimodal Retrieval and Reasoning over 40K Images, Videos, and Documents`; first year: `2026`.
- [Video-MME](07_multimodal/video-mme.md): Long-Context Video; primary paper title: `Video-MME: The First-Ever Comprehensive Evaluation Benchmark of Multi-modal LLMs in Video Analysis`; first year: `2025`.
- [Visual Haystacks](07_multimodal/visual-haystacks.md): Multi-Image / Multimodal Retrieval and Reasoning; primary paper title: `Visual Haystacks: A Vision-Centric Needle-In-A-Haystack Benchmark`; first year: `2025`.
