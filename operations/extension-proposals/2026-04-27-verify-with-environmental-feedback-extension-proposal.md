---
title: "Extension Proposal — verify-with-environmental-feedback-not-self-assessment → agent-self-reporting-unreliability-independent-eval"
type: "extension-proposal"
target_system: "improvement-loop"
proposed_during: "session-83"
proposed_during_sl: "session-83-codifier-ib164-resume-extract-artifacts"
candidate_finding: "ground-truth-environmental-feedback-loops"
candidate_form: "rule"
candidate_headline: "verify-with-environmental-feedback-not-self-assessment"
candidate_harvest_row: "session-persistence-and-memory.harvest-queue.md::ground-truth-environmental-feedback-loops::rule::verify-with-environmental-feedback-not-self-assessment"
primary_match_artifact: "agent-self-reporting-unreliability-independent-eval.md"
primary_match_form: "rule"
status: "proposed"
governance: "DD-97 (calibration LLM-loose; propose-don't-decide invariant; auto-merge prohibition — Nick rules per proposal; this skill never auto-merges)"
date: "2026-04-27"
---

# Extension Proposal — verify-with-environmental-feedback-not-self-assessment

## Summary

Candidate rule `verify-with-environmental-feedback-not-self-assessment` (sourced from finding [[ground-truth-environmental-feedback-loops]]) overlaps with existing rule [[agent-self-reporting-unreliability-independent-eval]]. Both forbid relying on agent self-report as the verification path and require a structurally independent signal. The candidate extends the existing rule's scope from **task-completion verification** (stage: verify, end-of-task) to **per-step environmental feedback during execution** (stage: build, every decision point). Same Condition class, same anti-pattern, broader Action surface.

This proposal recommends Nick rule. The skill does not auto-merge per DD-97.

## Existing Rule (Primary Match)

**Artifact:** [[agent-self-reporting-unreliability-independent-eval]] (`extracts/rules/agent-self-reporting-unreliability-independent-eval.md`)
**Source finding:** `agent-self-reporting-unreliability-independent-eval`
**Mechanism:** Independent verification mechanism (test runner, linter, type checker, post-task hook) gates task-completion. No task is marked complete based solely on agent self-report.
**Stage:** verify (post-task gate)
**Enforcement surface:** at task-completion boundary — independent check runs before the task transitions to "done"; fails → flag, block, or fallback to human.

## Candidate Rule

**Source finding:** [[ground-truth-environmental-feedback-loops]]
**Source excerpt (Plain-English summary):** "LLMs confabulate about their own progress. Environmental ground truth provides an objective anchor that prevents agents from pursuing dead-end strategies. This is why coding agents (with test feedback) outperform agents in domains lacking objective verification signals."
**Codifier's reading:** Imperative directive — agents must consult environmental feedback (test runs, type-check output, linter results, runtime probes, structured logs) at every meaningful decision point during execution, not just at task completion. Self-assessment is rejected as a substitute. Builds on the existing rule's anti-self-report invariant by extending it from end-of-task to mid-task.
**Mechanism:** Continuous environmental feedback — at each decision point (after each tool call, before each next-step planning, after each subagent return), the agent consumes ground-truth signal (run tests, check types, probe filesystem, observe logs) and adjusts plan accordingly. Self-narrated progress without environmental ground-truth is forbidden as a planning input.
**Stage:** build (during execution)
**Enforcement surface:** at every loop iteration / decision point — structural property of the agent's execution loop; reviewable from session logs (does the agent pause to consult ground truth before each plan-step, or does it self-narrate?).

## Overlap Analysis

| Dimension | Existing Rule | Candidate |
|-----------|---------------|-----------|
| Anti-pattern targeted | Agent self-attestation as verification | Agent self-narration as planning input |
| Required signal | Independent post-task check | Continuous environmental feedback |
| When fired | Task-completion boundary (single gate) | Every decision point during execution (continuous) |
| Stage | verify | build |
| Detection | Self-report not externally validated → block completion | Self-narration without ground-truth probe → flag plan as ungrounded |
| Independent or layered | Independent — final gate | Layered — per-step backstop preventing dead-end pursuit |
| Failure mode without rule | Agent claims success, downstream consumes broken output | Agent pursues dead-end strategy for many steps, wastes budget, lands at task end with self-attested "complete" that fails the existing rule's gate |

Both are anti-confabulation mechanisms. The candidate is a *per-step backstop* to the existing rule's *task-end gate*: ground-truth feedback during execution catches the dead-end-pursuit failure mode early; the task-end gate catches anything that slips through. Together they bracket execution at both ends.

## Three Possible Resolutions

### Option A — Merge as extension (recommended for review)

Amend the existing rule to integrate the candidate's per-step environmental-feedback obligation as a second mechanism. The merged rule would carry both:
- Per-step environmental feedback during execution (stage: build) — agent consumes ground-truth signal at every decision point.
- Independent post-task verification (stage: verify) — independent check gates task completion.

The merged rule's title might shift (e.g., "Agent Self-Report Is Insufficient — Environmental Feedback During Execution and Independent Verification at Completion"). The candidate's source finding would join the existing rule's `source_finding` (or be noted as a contributing source). Stage field becomes a list `[build, verify]` or the rule's stage is captured as the broader anti-confabulation discipline applied at both surfaces.

**Pros:** Single rule covering one anti-pattern at both temporal surfaces (during + after); complementary mechanisms in one place; reduces rule-count fragmentation; the two failure modes (mid-task dead-end pursuit + end-of-task false-attestation) are each other's complement.
**Cons:** Larger artifact; two stage values is mildly awkward to express in a single rule; merging shifts the existing rule's framing from "post-task gate" to "anti-confabulation discipline," which is a meaningful re-scoping that subsequent consumers will need to internalize.

### Option B — Separate rule

Draft `verify-with-environmental-feedback-not-self-assessment` as an independent artifact. The existing rule covers the post-task gate; the new rule covers per-step feedback. The two cross-reference each other via `related_findings` or a body-level `See also` block.

**Pros:** Each rule has one mechanism, one stage, one enforcement surface — cleaner separation; consumers can adopt one without the other (e.g., a project with strong end-of-task gates but no per-step environmental loop adopts the new rule independently).
**Cons:** Two artifacts targeting the same anti-pattern; cross-reference burden; possible drift between them; the conceptual unity ("agent self-report is unreliable") is fragmented across two artifacts.

### Option C — Reject the candidate as redundant

Treat the candidate's per-step feedback obligation as inline guidance covered implicitly by the existing rule's post-task gate (the argument: if an agent runs into dead ends, the post-task gate will flag the failure, so per-step feedback is descriptive rather than independently required). Mark the queue row as nick-dismissed.

**Pros:** Smallest artifact set; the existing rule, strictly applied, eventually catches the failures.
**Cons:** Discards the per-step backstop; the existing rule fires only at task-end, by which point the agent has burned execution budget pursuing the dead-end strategy; per-step feedback is the cheaper, earlier signal; "coding agents outperform agents lacking objective verification signals" is direct evidence that per-step feedback is not equivalent to post-task verification — they have measurably different effects.

## Recommendation

The Codifier recommendation is **Option A (merge as extension)**. The two mechanisms are the same discipline applied at different temporal surfaces; they are not independent claims about different problems. Merging captures the conceptual unity. Calibration is genuinely LLM-loose; reasonable readers could prefer Option B given the clean stage-separation argument. Nick rules.

## Procedure for Application (per DD-97)

If Nick rules **Option A (merge)**: manually amend `extracts/rules/agent-self-reporting-unreliability-independent-eval.md` to integrate the per-step environmental-feedback mechanism (the skill does not auto-merge per DD-97 v1; auto-merge is prohibited at Step 1.7). After the manual merge lands, re-invoke `/extract-artifacts --harvest-row session-persistence-and-memory.harvest-queue.md::ground-truth-environmental-feedback-loops::rule::verify-with-environmental-feedback-not-self-assessment` so Step 4.8 flips the queue row Status to `extracted` and Resolution to `merged into [[agent-self-reporting-unreliability-independent-eval]]`.

If Nick rules **Option B (separate)**: re-invoke `/extract-artifacts --harvest-row ...` against this row WITH the explicit ruling that no extension applies; the skill drafts and writes `verify-with-environmental-feedback-not-self-assessment.md` as a standalone artifact; Step 4.8 flips Status to `extracted` and Resolution to `extracted to [[verify-with-environmental-feedback-not-self-assessment]]`.

If Nick rules **Option C (dismiss)**: invoke `/extract-artifacts --harvest-dismiss session-persistence-and-memory.harvest-queue.md::ground-truth-environmental-feedback-loops::rule::verify-with-environmental-feedback-not-self-assessment`; Step 4.8 Branch A flips Status to `nick-dismissed` and Resolution to `dismissed`.

## Status

Pending Nick's ruling. Queue row remains `nick-approved` (per DD-101 Branch C); Resolution remains blank in the queue file pending merge or alternative resolution. This proposal is the audit-trail record of the extension scan.
