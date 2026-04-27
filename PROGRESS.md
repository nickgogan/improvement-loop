# Improvement Loop — Progress

**Last Updated:** 2026-04-26 (session 77 close — G7 re-synthesized; live-validation pass on Phase-1 + Phase-3 stack clean)

## Current Focus

Codifier disposition. Session 77 re-synthesized **G7 (Session Persistence and Memory)** at `extracts/guides/session-persistence-and-memory.md` via `/synthesize-guide --findings <…> --trigger staleness-threshold --session 77`. First live exercise of the Phase-1 + Phase-3 lifecycle stack on real input. Cluster grew 14 → 27 findings (+13 net-new P1+P2 Memory Architecture findings; 0 removed). All exercised surfaces matched contract; no procedural defects observed; no follow-up IBs filed.

**Surfaces live-validated this session:**

- **DD-93 preservation capture (no-preserve case):** `preserved = empty`; Steps 3.5/3.7 dispatched as no-op as predicted; marker validation trivially clean.
- **DD-98 split-trigger detection:** count=27 ≥25 ✓; practitioner-question count=1 (single per routing table); single-condition dispatch path → inline observation only, NO proposal file emitted; `operations/split-proposals/` directory not created (lazy emission honored).
- **DD-94 changelog append:** trigger `staleness-threshold` validated against the post-session-76 7-tag enum; non-header line count = 6 → clean (≤10); most-recent-first ordering; companion file at `extracts/guides/changelog/session-persistence-and-memory.changelog.md` now carries 2 entries (session 44 initial-synthesis stub + session 77 re-synthesis).
- **DD-101 co-occurrence harvest scan:** 8 candidates queued (5 rule + 2 skill + 1 template; recommendations: 5 extract + 3 dismiss-as-inline). 0 agent-shape detections. 0 supersessions (all 14 prior findings retained). 0 duplicate-suppressions (queue file new). Queue file created lazily at `extracts/guides/session-persistence-and-memory.harvest-queue.md`.
- **DD-81 routing table sync + back-annotations:** G7 row updated (last synthesized 2026-04-26; 27 findings; status draft). Bidirectional cross-refs added to G9 + G1 (G2 + G3 already had reciprocal G7 references). 13 net-new findings flipped `pipeline_status: classified` → `synthesized`; `consumed_by: ["session-persistence-and-memory.md"]`.

**Structural restructure** to absorb new material: promoted Retrieval Pipeline to its own Part 2 (6 sub-steps; was Step 1.3 alone) and Write Governance to its own Part 5 (3 sub-steps; was template-only); added Part 1 sub-steps for storage topology / bank isolation / org-scale fit; added Step 3.4 (memory.md cross-session) and Step 6.3 (byproduct capture); 2 new templates (Hybrid Retrieval Recipe, Subagent Memory Directory Setup); 1 new worked example (Memongo recipe); 4 new pitfalls (#9–12).

**One atomic commit** (regen + changelog + queue file + bidirectional cross-refs + finding back-annotations): 19 files changed, +738/-78. Session-77 SL: `session-77-codifier-g7-re-synthesis.md`.

**Downstream of this session:**
- 8 harvest-queue rows in `extracts/guides/session-persistence-and-memory.harvest-queue.md` await Nick rulings. Approved-extraction rows feed `/extract-artifacts` queue-row promotion path (IB-164). 3 rows have Codifier recommendation `dismiss as inline`.

**Next session target:** Per the prioritization queue below, **G2 (Managing Agent Context) re-synthesis** is the natural next-up Codifier unit — second of the G7/G2/G9 live-validation sweep. G2 had 26 findings at last synthesis (2026-04-19); current finding count drift unmeasured but staleness window is comparable to G7's. Post-G2: G9 (Agent Governance and Trust; 10 findings at last synthesis) is the third unit. Alternative: `/summarize-encounters` brainstorm if Nick has surfaced it. Nick gates next.

---

## Nick's Prioritizaton

Ordered queue. Status markers: `[nick-gate]` waits on Nick's ruling; `[deferred]` held by Nick, re-evaluate on trigger; `[trigger]` waits on external evidence or volume; `[don't-do-yet]` do not reintroduce until a specific upstream condition lands.

- **G2 / G9 re-synthesis** — top unblocked Codifier unit (G7 re-synthesized session 77; 27 findings; live-validation pass clean). G2 next-up (26 findings at last synthesis); G9 third (10 findings). Both remain fully Phase-1 + Phase-2 + Phase-3 lifecycle-aware: DD-93 preservation + DD-94 changelog (7-tag enum) on `/synthesize-guide`; DD-95 lifecycle pointer + DD-97 corpus-scan extension proposal + DD-100 template version-bump path on `/extract-artifacts`; DD-96 `/detect-drift` skill; DD-98 split-trigger detection on `/synthesize-guide` Step 0.7 + `/identify-artifacts` Step 6.a; DD-99 graduation-trigger detection on `/identify-artifacts` Step 6.b; DD-101 co-occurrence harvest-queue scan on `/synthesize-guide` Step 4.7 + queue-row promotion on `/extract-artifacts` Step 0a / Step 4.8. G2 will exercise the surfaces a second time on a Context-Engineering-heavy finding set; G9 a third time at smaller cluster size (threshold-edge behavior).
- **G7 harvest queue rulings** — 8 candidate rows in `extracts/guides/session-persistence-and-memory.harvest-queue.md` await Nick gate. 5 rows recommended `extract via /extract-artifacts` (rule + skill candidates); 3 rows recommended `dismiss as inline`. Approved-extraction rows feed IB-164's queue-row promotion path on `/extract-artifacts`.
- **IB-153** — /dimension-rebalance after Sub-dim 1.B. Codifier capacity; not urgent per Nick. Will reclassify Memory Architecture findings to Context Engineering parent.
- **`/summarize-encounters` skill build** — [trigger] volume trigger or Nick's brief. Nick: Lets brainstorm together what this could look like and why.
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
