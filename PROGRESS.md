# Improvement Loop — Progress

**Last Updated:** 2026-04-26 (session 76 close — Phase-3 IB execution complete; IB-159 → IB-164 all Done)

## Current Focus

Codifier disposition. Session 76 executed all six Phase-3 implementation IBs (IB-159 → IB-164) in a single Codifier pass per the handoff's recommended order. Phase 1 (DD-93/94/95) implementation was IB-154/155/156 (session 71); Phase 2 (DD-96/97) implementation was IB-157/158 (session 71); Phase 3 (DD-98/99/100/101) implementation is now IB-159 through IB-164 (session 76). Phase 1 + Phase 2 + Phase 3 lifecycle infrastructure is wired end-to-end at the procedure-design layer.

**Outcome — six IBs Done.** IB-161 (DD-100 schema field + retroactive `version: 1` backfill on 5 templates + 2 agents — corrected from session-75's 6+3 miscount); IB-162 (DD-100 `/extract-artifacts` Step 1.8 template version-bump path + agent flag-only); IB-163 (DD-101 `/synthesize-guide` Step 4.7 co-occurrence harvest-queue scan); IB-164 (DD-101 `/extract-artifacts` Step 0a + Step 4.8 queue-row promotion / dismissal); IB-159 (DD-98 split-trigger detection on `/synthesize-guide` Step 0.7 + `/identify-artifacts` Step 6.a + DD-94 `guide-split` enum); IB-160 (DD-99 graduation-trigger detection on `/identify-artifacts` Step 6.b + DD-94 `theme-graduation` enum + Step 4.5 enum extension on `/synthesize-guide`).

**After this session.** `/synthesize-guide` honors DD-93 + DD-94 (with extended 7-tag enum) + DD-98 + DD-101. `/extract-artifacts` honors DD-95 + DD-97 + DD-100 + DD-101. `/identify-artifacts` honors DD-81 + DD-98 + DD-99. `_schema.yaml` documents both DD-95 lifecycle-tracking block and DD-100 versioning block. Four operations directories prepared (`operations/split-proposals/`, `operations/graduation-proposals/`, `operations/version-bump-proposals/`, `operations/extension-proposals/`) — all created lazily on first emission. Per-guide companion-file pattern extends from `<stem>.changelog.md` (DD-94, populated since session 71) to `<stem>.harvest-queue.md` (DD-101, lazy on first detection).

**Six atomic commits** (one per IB) plus this close commit. Per-IB closure notes rewritten per IB-152 closure pattern; all IBs flipped Queued → Done.

**One bug surfaced.** Session-75 SL recorded `extracts/templates/` (6 files) and `extracts/agents/` (3 files) at filing; actual filesystem at session-76 execution is 5 templates + 2 agents (no `_index.md`; no commits between session-75 close and session-76 start). Session-75 was a miscount. IB-161 backfilled all extant artifacts (5 + 2 = 7); session-75 SL retained unmodified per audit-trail-preserving alternative; session-76 SL carries the correction inline.

Session-76 SL: `session-76-codifier-phase-3-ib-execution.md`.

**Next session target:** Per the prioritization queue below, the natural next-up Codifier unit is **G7 / G2 / G9 re-synthesis** — the live-validation gate for IB-154 + IB-155 (Phase 1) AND IB-159 + IB-160 (Phase 3 detection paths) AND IB-163 (Phase 3 harvest-queue write-side) AND IB-162 (Phase 3 version-bump; if a re-synthesized guide's pattern findings include template-shaped content) AND IB-164 (Phase 3 queue-row promotion; downstream of IB-163's queue writes once Nick rules per-row). G7 is most overdue (+11 findings). Alternative: `/summarize-encounters` brainstorm if Nick has surfaced it. Nick gates next.

---

## Nick's Prioritizaton

Ordered queue. Status markers: `[nick-gate]` waits on Nick's ruling; `[deferred]` held by Nick, re-evaluate on trigger; `[trigger]` waits on external evidence or volume; `[don't-do-yet]` do not reintroduce until a specific upstream condition lands.

- **G7 / G2 / G9 re-synthesis** — top unblocked Codifier unit. G7 most overdue (+11 findings). All three are now fully Phase-1 + Phase-2 + Phase-3 lifecycle-aware after session 76: DD-93 preservation + DD-94 changelog (with 7-tag enum including `guide-split` and `theme-graduation`) on `/synthesize-guide`; DD-95 lifecycle pointer + DD-97 corpus-scan extension proposal + DD-100 template version-bump path on `/extract-artifacts`; DD-96 `/detect-drift` skill available; DD-98 split-trigger detection on `/synthesize-guide` Step 0.7 + `/identify-artifacts` Step 6.a; DD-99 graduation-trigger detection on `/identify-artifacts` Step 6.b; DD-101 co-occurrence harvest-queue scan on `/synthesize-guide` Step 4.7 + queue-row promotion on `/extract-artifacts` Step 0a / Step 4.8. Re-synthesis is the natural live-validation gate for the full lifecycle stack.
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
