---
name: "Static/Dynamic Context Partition as a Versioned Architectural Decision"
summary: |-
  We already split context into always-loaded (CLAUDE.md, rules) and on-demand (skills, KB reads)
  layers — but nothing governs where that boundary sits, so it drifts silently as files accrete.
  This finding says: treat the static/dynamic partition itself as a first-class architectural
  decision — reviewed in a pull request, versioned like code, ADR-style. Static context is paid
  for on every call; dynamic context only when a task touches it, so moving the boundary is a
  cost-and-reliability decision, not housekeeping.
implementation_notes: |-
  Candidate DD-style practice for the engine's own context files: a lightweight DD (or rule in
  governance/) declaring which files are static-tier (CLAUDE.md, rules/*.md, memory) vs
  dynamic-tier (skills, agents, KB), with boundary moves requiring an explicit reviewed change
  rather than incidental edits. /simplify-context already audits static-tier weight; this adds
  the governance half — the partition is decided, not discovered. Keep minimal per Occam's
  razor: one declaration doc, no new tooling.
category: "Governance"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: "P2 (Design Required)"
applicability:
  - "General"
adopted_in: []
sources:
  - "osmani-new-sdlc-vibe-coding.md"
related_findings: []
proposals: null
date_discovered: "2026-07-11"
last_updated: "2026-07-11"
---

## What It Is

A governance move from the Google whitepaper "The New SDLC" (Osmani/Saboo/Kartakis): partition agent context into a **static layer** — "loaded every turn: system instructions, rule files (AGENTS.md, CLAUDE.md, GEMINI.md), global memory, core guardrails. It's reliable, and it's expensive, because you pay for it on every single call" — and a **dynamic layer** — "skills that fire when a task matches, tool results, documents pulled from RAG. You only pay for the bits a given task touches." The novel part is not the partition (push-vs-pull loading is established practice) but the governance: "treat the boundary as a real architectural decision: reviewed in a pull request, versioned like code."

## Why It Matters

The static tier is a per-call tax on every interaction; the dynamic tier is pay-per-use. Where a piece of context lives is therefore a recurring cost decision and a reliability decision (static = guaranteed present, dynamic = present only if retrieval/matching fires). When nothing owns that boundary, content migrates into the static tier by default — every "add this to CLAUDE.md" edit is an unreviewed architectural change. Making the partition a versioned decision gives the boundary an owner, a review gate, and a history.

## Why People Are Using It

Documented as recommended practice in a Google-published whitepaper on the agentic SDLC; mirrors ADR (Architecture Decision Record) discipline that teams already apply to code architecture, extended to context architecture.

## Potential Alternatives

- Periodic audit-only approach (detect static-tier bloat after the fact, e.g. /simplify-context) without a declared boundary.
- Tooling-enforced budgets (hard token caps on static files) without decision records.

## Potential Improvements

- Pair the declared partition with a measured static-tier token cost so boundary-move reviews see the price delta.
- Extend the decision record to cover promotion/demotion criteria (when does a dynamic doc earn static placement, and vice versa).

## Potential Failure Modes

- Process overhead: if every trivial CLAUDE.md edit needs an ADR, the gate gets bypassed — scope the review requirement to boundary *moves*, not content edits within a tier.
- The partition record itself becomes stale if it hardcodes file lists that drift; declare tiers by location/pattern, not enumerated files.
