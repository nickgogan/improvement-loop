---
name: "Tool and Model IO Contracts with Preconditions and Idempotency"
summary: "Every external side effect in a governed multi-agent system is governed by a formal IO contract defining strict preconditions, rate limits, and idempotency rules. If preconditions are unmet, the effect is blocked — no exceptions."
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
  - file: non-deterministic-tool-contract-model.md
    rel: same-problem
  - file: tool-gateway-security-boundary.md
    rel: same-problem
  - file: context-warrant-justified-data-package.md
    rel: depends-on
date_discovered: "2026-04-19"
last_updated: "2026-04-19"
pipeline_status: raw
---

## What It Is

Step 7 of the 11-step governed multi-agent build order. After context is assembled (Step 5) and coordination state is established (Step 6), the system reaches the moment of authorized external effect — when the digital system impacts the physical or enterprise world. Tool and model IO contracts govern this moment.

**Three contract elements:**

1. **Strict preconditions** — conditions that must be true before the tool or model call can execute. These are not soft checks or logged warnings; failure to meet preconditions blocks the effect entirely. Preconditions may check actor authority, context warrant validity, state machine position, or external system state.

2. **Rate limits** — strict bounds on how often an effect can be triggered. Rate limits prevent runaway execution (agent loops calling the same tool repeatedly) and protect downstream systems from overload. Like preconditions, rate limit violations block execution, not just warn.

3. **Idempotency rules** — "item potency rules" define what happens if the same effect is triggered twice. This is critical for resilience: if an effect is retried due to network failure or state recovery, idempotent effects are safe; non-idempotent effects need explicit deduplication guards.

**Position in dependency chain:** IO contracts sit below provenance and audit (Step 8) — every effect execution is recorded in the audit trail (Step 8), creating a verifiable record of what the system actually did in the world. The contract is what makes that record meaningful: it proves the effect was authorized, not just that it occurred.

## Why It Matters

This pattern is distinct from `non-deterministic-tool-contract-model` (which addresses the AI-specific challenge that agents choose whether to call tools) and from `tool-gateway-security-boundary` (which focuses on security perimeters). IO contracts address the governance question: given that an agent has decided to call a tool and the call is within the security perimeter, what formal constraints govern execution?

The precondition-block pattern (rather than precondition-warn) is the critical design choice. Many systems log when preconditions fail but still execute the effect. This produces systems where governance failures are observable in hindsight but not preventable in the moment.

## Why People Are Using It

Practitioner-documented in the 11-step governance build order. The pattern draws on contract programming traditions (Eiffel, DbC) and applies them to the agent-tool interface. The "authorized external effect" framing emphasizes that tool calls are not just technical operations but governed events that carry accountability.

## Potential Improvements

- Contract inheritance: base contracts for common patterns (read-only, write-with-confirmation, destructive) that specific tools inherit and specialize
- Dynamic preconditions: preconditions that evaluate against live system state rather than static rules, enabling context-sensitive enforcement
- Effect simulation: before executing a real effect, simulate it to verify the result would be within expected bounds — catch violations before they happen rather than after

## Potential Failure Modes

- **Precondition enumeration gap**: Real systems have edge cases that precondition authors didn't anticipate; novel situations may bypass checks
- **Idempotency assumption violations**: Effects designed to be idempotent may not be in all downstream systems (the tool is idempotent; the API it calls is not)
- **Rate limit gaming**: Agents that can spawn sub-agents may distribute calls across identities to bypass per-identity rate limits
- **Contract maintenance lag**: As tool behavior evolves, contracts become stale; outdated contracts may block valid effects or permit invalid ones
