# Improvement Loop — Progress

**Last Updated:** 2026-04-26 (session 74 close — Phase-3 lifecycle-spec DDs filed, design loop closed)

## Current Focus

Codifier disposition. Session 74 closed the artifact-lifecycle spec's design loop by filing the four Phase-3 DDs in a single Codifier pass: DD-98 (guide split), DD-99 (theme graduation), DD-100 (template and agent versioning), DD-101 (co-occurrence harvest queue). Phase 1 (DD-93/94/95) and Phase 2 (DD-96/97) ratified session 70; Phase 3 closes the spec.

**Outcome — four DDs filed.** Each DD codifies its own procedure or structural pattern. Two amend DD-94's closed trigger-tag enum (DD-98 adds `guide-split`; DD-99 adds `theme-graduation`); the amendments honor DD-94's "new trigger tags require a DD amendment" rule by being the DDs that amend it. DD-100 is the missing Phase-3 sibling to DD-97 — DD-97 governs rule/skill extension; DD-100 governs template versioning and agent version-bump (with DD-82 invariant: agent bumps require Nick's prior approval). DD-101 makes DD-77's "co-occurrence resolved at read time by downstream consumers" operational for one specific consumer (`/synthesize-guide`), without contradicting DD-77's negative design decision.

**Cross-DD consistency check passed inline.** Seven cross-DD invariants spot-checked at filing time (DD-94 enum amendments, DD-95 per-version independence, DD-96 multi-version scan, DD-77 read-time-resolution preservation, DD-93 preserved-section disposition on split, DD-97/DD-100 downstream from DD-101, IB-153 dependency for DD-99 ABSORB path). No structural ambiguities surfaced for stop-and-surface.

**Four atomic commits** (one per DD). Form matches DD-93..97 verbatim — frontmatter, agent callout, Constraint, Why, Rules, Acceptance Criteria, Scope and Non-Goals, Related, Source, Phase-3 Marker. No spec rewrites; the design note remains a frozen reference. No Phase-3 IB filing inline (standing rule); IB sweep is session-75+ work.

Session-74 SL: `session-74-codifier-lifecycle-phase-3-dds.md`.

**Next session target (session 75):** Open. Top candidates from Nick's prioritization queue:
- **G7 / G2 / G9 re-synthesis** — top unblocked Codifier unit; live-validation gate for IB-154 + IB-155. G7 most overdue (+11 findings).
- **Retroactive migration of ~100 non-guide/non-pattern extracts** — pipeline-collapse Phase M1 audit follow-up.
- **Phase-3 IB sweep** — implementation IBs for DD-98/99/100/101, analogous to session 71's IB-154…158 sweep. Includes DD-94's enum-bullet edits and `_schema.yaml`'s `version` field addition.

---

## Nick's Prioritizaton

Ordered queue. Status markers: `[nick-gate]` waits on Nick's ruling; `[deferred]` held by Nick, re-evaluate on trigger; `[trigger]` waits on external evidence or volume; `[don't-do-yet]` do not reintroduce until a specific upstream condition lands.

- **G7 / G2 / G9 re-synthesis** — top unblocked Codifier unit. G7 most overdue (+11 findings). Skill is fully lifecycle-aware after session 71 (DD-93 preservation + DD-94 changelog on `/synthesize-guide`; DD-95 lifecycle pointer + DD-97 corpus-scan extension proposal on `/extract-artifacts`; DD-96 `/detect-drift` skill available). Re-synthesis is the natural live-validation gate for IB-154 + IB-155.
- **Retroactive migration of ~100 non-guide/non-pattern extracts** — per pipeline-collapse Phase M1 audit.
- **Phase-3 IB sweep** — implementation IBs for DD-98/99/100/101 (session 74 filing). Analogous to session 71's IB-154…158 sweep for Phases 1+2. Includes DD-94's enum-bullet edits (`guide-split`, `theme-graduation`) and `_schema.yaml`'s `version` field addition.
- **IB-153** — /dimension-rebalance after Sub-dim 1.B. Codifier capacity; not urgent per Nick. Will reclassify Memory Architecture findings to Context Engineering parent.
- **`/summarize-encounters` skill build** — [trigger] volume trigger or Nick's brief.
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
