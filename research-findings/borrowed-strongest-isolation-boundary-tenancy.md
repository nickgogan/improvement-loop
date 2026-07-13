---
name: "Borrow the Strongest Available Isolation Boundary for Tenancy"
summary: |-
  Rather than engineering ever-stronger custom isolation, Replit puts every customer's
  deployed apps in a dedicated Google Cloud project — including free tier — because the
  GCP project boundary is the strongest tenant-isolation primitive Google offers: the
  same boundary that separates Google from its own customers, hardened by years of
  adversarial attention. Defense-in-depth logic: even if a malicious agent escapes its
  container, the next wall it hits is Google's own tenancy boundary. The trade: GCP
  projects are operationally heavyweight (billing, quotas, lifecycle), so Replit had to
  build internal automation most companies could not sustain. The threat model
  justification: AI agents running arbitrary code void the friendly-customer assumption
  of classic PaaS isolation — isolation must assume hostile. Secondhand — verify against
  Replit primary sources.
implementation_notes: null
category: "Sandboxing"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: "P3 (Monitor)"
applicability:
  - "General"
adopted_in: []
sources:
  - "replit-agent-engineering-teardown.md"
related_findings:
  - file: "three-layer-reversible-state-single-undo-surface.md"
    rel: "same-problem"
proposals: null
date_discovered: "2026-07-13"
last_updated: "2026-07-13"
pipeline_status: "raw"
consumed_by: []
tags:
  - "sandboxing"
  - "multi-agent"
  - "infrastructure"
---

# Borrow the Strongest Available Isolation Boundary for Tenancy

## What It Is

A tenancy design heuristic: identify the strongest isolation primitive your platform
provider already offers — the one hardened by the provider's own adversarial exposure —
and place your tenant boundary there, even when it looks operationally oversized.
Replit's instance: one GCP project per customer for deployments, with container/namespace
isolation remaining the inner (development-time) layer. Complemented by a clean
dev/production world split: the agent's flexible, reversible development environment
never touches the locked-down deployed app; dev messes roll back, production never sees
them.

## Why It Matters

Two transferable ideas. First, the **threat-model shift**: an AI agent is a tenant that
runs weird commands, installs arbitrary packages, and may be steered by a malicious
prompt — the "reasonably well-behaved developer" assumption underlying classic container
isolation is dead, so agent platforms need a stronger boundary than human platforms did.
Second, the **borrowing move**: security boundaries earn trust through adversarial
exposure, and a provider's own tenant boundary has absorbed more attack attention than
any custom sandbox you could build; renting that boundary converts a security engineering
problem into an (automatable) operations problem.

## Why People Are Using It

Named in the teardown as one of its five explicit lessons ("you can borrow somebody
else's strongest isolation boundary"). The same shape appears wherever agent platforms
choose hypervisor/microVM/account-level boundaries over shared-kernel containers for
untrusted agent code.

## Potential Alternatives

- **MicroVMs (Firecracker-class)** per agent — stronger than containers, lighter than
  cloud projects; the common middle choice.
- **Hardened shared-kernel containers** (gVisor-class syscall filtering) — cheapest,
  weakest; acceptable when the agent surface is already stripped down.
- **Physical/account-level separation** (one cloud account per tenant) — the same
  borrowing move one level up; even heavier operationally.

## Potential Failure Modes

- **Operational drowning** — per-tenant provisioning, quota, billing, and cleanup at
  project granularity requires dedicated internal tooling; adopting the pattern without
  that automation investment fails on lifecycle management, not security.
- **Cost floor** — heavyweight boundaries price out high-tenant-count/low-revenue tiers
  unless the provider's primitive is genuinely free to hold.
- **Inner-layer complacency** — the borrowed outer wall can rationalize weak inner
  isolation; the pattern is defense-in-depth, not defense-substitution.
