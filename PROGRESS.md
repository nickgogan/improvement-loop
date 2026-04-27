# Improvement Loop — Progress

**Last Updated:** 2026-04-27 (session 82 close — G11 (Building Agentic Systems) initial synthesis from Agentic Systems theme: 29 findings absorbed, 7-row harvest queue queued; routing-table graduation complete)

## Current Focus

Codifier disposition. Session 82 graduated the **Agentic Systems theme to G11 (Building Agentic Systems)** — the cluster's first full-pass synthesis. Nick chose path (a) (graduate now + synthesize now in single pass) over (b) (defer + update routing table only) and (c) (everything mixed). Single G11 — no pre-decomposition into G11/G11b despite cluster heterogeneity. Skill spec's `>20 findings → split` flag noted as logged-for-future per DD-98 (no-op on initial synthesis).

**Outcomes:**

- **G11 initial synthesis complete.** 29 findings absorbed (2 P1 + 17 P2 + 9 P3 + 1 Not-Flagged) across 7 subtopic clusters (Maturity / Foundations / Substrate / Ingestion / Query / Proactive loops / Operations). 4 templates (vault scaffold, daily brief skill, time-window proactive loop, operator weekly cadence). 2 worked examples (MetaSystem itself; Fitness Learn-Plan-Act-Review). ~5,400 words (slightly over skill's 5K soft limit; logged-for-future). ContractSpec per DD-78; cross-refs G11 → G2/G7/G3b/G5/G9. Staged at `extracts/guides/building-agentic-systems.md`.
- **Routing-table graduation.** Agentic Systems theme moved from emerging-theme (former line 97) to G11 cluster row. Six surgical edits across `guide-routing-table.md`: Dimension→Guide mapping row with secondary guides (G7, Orchestration); Active Clusters row; Synthesis Status row (29 findings, 2026-04-27, `draft`); `specify` stage entry with broadened description ("agent or system"); 12 trigger keywords; Unrouted Bucket emptied. History entry appended.
- **Harvest queue queued.** `extracts/guides/building-agentic-systems.harvest-queue.md` with 7 candidate rows (5 rule + 1 skill + 1 template; 0 agent-shape suppressed per DD-82's three-layer enforcement). Queue file uses DD-101's full 9-field per-row block + 6-column summary-table format — **confirms session-81 SKILL.md Step 4.7 patch holds under live invocation** (positive case for IB-165 closure; closes session-81's "verify next regen-active session" follow-up).
- **29 findings back-annotated.** `pipeline_status: synthesized`; `consumed_by` appended with `building-agentic-systems.md`. Existing entries (G7 synthesis pointers, pattern-extraction artifacts) preserved. Subagent-executed; 55 edits clean on first attempt across format-variant files.
- **Single atomic commit `4218172`** covering 32 files (869+/57−): routing-table, G11 guide, G11 harvest queue, 29 back-annotated findings. Parallel `/extract-artifacts` session-82 work (8 modified findings, 7 untracked rule artifacts, IB-166, 2 SLs) deliberately left uncommitted per Nick's commit-scope (a) ruling.

### Session 82 parallel stream — `/extract-artifacts` IB-164 first execution (11 of 24 rows resolved)

The parallel /extract-artifacts session-82 stream made further progress beyond the snapshot captured in commit `4218172`. Final state at session pause:

- **Pre-execution contract bug surfaced + closed.** IB-163 vs IB-164 row-ID shape mismatch discovered at first invocation (the verification specifically flagged in IB-163 closure note (a)). Patched `/extract-artifacts/SKILL.md` inline: argument shape canonicalized to `<finding-stem>::<target-form>::<headline-slug>`; Step 0a step 2 auto-locates queue file by literal heading match across `extracts/guides/*.harvest-queue.md`; new optional `--guide <guide-stem>` disambiguation flag; failure-modes table + DD-101 row updated. **IB-166 filed and closed Done in-session.** End-to-end validation across 11 rows under the patched contract.
- **G9 rules: 8/8 complete** (Branch B, all wrote new artifacts): ship-only-what-at-least-one-human-comprehended, claudemd-symlink-to-agentsmd-at-every-governance-boundary, spec-and-code-reconcile-bidirectionally, every-recurring-review-comment-triages-to-mechanism-or-judgment, maximum-unreviewed-depth-policy, trust-promotion-and-demotion-thresholds, no-agent-action-without-identity-record, audit-log-append-only-never-overwritten.
- **G2 rules: 3/6 complete.** Rows 9 + 11 wrote new artifacts (`never-ask-claude-to-compact-claudemd`, `skills-reference-shared-context-by-path`). **Row 10 hit DD-97 Branch C** — first Branch-C event in `/extract-artifacts` harvest mode. Extension proposal filed at `operations/extension-proposals/2026-04-27-claudemd-global-rule-cap-extension-proposal.md` (primary match: existing rule `claudemd-minimum-viable-rule-only-add-globally-true-lines`); Codifier-recommended Option A (merge as extension); queue row stays `nick-approved` pending Nick's A/B/C ruling.
- **100% Codifier-recommendation accuracy across 10 written drafts.** Nick approved each as-written; no edits requested. Sample-size signal small but consistent with session-81 rulings-accuracy (still defer calibration conclusions until more data accumulates).
- **Net session-82 IB-164 deliverables:** 10 staged rule artifacts, 1 DD-97 extension proposal pending, IB-166, session-82 SL (`session-82-codifier-extract-artifacts-harvest-promotion-batch.md`), `/extract-artifacts/SKILL.md` patch, 10 source-finding back-annotations, queue-row updates across G9 (8 rows extracted) and G2 (2 rows extracted + 1 pending merge). Session paused after row 11 per Nick's call.

**Logged-for-future:**

1. **Bidirectional cross-refs on adjacent guides** — G2/G7/G3b/G5/G9 should have `[[building-agentic-systems]]` entries in their Related Guides sections too. G11 → others done; reverse pending. Trigger: hygiene pass or next regen of an adjacent guide.
2. **G11 word count over 5K limit** (~5,400) — skill flags this as "split or extract reference sections to appendices". Not blocking; address on first re-synthesis if it grows further.
3. **Agentic Systems data hygiene** — `flat-root-vault-with-property-based-organization` has `priority: Not Flagged` (should be P2 or P3). "P3 (Monitor)" vs bare "P3" taxonomy split across the cluster (5 vs 4 findings). Worth a sweep.
4. **DD-98 split-trigger watch** — G11's count threshold (≥25) is met today. On first re-synthesis, if practitioner-question bifurcation emerges (likely candidates: "design my system" vs "operate my system"), trigger may fire with both conditions met. Future-Nick decision per DD-98.
5. **Codifier reflection on calibration** — still deferred (was logged session 81); session 82 added no calibration data points (no Nick rulings occurred this session). Continue accumulating signal.

**Next session target:** Two-phase Codifier session — **(A)** rule on the 7 G11 harvest-queue rows, then **(B)** `/extract-artifacts` queue-row promotion (IB-164) across the consolidated approved pool (24 prior nick-approved from sessions 77–79's sweep + new G11 approvals from Phase A). DD-97 fires for rule/skill targets; DD-100 fires for template targets. Per IB-164 single-row contract: one `--harvest-row` invocation per row; sequential batching. Suggested batching: form-grouped (session-81-validated). **Handoff prompt** at `operations/handoffs/handoff-prompt-session-83-codifier-g11-rulings-ib-164-promotion.md`.

---

## Nick's Prioritizaton

Ordered queue. Status markers: `[nick-gate]` waits on Nick's ruling; `[deferred]` held by Nick, re-evaluate on trigger; `[trigger]` waits on external evidence or volume; `[don't-do-yet]` do not reintroduce until a specific upstream condition lands.

- **Session 83 two-phase plan (REVISED): G11 harvest rulings + IB-164 promotion of remaining 13 rows + Nick's Branch C ruling** — `[nick-gate]` top unblocked Codifier item per session-82 handoff. State updated post-session-82 close:
  - **Phase A**: rule on 7 G11 harvest-queue rows (5 rule + 1 skill + 1 template) at `extracts/guides/building-agentic-systems.harvest-queue.md`.
  - **Phase B**: `/extract-artifacts --harvest-row` promotion across remaining queue rows. **Original 24-row pool reduced to 13 remaining**: 0 G9 (all 8 rules complete + 2 G9 skills pending in skill batch); 4 G2 (3 rules remaining: rows 12-14 + 1 G2 skill + 2 G2 templates; row 10 handled separately under Nick's pending Branch C ruling); 5 G7 (3 rules + 2 skills). Plus new G11 approvals from Phase A.
  - **Phase C (new)**: Nick rules row 10's DD-97 extension proposal at `operations/extension-proposals/2026-04-27-claudemd-global-rule-cap-extension-proposal.md`. Options: A (merge into `claudemd-minimum-viable-rule-only-add-globally-true-lines`), B (draft `claudemd-global-rule-cap` as separate artifact), C (dismiss as redundant). Codifier-recommended: A. After ruling, the row's queue Status flips to terminal — `extracted` (with Resolution `merged into ...` for A or `extracted to ...` for B) or `nick-dismissed` for C.
  - DD-97 for rule/skill targets; DD-100 for templates. Per IB-164 single-row contract; sequential. Suggested batching: form-grouped (session-81-validated default; session-82 also validated with 8 G9 rules + 3 G2 rules complete). Handoff prompt prepared.
- **G2 vs G7 routing disambiguation audit** — `[trigger]` post-rebalance check. Both G2 (Managing Agent Context) and G7 (Session Persistence and Memory) now share `Context Engineering` in their routing-table Dimensions field; the prior discriminator (G7 also having "Memory Architecture") is gone. Disambiguation now lives entirely in stage (build vs operate), question text, and trigger-keyword table (lines 148-164). Functional but weaker. Trigger: if the next `/identify-artifacts` run mis-routes a finding between G2 and G7 (or queues an ambiguous one), spend a session formalizing the discriminator (e.g., explicit `lifecycle: build|operate` field on findings, OR a routing-rubric step that consults trigger keywords first when Dimensions overlap). Not urgent until evidence of misrouting.
- **Sub-dim 1.B graduation track monitoring** — `[trigger]` count-based. Post-rebalance, Sub-dim 1.B (Memory Isolation and Topology) has 4 explicit seed findings retained in Context Engineering; the 8 borderlines moved to Agentic Systems were system-shape, not isolation/topology mechanism, so 1.B count is unchanged. Graduation threshold is ≥10 findings. Trigger: re-evaluate cluster size after each `/research-loop` run that touches isolation/topology themes. Defer top-level Dim 12 candidacy until threshold met.
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
