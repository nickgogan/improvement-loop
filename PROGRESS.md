# Improvement Loop — Progress

**Last Updated:** 2026-04-27 (session 80 close — IB-153 dimension rebalance: Memory Architecture orphan retired (41 → 0); Dim 2-5 names aligned)

## Current Focus

Codifier disposition. Session 80 closed **IB-153** — the cleanup follow-up to session 63's introduction of Sub-dim 1.B (Memory Isolation and Topology) under Dimension 1 (Context Engineering). Ran `/dimension-rebalance` per its own procedure with human-gated proposal.

**Outcomes:**

- **41 findings reclassified** out of orphan `category: Memory Architecture` (not a registered top-level dimension). Default Option A (all 41 → Context Engineering) approved with **8 borderlines re-routed to Agentic Systems** on Nick's review (vault-as-OS / personal-knowledge-store / org-memory-system patterns whose primary subject was the Dim 11 system pattern, not the memory mechanism). Per-file YAML quoting style preserved; `last_updated` bumped on all 41.
- **Routing-table G7 row** Dimensions field stripped of "Memory Architecture" per IB-153 acceptance.
- **Bonus dimension-name alignment** (per Nick's in-session ask): `research-dimensions.md` taxonomy block + 4 section headers and `guide-routing-table.md` Dimensions column for G1/G3/G5/G7/G8 aligned to the canonical long forms used in 100% of findings (Model→Model Selection, Prompt→Prompt Craft, Tools→Tool Integration, Intent→Intent Engineering).
- **2 stale prose references** to "Memory Architecture dimension" updated (`librarian/second-brain.md` L74; `agentic-speculation-…` finding `implementation_notes`).
- **IB-153 status:** `Done`; notes appended with execution summary.

**Final distribution (post-rebalance):** Context Engineering 132 (was 99, +33), Agentic Systems 29 (was 21, +8), Memory Architecture 0 (was 41). Total 588 findings, fully resident in the 11 registered dimensions.

**One atomic commit:** 46 files changed, +199/-100. Session-80 SL: `session-80-codifier-ib-153-dimension-rebalance.md`.

**Logged-for-future, not done:**
1. **YAML category-quoting normalization** (quoted vs unquoted variants across the KB) — flagged in the rebalance report's "Additional Drift" section but left out of scope; no behavioral impact, would be a separate hygiene pass.
2. **`guide-routing-table.md` line 97 stale note** — "Agentic Systems below 5-finding threshold" prose is now stale (29 ≥ 5). Not in IB-153 scope; left for the future decision about whether to propose G11.
3. **Sub-dim 1.B graduation criteria** — with 8 explicit isolation/topology findings (the 2 seeds + 6 of the borderlines absorbed there), 1.B is below the ≥10 graduation threshold but moving toward it. Continue monitoring.

**Next session target:** Back to the natural next-up Codifier unit — Nick rulings on the **38 cumulative harvest-queue rows** (G7 + G2 + G9) gating downstream `/extract-artifacts` queue-row promotion (IB-164). Top unblocked action remains: Nick rules a batch. Alternative: spec-amendment-from-live-validation session (optional, motivated by logged-for-future #1 cadence-3 from session 79).

---

## Nick's Prioritizaton

Ordered queue. Status markers: `[nick-gate]` waits on Nick's ruling; `[deferred]` held by Nick, re-evaluate on trigger; `[trigger]` waits on external evidence or volume; `[don't-do-yet]` do not reintroduce until a specific upstream condition lands.

- **Harvest-queue rulings (cumulative G7 + G2 + G9 — 38 rows)** — `[nick-gate]` top unblocked item gating downstream Codifier work. 8 G7 rows (5 extract + 3 dismiss recommendations) from session 77; 16 G2 rows (9 extract + 7 dismiss) from session 78; 14 G9 rows (10 extract + 4 dismiss) from session 79. Approved-extraction rows feed `/extract-artifacts` queue-row promotion path (IB-164). Suggested batching: rule via batch (most rows are rule-shape; cleanest review unit); skill via individual review; template via dismiss-vs-extract calibration check (most templates are already absorbed inline).
- **Spec amendment from live-validation observations** — Optional. Logged-for-future #1 reaches 3-occurrence cadence (G7 + G2 + G9 all used `--findings` mode at effective P1+P2 bar; skill spec Step 0.3 prescribes P1-only filter for topic/dimension input modes). Candidate amendment: extend Step 0.3 filter language to include P2 by default with a flag for P1-only, OR per-cluster `priority_floor` field on routing table. Low-priority; not blocking. Defer to a separate "spec amendment from live-validation observations" session.
- **Retroactive migration of ~100 non-guide/non-pattern extracts** — per pipeline-collapse Phase M1 audit.
- **Visualization brainstorm** — [deferred] boil DDs/architecture into human-visualizable form. Session 62: `interactive-explanations-extend-linear-walkthroughs` finding (P2) is a direct technique for this work.
- **`agent.md` variant-depth iteration** — [trigger] demand-driven on concrete consumer queries; variants (prompt-based / harness-based / autonomous-vs-supervised) exist as stubs per session-49 gate.
- **Weight calibration** for use-case-registry core/long-tail estimates — [trigger] meaningful once encounter tracking accumulates data.
---

## Open IB Items

Filed items live in `project-management/implementation-backlog/IB-*.md`. Source-of-truth status is the `status:` field in each file's frontmatter.

---

## Key Files

| Entity | Path |
|--------|------|
| IL identity, agents, pipeline | `CLAUDE.md` |
| Agent definitions | `agents/{owner,researcher,codifier,librarian}/agent.md` |
| Agent reflections (agent-private) | `agents/{owner,researcher,codifier,librarian}/reflections/` |
| IL-specific governance | `governance/` |
| Governance proposals (Owner + agent-authored) | `governance/proposals/` |
| Cross-system DD proposals (MetaSystem-level) | `../meta-system/governance/proposals/` |
| Design notes (deliberative specs) | `project-management/design-notes/` |
| Design Decisions | `project-management/design-decisions/` |
| Implementation Backlog | `project-management/implementation-backlog/` |
| Session handoffs | `operations/handoffs/` |
| System Log | `operations/system-log/` |
| Librarian reference layer | `operations/references/librarian/` |
| Guide routing table | `operations/references/guide-routing-table.md` |
| Research dimensions | `operations/references/research-dimensions.md` |
| Form classification rubric | `operations/references/form-classification-rubric.md` |
| Research KB (findings, sources, authorities) | `research-findings/`, `research-sources/`, `research-authorities/` |
| Watched libraries registry | `watched-libraries/_index.md` |
| Staged extracts | `extracts/` |
| IL-scoped skills | `.claude/skills/` |

---

## Session History

Session-by-session narrative lives in `operations/system-log/`. Handoff prompts in `operations/handoffs/` carry session-to-session continuation context. This file carries current focus and pointers only — not a session ledger.
