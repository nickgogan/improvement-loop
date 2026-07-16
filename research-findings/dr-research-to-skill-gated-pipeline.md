---
name: '/dr Deep-Research-to-Skill Pipeline — Gap-Aware Research with Independent Quality Gates'
summary: 'A six-phase pipeline that turns a topic into an installed, registered, hub-routed skill: (0) enumerate the live registry and search a concept tree so only the GAP versus existing coverage is researched; (1) research to saturation under hard rules — 3+ independent sources per concept, ~20% negation queries, stop at 2 empty searches or a 15-concept cap; (2) synthesize under an artifact contract, then pass three INDEPENDENT gates — trigger-accuracy eval (≥9/10), sibling collision check, and a blind fresh-context claim-verification gate — plus an injection scan at the write boundary; (3) persist through an idempotent script gated on zero unresolved High findings; (4) cross-pollinate peers conservatively (≤5% of peer length); (5) record researched concepts back into the concept tree, feeding a staleness clock. The doc explicitly warns the trigger eval is a Goodhart-able proxy, which is why the gates stay independent.'
implementation_notes: 'The closest production analog to the engine''s own research pipeline (/research-loop → /identify-artifacts → /extract-artifacts), and the comparison exposes concrete gaps on the engine side: (a) no gap-awareness — engine intake does not query what the KB already covers before researching (the concept tree''s staleness clock also answers the engine''s evergreen-vs-volatile problem mechanically); (b) no saturation rules — the 3-source floor, negation-query quota, and 2-empty-search stop are countable termination criteria where the engine relies on judgment; (c) no independent gates at the write boundary — the engine''s human gate substitutes for the blind claim-verification gate, but as the restructure program pushes toward Nick-extricated operation, these machine gates are the replacement design; (d) the injection scan at the write boundary (treat all web content as data; nothing unscanned reaches the skill tree) is directly adoptable for engine KB intake today. Also validates the engine''s no-hardcoded-lists rule: Phase 0 enumerates the live hub registry from manifests, never a hardcoded family list.'
category: Agentic Systems
evidence_strength: Medium (practitioner-documented, production system at a large enterprise (repo private, author-shared writeup))
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- General
adopted_in: []
sources:
- hub-and-spoke-context-hub.md
proposals: null
date_discovered: '2026-07-12'
last_updated: '2026-07-12'
related_findings:
- file: convergence-loop-optimizer-family-contract.md
  rel: enabled-by
- file: concept-family-explorer-five-neighborhood-gap-mapping.md
  rel: extended-by
- file: two-tree-model-authoring-vs-canonical-generated-pack.md
  rel: enables
pipeline_status: synthesized
consumed_by:
- building-agentic-systems.md
tags:
- research-pipeline
- saturation-rules
- independent-gates
- prompt-injection
- goodhart
---

# /dr Deep-Research-to-Skill Pipeline — Gap-Aware Research with Independent Quality Gates

## What It Is

`/dr <topic>` is the context-hub system's build engine: web research in, installed and
hub-routed skill out, with every step bounded by countable rules and gated by independent
verifiers. Six phases:

- **Phase 0 — Concept analysis.** Enumerate the *live* hub registry from manifest files
  (never a hardcoded list); search the concept tree so only the gap versus existing
  coverage gets researched; queue stale concepts (>90 days) for refresh; classify multi-
  topic requests as parallel vs family (families research shared branches first).
- **Phase 1 — Research to saturation.** 3+ independent sources per concept; ~20% negation
  queries; per-claim confidence (3 sources → fact, 2 → qualify, 1/contested → tentative);
  stop at saturation (2 empty searches AND every concept met the 3-source floor) or the
  15-concept cap; parallel research capped at 4 agents per batch with bounded briefs.
- **Phase 2 — Skill creation + gates.** Write to a generated-artifact contract
  (description ≤1000 chars in TRIGGER/SKIP grammar, ≥8 keywords, body >500 lines → split
  into references/). Injection scan at the write boundary. Hub-routing decision (spoke vs
  new hub vs standalone). Then run trigger eval (Pass H ≥9/10), collision check (Pass I),
  and the blind claim-verification gate.
- **Phase 3 — Persist + register**, gated on zero unresolved High findings; then repair
  deferral edges.
- **Phase 4 — Cross-pollination.** Append findings to overlapping peers: idempotent, ≤5%
  of peer length per run, snapshot-backed, never delete (conflicts get a `### Conflicts`
  note instead of overwrites).
- **Phase 5 — Concept-tree update.** Record researched concepts, their skill id, and
  links; advance the staleness clock (`firstResearchedAt` preserved, `researchedAt`
  advances).

## Why It Matters

Plain English: this is what "research becomes a durable asset without a human in the
loop" looks like when done carefully. Every place the engine currently relies on Nick's
judgment — when to stop researching, whether claims are actually supported, whether a new
artifact collides with an existing one — has a mechanical counterpart here. The gates are
deliberately *independent*: a skill that routes perfectly can still be full of
unsupported claims, and a well-cited skill can still collide with a sibling. One gate
passing never excuses another.

## How It Works (key mechanics)

- **Gap-aware research** is the token-economy move: the concept tree tells Phase 0 what
  is already known, so research spend goes only to the delta. The >90-day staleness queue
  turns freshness into a scheduled property rather than a hope.
- **Saturation is countable.** 3-source floor per concept, ~20% negation queries (search
  for disconfirmation, not just support), 2-empty-search stop, 15-concept cap. The best-
  practices list is explicit: trust the caps over the instinct to keep going.
- **The blind claim-verification gate** runs in a fresh-context subagent (it has not seen
  the research trail), multi-engine, and verdicts every anchored claim
  SUPPORTED / NOT-IN-SOURCE / CONTRADICTED. Optionally routed through a *different*
  frontier model (`--cross-model`).
- **Goodhart warning is in the contract.** Pass H's ≥9/10 trigger score is a proxy; a
  gamed description scores high and routes garbage. The blind claim gate and anti-pattern
  checks exist precisely because the proxy can be gamed.
- **Security boundary.** All researched/web content is data; the injection scan at the
  write boundary is non-negotiable — nothing unscanned reaches the installed skill tree.

## How It Could Fail

- **Concept-tree rot.** Gap-awareness inverts into gap-blindness if Phase 5 upserts are
  skipped — the tree claims coverage that drifted.
- **Saturation rules on thin domains.** A 3-source floor forces weak sources into scope
  for genuinely novel topics; the per-claim confidence ladder (qualify/tentative) is the
  pressure valve.
- **Gate fatigue.** Three gates plus a sync gate per artifact is real cost; the pipeline
  amortizes it by making each gate scriptable, but a manual adoption of this design
  without automation would stall.
