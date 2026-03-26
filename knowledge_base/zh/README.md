# ForgetMeNot 中文知识库

[仓库首页](../../README_zh.md) | [English Index](../en/README.md)

这个中文索引与仓库首页对应，提供所有 benchmark 中文卡片的统一入口。

当前版本共收录 **73** 份 benchmark 卡片，覆盖 **7** 个大类，并提供中英文双语卡片。

> [!NOTE]
> 如果你想看仓库级的英文展示页，请回到 `../../README.md`。

## 导航

- [仓库首页](../../README_zh.md)
- [English Knowledge Base Index](../en/README.md)

- [长上下文理解与推理](#长上下文理解与推理)
- [长上下文针类诊断](#长上下文针类诊断)
- [检索、Embedding 与 RAG](#检索、Embedding 与 RAG)
- [多会话对话记忆与个性化](#多会话对话记忆与个性化)
- [智能体记忆与持续学习](#智能体记忆与持续学习)
- [知识编辑与语义记忆更新](#知识编辑与语义记忆更新)
- [多模态长程记忆与检索推理](#多模态长程记忆与检索推理)

## 长上下文理解与推理

这一类 benchmark 聚焦模型在超长文本、代码仓库、长对话历史和结构化长输入中的定位、综合、推理与生成能力，是“给定上下文内工作记忆”的核心评测集合。

- [AcademicEval](01_long_context/academiceval.md) ([EN](../en/01_long_context/academiceval.md))：设计：以 arXiv 论文构造学术写作任务（Title/Abstract/Introduction/Related Work），强调 live evaluation 与减少标签泄漏。
- [Ada-LEval](01_long_context/ada-leval.md) ([EN](../en/01_long_context/ada-leval.md))：任务：TSort（片段排序）与 BestAnswer（多候选选择），以“长度可调”方式评测长上下文理解。
- [BAMBOO](01_long_context/bamboo.md) ([EN](../en/01_long_context/bamboo.md))：组成：10 数据集、5 任务（QA、幻觉检测、文本排序、语言建模、代码补全），强调抗污染与更准确自动评测。
- [CLongEval](01_long_context/clongeval.md) ([EN](../en/01_long_context/clongeval.md))：定位：面向中文 long-context LLM 的综合评测集，包含 7 类任务、7,267 个样本，并覆盖 1K 到 100K 的窗口长度。
- [HELMET](01_long_context/helmet.md) ([EN](../en/01_long_context/helmet.md))：定位：一个覆盖 7 个应用导向类别的综合型长上下文 benchmark，强调可控长度、更稳定指标与更可靠的整体排序。
- [∞Bench](01_long_context/infinitebench.md) ([EN](../en/01_long_context/infinitebench.md))：定位：宣称“首个平均长度超过 100k tokens 的 LLM benchmark”，含合成与现实任务，中英双语。
- [L-CiteEval](01_long_context/l-citeeval.md) ([EN](../en/01_long_context/l-citeeval.md))：特征：多任务长上下文 + 必须产出 citations；自动评测引用准确与召回，旨在检测“模型是否真正利用上下文而非靠固有知识”。
- [L-Eval](01_long_context/l-eval.md) ([EN](../en/01_long_context/l-eval.md))：构成：20 子任务、508 长文档、2,000+人工标注 query‑response；输入跨度 3k–200k tokens；并讨论评测指标有效性。 任务形态：包含闭集与开放式任务（repo 列出分组与评测方式）。
- [LV-Eval](01_long_context/lv-eval.md) ([EN](../en/01_long_context/lv-eval.md))：定位：一个具备 5 档长度、双语 QA 任务和干扰事实插入机制的长上下文 benchmark，最高延伸到 256K。
- [LongBench-E](01_long_context/longbench-e.md) ([EN](../en/01_long_context/longbench-e.md))：提出方：作为分析不同输入长度下性能退化的变体，被 lm‑evaluation‑harness 文档明确描述为“均匀长度分布”版本。 目的：把“基准知识/短输入强项”与“真正长上下文能力”在统计上更多解耦（但仍需结合其它无泄漏/可控基准验证）。
- [LongBench Pro](01_long_context/longbench-pro.md) ([EN](../en/01_long_context/longbench-pro.md))：年份与规模：2026；1,500 条“自然出现”的长样本，中英双语；8k–256k tokens；11 主任务 25 子任务，并提出多维 taxonomy（依赖范围/长度/难度）。 构造：提出 human‑model 协作构造管线以降低专家标注成本，同时保持可核验性。 用途：适合做更接近真实“长上下文理解”回归测试与细粒度诊断（跨语对齐、有效上下文长度与 claimed length 的差距等）。
- [LongBench v2](01_long_context/longbench-v2.md) ([EN](../en/01_long_context/longbench-v2.md))：目标：强调“真实多任务场景下的深度理解与推理”，长度可到 2M words；并声称即便人类专家也难以快速完成。 覆盖：官方项目页与 repo 描述其长度范围、困难度与应用覆盖。
- [LongBench](01_long_context/longbench.md) ([EN](../en/01_long_context/longbench.md))：年份与提出方：2023 arXiv / 2024 ACL 发表；由清华相关团队（THUDM）提出与维护。 任务：单文档 QA、多文档 QA、摘要、Few-shot、合成任务、代码补全等 6 类；覆盖中文与英文。 规模与格式：标准化 21 个数据集为统一格式；论文提供平均长度统计，并强调自动化评测。 指标：按子任务采用 EM/F1/ROUGE/准确率等；以统一脚本汇总。 优势：多任务、双语、自动化统一格式；局限：典型样本长度仍以万级为主，面对百万上下文需要更“超长”基准补充。 典型用法：比较长上下文改造方法（RoPE scaling、长序列 SFT、检索压缩等）的整体收益。 许可：官方 repo/dataset card 未在摘要层明确统一说明（需以具体发布页为准）。 实现与榜单：官方 GitHub；也有 HuggingFace dataset 镜像；常见接入 lm‑evaluation‑harness。
- [LongBioBench](01_long_context/longbiobench.md) ([EN](../en/01_long_context/longbiobench.md))：动机：指出传统 NIAH 的“上下文不连贯、数字针、无干扰项”等设计可能被模型投机；以连贯传记文本构造可控环境，从理解/推理/可信维度评估。
- [LooGLE v2](01_long_context/loogle-v2.md) ([EN](../en/01_long_context/loogle-v2.md))：定位：NeurIPS 2025 DB Track；覆盖更贴近真实应用（repo 提到金融、法律、代码、游戏等域）。
- [LooGLE](01_long_context/loogle.md) ([EN](../en/01_long_context/loogle.md))：关键特征：文档较新（post‑2022），单文档平均 >24k tokens；6,000 自动生成问题；1,100+高质量人工 QA 用于长依赖评估。
- [Loong](01_long_context/loong.md) ([EN](../en/01_long_context/loong.md))：核心设计：不同于“用无关噪声补长度”，Loong 让每份文档都与答案相关，“漏掉任何文档会失败”；任务类型包括 Spotlight Locating、Comparison、Clustering、Chain of Reasoning；并提供中英场景（金融报告、法律案例、论文）。
- [Ref-Long](01_long_context/ref-long.md) ([EN](../en/01_long_context/ref-long.md))：定义：要求模型识别“哪些文档引用/指向某 key”，更强调上下文关系而非直接检索；构造三个子集（从合成到真实）。
- [RULER](01_long_context/ruler.md) ([EN](../en/01_long_context/ruler.md))：构成：13 个“代表性任务”，类别含检索、多跳 tracing、聚合、QA；强调“vanilla NIAH 近满分并不代表真实长上下文能力”。 工具支持：被 lm‑evaluation‑harness 明确集成（README）。
- [SCROLLS](01_long_context/scrolls.md) ([EN](../en/01_long_context/scrolls.md))：SCROLLS：7 个长文本任务/多域（摘要、QA、NLI 等），目标是“需要在长文本中综合信息”。
- [ZeroSCROLLS](01_long_context/zeroscrolls.md) ([EN](../en/01_long_context/zeroscrolls.md))：ZeroSCROLLS：从 SCROLLS 选 6 个任务并新增 4 个数据集，仅保留 test 与极小验证集，主要面向 zero-shot 长文本评测。

## 长上下文针类诊断

这一类 benchmark 主要使用可控合成任务，测试模型是否真的能在长上下文里定位关键信息，并诊断注意力覆盖、检索稳健性和多针区分能力。

- [BABILong](02_needle_and_diagnostics/babilong.md) ([EN](../en/02_needle_and_diagnostics/babilong.md))：设计：把 bAbI 风格推理任务嵌入超长文档（“推理在干草堆里”），包含 20 推理任务。
- [GraphWalks](02_needle_and_diagnostics/graphwalks.md) ([EN](../en/02_needle_and_diagnostics/graphwalks.md))：定义：把图以 edge list 形式放进上下文，让模型执行图操作（如多跳推理/搜索）。
- [MRCR](02_needle_and_diagnostics/mrcr.md) ([EN](../en/02_needle_and_diagnostics/mrcr.md))：公开来源： 在 HuggingFace 发布 MRCR 数据集卡片，描述其为“long context multiple needle in a haystack”，并注明灵感来自 Gemini 提出的 MRCR 评测； 的 Cloud Blog 解释 MRCR 为多轮长对话中复现早前回答/区分相似请求的能力测试。
- [NeedleBench](02_needle_and_diagnostics/needlebench.md) ([EN](../en/02_needle_and_diagnostics/needlebench.md))：动机：批评已有基准难以系统控制 needle 深度/数量/推理复杂度，提出合成框架评测双语长上下文的检索与推理。
- [Needle-in-a-Haystack](02_needle_and_diagnostics/niah.md) ([EN](../en/02_needle_and_diagnostics/niah.md))：定义：把关键事实随机插入长文本中，询问模型是否能找回；常用于压测“注意力是否能覆盖长上下文”。
- [NoLiMa](02_needle_and_diagnostics/nolima.md) ([EN](../en/02_needle_and_diagnostics/nolima.md))：动机：去掉 NIAH 中 question 与 needle 的字面重合捷径，更严格地测试模型是否能通过语义关联完成长上下文检索。
- [Passkey Retrieval](02_needle_and_diagnostics/passkey-retrieval.md) ([EN](../en/02_needle_and_diagnostics/passkey-retrieval.md))：来源：Landmark Attention 论文提出并用于评测“长文本中找回随机 passkey 数字”；后续大量长上下文工作复用其设置。
- [Phonebook](02_needle_and_diagnostics/phonebook.md) ([EN](../en/02_needle_and_diagnostics/phonebook.md))：典型定义：给定若干姓名-电话号码条目，few-shot 询问某人号码；在 Mamba‑based LM 实证研究中用于长上下文检索能力评估。 数据集：社区在 HuggingFace 上整理 phonebook 数据集集合（如 booydar/phonebook_N16，百万行规模在卡片中可见）。

## 检索、Embedding 与 RAG

这一类 benchmark 将外部知识库、索引或 retriever 视为语义记忆，评测范围从长文档表示学习到端到端 RAG 管线与忠实性。

- [BEIR](03_retrieval_rag/beir.md) ([EN](../en/03_retrieval_rag/beir.md))：BEIR：18 个数据集构成异质检索 benchmark，强调 zero-shot / OOD 泛化评测。
- [GraphRAG-Bench](03_retrieval_rag/graphrag-bench.md) ([EN](../en/03_retrieval_rag/graphrag-bench.md))：内容：16 学科、20 本核心教材构成域内语料；题型多样（选择/判断/多选/填空/开放式等），并不仅看最终答案正确性，也企图覆盖 graph construction、retrieval、generation、reasoning coherence 等维度。
- [KILT](03_retrieval_rag/kilt.md) ([EN](../en/03_retrieval_rag/kilt.md))：KILT：把多个知识密集任务统一到同一份 Wikipedia 快照，并联合评估答案质量与 provenance。
- [LaRA](03_retrieval_rag/lara.md) ([EN](../en/03_retrieval_rag/lara.md))：动机：指出既有研究对 “RAG vs 长上下文” 得出不一致结论，提出 LaRA 用于更严格比较；规模 2,326 test cases，覆盖四类实用 QA 任务与三类自然长文本。
- [LMEB](03_retrieval_rag/lmeb.md) ([EN](../en/03_retrieval_rag/lmeb.md))：定位：明确指出传统 embedding 基准（如 MTEB）主要覆盖“passage retrieval”，不足以衡量“碎片化、上下文依赖、时间跨度远”的记忆检索；因此提出 LMEB，覆盖 22 datasets、193 zero‑shot retrieval tasks、4 种记忆类型（episodic/dialogue/semantic/procedural），并指出与 MTEB 存在“正交性”。
- [LoCoV1](03_retrieval_rag/locov1.md) ([EN](../en/03_retrieval_rag/locov1.md))：问题：长文档检索场景中“chunking 不可行/无效”，需要真正对长文整体建模；提出 LoCoV1（12 项任务）来评测 long-context retrieval。
- [LongEmbed](03_retrieval_rag/longembed.md) ([EN](../en/03_retrieval_rag/longembed.md))：内容：构造 LongEmbed benchmark（2 合成 + 4 真实任务），评测 embedding 模型从 512/4k 等上下文扩展到 32k 的检索能力；合成任务包括 Personalized Passkey Retrieval 等设置。
- [MTEB](03_retrieval_rag/mteb.md) ([EN](../en/03_retrieval_rag/mteb.md))：MTEB：大规模 embedding benchmark，覆盖 58 个数据集、8 类任务和 112 种语言，常被用作通用检索与表征能力对照。
- [RAGBench](03_retrieval_rag/ragbench.md) ([EN](../en/03_retrieval_rag/ragbench.md))：规模：100k 样本，覆盖 5 个行业域与多种 RAG 任务类型；特点之一是“来自工业语料（如用户手册）”。
- [RAGTruth](03_retrieval_rag/ragtruth.md) ([EN](../en/03_retrieval_rag/ragtruth.md))：内容：近 18,000 条在 RAG setting 下由多模型产生的响应，进行 case 与 word-level 的幻觉标注（含幻觉强度）。
- [T2-RAGBench](03_retrieval_rag/t2-ragbench.md) ([EN](../en/03_retrieval_rag/t2-ragbench.md))：目的：评测真实文档常见的“文本+表格”场景；规模为 23,088 question‑context‑answer triples。

## 多会话对话记忆与个性化

这一类 benchmark 面向跨会话用户事实、长期项目历史和动态画像建模，关注情景记忆、跨轮追踪与个性化响应。

- [DialSim](04_dialogue_memory/dialsim.md) ([EN](../en/04_dialogue_memory/dialsim.md))：定义：为评估“长期多方对话理解”而提出对话模拟器；论文/摘要提到平均对话长度可达 350k tokens，并含不可回答问题。
- [LoCoMo](04_dialogue_memory/locomo.md) ([EN](../en/04_dialogue_memory/locomo.md))：语境：多论文与项目把 LoCoMo 作为长对话/长期记忆评测基准；其作为 “long-term memory” 场景常被方法论文引用（例如 2026 的 SimpleMem 在 LoCoMo 上报告显著提升）。
- [LongMemEval](04_dialogue_memory/longmemeval.md) ([EN](../en/04_dialogue_memory/longmemeval.md))：设置：把 500 个问题嵌入可扩展对话历史，对聊天助手的“长期交互记忆”做 benchmark；强调有统一环境与可扩展对话历史。
- [Mem-Gallery](04_dialogue_memory/mem-gallery.md) ([EN](../en/04_dialogue_memory/mem-gallery.md))：定位：评测多模态 agent 的长期会话记忆（综述页给出）。
- [PersonaMem](04_dialogue_memory/personamem.md) ([EN](../en/04_dialogue_memory/personamem.md))：定位：OpenReview 条目明确其为用于评估“动态用户交互中的个性化能力”的大规模 benchmark。
- [RealMem](04_dialogue_memory/realmem.md) ([EN](../en/04_dialogue_memory/realmem.md))：定义：定位为“真实场景的长期记忆交互 benchmark”；来源清单与条目描述强调跨会话、可控插入/回忆。
- [RealTalk](04_dialogue_memory/realtalk.md) ([EN](../en/04_dialogue_memory/realtalk.md))：定义：21 天语料，用于评测长期会话记忆。

## 智能体记忆与持续学习

这一类 benchmark 将 memory 放进 agent 任务、环境交互和持续学习场景中，考察的不仅是命中率，还包括长期决策、任务迁移与反馈累积。

- [AMA-Bench](05_agent_memory/ama-bench.md) ([EN](../en/05_agent_memory/ama-bench.md))：动机：指出现有记忆评测偏“对话中心”，而真实 agent memory 更多是 agent‑environment 交互流；AMA‑Bench 提供真实轨迹 QA + 可扩展合成轨迹 QA，并提出 AMA‑Agent。
- [CLLE](05_agent_memory/clle.md) ([EN](../en/05_agent_memory/clle.md))：定义：提出 Continual Language Learning Evaluation（CLLE）用于多语翻译持续学习评测。
- [CoIN](05_agent_memory/coin.md) ([EN](../en/05_agent_memory/coin.md))：定义：10 数据集、8 任务，评测持续指令学习下的“指令跟随”与“常识保留”，并观察灾难性遗忘。
- [GoodAI LTM Benchmark](05_agent_memory/goodai-ltm-benchmark.md) ([EN](../en/05_agent_memory/goodai-ltm-benchmark.md))：系列：官方博客与 GitHub 提供 benchmark 介绍、更新与 v3 标准化版本，强调评测“可持续与终身学习的 agent”。
- [LifelongAgentBench](05_agent_memory/lifelongagentbench.md) ([EN](../en/05_agent_memory/lifelongagentbench.md))：定义：将 LLM agents 视为“终身学习系统”，提供统一 benchmark 与框架。
- [LOCA-bench](05_agent_memory/loca-bench.md) ([EN](../en/05_agent_memory/loca-bench.md))：特点：把评测从“单步长片段检索”扩展到“代理在环境中探索/计划/行动”的场景；环境状态可控增长，context 可潜在趋于无限，并可评估不同 context‑management scaffold。
- [MemBench](05_agent_memory/membench.md) ([EN](../en/05_agent_memory/membench.md))：定义：将记忆拆成 factual memory 与 reflective memory 两层，并区分参与/观察等交互场景；强调从 effectiveness、efficiency、capacity 多方面评估 agent memory。
- [MemoryAgentBench](05_agent_memory/memoryagentbench.md) ([EN](../en/05_agent_memory/memoryagentbench.md))：定位：用于评测“长期偏好与工具使用”的 agent memory（arXiv 条目）。
- [MemoryArena](05_agent_memory/memoryarena.md) ([EN](../en/05_agent_memory/memoryarena.md))：定位：面向“相互依赖的多 session agentic 任务”评测 agent memory；该名称在集中清单与论文条目中出现。
- [MemoryBench](05_agent_memory/memorybench.md) ([EN](../en/05_agent_memory/memorybench.md))：定义：指出既有“LLM memory benchmark”偏阅读理解长输入，缺少“服务期从用户反馈中持续学习”的评测；提出用户反馈模拟框架与多域多语言 benchmark。
- [MemoryCD](05_agent_memory/memorycd.md) ([EN](../en/05_agent_memory/memorycd.md))：定位：OpenReview 条目称其为“首个大规模、用户中心、跨域记忆 benchmark”，由 Amazon Review 生命周期行为派生。
- [Rubric Feedback Bench](05_agent_memory/rubric-feedback-bench.md) ([EN](../en/05_agent_memory/rubric-feedback-bench.md))：来源：提出 Memory‑as‑a‑Tool 范式，把迭代反馈转为可检索指南，并在 Rubric Feedback Bench 上评测；PDF 提到该数据集含 42 精选场景。

## 知识编辑与语义记忆更新

这一类 benchmark 检验模型写入新事实后的更新质量，重点看局部性、泛化、连锁传播与一致性保持。

- [CounterFact](06_knowledge_editing/counterfact.md) ([EN](../en/06_knowledge_editing/counterfact.md))：来源：ROME 论文明确提出“COUNTERFACT”作为更敏感的编辑评测数据集；并提供项目页与代码。
- [MQuAKE](06_knowledge_editing/mquake.md) ([EN](../en/06_knowledge_editing/mquake.md))：动机：编辑一个事实应导致相关推论答案改变；MQuAKE 用多跳问题检验“涟漪效应”。
- [QAEdit + WILD](06_knowledge_editing/qaeedit-wild.md) ([EN](../en/06_knowledge_editing/qaeedit-wild.md))：内容：指出既有编辑指标可能高估实用效果；提出 QAEdit benchmark 与 WILD 框架。
- [ZsRE](06_knowledge_editing/zsre.md) ([EN](../en/06_knowledge_editing/zsre.md))：来源：Levy 等 2017 提出，把关系抽取转为 QA；并提供公开数据集页面；在模型编辑文献中被广泛用作“context‑free QA 编辑”基准。

## 多模态长程记忆与检索推理

这一类 benchmark 把长程记忆问题扩展到 PDF、图像池和长视频，强调跨模态大规模证据池中的定位与整合。

- [DocHaystack](07_multimodal/dochaystack.md) ([EN](../en/07_multimodal/dochaystack.md))：既有多图 QA 候选集合过小，不足以代表真实检索，因此该工作提出可扩展到 1,000 视觉文档的检索与理解基准，并报告 recall@1 等检索指标。
- [Ego4D Episodic Memory](07_multimodal/ego4d-episodic-memory.md) ([EN](../en/07_multimodal/ego4d-episodic-memory.md))：官方定义：Episodic Memory 任务旨在使“过去视频可查询”，并要求定位答案在过去视频何处出现；Ego4D 官方页给出数据规模与基准概览，并提供 benchmark repo 链接。
- [InfoHaystack](07_multimodal/infohaystack.md) ([EN](../en/07_multimodal/infohaystack.md))：既有多图 QA 候选集合过小，不足以代表真实检索，因此该工作提出可扩展到 1,000 视觉文档的检索与理解基准，并报告 recall@1 等检索指标。
- [LongVideoBench](07_multimodal/longvideobench.md) ([EN](../en/07_multimodal/longvideobench.md))：数据：3,763 视频与字幕；6,678 多选题；强调“referring reasoning”。
- [MM-NIAH](07_multimodal/mm-niah.md) ([EN](../en/07_multimodal/mm-niah.md))：设计：把多段图文文档拼接成超长图文“干草堆”，任务含 retrieval/counting/reasoning。
- [MMLongBench-Doc](07_multimodal/mmlongbench-doc.md) ([EN](../en/07_multimodal/mmlongbench-doc.md))：内容：基于多页 PDF（平均约 47.5 页、~21k tokens），含跨页与不可答问题；在多 LVLM 上评测，显示长文档多模态理解仍具挑战。
- [MMNeedle](07_multimodal/mmneedle.md) ([EN](../en/07_multimodal/mmneedle.md))：特点：通过 multi-image 与 image stitching 增大上下文，评测模型按文本描述定位子图；并观察负样本幻觉。
- [MultiHaystack](07_multimodal/multihaystack.md) ([EN](../en/07_multimodal/multihaystack.md))：定位：强调“在巨大异质多模态池里先检索后推理”，并显示“给正确证据 vs 需要自己检索”的性能差距；提供 46,000+候选与 747 问题。
- [Video-MME](07_multimodal/video-mme.md) ([EN](../en/07_multimodal/video-mme.md))：数据：900 视频（约 254 小时）与 2,700 人工标注 QA；多域多时长。
- [Visual Haystacks](07_multimodal/visual-haystacks.md) ([EN](../en/07_multimodal/visual-haystacks.md))：定位：评测 LMM 在大量“可能不相关”的图像集合中检索并推理；并提供 MIRAGE 作为视觉 RAG baseline；项目页与 paper 给出。
