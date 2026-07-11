---
name: "Addy Osmani — The New SDLC With Vibe Coding (blog extraction of the Google whitepaper)"
source_type: "Article"
status: "Not started"
key_takeaways: |-
  One source covering two batch URLs: the Kaggle-hosted Google whitepaper
  (kaggle.com/whitepaper-the-new-SDLC-with-vibe-coding, co-authors Osmani/Saboo/Kartakis)
  and Osmani's own blog extraction of it — confirmed same content; blog is the accessible
  canonical (the Kaggle page serves a JS shell to fetchers; the PDF needs /pdf-to-markdown
  if full-whitepaper depth is wanted). Three patterns survive KB dedup: (1) static/dynamic
  context partition documented as a VERSIONED ARCHITECTURAL DECISION — we have push-vs-pull
  loading but not the partition-as-ADR governance move; candidate DD-style practice for the
  engine's own context files. (2) Dual verification — trajectory (reasoning-path soundness)
  as a distinct eval axis from output correctness, absent from the four-layer eval finding.
  (3) Conductor-vs-orchestrator operating modes — interactive IDE exploration vs async
  delegation for well-specified tasks. Already covered: harness 10/90, progressive
  disclosure, complexity-based model routing. Est. 3 novel findings.
relevance: "High"
added_by: "Agent (Link-Intake Triage)"
tags:
  - sdlc
  - harness
  - evals
  - context-engineering
  - agentic-os
url: "https://addyosmani.com/blog/new-sdlc-vibe-coding/"
authority: []
findings: []
date_added: "2026-07-11"
date_processed: null
---

Queued for `/research-loop` extraction by the 2026-07-11 link-intake triage
(`operations/research-reports/2026-07-11-link-intake-triage.md`, links #7+#8 — one
extraction pass covers both URLs; underlying primary:
https://www.kaggle.com/whitepaper-the-new-SDLC-with-vibe-coding).
