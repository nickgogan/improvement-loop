# Improvement Loop — Progress

**Last Updated:** 2026-04-26 (session 78 close — G2 re-synthesized; live-validation pass #2 on Phase-1 + Phase-3 stack clean)

## Current Focus

Codifier disposition. Session 78 re-synthesized **G2 (Managing Agent Context)** at `extracts/guides/managing-agent-context.md` via `/synthesize-guide --findings <…> --trigger staleness-threshold --session 78`. Second live exercise of the Phase-1 + Phase-3 lifecycle stack on real input — first on the IL's largest dimension (Context Engineering) and largest cluster shape to date. Cluster grew 26 → 44 findings (+18 net-new: 2 P1 + 13 P2 + 3 borderline approved at Nick gate; 0 removed). All exercised surfaces matched contract; no procedural defects observed; no follow-up IBs filed.

**Surfaces live-validated this session:**

- **DD-93 preservation capture (no-preserve case, second consecutive):** `preserved = empty`; Steps 3.5/3.7 dispatched as no-op; marker validation trivially clean. Byte-equality regression test (Step 3.7) remains unexercised on real preserved content (logged for future).
- **DD-98 split-trigger detection:** count=44 ≥25 ✓ (substantially above G7's 27); practitioner-question evaluation = single (design-vs-defense is sub-organization within "losing context or burning tokens", not bifurcation); single-condition dispatch path → inline observation only, NO proposal file emitted; `operations/split-proposals/` directory not created (lazy emission honored).
- **DD-94 changelog append:** trigger `staleness-threshold` validated against the post-session-76 7-tag enum; non-header line count = 6 → clean (≤10); most-recent-first ordering; companion file at `extracts/guides/changelog/managing-agent-context.changelog.md` now carries 2 entries (session 44 initial-synthesis stub + session 78 re-synthesis).
- **DD-101 co-occurrence harvest scan:** 16 candidates queued (7 rule + 1 skill + 8 template; recommendations: 9 extract + 7 dismiss-as-inline). 0 agent-shape detections. 0 supersessions (all 26 prior findings retained). 0 duplicate-suppressions (queue file new). Queue file created lazily at `extracts/guides/managing-agent-context.harvest-queue.md`.
- **DD-81 routing table sync + back-annotations:** G2 row updated (last synthesized 2026-04-26; 44 findings; status draft). Bidirectional cross-refs: G5/G7/G4/G8 already reciprocal; G3 reciprocal added. 18 net-new findings flipped `pipeline_status` → `synthesized`; `consumed_by` populated with `managing-agent-context.md`. 3 of 18 had no prior pipeline_status/consumed_by fields (added inline).

**Structural restructure** to absorb new material: added Step 8 (Architect Context Across Tools, Tiers, and Sessions; 6 sub-steps for vault tiering / folder-as-workspace / skill scoping / cross-platform portability / monorepo distribution / PROGRESS.md bridge); 5 new sub-steps across Steps 3-4 (content-granularity L0/L1/L2 tiers; progressive skill loading; technique-selector preference order; /re trajectory engineering; harness+model layered awareness); 2 new defenses in Step 5 (atomic session scoping; never let Claude compact CLAUDE.md); 2 new templates (Module Manifest; Multi-Tool Context Mirror Map); 4 new pitfalls (#12-15); Key Concepts 5 → 6.

**One atomic commit** (regen + changelog + queue file + bidirectional cross-refs + finding back-annotations): 23 files changed, +573/-44. Session-78 SL: `session-78-codifier-g2-re-synthesis.md`.

**Downstream of this session:**
- 16 harvest-queue rows in `extracts/guides/managing-agent-context.harvest-queue.md` await Nick rulings. 9 rows recommended `extract via /extract-artifacts` (rule + skill + template candidates); 7 rows recommended `dismiss as inline` (already absorbed as guide sub-steps or templates). Approved-extraction rows feed IB-164's queue-row promotion path on `/extract-artifacts`.
- G7 harvest-queue rulings from session 77 still await Nick gate (8 rows).

**Two consecutive clean live-validation passes** (G7 + G2): the procedure-design substrate from sessions 73-76 is operating correctly under real-cluster load.

**Next session target:** Per the prioritization queue below, **G9 (Agent Governance and Trust) re-synthesis** is the natural next-up Codifier unit — third of the G7/G2/G9 live-validation sweep. G9 had 10 findings at last synthesis (2026-04-19); current count drift unmeasured but Governance is among the smaller dimensions. G9 exercises threshold-edge behavior (10 findings is below DD-98's split count threshold of 25, so the count-axis trigger evaluates to no-op) — a different live-validation shape than G7's 27 and G2's now-large 44. Alternative: `/summarize-encounters` brainstorm if Nick has surfaced it. Nick gates next.

---

## Nick's Prioritizaton

Ordered queue. Status markers: `[nick-gate]` waits on Nick's ruling; `[deferred]` held by Nick, re-evaluate on trigger; `[trigger]` waits on external evidence or volume; `[don't-do-yet]` do not reintroduce until a specific upstream condition lands.

- **G9 re-synthesis** — top unblocked Codifier unit; third of the G7/G2/G9 live-validation sweep (G7 re-synthesized session 77 at 27 findings clean; G2 re-synthesized session 78 at 44 findings clean). G9 had 10 findings at last synthesis (2026-04-19). Exercises threshold-edge behavior on `/synthesize-guide` Step 0.7 (count=10 < DD-98's 25 threshold → count-axis trigger no-op; conjunction trivially un-met regardless of question count). Remains fully Phase-1 + Phase-2 + Phase-3 lifecycle-aware: DD-93 preservation + DD-94 changelog (7-tag enum); DD-95 lifecycle pointer + DD-97 corpus-scan extension proposal + DD-100 template version-bump path on `/extract-artifacts`; DD-96 `/detect-drift` skill; DD-98 split-trigger detection on `/synthesize-guide` Step 0.7 + `/identify-artifacts` Step 6.a; DD-99 graduation-trigger detection on `/identify-artifacts` Step 6.b; DD-101 co-occurrence harvest-queue scan on `/synthesize-guide` Step 4.7 + queue-row promotion on `/extract-artifacts` Step 0a / Step 4.8. Different live-validation shape than G7's 27 (mid) and G2's 44 (large); third data point on threshold-edge behavior.
- **G2 harvest queue rulings** — 16 candidate rows in `extracts/guides/managing-agent-context.harvest-queue.md` await Nick gate. 9 rows recommended `extract via /extract-artifacts` (6 rule + 1 skill + 2 template candidates); 7 rows recommended `dismiss as inline` (already absorbed as guide sub-steps / templates). Approved-extraction rows feed IB-164's queue-row promotion path on `/extract-artifacts`.
- **G7 harvest queue rulings** — 8 candidate rows in `extracts/guides/session-persistence-and-memory.harvest-queue.md` await Nick gate (carry-over from session 77). 5 rows recommended `extract via /extract-artifacts` (rule + skill candidates); 3 rows recommended `dismiss as inline`. Approved-extraction rows feed IB-164's queue-row promotion path on `/extract-artifacts`.
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
