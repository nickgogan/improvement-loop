---
name: "Runtime Governance Gap — Buildtime Policy Abandoned at Deployment"
summary: "Agentic systems create a structural governance gap: rules are designed at buildtime, validated at deployment, then left behind as agents execute continuously. Policy as code exits the room the moment the agent goes live, leaving production decisions ungoverned."
implementation_notes: null
category: "Governance"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
proposer_priority: "P2 (Design Required)"
applicability:
  - "General"
adopted_in: []
sources:
  - "policy-as-data-runtime-governance-agentic-systems.md"
related_findings:
  - file: "policy-as-data-runtime-governance-pattern.md"
    rel: "solved-by"
  - file: "passport-object-decision-governance-binding.md"
    rel: "solved-by"
  - file: "mcp-enterprise-governance-gaps.md"
    rel: "same-problem"
  - file: "three-enforcement-pipeline-architectures.md"
    rel: "same-problem"
  - file: "five-commandments-for-agent-deployment-audit-first.md"
    rel: "same-problem"
  - file: "agent-identity-governance-enforcement-layer.md"
    rel: "same-problem"
date_discovered: "2026-04-19"
last_updated: "2026-04-19"
pipeline_status: "raw"
---

## What It Is

A structural failure in how governance is applied to agentic systems. The problem has three layers:

**Layer 1 — The static assumption.** Traditional compliance tools (policy as code, infrastructure-as-code, CI/CD gates) were engineered for a world where systems are built, deployed, and then remain still until the next patch. The deployment gate is the enforcement point. Everything downstream is assumed to be static.

**Layer 2 — Agents contradict the assumption.** When an agentic workload is deployed, it wakes up. Decision nodes fire continuously. The agent allocates resources, routes work, triggers APIs, and spends money between deployments — it is never still. Oversight that only covers the deployment gate covers only a single moment in a system that never stops acting.

**Layer 3 — The gap compounds.** As agents execute, they move progressively further from the original stationary deployment gate. The farther they travel, the larger the gap between "what the agent was authorized to do at deployment" and "what rules are actually governing current decisions." In a multi-agent system, this gap translates to thousands of autonomous actions per hour under potentially outdated, misaligned, or unchecked parameters.

The gap is not a bug — it is a category error. Policy as code was purpose-built for infrastructure governance and deployment gates. Applying it to continuously executing agents is using the right tool in the wrong environment.

## Why It Matters

The gap produces two concrete failure modes:

1. **Audit failure**: Regulators cannot be shown the rule that governed a past decision because the rule did not travel with the decision. Log reconstruction is required, producing inference rather than citation. This fails regulatory scrutiny.

2. **Update lag risk**: Policy changes that must take effect immediately (e.g., emergency risk threshold tightening) must flow through the full deployment pipeline — write → pipeline run → deployment. Meanwhile agents continue executing under the outdated policy. Execution velocity always outpaces deployment velocity.

The framing matters: this is not primarily a security vulnerability or a tooling gap. It is a category-level architectural mismatch between tools designed for static systems and systems that are by design never static.

## Why People Are Using It

Recognition of this gap is emerging in regulated sectors (financial services, healthcare) that deploy autonomous agents in compliance-sensitive environments. The problem becomes visible when auditors or regulators request justification for specific agent decisions and engineering teams discover they cannot produce it.

The video source estimates this gap affects 99% of agentic systems currently deployed — a provocation, but directionally accurate: most organizations have not instrumented runtime governance because they inherited tooling designed for a pre-agent world.

## Potential Improvements

This is a problem frame, not a solution. The target state is an architecture where:
- Policy rules travel with every decision (passport objects)
- Policy updates take effect without deployment lag (policy bundles with instant promotion)
- Every production decision is answerable in real time: rule, version, evidence, authority

## Potential Failure Modes

The gap itself is the failure mode. Specific manifestations:
- **Regulatory exposure**: Inability to produce definitive compliance citations for past agent decisions.
- **Risk window**: Emergency policy changes that cannot reach running agents in time.
- **Invisible drift**: Agents running under policies that were correct at deployment but have been superseded by changed conditions — with no mechanism to detect or correct this at agent speed.
- **False confidence**: Organizations that assume deployment-gate governance covers production are not aware they have a gap. The most dangerous failure mode is not knowing the gap exists.
