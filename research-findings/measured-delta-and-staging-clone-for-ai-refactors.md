---
name: "Measured Delta + Staging Clone Verification for AI Refactors"
summary: |-
  Plain English: don't trust an AI's claim that its refactor is safe or beneficial —
  measure the improvement, and rehearse risky changes in a disposable clone of production.
  Three composed mechanisms from the Ponytail workflow: (1) measure the delta — a `gain`
  command runs with/without comparisons to prove the skill's claimed impact on your repo,
  not the vendor's benchmark; (2) staging clone — for repo-wide refactors, create a
  duplicate environment (separate database, separate deployment target), merge and
  manually test there, keep rollback available, and only then promote to production
  ("I usually don't trust what AI gave us" — even when the audit says behavior is
  identical); (3) hand implementation to spec- plus test-driven development — the audit
  output becomes a spec.md, and tests locking current behavior are written and passing
  BEFORE the refactoring starts, so "no behavior change" is checked mechanically, not
  asserted.
implementation_notes: null
category: "Evaluation"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: "P3"
applicability:
  - "General"
adopted_in: []
sources:
  - "claude-code-cuts-token-usage-by-94-percent.md"
related_findings:
  - file: "seven-rung-minimal-code-decision-ladder.md"
    rel: "same-problem"
  - file: "test-driven-development-as-counterweight-to-agenti.md"
    rel: "extends"
  - file: "dual-verification-trajectory-vs-output-correctness.md"
    rel: "same-problem"
  - file: "agent-self-reporting-unreliability-independent-eval.md"
    rel: "same-problem"
proposals: null
date_discovered: "2026-07-12"
last_updated: "2026-07-12"
pipeline_status: "raw"
---

# Measured Delta + Staging Clone Verification for AI Refactors

## What It Is

A verification bundle for the riskiest thing coding agents are now asked to do —
repo-wide simplification/refactoring — treating the agent's own safety assessment as
untrusted input:

1. **Measured delta.** Prove impact empirically on your own repo (with-skill vs baseline
   runs) before believing any claimed percentage. The audited repo in the source: 200k
   lines across 1,000 files, scanned by parallel subagents for dead code, unused
   flags/configs, over-abstract services, hand-rolled standard-library clones, and
   single-implementation interfaces.
2. **Staging clone.** A duplicated environment with its own database and deployment
   target; the refactor merges there, gets manually tested, and carries a rollback path.
   The agent's own risk table (which features/pages are affected, whether UX changes) is
   used to focus testing, not to skip it.
3. **Spec + test-first handoff.** The audit tool only identifies; implementation moves to
   a spec-driven workflow where type checks and the existing test suite must pass before
   changes land, and current expected behavior is encoded as automated tests before any
   refactoring — turning "behaviors are identical" from an agent assertion into a
   checkable property.

## Why It Matters

AI refactors fail in a specific way: confident, plausible, mostly-correct bulk changes
whose regressions surface far from the change site. The bundle addresses each gap —
claimed benefit (measure it), claimed safety (rehearse it), claimed behavior preservation
(test-lock it). It is the operational counterpart to the KB's
agent-self-reporting-unreliability line: the practitioner explicitly discounts the model's
own summary table even while using its audit.

## Why People Are Using It

Demonstrated on a production SaaS repo where a botched refactor has customer impact; the
staging-clone habit generalizes from ordinary deployment hygiene into an AI-specific trust
boundary.

## Potential Improvements

Automate the delta measurement as a standing A/B harness (the with/without-skill baseline
pattern appears independently in the loop-engineering cluster). Diffable behavior
snapshots for repos without good test coverage — the weakest link is rung 3 when no tests
exist to lock.

## Potential Failure Modes

Staging clones drift from production (data shape, scale, config) and pass tests that
production fails. Manual staging verification doesn't scale with refactor frequency —
becomes a rubber stamp. Test-locking current behavior also locks current bugs; refactor
plus behavior change must be strictly sequenced, never mixed.
