---
name: "Passport Object — Decision-Level Governance Binding"
summary: "A per-decision artifact that permanently fuses action data with the exact policy bundle version, permits, denials, obligations, and evidence that governed the decision — making every agent action self-contained and auditable without log reconstruction."
implementation_notes: null
category: "Governance"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: "P2 (Design Required)"
applicability:
  - "General"
adopted_in: []
sources:
  - "policy-as-data-runtime-governance-agentic-systems.md"
related_findings:
  - file: "policy-as-data-runtime-governance-pattern.md"
    rel: "part-of"
  - file: "runtime-governance-gap-buildtime-to-production.md"
    rel: "solves"
  - file: "immutable-sessions-as-audit-architecture.md"
    rel: "same-problem"
  - file: "governance-memory-append-only-audit-layer.md"
    rel: "same-problem"
  - file: "five-commandments-for-agent-deployment-audit-first.md"
    rel: "same-problem"
date_discovered: "2026-04-19"
last_updated: "2026-04-19"
pipeline_status: "raw"
---

## What It Is

A **passport object** is a structured artifact generated at the moment an agent executes an action under the policy-as-data architecture. It permanently fuses:

- The action data (what the agent did, when, with what inputs/outputs)
- The exact policy bundle version that was bound at execution time
- The specific permits granted by that bundle
- The denials enforced
- The obligations that were required to fire
- The evidence that the rule required before execution was allowed

The passport is cryptographically bound to the bundle version, creating an immutable, self-contained record. An auditor presented with a passport object can answer every regulatory question — rule, version, evidence, approving authority — from the passport alone, without initiating any log search or developer query.

This differs from standard telemetry (timestamps, event records, execution traces, actor identifiers), which records *what happened* but not *what rule governed the decision*. The rule lived in a repository; it did not travel with the event. The passport makes the rule travel.

## Why It Matters

The diagnostic test for runtime governance: for any single active decision happening right now, can you name the rule that governed it? The version? The evidence evaluated? The approving authority? If answering those questions requires a log search, a Slack thread, or a developer — runtime governance does not exist.

Passport objects make this question instantly answerable. Every decision becomes self-documenting. The audit trail is not reconstructed after the fact; it is generated at the moment of execution and remains coherent across time, even as the underlying policy bundles evolve.

For regulated industries, this shifts compliance posture from "reconstruct and infer" to "cite and produce." The difference is material: one is archaeology, the other is a certificate.

## Why People Are Using It

Emerging in financial services and other regulated contexts where autonomous agent decisions must be provable to regulators. The pattern emerges directly from the failure of standard telemetry under regulatory scrutiny — engineers opening logs and discovering they cannot produce the definitive citation a regulator requires.

## Potential Improvements

- **Passport indexing**: A searchable index of passports by action type, agent, bundle version, or time window — enabling compliance teams to query decisions without opening individual files.
- **Passport diffing**: Comparing passports from the same action type across bundle versions to surface policy drift.
- **Lightweight passport variants**: Full passport for high-consequence actions; summary passport for routine operations — tiered by action risk level.
- **Cross-agent passport chains**: For multi-agent workflows where one agent's output is another's input, chaining passports to prove the full decision provenance.

## Potential Failure Modes

- **Passport storage growth**: Every agent action generates a passport. At high execution velocity, storage becomes a significant cost and operational burden.
- **Key management failure**: Cryptographic binding requires key management infrastructure. Key loss breaks the audit chain; key rotation requires a strategy for historical passports.
- **Passport tampering**: If the passport store is mutable, an actor with write access can falsify the record. The store must be append-only or otherwise tamper-evident.
- **Schema evolution**: As the passport schema evolves, older passports may become unreadable by newer audit tools. Version management for passport schemas is a parallel problem to policy bundle versioning.
- **False confidence**: A passport proves what rule was cited, not that the rule was correct or that the agent actually followed it. Compliance teams may treat passport existence as proof of compliance when it is only proof of citation.
