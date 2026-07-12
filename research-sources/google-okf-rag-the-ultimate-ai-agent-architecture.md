---
name: 'Google OKF + RAG: The Ultimate AI Agent Architecture'
source_type: Video
status: Done
key_takeaways: 'The hybrid-architecture companion to the OKF explainers: don''t pick OKF or RAG, wire

  both behind a query router. Canonical, high-stakes queries route to the curated OKF

  spine (exact, cited answers); open-ended exploratory queries route to RAG over the

  uncurated long tail. 80/20 split: OKF carries the canonical core you can''t get wrong,

  RAG covers the mess you''d never curate by hand. Two coupling rules: a curated concept

  outranks fuzzy retrieved chunks when both exist, and the OKF index acts as a

  pre-search map (progressive disclosure) so the agent drills into RAG only where

  curation runs out. The whole stack can hide behind one retrieval facade (even a

  single MCP server). Economics: curated text in git is cheap to edit; RAG carries

  standing embedding/re-embedding/hosting cost — curate what''s worth curating, pay to

  index the rest.'
relevance: Medium
added_by: Nick
tags:
- context-engineering
- vault-architecture
url: https://www.youtube.com/watch?v=_X55fkwdC-Q
authority:
- cloud-codes.md
findings:
- curated-spine-plus-rag-hybrid-query-router.md
date_added: '2026-07-12'
date_processed: '2026-07-12'
date_published: '2026-06-28'
---

# Google OKF + RAG: The Ultimate AI Agent Architecture (Cloud Codes)

Pass 2 deep extraction completed 2026-07-12 from cached transcript
(`app/transcript-fetcher/transcripts/_X55fkwdC-Q.md`). Survives the four-video
cluster's recency cut because it alone carries the hybrid router architecture.
