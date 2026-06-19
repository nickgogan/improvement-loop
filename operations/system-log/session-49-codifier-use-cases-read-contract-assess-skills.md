---
notion_id: null
log_entry: "Session 49 — Codifier: Use-Case Registry + Read-Contract Design + Three Assessment Skills"
actor: "Agent: Claude"
area: null
change_type: "Design + Implementation"
milestone: null
rationale: "Executed Phases 4–6 of the session-48 plan. Phase 4 canonicalized 35 Librarian use cases under (concept, operation) decomposition; cross-tab revealed `agent.md` as the gravity well (11 of 35 UCs) and produced the authoring backlog. Phase 5 formalized the Librarian read-contract — query parsing, operation-first load order, Tier-1 default shape, Tier-2 graph traversal with 3-hop ceiling, Tier-3 consumer-request-gated reads, confidence disclosure, provenance surfacing with exact links. Phase 6 authored three minimal concept files (`agent.md`, `prompt.md`, `skill.md`) and three IL-scoped assessment skill drafts (`assess-agent`, `assess-prompt`, `assess-skill`); `assess-prompt` reframed mid-session as an *extension* over `/prompt-evaluator` rather than a parallel rubric after Nick pushed back on duplication. Substrate is now exercisable end-to-end for the three assess-* deliverables."
source_dd: "DD-29, DD-77, DD-78, DD-80, DD-81, DD-82, DD-86"
target_system: "improvement-loop"
date: "2026-04-21"
---

# Session 49 — Codifier: Use-Case Registry + Read-Contract Design + Three Assessment Skills

## What Changed

### Phase 4 — Librarian Use-Case Registry

- Produced `project-management/design-notes/2026-04-21-librarian-use-case-registry.md`.
- **35 use cases** canonicalized across 9 categories (design advice, concrete deliverables, assessment, diagnosis, decision support, explanation, currency, meta/KB, planning). Row schema: `ID | query shape | example | concept file(s) | operation file | tier | deliverable shape | weight | needs concept? | needs op?`.
- **Cross-tab** concept × operation produced:
  - `agent.md` is the gravity well — 11 of 35 UCs route through it (31%).
  - `audit.md` exercised by 6 UCs (already authored); the other 8 operation files are greenfield.
  - Tier-2 escalation is the default for 10 UCs (29%) — memory, second-brain variant C, design-debate decisions.
  - Tier-3 appears explicitly in 1 UC; implicitly escalatable in a few more.
- **Phase-6 blockers identified:** `agent.md` (P1, 11 UCs), `prompt.md` (P1, 2 UCs), `skill.md` (P1, 2 UCs) — all authored in Phase 6.
- **Session-50+ authoring backlog:** P2 concepts `memory.md`, `context-rot.md`; P2 operations `diagnose.md`, `design.md`; plus P3/P4 concepts and operations.
- **Frequency weights:** assessment ~40%, design advice ~25%, diagnosis ~15% = ~80% core; remaining 6 categories distribute the 20% long tail.
- **Nick's gate decisions** captured inline in the registry:
  - Q1 — `coverage.md` stays as an operation file (symmetry over meta-behavior).
  - Q2 — `fetch.md` collapsed with three sub-ops; token-budget threshold determines if split is needed later. Meta-concern of the reference layer.
  - Q3 — `whats-new` takes `since: <date>` input (consumer-parameterized, no staleness-ledger dependency).
  - Q4 — Agent variants kept light; stubs enough to distinguish referents.
  - Q5 — **No separate Librarian usage log**; the IL System Log carries usage-record responsibility.

### Phase 5 — Librarian Read-Contract Design

- Produced `project-management/design-notes/2026-04-21-librarian-read-contract.md`.
- **Execution flow formalized:** `parse → load → compose → read → assemble → cite`. Ten steps:
  1. Query parsing (canonical verb map; noun + variant extraction; meta `*` detection; cross-concept handling; size/urgency heuristics).
  2. Load order — operation file first (determines which subsection kinds to read), then concept file(s), then Tier-1 substrate. Fallbacks when the reference layer is incomplete: graceful degradation to runtime aggregation, never refusal.
  3. Tier-1 default read shape per operation × concept (mapping table for all 9 operations' subsection kinds).
  4. Tier-2 escalation — 5 signals, graph traversal via `related_findings` typed links (`contradicts`, `extends`, `enables`, `same-problem`), **3-hop ceiling**.
  5. Tier-3 escalation — consumer-request-gated by default; cache-first reads; SL one-line note per read.
  6. Confidence disclosure — High / Medium / Low / None-gap with forced escalation on Low.
  7. Provenance surfacing — every claim cites; tier attribution explicit; inferred claims marked.
  8. Consumer-input handling — per operation (audit, diagnose, whats-new with `since` param, meta, design/decide/explain/fetch/plan).
  9. Boundary and edge cases (missing concept/operation files, ambiguous verb, oversized artifact, cross-concept queries, verb-noun mismatch).
  10. Output shape — cross-operation elements (query restatement, tier trace, confidence tags, citations, gap report, next-step suggestions).
- **Nick's inline annotations on read-contract** captured (verbatim locations in the source):
  - Provenance §7: exact links requested; skills must emit navigable references (`<guide>.md#<anchor>` plus line-range appendix until section manifest lands).
  - Boundary cases §9: encounter-tracking mechanism needed so the Librarian tracks with what the world needs from it — flagged as session-50 design item; no home chosen yet.
  - Query restatement (Q1): always keep.
  - Tier-2 hop ceiling (Q3): 3 for now; monitor and refine via IL SL traces from actual assess-* usage.
  - Cross-concept queries (Q4): deferred; design direction is Lucene-style parallel subagent decomposition combined by the Librarian into a unified answer. Requires a high-quality subagent template. Session-50+ scope.
  - Output shape (Q5): all five elements kept.
- **Token-budget meta-concern** codified: operation files ~600 lines; concept files ~300 lines; split when threshold approached.

### Phase 6 — Three Concept Files + Three Assessment Skills

- **Concept files (`operations/references/librarian/`):**
  - `agent.md` — three variant stubs (prompt-based / harness-based / autonomous-vs-supervised) with variant-selection heuristics, 10-aspect composition table with variant overlays, Tier-1/2/3 pointers. Kept light per Nick's session-49 gate; deeper per-variant iteration is session-50+.
  - `prompt.md` — single referent; **reframed mid-session to extension-over-`/prompt-evaluator` semantics** after Nick challenged the "parallel rubric" draft. Composition table now records only IL *additions* that `/prompt-evaluator` structurally cannot cover (G2 on embedded context, G5 on embedded tool directives, G1 at spec-document scale, harness-specific Tier-2 findings).
  - `skill.md` — single referent; safety-critical classification rule (G9.I6 unconditional for destructive-action skills, per session-48 Test 4); composition table with {G1, G3b, G5, G6, G8} default plus G9.I6 gate.
- **SKILL.md files (`.claude/skills/` — IL-scoped per DD-49, not workspace-root):**
  - `systems/improvement-loop/.claude/skills/assess-agent/SKILL.md` — load-and-apply wrapper over `audit.md` × `agent.md`. Variant selection at Step 0; variant-specific guide sets resolved at Step 1.
  - `systems/improvement-loop/.claude/skills/assess-prompt/SKILL.md` — extension over `/prompt-evaluator`. Step 0 classifies triggers (embeds context / tool directives / is spec-document / harness-specific). Step 1 invokes or receives `/prompt-evaluator` baseline via `Skill` tool. Step 3 has an **early-exit path** when no triggers fire — reports "IL audit adds no further findings" and exits rather than producing redundant output.
  - `systems/improvement-loop/.claude/skills/assess-skill/SKILL.md` — safety-critical classification at Step 0 triggers G9.I6 fire at Step 1. Summary opens with the G9.I6 outcome when the classification is safety-critical.
- **`_index.md` updated** — three new concept files cataloged; planned-next-entries section updated with P2/P3/P4 priority structure from the use-case registry.
- **All three skills `allowed-tools: Read Grep Glob`** (read-only). `assess-prompt` additionally has `Skill` to invoke `/prompt-evaluator`.

## Counts

| Metric | Value |
|--------|-------|
| Design notes produced | 2 (use-case registry, read-contract) |
| Concept files produced | 3 (`agent.md`, `prompt.md`, `skill.md`) |
| Operation files produced | 0 (all assess-* skills compose existing `audit.md`) |
| SKILL.md files produced | 3 (IL-scoped at `systems/improvement-loop/.claude/skills/`) |
| Existing files modified | 2 (`_index.md`, `prompt.md` mid-session reframe) |
| Use cases canonicalized | 35 across 9 categories |
| Nick gates cleared | 3 (post-Phase 4, post-Phase 5, post-Phase 6) |
| Mid-session reframes | 1 (`assess-prompt`: parallel rubric → extension over `/prompt-evaluator`) |
| Phases executed | 3 of 3 planned for session 49 (4, 5, 6 complete) |

## Design Decisions Applied

| DD | How Applied |
|----|-------------|
| DD-29 | Human gate honored at each phase boundary. No deployment to live `.claude/` (workspace root) or `meta-system/knowledge/`. Skills deployed only to IL-scoped `.claude/skills/`. |
| DD-49 | IL-specific skills written to `systems/improvement-loop/.claude/skills/` (not workspace root). Nick explicitly reminded of this at Phase-6 gate. |
| DD-77 | Single-form classification preserved. Concept/operation distinguish by `type:` frontmatter. |
| DD-78 | ContractSpec triple-role (governance + audit criteria + applicability gating) continues to carry load. `audit.md`'s Preconditions-as-gates pattern is the operational form. |
| DD-80 | Pipeline simplification unchanged. Reference layer is consumer-side; does not touch Researcher pipeline. |
| DD-81 | Pattern filter unchanged. |
| DD-82 | 4-agent architecture preserved. Codifier authored reference-layer artifacts and skills; Librarian is the consumer of both. Librarian role-expansion amendment still deferred. |
| DD-86 | Owner responsibility unchanged. |

## Affected Items

- `project-management/design-notes/2026-04-21-librarian-use-case-registry.md` — created (Phase 4; Nick inline-annotated at close)
- `project-management/design-notes/2026-04-21-librarian-read-contract.md` — created (Phase 5; Nick inline-annotated at close)
- `operations/references/librarian/agent.md` — created (Phase 6, concept with 3 variant stubs)
- `operations/references/librarian/prompt.md` — created, then modified mid-Phase-6 to extension semantics after Nick's push-back
- `operations/references/librarian/skill.md` — created (Phase 6, with safety-critical classification + G9.I6 gate)
- `operations/references/librarian/_index.md` — updated (three new concepts + planned-next restructured by priority)
- `systems/improvement-loop/.claude/skills/assess-agent/SKILL.md` — created (Phase 6, post-gate)
- `systems/improvement-loop/.claude/skills/assess-prompt/SKILL.md` — created (Phase 6, post-gate; extension-over-`/prompt-evaluator` shape)
- `systems/improvement-loop/.claude/skills/assess-skill/SKILL.md` — created (Phase 6, post-gate)
- `operations/system-log/session-49-codifier-use-cases-read-contract-assess-skills.md` — created (this file)

## Deferred to Session 50+

### Primary scope (new this session)

1. **Test the three assess-* skills in practice.** Run each against a real artifact; log what works, what the reference layer missed, what edge cases emerged. Feed results into §9 boundary-case tracking.
2. **Boundary-case tracking mechanism.** Nick's read-contract §9 annotation: capture Librarian encounters "somewhere" so the Librarian tracks with what the world needs. Candidates: SL entries with structured tags, a dedicated `librarian-encounters/` folder, or a rolling feedback file. Design decision needed before enforcement.
3. **Librarian subagent template.** From Nick's read-contract Q4 annotation: cross-concept queries should decompose Lucene-style into parallel subagent queries, combined by the Librarian. Needs a high-quality template; not yet authored.
4. **Operation files P2:** `diagnose.md`, `design.md`. Each has 5 UCs in the registry; natural next-wave authoring.
5. **Concept files P2:** `memory.md` (with variants), `context-rot.md`. Unblocks diagnose/design use cases.

### Secondary scope (carried from earlier sessions, still deferred)

6. **Session-45 identification Status fields** — Nick's APPROVED/REJECTED/REDIRECTED edits on 4 guided + 8 auto-tier entries still pending.
7. **Lifecycle spec Phase 1 DDs** (DD-X1, DD-X3, DD-X4) — still pending. Blocks G7/G2/G9 re-syntheses.
8. **DD-78 amendment proposal** (Contract triple-role). Defer until further reference-layer exercise.
9. **DD-82 amendment proposal** (Librarian role expansion — reference-layer maintenance, three-tier access). Defer until reference layer is exercised.
10. **References-by-agent reorg IB.** `operations/references/` currently mixes files owned by different agents; `librarian/` is the first agent-scoped subdirectory. IB item to author.
11. **`/dimension-rebalance` on 2 P2 Agentic Systems findings** whose `category:` frontmatter still reads "Agentic OS."
12. **MetaSystem-as-canonical-hybrid framing** — Nick's MetaSystem-as-harness-builder framing is still in flux. Do not reintroduce canonical framing anywhere until Nick lands it.

### Open questions to resolve in session 50 close or next sync

- **SL entry shape for Tier-3 reads** (read-contract Q2): Nick deferred. Structured frontmatter vs. free-form appended lines under a rolling `librarian-reads` SL entry.
- **Weight-calibration timing** — once assess-* skills are exercised, revise the core/long-tail weights in the registry from estimates to measurements. Source data: IL SL per Nick's decision.

## Cross-References

- Session 48 SL entry: `operations/system-log/session-48-codifier-librarian-reference-layer-build.md`
- Session 49 handoff (the plan executed): `operations/handoffs/handoff-prompt-session-49-codifier-use-cases-read-contract-assess-skills.md`
- Phase 4 output: `project-management/design-notes/2026-04-21-librarian-use-case-registry.md`
- Phase 5 output: `project-management/design-notes/2026-04-21-librarian-read-contract.md`
- Reference layer (full current state): `operations/references/librarian/`
- New skills (IL-scoped): `systems/improvement-loop/.claude/skills/assess-agent/`, `.../assess-prompt/`, `.../assess-skill/`
- Coordination target for `assess-prompt`: `.claude/skills/prompt-evaluator/` (workspace root)
- Codifier agent definition: `agents/codifier/agent.md`
- Librarian agent definition: `agents/librarian/agent.md`
