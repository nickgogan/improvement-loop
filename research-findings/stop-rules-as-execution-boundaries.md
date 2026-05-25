---
name: Stop Rules as Execution Boundaries
summary: Explicit stop rules -- conditions for halting, escalating, or declaring completion -- are the most commonly omitted component of agent intent specifications. Without stop rules, agents either loop
  indefinitely, declare premature completion, or silently degrade. Stop rules are execution boundaries, not suggestions. They should be defined before deployment, not discovered during failure.
implementation_notes: 'Audit MetaSystem agent specs (skills, handoff prompts) for explicit stop rules. Current skills have implicit stop conditions but few have explicit halt/escalate triggers. Add to each
  skill: ''Stop if: ambiguity exceeds threshold, policy conflict detected, file count exceeds N, or token budget reaches 80%.'''
category: Intent Engineering
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- General
adopted_in: []
sources:
- intent-engineering-framework-for-ai-agents-product.md
related_findings:
- file: autonomy-gradient-not-binary-delegation.md
  rel: same-problem
- file: health-metrics-vs-hard-constraints-distinction.md
  rel: same-problem
- file: acceptance-criteria-as-verifiable-eval-anchor.md
  rel: same-problem
- file: intent-engineering-framework-seven-part-agent-inten.md
  rel: extended-by
- file: ralph-wiggum-execution-pattern.md
  rel: enables
proposals: []
date_discovered: '2026-04-07'
last_updated: '2026-04-08'
pipeline_status: synthesized
consumed_by:
  - "writing-agent-specifications.md"
---
## What It Is

The seventh component of Huryn's Intent Engineering Framework, and by his assessment the most frequently omitted. Stop rules define three types of execution boundaries:

1. **Halt conditions**: When the agent should stop working entirely (e.g., "stop if the error rate exceeds 5%", "stop if you've made more than 3 unsuccessful attempts at the same approach")
2. **Escalation triggers**: When the agent should hand off to a human (e.g., "escalate if the customer mentions legal action", "escalate if the proposed change touches more than 5 files")
3. **Completion criteria**: How the agent knows it's genuinely done (e.g., "complete when all tests pass and the diff is under 200 lines")

The key principle: "The reasoning layer proposes. The orchestration layer enforces." Stop rules in the prompt guide the agent's judgment; stop rules in the orchestration layer (timeouts, token budgets, iteration caps) guarantee enforcement.

## Why It Matters

Without stop rules, agents exhibit three failure modes:
- **Infinite loops**: Continuing to retry a failing approach because nothing tells them to stop
- **Premature completion**: Declaring "done" based on partial success because completion criteria were never specified
- **Silent degradation**: Output quality declining over a long session because the agent doesn't recognize it's past the point of useful work

The "Ralph loop" pattern (checking if the agent is really done) is a workaround for missing completion criteria. Proper stop rules make the workaround unnecessary.

## Why People Are Using It

Huryn's framework, Anthropic's long-running Claude research (which recommends explicit "stop the line" rules), and the GSD plugin (which uses phase-level completion verification) all converge on stop rules as essential. The industrial automation community (ICLR Agentic AI for Intent-Based Industrial Automation) implements stop rules as formal "conditions" in the intent decomposition pipeline.

## Potential Improvements

Dynamic stop rules that adapt based on task context: a simple formatting task might have tight iteration caps (stop after 2 attempts) while a complex debugging task might have generous ones (stop after 10 attempts). Token budget awareness: stop rules that fire when the remaining context window drops below a threshold.

## Potential Failure Modes

Overly aggressive stop rules cause the agent to bail out of solvable tasks. Overly permissive stop rules provide no practical benefit. Stop rules that depend on the agent's self-assessment of quality are unreliable -- external validation (tests, linters, human review) is more trustworthy.
