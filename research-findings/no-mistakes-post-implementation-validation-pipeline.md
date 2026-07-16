---
name: 'Post-Implementation Validation Pipeline (No-Mistakes: Worktree → Intent → Rebase → Adversarial Review → Evidence → Risk-Gated Human Review)'
summary: 'Plain English: instead of a human reviewing every AI diff (the velocity hard-cap) or

  trusting the agent''s "done," route every first-pass change through a fixed validation

  pipeline before it becomes a PR. Kun Chen''s open-source "no mistakes" pipeline: (1)

  branch/commit, then run everything in an isolated worktree so validation never touches

  the working repo; (2) extract the *real intent* behind the change by analyzing the

  agent session that produced it; (3) rebase onto latest main first, resolving conflicts

  up front; (4) adversarial review in its own fresh context window — obvious problems

  self-correct, ambiguous ones with product implications escalate to the human; (5) test

  end-to-end against the original intent, recording evidence artifacts (screenshot,

  video, log) attached to the PR as proof-of-done; (6) docs pass + lint, raise the PR,

  then babysit it (incoming conflicts, CI failures) until merge. The PR carries a risk

  assessment that gates how deeply the human reviews: low-risk changes get no diff read

  at all.'
implementation_notes: 'The engine''s closest analogue is assess-* audits of artifacts, but nothing pipelines

  post-change validation with evidence artifacts and risk-gated review depth. Candidate

  design input for the restructure program''s harness phase: intent-extraction-from-

  session and evidence-artifact-attached-to-output are the two stages the engine lacks

  entirely. The adversarial fresh-context stage is independent corroboration of

  governance rule 10 (generator-assessor separation) — recorded as one-way links; those

  findings are owned by another lane this session.'
category: Evaluation
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- IL (validation harness design, audit pipeline)
- General
adopted_in: []
sources:
- l8-principals-agentic-engineering-workflow.md
related_findings:
- file: context-pollution-same-window-verification-bias.md
  rel: extends
- file: generator-assessor-separation-in-skill-iteration.md
  rel: same-problem
- file: agent-self-reporting-unreliability-independent-eval.md
  rel: same-problem
- file: holdout-validation-pattern-blind-regression.md
  rel: same-problem
- file: tiered-review-escalation-strategy.md
  rel: same-problem
- file: worktree-isolation-for-parallel-agent-sessions.md
  rel: enabled-by
proposals: null
date_discovered: '2026-07-12'
last_updated: '2026-07-12'
pipeline_status: synthesized
consumed_by:
- building-agent-evaluation-suites.md
---

## What It Is

A fixed, orchestrated pipeline that takes an agent's first-pass code "all the way through
to a clean PR" — triggered by handing the change to the pipeline (or invoking it as a
skill) instead of opening the diff. Stages, in order:

1. **Worktree isolation** — branch + commit, then all validation runs in an isolated
   worktree; nothing can affect the current repo state.
2. **Intent extraction** — the pipeline analyzes the agent session that produced the
   change to recover the real intent, so validation targets what was *asked for*, not
   what was built.
3. **Rebase-first** — rebase onto latest remote main and resolve merge conflicts before
   any review, so review sees the code that will actually land.
4. **Adversarial fresh-context review** — a reviewer in its own fresh context window
   ("this is where most problems get caught"). Obvious problems are self-corrected;
   ambiguous ones with product implications are escalated to the human for a decision.
5. **End-to-end test against intent, with evidence** — the change is exercised against
   the recovered intent and evidence is recorded (screenshot, video demo, log file —
   whatever most directly shows the change working) and attached to the PR.
6. **Documentation pass, lint, PR, babysitting** — docs updated to reflect the change,
   lint clean, branch pushed, PR raised; the pipeline then watches the PR for incoming
   merge conflicts and CI failures until merge.

The PR body summarizes original intent, what changed, how it was tested, what the
pipeline found and fixed, and a **risk assessment** the human uses to calibrate review
depth — "for low-risk changes, I don't really look at the diff at all."

## Why It Matters

It resolves the reviewer hard-cap without surrendering quality control: "AI writes code
so fast that if every piece requires your review, your velocity is hard-capped by it."
The management reframe: influence quality through process, like an engineering director
who reviews no diffs — then spend human attention only at the two ends (planning up
front, judgment on the evidence and risk at the end). Several stages are independently
established in the KB (fresh-context review, self-report distrust, worktree isolation);
the contribution is their composition into one deterministic rail plus the two novel
stages: intent extraction from the producing session, and evidence artifacts as the
review substrate instead of the diff.

## Why People Are Using It

Chen ships 40-50 tested production changes daily through this pipeline, across parallel
agent sessions ("I never stare at this screen — I spin up other tasks and come back when
it says all checks passed"). The risk-gating claim is experience-calibrated: "I have
validated time and time again — for low-risk changes, any problem I could catch is very
likely already caught by the pipeline." Free and open source; also invocable as a skill
so any implementing agent can hand itself off to validation.

## Potential Alternatives

- Human review of every diff — reliable but hard-caps throughput
- CI-only gating — catches regressions but not intent mismatches or product-implication
  ambiguities
- Hosted PR-review products (e.g., AI code review bots) — cover the review stage but not
  intent extraction, evidence recording, or babysitting

## Potential Improvements

- Typed evidence requirements per change class (UI change → screenshot/video; perf
  change → benchmark log)
- Feeding escalated ambiguities back into memory files/skills so the same ambiguity
  doesn't recur (system-evolution loop)
- Calibration audit of the risk assessment itself: periodically deep-review a sample of
  "low-risk" PRs to verify the gate isn't drifting

## Potential Failure Modes

- Risk-assessment gaming/miscalibration: the pipeline scores its own change low-risk and
  the human never looks — the gate inherits self-report unreliability one level up
- Evidence theater: a screenshot proves one path works, not that others didn't break;
  evidence is necessary, not sufficient
- Intent extraction from a messy session can recover the wrong intent and validate
  against it convincingly
- Babysitting agents that auto-resolve PR conflicts can silently make post-review changes
  that were never reviewed
