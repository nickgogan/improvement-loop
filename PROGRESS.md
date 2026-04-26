# Improvement Loop — Progress

**Last Updated:** 2026-04-26 (session 71 close — full Phase-1+2 lifecycle implementation sweep: IB-154 → IB-158 all shipped)

## Current Focus

Codifier disposition. Session 71 shipped the entire Phase-1 + Phase-2 implementation queue ratified in session 70 — five IBs across one session, in two phases (initial handoff scope was IB-154 + IB-155; Nick directed in-session expansion to IB-156/157/158 after the first two committed cleanly). Five atomic commits, one per IB.

**Phase A (initial handoff scope):**

1. **IB-154 (DD-93) — preserved-section enforcement.** `/synthesize-guide` SKILL.md gains three procedure steps: Step 0.5 (pre-regen capture of `## Nick's Annotations` + `<!-- PRESERVE -->` regions, marker validation), Step 3.5 (re-insertion at original ordinal / closest anchor with documented fallbacks), Step 3.7 (post-regen byte-equality regression test, fail-closed on drift with structured report). No-op for guides with no preserved surfaces.
2. **IB-155 (DD-94) — companion changelog appender + retroactive stubs.** Step 4.5 added: locate-or-create `extracts/guides/changelog/<stem>.changelog.md` on re-synthesis, write entry per DD-94 shape, enforce closed trigger-tag enum + ~10-line cap (≤10 clean / 11–15 warn / >15 abort), insert at top. Two new optional args (`--trigger`, `--session`). Initial synthesis writes no entry. 11 retroactive stubs written (one per staged guide; `## 2026-04-19 — Session 44 — initial-synthesis` heading).

**Phase B (Nick mid-session scope expansion):**

3. **IB-156 (DD-95) — `/extract-artifacts` lifecycle pointer writer + SL stem validation.** Three new args (`--session`, `--sl`, `--update`). Step 2.7 resolves both fields and validates `operations/system-log/<stem>.md` exists. Step 3 update-mode dedup behavior preserves `extraction_date` + `deployed*` while overwriting `last_change_*`. Frontmatter template gains both fields between `extraction_date` and `identification_report`.
4. **IB-157 (DD-96) — `/detect-drift` skill (new).** ~250-line read-only on-demand source-drift scanner. Enumerates `extracts/{rules,skills,templates,agents}/`, compares `source_finding.last_updated > artifact.extraction_date` (strict), emits per-run report at `operations/drift-reports/<YYYY-MM-DD>-source-drift.md` with closed three-value Recommendation enum. Guides + patterns excluded. Read-only invariant codified.
5. **IB-158 (DD-97) — `/extract-artifacts` corpus-scan + extension-proposal.** Step 1.7 added (rule + skill forms only). LLM-loose calibration (i). Per-finding categorization: no-match passes through; single-match emits one proposal and skips drafting; multi-match emits proposal with secondaries flagged. Aggregated proposals written to `operations/extension-proposals/<YYYY-MM-DD>-extension-proposals.md`. Auto-merge prohibition codified.

After this session: `/synthesize-guide` honors DD-93 + DD-94; `/extract-artifacts` honors DD-95 + DD-97; `/detect-drift` implements DD-96. The non-guide artifact lifecycle (writer side, reader side, drift visibility, redundancy avoidance) is fully wired. One field-name discrepancy logged for a future DD-96 amendment: findings carry `last_updated`, DD-96 names the field `updated`; implementation reads the live-schema field with semantic intent preserved.

Session-71 SL: `session-71-codifier-ib-154-ib-155-synthesize-guide-update.md` (filename retained from initial handoff scope; body covers all five IBs in Phase A + Phase B sections).

**Next session target (session 72 — Codifier disposition):** **Top 3 items in Nick's Prioritization** — (1) promote `harness-engineering-third-evolution` from raw → classified; (2) Candidate 2 re-evaluation [trigger]: check if 4th–5th independent-repo surfacing has fired since session 62; (3) Re-evaluate two DEFERRED findings [trigger checks]: `agentic-search-memory-retrieval-architecture` (2nd production source?) and `agent-native-app-store-emerging-category` (evidence maturity?). Session texture is evidence-driven evaluation, not skill build — trigger checks before action on items 2-3. G7/G2/G9 re-synthesis remains queued for a subsequent session. Handoff: `operations/handoffs/handoff-prompt-session-72-codifier-queue-top-3.md`.

---

## Nick's Prioritizaton

Ordered queue. Status markers: `[nick-gate]` waits on Nick's ruling; `[deferred]` held by Nick, re-evaluate on trigger; `[trigger]` waits on external evidence or volume; `[don't-do-yet]` do not reintroduce until a specific upstream condition lands.

- **Promote `harness-engineering-third-evolution` from `raw` to `classified`** — adjacent and reinforcing to G3 Step 8 (added session 69). Researcher-or-Codifier scope, low-cost. Position TBD; could fold into next intake or `/identify-artifacts` pass.
- **Candidate 2 re-evaluation** (spec-as-governance P2 → P1) — [trigger] revisit at 4th–5th independent-repo surfacing per session-62 decision.
- **Re-evaluate DEFERRED findings** (session 62): `agentic-search-memory-retrieval-architecture` ([trigger] 2nd production source), `agent-native-app-store-emerging-category` ([trigger] evidence maturity).
- **Lifecycle-spec Phase-3 DDs (DD-X5, DD-X6, DD-X8, DD-X9)** — [deferred] guide-split / theme-graduation / template-and-agent versioning / co-occurrence harvesting. Phase 1 + Phase 2 ratified session 70.
- **G7 / G2 / G9 re-synthesis** — top unblocked Codifier unit. G7 most overdue (+11 findings). Skill is fully lifecycle-aware after session 71 (DD-93 preservation + DD-94 changelog on `/synthesize-guide`; DD-95 lifecycle pointer + DD-97 corpus-scan extension proposal on `/extract-artifacts`; DD-96 `/detect-drift` skill available). Re-synthesis is the natural live-validation gate for IB-154 + IB-155.
- **First `/detect-drift` smoke-test run against the live KB** — validates IB-157 read paths (enumeration-gap counts, unresolvable-source counts). Low-cost; can fold into next Codifier session.
- **IB-153** — /dimension-rebalance after Sub-dim 1.B. Codifier capacity; not urgent per Nick. Will reclassify Memory Architecture findings to Context Engineering parent.
- **Librarian subagent template** for cross-concept queries (read-contract Q4). Position TBD.
- **Retroactive migration of ~100 non-guide/non-pattern extracts** — per pipeline-collapse Phase M1 audit.
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
