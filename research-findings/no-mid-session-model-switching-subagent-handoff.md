---
name: "Never Switch Models Mid-Session — Hand Off to a Subagent Instead"
summary: |-
  Prompt caches are model-specific, so switching models mid-session (e.g., Opus to Haiku for an
  "easy" stretch) invalidates the entire cache and can cost more than staying on the expensive
  model. The Claude Code team's rule: keep the session on one model and delegate cheap subtasks
  to a subagent on the cheaper model via an explicit hand-off message. For us this is a hard
  constraint on skill-to-model coupling — model choice is a session-boundary decision, not a
  mid-session dial.
implementation_notes: |-
  Feeds directly into our skill/model coupling guidance and /design-agent variant B (harness-
  based agents): (1) a skill or agent definition should pin its model at spawn time and never
  recommend switching within a running session; (2) where a workflow has a cheap phase, the
  design should spawn a subagent on the cheaper model with a prepared hand-off message rather
  than downshifting the parent; (3) our model-capability registry guidance should note that
  per-session model pinning is also a cost rule, not just a capability rule.
category: "Model Selection"
evidence_strength: "Strong (production-tested, first-party)"
adoption_status: "Not Yet Started"
priority: "P2 (Design Required)"
applicability:
  - "Improvement Loop"
  - "General"
adopted_in: []
sources:
  - "claude-code-prompt-caching-is-everything.md"
related_findings: []
proposals: null
date_discovered: "2026-07-11"
last_updated: "2026-07-11"
---

## What It Is

A Claude Code team rule: prompt caches do not transfer between models. Switching a running session from Opus to Haiku re-processes the entire accumulated context at the new model's full input price — frequently more expensive than simply finishing the subtask on Opus, despite Haiku's lower rates. The sanctioned pattern is subagent hand-off: the parent model composes a hand-off message describing the subtask, and a fresh subagent session on the cheaper model executes it, building its own cache from scratch over a much smaller context.

## Why It Matters

"Use a cheaper model for the easy parts" is intuitive cost advice that backfires inside a single session. The real unit of model choice is the session, not the turn. This reframes multi-model architecture: cost savings come from topology (which agent runs on which model) rather than from dynamic switching. It also means any harness UI or skill that offers mid-session model changes is silently offering a cache-destroying operation.

## Why People Are Using It

First-party production practice in Claude Code; the subagent hand-off pattern is how the product routes appropriate subtasks to smaller models without breaking the parent's cache.

## Potential Alternatives

| Alternative | Description | When to Prefer |
|-------------|-------------|----------------|
| Accept the cache break | Switch models anyway | Session context is small enough that re-processing is cheap |
| Single-model everything | Never use a second model | Workloads with no clearly separable cheap subtasks |
| Pre-planned model routing | Route whole tasks to models before any session starts | Batch pipelines where task difficulty is known upfront |

## Potential Improvements

- Encode "model pinned per session; delegate to switch" as an explicit rule in agent/skill design templates
- Add a design-time check: any skill that suggests changing model mid-run gets flagged

## Potential Failure Modes

- **Hand-off information loss:** the subagent only knows what the hand-off message carries; a thin hand-off produces wrong work at any price
- **Over-delegation:** spawning subagents for trivial subtasks adds latency and orchestration overhead exceeding the model-cost savings
- **False economy on short sessions:** with little accumulated context, a direct switch may actually be cheaper than orchestrating a hand-off
