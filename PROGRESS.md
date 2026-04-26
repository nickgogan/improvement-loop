# Improvement Loop — Progress

**Last Updated:** 2026-04-26 (session 71 close — IB-154 + IB-155 shipped; `/synthesize-guide` honors DD-93 preservation + DD-94 changelog)

## Current Focus

Codifier disposition. Session 71 shipped two of the three Phase-1 implementation IBs queued by session 70:

1. **IB-154 (DD-93) — preserved-section enforcement.** `/synthesize-guide` SKILL.md gains three procedure steps: Step 0.5 (pre-regen capture of `## Nick's Annotations` + `<!-- PRESERVE -->` regions, marker validation), Step 3.5 (re-insertion at original ordinal / closest anchor with documented fallbacks), Step 3.7 (post-regen byte-equality regression test, fail-closed on drift with structured report). No-op for guides with no preserved surfaces.
2. **IB-155 (DD-94) — companion changelog appender + retroactive stubs.** Step 4.5 added: locate-or-create `extracts/guides/changelog/<stem>.changelog.md` on re-synthesis, write entry per DD-94 shape, enforce closed trigger-tag enum + ~10-line cap (≤10 clean / 11–15 warn / >15 abort), insert at top. Two new optional args (`--trigger`, `--session`). Initial synthesis writes no entry. 11 retroactive stubs written (one per staged guide; `## 2026-04-19 — Session 44 — initial-synthesis` heading; `initial-synthesis` tag permitted ONLY for backfill).

Two atomic commits per handoff sequencing. No real-guide runs this session — skill change only; live validation is the next-session work. Session-71 SL: `session-71-codifier-ib-154-ib-155-synthesize-guide-update.md`.

**Next session target:** **G7 / G2 / G9 re-synthesis** (Codifier disposition). All three are now fully unblocked. G7 most overdue (+11 findings since last). Re-synthesis exercises the new DD-93 + DD-94 lifecycle behaviors against real input — the actual acceptance gate for IB-154 + IB-155.

---

## Nick's Prioritizaton

Ordered queue. Status markers: `[nick-gate]` waits on Nick's ruling; `[deferred]` held by Nick, re-evaluate on trigger; `[trigger]` waits on external evidence or volume; `[don't-do-yet]` do not reintroduce until a specific upstream condition lands.

- **G7 / G2 / G9 re-synthesis** — top unblocked Codifier unit. G7 most overdue (+11 findings). Skill is now lifecycle-aware (DD-93 preservation + DD-94 changelog) after session 71; re-synthesis exercises both behaviors against real input. Real acceptance gate for IB-154 + IB-155.
- **IB-156** — Phase-1 implementation work; independent. `/extract-artifacts` writer update for `last_change_*` going forward (session-70 backfill already executed in-session).
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
