---
name: "Harness Depth as Maintenance-Ownership Tradeoff"
summary: |-
  Plain English: when you build an agent setup, you are not just choosing a model — you
  are choosing how much harness maintenance you own versus outsource to the vendor. A
  light custom harness (instructions, memory, source folders, repeatable methods around
  Codex/Claude: here are the sources, here's the job, here's what you can't touch,
  here's the proof I need, here's when a human decides) rides the vendor's maintenance
  flywheel. A deep custom harness (data feeds, review screens, permission levels, logs,
  model choice, escalation paths, approval rules, a plan for model changes) can be
  worth it — but you now own evolving that system as models and the world change. The
  more custom the harness, the more upkeep you own, forever.
implementation_notes: null
category: "Agent Design"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Partially Adopted"
priority: "P3 (Monitor)"
applicability:
  - "IL (harness-layer scope decisions)"
  - "General"
adopted_in:
  - "Improvement Loop"
sources:
  - "dont-build-more-ai-agents-until-you-watch-this.md"
related_findings:
  - file: "platform-native-harness-over-agent-frameworks.md"
    rel: "same-problem"
  - file: "framework-abstraction-tax-for-agents.md"
    rel: "same-problem"
  - file: "bidirectional-agent-breakage-world-drift-model-improvement.md"
    rel: "enabled-by"
proposals: null
date_discovered: "2026-07-13"
last_updated: "2026-07-13"
pipeline_status: "raw"
consumed_by: []
---

# Harness Depth as Maintenance-Ownership Tradeoff

## What It Is

A framing for the build-vs-ride decision on agent infrastructure. Because agents break
bidirectionally (world drift + model improvement), every piece of harness you author is
a maintenance liability with no end date. That makes harness depth a spectrum of
ownership:

- **Light custom harness:** a clean set of instructions, memory, source folders, and
  repeatable methods around a vendor harness (Codex, Claude Code). Its contract fits in
  five clauses: here are the sources; here's the job; here's what you can't touch;
  here's the proof I need; here's when a human decides. The vendor's harness flywheel
  (terminal, browser, computer use, plugins, memory, approvals, sandboxing, logs — all
  continuously maintained by the two teams Jones says are doing this well, Anthropic
  and OpenAI) carries the rest.
- **Deep custom harness:** data feeds, review screens, permission levels, logs, model
  choice, escalation paths, approval rules, and a plan for what happens when the model
  changes. Sometimes worth it — but "now you're not just building an agent; you are
  taking responsibility for evolving the system around the agent over time."

Everyone has a harness whether they name it or not (a writer's drafts + transcripts +
editorial rules + cite-your-source instruction; an engineer's repo + tests + terminal +
permissions + worktrees + review rules). The operative questions: what is my harness,
do I know when and how to rebuild it, and what part will I need to delete later?

## Why It Matters

The engine is an explicitly harness-heavy system (governance, skills, hooks, session
ops authored in-house on top of Claude Code). This finding names the recurring cost
that design accepts, and gives the counter-pressure vocabulary for scope decisions:
each new engine-owned surface is upkeep owned forever, so it must beat the alternative
of riding the vendor surface — the same logic as the engine's abstractions-earn-their-
keep rule, applied at the harness layer.

## Why People Are Using It

Jones's synthesis across the Vercel case, his own personal-harness evolution (folder
rules, memory scope, read-vs-search decisions changing as models improve), and the
frontier labs' visible strategy of maintaining the harness as the product.

## Potential Improvements

- A depth audit: classify each engine-owned harness element as ride-vendor,
  light-custom, or deep-custom, with the maintenance trigger each one carries.
- Exit criteria authored at build time: what vendor capability would let us delete this
  element?

## Potential Failure Modes

- Depth creep: light harnesses accrete deep-harness responsibilities one exception at a
  time, without the ownership decision ever being made explicitly.
- Vendor-riding has its own failure mode — behavioral lock-in and breaking changes on
  the vendor's schedule, not yours.
- Underestimating the "plan for model changes" clause: deep harnesses without a model-
  upgrade playbook inherit the full bidirectional-breakage problem.
