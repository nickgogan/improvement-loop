---
name: "Actor Passport Schema — Bound, Governed Agent Identity"
summary: "Every actor in a governed multi-agent system is wrapped in a passport schema carrying role bindings, authority ceilings, and trust markers. Agency becomes a bound, verifiable identity rather than an anonymous prompt — enabling runtime policy validation of rights."
implementation_notes: null
category: "Governance"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: "P2 (Design Required)"
applicability:
  - "General"
adopted_in: []
sources:
  - "11-step-governance-build-order-multi-agent-systems.md"
related_findings:
  - file: governed-dependency-chain-build-order.md
    rel: part-of
  - file: policy-as-data-machine-readable-constraints.md
    rel: depends-on
  - file: agent-identity-governance-enforcement-layer.md
    rel: same-problem
  - file: context-warrant-justified-data-package.md
    rel: enables
date_discovered: "2026-04-19"
last_updated: "2026-04-19"
pipeline_status: "raw"
---

## What It Is

Step 4 of the 11-step governed multi-agent build order. After defining what policies govern the system, the architecture must define who can act within it. The actor model assigns every permitted actor a passport schema — a structured identity artifact that the policy layer consults at runtime.

**Passport schema components:**

1. **Role bindings** — which roles the actor holds (e.g., orchestrator, executor, auditor). Roles determine which events the actor may trigger.
2. **Authority ceilings** — the maximum scope of action the actor is permitted, regardless of role. A ceiling prevents privilege escalation even if a role temporarily gains broader permissions.
3. **Trust markers** — verifiable signals of the actor's trustworthiness (e.g., authentication source, delegation chain, JIT provisioning timestamp).

**The threshold of agency capture:** This is the layer where anonymous prompts become governed identities. From this point in the dependency chain, every event has a bound identity and a strictly defined authority limit. Before the actor model, agency is implicit (any prompt can claim any role). After it, agency is explicit and verifiable.

**Runtime validation flow:** When an actor triggers an event, the policy layer (Step 3) validates the actor's passport against the event's authority requirements. If the actor's passport does not carry the required role bindings or exceeds its authority ceiling, the event is blocked.

## Why It Matters

Most agent systems treat identity as an afterthought — agents are differentiated by their system prompts, not by verifiable identity structures. This creates a governance gap: policies can be written but not enforced, because there is no runtime mechanism to verify who is actually acting.

The passport schema pattern closes this gap. It is a prerequisite for any audit trail that traces actions to specific actors. Without bound identities, "agent X did Y" cannot be proven — only inferred from log context. With passport schemas, actor identity is asserted, validated against policy, and recorded in the provenance trail (Step 8).

This differs from `agent-identity-governance-enforcement-layer` (HITL focus, JIT provisioning for ephemeral agents, time-boxed decision lanes) in that it focuses on the structural artifact — the passport schema — and its role in the dependency chain.

## Why People Are Using It

Practitioner-documented in the 11-step governance build order. The pattern aligns with identity-first security principles from enterprise IAM (identity and access management), applied to multi-agent systems. The EU AI Act's requirement for demonstrable human oversight is easier to satisfy when every agent action is tied to a verifiable actor identity with documented authority limits.

## Potential Improvements

- Dynamic passport issuance: passports generated at agent spawn time (JIT) rather than statically pre-defined, enabling time-bound authority and automatic expiry
- Delegation chains: when an orchestrator spawns a sub-agent, the sub-agent's passport derives from the orchestrator's authority ceiling — it cannot exceed its parent's permissions
- Passport revocation: mechanisms to invalidate passports mid-execution if an actor's trust markers are violated or authority is withdrawn

## Potential Failure Modes

- **Static passport staleness**: Authority ceilings or role bindings that were correct at provisioning time but become incorrect as the system evolves
- **Trust marker forgery**: If trust markers are not cryptographically verifiable, actors may self-assert trust they don't hold
- **Overly coarse roles**: Roles that are too broad grant more authority than needed for any specific task, violating least-privilege
- **Passport bypass**: Actors that interact with the system through channels that don't check passports — gaps in the enforcement perimeter
