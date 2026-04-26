# Improvement Loop — Progress

**Last Updated:** 2026-04-26 (session 73 close — /detect-drift smoke-test + scan.py codification + Librarian cross-concept subagent template)

## Current Focus

Codifier disposition. Session 73 ran the first end-to-end `/detect-drift` smoke-test, then expanded scope twice (Nick-directed) to codify scan.py and pull the Librarian cross-concept subagent template forward.

**Outcome 1 — `/detect-drift` smoke-test against live extracts corpus.** First run of IB-157. 31 artifacts scanned across 4 forms; 1 drift hit, 30 clean, 0 enumeration gaps, 0 unresolvable sources. Report at `operations/drift-reports/2026-04-26-source-drift.md`. Drift hit: `rules/agent-self-reporting-unreliability-independent-eval` (source updated 2026-04-20, extracted 2026-04-19). Codifier recommendation: `dismiss as cosmetic` — source body shows post-extraction administrative updates only (extraction-note section, `consumed_by` list growth, `pipeline_status: synthesized`); artifact substance unchanged. PENDING Nick gate.

**Outcome 2 — `scan.py` helper + SKILL.md update.** First pass of the smoke-test (LLM-driven inline parsing) returned a false-clean result; spot-check surfaced a YAML quote-style heterogeneity bug (corpus has 27 double-quoted + 4 single-quoted `extraction_date` fields; inline parser stripped only double quotes, silently masking the drift hit). Nick directed mid-session codification. `scan.py` reifies Steps 1-2 of `/detect-drift` (enumeration + frontmatter parse + source resolution + strict-greater-than compare); LLM-judgment steps (recommendation, report construction) remain in the skill body.

**Outcome 3 — Librarian cross-concept subagent template (read-contract §Q4).** Workflow file at `agents/librarian/workflows/cross-concept-subagent.md`. Lucene-style decomposition: one subagent per `(operation × concept)` pair, parent recombines via per-operation join rules. Includes parameterized subagent prompt template, recombination logic across all 9 operations, UC-9.2 worked example, failure-modes table.

**Smoke-test signals (5 from handoff + 1 surfaced):** enumeration coverage clean (31/31); source-pointer resolution clean (31/31); DD-96 amendment field-name alignment clean (0 legacy `updated`); recommendation-enum distribution single data point (1 hit / 1 `dismiss as cosmetic`); DD-95 lifecycle-pointer presence — corpus fully backfilled, **pre-DD-95 graceful-degradation path NOT exercised** (future fixture-based validation needed); surfaced — YAML quote-style heterogeneity in artifact frontmatter, corpus-wide.

**Surfaced for Owner / Nick gate (not filed inline per standing rule):**

- Operation-file "join rule" subsection — the cross-concept template names join rules for all 9 operations but those rules currently live in the template, not in the operation files themselves. IB candidate.
- YAML quote-style normalization across the artifact corpus — affects all frontmatter readers, not just `/detect-drift`. Owner-routable.

**Four atomic commits** (three outcome commits + close commit). No DDs / IBs filed inline (standing rule).

Session-73 SL: `session-73-codifier-detect-drift-smoke-test.md`.

**Next session target (session 74):** **Lifecycle-spec Phase-3 DDs (DD-X5 / DD-X6 / DD-X8 / DD-X9).** Per Nick's session-73 direction. Phase 1 + Phase 2 ratified session 70. Phase-3 four-DD bundle: guide-split / theme-graduation / template-and-agent versioning / co-occurrence harvesting. Handoff: `operations/handoffs/handoff-prompt-session-74-codifier-lifecycle-phase-3-dds.md` (written this session's close via `/session-handoff`).

---

## Nick's Prioritizaton

Ordered queue. Status markers: `[nick-gate]` waits on Nick's ruling; `[deferred]` held by Nick, re-evaluate on trigger; `[trigger]` waits on external evidence or volume; `[don't-do-yet]` do not reintroduce until a specific upstream condition lands.

- **Lifecycle-spec Phase-3 DDs (DD-X5, DD-X6, DD-X8, DD-X9)** — [next-session] guide-split / theme-graduation / template-and-agent versioning / co-occurrence harvesting. Phase 1 + Phase 2 ratified session 70. Promoted to next-session focus by Nick at session-73 close.
- **IB-153** — /dimension-rebalance after Sub-dim 1.B. Codifier capacity; not urgent per Nick. Will reclassify Memory Architecture findings to Context Engineering parent.
- **Retroactive migration of ~100 non-guide/non-pattern extracts** — per pipeline-collapse Phase M1 audit.
- **G7 / G2 / G9 re-synthesis** — top unblocked Codifier unit. G7 most overdue (+11 findings). Skill is fully lifecycle-aware after session 71 (DD-93 preservation + DD-94 changelog on `/synthesize-guide`; DD-95 lifecycle pointer + DD-97 corpus-scan extension proposal on `/extract-artifacts`; DD-96 `/detect-drift` skill available). Re-synthesis is the natural live-validation gate for IB-154 + IB-155.
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
