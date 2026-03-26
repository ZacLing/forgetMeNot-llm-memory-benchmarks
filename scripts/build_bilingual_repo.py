from __future__ import annotations

import re
import textwrap
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Tuple

import yaml


ROOT = Path(__file__).resolve().parents[1]
SOURCE_ROOT = ROOT / "source_catalog"
KB_ROOT = ROOT / "knowledge_base"


CATEGORY_ORDER = [
    "01_long_context",
    "02_needle_and_diagnostics",
    "03_retrieval_rag",
    "04_dialogue_memory",
    "05_agent_memory",
    "06_knowledge_editing",
    "07_multimodal",
]


CATEGORY_META = {
    "01_long_context": {
        "zh": "长上下文理解与推理",
        "en": "Long-Context Understanding and Reasoning",
        "intro_zh": "这一类 benchmark 聚焦模型在超长文本、代码仓库、长对话历史和结构化长输入中的定位、综合、推理与生成能力，是“给定上下文内工作记忆”的核心评测集合。",
        "intro_en": "This family focuses on retrieval, synthesis, reasoning, and generation inside very long contexts such as long documents, code repositories, long dialogue histories, and structured long inputs.",
    },
    "02_needle_and_diagnostics": {
        "zh": "长上下文针类诊断",
        "en": "Needle Retrieval and Diagnostic Probes",
        "intro_zh": "这一类 benchmark 主要使用可控合成任务，测试模型是否真的能在长上下文里定位关键信息，并诊断注意力覆盖、检索稳健性和多针区分能力。",
        "intro_en": "This family uses controllable synthetic setups to test whether a model can truly locate critical information in long contexts and to diagnose retrieval robustness, attention coverage, and multi-needle disambiguation.",
    },
    "03_retrieval_rag": {
        "zh": "检索、Embedding 与 RAG",
        "en": "Retrieval, Embeddings, and RAG",
        "intro_zh": "这一类 benchmark 将外部知识库、索引或 retriever 视为语义记忆，评测范围从长文档表示学习到端到端 RAG 管线与忠实性。",
        "intro_en": "This family treats external corpora, indices, and retrievers as semantic memory, spanning long-document representation learning, end-to-end RAG pipelines, and faithfulness evaluation.",
    },
    "04_dialogue_memory": {
        "zh": "多会话对话记忆与个性化",
        "en": "Multi-Session Dialogue Memory and Personalization",
        "intro_zh": "这一类 benchmark 面向跨会话用户事实、长期项目历史和动态画像建模，关注情景记忆、跨轮追踪与个性化响应。",
        "intro_en": "This family targets episodic memory across sessions, long-running user history, and dynamic personalization, with emphasis on cross-turn tracking and user-aware responses.",
    },
    "05_agent_memory": {
        "zh": "智能体记忆与持续学习",
        "en": "Agent Memory and Continual Learning",
        "intro_zh": "这一类 benchmark 将 memory 放进 agent 任务、环境交互和持续学习场景中，考察的不仅是命中率，还包括长期决策、任务迁移与反馈累积。",
        "intro_en": "This family places memory inside agent tasks, environment interaction, and continual-learning settings, evaluating not only recall but also long-term decision quality, task transfer, and feedback accumulation.",
    },
    "06_knowledge_editing": {
        "zh": "知识编辑与语义记忆更新",
        "en": "Knowledge Editing and Semantic Memory Updates",
        "intro_zh": "这一类 benchmark 检验模型写入新事实后的更新质量，重点看局部性、泛化、连锁传播与一致性保持。",
        "intro_en": "This family evaluates how well a model updates semantic memory after a new fact is written, including locality, generalization, ripple effects, and consistency.",
    },
    "07_multimodal": {
        "zh": "多模态长程记忆与检索推理",
        "en": "Multimodal Long-Horizon Memory and Retrieval-Reasoning",
        "intro_zh": "这一类 benchmark 把长程记忆问题扩展到 PDF、图像池和长视频，强调跨模态大规模证据池中的定位与整合。",
        "intro_en": "This family extends long-horizon memory to PDFs, image pools, and long videos, emphasizing evidence localization and integration over large multimodal contexts.",
    },
}


OVERVIEW_EN = {
    "academiceval": "A live long-context generation benchmark built from recent arXiv papers for title, abstract, introduction, and related-work writing tasks.",
    "ada-leval": "A length-adaptable benchmark with TSort and BestAnswer for controllable long-context evaluation.",
    "bamboo": "A contamination-aware long-text benchmark spanning QA, hallucination detection, ranking, language modeling, and code completion.",
    "infinitebench": "A bilingual benchmark that mixes synthetic and realistic tasks with average context length beyond 100k tokens.",
    "l-citeeval": "A citation-grounded long-context benchmark that scores both answer quality and citation precision and recall.",
    "l-eval": "A standardized long-context suite with 20 tasks, 508 long documents, and 2,000+ human-labeled query-response pairs.",
    "longbench-e": "A uniform-length evaluation variant of LongBench designed to decouple true long-context ability from short-context bias.",
    "longbench-pro": "A more realistic bilingual long-context benchmark with 1,500 naturally occurring long samples and a fine-grained taxonomy.",
    "longbench-v2": "A realistic multitask benchmark with 8k-to-2M-word contexts targeting deep understanding and reasoning.",
    "longbench": "The first bilingual multitask long-context benchmark covering QA, summarization, few-shot learning, synthetic tasks, and code completion.",
    "longbiobench": "A controllable long-context benchmark built from coherent biographical narratives to avoid shortcut-prone needle-style setups.",
    "loogle-v2": "A real-world long-dependency benchmark targeting practical domains such as finance, law, code, and games.",
    "loogle": "A long-document benchmark built from recent real-world documents with both automatic and human-written QA.",
    "loong": "An extended multi-document QA benchmark where every document is relevant, so missing any document hurts performance.",
    "ref-long": "A referencing-oriented long-context benchmark that asks models to identify which documents point to a target key.",
    "ruler": "A controllable long-context diagnostic suite covering retrieval, aggregation, multi-hop tracing, and QA.",
    "scrolls": "A standardized long-text benchmark spanning summarization, QA, NLI, and other long-sequence tasks.",
    "zeroscrolls": "A zero-shot long-text benchmark derived from SCROLLS and additional datasets with tiny validation sets and no training split.",
    "babilong": "A reasoning-in-a-haystack benchmark that embeds bAbI-style reasoning tasks inside ultra-long documents.",
    "graphwalks": "An edge-list-based graph reasoning dataset for long-context multi-hop search and traversal operations.",
    "mrcr": "A multiple-needle long-context benchmark focused on multi-round retrieval and distinguishing similar earlier requests.",
    "needlebench": "A synthetic bilingual benchmark that systematically varies needle depth, density, and reasoning difficulty.",
    "niah": "The canonical needle-in-a-haystack stress test that inserts key facts into long contexts and asks models to recover them.",
    "passkey-retrieval": "A classic passkey recall setup, originating from Landmark Attention, for testing retrieval of a hidden random key.",
    "phonebook": "A task family that measures long-context retrieval by querying names and phone numbers from large lookup tables.",
    "beir": "A heterogeneous zero-shot retrieval benchmark for evaluating generalization across 18 IR datasets.",
    "graphrag-bench": "A full-pipeline GraphRAG benchmark over textbook corpora that evaluates construction, retrieval, generation, and reasoning coherence.",
    "kilt": "A knowledge-intensive benchmark that unifies multiple tasks over a shared Wikipedia snapshot and provenance evaluation.",
    "lara": "A benchmark for comparing long-context LLMs and RAG systems under the same realistic QA settings.",
    "lmeb": "A long-horizon memory embedding benchmark covering episodic, dialogue, semantic, and procedural retrieval.",
    "locov1": "A long-document retrieval benchmark for encoders where chunking is often ineffective or impossible.",
    "longembed": "A benchmark for extending embedding models from short contexts to long-context retrieval up to 32k tokens.",
    "mteb": "A large-scale general text-embedding benchmark covering multiple tasks, datasets, and languages.",
    "ragbench": "An explainable end-to-end RAG benchmark with large-scale industrial-style data and annotated failure modes.",
    "ragtruth": "A hallucination corpus for RAG that provides case-level and word-level faithfulness annotations.",
    "t2-ragbench": "A text-and-table RAG benchmark with 23,088 context-independent triples for retrieval plus numerical reasoning.",
    "dialsim": "A dialogue simulator for long multi-party conversations, including very long contexts and unanswerable cases.",
    "locomo": "A benchmark of very long-term conversational memory with event-grounded multi-session dialogues.",
    "longmemeval": "An interactive benchmark that embeds 500 questions into expandable chat histories for long-term assistant memory.",
    "mem-gallery": "A multimodal long-term conversational memory benchmark for MLLM agents across multi-session interactions.",
    "personamem": "A dynamic personalization benchmark that evaluates whether LLMs track evolving user traits and preferences over time.",
    "realmem": "A benchmark for project-oriented real-world memory interactions with cross-session dialogues and evolving goals.",
    "realtalk": "A 21-day real-world conversation dataset and benchmark for long-term open-domain dialogue memory.",
    "ama-bench": "A long-horizon agent-memory benchmark built from real trajectories and scalable synthetic traces.",
    "clle": "A benchmark for continual language learning in multilingual machine translation.",
    "coin": "A multimodal continual instruction-tuning benchmark that measures instruction following and retained knowledge under drift.",
    "goodai-ltm-benchmark": "A dynamic conversational benchmark for long-term memory, continual learning, and information integration in agents.",
    "lifelongagentbench": "A unified benchmark that evaluates LLM agents as lifelong learners across evolving tasks.",
    "loca-bench": "A controllable benchmark for language agents under extreme context growth in interactive environments.",
    "membench": "A comprehensive benchmark that separates factual and reflective memory in LLM-based agents.",
    "memoryagentbench": "A benchmark that reformats memory-agent evaluation into incremental multi-turn interactions.",
    "memoryarena": "A benchmark for agent memory in interdependent multi-session agentic tasks.",
    "memorybench": "A benchmark for memory and continual learning in LLM systems driven by simulated user feedback.",
    "memorycd": "A user-centric cross-domain benchmark for lifelong personalization and long-context user memory in LLM agents.",
    "rubric-feedback-bench": "A benchmark for turning iterative feedback into retrievable rules or memory tools.",
    "counterfact": "A classic counterfactual dataset introduced by ROME for evaluating factual editing efficacy, specificity, and generalization.",
    "mquake": "A multi-hop benchmark that tests whether factual edits propagate correctly through related reasoning chains.",
    "qaeedit-wild": "A realistic editing benchmark and evaluation framework that revisits model editing in the wild.",
    "zsre": "A zero-shot relation extraction dataset often repurposed as a context-free QA editing benchmark.",
    "dochaystack": "A visual document reasoning benchmark over piles of up to 1,000 documents.",
    "ego4d-episodic-memory": "The official Ego4D task for making past egocentric video queryable and temporally localizable.",
    "infohaystack": "A large-pool visual document retrieval benchmark introduced alongside DocHaystack.",
    "longvideobench": "An interleaved video-language long-context benchmark with videos up to around one hour.",
    "mm-niah": "A long multimodal document needle benchmark with retrieval, counting, and reasoning tasks.",
    "mmlongbench-doc": "A multimodal long-document benchmark built on long PDFs with text, figures, and tables.",
    "mmneedle": "A multi-image needle benchmark that stresses sub-image localization and negative-sample hallucination.",
    "multihaystack": "A multimodal retrieval-and-reasoning benchmark over 46k images, videos, and documents.",
    "video-mme": "A comprehensive video MLLM benchmark spanning domains, durations, and 2,700 human-labeled QA pairs.",
    "visual-haystacks": "A vision-centric needle-in-a-haystack benchmark for retrieval and reasoning over large image sets.",
}


NOTE_EN = {
    "本卡片优先使用论文页、项目页与代码仓库等官方来源；若原报告中的链接存在错误，则以标题匹配后的官方链接为准。": "This card prioritizes official paper pages, project pages, and code repositories. When a link in the original report was incorrect, the corrected official link is used instead.",
    "原报告中的 arXiv 链接指向了无关论文，已按 benchmark 标题校正为 LoCoMo 官方论文。": "The original report pointed to an unrelated arXiv page. This card corrects it to the official LoCoMo paper.",
    "原报告中的 arXiv 与 GitHub 链接均与 benchmark 不一致，这里改为与 REALTALK 论文标题一致的官方资源。": "Both the arXiv and GitHub links in the original report were mismatched. This card replaces them with official REALTALK resources.",
    "原报告仅给出 OpenReview 链接；这里补充了可直接抓取 abstract 与 BibTeX 的 arXiv 版本及官方代码页。": "The original report only included an OpenReview link. This card additionally provides the arXiv version and official code page so that the abstract and BibTeX can be accessed directly.",
    "原报告中的 arXiv 链接有误，已替换为标题匹配的 RealMem 论文。": "The original arXiv link was incorrect. This card replaces it with the title-matched RealMem paper.",
    "原报告中的 arXiv 链接有误，已替换为 Mem-Gallery 官方论文。": "The original arXiv link was incorrect. This card replaces it with the official Mem-Gallery paper.",
    "原报告中的 arXiv 链接有误，已替换为 MemoryArena 官方论文。": "The original arXiv link was incorrect. This card replaces it with the official MemoryArena paper.",
    "LongBench-E 更像 LongBench 的长度分布变体说明，而不是单独发表的 benchmark 论文；因此这里以 lm-evaluation-harness 官方任务文档作为可引用来源。": "LongBench-E is better understood as the uniform-length evaluation variant of LongBench than as a separately published benchmark paper. This card therefore cites the official lm-evaluation-harness task documentation.",
    "NIAH 在当前文献里更多是一套测试方法与实现范式，而非单一正式论文 benchmark；因此这里采用官方 GitHub 实现作为主引用。": "In the current literature, NIAH is better treated as a testing protocol and implementation pattern than as a single formally published benchmark paper. This card therefore uses the official GitHub implementation as the primary source.",
    "GraphWalks 在原报告中以官方数据集形式出现，未给出独立论文；这里以数据集卡片作为主来源。": "GraphWalks appears in the original report as an official dataset release without a dedicated benchmark paper, so this card uses the dataset card as the primary source.",
    "Phonebook 更接近一类被多篇长上下文论文复用的任务家族，而不是单独命名发表的 benchmark 论文。这里沿用报告中的代表性论文与数据集集合来说明其标准设定。": "Phonebook is better viewed as a task family reused across multiple long-context papers than as a standalone benchmark paper. This card therefore follows the representative paper and dataset collection cited in the report.",
    "OpenReview 页面当前拒绝直接抓取，作者、标题与年份来自检索结果中的 OpenReview 官方列表页；abstract 未能可靠抓取，因此本卡片只保留中文概述。": "The OpenReview page currently blocks direct crawling. The authors, title, and year were reconstructed from official OpenReview listing results, while the abstract could not be retrieved reliably.",
    "Ego4D Episodic Memory 在原报告中以官方 benchmark 文档和 repo 的形式出现，而不是单篇定义论文；因此这里以官方 benchmark 页面作为主引用来源。": "Ego4D Episodic Memory appears in the original report as an official benchmark page and repository rather than as a single defining paper, so this card uses the official benchmark documentation as the primary source.",
    "主论文链接通过检索补齐：CLLE: A Benchmark for Continual Language Learning Evaluation in ...": "The main paper link was completed through search because the source report only listed the ACL PDF.",
}


ROOT_NAV_EN = "[English](./README.md) | [中文](./README_zh.md) | [English KB](./knowledge_base/en/README.md) | [中文知识库](./knowledge_base/zh/README.md)"
ROOT_NAV_ZH = "[English](./README.md) | [中文](./README_zh.md) | [English KB](./knowledge_base/en/README.md) | [中文知识库](./knowledge_base/zh/README.md)"
KB_NAV_EN = "[Repository Home](../../README.md) | [中文索引](../zh/README.md)"
KB_NAV_ZH = "[仓库首页](../../README_zh.md) | [English Index](../en/README.md)"


@dataclass
class Card:
    path: Path
    folder: str
    slug: str
    name: str
    year: str
    category_zh: str
    subcategory_zh: str
    memory_type: str
    primary_source_kind: str
    primary_source_url: str
    overview_zh: str
    abstract_raw: str
    notes_zh: List[str]
    urls: List[Tuple[str, str]]
    bibtex: str
    paper_title: str


def parse_frontmatter(text: str) -> Tuple[Dict, str]:
    if not text.startswith("---\n"):
        return {}, text
    _, rest = text.split("---\n", 1)
    front, body = rest.split("\n---\n", 1)
    return yaml.safe_load(front), body


def extract_section(body: str, title: str) -> str:
    pattern = rf"## {re.escape(title)}\n+(.*?)(?=\n## |\Z)"
    match = re.search(pattern, body, re.S)
    return match.group(1).strip() if match else ""


def parse_urls(section: str) -> List[Tuple[str, str]]:
    rows = []
    for line in section.splitlines():
        if not line.startswith("| "):
            continue
        if "---" in line:
            continue
        parts = [part.strip() for part in line.strip("|").split("|")]
        if len(parts) == 2 and parts[0] != "类型":
            rows.append((parts[0], parts[1]))
    return rows


def parse_card(path: Path) -> Card:
    text = path.read_text()
    frontmatter, body = parse_frontmatter(text)
    info = extract_section(body, "结构化信息")
    overview = extract_section(body, "基础介绍")
    abstract = extract_section(body, "Abstract")
    urls = parse_urls(extract_section(body, "URL 汇总"))
    bib = extract_section(body, "BibTeX")
    bib = re.sub(r"^```bibtex\n", "", bib)
    bib = re.sub(r"\n```$", "", bib).strip()
    notes_raw = extract_section(body, "备注")
    notes = [line[2:].strip() for line in notes_raw.splitlines() if line.startswith("- ")]

    def table_value(field: str) -> str:
        m = re.search(rf"\| {re.escape(field)} \| (.*?) \|", info)
        return m.group(1).strip() if m else ""

    abstract_lines = []
    for line in abstract.splitlines():
        if line.startswith("> "):
            abstract_lines.append(line[2:])
    abstract_raw = " ".join(abstract_lines).strip()
    return Card(
        path=path,
        folder=path.parent.name,
        slug=frontmatter["slug"],
        name=frontmatter["name"],
        year=str(frontmatter.get("year", "")),
        category_zh=frontmatter["category"],
        subcategory_zh=frontmatter["subcategory"],
        memory_type=frontmatter["memory_type"],
        primary_source_kind=frontmatter["primary_source_kind"],
        primary_source_url=frontmatter["primary_source_url"],
        overview_zh=overview,
        abstract_raw=abstract_raw,
        notes_zh=notes,
        urls=urls,
        bibtex=bib,
        paper_title=table_value("论文标题"),
    )


def load_cards() -> List[Card]:
    cards = []
    for folder in CATEGORY_ORDER:
        for path in sorted((SOURCE_ROOT / folder).glob("*.md")):
            cards.append(parse_card(path))
    return cards


def translate_url_label(label: str) -> str:
    mapping = {
        "论文页": "Paper",
        "论文 PDF": "Paper PDF",
        "论文 HTML": "Paper HTML",
        "项目主页": "Project Page",
        "补充主页": "Supplementary Page",
        "版本发布页": "Release Page",
        "GitHub": "GitHub",
        "数据集页": "Dataset",
    }
    return mapping.get(label, label)


def notes_to_en(notes_zh: List[str]) -> List[str]:
    return [NOTE_EN.get(note, "See the Chinese card for the original curator note.") for note in notes_zh]


def normalize_bibtex(bib: str) -> str:
    return bib.strip() if bib.strip() else "% BibTeX not available"


def write_card_zh(card: Card) -> None:
    out = KB_ROOT / "zh" / card.folder / f"{card.slug}.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    en_rel = f"../../en/{card.folder}/{card.slug}.md"
    content = textwrap.dedent(
        f"""\
        ---
        name: {card.name}
        slug: {card.slug}
        language: zh
        category: {card.category_zh}
        subcategory: {card.subcategory_zh}
        memory_type: {card.memory_type}
        year: "{card.year}"
        primary_source_kind: {card.primary_source_kind}
        primary_source_url: {card.primary_source_url}
        counterpart_en: {en_rel}
        ---

        # {card.name}

        [中文知识库索引](../README.md) | [English Card]({en_rel})

        ## 结构化信息

        | 字段 | 内容 |
        |---|---|
        | Benchmark | {card.name} |
        | 分类 | {card.category_zh} |
        | 子类 | {card.subcategory_zh} |
        | 记忆侧重 | {card.memory_type} |
        | 首次年份 | {card.year} |
        | 主要来源类型 | {card.primary_source_kind} |
        | 论文标题 | {card.paper_title} |
        | 英文卡片 | [{card.name}]({en_rel}) |

        ## 基础介绍

        {card.overview_zh}

        ## Abstract
        """
    ).strip()
    if card.abstract_raw:
        content += f"\n### 原始摘要\n> {card.abstract_raw}\n\n### 中文抽取\n{card.overview_zh}\n"
    else:
        content += f"\n未能从当前可访问的官方页面稳定抓取原始 abstract。以下中文说明基于知识库整理结果：\n\n{card.overview_zh}\n"
    content += "\n## URL 汇总\n\n| 类型 | 链接 |\n|---|---|\n"
    for label, url in card.urls:
        content += f"| {label} | {url} |\n"
    content += f"\n## BibTeX\n\n```bibtex\n{normalize_bibtex(card.bibtex)}\n```\n"
    content += "\n## 备注\n\n"
    for note in card.notes_zh:
        content += f"- {note}\n"
    out.write_text(content)


def write_card_en(card: Card) -> None:
    out = KB_ROOT / "en" / card.folder / f"{card.slug}.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    zh_rel = f"../../zh/{card.folder}/{card.slug}.md"
    overview_en = OVERVIEW_EN[card.slug]
    note_en = notes_to_en(card.notes_zh)
    category_en = CATEGORY_META[card.folder]["en"]
    content = textwrap.dedent(
        f"""\
        ---
        name: {card.name}
        slug: {card.slug}
        language: en
        category: {category_en}
        subcategory: {card.subcategory_zh}
        memory_type: {card.memory_type}
        year: "{card.year}"
        primary_source_kind: {card.primary_source_kind}
        primary_source_url: {card.primary_source_url}
        counterpart_zh: {zh_rel}
        ---

        # {card.name}

        [English Knowledge Base Index](../README.md) | [中文卡片]({zh_rel})

        ## Structured Metadata

        | Field | Content |
        |---|---|
        | Benchmark | {card.name} |
        | Category | {category_en} |
        | Subcategory | {card.subcategory_zh} |
        | Memory Focus | {card.memory_type} |
        | First Year | {card.year} |
        | Primary Source Type | {card.primary_source_kind} |
        | Paper Title | {card.paper_title} |
        | Chinese Card | [{card.name}]({zh_rel}) |

        ## Overview

        {overview_en}

        ## Abstract
        """
    ).strip()
    if card.abstract_raw:
        content += f"\n### Original Abstract\n> {card.abstract_raw}\n\n### Curated Summary\n{overview_en}\n"
    else:
        content += f"\nNo stable official abstract was retrievable from the current source pages. The curated English summary below is derived from the Chinese knowledge card:\n\n{overview_en}\n"
    content += "\n## Links\n\n| Type | Link |\n|---|---|\n"
    for label, url in card.urls:
        content += f"| {translate_url_label(label)} | {url} |\n"
    content += f"\n## BibTeX\n\n```bibtex\n{normalize_bibtex(card.bibtex)}\n```\n"
    content += "\n## Remarks\n\n"
    for note in note_en:
        content += f"- {note}\n"
    out.write_text(content)


def entry_line_en(card: Card, root: bool) -> str:
    en_prefix = "knowledge_base/en/" if root else ""
    zh_prefix = "knowledge_base/zh/" if root else "../zh/"
    if not root:
        zh_prefix = f"../zh/{card.folder}/{card.slug}.md"
        en_link = f"{card.folder}/{card.slug}.md"
        return f"- [{card.name}]({en_link}) ([CN]({zh_prefix})): {OVERVIEW_EN[card.slug]}"
    en_link = f"{en_prefix}{card.folder}/{card.slug}.md"
    zh_link = f"{zh_prefix}{card.folder}/{card.slug}.md"
    return f"- [{card.name}]({en_link}) ([CN]({zh_link})): {OVERVIEW_EN[card.slug]}"


def entry_line_zh(card: Card, root: bool) -> str:
    overview_zh = re.sub(r"\s*\n\s*", " ", card.overview_zh).strip()
    zh_prefix = "knowledge_base/zh/" if root else ""
    en_prefix = "knowledge_base/en/" if root else "../en/"
    if not root:
        zh_link = f"{card.folder}/{card.slug}.md"
        en_link = f"../en/{card.folder}/{card.slug}.md"
        return f"- [{card.name}]({zh_link}) ([EN]({en_link}))：{overview_zh}"
    zh_link = f"{zh_prefix}{card.folder}/{card.slug}.md"
    en_link = f"{en_prefix}{card.folder}/{card.slug}.md"
    return f"- [{card.name}]({zh_link}) ([EN]({en_link}))：{overview_zh}"


def build_index_en(cards: List[Card], root: bool) -> str:
    groups: Dict[str, List[Card]] = {folder: [] for folder in CATEGORY_ORDER}
    for card in cards:
        groups[card.folder].append(card)
    total = len(cards)
    nav = ROOT_NAV_EN if root else KB_NAV_EN
    if root:
        lines = [
            "# ForgetMeNot",
            "",
            "> An awesome-style repository collecting benchmarks for LLM memory.",
            "",
            '<p align="center">',
            '  <img src="./assets/cover.svg" alt="ForgetMeNot cover" width="100%">',
            "</p>",
            "",
            '<p align="center">',
            "  <strong>A curated bilingual knowledge base of LLM memory benchmarks.</strong><br/>",
            "  Long-context reasoning, dialogue memory, agent memory, RAG, continual learning, and multimodal long-horizon evaluation.",
            "</p>",
            "",
            '<p align="center">',
            '  <a href="https://awesome.re"><img src="https://awesome.re/badge-flat.svg" alt="Awesome"></a>',
            '  <img src="https://img.shields.io/badge/cards-69-0f766e?style=flat-square" alt="69 cards">',
            '  <img src="https://img.shields.io/badge/families-7-1d4ed8?style=flat-square" alt="7 families">',
            '  <img src="https://img.shields.io/badge/language-English%20default-black?style=flat-square" alt="English default">',
            '  <img src="https://img.shields.io/badge/Chinese-mirror-b91c1c?style=flat-square" alt="Chinese mirror">',
            '  <img src="https://img.shields.io/badge/license-MIT-16a34a?style=flat-square" alt="MIT License">',
            '  <img src="https://img.shields.io/badge/PRs-welcome-e11d48?style=flat-square" alt="PRs welcome">',
            "</p>",
            "",
            nav,
            "",
            "ForgetMeNot is built as a bilingual, repository-style survey layer over a structured benchmark knowledge base. It is designed for researchers who need to move quickly from a benchmark family, to an index, to an individual benchmark card with links, abstracts, and BibTeX.",
            "",
            "> [!NOTE]",
            "> English is the default reading path. If you prefer the manually curated Chinese summaries, jump to `README_zh.md` or `knowledge_base/zh/README.md`.",
            "",
            "## Why ForgetMeNot",
            "",
            "- It organizes benchmark discovery around memory-oriented research questions rather than a flat paper list.",
            "- It exposes a bilingual workflow: English for default navigation, Chinese for detailed curated notes.",
            "- It links every benchmark entry to a structured card with URLs, scope, and full BibTeX.",
            "",
            "## At a Glance",
            "",
            "| Field | Value |",
            "|---|---|",
            f"| Benchmark cards | {total} |",
            f"| Benchmark families | {len(CATEGORY_ORDER)} |",
            "| Default entry | `README.md` |",
            "| Chinese mirror | `README_zh.md` and `knowledge_base/zh/` |",
            "| Contribution guide | `CONTRIBUTING.md` |",
            "| Citation file | `CITATION.cff` |",
            "",
            "## Coverage Snapshot",
            "",
            "| Family | Cards | Focus |",
            "|---|---:|---|",
        ]
        for folder in CATEGORY_ORDER:
            meta = CATEGORY_META[folder]
            lines.append(
                f"| {meta['en']} | {len(groups[folder])} | {meta['intro_en']} |"
            )
        lines.extend(
            [
                "",
                "## Reading Paths",
                "",
                "1. **Survey first**: start from the family index below, then open the English card that best matches your task.",
                "2. **Chinese notes first**: jump to `README_zh.md` or `knowledge_base/zh/README.md` for manually curated Chinese summaries.",
                "3. **Source-first verification**: use the benchmark card to open the original paper, repo, or project page and inspect the full BibTeX.",
                "",
                "## Repository Layout",
                "",
                "- `README.md`: English landing page and high-level index.",
                "- `README_zh.md`: Chinese landing page and high-level index.",
                "- `assets/cover.svg`: repository banner used by the landing pages.",
                "- `knowledge_base/en/`: English benchmark cards.",
                "- `knowledge_base/zh/`: Chinese benchmark cards.",
                "- `source_catalog/`: internal structured source cards used to regenerate the bilingual knowledge base.",
                "- `scripts/build_benchmark_catalog.py`: generator for the structured benchmark source catalog.",
                "- `scripts/build_bilingual_repo.py`: generator for the bilingual repository landing pages and cards.",
                "",
                "## Table of Contents",
                "",
            ]
        )
    else:
        lines = [
            "# ForgetMeNot Knowledge Base (English)",
            "",
            '<p align="center">',
            '<a href="https://awesome.re"><img src="https://awesome.re/badge-flat.svg" alt="Awesome"></a>',
            "</p>",
            "",
            nav,
            "",
            "This English index mirrors the repository landing page and points to the detailed benchmark cards in the English knowledge base.",
            "",
            f"As of the current version, the repository contains **{total}** benchmark cards across **{len(CATEGORY_ORDER)}** benchmark families, with parallel **English** and **Chinese** cards.",
            "",
            "> [!NOTE]",
            "> English is the default reading path. Use the Chinese links if you want the manually curated Chinese summaries first.",
            "",
            "## Navigation",
            "",
            "- [Repository Home](../../README.md)",
            "- [Chinese Knowledge Base Index](../zh/README.md)",
            "",
        ]
    for folder in CATEGORY_ORDER:
        lines.append(f"- [{CATEGORY_META[folder]['en']}](#{CATEGORY_META[folder]['en'].lower().replace(' ', '-').replace(',', '').replace('/', '').replace('--', '-')})")
    lines.append("")
    for folder in CATEGORY_ORDER:
        meta = CATEGORY_META[folder]
        lines.append(f"## {meta['en']}")
        lines.append("")
        lines.append(meta["intro_en"])
        lines.append("")
        for card in groups[folder]:
            lines.append(entry_line_en(card, root=root))
        lines.append("")
    return "\n".join(lines).strip() + "\n"


def build_index_zh(cards: List[Card], root: bool) -> str:
    groups: Dict[str, List[Card]] = {folder: [] for folder in CATEGORY_ORDER}
    for card in cards:
        groups[card.folder].append(card)
    total = len(cards)
    nav = ROOT_NAV_ZH if root else KB_NAV_ZH
    if root:
        lines = [
            "# ForgetMeNot 中文索引",
            "",
            "> 一个系统收集各类 LLM memory benchmark 的仓库。",
            "",
            '<p align="center">',
            '  <img src="./assets/cover.svg" alt="ForgetMeNot cover" width="100%">',
            "</p>",
            "",
            '<p align="center">',
            "  <strong>一个面向 LLM memory benchmark 的双语知识库。</strong><br/>",
            "  覆盖长上下文理解、对话记忆、agent memory、RAG、持续学习与多模态长程推理。",
            "</p>",
            "",
            nav,
            "",
            f"当前版本共收录 **{total}** 份 benchmark 卡片，覆盖 **{len(CATEGORY_ORDER)}** 个大类，并提供中英文双语入口。",
            "",
            "> [!NOTE]",
            "> 默认入口是英文首页；如果你更希望先看中文整理版，请直接从本页或 `knowledge_base/zh/README.md` 开始。",
            "",
            "## 为什么用 ForgetMeNot",
            "",
            "- 它不是简单罗列论文，而是按 memory-oriented research question 组织 benchmark。",
            "- 它提供默认英文导航与中文精细整理并行的双语阅读路径。",
            "- 每个 benchmark 都对应一张结构化卡片，集中给出简介、链接与完整 BibTeX。",
            "",
            "## 快速概览",
            "",
            "| 字段 | 内容 |",
            "|---|---|",
            f"| Benchmark 卡片数 | {total} |",
            f"| 分类数 | {len(CATEGORY_ORDER)} |",
            "| 默认入口 | `README.md` |",
            "| 中文镜像 | `README_zh.md` 与 `knowledge_base/zh/` |",
            "| 贡献说明 | `CONTRIBUTING.md` |",
            "| 引用文件 | `CITATION.cff` |",
            "",
            "## 覆盖概览",
            "",
            "| 大类 | 数量 | 说明 |",
            "|---|---:|---|",
        ]
        for folder in CATEGORY_ORDER:
            meta = CATEGORY_META[folder]
            lines.append(
                f"| {meta['zh']} | {len(groups[folder])} | {meta['intro_zh']} |"
            )
        lines.extend(
            [
                "",
                "## 阅读路径",
                "",
                "1. **先看综述入口**：从下面的大类索引进入，再打开最相关的英文 benchmark 卡片。",
                "2. **先看中文整理**：直接去 `README_zh.md` 或 `knowledge_base/zh/README.md` 看中文说明与索引。",
                "3. **回到源材料核对**：通过卡片中的 paper / repo / homepage 链接回到原始来源，并查看完整 BibTeX。",
                "",
                "## 仓库结构",
                "",
                "- `README.md`：英文首页与总索引。",
                "- `README_zh.md`：中文首页与总索引。",
                "- `assets/cover.svg`：仓库封面图。",
                "- `knowledge_base/en/`：英文 benchmark 卡片。",
                "- `knowledge_base/zh/`：中文 benchmark 卡片。",
                "- `source_catalog/`：用于重建双语知识库的内部结构化源卡片。",
                "- `scripts/build_benchmark_catalog.py`：结构化 benchmark 源目录生成脚本。",
                "- `scripts/build_bilingual_repo.py`：双语首页与卡片生成脚本。",
                "",
                "## 目录",
                "",
            ]
        )
    else:
        lines = [
            "# ForgetMeNot 中文知识库",
            "",
            nav,
            "",
            "这个中文索引与仓库首页对应，提供所有 benchmark 中文卡片的统一入口。",
            "",
            f"当前版本共收录 **{total}** 份 benchmark 卡片，覆盖 **{len(CATEGORY_ORDER)}** 个大类，并提供中英文双语卡片。",
            "",
            "> [!NOTE]",
            "> 如果你想看仓库级的英文展示页，请回到 `../../README.md`。",
            "",
            "## 导航",
            "",
            "- [仓库首页](../../README_zh.md)",
            "- [English Knowledge Base Index](../en/README.md)",
            "",
        ]
    for folder in CATEGORY_ORDER:
        lines.append(f"- [{CATEGORY_META[folder]['zh']}](#{CATEGORY_META[folder]['zh']})")
    lines.append("")
    for folder in CATEGORY_ORDER:
        meta = CATEGORY_META[folder]
        lines.append(f"## {meta['zh']}")
        lines.append("")
        lines.append(meta["intro_zh"])
        lines.append("")
        for card in groups[folder]:
            lines.append(entry_line_zh(card, root=root))
        lines.append("")
    return "\n".join(lines).strip() + "\n"


def main() -> None:
    cards = load_cards()
    KB_ROOT.mkdir(parents=True, exist_ok=True)
    for folder in CATEGORY_ORDER:
        (KB_ROOT / "en" / folder).mkdir(parents=True, exist_ok=True)
        (KB_ROOT / "zh" / folder).mkdir(parents=True, exist_ok=True)

    for card in cards:
        write_card_zh(card)
        write_card_en(card)

    (ROOT / "README.md").write_text(build_index_en(cards, root=True))
    (ROOT / "README_zh.md").write_text(build_index_zh(cards, root=True))
    (KB_ROOT / "en" / "README.md").write_text(build_index_en(cards, root=False))
    (KB_ROOT / "zh" / "README.md").write_text(build_index_zh(cards, root=False))


if __name__ == "__main__":
    main()
