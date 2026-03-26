from __future__ import annotations

import re
import textwrap
import unicodedata
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import requests
from bs4 import BeautifulSoup


ROOT = Path(__file__).resolve().parents[1]
REPORT_PATH = ROOT / "source_materials" / "benchmark_research_input.md"
OUT_ROOT = ROOT / "source_catalog"


SECTION_META = {
    "长上下文理解与推理": {
        "category": "长上下文理解与推理",
        "subcategory": "综合评测与真实任务",
        "memory_type": "Working / In-Context",
        "folder": "01_long_context",
        "category_intro": "这组 benchmark 关注模型在超长文本、代码仓库、长对话历史或结构化长输入中的定位、综合、推理与生成能力，强调“给定长上下文内的工作记忆”。",
    },
    "长上下文“针类”检索与诊断": {
        "category": "长上下文针类诊断",
        "subcategory": "Needle / Passkey / 合成诊断",
        "memory_type": "Working / In-Context",
        "folder": "02_needle_and_diagnostics",
        "category_intro": "这组 benchmark 倾向于用可控合成任务诊断“是否真的找到了长上下文中的关键信息”，适合做最低层的长上下文检索与注意力压力测试。",
    },
    "长上下文检索、RAG 与“外部记忆”": {
        "category": "检索、Embedding 与 RAG",
        "subcategory": "Retriever / RAG / External Memory",
        "memory_type": "Semantic / Retrieval-Augmented",
        "folder": "03_retrieval_rag",
        "category_intro": "这组 benchmark 将外部知识库、索引或 retriever 视为可写可读的语义记忆，重点评价检索质量、生成忠实性以及长文档表示学习能力。",
    },
    "多会话对话记忆与个性化": {
        "category": "多会话对话记忆与个性化",
        "subcategory": "Dialogue / Episodic / Personalization",
        "memory_type": "Episodic / Multi-Session",
        "folder": "04_dialogue_memory",
        "category_intro": "这组 benchmark 关注跨会话对话、长期用户画像和真实交互轨迹中的情景记忆，核心问题是“模型能否在时间维度上保留并正确调用过往信息”。",
    },
    "智能体记忆、长视野与持续学习": {
        "category": "智能体记忆与持续学习",
        "subcategory": "Agentic Memory / Continual Learning",
        "memory_type": "Agentic / Procedural / Continual",
        "folder": "05_agent_memory",
        "category_intro": "这组 benchmark 将 memory 放到 agent 任务、环境交互和持续学习场景里考察，不只看检索命中，还看行动成功率、效率与长期行为适配。",
    },
    "知识编辑与“语义记忆更新”评测": {
        "category": "知识编辑与语义记忆更新",
        "subcategory": "Model Editing / Knowledge Update",
        "memory_type": "Semantic Memory Update",
        "folder": "06_knowledge_editing",
        "category_intro": "这组 benchmark 用于测试模型或外部记忆在写入新事实之后，是否能实现正确回忆、局部更新、泛化传播与一致性保持。",
    },
    "多模态长程记忆与检索-推理": {
        "category": "多模态长程记忆与检索推理",
        "subcategory": "Document / Image / Video Long-Horizon",
        "memory_type": "Multimodal Long-Horizon",
        "folder": "07_multimodal",
        "category_intro": "这组 benchmark 将长程记忆问题扩展到 PDF、图像池和长视频，重点挑战通常不在单步推理，而在大规模跨模态证据池中的定位与整合。",
    },
}


SLUG_OVERRIDES = {
    "LongBench": "longbench",
    "LongBench-E": "longbench-e",
    "LongBench v2": "longbench-v2",
    "LongBench Pro": "longbench-pro",
    "L-Eval": "l-eval",
    "Ada-LEval": "ada-leval",
    "LooGLE": "loogle",
    "LooGLE v2": "loogle-v2",
    "∞Bench": "infinitebench",
    "RULER": "ruler",
    "SCROLLS": "scrolls",
    "ZeroSCROLLS": "zeroscrolls",
    "BAMBOO": "bamboo",
    "Loong": "loong",
    "LongBioBench": "longbiobench",
    "Ref-Long": "ref-long",
    "L-CiteEval": "l-citeeval",
    "AcademicEval": "academiceval",
    "Needle-in-a-Haystack": "niah",
    "Passkey Retrieval": "passkey-retrieval",
    "NeedleBench": "needlebench",
    "BABILong": "babilong",
    "MRCR": "mrcr",
    "GraphWalks": "graphwalks",
    "Phonebook": "phonebook",
    "LoCoV1": "locov1",
    "LongEmbed": "longembed",
    "LMEB": "lmeb",
    "BEIR": "beir",
    "KILT": "kilt",
    "MTEB": "mteb",
    "RAGBench": "ragbench",
    "T2-RAGBench": "t2-ragbench",
    "GraphRAG-Bench": "graphrag-bench",
    "LaRA": "lara",
    "RAGTruth": "ragtruth",
    "LoCoMo": "locomo",
    "LongMemEval": "longmemeval",
    "DialSim": "dialsim",
    "RealTalk": "realtalk",
    "PersonaMem": "personamem",
    "RealMem": "realmem",
    "Mem-Gallery": "mem-gallery",
    "LOCA-bench": "loca-bench",
    "AMA-Bench": "ama-bench",
    "MemBench": "membench",
    "MemoryArena": "memoryarena",
    "MemoryAgentBench": "memoryagentbench",
    "GoodAI LTM Benchmark": "goodai-ltm-benchmark",
    "LifelongAgentBench": "lifelongagentbench",
    "MemoryBench": "memorybench",
    "MemoryCD": "memorycd",
    "CoIN": "coin",
    "CLLE": "clle",
    "Rubric Feedback Bench": "rubric-feedback-bench",
    "MQuAKE": "mquake",
    "QAEdit + WILD": "qaeedit-wild",
    "CounterFact": "counterfact",
    "ZsRE": "zsre",
    "MMLongBench-Doc": "mmlongbench-doc",
    "MMNeedle": "mmneedle",
    "MM-NIAH": "mm-niah",
    "Visual Haystacks": "visual-haystacks",
    "DocHaystack": "dochaystack",
    "InfoHaystack": "infohaystack",
    "MultiHaystack": "multihaystack",
    "LongVideoBench": "longvideobench",
    "Video-MME": "video-mme",
    "Ego4D Episodic Memory": "ego4d-episodic-memory",
}


URL_KEY_MAP = {
    "paper": "paper_url",
    "paper(pdf)": "paper_pdf_url",
    "paper html": "paper_html_url",
    "acl pdf": "paper_pdf_url",
    "acl entry": "paper_url",
    "pmlr page": "paper_url",
    "openreview": "paper_url",
    "openreview pdf": "paper_pdf_url",
    "neurips page": "paper_url",
    "project": "project_url",
    "project page": "project_url",
    "intro blog": "project_url",
    "v3 release": "project_release_url",
    "github": "github_url",
    "code": "github_url",
    "code/dataset": "github_url",
    "dataset": "dataset_url",
    "hf dataset": "dataset_url",
    "dataset page": "dataset_url",
    "hf collection": "dataset_url",
    "repo": "github_url",
    "benchmark overview": "project_url",
    "episodic memory page": "project_url_2",
    "dataset main site": "dataset_url",
    "lm-eval task doc": "project_url",
    "lm-eval task doc (longbench-e description)": "project_url",
    "opencompass doc (niah eval)": "project_url",
    "reference implementation (github)": "github_url",
}


OVERRIDES = {
    "LongBench v2": {
        "paper_url": "https://arxiv.org/abs/2412.15204",
        "dataset_url": "https://huggingface.co/datasets/zai-org/LongBench-v2",
    },
    "LongBench-E": {
        "source_kind": "variant-doc",
    },
    "T2-RAGBench": {
        "paper_url": "https://arxiv.org/abs/2506.12071",
    },
    "LoCoMo": {
        "paper_url": "https://arxiv.org/abs/2402.17753",
        "paper_pdf_url": "https://aclanthology.org/2024.acl-long.747.pdf",
        "project_url": "https://snap-research.github.io/locomo/",
        "github_url": "https://github.com/snap-research/LoCoMo",
        "note": "原报告中的 arXiv 链接指向了无关论文，已按 benchmark 标题校正为 LoCoMo 官方论文。",
    },
    "RealTalk": {
        "paper_url": "https://arxiv.org/abs/2502.13270",
        "github_url": "https://github.com/danny911kr/REALTALK",
        "note": "原报告中的 arXiv 与 GitHub 链接均与 benchmark 不一致，这里改为与 REALTALK 论文标题一致的官方资源。",
    },
    "PersonaMem": {
        "paper_url": "https://arxiv.org/abs/2504.14225",
        "github_url": "https://github.com/bowen-upenn/PersonaMem",
        "project_url": "https://zhuoqunhao.github.io/PersonaMem.github.io/",
        "note": "原报告仅给出 OpenReview 链接；这里补充了可直接抓取 abstract 与 BibTeX 的 arXiv 版本及官方代码页。",
    },
    "RealMem": {
        "paper_url": "https://arxiv.org/abs/2601.06966",
        "github_url": "https://github.com/AvatarMemory/RealMemBench",
        "note": "原报告中的 arXiv 链接有误，已替换为标题匹配的 RealMem 论文。",
    },
    "Mem-Gallery": {
        "paper_url": "https://arxiv.org/abs/2601.03515",
        "github_url": "https://github.com/YuanchenBei/Mem-Gallery",
        "note": "原报告中的 arXiv 链接有误，已替换为 Mem-Gallery 官方论文。",
    },
    "MemoryArena": {
        "paper_url": "https://arxiv.org/abs/2602.16313",
        "project_url": "https://memoryarena.github.io/",
        "note": "原报告中的 arXiv 链接有误，已替换为 MemoryArena 官方论文。",
    },
    "MemoryAgentBench": {
        "github_url": "https://github.com/HUST-AI-HYZ/MemoryAgentBench",
        "dataset_url": "https://huggingface.co/datasets/ai-hyz/MemoryAgentBench",
    },
    "GoodAI LTM Benchmark": {
        "paper_url": "https://arxiv.org/abs/2409.20222",
        "paper_pdf_url": "https://papers.neurips.cc/paper_files/paper/2024/file/4aedf0cba303537fcb6cf948bb41b2df-Paper-Datasets_and_Benchmarks_Track.pdf",
    },
    "MemoryCD": {
        "source_kind": "openreview-listing",
    },
    "GraphWalks": {
        "source_kind": "dataset-only",
    },
    "Needle-in-a-Haystack": {
        "source_kind": "repo-only",
    },
    "Phonebook": {
        "source_kind": "task-family",
    },
    "Ego4D Episodic Memory": {
        "source_kind": "official-benchmark-page",
    },
}


MANUAL_META = {
    "LongBench-E": {
        "paper_title": "LongBench-E: Uniform-Length Variant for LongBench in lm-evaluation-harness",
        "year": "2025",
        "abstract": "",
        "bibtex": textwrap.dedent(
            """\
            @misc{longbench_e_lm_eval,
              title = {LongBench-E: Uniform-Length Variant for LongBench in lm-evaluation-harness},
              author = {{EleutherAI}},
              howpublished = {GitHub documentation},
              year = {2025},
              url = {https://github.com/EleutherAI/lm-evaluation-harness/blob/main/lm_eval/tasks/longbench/README.md},
              note = {LongBench-E is documented as the uniform-length evaluation variant of LongBench in lm-evaluation-harness.}
            }"""
        ),
        "note": "LongBench-E 更像 LongBench 的长度分布变体说明，而不是单独发表的 benchmark 论文；因此这里以 lm-evaluation-harness 官方任务文档作为可引用来源。",
    },
    "Needle-in-a-Haystack": {
        "paper_title": "Needle In A Haystack - Pressure Testing LLMs",
        "year": "2024",
        "abstract": "",
        "bibtex": textwrap.dedent(
            """\
            @misc{kamradt2024needlehaystack,
              title = {Needle In A Haystack - Pressure Testing LLMs},
              author = {Greg Kamradt},
              howpublished = {GitHub repository},
              year = {2024},
              url = {https://github.com/gkamradt/LLMTest_NeedleInAHaystack},
              note = {Reference implementation widely used for long-context needle-in-a-haystack evaluation.}
            }"""
        ),
        "note": "NIAH 在当前文献里更多是一套测试方法与实现范式，而非单一正式论文 benchmark；因此这里采用官方 GitHub 实现作为主引用。",
    },
    "GraphWalks": {
        "paper_title": "GraphWalks: Long-Context Graph Reasoning Dataset",
        "year": "2025",
        "abstract": "",
        "bibtex": textwrap.dedent(
            """\
            @misc{openai2025graphwalks,
              title = {GraphWalks: Long-Context Graph Reasoning Dataset},
              author = {{OpenAI}},
              howpublished = {Hugging Face dataset card},
              year = {2025},
              url = {https://huggingface.co/datasets/openai/graphwalks},
              note = {Official dataset release for edge-list based long-context graph reasoning evaluation.}
            }"""
        ),
        "note": "GraphWalks 在原报告中以官方数据集形式出现，未给出独立论文；这里以数据集卡片作为主来源。",
    },
    "Phonebook": {
        "paper_title": "An Empirical Study of Mamba-based Language Models",
        "year": "2024",
        "abstract": "",
        "bibtex": "",
        "note": "Phonebook 更接近一类被多篇长上下文论文复用的任务家族，而不是单独命名发表的 benchmark 论文。这里沿用报告中的代表性论文与数据集集合来说明其标准设定。",
    },
    "MemoryCD": {
        "paper_title": "MemoryCD: Benchmarking Long-Context User Memory of LLM Agents for Lifelong Cross-Domain Personalization",
        "year": "2026",
        "abstract": "",
        "bibtex": textwrap.dedent(
            """\
            @inproceedings{zhang2026memorycd,
              title = {MemoryCD: Benchmarking Long-Context User Memory of LLM Agents for Lifelong Cross-Domain Personalization},
              author = {Weizhi Zhang and Xiaokai Wei and Wei-Chieh Huang and Zheng Hui and Chen Wang and Michelle Gong and Philip S. Yu},
              booktitle = {ICLR 2026 Workshop on Lifelong Learning Agents},
              year = {2026},
              url = {https://openreview.net/forum?id=Lpq4aEqvmg},
              note = {Metadata reconstructed from the OpenReview workshop listing because the forum page did not expose machine-readable metadata to the current crawler.}
            }"""
        ),
        "note": "OpenReview 页面当前拒绝直接抓取，作者、标题与年份来自检索结果中的 OpenReview 官方列表页；abstract 未能可靠抓取，因此本卡片只保留中文概述。",
    },
    "Ego4D Episodic Memory": {
        "paper_title": "Ego4D Episodic Memory Benchmark",
        "year": "2021",
        "abstract": "",
        "bibtex": textwrap.dedent(
            """\
            @misc{ego4d2021episodicmemory,
              title = {Ego4D Episodic Memory Benchmark},
              author = {{Ego4D Consortium}},
              year = {2021},
              url = {https://ego4d-data.org/docs/benchmarks/episodic-memory/},
              note = {Official benchmark documentation for the Ego4D episodic memory task.}
            }"""
        ),
        "note": "Ego4D Episodic Memory 在原报告中以官方 benchmark 文档和 repo 的形式出现，而不是单篇定义论文；因此这里以官方 benchmark 页面作为主引用来源。",
    },
}


SEARCH_OVERRIDES = {
    "GoodAI LTM Benchmark": "GoodAI LTM Benchmark arxiv",
    "PersonaMem": "PersonaMem benchmark arxiv",
    "MemoryCD": "\"MemoryCD\" benchmark",
    "LongBench v2": "LongBench v2 arxiv",
    "LoCoMo": "LoCoMo long conversation memory arxiv",
    "RealTalk": "RealTalk benchmark arxiv",
    "RealMem": "RealMem benchmark github long-term memory",
    "Mem-Gallery": "Mem-Gallery benchmark arxiv",
    "MemoryArena": "MemoryArena benchmark arxiv",
}


@dataclass
class BenchmarkEntry:
    name: str
    section: str
    body: str
    raw_urls: Dict[str, str]
    category: str = ""
    subcategory: str = ""
    memory_type: str = ""
    folder: str = ""
    category_intro: str = ""
    slug: str = ""
    urls: Dict[str, str] = field(default_factory=dict)
    note: str = ""


def clean_text(text: str) -> str:
    text = re.sub(r"cite.*?", "", text, flags=re.S)
    text = re.sub(r"entity.*?", "", text, flags=re.S)
    text = text.replace("**", "")
    text = re.sub(r"\s+\n", "\n", text)
    text = re.sub(r"\n{2,}", "\n", text)
    return text.strip()


def parse_report() -> List[BenchmarkEntry]:
    lines = REPORT_PATH.read_text().splitlines()
    entries: List[BenchmarkEntry] = []
    current_section = None
    i = 0
    while i < len(lines):
        line = lines[i]
        m_sec = re.match(r"^###\s+(.+)$", line)
        if m_sec:
            current_section = m_sec.group(1).strip()
            i += 1
            continue
        m = re.match(r"^\*\*(.+?)\*\*\s*$", line)
        if m and not any(x in m.group(1) for x in ["清晰结论", "置信度", "关键注意事项"]):
            title = m.group(1).strip()
            body_lines: List[str] = []
            code_lines: List[str] = []
            in_code = False
            j = i + 1
            while j < len(lines):
                next_line = lines[j]
                if re.match(r"^##\s+.+$", next_line):
                    break
                if re.match(r"^###\s+(.+)$", next_line):
                    break
                m2 = re.match(r"^\*\*(.+?)\*\*\s*$", next_line)
                if m2 and not any(x in m2.group(1) for x in ["清晰结论", "置信度", "关键注意事项"]):
                    break
                if next_line.startswith("```"):
                    in_code = not in_code
                    j += 1
                    continue
                if in_code:
                    code_lines.append(next_line)
                else:
                    body_lines.append(next_line)
                j += 1
            raw_urls = {}
            for code in code_lines:
                if ": " in code:
                    label, url = code.split(": ", 1)
                    raw_urls[label.strip()] = url.strip()
            body = clean_text("\n".join([line for line in body_lines if line.strip()]))
            entries.extend(expand_entry(title, current_section or "", body, raw_urls))
            i = j
            continue
        i += 1
    return entries


def expand_entry(title: str, section: str, body: str, raw_urls: Dict[str, str]) -> List[BenchmarkEntry]:
    def base(name: str, entry_body: str, entry_urls: Dict[str, str]) -> BenchmarkEntry:
        meta = SECTION_META[section]
        return BenchmarkEntry(
            name=name,
            section=section,
            body=clean_text(entry_body),
            raw_urls=entry_urls.copy(),
            category=meta["category"],
            subcategory=meta["subcategory"],
            memory_type=meta["memory_type"],
            folder=meta["folder"],
            category_intro=meta["category_intro"],
            slug=SLUG_OVERRIDES[name],
        )

    if title.startswith("SCROLLS（"):
        return [
            base(
                "SCROLLS",
                "SCROLLS：7 个长文本任务/多域（摘要、QA、NLI 等），目标是“需要在长文本中综合信息”。",
                {
                    "SCROLLS site": raw_urls.get("SCROLLS site", ""),
                    "SCROLLS paper (EMNLP 2022)": raw_urls.get("SCROLLS paper (EMNLP 2022)", ""),
                },
            ),
            base(
                "ZeroSCROLLS",
                "ZeroSCROLLS：从 SCROLLS 选 6 个任务并新增 4 个数据集，仅保留 test 与极小验证集，主要面向 zero-shot 长文本评测。",
                {
                    "ZeroSCROLLS paper": raw_urls.get("ZeroSCROLLS paper", ""),
                    "ZeroSCROLLS HF": raw_urls.get("ZeroSCROLLS HF", ""),
                },
            ),
        ]
    if title.startswith("BEIR / KILT / MTEB"):
        return [
            base(
                "BEIR",
                "BEIR：18 个数据集构成异质检索 benchmark，强调 zero-shot / OOD 泛化评测。",
                {"BEIR paper": raw_urls.get("BEIR paper", ""), "BEIR GitHub": raw_urls.get("BEIR GitHub", "")},
            ),
            base(
                "KILT",
                "KILT：把多个知识密集任务统一到同一份 Wikipedia 快照，并联合评估答案质量与 provenance。",
                {"KILT paper": raw_urls.get("KILT paper", ""), "KILT GitHub": raw_urls.get("KILT GitHub", "")},
            ),
            base(
                "MTEB",
                "MTEB：大规模 embedding benchmark，覆盖 58 个数据集、8 类任务和 112 种语言，常被用作通用检索与表征能力对照。",
                {"MTEB paper": raw_urls.get("MTEB paper", ""), "MTEB GitHub & leaderboard": raw_urls.get("MTEB GitHub & leaderboard", "")},
            ),
        ]
    if title.startswith("DocHaystack / InfoHaystack"):
        shared = "既有多图 QA 候选集合过小，不足以代表真实检索，因此该工作提出可扩展到 1,000 视觉文档的检索与理解基准，并报告 recall@1 等检索指标。"
        return [
            base("DocHaystack", shared, {"Paper": raw_urls.get("Paper", ""), "GitHub": raw_urls.get("GitHub", "")}),
            base("InfoHaystack", shared, {"Paper": raw_urls.get("Paper", ""), "GitHub": raw_urls.get("GitHub", "")}),
        ]

    name = re.split(r"[（(]", title)[0].strip()
    name = (
        name.replace("‑", "-")
        .replace("–", "-")
        .replace("—", "-")
        .replace("T²", "T2")
        .replace("MM‑", "MM-")
        .replace("L‑", "L-")
        .replace("Ada‑", "Ada-")
        .replace("Ref‑", "Ref-")
        .replace("LOCA‑", "LOCA-")
        .replace("AMA‑", "AMA-")
        .replace("Mem‑", "Mem-")
        .replace("Video‑", "Video-")
    )
    if name not in SLUG_OVERRIDES:
        raise KeyError(f"Missing slug override for {name}")
    return [base(name, body, raw_urls)]


def pick_url_key(label: str) -> str:
    label_norm = label.lower().strip()
    label_norm = label_norm.replace("（", "(").replace("）", ")")
    if label_norm in URL_KEY_MAP:
        return URL_KEY_MAP[label_norm]
    for key, value in URL_KEY_MAP.items():
        if key in label_norm:
            return value
    return f"other_{slugify(label_norm)}_url"


def slugify(text: str) -> str:
    text = unicodedata.normalize("NFKD", text)
    text = text.encode("ascii", "ignore").decode("ascii")
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-") or "item"


def normalize_urls(entry: BenchmarkEntry) -> None:
    urls: Dict[str, str] = {}
    for label, url in entry.raw_urls.items():
        if not url:
            continue
        key = pick_url_key(label)
        if key in urls and urls[key] != url:
            key = f"{key}_{len([k for k in urls if k.startswith(key)]) + 1}"
        urls[key] = url
    for key, value in OVERRIDES.get(entry.name, {}).items():
        if key.endswith("_url"):
            urls[key] = value
    entry.urls = urls
    note = OVERRIDES.get(entry.name, {}).get("note")
    if note:
        entry.note = note


def ddg_search(query: str, max_results: int = 5) -> List[Dict[str, str]]:
    session = requests.Session()
    session.headers.update({"User-Agent": "Mozilla/5.0"})
    resp = session.get(
        "https://duckduckgo.com/html/",
        params={"q": query},
        timeout=30,
    )
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")
    results: List[Dict[str, str]] = []
    for result in soup.select(".result")[:max_results]:
        a = result.select_one(".result__title a")
        snippet = result.select_one(".result__snippet")
        if not a:
            continue
        href = a.get("href", "").replace("//duckduckgo.com/l/?uddg=", "")
        href = requests.utils.unquote(href.split("&rut=", 1)[0])
        results.append(
            {
                "title": a.get_text(" ", strip=True),
                "url": href,
                "snippet": snippet.get_text(" ", strip=True) if snippet else "",
            }
        )
    return results


def maybe_fill_missing_urls(entry: BenchmarkEntry) -> None:
    source_kind = OVERRIDES.get(entry.name, {}).get("source_kind", "")
    if source_kind in {"variant-doc", "dataset-only", "repo-only", "official-benchmark-page"}:
        return
    if entry.urls.get("paper_url"):
        return
    query = SEARCH_OVERRIDES.get(entry.name, f"{entry.name} benchmark arxiv")
    for result in ddg_search(query):
        url = result["url"]
        if any(host in url for host in ["arxiv.org/abs/", "aclanthology.org/", "proceedings.mlr.press/", "openreview.net/forum"]):
            entry.urls["paper_url"] = url
            if not entry.note and result["snippet"]:
                entry.note = f"主论文链接通过检索补齐：{result['title']}"
            break


def fetch_meta_tag_map(html: str) -> Dict[str, str]:
    soup = BeautifulSoup(html, "html.parser")
    meta: Dict[str, str] = {}
    for tag in soup.find_all("meta"):
        key = tag.get("name") or tag.get("property")
        value = tag.get("content")
        if key and value:
            meta[key] = value
    return meta


def fetch_arxiv(url: str, session: requests.Session) -> Dict[str, str]:
    resp = session.get(url, timeout=30)
    resp.raise_for_status()
    meta = fetch_meta_tag_map(resp.text)
    paper_title = meta.get("citation_title", "")
    authors = [m.get("content") for m in BeautifulSoup(resp.text, "html.parser").find_all("meta", attrs={"name": "citation_author"}) if m.get("content")]
    year = ""
    if meta.get("citation_online_date"):
        year = meta["citation_online_date"][:4]
    elif meta.get("citation_date"):
        year = meta["citation_date"][:4]
    else:
        m_year = re.search(r"/abs/(\d{2})(\d{2})\.\d+", url)
        if m_year:
            year = f"20{m_year.group(1)}"
    abstract = meta.get("citation_abstract", "") or meta.get("og:description", "")
    arxiv_id = re.search(r"/abs/([^/?#]+)", url)
    bibtex = ""
    if arxiv_id:
        doi_url = f"https://doi.org/10.48550/arXiv.{arxiv_id.group(1)}"
        bib = session.get(doi_url, headers={"Accept": "application/x-bibtex"}, timeout=30)
        if bib.ok and bib.text.lstrip().startswith("@"):
            bibtex = bib.text.strip()
    return {"paper_title": paper_title, "authors": ", ".join(authors), "year": year, "abstract": abstract.strip(), "bibtex": bibtex}


def fetch_acl(url: str, session: requests.Session) -> Dict[str, str]:
    url = url[:-4] if url.endswith(".pdf") else url
    resp = session.get(url, timeout=30)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")
    meta = fetch_meta_tag_map(resp.text)
    abstract_node = soup.select_one("div.card-body.acl-abstract")
    bib_node = soup.select_one("#citeBibtexContent")
    authors = [m.get("content") for m in soup.find_all("meta", attrs={"name": "citation_author"}) if m.get("content")]
    year = (meta.get("citation_publication_date", "") or "")[:4]
    return {
        "paper_title": meta.get("citation_title", "") or meta.get("og:title", ""),
        "authors": ", ".join(authors),
        "year": year,
        "abstract": abstract_node.get_text(" ", strip=True).replace("Abstract ", "", 1) if abstract_node else "",
        "bibtex": bib_node.get_text("\n", strip=True) if bib_node else "",
    }


def fetch_pmlr(url: str, session: requests.Session) -> Dict[str, str]:
    resp = session.get(url, timeout=30)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")
    meta = fetch_meta_tag_map(resp.text)
    abstract_node = soup.select_one("div#abstract")
    bib_node = soup.select_one("code#bibtex")
    authors = [m.get("content") for m in soup.find_all("meta", attrs={"name": "citation_author"}) if m.get("content")]
    year = (meta.get("citation_publication_date", "") or "")[:4]
    return {
        "paper_title": meta.get("citation_title", "") or meta.get("og:title", ""),
        "authors": ", ".join(authors),
        "year": year,
        "abstract": abstract_node.get_text(" ", strip=True) if abstract_node else meta.get("og:description", ""),
        "bibtex": bib_node.get_text("\n", strip=True) if bib_node else "",
    }


def fetch_generic(url: str, session: requests.Session) -> Dict[str, str]:
    resp = session.get(url, timeout=30)
    resp.raise_for_status()
    meta = fetch_meta_tag_map(resp.text)
    title = meta.get("og:title") or meta.get("twitter:title") or ""
    desc = meta.get("og:description") or meta.get("description") or meta.get("twitter:description") or ""
    soup = BeautifulSoup(resp.text, "html.parser")
    if not title and soup.title:
        title = soup.title.get_text(" ", strip=True)
    return {"paper_title": title, "authors": "", "year": "", "abstract": desc, "bibtex": ""}


def synthesize_misc_bibtex(title: str, url: str, year: str, author: str, note: str, key: str) -> str:
    author = author or "{{Unknown}}"
    year = year or "n.d."
    note_line = f"\n  note = {{{note}}}," if note else ""
    return textwrap.dedent(
        f"""\
        @misc{{{key},
          title = {{{title}}},
          author = {{{author}}},
          year = {{{year}}},
          url = {{{url}}},{note_line}
        }}"""
    ).strip()


def fetch_metadata(entry: BenchmarkEntry, session: requests.Session) -> Dict[str, str]:
    manual = MANUAL_META.get(entry.name, {})
    source_kind = OVERRIDES.get(entry.name, {}).get("source_kind", "paper")
    primary_url = get_primary_source_url(entry)
    meta = {"paper_title": "", "authors": "", "year": "", "abstract": "", "bibtex": ""}

    if primary_url:
        try:
            if "arxiv.org/abs/" in primary_url:
                meta = fetch_arxiv(primary_url, session)
            elif "aclanthology.org/" in primary_url:
                meta = fetch_acl(primary_url, session)
            elif "proceedings.mlr.press/" in primary_url:
                meta = fetch_pmlr(primary_url, session)
            else:
                meta = fetch_generic(primary_url, session)
        except Exception:
            meta = {"paper_title": "", "authors": "", "year": "", "abstract": "", "bibtex": ""}

    force_manual = source_kind in {"variant-doc", "dataset-only", "repo-only", "task-family", "openreview-listing", "official-benchmark-page"}
    for key, value in manual.items():
        if not value:
            continue
        if force_manual and key in {"paper_title", "year", "abstract", "bibtex"}:
            meta[key] = value
        elif not meta.get(key):
            meta[key] = value

    if not meta.get("paper_title"):
        meta["paper_title"] = entry.name
    if not meta.get("year"):
        m = re.search(r"(20\d{2})", entry.body)
        meta["year"] = m.group(1) if m else manual.get("year", "")
    if not meta.get("abstract"):
        meta["abstract"] = manual.get("abstract", "")
    if not meta.get("bibtex"):
        if manual.get("bibtex"):
            meta["bibtex"] = manual["bibtex"]
        elif primary_url:
            title = meta["paper_title"]
            note = manual.get("note", "")
            author = meta.get("authors", "") or "{{Unknown}}"
            meta["bibtex"] = synthesize_misc_bibtex(title, primary_url, meta.get("year", ""), author, note, entry.slug)
    meta["source_kind"] = source_kind
    return meta


def url_rows(entry: BenchmarkEntry) -> List[Tuple[str, str]]:
    order = [
        "paper_url",
        "paper_pdf_url",
        "paper_html_url",
        "project_url",
        "project_url_2",
        "project_release_url",
        "github_url",
        "dataset_url",
    ]
    rows: List[Tuple[str, str]] = []
    for key in order:
        if entry.urls.get(key):
            rows.append((key, entry.urls[key]))
    for key, value in entry.urls.items():
        if key not in order and value:
            rows.append((key, value))
    return rows


def key_to_cn(key: str) -> str:
    mapping = {
        "paper_url": "论文页",
        "paper_pdf_url": "论文 PDF",
        "paper_html_url": "论文 HTML",
        "project_url": "项目主页",
        "project_url_2": "补充主页",
        "project_release_url": "版本发布页",
        "github_url": "GitHub",
        "dataset_url": "数据集页",
    }
    return mapping.get(key, key)


def infer_fine_subcategory(entry: BenchmarkEntry) -> str:
    name = entry.name
    if entry.category == "长上下文理解与推理":
        if "Cite" in name or "Ref-" in name:
            return "引用定位与忠实性"
        if name in {"RULER", "L-Eval", "Ada-LEval"}:
            return "诊断套件与标准化评测"
        return "长上下文综合任务"
    if entry.category == "长上下文针类诊断":
        if name in {"MRCR", "GraphWalks", "Phonebook"}:
            return "多针 / 结构化检索"
        return "Needle / Passkey / 合成诊断"
    if entry.category == "检索、Embedding 与 RAG":
        if name in {"BEIR", "KILT", "MTEB", "LoCoV1", "LongEmbed", "LMEB"}:
            return "检索与表示学习"
        return "端到端 RAG 与忠实性"
    if entry.category == "多会话对话记忆与个性化":
        if name in {"PersonaMem", "RealMem"}:
            return "个性化与真实多会话"
        return "长期对话记忆"
    if entry.category == "智能体记忆与持续学习":
        if name in {"CoIN", "CLLE", "Rubric Feedback Bench", "MemoryBench"}:
            return "持续学习与反馈记忆"
        return "Agentic memory benchmark"
    if entry.category == "知识编辑与语义记忆更新":
        return "知识编辑评测"
    if entry.category == "多模态长程记忆与检索推理":
        if name in {"MMLongBench-Doc", "DocHaystack", "InfoHaystack"}:
            return "长文档与视觉文档"
        if name in {"LongVideoBench", "Video-MME", "Ego4D Episodic Memory"}:
            return "视频长上下文"
        return "多图 / 多模态检索推理"
    return entry.subcategory


def build_card(entry: BenchmarkEntry, meta: Dict[str, str]) -> str:
    url_table = ["| 类型 | 链接 |", "|---|---|"]
    rows = url_rows(entry)
    if rows:
        for key, value in rows:
            url_table.append(f"| {key_to_cn(key)} | {value} |")
    else:
        url_table.append("| 官方链接 | （空） |")

    abstract_section = ""
    if meta.get("abstract"):
        abstract_section = "\n".join(
            [
                "## Abstract",
                "### 原始摘要",
                f"> {meta['abstract']}",
                "",
                "### 中文抽取",
                entry.body,
            ]
        ).strip()
    else:
        abstract_section = textwrap.dedent(
            f"""\
            ## Abstract
            未能从当前可访问的官方页面稳定抓取原始 abstract。以下中文说明来自原报告与官方资源描述的交叉整理：

            {entry.body}
            """
        ).strip()

    note_lines = []
    if entry.note:
        note_lines.append(f"- {entry.note}")
    if MANUAL_META.get(entry.name, {}).get("note"):
        note_lines.append(f"- {MANUAL_META[entry.name]['note']}")
    if not note_lines:
        note_lines.append("- 本卡片优先使用论文页、项目页与代码仓库等官方来源；若原报告中的链接存在错误，则以标题匹配后的官方链接为准。")

    frontmatter = textwrap.dedent(
        f"""\
        ---
        name: {entry.name}
        slug: {entry.slug}
        category: {entry.category}
        subcategory: {infer_fine_subcategory(entry)}
        memory_type: {entry.memory_type}
        year: "{meta.get('year', '')}"
        primary_source_kind: {meta.get('source_kind', 'paper')}
        primary_source_url: {get_primary_source_url(entry)}
        ---
        """
    ).strip()

    info_table = textwrap.dedent(
        f"""\
        | 字段 | 内容 |
        |---|---|
        | Benchmark | {entry.name} |
        | 分类 | {entry.category} |
        | 子类 | {infer_fine_subcategory(entry)} |
        | 记忆侧重 | {entry.memory_type} |
        | 首次年份 | {meta.get('year', '未注明') or '未注明'} |
        | 主要来源类型 | {meta.get('source_kind', 'paper')} |
        | 论文标题 | {meta.get('paper_title', entry.name)} |
        """
    ).strip()

    return "\n\n".join(
        [
            frontmatter,
            f"# {entry.name}",
            "## 结构化信息",
            info_table,
            "## 基础介绍",
            entry.body,
            abstract_section,
            "## URL 汇总",
            "\n".join(url_table),
            "## BibTeX",
            "```bibtex\n" + (meta.get("bibtex", "").strip() or "% 未获取到可用 BibTeX") + "\n```",
            "## 备注",
            "\n".join(note_lines),
        ]
    ).strip() + "\n"


def build_index(entries: List[BenchmarkEntry], meta_map: Dict[str, Dict[str, str]]) -> str:
    grouped: Dict[str, List[BenchmarkEntry]] = {}
    for entry in entries:
        grouped.setdefault(entry.category, []).append(entry)

    lines = [
        "# LLM Memory Benchmark 结构化目录",
        "",
        "本目录汇总了用于构建双语知识库的结构化 benchmark 源卡片，并补充了论文 abstract、官方链接、BibTeX 与分类说明。若早期研究素材中的链接与 benchmark 名称不一致，本目录会在对应卡片中显式说明并给出校正后的链接。",
        "",
        "## 分类原则",
        "",
        "- 长上下文理解与推理：评估模型在单轮超长输入中的定位、综合、推理与长生成能力。",
        "- 长上下文针类诊断：用可控合成任务压测 retrieval、needle 定位和注意力覆盖。",
        "- 检索、Embedding 与 RAG：把外部知识库与 retriever 视为语义记忆，评估检索质量与 RAG 忠实性。",
        "- 多会话对话记忆与个性化：关注跨会话用户事实、偏好、项目历史与个性化响应。",
        "- 智能体记忆与持续学习：关注 agent 在环境交互、任务迁移和反馈累积中的长期记忆能力。",
        "- 知识编辑与语义记忆更新：关注“写入新事实后是否能正确回忆并保持局部一致性”。",
        "- 多模态长程记忆与检索推理：关注 PDF、图像池与长视频中的跨模态长程证据定位与推理。",
        "",
        "## 总量统计",
        "",
        f"- Benchmark 卡片数：{len(entries)}",
        f"- 主类别数：{len(grouped)}",
        "",
    ]

    order = [v["category"] for v in SECTION_META.values()]
    seen = set()
    ordered_categories = []
    for item in order:
        if item not in seen:
            ordered_categories.append(item)
            seen.add(item)

    for category in ordered_categories:
        items = sorted(grouped.get(category, []), key=lambda e: e.name.lower())
        if not items:
            continue
        intro = items[0].category_intro
        lines.extend([f"## {category}", "", intro, ""])
        for entry in items:
            rel_path = f"{entry.folder}/{entry.slug}.md"
            title = meta_map[entry.slug].get("paper_title") or entry.name
            year = meta_map[entry.slug].get("year") or "未注明"
            lines.append(f"- [{entry.name}]({rel_path})：{infer_fine_subcategory(entry)}；主要论文题目为 `{title}`；首次年份 `{year}`。")
        lines.append("")

    return "\n".join(lines).strip() + "\n"


def main() -> None:
    if not REPORT_PATH.exists():
        raise FileNotFoundError(
            f"Missing external source report: {REPORT_PATH}. "
            "This public repository does not ship the private source material. "
            "If you need to rebuild `source_catalog/`, place the report at the path above first."
        )

    entries = parse_report()
    session = requests.Session()
    session.headers.update({"User-Agent": "Mozilla/5.0"})

    for entry in entries:
        normalize_urls(entry)
        maybe_fill_missing_urls(entry)

    meta_map: Dict[str, Dict[str, str]] = {}
    for entry in entries:
        meta_map[entry.slug] = fetch_metadata(entry, session)

    OUT_ROOT.mkdir(parents=True, exist_ok=True)
    for meta in SECTION_META.values():
        (OUT_ROOT / meta["folder"]).mkdir(parents=True, exist_ok=True)

    for entry in entries:
        card = build_card(entry, meta_map[entry.slug])
        out_path = OUT_ROOT / entry.folder / f"{entry.slug}.md"
        out_path.write_text(card)

    index = build_index(entries, meta_map)
    (OUT_ROOT / "README.md").write_text(index)


def get_primary_source_url(entry: BenchmarkEntry) -> str:
    source_kind = OVERRIDES.get(entry.name, {}).get("source_kind", "paper")
    if source_kind == "repo-only":
        return entry.urls.get("github_url") or entry.urls.get("project_url") or entry.urls.get("dataset_url") or ""
    if source_kind == "dataset-only":
        return entry.urls.get("dataset_url") or entry.urls.get("project_url") or entry.urls.get("github_url") or ""
    if source_kind == "variant-doc":
        return entry.urls.get("project_url") or entry.urls.get("github_url") or ""
    if source_kind == "official-benchmark-page":
        return entry.urls.get("project_url") or entry.urls.get("project_url_2") or entry.urls.get("github_url") or ""
    return entry.urls.get("paper_url") or entry.urls.get("project_url") or entry.urls.get("github_url") or entry.urls.get("dataset_url") or ""


if __name__ == "__main__":
    main()
