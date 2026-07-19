---
title: "Side-Effect Skills Require Explicit Invocation"
type: "extracted-artifact"
assigned_form: "rule"
source_finding: "skill-invocation-control-side-effect-guard"
extraction_date: "2026-07-19"
last_change_session: 152
last_change_report: "agent-governance-and-trust.harvest-queue"
identification_report: "agent-governance-and-trust.harvest-queue"
deployed: false
deployed_to: null
context:
  applies_to:
    - "agent frameworks or harnesses where skills, tools, or capabilities can be triggered either by explicit user command or by the model's own judgment on a description match"
    - "skill authors deciding whether a given capability should be auto-invocable by the model or user-invocation-only"
    - "reviewers auditing a skill catalog for capabilities that can act on the world (commit, deploy, send a message, spend money) without a human having explicitly asked for that specific action"
  platform_coupling: "specific:claude-code"
  autonomy: "hitl-only"
  stage: "specify"
  reversibility: "trivial — a frontmatter flag; flipping it is a one-line edit with no migration cost"
  auditability: "high — the flag is a lintable, per-skill boolean; a catalog scan can enumerate every skill whose procedure performs a side effect and check whether the flag is set"
  evidence_strength: "Strong"
  adoption:
    status: "Not Yet Started"
    notes: "Documented in canonical platform documentation and demonstrated in at least one shipped third-party skill catalog (an intentionally harsh review mode gated the same way); not yet applied as a systematic authoring rule in the adopting workspace's own skill catalog at time of extraction."
contract:
  preconditions: "The platform or harness supports at least two invocation modes for a capability: model-triggered (auto-invoked on a description or context match) and user-triggered (explicitly named by the human). The skill or capability being authored has a procedure that performs a side effect — it changes state outside the conversation (commits code, deploys, sends a message, spends a resource) or adopts a posture/intensity the user should consciously opt into."
  invariants: "Every skill whose procedure performs a side effect, or whose posture is deliberately aggressive/high-cost, is marked non-model-invocable — the model cannot trigger it on a description match alone; only an explicit user invocation runs it. Skills with no side effects and no deliberately opt-in posture may default to model-invocable. The invocation-mode decision is made and recorded at authoring time, not left to the default."
  governance: "Owner: the skill's author, at the point of authoring or review. A skill-assessment or catalog-audit process checks every skill's procedure for side effects and flags any side-effect skill missing the explicit-invocation-only marker as under-specified. The flag is overridable by harness-level settings in some platforms — if so, the override surface itself is part of what an audit should check, since it can silently change an author's intended trust boundary."
  recovery: "If a side-effect skill is found without the explicit-invocation-only marker, treat it as a governance gap: add the marker before the skill is exposed to model-triggered invocation, or explicitly document why the side effect is acceptable to auto-trigger (rare — most side effects are not). If a user reports a side effect happening without them having explicitly requested it, audit which skill fired and whether it was missing the marker; this is the concrete failure signature the rule exists to prevent."
tags:
  - "extracted-artifact"
  - "rule"
  - "skill-authoring"
  - "governance"
  - "invocation-control"
---

# Side-Effect Skills Require Explicit Invocation

**Source:** [[skill-invocation-control-side-effect-guard]]
**Form:** rule
**Extraction date:** 2026-07-19

## Condition

A skill, tool, or capability is being authored or reviewed in a system that supports both model-triggered and user-triggered invocation. The skill's procedure performs a side effect — it changes state outside the conversation (committing code, deploying, sending an outbound message, spending a resource) — or it deliberately adopts an aggressive, high-cost, or otherwise opt-in posture even without a literal side effect (e.g., an unusually harsh review mode).

## Action

**Required:** Mark any side-effect (or deliberately opt-in-posture) skill as explicit-invocation-only — the model must not be able to trigger it on a description match alone; only a direct user invocation runs it.

**Forbidden:** Shipping a side-effect skill with default (both-can-invoke) settings. Relying on the skill's own internal wording ("are you sure?") as a substitute for the invocation-mode control — a model that already decided to invoke the skill can also decide to answer its own confirmation prompt.

## Boundary

Enforced at skill-authoring time (the frontmatter/config declaration) and re-checked at catalog-audit time. The check is static — it inspects the skill's declared procedure and its invocation-mode flag, not runtime behavior — so it can run before the skill is ever exposed to live traffic.

## Enforcement

- **Mechanism:** A per-skill frontmatter or config flag that the platform reads before allowing model-triggered invocation (e.g., a `disable-model-invocation`-style boolean). When set, the skill's description is excluded from the model's available-triggers context entirely — the model cannot select it without the user having named it.
- **Check (lintable):** For every skill, inspect its procedure for side-effect operations (write/commit/deploy/send/spend, or an explicitly-flagged high-intensity mode). If any are present AND the explicit-invocation-only flag is absent → flag as under-specified.
- **Violation response:** Add the flag before the skill is exposed to model-triggered invocation. If the side effect is genuinely intended to be auto-triggerable (rare), document the rationale explicitly at authoring time rather than leaving it as an unexamined default.

## Rationale

Without an explicit control, any skill is vulnerable to firing on a description match alone — a vague request ("make sure my work is saved") can read as a match for a skill that commits or deploys, and the model invokes it before the human meant to authorize that specific action. This is a harness-level expression of a more general authority boundary: some operations require explicit human consent per-instance, and others the agent may perform on its own judgment. Marking side-effect skills as explicit-invocation-only moves that boundary from a hoped-for behavioral norm to a structural control the platform enforces before the skill's description ever reaches the model's decision surface.

The same control generalizes past literal side effects: a skill with no destructive action at all but a deliberately harsh or costly posture (an unusually strict review mode, for instance) belongs in the same category — the thing being gated is "the user should consciously opt into this," not narrowly "this changes external state."

## Failure Modes

- **Side-effect skill shipped without the flag.** The most direct failure: an author writes a capability with a real side effect, ships with default settings, and the model triggers it on a plausible-but-unintended description match. Mitigation: this rule, enforced at author- and audit-time.
- **False sense of security.** The flag prevents the model from auto-triggering the skill, but a user can still invoke it by name, and a skill that manages to get the user to type its name (e.g., via misleading suggested-next-step text) still runs. The flag gates model-initiated triggering, not the action itself once explicitly invoked — it is not a substitute for reviewing what a user-invoked skill actually does.
- **Override surfaces shadow the flag.** If the platform allows an external settings layer to flip a skill's invocation mode from outside the skill's own declaration, an author's intended trust boundary can be silently changed by someone else's configuration. Mitigation: audit tooling should check the effective invocation mode (declaration plus any override), not just the skill's own declared flag.
