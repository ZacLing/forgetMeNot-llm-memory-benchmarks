# ForgetMeNot Knowledge Base (English)

<p align="center">
<a href="https://awesome.re"><img src="https://awesome.re/badge-flat.svg" alt="Awesome"></a>
</p>

[Repository Home](../../README.md) | [中文索引](../zh/README.md)

This English index mirrors the repository landing page and points to the detailed benchmark cards in the English knowledge base.

As of the current version, the repository contains **69** benchmark cards across **7** benchmark families, with parallel **English** and **Chinese** cards.

> [!NOTE]
> English is the default reading path. Use the Chinese links if you want the manually curated Chinese summaries first.

## Navigation

- [Repository Home](../../README.md)
- [Chinese Knowledge Base Index](../zh/README.md)

- [Long-Context Understanding and Reasoning](#long-context-understanding-and-reasoning)
- [Needle Retrieval and Diagnostic Probes](#needle-retrieval-and-diagnostic-probes)
- [Retrieval, Embeddings, and RAG](#retrieval-embeddings-and-rag)
- [Multi-Session Dialogue Memory and Personalization](#multi-session-dialogue-memory-and-personalization)
- [Agent Memory and Continual Learning](#agent-memory-and-continual-learning)
- [Knowledge Editing and Semantic Memory Updates](#knowledge-editing-and-semantic-memory-updates)
- [Multimodal Long-Horizon Memory and Retrieval-Reasoning](#multimodal-long-horizon-memory-and-retrieval-reasoning)

## Long-Context Understanding and Reasoning

This family focuses on retrieval, synthesis, reasoning, and generation inside very long contexts such as long documents, code repositories, long dialogue histories, and structured long inputs.

- [AcademicEval](01_long_context/academiceval.md) ([CN](../zh/01_long_context/academiceval.md)): A live long-context generation benchmark built from recent arXiv papers for title, abstract, introduction, and related-work writing tasks.
- [Ada-LEval](01_long_context/ada-leval.md) ([CN](../zh/01_long_context/ada-leval.md)): A length-adaptable benchmark with TSort and BestAnswer for controllable long-context evaluation.
- [BAMBOO](01_long_context/bamboo.md) ([CN](../zh/01_long_context/bamboo.md)): A contamination-aware long-text benchmark spanning QA, hallucination detection, ranking, language modeling, and code completion.
- [∞Bench](01_long_context/infinitebench.md) ([CN](../zh/01_long_context/infinitebench.md)): A bilingual benchmark that mixes synthetic and realistic tasks with average context length beyond 100k tokens.
- [L-CiteEval](01_long_context/l-citeeval.md) ([CN](../zh/01_long_context/l-citeeval.md)): A citation-grounded long-context benchmark that scores both answer quality and citation precision and recall.
- [L-Eval](01_long_context/l-eval.md) ([CN](../zh/01_long_context/l-eval.md)): A standardized long-context suite with 20 tasks, 508 long documents, and 2,000+ human-labeled query-response pairs.
- [LongBench-E](01_long_context/longbench-e.md) ([CN](../zh/01_long_context/longbench-e.md)): A uniform-length evaluation variant of LongBench designed to decouple true long-context ability from short-context bias.
- [LongBench Pro](01_long_context/longbench-pro.md) ([CN](../zh/01_long_context/longbench-pro.md)): A more realistic bilingual long-context benchmark with 1,500 naturally occurring long samples and a fine-grained taxonomy.
- [LongBench v2](01_long_context/longbench-v2.md) ([CN](../zh/01_long_context/longbench-v2.md)): A realistic multitask benchmark with 8k-to-2M-word contexts targeting deep understanding and reasoning.
- [LongBench](01_long_context/longbench.md) ([CN](../zh/01_long_context/longbench.md)): The first bilingual multitask long-context benchmark covering QA, summarization, few-shot learning, synthetic tasks, and code completion.
- [LongBioBench](01_long_context/longbiobench.md) ([CN](../zh/01_long_context/longbiobench.md)): A controllable long-context benchmark built from coherent biographical narratives to avoid shortcut-prone needle-style setups.
- [LooGLE v2](01_long_context/loogle-v2.md) ([CN](../zh/01_long_context/loogle-v2.md)): A real-world long-dependency benchmark targeting practical domains such as finance, law, code, and games.
- [LooGLE](01_long_context/loogle.md) ([CN](../zh/01_long_context/loogle.md)): A long-document benchmark built from recent real-world documents with both automatic and human-written QA.
- [Loong](01_long_context/loong.md) ([CN](../zh/01_long_context/loong.md)): An extended multi-document QA benchmark where every document is relevant, so missing any document hurts performance.
- [Ref-Long](01_long_context/ref-long.md) ([CN](../zh/01_long_context/ref-long.md)): A referencing-oriented long-context benchmark that asks models to identify which documents point to a target key.
- [RULER](01_long_context/ruler.md) ([CN](../zh/01_long_context/ruler.md)): A controllable long-context diagnostic suite covering retrieval, aggregation, multi-hop tracing, and QA.
- [SCROLLS](01_long_context/scrolls.md) ([CN](../zh/01_long_context/scrolls.md)): A standardized long-text benchmark spanning summarization, QA, NLI, and other long-sequence tasks.
- [ZeroSCROLLS](01_long_context/zeroscrolls.md) ([CN](../zh/01_long_context/zeroscrolls.md)): A zero-shot long-text benchmark derived from SCROLLS and additional datasets with tiny validation sets and no training split.

## Needle Retrieval and Diagnostic Probes

This family uses controllable synthetic setups to test whether a model can truly locate critical information in long contexts and to diagnose retrieval robustness, attention coverage, and multi-needle disambiguation.

- [BABILong](02_needle_and_diagnostics/babilong.md) ([CN](../zh/02_needle_and_diagnostics/babilong.md)): A reasoning-in-a-haystack benchmark that embeds bAbI-style reasoning tasks inside ultra-long documents.
- [GraphWalks](02_needle_and_diagnostics/graphwalks.md) ([CN](../zh/02_needle_and_diagnostics/graphwalks.md)): An edge-list-based graph reasoning dataset for long-context multi-hop search and traversal operations.
- [MRCR](02_needle_and_diagnostics/mrcr.md) ([CN](../zh/02_needle_and_diagnostics/mrcr.md)): A multiple-needle long-context benchmark focused on multi-round retrieval and distinguishing similar earlier requests.
- [NeedleBench](02_needle_and_diagnostics/needlebench.md) ([CN](../zh/02_needle_and_diagnostics/needlebench.md)): A synthetic bilingual benchmark that systematically varies needle depth, density, and reasoning difficulty.
- [Needle-in-a-Haystack](02_needle_and_diagnostics/niah.md) ([CN](../zh/02_needle_and_diagnostics/niah.md)): The canonical needle-in-a-haystack stress test that inserts key facts into long contexts and asks models to recover them.
- [Passkey Retrieval](02_needle_and_diagnostics/passkey-retrieval.md) ([CN](../zh/02_needle_and_diagnostics/passkey-retrieval.md)): A classic passkey recall setup, originating from Landmark Attention, for testing retrieval of a hidden random key.
- [Phonebook](02_needle_and_diagnostics/phonebook.md) ([CN](../zh/02_needle_and_diagnostics/phonebook.md)): A task family that measures long-context retrieval by querying names and phone numbers from large lookup tables.

## Retrieval, Embeddings, and RAG

This family treats external corpora, indices, and retrievers as semantic memory, spanning long-document representation learning, end-to-end RAG pipelines, and faithfulness evaluation.

- [BEIR](03_retrieval_rag/beir.md) ([CN](../zh/03_retrieval_rag/beir.md)): A heterogeneous zero-shot retrieval benchmark for evaluating generalization across 18 IR datasets.
- [GraphRAG-Bench](03_retrieval_rag/graphrag-bench.md) ([CN](../zh/03_retrieval_rag/graphrag-bench.md)): A full-pipeline GraphRAG benchmark over textbook corpora that evaluates construction, retrieval, generation, and reasoning coherence.
- [KILT](03_retrieval_rag/kilt.md) ([CN](../zh/03_retrieval_rag/kilt.md)): A knowledge-intensive benchmark that unifies multiple tasks over a shared Wikipedia snapshot and provenance evaluation.
- [LaRA](03_retrieval_rag/lara.md) ([CN](../zh/03_retrieval_rag/lara.md)): A benchmark for comparing long-context LLMs and RAG systems under the same realistic QA settings.
- [LMEB](03_retrieval_rag/lmeb.md) ([CN](../zh/03_retrieval_rag/lmeb.md)): A long-horizon memory embedding benchmark covering episodic, dialogue, semantic, and procedural retrieval.
- [LoCoV1](03_retrieval_rag/locov1.md) ([CN](../zh/03_retrieval_rag/locov1.md)): A long-document retrieval benchmark for encoders where chunking is often ineffective or impossible.
- [LongEmbed](03_retrieval_rag/longembed.md) ([CN](../zh/03_retrieval_rag/longembed.md)): A benchmark for extending embedding models from short contexts to long-context retrieval up to 32k tokens.
- [MTEB](03_retrieval_rag/mteb.md) ([CN](../zh/03_retrieval_rag/mteb.md)): A large-scale general text-embedding benchmark covering multiple tasks, datasets, and languages.
- [RAGBench](03_retrieval_rag/ragbench.md) ([CN](../zh/03_retrieval_rag/ragbench.md)): An explainable end-to-end RAG benchmark with large-scale industrial-style data and annotated failure modes.
- [RAGTruth](03_retrieval_rag/ragtruth.md) ([CN](../zh/03_retrieval_rag/ragtruth.md)): A hallucination corpus for RAG that provides case-level and word-level faithfulness annotations.
- [T2-RAGBench](03_retrieval_rag/t2-ragbench.md) ([CN](../zh/03_retrieval_rag/t2-ragbench.md)): A text-and-table RAG benchmark with 23,088 context-independent triples for retrieval plus numerical reasoning.

## Multi-Session Dialogue Memory and Personalization

This family targets episodic memory across sessions, long-running user history, and dynamic personalization, with emphasis on cross-turn tracking and user-aware responses.

- [DialSim](04_dialogue_memory/dialsim.md) ([CN](../zh/04_dialogue_memory/dialsim.md)): A dialogue simulator for long multi-party conversations, including very long contexts and unanswerable cases.
- [LoCoMo](04_dialogue_memory/locomo.md) ([CN](../zh/04_dialogue_memory/locomo.md)): A benchmark of very long-term conversational memory with event-grounded multi-session dialogues.
- [LongMemEval](04_dialogue_memory/longmemeval.md) ([CN](../zh/04_dialogue_memory/longmemeval.md)): An interactive benchmark that embeds 500 questions into expandable chat histories for long-term assistant memory.
- [Mem-Gallery](04_dialogue_memory/mem-gallery.md) ([CN](../zh/04_dialogue_memory/mem-gallery.md)): A multimodal long-term conversational memory benchmark for MLLM agents across multi-session interactions.
- [PersonaMem](04_dialogue_memory/personamem.md) ([CN](../zh/04_dialogue_memory/personamem.md)): A dynamic personalization benchmark that evaluates whether LLMs track evolving user traits and preferences over time.
- [RealMem](04_dialogue_memory/realmem.md) ([CN](../zh/04_dialogue_memory/realmem.md)): A benchmark for project-oriented real-world memory interactions with cross-session dialogues and evolving goals.
- [RealTalk](04_dialogue_memory/realtalk.md) ([CN](../zh/04_dialogue_memory/realtalk.md)): A 21-day real-world conversation dataset and benchmark for long-term open-domain dialogue memory.

## Agent Memory and Continual Learning

This family places memory inside agent tasks, environment interaction, and continual-learning settings, evaluating not only recall but also long-term decision quality, task transfer, and feedback accumulation.

- [AMA-Bench](05_agent_memory/ama-bench.md) ([CN](../zh/05_agent_memory/ama-bench.md)): A long-horizon agent-memory benchmark built from real trajectories and scalable synthetic traces.
- [CLLE](05_agent_memory/clle.md) ([CN](../zh/05_agent_memory/clle.md)): A benchmark for continual language learning in multilingual machine translation.
- [CoIN](05_agent_memory/coin.md) ([CN](../zh/05_agent_memory/coin.md)): A multimodal continual instruction-tuning benchmark that measures instruction following and retained knowledge under drift.
- [GoodAI LTM Benchmark](05_agent_memory/goodai-ltm-benchmark.md) ([CN](../zh/05_agent_memory/goodai-ltm-benchmark.md)): A dynamic conversational benchmark for long-term memory, continual learning, and information integration in agents.
- [LifelongAgentBench](05_agent_memory/lifelongagentbench.md) ([CN](../zh/05_agent_memory/lifelongagentbench.md)): A unified benchmark that evaluates LLM agents as lifelong learners across evolving tasks.
- [LOCA-bench](05_agent_memory/loca-bench.md) ([CN](../zh/05_agent_memory/loca-bench.md)): A controllable benchmark for language agents under extreme context growth in interactive environments.
- [MemBench](05_agent_memory/membench.md) ([CN](../zh/05_agent_memory/membench.md)): A comprehensive benchmark that separates factual and reflective memory in LLM-based agents.
- [MemoryAgentBench](05_agent_memory/memoryagentbench.md) ([CN](../zh/05_agent_memory/memoryagentbench.md)): A benchmark that reformats memory-agent evaluation into incremental multi-turn interactions.
- [MemoryArena](05_agent_memory/memoryarena.md) ([CN](../zh/05_agent_memory/memoryarena.md)): A benchmark for agent memory in interdependent multi-session agentic tasks.
- [MemoryBench](05_agent_memory/memorybench.md) ([CN](../zh/05_agent_memory/memorybench.md)): A benchmark for memory and continual learning in LLM systems driven by simulated user feedback.
- [MemoryCD](05_agent_memory/memorycd.md) ([CN](../zh/05_agent_memory/memorycd.md)): A user-centric cross-domain benchmark for lifelong personalization and long-context user memory in LLM agents.
- [Rubric Feedback Bench](05_agent_memory/rubric-feedback-bench.md) ([CN](../zh/05_agent_memory/rubric-feedback-bench.md)): A benchmark for turning iterative feedback into retrievable rules or memory tools.

## Knowledge Editing and Semantic Memory Updates

This family evaluates how well a model updates semantic memory after a new fact is written, including locality, generalization, ripple effects, and consistency.

- [CounterFact](06_knowledge_editing/counterfact.md) ([CN](../zh/06_knowledge_editing/counterfact.md)): A classic counterfactual dataset introduced by ROME for evaluating factual editing efficacy, specificity, and generalization.
- [MQuAKE](06_knowledge_editing/mquake.md) ([CN](../zh/06_knowledge_editing/mquake.md)): A multi-hop benchmark that tests whether factual edits propagate correctly through related reasoning chains.
- [QAEdit + WILD](06_knowledge_editing/qaeedit-wild.md) ([CN](../zh/06_knowledge_editing/qaeedit-wild.md)): A realistic editing benchmark and evaluation framework that revisits model editing in the wild.
- [ZsRE](06_knowledge_editing/zsre.md) ([CN](../zh/06_knowledge_editing/zsre.md)): A zero-shot relation extraction dataset often repurposed as a context-free QA editing benchmark.

## Multimodal Long-Horizon Memory and Retrieval-Reasoning

This family extends long-horizon memory to PDFs, image pools, and long videos, emphasizing evidence localization and integration over large multimodal contexts.

- [DocHaystack](07_multimodal/dochaystack.md) ([CN](../zh/07_multimodal/dochaystack.md)): A visual document reasoning benchmark over piles of up to 1,000 documents.
- [Ego4D Episodic Memory](07_multimodal/ego4d-episodic-memory.md) ([CN](../zh/07_multimodal/ego4d-episodic-memory.md)): The official Ego4D task for making past egocentric video queryable and temporally localizable.
- [InfoHaystack](07_multimodal/infohaystack.md) ([CN](../zh/07_multimodal/infohaystack.md)): A large-pool visual document retrieval benchmark introduced alongside DocHaystack.
- [LongVideoBench](07_multimodal/longvideobench.md) ([CN](../zh/07_multimodal/longvideobench.md)): An interleaved video-language long-context benchmark with videos up to around one hour.
- [MM-NIAH](07_multimodal/mm-niah.md) ([CN](../zh/07_multimodal/mm-niah.md)): A long multimodal document needle benchmark with retrieval, counting, and reasoning tasks.
- [MMLongBench-Doc](07_multimodal/mmlongbench-doc.md) ([CN](../zh/07_multimodal/mmlongbench-doc.md)): A multimodal long-document benchmark built on long PDFs with text, figures, and tables.
- [MMNeedle](07_multimodal/mmneedle.md) ([CN](../zh/07_multimodal/mmneedle.md)): A multi-image needle benchmark that stresses sub-image localization and negative-sample hallucination.
- [MultiHaystack](07_multimodal/multihaystack.md) ([CN](../zh/07_multimodal/multihaystack.md)): A multimodal retrieval-and-reasoning benchmark over 46k images, videos, and documents.
- [Video-MME](07_multimodal/video-mme.md) ([CN](../zh/07_multimodal/video-mme.md)): A comprehensive video MLLM benchmark spanning domains, durations, and 2,700 human-labeled QA pairs.
- [Visual Haystacks](07_multimodal/visual-haystacks.md) ([CN](../zh/07_multimodal/visual-haystacks.md)): A vision-centric needle-in-a-haystack benchmark for retrieval and reasoning over large image sets.
