---
name: "Tool Pruning as Harness Maintenance Discipline"
summary: |-
  Plain English: agents don't monotonically improve as you give them more tools —
  Vercel made its sales agent better by deleting 80% of its tools. The beginner
  instinct is to add (a tool, a memory file, a Slack integration, another exception)
  until the agent looks powerful but can't be trusted; the maintenance instinct asks
  what should be removed. Pruning is a recurring maintenance action on the whole
  harness surface — tools, and equally piles of accumulated skills — with simplicity
  treated as a key to maintainability (Stewart Brand). The mature design question is
  "what part of this harness will I need to delete later?"
implementation_notes: |-
  P2: directly applicable to the engine's own surfaces — the skill roster and any
  future tool allowlists. Nothing in the engine currently schedules subtractive review
  (audits check consistency and drift, not whether an artifact should be deleted).
  Candidate input for /system-health or the restructure program's Phase 2 audit; the
  triage gate ruled no new mechanism from one source (natural ENHANCE delta if the
  pattern recurs).
category: "Tool Integration"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: "P2 (Design Required)"
applicability:
  - "IL (skill roster, tool surface reviews)"
  - "General"
adopted_in: []
sources:
  - "dont-build-more-ai-agents-until-you-watch-this.md"
related_findings:
  - file: "bidirectional-agent-breakage-world-drift-model-improvement.md"
    rel: "same-problem"
  - file: "skill-pruning-failure-modes-noop-deletion-test.md"
    rel: "same-problem"
  - file: "claudemd-context-rot-from-indiscriminate-rule-accu.md"
    rel: "same-problem"
  - file: "build-from-observed-workflow.md"
    rel: "enabled-by"
  - file: "add-then-retire-lifecycle-at-framework-scale.md"
    rel: "same-problem"
proposals: null
date_discovered: "2026-07-13"
last_updated: "2026-07-13"
pipeline_status: "raw"
consumed_by: []
---

# Tool Pruning as Harness Maintenance Discipline

## What It Is

The Vercel case: an SDR agent built from a top rep's observed workflow (filter inbound,
qualify leads, research companies, draft replies, route support away from sales, human
review) did not get better as the team piled on tools — it got better when they **took
tools away**, deleting 80% of them. Jones's generalization: the usual story ("agents
get better as you give them more stuff — more context, memory, tools, integrations,
access, autonomy") is backwards after the build phase. And it is explicitly not just a
context-window argument — the usual reason people dump tools — but a trust and
correctness one: each addition makes the agent look more muscled-up and harder to
trust.

The discipline: "the beginner instinct is to add; the maintenance instinct is to ask
what should be removed." He extends it beyond tools to skill piles ("if you've got a
pile of skills in your Codex or Claude, pay attention") and anchors it in Brand's
simplicity-as-maintainability principle. The mature design question is asked at build
time: what part of this harness will need deleting later?

## Why It Matters

Additive growth is the default failure path for every agentic surface the engine owns —
skills, rules, context files, tool grants. The KB already holds the failure-mode side
(context rot from rule accumulation; no-op deletion tests for skill pruning); this
finding supplies the positive maintenance framing with a measured production anchor: a
real system where subtraction, not addition, produced the improvement.

## Why People Are Using It

Vercel's production sales agent is the documented case (relayed secondhand by Jones —
verify against Vercel primaries before citing as Strong). The pattern matches
first-party Anthropic guidance already in the KB (harness simplification as models
improve).

## Potential Improvements

- Pruning trials as standard practice: remove a tool, run the eval set, keep the
  deletion if quality holds (the no-op deletion test generalized to tools).
- Track per-tool invocation rates so pruning candidates are data-selected rather than
  intuited.

## Potential Failure Modes

- Pruning without evals — deleting tools the agent rarely but critically needs
  (long-tail capability loss invisible until the rare case).
- Treating pruning as one-time cleanup rather than recurring discipline; the surface
  regrows.
- Cargo-culting the 80% number — the right amount of deletion is workload-specific;
  the discipline is the review, not the ratio.
