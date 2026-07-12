---
name: I Pointed My Agent at the Bills
source_type: Video
status: Done
key_takeaways: 'A complete, reusable recipe for high-trust document work, demonstrated three times (email

  /calendar, insurance appeal, tax prep) with the same skeleton. Nine primitives: context

  pack, ingest, chunk, normalize, store, retrieve, cite, export, gate — with the gate

  (prepare-don''t-submit: the agent may read/organize/draft/cite but never submit/pay/sign)

  designed in from the start, not bolted on. The receipt artifact (sources used, what

  changed, what still needs approval) is the trust mechanism that makes human review fast.

  For cited-document domains (insurance denials cite the exact policy section), retrieval is

  structure-addressed — no vector DB, no similarity search; you already know the address of

  the text that matters. Clean normalized data (dates become dates, every claim has an

  address, SQLite + local folder) is what lets cheap/open-source models do the work.'
relevance: High
added_by: Nick
tags:
- orchestration
- context-engineering
- memory
url: https://www.youtube.com/watch?v=U4TmrlWEY4M
authority:
- nate-b-jones.md
findings:
- nine-primitive-document-agent-skeleton.md
- receipt-artifact-as-agent-trust-mechanism.md
- structure-addressed-retrieval-for-cited-document-domains.md
- data-normalization-as-cheap-model-enabler.md
date_added: '2026-07-12'
date_processed: '2026-07-12'
date_published: '2026-07-03'
---

# I Pointed My Agent at the Bills (Nate B Jones)

Pass 2 extraction completed 2026-07-12 (session 136) from the full transcript
(`app/transcript-fetcher/transcripts/U4TmrlWEY4M.md`). Full title: "Every AI Agent Demo
Stops at Email. I Pointed Mine at the Bills That Cost You Money." Demo uses real insurer
policy documents with synthetic patient data; runbooks and the two open skills live on the
author's Substack.
