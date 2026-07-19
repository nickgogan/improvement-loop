---
title: "Declare Capabilities as Tiers, Not Booleans"
type: "extracted-artifact"
assigned_form: "rule"
source_finding: "tiered-capability-registry-engine-behavior-branching"
extraction_date: "2026-07-19"
last_change_session: 152
last_change_report: "designing-agent-tools.harvest-queue"
deployed: false
deployed_to: null
context:
  applies_to:
    - "engines or orchestration layers that integrate two or more backends, providers, or tool implementations offering the same feature at different levels of fidelity"
    - "teams building or maintaining a capability registry, feature-detection layer, or provider-adapter system that gates behavior on what each integration supports"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "specify"
  reversibility: "low — migrating a boolean capability field to a tiered enum requires a schema change plus updating every consumer branch that reads the field; reverting is a symmetric rewrite, not a simple flag flip"
  auditability: "high — a tiered registry is enumerable and diffable; reviewers can check that every tier has a declared consumer behavior without executing the system, though verifying the declarations match actual backend behavior requires runtime bench-testing"
  evidence_strength: "Medium (practitioner-documented)"
  adoption:
    status: "Not Yet Started"
    notes: "Observed in one production multi-backend coding-agent orchestration project at extraction time (its provider registry uses this exact tiered-declaration shape); no broader cross-system adoption signal collected yet."
contract:
  preconditions: "An engine or orchestration layer integrates two or more backends, providers, or tool implementations that support at least one shared feature at differing levels of fidelity. A capability registry, config, or manifest is the mechanism by which those capabilities are declared and consumed."
  invariants: "Every gradable feature's capability field is a discriminated/enum value, not a boolean. Every tier in the enum's vocabulary has an explicitly declared consumer behavior (enforce / verify-and-retry / refuse-or-degrade, or an equivalent named ladder). Workflow and orchestrator code branches on the declared capability tier, never on backend/provider identity."
  governance: "Owner: whoever maintains the capability registry schema and the consumer code that branches on it. New backend registrations must declare a tier for every gradable feature in the schema before activation. New features added to the registry must define per-tier consumer behavior before any backend consumes them. Schema changes to the tier vocabulary (adding or removing a tier) follow the same review as other capability-registry changes — not ad hoc."
  recovery: "If a boolean capability field is found for a feature with more than two meaningfully distinct support levels → flag for migration to a tiered enum before the next schema version ships. If a declared tier has no corresponding consumer behavior → block consumption of that tier until the behavior is authored; do not silently fall through to another tier's behavior. If a backend's declared tier is found to drift from its actual behavior (bench-verification gap) → re-verify and correct the declaration; treat undetected drift as an open risk, not a closed issue. If a new backend's capability doesn't fit the existing tier vocabulary → treat as a deliberate schema-change decision (add a tier), not a silent lossy mapping."
tags:
  - "extracted-artifact"
  - "rule"
  - "capability-registry"
  - "tiered-design"
  - "multi-provider"
---

# Declare Capabilities as Tiers, Not Booleans

**Source:** [[tiered-capability-registry-engine-behavior-branching]]
**Form:** rule
**Extraction date:** 2026-07-19

## Condition

An engine, orchestrator, or integration layer drives behavior across two or more backends, providers, or tool implementations that support the same feature to different degrees of fidelity — one supports it natively and fully, another approximates it, a third doesn't support it at all. A capability registry, config file, or manifest declares what each backend supports for that feature.

## Action

**Required:** Represent capability claims for a gradable feature as a discriminated (enum) value with a closed, named vocabulary of tiers — not as a boolean. For every tier in that vocabulary, spell out explicit consumer behavior:

- **Enforce** — deliver the feature via the strict, native mechanism for backends declared at the top tier.
- **Verify-and-retry** — deliver a degraded-but-usable mechanism and check its output for correctness with a bounded retry loop, for backends declared at a middle "best-effort" tier.
- **Refuse-or-degrade** — explicitly fail closed, or fall back to a documented alternative delivery mechanism, for backends declared unsupported at the bottom tier — never silently attempt the strict mechanism, and never silently omit the feature without signaling it.

Workflow and orchestrator code branches on the declared capability tier, never on backend or provider identity — no scattered `if (provider === 'x')` conditionals standing in for a capability check.

**Forbidden:** Expressing capability support as `true`/`false` where three or more meaningfully distinct behaviors exist. Adding a backend or provider without declaring its tier for every gradable feature the registry covers. Leaving a declared tier without a corresponding consumer behavior (silent degradation). Branching engine behavior on backend identity instead of the declared tier.

## Boundary

Enforced at registry-authoring time — when a new backend, provider, or tool is registered, or a new feature's capability field is added to the schema — and at consumer-authoring time, when workflow or orchestrator code reads the capability field to decide how to deliver the feature.

Does not apply to features every backend supports identically; those may remain a plain existence check with no tiering value. This rule governs the design/config layer, not runtime drift detection — pairing it with bench-verification of the declared tiers (see Failure Modes) is a separate, complementary discipline.

## Enforcement

- **Mechanism:** The registry schema types the capability field as an enum (not a boolean) for any feature with more than one meaningfully distinct support level. Consumer code that dispatches on capability reads the enum and switches on it; a schema lint or type-check can flag a boolean field on a gradable-feature domain.
- **Check (deterministic):** `(capability_field_type == enum OR explicit "no gradation" exemption is documented) AND (every tier in the vocabulary has a declared consumer behavior)`. Either branch false → violation.
- **Violation response:**
  - *Boolean field found for a gradable feature:* flag for migration to a tiered enum before the next schema version ships.
  - *Tier declared with no consumer behavior:* block consumption of that tier until the missing behavior branch is authored.
  - *Behavior branches on backend identity rather than declared tier:* refactor to branch on the capability field.
- **Cannot be self-certified:** Schema/type-level enforcement (the registry's own type system rejecting a boolean where an enum is required) is more reliable than prose review alone — gradation drift is easy to miss when only reading code, not the schema.

## Rationale

Boolean capability flags force a lie at the margins: a backend that partially or approximately supports a feature is neither fully `true` nor fully `false`. The caller either over-trusts it — treats partial as full and gets silent failures at the edges — or under-uses it — treats partial as none and wastes real capability the backend actually has. Declaring the tier as data, with consumer behavior spelled out per tier, turns a graceful-degradation ladder into something reviewable and diffable, instead of scattered per-backend conditionals buried in code.

The generalizable move is that the feature is written once against the capability contract, and every backend gets the strongest delivery mechanism its declared tier supports — the registry is the seam that lets new backends be absorbed without forking engine behavior per backend.

## Failure Modes

- **Declared tiers drift from actual behavior.** A backend labeled at the top tier quietly regresses to best-effort behavior in a later release, and the registry has no way to see it because the tier was declared once and never re-checked. Mitigation: pair tiered declarations with periodic bench-verification of the claims, not one-time self-reported labeling.
- **Tier vocabulary ossifies.** A new backend's capability doesn't cleanly fit any existing tier, forcing either a lossy mapping (pick the nearest tier and accept the mismatch) or a breaking schema change. Mitigation: treat tier-vocabulary changes as a deliberate, reviewed schema change, not an ad-hoc addition made to unblock one backend.
- **Verify-and-retry cost explosion.** The best-effort tier's validate-and-retry loop can multiply token or latency cost several-fold on backends that ultimately still fail. Mitigation: bound retry attempts explicitly, and treat repeated best-effort failures as a signal to reconsider the backend's declared tier.
- **Enum-wrapped boolean.** A team adds an enum with only two values that map 1:1 onto `true`/`false`, satisfying the letter of the rule while missing its point. Mitigation: treat "no gradation" as an explicit, reviewed exemption decision — not the default shape an enum wrapper produces.

## Contract

### Preconditions
An engine or orchestration layer integrates two or more backends, providers, or tool implementations that support at least one shared feature at differing levels of fidelity. A capability registry, config, or manifest is the mechanism by which those capabilities are declared and consumed.

### Invariants
Every gradable feature's capability field is a discriminated/enum value, not a boolean. Every tier in the enum's vocabulary has an explicitly declared consumer behavior (enforce / verify-and-retry / refuse-or-degrade, or an equivalent named ladder). Workflow and orchestrator code branches on the declared capability tier, never on backend/provider identity.

### Governance
Owner: whoever maintains the capability registry schema and the consumer code that branches on it. New backend registrations must declare a tier for every gradable feature in the schema before activation. New features added to the registry must define per-tier consumer behavior before any backend consumes them. Schema changes to the tier vocabulary (adding or removing a tier) follow the same review as other capability-registry changes — not ad hoc.

### Recovery
If a boolean capability field is found for a feature with more than two meaningfully distinct support levels → flag for migration to a tiered enum before the next schema version ships. If a declared tier has no corresponding consumer behavior → block consumption of that tier until the behavior is authored; do not silently fall through to another tier's behavior. If a backend's declared tier is found to drift from its actual behavior (bench-verification gap) → re-verify and correct the declaration; treat undetected drift as an open risk, not a closed issue. If a new backend's capability doesn't fit the existing tier vocabulary → treat as a deliberate schema-change decision (add a tier), not a silent lossy mapping.
