# Improvement Loop — Progress

**Last Updated:** 2026-04-26 (session 75 close — Phase-3 implementation IBs filed (IB-159 → IB-164))

## Current Focus

Codifier disposition. Session 75 closed the Phase-3 IB sweep by filing the six implementation IBs that translate DD-98/99/100/101 into actionable backlog items. Phase 1 (DD-93/94/95) implementation sweep was IB-154/155/156 (session 71); Phase 2 (DD-96/97) implementation sweep was IB-157/158 (session 71); Phase 3's implementation sweep is now IB-159 through IB-164.

**Outcome — six IBs filed.** IB-159 (DD-98 split-trigger detection on `/synthesize-guide` Step 0 + `/identify-artifacts` routing-table reads + DD-94 enum bullet add `guide-split`); IB-160 (DD-99 graduation-trigger detection on `/identify-artifacts` Step 6 + DD-94 enum bullet add `theme-graduation`); IB-161 (DD-100 `_schema.yaml` `version: integer` field for template/agent extracts + retroactive `version: 1` backfill of all 6 templates and 3 agents); IB-162 (DD-100 template version-bump path + agent flag-only path on `/extract-artifacts`); IB-163 (DD-101 co-occurrence harvest-queue scan on `/synthesize-guide` absorption phase); IB-164 (DD-101 queue-row promotion path on `/extract-artifacts` with DD-97/DD-100 dispatch by target form).

**Cross-IB consistency check passed inline.** Seven cross-IB invariants spot-checked at filing time (DD-94 enum bullet split additivity, IB-161 → IB-162 schema dependency, IB-163 → IB-164 input dependency, IB-162 → IB-164 template-target dispatch, DD-77 invariant preservation in IB-163+IB-164, DD-82 agent invariant three-layer enforcement, DD-93 preserved-section disposition in IB-159). Recommended execution order: IB-161 → IB-162 → IB-163 → IB-164 → (IB-159 + IB-160 parallel).

**Six atomic commits** (one per IB). Form matches IB-154..158 verbatim — frontmatter-only with all substance in `notes:` field. All six at status `Queued`, priority `P2`, type `Build`. No skill modifications inline (standing rule); skill SKILL.md edits are downstream of IB approval.

Session-75 SL: `session-75-codifier-phase-3-ib-sweep.md`.

**Next session target:** Per the prioritization queue below, the natural next-up Codifier units are: (a) execute the Phase-3 IB sweep (IB-159 → IB-164 — analogous to session 71's IB-154..158 implementation sweep, ~6 atomic commits in one session); or (b) G7 / G2 / G9 re-synthesis (top unblocked Codifier unit per existing queue; live-validation gate for IB-154+155); or (c) `/summarize-encounters` brainstorm (Nick has flagged for collaborative scoping). Nick gates which to take next.

---

## Nick's Prioritizaton

Ordered queue. Status markers: `[nick-gate]` waits on Nick's ruling; `[deferred]` held by Nick, re-evaluate on trigger; `[trigger]` waits on external evidence or volume; `[don't-do-yet]` do not reintroduce until a specific upstream condition lands.

- **Phase-3 IB execution** — implement IB-159 → IB-164 (session 75 filing). Recommended order per session-75 SL cross-IB consistency notes: IB-161 (schema + backfill) → IB-162 (`/extract-artifacts` version-bump path) → IB-163 (`/synthesize-guide` queue scan) → IB-164 (`/extract-artifacts` queue-row promotion) → IB-159 + IB-160 (parallel; independent of DD-100/DD-101 chain). Analogous to session 71's IB-154..158 implementation sweep.
- **`/summarize-encounters` skill build** — [trigger] volume trigger or Nick's brief. Nick: Lets brainstorm together what this could look like and why.
- **IB-153** — /dimension-rebalance after Sub-dim 1.B. Codifier capacity; not urgent per Nick. Will reclassify Memory Architecture findings to Context Engineering parent.
- **G7 / G2 / G9 re-synthesis** — top unblocked Codifier unit. G7 most overdue (+11 findings). Skill is fully lifecycle-aware after session 71 (DD-93 preservation + DD-94 changelog on `/synthesize-guide`; DD-95 lifecycle pointer + DD-97 corpus-scan extension proposal on `/extract-artifacts`; DD-96 `/detect-drift` skill available). Re-synthesis is the natural live-validation gate for IB-154 + IB-155.
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
