---
title: "Librarian Boundary-Case Encounters — Taxonomy, Shape, Routing"
type: "operational-reference"
target_system:
  - "improvement-loop"
created: "2026-07-12"
updated: "2026-07-12"
author: "owner"
source_dd:
  - "DD-82"
  - "DD-86"
  - "DD-116"
tags:
  - "librarian"
  - "boundary-cases"
  - "reference-layer"
---

# Librarian Boundary-Case Encounters

The schema source for the Librarian-layer skills (`/assess-*`, `/design-*`, `/ask-kb`, `/compare-repos`). Distilled 2026-07-12 (substrate-audit gate G6) from the ratified design note `2026-04-22-librarian-boundary-case-tracking.md` (session-52 acceptance; now archived in `project-management/design-notes/` → `archive/design-notes/`). This file carries the living taxonomy, entry shape, and routing table; the note carries the deliberation.

**Current status — persistence suspended.** The original write destination (`operations/system-log/session-<N>-librarian-encounters.md`) was retired with the SL producer (DD-116; DD-59 scope note). The durable destination for encounter records is a Nick-gated question folded into the Phase-2 second-brain proposal (substrate-audit gate G9). Until that ruling: skills **surface** encounters in their run report output (type + one-line description) and write nothing to disk. The taxonomy and shapes below remain the contract for that surfacing and for whatever store G9 selects. (Mitigating context: zero encounter logs were written in 27+ sessions under the old contract.)

## 1 — Taxonomy: 13 encounter types (controlled vocabulary)

An encounter is any query-handling event where the pipeline (parse → load → compose → read → assemble → cite) **deviated from the Tier-1 happy path** — took a fallback, asked a clarifying question, escalated tiers, or reported a gap. Skills must use these tags verbatim.

| # | Encounter type | Fires at (read-contract step) | Trigger |
|---|---|---|---|
| 1 | `missing-concept` | Step 1.2(c) | No concept file resolves the noun |
| 2 | `missing-operation` | Step 2 / §9.2 | No operation file resolves the verb |
| 3 | `ambiguous-verb` | Step 1.1 / §9.3 | Query blends verbs or verb is non-canonical |
| 4 | `ambiguous-variant` | Step 1.2(b) | Variant-selection heuristic does not disambiguate |
| 5 | `cross-concept` | Step 1.4 / §9.5 | Query spans two concept files |
| 6 | `verb-noun-mismatch` | §9.6 | Operation doesn't semantically apply to the concept |
| 7 | `oversized-artifact` | Step 1.5 / §9.4 | Submitted artifact > ~500 lines |
| 8 | `hop-ceiling-hit` | Step 4.2 | Tier-2 traversal stopped at 3-hop ceiling |
| 9 | `tier-3-read` | Step 5 | External / watched-library read performed |
| 10 | `low-confidence` | Step 6.1 | Substrate supports claim weakly or indirectly |
| 11 | `kb-gap` | Step 6.4 | No substrate found for a requested aspect |
| 12 | `redirect` | Step 8.1 | Query routed out of scope (e.g., `/prompt-evaluator`, `/security-review`) |
| 13 | `clarification-asked` | Steps 1.2, 1.5, 8.2–8.5 | Librarian asked the consumer one disambiguating question |

Notes:
- **Not every encounter is a failure.** `tier-3-read` and `clarification-asked` are healthy behavior; their frequency is still signal (Tier-3 volume = cost watch; clarification volume = parser or input-contract signal).
- **An encounter can carry multiple types** — a list, not a single label.
- **Vocabulary amendment path:** Owner proposes → Nick gates → read-contract and this reference both updated (session-50 Q4 ruling).

## 2 — Per-encounter shape

Used today for report-output surfacing; becomes the record shape when G9 selects a store.

```markdown
## <ISO timestamp> — <encounter-type>[, <encounter-type>...]

- **Query:** <natural-language query, ≤1 line>
- **Parsed as:** (verb: `<v>`, noun(s): `<n>`[; variant: `<var>`])
- **Invoking skill:** `<skill-name>` (or `direct` if Librarian invoked without a skill)
- **Substrate read:** Tier-1=<N sections>; Tier-2=<M findings>; Tier-3=<K reads>
- **Resolution:** <how the Librarian proceeded — fallback, degraded, asked, escalated, redirected>
- **Gap (if any):** <what was missing — e.g., "no concept file for `mcp.md`">
- **Consumer disposition:** <optional — answered / user abandoned / user redirected>
```

Required: timestamp, encounter-type(s), query, parsed-as, resolution. Optional but encouraged: substrate read, gap, consumer disposition. Inline report surfacing may compress to `type + one-line description` when a full block is disproportionate.

## 3 — Feedback routing (who acts on a pattern)

| Encounter type | Primary feedback path | Who acts |
|---|---|---|
| `missing-concept` | Use-case registry → promote concept priority; Codifier authors next session | Codifier (after Nick re-prioritizes) |
| `missing-operation` | Use-case registry → promote operation; Codifier authors | Codifier |
| `ambiguous-verb` | IB item → canonical-verb-map refinement (read-contract §1.1) | Codifier or Owner |
| `ambiguous-variant` | Concept file update (variant-selection heuristics) | Codifier |
| `hop-ceiling-hit` (frequent) | IB item → revisit 3-hop ceiling; tune with evidence | Owner proposal |
| `oversized-artifact` (frequent) | IB item → scope protocol refinement | Owner proposal |
| `kb-gap` | IB item → Researcher queues for next scan | Researcher |
| `redirect` (frequent to same target) | Read-contract §8.1 update, or scope-expansion proposal | Owner |
| `low-confidence` (pattern by aspect) | Evidence-strength review; possibly Researcher scan | Researcher or Codifier |
| `verb-noun-mismatch` | Usually parser-side; IB if frequent | Codifier |
| `clarification-asked` (frequent for same reason) | Input-contract refinement (e.g., require `since:` for `whats-new`) | Codifier |
| `tier-3-read` | Watch-only. Volume → cost signal. Rolling read log: `librarian-reads.md` (this folder) | Owner monitors |
| `cross-concept` | Subagent template work (read-contract Q4) | Codifier |

The Owner proposes routing; Nick gates reprioritization (session-50 §5.3 ruling).

## Cross-References

- Read-contract (query-execution protocol; §5.3 Tier-3 read log): `operations/references/librarian/read-contract.md`
- Use-case registry: `operations/references/librarian/use-case-registry.md`
- Rolling Tier-3 read log: `operations/references/librarian/librarian-reads.md`
- Provenance (deliberation, session-50/52 rulings): `archive/design-notes/2026-04-22-librarian-boundary-case-tracking.md`
- G9 destination question: second-brain proposal (Phase 2, restructure program)
