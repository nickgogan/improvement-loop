---
name: CareerBuddy ops-self-improve — store schema, promotion rules, dispatch table, live store
source_type: "Repository"
status: Done
key_takeaways: CareerBuddy's self-improvement memory mechanism in full — a central append-only lesson store keyed by (owning surface, failure pattern), recurrence thresholds that gate agent autonomy but never operator direction, a five-stage per-proposal promotion pipeline (shadow sandbox, separate-context grading, human gate, append-only log), a deterministic schema checker with runtime-computed threshold flags, and a dispatch table that routes non-owned work instead of re-implementing it. Uniquely valuable as live evidence — the ops/self/ store shows 20 lessons and 16 gated proposals from ~5 days of real sessions, including the loop maintaining its own schema through its own gate. The skill was itself grounded in this KB (it cites IL finding slugs), making it a downstream production validation of several existing findings.
relevance: High
added_by: Nick
tags: [self-improvement, lesson-store, promotion-rules, human-gate, dispatch-table, memory]
url: https://github.com/nickgogan/CareerBuddy (.github/skills/ops-self-improve/ + ops/self/)
authority: []
findings:
- append-only-lesson-store-owning-surface-identity.md
- recurrence-threshold-gates-autonomy-not-direction.md
- per-proposal-human-gate-promotion-pipeline.md
- deterministic-store-checker-runtime-threshold-flags.md
- self-improvement-dispatch-table-route-never-reimplement.md
- skill-self-improvement-three-approaches.md
- sandbox-first-modification-validation.md
date_added: '2026-07-12'
date_processed: '2026-07-12'
date_published: '2026-07-12'
---

# CareerBuddy ops-self-improve — store schema, promotion rules, dispatch table, live store

CareerBuddy's internal-improvement engine: a single skill (`ops-self-improve`, four modes — capture/scan/promote/status) that harvests what real sessions teach into a central markdown-native store at `ops/self/` and returns it to the system as human-gated proposals against the surface that owns each lesson. Extracted here are the store schema (`references/store-schema.md` — lesson identity, entry grammar, status lifecycle, growth bounds), the promotion rules (`references/promotion-rules.md` — thresholds, proposal shape, shadow sandbox, binary grading rubric, per-proposal gate, rollback), the dispatch table (`references/dispatch-table.md` — seven classes keyed on owning surface), the deterministic checker (`scripts/store_check.py`), and the live store files (`ops/self/lessons.md`, `proposal-log.md`, `eval-candidates.md`, `retro-latest.md`) as production evidence of what the store actually accumulates. Directly relevant to the engine's restructure-program Phase 2 (second brain for operations) and IB-172 (layered memory architecture).
