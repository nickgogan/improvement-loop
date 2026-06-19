---
title: "Session 84 — Codifier: Parallel-session reconciliation + DD-97 sweep ruling on 3 accumulated proposals (all Option A applied)"
type: "system-log"
target_system:
  - "improvement-loop"
actor: "Claude (Codifier disposition)"
area: "harvest-queue / dd-101 / dd-97 / extension-proposals / ib-164 / session-reconciliation / calibration"
change_type: "Update"
milestone: null
rationale: "Two-phase Codifier session per the piped session-84 handoff. **Phase 1**: reconciled parallel-session outputs from session 83 — confirmed canonical session-83 SL is correct; the two 'untracked' SLs Nick flagged were complementary DD-59 single-change SLs (queue-hygiene stream), not orphaned session-83 drafts; the parallel session's PROGRESS.md queue-prune had already been absorbed into session 83's commit (9e0524b); the still-uncommitted complementary work (2 SLs + PROGRESS.md +2 Key Files rows + guide-routing-table.md Disambiguation Notes section) was committed as its own atomic commit `8515af8` ahead of Phase 2 per Nick's Option 1 choice. **Phase 2**: swept all 3 accumulated DD-97 Branch-C extension proposals (rows 10, 12, 16) — Nick ruled Option A on all 3 (3/3 calibration match with Codifier's recommendations); Codifier drafted merge-amendments for Nick's gate (default structural choices proposed: Row 10 keep frontmatter title, Row 12 broader title shift, Row 16 broader title + stage list); Nick approved defaults with 'go'; Codifier applied 3 manual amendments to existing rule artifacts + 3 source-finding `consumed_by[]` back-annotations + 3 extension-proposal status flips to 'applied' + 2 queue file updates (G2 rows 10+12; G7 row 16) — all in one batch; atomic-write invariant verified post-batch (G2: 9 extracted per-row blocks ↔ 9 extracted summary-table rows; G7: 5 ↔ 5; zero nick-approved leftover). IB-164 `/extract-artifacts --harvest-row` promotion path is now **fully complete for the current 4-guide harvest-queue corpus** (G2 + G7 + G9 + G11). Single combined atomic commit at session close covers Phase 2's outputs."
source_dd: "DD-29, DD-78, DD-92, DD-95, DD-97, DD-101, IB-164"
date: "2026-04-27"
session: 84
tags:
  - "system-log"
  - "codifier"
  - "harvest-queue"
  - "dd-97"
  - "dd-101"
  - "ib-164"
  - "extension-proposal"
  - "merge-applied"
  - "session-reconciliation"
  - "calibration"
  - "g2"
  - "g7"
---

# Session 84 — Codifier: Parallel-session reconciliation + DD-97 sweep ruling

## Summary

| Phase | Scope | Outcome |
|---|---|---|
| 1 — Reconciliation | Parallel session-83 outputs (2 untracked SLs + working-tree edits) | Canonical session-83 SL confirmed; parallel queue-hygiene work committed as own atomic commit `8515af8`; no divergence; no load-bearing content missing |
| 2 — DD-97 sweep | 3 accumulated Branch-C proposals (rows 10, 12, 16) | All ruled Option A (merge); 3 manual amendments applied; 3 queue rows flipped to `extracted`; atomic-write invariant verified |

**Net delta:**

- 3 existing rule artifacts amended (Row 10: `claudemd-minimum-viable-rule-only-add-globally-true-lines`; Row 12: `never-ask-claude-to-compact-claudemd`; Row 16: `agent-self-reporting-unreliability-independent-eval`)
- 3 source findings back-annotated (`consumed_by[]` extended; "Extraction Note — 2026-04-27 (Session 84)" appended)
- 3 extension-proposal files status-flipped to `applied` with ruling metadata + body Status section updated
- 2 queue files updated (G2: rows 10+12; G7: row 16) — Status `nick-approved → extracted`, Resolution `merged into [[<existing>]]`, session-84 footer appended below the prior session-82/83 pending-merge annotation
- DD-95 lifecycle pointers updated on all 3 amended artifacts (`last_change_session: 84`, `last_change_sl: session-84-codifier-reconcile-and-dd97-sweep`)
- 1 separate atomic commit (`8515af8`) for Phase 1 reconciliation work

## Phase 1 — Parallel-session reconciliation

### Findings

- **Session-83 canonical SL** at `operations/system-log/session-83-codifier-ib164-resume-extract-artifacts.md` (committed in `9e0524b`) — describes the IB-164 work: 18 artifacts + 2 new Branch-C proposals. Content matches the commit's file list. Confirmed canonical.
- **Two untracked SLs** Nick flagged were NOT orphaned session-83 drafts. They are DD-59 single-change operational-learning SLs documenting a complementary parallel queue-hygiene stream:
  - `dropped-summarize-encounters-from-il-priority-queue.md` — `/summarize-encounters` skill build line dropped (zero producer-side data after 27 sessions; mechanism-on-zero-occurrence)
  - `swept-il-priority-queue-five-entries-dropped-disambiguation-note-lifted.md` — 5 trigger-gated queue entries dropped (Sub-dim 1.B graduation, G2/G7 disambiguation, retroactive ~100-extract migration, use-case-registry weight calibration, agent.md variant-depth iteration); G2/G7 disambiguation note lifted to `guide-routing-table.md` Disambiguation Notes section.
  Naming convention (`dropped-*` / `swept-*` rather than `session-83-*`) was intentional — these are single-change SLs, not session-narrative SLs.
- **Working-tree edits at Phase 1 start**:
  - `PROGRESS.md` +2 Key Files rows (extension-proposals/ + version-bump-proposals/ pointers)
  - `guide-routing-table.md` +8 lines (Disambiguation Notes section with G2/G7 weakened-discriminator note)
  - 2 untracked SL files
  - 2 untracked handoff prompts (session-83 + session-84) — left for session-close commit handling
- **Critical observation:** the parallel session's PROGRESS.md queue-prune (6 dropped queue items across the two SLs) had already been absorbed into session 83's commit (`9e0524b`). The committed PROGRESS.md correctly reflected the post-prune `Nick's Prioritizaton` state (3 items: DD-97 sweep, subagent discipline, visualization brainstorm). No load-bearing content was missing or duplicated.

### Resolution

Per Nick's choice ("Option 1 please" — separate atomic commit before Phase 2), the parallel queue-hygiene work was committed as commit `8515af8`: 2 SLs + PROGRESS.md +2 Key Files rows + guide-routing-table.md Disambiguation Notes section. The 2 untracked handoff prompts were not bundled (they're session-bridge artifacts; out of scope for the queue-hygiene narrative). Working tree clean ahead of Phase 2.

## Phase 2 — DD-97 sweep ruling

### Cadence

Sweep then batch-apply (Option 1 per session-84 handoff cadence options). Nick ruled all 3 proposals at once with `agreed with all, please proceed`. Codifier drafted merge-amendments concurrently and presented them as concise structural plans for Nick's gate; Nick approved the proposed defaults (`go`); Codifier applied amendments + queue write-backs + back-annotations + proposal status flips in a single batch; atomic-write invariant verified before commit. The handoff's "stop at first divergence from Option A" hedge did not fire — all 3 rulings were uniform.

### Per-row outcomes

| Row | Source finding | Existing rule (merge target) | Ruling | Codifier reco match? |
|---|---|---|---|---|
| 10 (G2) | `claudemd-context-rot-from-indiscriminate-rule-accu` | `claudemd-minimum-viable-rule-only-add-globally-true-lines` | Option A | yes |
| 12 (G2) | `ace-delta-updates-over-monolithic-rewrites` | `never-ask-claude-to-compact-claudemd` | Option A | yes |
| 16 (G7) | `ground-truth-environmental-feedback-loops` | `agent-self-reporting-unreliability-independent-eval` | Option A | yes |

**Calibration: 3/3 Codifier-reco match (100%).**

### Per-amendment structural changes

**Row 10 — `claudemd-minimum-viable-rule-only-add-globally-true-lines.md`**

- **Title.** Frontmatter `title` preserved (rule's core identity is the per-line test); body H1 subtitled `"— Per-Line Truth Test + Volume Cap"`.
- **Action section.** New `**Volume cap (operate-stage backstop):**` subsection added between `**Permitted alternatives:**` and `## Boundary` — Tier-0 (global `~/.claude/CLAUDE.md`): 3-5 lines hard cap; Tier-1 (per-project `CLAUDE.md`): 60-80 line band soft band; framed as a structural backstop to the per-line test, not a replacement.
- **Enforcement section.** New deterministic check `line_count(file) ≤ tier_cap` (Tier-0: 5; Tier-1: 80); violations surface as file-write-time warning or periodic audit flag.
- **Rationale section.** Appended paragraph framing the volume cap as an operate-stage backstop to the specify-stage per-line test — captures the failure mode where the per-line test was misapplied and accumulated drift would otherwise go unsignaled.
- **Frontmatter deltas.** `contributing_sources: [claudemd-context-rot-from-indiscriminate-rule-accu]` added; `last_change_session: 66 → 84`; `last_change_sl: session-66-codifier-ib-150-acceptance-test → session-84-codifier-reconcile-and-dd97-sweep`; `contract.invariants` extended with the volume-cap invariant.
- **Body Contract.Invariants.** Extended to mirror the YAML invariants (the cap stays within range independent of the per-line test result).

**Row 12 — `never-ask-claude-to-compact-claudemd.md`**

- **Title.** Shifted from `"Never Ask the Model to Compact Its Own Context File — Catastrophic-Collapse Prevention Rule"` to `"Evolving Load-Bearing Documents: No In-Place LLM Rewrite + Delta-Update Discipline"` (frontmatter + body H1). Meaningful re-scoping per the proposal's noted Cons; broader title reflects the merged rule's expanded scope.
- **Condition section.** Generalized from "context file" language ("CLAUDE.md, AGENTS.md, system-prompt files") to "load-bearing evolving documents" (PROGRESS.md, playbooks, accumulated notes). Condition now fires both on compact/summarize/rewrite contemplation AND on the more general question of how to update an evolving document.
- **Action — Required (negative-space).** Existing list of bounded-failure mechanisms preserved.
- **Action — Required (positive-space).** New fully-specified delta-update mechanism subsection promoted from the existing rule's passing reference to ACE-style voting curators. Four named steps: (1) Append structured delta entries (each with date/session/source/type, independently citable and revertable); (2) Periodic non-LLM consolidation (deterministic merge logic preserves source attribution; LLM never as merge writer); (3) Grow-and-refine (deterministic semantic-similarity rules or human review; LLM advisory but never writer); (4) Multi-epoch refinement (additive — new delta entries — rather than rewriting prior entries in place). Delta-update positioned as the *named, specified* canonical alternative; voting/clear-rebuild/human-edit remain valid bounded-failure alternatives.
- **Action — Forbidden.** Extended to name brevity-bias detail loss as a parallel failure mode alongside catastrophic collapse — "succeeds with subtle detail loss (silent erosion) or destroys accumulated content entirely (catastrophic collapse)."
- **Boundary section.** Generalized to all load-bearing evolving documents.
- **Rationale section.** Extended with two-failure-mode framing: catastrophic collapse (unbounded; primarily CLAUDE.md/AGENTS.md/system-prompt) AND brevity-bias detail loss (every LLM-driven rewrite; cumulative across iterations). Added the ACE finding's quantitative evidence (86.9% lower adaptation latency, 83.6% lower rollout cost) as direct cost evidence of the rewrite path even at non-catastrophic baselines. Positive invariant restated for broader scope.
- **Failure modes.** 2 new entries: (a) "Brevity bias on smaller-than-collapse rewrites" (every LLM rewrite drops domain-specific details across iterations; document's information density quietly halves over several "successful" rewrites; mitigation: delta-update by construction); (b) "'Just consolidate it for me' framing" (consolidation is bounded-failure only when merge logic is deterministic; LLM-driven consolidation re-introduces brevity bias regardless of framing).
- **Frontmatter deltas.** `contributing_sources: [ace-delta-updates-over-monolithic-rewrites]` added; `last_change_session: 82 → 84`; `last_change_sl` updated; `applies_to` generalized to "load-bearing evolving documents"; tags extended (`ace`, `delta-updates`, `evolving-docs`); `contract.invariants` extended with delta-update mechanism + scope generalization.
- **Body Contract.Invariants.** Extended to mirror the YAML invariants.

**Row 16 — `agent-self-reporting-unreliability-independent-eval.md`**

- **Title.** Shifted from `"Agent Self-Reporting Unreliability and Independent Evaluation Requirement"` to `"Agent Self-Report Is Insufficient: Environmental Feedback During Execution + Independent Verification at Completion"`. Meaningful re-scoping per the proposal's noted Cons; broader title captures both temporal surfaces.
- **Condition section.** Broadened to fire at two temporal surfaces: (1) task-completion (verify stage) — existing; (2) during execution (build stage) — new — at every meaningful decision point where the agent could consult environmental signal versus proceed on self-narration. Decision points enumerated: after each tool call, before each next-step planning, after each subagent return, before each significant state mutation.
- **Action section.** Existing post-task gate preserved as `**Required (verify stage — post-task gate):**`. New `**Required (build stage — per-step environmental feedback):**` subsection added — 4 specific decision-point obligations, plus the explicit prohibition of self-narrated progress without environmental probe as a planning input. Compose statement: "per-step environmental feedback catches dead-end pursuit early during execution; the post-task gate catches anything that slips through. Together they bracket execution at both ends."
- **Boundary section.** Existing 4 surfaces preserved; new `**Agent execution loops:**` surface added (per-step environmental probes preceding plan-step decisions; reviewable from session logs). Trailing scope paragraph: "rule applies at every surface where agent state transitions are made — both task-completion boundaries (verify stage) and per-step decision points within execution (build stage). It does NOT apply to internal reasoning that the agent surfaces as transparent monologue."
- **Enforcement section.** Existing 3 enforcement mechanisms preserved; new "Per-step environmental-feedback enforcement" item added — reviewable from session logs; self-narration without preceding tool call → flag plan as ungrounded.
- **Rationale section.** Extended with the per-step-vs-post-task distinction: post-task gate alone is insufficient because by the time it fires, agent has burned execution budget pursuing dead-end. Per-step feedback catches the failure earlier at cheaper end of cost curve. Coding-agent verification-signal evidence cited (Anthropic framing on coding-agent outperformance in domains lacking objective verification signals) as direct evidence the two are not equivalent.
- **Frontmatter deltas.** `contributing_sources: [ground-truth-environmental-feedback-loops]` added; `last_change_session: 44 → 84`; `last_change_sl` updated; `applies_to` extended with "agent execution loops where ground-truth environmental signals are available at decision points"; `stage` shifted from `"verify"` to `["build", "verify"]`; tags extended (`environmental-feedback`, `ground-truth`); `contract.invariants` extended.
- **Body Contract.Invariants.** Extended with 2 new bullets (decision-point ground-truth consultation; self-narration prohibition as planning input).

### Files touched

**Existing rule artifacts amended (3):**
- `extracts/rules/claudemd-minimum-viable-rule-only-add-globally-true-lines.md`
- `extracts/rules/never-ask-claude-to-compact-claudemd.md`
- `extracts/rules/agent-self-reporting-unreliability-independent-eval.md`

**Source findings back-annotated (3):**
- `research-findings/claudemd-context-rot-from-indiscriminate-rule-accu.md`
- `research-findings/ace-delta-updates-over-monolithic-rewrites.md`
- `research-findings/ground-truth-environmental-feedback-loops.md`

**Extension proposals status-flipped to `applied` (3):**
- `operations/extension-proposals/2026-04-27-claudemd-global-rule-cap-extension-proposal.md`
- `operations/extension-proposals/2026-04-27-evolving-docs-use-delta-updates-extension-proposal.md`
- `operations/extension-proposals/2026-04-27-verify-with-environmental-feedback-extension-proposal.md`

**Queue files updated (2):**
- `extracts/guides/managing-agent-context.harvest-queue.md` (rows 10 + 12 — table + per-row blocks)
- `extracts/guides/session-persistence-and-memory.harvest-queue.md` (row 16 — table + per-row block)

### Atomic-write invariant verification

| Queue | Per-row blocks `extracted` | Summary-table rows `extracted` | `nick-approved` leftover |
|---|---|---|---|
| G2 | 9 | 9 | 0 |
| G7 | 5 | 5 | 0 |

Verified post-batch via grep. All 3 session-84 footers present in the queues (`Session 84 — [[session-84-codifier-reconcile-and-dd97-sweep]]` — 2 in G2, 1 in G7). Resolutions correctly populated with `merged into [[<existing-stem>]]` link.

## IB-164 path closure

After Phase 2, the IB-164 `/extract-artifacts --harvest-row` promotion path is **fully complete for the current 4-guide harvest-queue corpus** (G2 Managing Agent Context, G7 Session Persistence and Memory, G9 Agent Governance and Trust, G11 Building Agentic Systems). Cumulative artifacts produced from the corpus across sessions 82-84:

| Form | Branch-B (new) | Branch-C (merged) | Total |
|---|---|---|---|
| Rule | 19 (10 from session 82 + 9 from session 83) | 3 (session 84) | 22 |
| Skill | 6 (session 83) | 0 | 6 |
| Template | 3 (session 83) | 0 | 3 |
| **Total** | **28** | **3** | **31** |

All accumulated DD-97 Branch-C proposals across sessions 82-84 are resolved (3/3 ruled Option A; 3/3 applied).

**Next harvest-queue activity** depends on either (a) a new `/research-loop` adding pattern findings whose bodies contain embedded artifact-shaped content, or (b) a guide regen via `/synthesize-guide` re-detecting embedded prose in evolved findings. No queue work is currently outstanding.

## DD-97 calibration trends (cumulative)

| Session | Rules drafted | Branch-C proposals | Branch-C rate | Codifier-reco rulings (Nick) |
|---|---|---|---|---|
| 82 | 11 | 1 (row 10) | 9% | (pending until session 84) |
| 83 | 11 | 2 (rows 12, 16) | 18% | (pending until session 84) |
| 84 | 0 (all rulings; 0 new drafts) | 0 (all applied) | n/a | 3/3 ruled Option A (Codifier-reco match) |
| **Cumulative 82-84** | **22** | **3** | **14%** | **3/3 (100%) Codifier-reco match** |

Calibration trends loose-but-actionable per DD-97 §Out of scope. Tightening to (ii) ContractSpec-overlap-structured or (iii) hybrid remains deferred until accumulated false-positive volume justifies it. Cumulative false-positive volume so far: 0 (all 3 Branch-C proposals were ruled Option A as recommended; none ruled "create new" or "dismiss"). DD-97 v1 calibration is empirically validated at this scale.

## Procedural notes

- **Edit tool stale-read failures** (recurring from session 83) — mitigated this session by going strictly sequential within each artifact's edits (no parallel Edits to the same file). All 21 sequential Edits to the 3 amended artifacts succeeded without stale-read failures. Procedural pattern worth recording: when applying multiple structural edits to a single file, sequence them within a single message rather than parallelizing.
- **One header-duplication recovery** mid-session: an Edit on `agent-self-reporting-unreliability-independent-eval.md` accidentally introduced a duplicate `## Boundary` heading (the new bullet list got orphaned above the new header). Caught immediately via Read; fixed in one corrective Edit. Surfacing as a procedural data point — when an Edit's `old_string` includes a section header, careful boundaries on `new_string` matter.

## Logged-for-future (carryover from session 83)

1. **Subagent queue-mutation discipline architectural decision** — still deferred. Session 83 saw subagents disregard "do not touch queue file" instruction; row 13's subagent went the full SKILL.md Step 4.8 distance (matches design intent). Architectural choice: (a) drop orchestrator-batched plan — make subagents fully responsible for queue + back-annotation + artifact write end-to-end (aligns with SKILL.md Step 4.8); (b) tighten subagent prompt with defensive abort if queue pre-state matches own row. Trigger: next bulk-promotion workflow OR governance audit. Option (a) likely correct.
2. **Bidirectional cross-refs hygiene pass** (carryover from session 82). G2/G7/G3b/G5/G9 should have `[[building-agentic-systems]]` entries in their Related Guides sections.
3. **Codifier reflection on calibration** — still deferred. Cumulative S81 (38) + S82 (10) + S83 (18) + S84 (3 merge-applies) Branch-B verdicts where Codifier recommended `new` and Nick has not overruled, plus 3/3 Branch-C verdicts ruled per Codifier's Option A recommendation.
4. **DD-98 split-trigger watch** on G11's first re-synthesis. Count threshold met (≥25 findings).
5. **Edit-tool race conditions with subagent + linter mutations** (procedural pattern worth recording). This session validated the sequential-edits workaround for orchestrator-direct execution; the pattern still needs codification for subagent-batched workflows.

## Session telemetry

- **model:** claude-opus-4-7[1m]
- **context_window_size:** 1,000,000
- **turns:** ~6 user↔assistant exchanges
- **tool_calls:** ~35 (sequential Edits + Reads + grep verifications + 1 atomic Phase-1 commit + 1 atomic Phase-2 commit pending)
- **subagents:** 0 (orchestrator-direct execution)
- **bulk-edits via Python:** 0 (sequential Edit tool calls were sufficient at this scale)
- **harness:** claude-code-cli-cursor-macos
- **capture_quality:** estimated
- **parallel_session:** no (single Codifier session)
