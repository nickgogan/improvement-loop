---
name: "Review-Triggered Remediation Sub-Agent Dispatch"
summary: "A code review skill identifies issues, classifies them by severity (critical/important), and automatically dispatches a fix sub-agent per issue — chaining review and remediation as a single composite step rather than requiring human routing between them. The fix agent gets fresh context with only the issue description and relevant code."
implementation_notes: null
category: "Orchestration"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: P2
applicability:
  - "S3 (Claude Code Build)"
sources:
  - "claude-code-plus-superpowers-tutorial.md"
related_findings:
  - file: "two-stage-sequential-review.md"
    rel: "extends"
  - file: "builder-validator-chain-pattern.md"
    rel: "extends"
  - file: "superpowers-plugin-spec-driven-sub-agent-orchestra.md"
    rel: "extends"
  - file: "gstack-review-army-parallel-specialist-dispatch.md"
    rel: "same-problem"
adopted_in: []
proposals: null
date_discovered: "2026-05-25"
last_updated: "2026-05-25"
pipeline_status: "synthesized"
consumed_by:
  - "agent-architecture-decisions.md"
  - "skills/review-triggered-remediation-chain.md"
tags:
  - "session-95-reextract"
---

# Review-Triggered Remediation Sub-Agent Dispatch

## What It Is

A composition pattern where a code review phase does not merely produce a report — it automatically chains into remediation by dispatching a fix sub-agent for each issue found. The chain is: review -> classify severity -> dispatch fix agent per issue -> verify fix.

In the observed Superpowers workflow (Eric Tech tutorial, BookZero.ai):
1. After all 11 implementation tasks complete, the code-review skill runs a full implementation review
2. The reviewer identifies specific issues with severity classifications (critical, important)
3. For each issue, the reviewer dispatches a fresh fix sub-agent with the issue description and relevant code context
4. The fix agent addresses the issue in isolation (fresh context window)
5. The orchestrator receives fix completion and moves to the next issue

This is structurally different from review patterns that produce a report for human triage (two-stage-sequential-review, gstack review army). Here, the review is not a terminal step — it is a trigger for automated remediation. The human gate shifts from "review issues and decide what to fix" to "review fixes after they are applied."

The composition primitive is: **review as trigger, not terminus.** The review output (issue list with severity) becomes the dispatch queue for fix agents.

## Why It Matters

In traditional review patterns, the human is the router between review findings and remediation. The reviewer identifies problems; the human decides which to fix, assigns them, and tracks completion. This works but creates a bottleneck: review output sits idle until the human processes it.

Review-triggered remediation removes the human routing step for severity-classified issues. The review skill makes the triage decision (critical issues get fixed immediately; important issues get fixed; informational issues may be deferred). The fix dispatch is automatic.

For MetaSystem: this pattern maps directly to how `/code-review` could evolve into `/code-review-fix`. The existing `/gsd-code-review-fix` skill already implements a version of this pattern. The finding validates the pattern with additional practitioner evidence from Superpowers.

The composition insight is that **any evaluation step that produces a structured issue list can chain into a dispatch queue**. This generalizes beyond code review to: spec compliance review -> fix non-compliant sections, security review -> fix vulnerabilities, test failure analysis -> fix failing tests.

## Why People Are Using It

Demonstrated in Superpowers' code review skill (Eric Tech tutorial). After the full implementation review found "stale credits" and "misleading metadata" issues, the reviewer dispatched fix agents for both without returning control to the user for triage.

Also present in GSD's `/gsd-code-review-fix` skill, which reads a REVIEW.md, spawns fixer agents per finding, commits each fix atomically, and produces REVIEW-FIX.md. The pattern is converging across frameworks.

## Potential Improvements

- Severity threshold for auto-dispatch: auto-fix critical/important issues but surface informational ones for human decision, rather than fixing everything or nothing
- Fix verification loop: after the fix agent completes, re-run the specific review check to confirm the issue is resolved before moving to the next issue
- Accumulated fix reporting: produce a single "here's what was auto-fixed and what was deferred" summary for human review after the batch completes
- Parallel fix dispatch for independent issues rather than sequential

## Potential Failure Modes

- **Fix agents introduce new bugs.** The fix agent operates on a narrow context (the issue + relevant code). It may fix the reported issue but break something adjacent that was not in its context. Mitigation: run full test suite after all fixes complete.
- **Severity misclassification.** If the review skill classifies an issue as critical when it is cosmetic, a fix agent wastes tokens and may make unnecessary changes. Mitigation: human review of the severity classifications before dispatch, or at least of the completed fixes.
- **Cascading fix conflicts.** Fix agent A changes file X to fix issue 1. Fix agent B changes file X to fix issue 2. If dispatched in parallel, their changes conflict. Mitigation: sequential dispatch or file-level locking.
- **Automated fix bypasses design intent.** The fix agent knows what the code should look like to satisfy the review finding, but it does not know the design rationale. It may fix the symptom with a solution that violates architectural constraints. Mitigation: fix agents should receive spec context, not just code context.
