---
name: "Policy as Data — Runtime Governance Pattern"
summary: "Decouple governance rules from application code into versioned, machine-readable policy bundles that agents query and bind to at runtime, enabling instant policy updates without redeployment and cryptographically auditable decision trails."
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
  - file: "runtime-governance-gap-buildtime-to-production.md"
    rel: "solves"
  - file: "passport-object-decision-governance-binding.md"
    rel: "enables"
  - file: "three-enforcement-pipeline-architectures.md"
    rel: "extends"
  - file: "immutable-sessions-as-audit-architecture.md"
    rel: "same-problem"
  - file: "mcp-enterprise-governance-gaps.md"
    rel: "same-problem"
  - file: "structural-vs-psychological-vs-economic-governance.md"
    rel: "extends"
date_discovered: "2026-04-19"
last_updated: "2026-04-19"
pipeline_status: raw
---

## What It Is

Policy as data is an architectural pattern where governance rules are completely decoupled from application code and stored as independent, version-controlled, machine-readable objects called **policy bundles**. Each bundle is a structured document that specifies: permits granted, denials enforced, obligations that must fire, and the specific evidence required before execution is allowed.

At runtime, agents query a policy service and bind to a specific bundle version (e.g., v2.1) before executing an action. When the action completes, the system generates a passport object that permanently fuses the action data with the exact bundle version that governed it. Policy changes are made by promoting a new bundle version — every agent in scope binds to the new logic instantly, with no pipeline redeployment required.

This contrasts with **policy as code**, where compliance rules live in version-controlled repositories but only govern the deployment gate. Policy as code governs infrastructure provisioning and the moment a workload is released; it exits the room the millisecond the agent goes live.

## Why It Matters

Agentic systems contradict the assumptions baked into traditional policy enforcement. Standard software is built, deployed, and then remains still until the next patch. Autonomous agents process logic, trigger APIs, and spend money continuously between deployments — they are never still. Policy as code creates a visibility gap: you know what the agent was authorized to do at the deployment gate, but have zero mechanism to govern decisions made in production afterward.

Two failure modes this solves:

1. **Audit failure**: When a regulator asks why an agent executed an anomalous action three weeks ago, standard telemetry (timestamps, event records, execution traces) cannot answer "which rule governed this, in which version, with what evidence." The rule existed in a repo, was checked during the last build, but did not travel with the decision event. Reconstruction from logs is archaeology, not compliance.

2. **Update lag**: When a sudden event requires tightening risk thresholds immediately, the policy-as-code path requires an engineer to write a change, wait for a pipeline run, then a deployment. Meanwhile, active agents continue firing decisions under compromised parameters. In a multi-agent system, that lag translates to thousands of autonomous actions per hour under outdated policy.

Policy as data closes both gaps: rules travel with decisions, and updates take effect instantly.

## Why People Are Using It

Emerging pattern in regulated agentic deployments (financial services, healthcare, compliance-sensitive industries) where "we cannot prove what rule governed this decision" is a hard regulatory failure. The velocity mismatch between agent execution speed and deployment pipeline speed is the forcing function — agent networks execute faster than any human-gated deployment process can track.

## Potential Improvements

- **Runtime dials**: Compliance teams adjusting live thresholds without touching underlying code — a specialized form of policy as data where certain parameters are externalized as config rather than full bundle promotions.
- **Agent authority models**: Dictating exactly which agent archetypes are permitted to hold which policy types — the policy bundle anatomy needs a corresponding authority model to prevent agents from self-issuing elevated permissions.
- **Bundle promotion lifecycle**: Draft → review → active → deprecated stages with human gate at the promotion step.
- **Cross-bundle dependency tracking**: When one bundle references another, changes cascade and must be coordinated.

## Potential Failure Modes

- **Bundle proliferation**: Without discipline, the number of active policy bundle versions multiplies as different agent populations bind to different versions, creating a governance management problem.
- **Query latency**: Every agent action requiring a real-time policy service query adds latency. If the service degrades, agent operations block or fail.
- **Stale bindings**: Agents that cache a bundle version and don't refresh on promotion will continue executing under outdated policy — the very problem the pattern is meant to solve.
- **Cryptographic complexity**: Binding decisions to bundle versions cryptographically requires key management infrastructure. Key rotation or loss breaks the audit chain.
- **Evidence definition drift**: The bundle specifies what evidence is required before execution. If evidence schemas evolve faster than bundle versioning, bundles become incomplete or internally inconsistent.
