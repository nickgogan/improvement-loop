---
name: Secure-by-Default Posture as Organizational Invariant
summary: When teams move fast, the technical default determines security outcomes — not policies or documentation. In agentic systems, the question 'what happens when nobody configures security?' must answer
  'denied by default.' The Lilly incident's 22 unauthenticated endpoints out of 200 were not individual lapses but evidence that the platform's default posture was open, not closed.
implementation_notes: null
category: Governance
evidence_strength: Strong (production-tested)
adoption_status: Partially Adopted
priority: P1 (Implement Now)
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources:
- lilly-incident-agent-security-permissions.md
related_findings:
- file: screen-as-permissions-model-agent-bypass-failure.md
  rel: same-problem
- file: velocity-vs-operational-discipline-risk-pattern.md
  rel: same-problem
- file: tool-gateway-security-boundary.md
  rel: extends
- file: skill-security-scanner-fail-closed.md
  rel: same-problem
- file: middleware-as-enforcement-architecture.md
  rel: extends
proposals: null
date_discovered: '2026-05-25'
last_updated: '2026-05-25'
pipeline_status: synthesized
consumed_by:
- extracts/rules/secure-by-default-posture.md
- agent-governance-and-trust.md
tags:
- session-95-reextract
---

# Secure-by-Default Posture as Organizational Invariant

## What It Is

A governance principle that shifts the security question from "did you remember to configure security?" to "what is the system's behavior when nobody touches the security settings?" The answer must be: denied by default, not open by default.

The Lilly/McKinsey incident illustrates this precisely. 22 of 200 API endpoints shipped unauthenticated — including endpoints with production write access. The video source argues this was not 22 individual lapses by 22 engineers on 22 Fridays. It was evidence that the platform's default posture was permissive: endpoints shipped open unless someone explicitly closed them. Under deadline pressure, nobody closed them.

The key diagnostic questions:
1. What does the platform look like in two years if nobody touches the security settings after initial setup?
2. What happens when the team is told to move quickly — where does the technical default land?
3. If the technical team does not have time to discuss architecture with the business, does the system default to authenticated or unauthenticated?

If the answer to any of these is "open by default," the system will accumulate unauthenticated surfaces under normal operating pressure. The Lilly incident is the predictable outcome, not a surprising one.

## Why It Matters

This reframes the Lilly incident from a security hygiene failure to an organizational design failure. The distinction matters because the mitigations are completely different:

- **Hygiene framing** leads to training, checklists, and post-incident reviews — all of which assume the default is secure and the failure was deviation.
- **Default-posture framing** leads to architectural changes that make the secure path the path of least resistance — so that deviation from default produces security, not vulnerability.

For agentic systems specifically, permissive defaults are catastrophically more dangerous than for traditional SaaS. A human encountering an open endpoint still has screen-mediated access constraints. An agent encountering an open endpoint has unbounded programmatic access at machine speed.

## Why People Are Using It

The video source documents a convergent response from six major vendors (Anthropic, OpenAI, SAP, Pinecone, Salesforce, ServiceNow) — all shipping products that assume agents will touch their surfaces and designing for deny-by-default postures. Salesforce's headless 360 exposes APIs with identity and audit attached. ServiceNow's action fabric requires governed workflows with identity verification. The market signal is that permissive defaults for agent-facing surfaces are being eliminated.

## Potential Improvements

- Express default-posture requirements as compile-time or deploy-time checks rather than runtime policies — prevent permissive endpoints from shipping rather than detecting them after deployment.
- Apply the principle to MetaSystem's tool permission model: new tools should default to requiring approval, not to being auto-approved.
- Audit existing permission allowlists against this principle — are there tools that were allow-listed for convenience under deadline pressure?

## Potential Failure Modes

- **Over-restriction**: Deny-by-default can slow down development velocity if the process for granting access is heavy. The default must be restrictive, but the path to legitimate access must be lightweight.
- **Security theater**: Organizations claim deny-by-default but maintain broad exception lists that effectively negate it.
- **Audit fatigue**: When everything requires explicit approval, reviewers stop reading the approval requests carefully — recreating the permissive-default problem at the human layer.
