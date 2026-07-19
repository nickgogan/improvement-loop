---
name: Pre-Code Validation Contracts with Dual Blind Adversarial Validators
summary: |-
  Factory's Missions: a validation contract, written by the orchestrator during planning
  before any code exists, defines correctness independently of any implementation — for a
  complex project, hundreds of individual assertions, with every feature assigned one or
  more assertions such that the sum of all features' assertions covers the contract.
  Targets a named failure mode directly: "tests written after implementation don't catch
  bugs, they confirm decisions." After each milestone, two validators run against the
  contract — a scrutiny validator (tests, type-checking, lint, plus dedicated code-review
  sub-agents per feature) and a user-testing validator that spawns the live application
  and drives it via computer-use-style interaction, checking functional flows end-to-end.
  Critical constraint: neither validator has seen the implementation — validation is
  adversarial by design. Reported outcome: validation "never succeeds on the first go" in
  the walked production example, with follow-up features created as standard course.
implementation_notes: |-
  The engine's /assess-* skills already satisfy the "assessor never authors" half of this
  pattern (rule 10); the gap this finding surfaces is the other half — IL's extraction/
  synthesis pipeline doesn't currently write an assertion-shaped "what must this artifact
  satisfy" contract before /extract-artifacts drafts it. Worth a design pass on whether
  /identify-artifacts' classification output could carry a lightweight validation-contract
  field for /extract-artifacts to draft against.
category: Evaluation
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- Improvement Loop
- General
adopted_in: []
sources:
- multi-agent-architecture-that-actually-ships.md
related_findings:
- file: builder-validator-chain-pattern.md
  rel: extends
- file: generator-assessor-separation-in-skill-iteration.md
  rel: same-problem
- file: multi-perspective-review-council.md
  rel: same-problem
- file: qa-plan-as-agent-trust-gate.md
  rel: same-problem
- file: missions-three-role-architecture-serial-targeted-parallelization.md
  rel: enabled-by
- file: droid-whispering-per-role-model-assignment.md
  rel: same-problem
- file: review-outcome-not-diff-for-agent-changes.md
  rel: same-problem
proposals: null
date_discovered: '2026-07-18'
last_updated: '2026-07-18'
pipeline_status: "synthesized"
consumed_by:
  - "agent-architecture-decisions.md"
  - verifying-agent-output.md
---

## What It Is

A verification design with two coupled parts. First, a **validation contract**: written
by the orchestrator during planning, before any code exists, defining correctness
independently of any implementation — for a complex project, hundreds of individual
assertions, with every feature assigned one or more assertions such that the sum of all
features' assertions covers the full contract. This directly targets a named failure
mode: "tests written after implementation don't catch bugs, they confirm decisions" —
because post-hoc tests are shaped by what the code happens to do, not by what it was
supposed to do. Second, **dual blind validators** that run after each milestone: a
*scrutiny validator* (test suite, type-checking, lint, plus dedicated code-review
sub-agents spawned per completed feature) and a *user-testing validator* that behaves
like a QA engineer — spawns the actual running application, drives it via
computer-use-style interaction (fills forms, clicks buttons, checks rendering), and
validates functional flows end-to-end rather than just checking that code looks right.
The critical design constraint: **neither validator has seen the implementation** —
validation is adversarial by design, not by policy. Reported outcome: validation "never
succeeds on the first go" in the walked example (a Slack-clone build) — follow-up
features get created as a matter of course, offered as evidence the QA loop is doing real
work rather than rubber-stamping.

## Why It Matters

This is the sharpest concrete instance in this batch of the KB's generator-assessor-
separation principle (rule 10; corroborated independently by Anthropic's skill-creator
and by Nate Jones's build/attack loop per that finding's corroboration log) — a further
independent origin, from a different production system, for the same architectural
answer to "how do you keep a generator from grading its own homework." It also names and
fixes a specific failure mode reviewer-skill-elevation-for-agentic-output.md gestures at
but doesn't operationalize (tests that look like coverage but don't test intent) with a
concrete mechanism: write the assertions *before* the code, so there's no code yet to
shape them. The user-testing validator additionally extends the KB's
builder-validator-chain-pattern.md (single validator, code-focused) with a *behavioral*
validator most existing KB verification findings don't cover — checking that the running
system does the right thing, not just that the code passes static checks.

## Why People Are Using It

Production account: this is described as the primary reason Missions can run for many
days without drifting — most of a mission's wall-clock time is reported spent in the
user-testing validator "waiting for real-world execution to occur instead of generating
tokens," offered as evidence the behavioral check is doing substantive, not cosmetic,
work.

## Potential Alternatives

- **Single validator covering all dimensions** (builder-validator-chain-pattern.md's base
  case): cheaper, but conflates "does the code look right" with "does the running system
  behave right" — this finding's evidence suggests those are genuinely different failure
  surfaces.
- **Post-hoc test-writing with a strong coverage bar** (the conventional practice this
  finding explicitly argues against): the KB has no prior finding directly naming why
  coverage percentage alone is an unreliable done-signal; this is a citable rebuttal.
- **Ryan Lopopolo's QA-plan-as-trust-gate** (qa-plan-as-agent-trust-gate.md): a lighter-
  weight, usage/journey-shaped alternative to a formal assertion contract, gating trust at
  PR-review time rather than defining coverage at planning time. The two are convergent
  evidence for "define done before you build," from different vendors, via different
  mechanisms — see MANIFEST cross-link note rather than treating them as one pattern.

## Potential Improvements

- A worked template for what "hundreds of assertions" actually look like structurally
  (granularity, how they map to features, how coverage-completeness is checked
  mechanically) — the talk asserts the practice but doesn't show the artifact.
- Guidance on validator model selection to preserve the "no shared blind spot"
  property — see droid-whispering-per-role-model-assignment.md, which names using a
  different model provider specifically for validation.

## Potential Failure Modes

- **Garbage-in contracts:** assertion contracts are only as good as the planning
  conversation that produced them — an under-specified or wrong contract still gets
  faithfully validated against, just faithfully validated against the wrong thing.
- **Latency cost:** the user-testing validator's computer-use-style execution is reported
  as the dominant wall-clock cost — this buys behavioral confidence at a real latency
  price that may not be affordable for faster-iteration contexts.
- **Silent isolation leaks:** "neither validator has seen the implementation" depends on
  strict context isolation being maintained in practice; a leak (e.g., a validator's tool
  access incidentally surfacing implementation details) would silently erode the
  adversarial-by-design property with no visible signal that it happened.
