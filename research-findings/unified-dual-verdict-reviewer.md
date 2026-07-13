---
name: "Unified Dual-Verdict Reviewer Supersedes Two-Stage Review"
summary: |-
  Plain English: instead of dispatching two sequential review subagents per task (one
  for spec compliance, one for code quality), dispatch ONE reviewer that reads the diff
  once and returns BOTH verdicts — plus an explicit "cannot verify from diff" verdict
  for requirements living in untouched code, which route back to the controller.
  Superpowers v6.0.0 collapsed its two-stage per-task review into a single
  task-reviewer-prompt.md with dual verdicts; one fix pass clears both. Upstream evals:
  similar quality, roughly 2x faster, ~50% fewer tokens than v5.x. Per-task review
  became a narrow task-scoped gate, with breadth concentrated in ONE whole-branch
  review at the end on the most capable model. Supersedes the architecture recorded in
  the KB's two-stage-sequential-review finding.
implementation_notes: null
category: "Orchestration"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: "P3 (Monitor)"
applicability:
  - "General"
adopted_in: []
sources: []
related_findings:
  - file: "two-stage-sequential-review.md"
    rel: "contradicts"
  - file: "superpowers-plugin-spec-driven-sub-agent-orchestra.md"
    rel: "extends"
  - file: "headless-multi-pass-iterative-review.md"
    rel: "same-problem"
  - file: "externalized-real-session-behavior-evals.md"
    rel: "enabled-by"
  - file: "review-triage-admissible-scope-authority.md"
    rel: "same-problem"
  - file: "two-axis-parallel-code-review-standards-vs-spec.md"
    rel: "contradicts"
proposals: null
date_discovered: "2026-07-13"
last_updated: "2026-07-13"
pipeline_status: "raw"
consumed_by: []
tags:
  - "orchestration"
  - "evaluation"
  - "review-architecture"
  - "supersession"
---

# Unified Dual-Verdict Reviewer Supersedes Two-Stage Review

## What It Is

A review-architecture revision from the framework that popularized per-task two-stage
review:

1. **One reviewer, two verdicts.** `task-reviewer-prompt.md` reads the task's diff once
   and returns a spec-compliance verdict AND a code-quality verdict in one structured
   report. The deleted `spec-reviewer-prompt.md` / `code-quality-reviewer-prompt.md`
   pair each re-read the same diff in separate contexts.
2. **A third verdict for the unverifiable.** "⚠️ cannot verify from diff" marks
   requirements that live in code the diff doesn't touch; those route back to the
   controller to resolve rather than being silently passed or failed.
3. **Cost re-architecture.** One fix subagent clears both verdicts per round; breadth
   moves to a single end-of-branch review on the most capable model, fed a full-branch
   review package. Upstream's evals: similar quality, ~2x faster, ~50% fewer tokens
   than the v5.x flow.

Reviewer independence survives the merge: the unified reviewer is read-only,
skeptical-by-instruction ("Do Not Trust the Report"), and findings need file:line
evidence.

## Why It Matters

The two-stage pattern spread widely on the intuition that separated concerns review
better. This is the source framework reversing itself with eval evidence: the second
context added token cost and latency, not catch rate — the diff is the same, and one
capable reviewer can hold two rubrics. The durable lessons are (a) concern-separation
in review pays at the *independence* boundary (reviewer vs implementer, reviewer vs
controller), not at the rubric boundary; and (b) the honest third verdict —
"unverifiable from what I was shown" — is what keeps a narrower review scope from
silently converting invisibility into approval.

## Why People Are Using It

Shipped as the core of Superpowers' v6.0.0 subagent-driven-development rewrite, with
before/after eval evidence published in its release notes; the framework dogfooded the
redesign through its own spec/plan workflow. Source: Observed in
[superpowers](https://github.com/obra/superpowers) v6.1.1 — see
[[superpowers-analysis]] for structural details. Supersedes the architecture recorded
in [[two-stage-sequential-review]].

## Potential Alternatives

- **Two-stage sequential review** — the superseded shape; still defensible when the two
  rubrics need different context (e.g., spec review against docs the quality reviewer
  shouldn't see).
- **Parallel multi-lens review** (reviewer rosters) — many concerns, many subagents;
  scales rubric coverage at multiplied cost, fits stakes-calibrated gates.
- **Single end review only** — cheapest; loses the per-task gate that keeps fix loops
  small.

## Potential Improvements

- Verdict-schema standardization so controllers can route mixed outcomes (spec ✅ /
  quality ❌ / unverifiable ⚠️) mechanically.
- Measuring where dual-rubric attention saturates — at what diff size does one
  reviewer start missing what two caught?

## Potential Failure Modes

- **Rubric bleed** — one context can let spec-compliance framing soften quality
  judgment or vice versa; the separated design had structural immunity.
- **⚠️-verdict dumping** — an overloaded reviewer can route too much to "cannot
  verify," pushing verification burden back onto the controller.
- **End-review overload** — concentrating breadth in one whole-branch review makes
  that single pass a large-context, single-point-of-failure gate.
