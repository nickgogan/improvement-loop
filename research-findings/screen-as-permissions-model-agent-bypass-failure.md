---
name: Screen-as-Permissions-Model Agent Bypass Failure
summary: APIs designed for human-mediated screen access rely on the UI as an implicit permissions boundary. Agents bypass this entirely — calling APIs programmatically without screen constraints. In the
  Lilly/McKinsey incident, a $20 autonomous agent got read/write access to tens of millions of records via 22 unauthenticated endpoints out of 200. Any agentic system must treat every API surface as potentially
  callable by an adversarial agent.
implementation_notes: 'MetaSystem''s tool gating (approval.py patterns, permission allowlists) addresses this for internal tools. The finding''s relevance is to external API consumption: any API MetaSystem
  agents call should be audited for agent-unaware permission surfaces.'
category: Governance
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
priority: P1 (Implement Now)
applicability:
- General
adopted_in: []
sources:
- lilly-incident-agent-security-permissions.md
proposals: null
date_discovered: '2026-05-24'
last_updated: '2026-05-25'
related_findings:
- file: agent-identity-governance-enforcement-layer.md
  rel: same-problem
- file: tool-gateway-security-boundary.md
  rel: extends
- file: os-level-agent-sandboxing-filesystem-network-isolation.md
  rel: same-problem
- file: advisory-only-for-persistent-mutations.md
  rel: same-problem
- file: secure-by-default-posture-as-organizational-invariant.md
  rel: same-problem
- file: agent-aware-api-surface-design.md
  rel: extends
- file: cross-system-permission-composition-audit-gap.md
  rel: extends
- file: instant-agent-revocation-kill-switch-pattern.md
  rel: same-problem
pipeline_status: extracted
consumed_by:
  - "rules/screen-as-permissions-model-agent-bypass.md"
tags:
- governance
- sandboxing
- security
---

# Screen-as-Permissions-Model Agent Bypass Failure

## What It Is

A systemic vulnerability pattern: APIs designed for human users treat the screen (UI) as an implicit permissions boundary. When agents call these APIs programmatically, they bypass the screen entirely. Endpoints that were "safe" because humans could only reach them through a gated UI become directly callable by agents with no authentication.

## Why It Matters

The Lilly/McKinsey incident demonstrated this at production scale: 22 of 200 API endpoints shipped unauthenticated, including endpoints with production write access. A $20 autonomous agent achieved read/write access to data used by 70% of 40,000 consultants. This is not a hygiene failure — it is a systemic failure to design APIs for the assumption that agents (not just humans) will call them.

## How It Could Fail

The mitigation (authenticating every endpoint, scoping agent permissions separately from user permissions) adds friction to API design and slows deployment. Organizations may resist the overhead until they experience their own incident. The compound risk: as of early 2026, autonomous agents probing public endpoints for production data is "very normal."

## Evidence Strengthening — 2026-05-25

The video source's deeper analysis (beyond the initial incident report) reframes this as an industry-wide pattern, not a McKinsey-specific failure. Six vendor announcements in a single week (Anthropic, OpenAI, SAP, Pinecone, Salesforce, ServiceNow) converge on solving this gap. The source argues: "The model was never the hard part. The hard part is whether the agent can reach the right data, use the right permissions, trigger the right workflow, leave the right audit trail." Evidence strength upgraded from Medium to Strong based on production-scale incident evidence plus market-wide vendor response confirming the pattern's systemic nature.

## Extraction Note — 2026-05-24
Extracted as **rule**: [[screen-as-permissions-model-agent-bypass]] in `extracts/rules/`
