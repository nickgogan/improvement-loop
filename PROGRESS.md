# Improvement Loop — Progress

**Last Updated:** 2026-04-24 (session 65 close)

## Current Focus

Codifier disposition. Session 65 closed IB-150 — `/extract-artifacts` now generates DD-92-conformant ContextSpec by default (8 edits; new Step 2.5 Validate Drafts enforces presence + mechanical-copy + forbidden-vocab; IL classification meta stripped at write). Session-65 SL: `session-65-codifier-ib-150-extract-artifacts-dd92-update.md`.

**Next session target:** **IB-152** — `/assess-skill` / `/assess-agent` ContextSpec audit extension. Unblocked by IB-150.

---

## Nick's Prioritizaton

Ordered queue. Status markers: `[nick-gate]` waits on Nick's ruling; `[deferred]` held by Nick, re-evaluate on trigger; `[trigger]` waits on external evidence or volume; `[don't-do-yet]` do not reintroduce until a specific upstream condition lands.

- **IB-152** — /assess-skill / /assess-agent ContextSpec audit extension. P3. Consumer-side audit tooling validates ContextSpec presence and universal-vocab conformance on deployed artifacts.
- **Guide re-synthesis (G4/G10)** — unblocked by session-63 inflow (G4 +2, G10 +1). G2/G7/G9 remain partially blocked on Lifecycle-spec Phase-1 DDs.
- **Fresh /extract-artifacts run** — real acceptance test of IB-150's skill update. Opens when promoted + curated + non-pattern findings reach the extractable queue.
- **Candidate 2 re-evaluation** (spec-as-governance P2 → P1) — [trigger] revisit at 4th–5th independent-repo surfacing per session-62 decision.
- **IB-153** — /dimension-rebalance after Sub-dim 1.B. Codifier capacity; not urgent per Nick. Will reclassify Memory Architecture findings to Context Engineering parent.
- **Librarian subagent template** for cross-concept queries (read-contract Q4). Position TBD.
- **DD-78 amendment** — Contract triple-role. [deferred] until reference layer is more exercised.
- **DD-65 full supersession** — skill-inventory drift flagged session 61 (6 listed, 24+ actual). Position TBD.
- **Retroactive migration of ~100 non-guide/non-pattern extracts** — per pipeline-collapse Phase M1 audit.
- **Re-evaluate DEFERRED findings** (session 62): `agentic-search-memory-retrieval-architecture` ([trigger] 2nd production source), `agent-native-app-store-emerging-category` ([trigger] evidence maturity).
- **Lifecycle-spec Phase-1 DDs (DD-X1, DD-X3, DD-X4)** — [nick-gate] approval unblocks G7/G2/G9 re-syntheses.
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
