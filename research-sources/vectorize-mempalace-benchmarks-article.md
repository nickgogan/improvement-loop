---
name: "Vectorize — MemPalace Benchmarks Don't Withstand Scrutiny (third-party adjudication)"
source_type: "Blog Post / Article"
status: "Done"
date_processed: "2026-04-23"
key_takeaways: "Vectorize (vendor of Hindsight, itself a LongMemEval-ranked system, disclosed conflict-of-interest) publishes a critical third-party adjudication of MemPalace's headline claims. Three methodological issues surfaced: (1) METRIC MISMATCH — MemPalace reports recall_any@5 (did the right chunk appear in top-5?) while competitors report end-to-end QA accuracy; retrieval recall is structurally higher than QA accuracy, so direct numeric comparison inflates MemPalace's apparent superiority. (2) FEATURE-DISABLED BASELINE — MemPalace's 96.6% headline uses the bare ChromaDB path with no MemPalace-specific logic; turning on the actual product features (rooms, compression) reduces performance by up to 12.4pp. (3) SCALABILITY CEILING — the system relies on retrieving everything when corpus size permits; no selective retrieval for realistic (tens of thousands of sessions, millions of tokens) corpora. Strengthened by multi-source independent reproductions: lhl/agentic-memory's code review, Thin Signal's analysis, and GitHub Issue #39's reproduction. The article is evidence for two findings: production-configuration-baseline-discipline and (indirectly) independent-convergence-retrieval-ceiling."
relevance: "High"
added_by: "Claude"
tags: ["benchmarking", "adjudication", "memory-architecture", "governance", "third-party-review"]
url: "https://vectorize.io/articles/mempalace-benchmarks"
authority: ["vectorize"]
findings:
  - "production-configuration-baseline-discipline.md"
date_added: "2026-04-23"
---
