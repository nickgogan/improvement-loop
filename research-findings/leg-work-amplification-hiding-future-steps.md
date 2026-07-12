---
name: Leg-Work Amplification by Hiding Future Steps
summary: 'Plain English: when an agent skimps on a step (shallow clarifying questions, cursory

  exploration), the cause is usually that it can see the next step — it optimizes for the

  visible end goal and rushes. The fix is structural: split the phase into its own skill so

  the agent sees only one step at a time. Matt Pocock''s diagnosis of plan mode: "ask

  clarifying questions" underperforms in every implementation he''s tried because the agent

  sees "create a plan" coming and eagerly jumps ahead. His grill-with-docs → to-spec split

  fixes it; v1.1 extends the same one-step-at-a-time shape into a full SDLC pipeline

  (grill → spec → tickets → implement → review), plus an explicit confirmation gate ("do

  not enact the plan until I confirm shared understanding") to stop eager phase-crossing.'
implementation_notes: 'Rubric-relevant for /design-skill (construction: when to split a skill): the decision

  rule is not size but effort starvation — split when a step needs more leg work than the

  agent gives it while the future goal is visible. Complementary lever: explicit

  human-confirmation gates at phase boundaries where models leak into the next phase.

  Nick-gated restructure Phase 2 decides substrate entry.'
category: Agent Design
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- IL (assess-skill/design-skill substrate)
- General
adopted_in: []
sources:
- pocock-skills-v1-1-wayfinder-research-implement.md
- building-great-agent-skills-the-missing-manual.md
related_findings:
- file: skill-phase-pipeline-shared-session-orchestrator.md
  rel: same-problem
- file: reference-only-skill-shape-for-afk-agents.md
  rel: same-problem
- file: wayfinder-issue-tracker-decision-map.md
  rel: extended-by
proposals: null
date_discovered: '2026-07-12'
last_updated: '2026-07-12'
pipeline_status: raw
---

# Leg-Work Amplification by Hiding Future Steps

## What It Is

A structural steering technique: when an agent under-invests in a step ("doesn't do enough
leg work"), split that step into its own skill so the agent cannot see the downstream goal.
The canonical failure is plan mode: two steps — ask clarifying questions, then create a
plan. In "every single implementation of plan mode" Pocock has tried, the questioning phase
is shallow because the agent sees that its ultimate goal is the plan and eagerly produces
it. His solution: `grill-with-docs` is a standalone skill whose only visible job is the
interrogation; only after it completes does the separate `to-spec` (formerly to-PRD) skill
run. "We have step one and step two, but the agent only sees one step at a time."

v1.1 (07-08) generalizes this into a full pipeline of single-purpose skills — grill →
to-spec → to-tickets → implement → code-review — each session-scoped, each blind to the
later phases. It also adds a complementary gate for phase-leak at the human boundary: "Do
not enact the plan until I confirm we've reached a shared understanding," added because
grilling sessions on multiple models were sliding straight into implementation.

## Why It Matters

It names a mechanism behind a widely felt failure (eager planning, shallow exploration) and
gives a structural rather than exhortative fix — "there's no technique like it." For the
engine it supplies a construction-time decision rule for `/design-skill`: skill-splitting
is not only about size or branches; it is an *effort dial*. Where a phase chronically
starves (clarifying questions, codebase exploration, verification), hiding the future
phase buys leg work that no amount of "be thorough" prose does. It also supports the
engine's existing gate discipline: confirmation gates at phase boundaries are the
backstop where structural hiding isn't possible.

## Why People Are Using It

Pocock built his flagship planning flow around it and, in v1.1, extended the same shape
into the whole SDLC after users kept asking "what's the flow?" The bug-fix half
(confirmation gate) is corroborated by user reports across multiple models.

## Potential Alternatives

Prompt-level emphasis ("ask at least N questions") — treats the symptom, brittle.
Orchestrator-enforced phase machines (heavier; the skill split achieves phase isolation
with no machinery). Subagent-per-phase with context isolation — same principle at higher
cost, appropriate when phases also need clean context.

## Potential Improvements

A diagnostic: measure per-step effort (questions asked, files read) with and without the
downstream step visible, to know when a split pays. Conventions for pipeline handoff
artifacts (Pocock uses docs/spec/tickets as the inter-skill state carriers).

## Potential Failure Modes

- **Over-splitting**: every step as its own skill produces pipeline friction and user
  cognitive load; Pocock is explicit that splitting is for steps that need *extra* leg
  work, not a default.
- **Lost coherence**: the later phase can't see the earlier phase's reasoning unless the
  handoff artifact captures it — the split is only as good as the intermediate document.
- **Gate fatigue**: confirmation gates at every boundary train the user to rubber-stamp.
