---
name: "Supermemory — We Broke the Frontier in Agent Memory (99% SOTA ASMR, 2026-03-22)"
source_type: "Blog Post"
status: "Done"
date_processed: "2026-04-23"
key_takeaways: "Supermemory's later blog post claiming ~99% on LongMemEval_s via ASMR (Agentic Search and Memory Retrieval). Architecture pivots from vector similarity to active agentic reasoning: INGESTION uses 3 parallel reader agents extracting across six vectors (Personal Info, Preferences, Events, Temporal, Updates, Assistant Info); RETRIEVAL uses 3 specialized search agents reasoning over stored findings; ANSWERING uses two experimental ensembles — 8-variant (98.60%) and 12-variant decision forest (97.20%). CRITICAL GOVERNANCE DISCLOSURES: (a) Explicitly marked 'highly experimental' and 'not our main production Supermemory engine (yet)'; even self-labeled as a 'parody / social experiment to create a new standard.' (b) 'Success' in the ensemble is defined as 'if _any_ of the 8 distinct reasoning paths successfully arrived at ground truth' — a union-of-successes aggregation, not majority-vote or best-of-N. (c) Cost/latency disclosures completely absent. The blog is evidence for three findings: experimental-sandbox-labeling-discipline (positive: the labels are clear), ensemble-eval-majority-required-for-success (anti-pattern evidence: the any-succeeds aggregation inflates scores), and agentic-search-memory-retrieval-architecture (the ASMR design itself, as a described architectural option)."
relevance: "High"
added_by: "Claude"
tags: ["benchmarking", "memory-architecture", "supermemory", "agentic-retrieval", "governance", "ensemble-eval"]
url: "https://supermemory.ai/blog/we-broke-the-frontier-in-agent-memory-introducing-99-sota-memory-system/"
authority: []
findings:
  - "experimental-sandbox-labeling-discipline.md"
  - "ensemble-eval-majority-required-for-success.md"
  - "agentic-search-memory-retrieval-architecture.md"
date_added: "2026-04-23"
---
