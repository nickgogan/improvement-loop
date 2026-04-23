---
name: "Supermemory Research — LongMemEval ~85% on GPT-4o"
source_type: "Research Page / Technical Report"
status: "Done"
date_processed: "2026-04-23"
key_takeaways: "Supermemory's original (pre-ASMR) research page documenting 84.6% overall on LongMemEval_s using GPT-4o (vs Zep 71.2%, full-context baseline 60.2%). LLM-as-Judge methodology with GPT-4o as judge, 6-category breakdown: Single-session-user 97.14%, Single-session-assistant 96.43%, Knowledge-update 88.46%, Temporal-reasoning 76.69%, Multi-session 71.43%, Single-session-preference 70.00%. Architectural patterns disclosed: chunk-based ingestion with atomic-memory generation; relational versioning (updates/extends/derives); dual-layer temporal grounding (documentDate vs eventDate); hybrid search (semantic on memories + original chunk injection); session-based (not turn-by-turn) ingestion. This is the baseline against which Supermemory's later ~99% ASMR claim is positioned as a sandbox improvement."
relevance: "High"
added_by: "Claude"
tags: ["benchmarking", "memory-architecture", "supermemory", "rag", "hybrid-search"]
url: "https://supermemory.ai/research/"
authority: []
findings: []
date_added: "2026-04-23"
---
