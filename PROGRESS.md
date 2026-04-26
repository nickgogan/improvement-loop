# Improvement Loop — Progress

**Last Updated:** 2026-04-26 (session 70 close — Lifecycle-spec Phase-1 ratified)

## Current Focus

Owner disposition. Session 70 ratified Phase-1 of the artifact lifecycle spec — three DDs filed (DD-93 preserved-section enforcement, DD-94 guide companion changelog, DD-95 non-guide `last_change_*` frontmatter). All three accepted as-spec. Three implementation IBs queued (IB-154, IB-155, IB-156). `_schema.yaml` updated with the two new fields. 31-artifact retroactive backfill executed in-session per Nick directive (scope expansion from spec's deferred IB framing). Session-70 SL: `session-70-owner-lifecycle-spec-phase1-ratification.md`.

**Next session target (Codifier disposition):** **G7 / G2 / G9 re-synthesis.** Phase-1 ratification has unblocked the largest pending Codifier unit. G7 is the most overdue (+11 findings since last synthesis). Re-synthesis runs against the new lifecycle contract — `/synthesize-guide` will need IB-154 + IB-155 implementation work to honor preserved sections and write companion changelog entries.

---

## Nick's Prioritizaton

Ordered queue. Status markers: `[nick-gate]` waits on Nick's ruling; `[deferred]` held by Nick, re-evaluate on trigger; `[trigger]` waits on external evidence or volume; `[don't-do-yet]` do not reintroduce until a specific upstream condition lands.

- **G7 / G2 / G9 re-synthesis** — top unblocked Codifier unit. G7 most overdue (+11 findings). Requires IB-154 + IB-155 work to honor DD-93 preservation and DD-94 companion changelog on the regen path.
- **IB-154 / IB-155 / IB-156** — Phase-1 implementation work. IB-154 + IB-155 are gating for G7/G2/G9 re-synthesis (skill must honor preservation + write changelog entries before next regen). IB-156 is independent — `/extract-artifacts` writer update for `last_change_*` going forward.
- **Promote `harness-engineering-third-evolution` from `raw` to `classified`** — adjacent and reinforcing to G3 Step 8 (added session 69). Researcher-or-Codifier scope, low-cost. Position TBD; could fold into next intake or `/identify-artifacts` pass.
- **Candidate 2 re-evaluation** (spec-as-governance P2 → P1) — [trigger] revisit at 4th–5th independent-repo surfacing per session-62 decision.
- **IB-153** — /dimension-rebalance after Sub-dim 1.B. Codifier capacity; not urgent per Nick. Will reclassify Memory Architecture findings to Context Engineering parent.
- **Librarian subagent template** for cross-concept queries (read-contract Q4). Position TBD.
- **DD-78 amendment** — Contract triple-role. [deferred] until reference layer is more exercised.
- **DD-65 full supersession** — skill-inventory drift flagged session 61 (6 listed, 24+ actual). Position TBD.
- **Retroactive migration of ~100 non-guide/non-pattern extracts** — per pipeline-collapse Phase M1 audit.
- **Re-evaluate DEFERRED findings** (session 62): `agentic-search-memory-retrieval-architecture` ([trigger] 2nd production source), `agent-native-app-store-emerging-category` ([trigger] evidence maturity).
- **Lifecycle-spec Phase-2 / Phase-3 DDs (DD-X2, DD-X5–X9)** — [deferred] sequence after Phase-1 ratification lands. Out of scope for session 70.
- **Visualization brainstorm** — [deferred] boil DDs/architecture into human-visualizable form. Session 62: `interactive-explanations-extend-linear-walkthroughs` finding (P2) is a direct technique for this work.
- **Decay cluster-normalization** — [deferred] held per Nick; decay tracked as sub-dim 1.A research, not a near-term build target. Re-evaluate if Household OS or another near-term build needs principled forgetting.
- **First /solicit-proposals round** — [deferred] infrastructure live; thrice-deferred. Waits until Nick directs a dedicated Owner session.
- **Deploy 11 guides** from `extracts/guides/` to `meta-system/knowledge/guides/` — [deferred] paused pending pipeline-collapse decision.
- **Test three assess-\* skills against real artifacts** — [trigger] seeds first encounter log once tracking is approved.
- **`agent.md` variant-depth iteration** — [trigger] demand-driven on concrete consumer queries; variants (prompt-based / harness-based / autonomous-vs-supervised) exist as stubs per session-49 gate.
- **Weight calibration** for use-case-registry core/long-tail estimates — [trigger] meaningful once encounter tracking accumulates data.
- **`/summarize-encounters` skill build** — [trigger] volume trigger or Nick's brief.

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
