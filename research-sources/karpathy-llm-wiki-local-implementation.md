---
name: "Local LLM Wiki with Obsidian (Karpathy Implementation)"
source_type: Video
status: Done
key_takeaways: "Concrete local implementation of Karpathy's LLM wiki using Ollama (Gemma 4) + LangChain + Obsidian. Multi-view wiki generation: index (broad summary), topic-based, entity-based, and source-based views. Chrome Clipper for article ingestion into clippings/ folder. Obsidian graph view for knowledge navigation."
relevance: Medium
added_by: Nick
tags:
  - context-engineering
  - memory
  - vault-architecture
url: "https://www.youtube.com/watch?v=l4EzuMKmeA0"
authority:
  - nanny-youtube.md
findings:
  - karpathy-llm-knowledge-base-obsidian-rag.md
  - dual-ingestion-funnel-human-clip-plus-llm-research.md
date_added: "2026-04-20"
date_processed: "2026-04-20"
---
# Local LLM Wiki with Obsidian (Karpathy Implementation)

Tutorial by "Nanny" implementing Karpathy's LLM wiki concept entirely locally using Ollama + LangChain + Obsidian. Key implementation details:

- **Ingestion:** Chrome Clipper extension saves articles to Obsidian `clippings/` folder with metadata (author, date, source, title, full text)
- **Processing:** LLM (Gemma 4 via Ollama) analyzes each article: extracts summary, key points, topics (broad), and entities (specific: persons, companies, countries). Structured JSON output.
- **Wiki generation:** Four view types — index.md (broad summary + links to topics/entities), topic pages (grouped articles by theme), entity pages (grouped by author/company), source pages (per-article detail)
- **Deduplication:** Topics and entities merged across articles — if two articles share "learning" topic, one page created with links to both
- **Graph view:** Obsidian's graph view visualizes connections between topics, entities, and sources
- **Limitation acknowledged:** Static (full regeneration), not incremental as Karpathy envisioned. Author notes incremental update is an easy extension.

Pass 2 deep extraction completed from manually-provided transcript.
