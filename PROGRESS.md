# Improvement Loop — Progress

**Last Updated:** 2026-04-26 (session 70 close — Lifecycle-spec Phase-1 + Phase-2 ratified, DD-78 amended, DD-65 superseded)

## Current Focus

Owner disposition. Session 70 closed four governance items:

1. **Lifecycle-spec Phase-1 ratification.** DD-93 (preserved-section enforcement), DD-94 (guide companion changelog), DD-95 (non-guide `last_change_*` frontmatter). All accepted as-spec. IB-154/155/156 queued. `_schema.yaml` updated. 31-artifact backfill executed in-session.
2. **DD-78 amendment.** Contract triple-role framing added — Contract sections operationally do three jobs (artifact-self-governance + emergent audit criteria + audit-applicability gating). In-place body amendment per DD-44 §When-to-Amend. Status remains Binding.
3. **DD-65 supersession.** Path B (no-successor) per DD-44 §Mark-as-Superseded-no-successor. Body callout enumerates piecewise supersession by DD-80/82/83/86/89/91 + IL CLAUDE.md + DD-29/49. Status changed Binding → Superseded.
4. **Lifecycle-spec Phase-2 ratification.** DD-96 (source drift detection — Codifier on-demand `/detect-drift` skill, no autonomous regen, Nick gates re-extraction). DD-97 (extension rubric for rules/skills — LLM-loose calibration (i), propose-don't-decide, Nick gates merge). Both accepted as-spec. IB-157/158 queued.

Session-70 SL: `session-70-owner-lifecycle-spec-phase1-ratification.md`.

**Next session target (Codifier disposition):** **G7 / G2 / G9 re-synthesis.** Phase-1 ratification has unblocked the largest pending Codifier unit. G7 is the most overdue (+11 findings since last synthesis). Re-synthesis runs against the new lifecycle contract — `/synthesize-guide` will need IB-154 + IB-155 implementation work to honor preserved sections and write companion changelog entries.

---

## Nick's Prioritizaton

Ordered queue. Status markers: `[nick-gate]` waits on Nick's ruling; `[deferred]` held by Nick, re-evaluate on trigger; `[trigger]` waits on external evidence or volume; `[don't-do-yet]` do not reintroduce until a specific upstream condition lands.

- **G7 / G2 / G9 re-synthesis** — top unblocked Codifier unit. G7 most overdue (+11 findings). Requires IB-154 + IB-155 work to honor DD-93 preservation and DD-94 companion changelog on the regen path.
- **IB-154 / IB-155 / IB-156** — Phase-1 implementation work. IB-154 + IB-155 are gating for G7/G2/G9 re-synthesis (skill must honor preservation + write changelog entries before next regen). IB-156 is independent — `/extract-artifacts` writer update for `last_change_*` going forward.
- **IB-157 / IB-158** — Phase-2 implementation work. IB-157 builds the on-demand `/detect-drift` skill (DD-96). IB-158 adds the corpus-scan + extension-proposal step to `/extract-artifacts` (DD-97). Both Codifier scope; both unblocked.
- **Promote `harness-engineering-third-evolution` from `raw` to `classified`** — adjacent and reinforcing to G3 Step 8 (added session 69). Researcher-or-Codifier scope, low-cost. Position TBD; could fold into next intake or `/identify-artifacts` pass.
- **Candidate 2 re-evaluation** (spec-as-governance P2 → P1) — [trigger] revisit at 4th–5th independent-repo surfacing per session-62 decision.
- **IB-153** — /dimension-rebalance after Sub-dim 1.B. Codifier capacity; not urgent per Nick. Will reclassify Memory Architecture findings to Context Engineering parent.
- **Librarian subagent template** for cross-concept queries (read-contract Q4). Position TBD.
- **Retroactive migration of ~100 non-guide/non-pattern extracts** — per pipeline-collapse Phase M1 audit.
- **Re-evaluate DEFERRED findings** (session 62): `agentic-search-memory-retrieval-architecture` ([trigger] 2nd production source), `agent-native-app-store-emerging-category` ([trigger] evidence maturity).
- **Lifecycle-spec Phase-3 DDs (DD-X5, DD-X6, DD-X8, DD-X9)** — [deferred] guide-split / theme-graduation / template-and-agent versioning / co-occurrence harvesting. Phase 1 + Phase 2 ratified session 70.
- **Visualization brainstorm** — [deferred] boil DDs/architecture into human-visualizable form. Session 62: `interactive-explanations-extend-linear-walkthroughs` finding (P2) is a direct technique for this work.
- **Decay cluster-normalization** — [deferred] held per Nick; decay tracked as sub-dim 1.A research, not a near-term build target. Re-evaluate if Household OS or another near-term build needs principled forgetting.
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
