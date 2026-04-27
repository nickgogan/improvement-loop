---
title: "Reach L6 Personally Before Attempting L7 — Maturity Sequencing Rule"
type: "extracted-artifact"
assigned_form: "rule"
source_finding: "context-infrastructure-seven-level-maturity-model"
identification_report: "building-agentic-systems.harvest-queue.md::context-infrastructure-seven-level-maturity-model::rule::reach-l6-before-l7"
extraction_date: "2026-04-27"
last_change_session: 83
last_change_sl: "session-83-codifier-ib164-resume-extract-artifacts"
deployed: false
deployed_to: null
context:
  applies_to:
    - "operators rolling out team-level agentic systems"
    - "organizations adopting personal-then-team OS patterns"
    - "decision points at the boundary between individual context infrastructure and shared team infrastructure"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "specify"
  reversibility: "moderate — defer-L7 decision is reversible (re-attempt later); rolling back a premature L7 deployment requires unwinding sync, permission scaffolding, and team training"
  auditability: "high — operator's personal L6 cadence is observable (vault activity, scheduled task logs, daily-brief consumption); pre-L7 readiness is checkable"
  evidence_strength: "Medium"
  adoption:
    status: "Practitioner-recommended"
    notes: "Beni's published practitioner framework derived from operating an AI-as-OS for self and team. Ordering recommendation aligns with general systems-engineering principle of stabilizing the unit of one before scaling. No counter-evidence in the KB; corroborating findings on second-brain centralization (L6) and team-sync mechanics (L7) are present but do not directly test the ordering claim."
contract:
  preconditions: "An operator or team is considering deploying L7 (team OS — second brain synced across team via Relay/GitHub/Obsidian Sync, with permission settings and a designated context operator). The operator has already implemented some prior level (L1-L6) of context infrastructure. The seven-level maturity model is the diagnostic frame in use."
  invariants: "L7 (team OS) deployment is gated on prior achievement of L6 (centralized personal second brain) by the operator who will own the team layer. L6 readiness means: a single Obsidian vault holds the operator's cross-area context, scheduled tasks add real-time context, skills reference vault files rather than embedding copies, and the operator's personal cadence (capture → enrich → consume) is working without operator-introduced friction. Any L7 rollout that the operator's own L6 cadence does not yet sustain is forbidden."
  governance: "Owner: Any decision-maker authorizing team-OS rollout. The rule must be embedded in the L7 rollout decision checklist or pre-deployment readiness review. The check is observable: review the operator's vault activity, scheduled-task health, and the frictionlessness of their personal capture-and-consume loop. Exemption: an organization that explicitly chooses to skip L6 must document the synchronization complexity it accepts and assign a context operator who has personally cleared L6 elsewhere."
  recovery: "If L7 has been deployed before L6 is stable → freeze new L7 work; route the responsible operator's personal context through L6 first; resume L7 only when the personal cadence is sustained. If team-sync complexity is already manifesting (merge conflicts, ambiguous ownership, stale context, permission disputes) → diagnose against L6 readiness rather than adding L7 tooling. If the operator cannot reach L6 personally → reassign the context operator role rather than continuing L7 rollout."
tags:
  - "extracted-artifact"
  - "rule"
  - "agentic-systems"
  - "maturity-model"
  - "sequencing"
  - "team-os"
  - "second-brain"
---

# Reach L6 Personally Before Attempting L7 — Maturity Sequencing Rule

**Source:** [[context-infrastructure-seven-level-maturity-model]]
**Form:** rule
**Extraction date:** 2026-04-27

## Condition

A team or operator is considering deploying L7 of the seven-level context-infrastructure maturity model — a business OS where a centralized second brain is synced across a team via Relay (or GitHub / Obsidian Sync), with per-folder read/write permissions and a designated context operator owning the layer. The operator who will own L7 has implemented some prior level (L1-L6) of personal context infrastructure.

Scope of application: any decision point at which an L7 rollout could be authorized — initial deployment, expansion to a new team, or re-launch after a previous attempt.

## Action

**Required:** Verify, before authorizing L7 rollout, that the operator's personal L6 cadence is working — a single Obsidian vault holds their cross-area context, scheduled tasks are adding real-time context, skills reference vault files rather than embedding copies, and the operator's personal capture-enrich-consume loop runs without operator-introduced friction.

**Forbidden:** Authorizing L7 (team OS) without prior achievement of L6 (centralized personal second brain) by the operator who will own the team layer. Treating "we use Obsidian" as evidence of L6; the diagnostic is whether the cadence is working, not whether the tools are installed. Distributing the context-operator role across multiple people who have not individually cleared L6.

**Permitted alternatives:** Defer L7 until L6 is stable. Continue investing in L6 (more vault coverage, scheduled-task expansion, skill-vault integration) until the personal cadence is sustained. Reassign the prospective context-operator role to a person who has personally cleared L6 elsewhere.

## Boundary

Enforced at the L7 rollout decision boundary — the moment any team-sync mechanism (Relay, GitHub, Obsidian Sync), per-folder permission scheme, or shared context channel is being authorized to go live. Applies from the moment L7 is proposed until either:
- L6 readiness is verified and L7 is authorized, *or*
- L7 is deferred and the personal L6 work continues.

The rule does not regulate L1-L5 transitions, which can be undertaken in any order suitable to the operator's scale.

## Enforcement

- **Mechanism:** Pre-deployment readiness review at the L7 rollout decision point. The reviewer (Owner of the rollout decision, or context operator's manager) inspects: (a) the operator's vault activity over the prior N weeks; (b) scheduled-task health (are real-time enrichments running without manual intervention?); (c) skill-to-vault references (do skills point to vault files rather than embedding copies?); (d) operator self-report of friction in their personal capture-enrich-consume loop.
- **Check (deterministic):** `(operator_owns_l6 == true) AND (l6_cadence_sustained_for_review_window == true) AND (operator_assigned_to_l7 == operator_who_cleared_l6)`. Any branch false → defer L7.
- **Violation response:**
  - *L7 authorized without L6 readiness:* freeze new L7 work; route the responsible operator's personal context through L6 first; resume L7 only when the personal cadence is sustained.
  - *L7 already deployed and team-sync complexity is manifesting:* diagnose against L6 readiness rather than adding L7 tooling; if the operator's personal L6 is the gap, regress L7 scope until L6 is stable.
  - *Operator cannot reach L6 personally:* reassign the context operator role rather than continuing L7 rollout.
- **Cannot be self-certified by the prospective L7 operator alone:** the readiness review involves at least one external reviewer who can observe vault activity and scheduled-task health.

## Rationale

The seven-level maturity model distinguishes two architectural inflection points: L3 (static → portable/testable) and L6 (distributed → centralized). L7 (centralized → synchronized-across-team) layers team-sync complexity on top of L6's centralized substrate. If the centralized substrate is not yet stable for the operator personally, L7 multiplies that instability across the team — synchronization complexity (merge conflicts, ambiguous ownership, stale context, permission disputes) compounds before context quality is established.

The practitioner recommendation underlying this rule is direct: "The business recommendation is to reach L6 personally before attempting L7." The failure mode is documented in the same source: L7 without L6 foundation creates synchronization complexity before context quality is established.

This rule is the positive-space reformulation of a known sequencing failure. Instead of enumerating L7 failure modes (sync conflicts, ownership ambiguity, permission churn, stale shared context), the positive invariant is "personal L6 first, then team L7." One rule; bounded enforcement at a single decision boundary.

## Failure Modes

- **Tools-installed mistaken for cadence-working.** Team adopts Obsidian and a sync mechanism, declares L6 achieved, jumps to L7. The diagnostic is whether the operator's personal capture-enrich-consume loop is running, not whether the toolchain is installed. Mitigation: the readiness review inspects activity and friction, not tool presence.
- **Skipped levels without explicit accounting.** Team skips L4-L5 and lands at "L7" via a SaaS team-knowledge product. The model is descriptive of progressively-resolved limitations, not prescriptive of rigid stages — but skipping L6 means the unresolved limitation (centralization) propagates into L7. Mitigation: if L6 is skipped, document the synchronization complexity accepted and assign a context operator who has personally cleared L6 elsewhere.
- **Distributed context-operator role.** Team assigns "context ownership" to a committee or to no one specific. L7's architectural assumption is a single context operator owning the layer. Mitigation: name a single operator; verify their personal L6.
- **Treating the model as prescriptive rather than descriptive.** Teams may correctly skip levels appropriate for their scale (e.g., a solo operator may not need L5 area-projects). The L6→L7 ordering is the load-bearing claim; other transitions are flexible. Mitigation: the rule scopes to the L6→L7 boundary specifically.
- **Context quality conflated with context structure.** L6 readiness is about structure (centralized, real-time-enriched, skill-integrated). What goes into the vault — context quality — is a separate concern this model does not address. Mitigation: do not use this rule to certify context quality; use it only for sequencing the structural transition.

## Contract

### Preconditions
An operator or team is considering deploying L7 (team OS — second brain synced across team via Relay/GitHub/Obsidian Sync, with permission settings and a designated context operator). The operator has already implemented some prior level (L1-L6) of context infrastructure. The seven-level maturity model is the diagnostic frame in use.

### Invariants
L7 (team OS) deployment is gated on prior achievement of L6 (centralized personal second brain) by the operator who will own the team layer. L6 readiness means: a single Obsidian vault holds the operator's cross-area context, scheduled tasks add real-time context, skills reference vault files rather than embedding copies, and the operator's personal cadence (capture → enrich → consume) is working without operator-introduced friction. Any L7 rollout that the operator's own L6 cadence does not yet sustain is forbidden.

### Governance
Owner: Any decision-maker authorizing team-OS rollout. The rule must be embedded in the L7 rollout decision checklist or pre-deployment readiness review. The check is observable: review the operator's vault activity, scheduled-task health, and the frictionlessness of their personal capture-and-consume loop. Exemption: an organization that explicitly chooses to skip L6 must document the synchronization complexity it accepts and assign a context operator who has personally cleared L6 elsewhere.

### Recovery
If L7 has been deployed before L6 is stable → freeze new L7 work; route the responsible operator's personal context through L6 first; resume L7 only when the personal cadence is sustained. If team-sync complexity is already manifesting (merge conflicts, ambiguous ownership, stale context, permission disputes) → diagnose against L6 readiness rather than adding L7 tooling. If the operator cannot reach L6 personally → reassign the context operator role rather than continuing L7 rollout.
