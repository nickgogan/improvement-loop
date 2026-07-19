---
title: "Pin Model per Session — Delegate to a Subagent Instead of Switching"
type: "extracted-artifact"
assigned_form: "rule"
source_finding: "no-mid-session-model-switching-subagent-handoff"
extraction_date: "2026-07-19"
last_change_session: 152
last_change_report: "model-resilient-prompt-engineering.harvest-queue"
identification_report: null
deployed: false
deployed_to: null
context:
  applies_to:
    - "harness or agent-runtime designs that let a running session switch to a different model mid-way through"
    - "multi-model systems trying to save cost by downshifting to a cheaper model for an 'easy' stretch of a session"
    - "skill or agent design templates that need a standing rule for how model choice interacts with session boundaries"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "specify"
  reversibility: "trivial — a design-template or prompt-layer rule; removing it costs nothing but risks re-introducing the cache-invalidation failure mode"
  auditability: "high — a mid-session model change is a discrete, loggable event; a design review can check whether a skill or harness ever offers this operation"
  evidence_strength: "Strong"
  adoption:
    status: "Not Yet Started"
    notes: "First-party production practice at another team building a coding agent: keep the session on one model and hand off cheap subtasks to a subagent on a cheaper model via an explicit hand-off message, rather than downshifting the running session."
contract:
  preconditions: "A system runs multi-turn sessions against an inference API where the prompt prefix is cached per model. The system supports more than one model or model tier. A design decision is being made about whether a running session can change models partway through, versus delegating cheap subtasks to a separately-spawned subagent."
  invariants: "A running session stays on one model for its full duration. When a subtask is cheap enough to warrant a lower-tier model, the parent composes an explicit hand-off message describing the subtask and spawns a subagent on the cheaper model to execute it — the parent session itself never downshifts. Model choice is fixed at session-spawn time, not adjusted as a mid-session dial."
  governance: "Owner: whoever authors skill or agent design templates, or the harness's session-management layer. Any skill, agent, or harness feature that would let a running session change its model must be flagged in design review and replaced with a subagent hand-off pattern. Skill/agent design templates should encode this as a standing constraint on skill-to-model coupling."
  recovery: "If a mid-session model switch is found in an existing design → replace it with a subagent hand-off: compose a hand-off message carrying the subtask context and spawn a subagent on the target model. If a hand-off message is too thin and the subagent produces wrong work → enrich the hand-off message with the missing context; do not fall back to a direct mid-session switch. If sessions are short enough that accumulated context is small → re-evaluate whether hand-off overhead exceeds the cache-preservation benefit; a direct switch may be acceptable when little context has accumulated."
tags:
  - "extracted-artifact"
  - "rule"
  - "model-selection"
  - "prompt-caching"
  - "subagent-dispatch"
---

# Pin Model per Session — Delegate to a Subagent Instead of Switching

**Source:** [[no-mid-session-model-switching-subagent-handoff]]
**Form:** rule
**Extraction date:** 2026-07-19

## Condition

A running session is on one model, and a subtask arrives that could plausibly run more cheaply on a different (usually smaller) model. A design decision is being made about how to route that subtask to the cheaper model.

## Action

**Required:** Keep the running session on its original model for its full duration. When a subtask warrants a cheaper model, compose an explicit hand-off message describing the subtask and spawn a subagent on the cheaper model to execute it, rather than switching the parent session's model.

**Forbidden:** Switching a running session's model mid-way through (e.g., downshifting from a capable model to a cheaper one for an "easy" stretch). Offering a harness or skill feature that lets a session change models mid-run without going through a subagent hand-off.

## Boundary

Enforced at the design level of skills, agents, and harness session management — anywhere a decision is made about whether a session can change models. Also enforced at design-review time: any skill or agent spec that recommends changing model mid-run should be flagged.

## Enforcement

- **Mechanism:** Skill and agent design templates state the constraint explicitly ("model pinned per session; delegate to switch"). A design-time check flags any skill or harness feature that would let a session change its model without spawning a subagent.
- **Check (deterministic):** `(session_model_constant_across_turns == true) AND (cheap_subtasks_routed_via_subagent_handoff == true)`. Either branch false → violation.
- **Violation response:** Replace the mid-session switch with a subagent-handoff pattern: compose a hand-off message and spawn the subtask on the cheaper model as a separate subagent session.
- **Cannot be fully self-certified:** design review is needed to catch harness or skill features that quietly offer mid-session model switching as a convenience; a runtime check alone can confirm a given session stayed on one model, but not that no such feature exists in the design.

## Rationale

Prompt caches are model-specific: switching a running session's model re-processes the entire accumulated context at the new model's full input price. This is frequently more expensive than simply finishing the subtask on the original model, even though the new model's per-token rate is lower — "use a cheaper model for the easy part" is intuitive advice that backfires inside a single session. The real unit of model choice is the session, not the turn: cost savings come from topology (which agent runs on which model) rather than from dynamic mid-session switching. The subagent-hand-off pattern captures the intended savings — a fresh subagent session on the cheaper model builds its own cache from scratch over a much smaller context — without paying the cache-invalidation cost the parent session would incur.

## Failure Modes

- **Hand-off information loss.** The subagent only knows what the hand-off message carries; a thin hand-off produces wrong work regardless of the model's per-token price. Mitigation: ensure the hand-off message carries sufficient subtask context.
- **Over-delegation.** Spawning a subagent for a trivial subtask can add latency and orchestration overhead that exceeds the model-cost savings the hand-off was meant to capture. Mitigation: reserve hand-off for subtasks where the model-cost differential outweighs delegation overhead.
- **False economy on short sessions.** With little accumulated context, a direct mid-session switch may actually be cheaper than orchestrating a hand-off, since there is little cache value to lose. Mitigation: treat this rule as the default for sessions with meaningful accumulated context, not an absolute in every case.

## Contract

### Preconditions
A system runs multi-turn sessions against an inference API where the prompt prefix is cached per model. The system supports more than one model or model tier. A design decision is being made about whether a running session can change models partway through, versus delegating cheap subtasks to a separately-spawned subagent.

### Invariants
A running session stays on one model for its full duration. When a subtask is cheap enough to warrant a lower-tier model, the parent composes an explicit hand-off message describing the subtask and spawns a subagent on the cheaper model to execute it — the parent session itself never downshifts. Model choice is fixed at session-spawn time, not adjusted as a mid-session dial.

### Governance
Owner: whoever authors skill or agent design templates, or the harness's session-management layer. Any skill, agent, or harness feature that would let a running session change its model must be flagged in design review and replaced with a subagent hand-off pattern. Skill/agent design templates should encode this as a standing constraint on skill-to-model coupling.

### Recovery
If a mid-session model switch is found in an existing design → replace it with a subagent hand-off: compose a hand-off message carrying the subtask context and spawn a subagent on the target model. If a hand-off message is too thin and the subagent produces wrong work → enrich the hand-off message with the missing context; do not fall back to a direct mid-session switch. If sessions are short enough that accumulated context is small → re-evaluate whether hand-off overhead exceeds the cache-preservation benefit; a direct switch may be acceptable when little context has accumulated.
