---
name: "TJSlattery/MemoryDemo — five memory types + typed shared-memory handoff slots"
source_type: "Documentation"
status: "Done"
key_takeaways: |-
  Compact working reference implementation of the five-memory-type taxonomy (working/episodic/
  semantic/procedural/shared) in one LangGraph + MongoDB Atlas + Chainlit stack: a multi-agent
  PM-assistant demo with a MemoryManager event bus rendering every memory op live in the UI.
  The striking pattern: typed shared-memory slots (plan / findings / disambiguation /
  handoff_payload) for coordinator↔sub-agent handoff that avoid paraphrase loss between
  agents — directly relevant to multi-agent context engineering (1.C). Evidence strength
  weak: zero-star, single-author, no-license personal demo (last push 2026-06-08) — cite the
  shared-memory-slot pattern only if corroborated elsewhere. Not watched-library material.
relevance: "Medium"
added_by: "Agent (Link-Intake Triage)"
tags:
  - memory
  - context-engineering
  - multi-agent
url: "https://github.com/TJSlattery/MemoryDemo"
authority:
  - "tj-slattery.md"
findings:
  - "typed-shared-memory-handoff-slots.md"
  - "converged-memory-substrate-vs-patchwork.md"
date_added: "2026-07-11"
date_processed: "2026-07-11"
---

Queued for `/research-loop` extraction by the 2026-07-11 link-intake triage
(`operations/research-reports/2026-07-11-link-intake-triage.md`, link #12).
