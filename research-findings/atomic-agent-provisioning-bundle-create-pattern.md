---
name: "Atomic Agent Provisioning (Bundle-Create Pattern)"
summary: "Creating an agent through a quickstart flow atomically provisions all three required resources -- agent definition, execution environment, and credential vault -- in a single operation. This is preferred over creating each resource independently because it guarantees correct coupling and avoids orphaned resources. The practitioner recommendation: always use the agent creation flow, never the environment tab."
implementation_notes: null
category: "Orchestration"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: P3 (Monitor)
applicability:
  - "S3 (Claude Code Build)"
  - "General"
adopted_in: []
sources:
  - "anthropic-managed-agents-platform.md"
related_findings:
  - file: "agent-environment-vault-triple-lifecycle-mismatch.md"
    rel: same-problem
  - file: "anthropic-managed-agents-platform.md"
    rel: extends
  - file: "production-configuration-baseline-discipline.md"
    rel: same-problem
proposals: null
date_discovered: "2026-05-25"
last_updated: "2026-05-25"
pipeline_status: "classified"
consumed_by: []
tags:
  - "session-95-reextract"
---

## What It Is

A provisioning pattern where agent creation bundles all dependent resources into a single atomic operation. Observed in Anthropic's managed agents platform:

**Quickstart/Agents tab flow (recommended):**
1. Describe agent -> platform generates spec
2. Click "create agent"
3. Platform atomically creates: agent definition + execution environment + credential vault
4. All three resources are correctly linked from the start

**Manual flow (anti-pattern):**
1. Create environment separately via Environments tab
2. Create vault separately via Vaults tab
3. Create agent and try to link to existing environment/vault
4. Result: "a bunch of additional environments per one agent" -- resource sprawl

The practitioner explicitly recommends: "The simplest and easiest way to set all of this stuff up so far I found is not to use this environment tab to create dedicated environments. But basically use either the quick start or the agents tab to create an agent and then alongside the creation of the agent you will create the environment and the credential vault if necessary."

## Why It Matters

This is a concrete instance of the general infrastructure principle: coupled resources should be provisioned together. When resources are created independently and then linked, three problems emerge:

1. **Coupling errors** -- wrong environment attached to wrong agent
2. **Orphaned resources** -- environments and vaults created but never linked to an agent
3. **Cognitive overhead** -- operators must remember which resources belong to which agents

For harness builders, the lesson is that agent deployment should be a single atomic action that provisions everything the agent needs. The "advanced" option of creating resources independently should exist but should not be the default path.

This maps to the MetaSystem pattern where the `/bootstrap` skill creates all fractal directories atomically rather than requiring manual directory creation -- the same principle applied to infrastructure provisioning.

## Why People Are Using It

Practitioner discovery through direct use of Anthropic's managed agents platform. The recommendation emerged after the practitioner experienced the alternative (creating environments independently) and found it produced resource sprawl.

## Potential Improvements

- Platform defaults to bundle-create and warns when users try to create resources independently
- Dependency graph visualization showing which resources belong to which agents
- Import/export of complete agent bundles (agent + environment + vault as a single portable artifact)
- Clone operation that duplicates an entire bundle for rapid iteration

## Potential Failure Modes

- Bundle-create may be too opinionated for advanced use cases where one environment serves multiple agents
- Atomic provisioning hides complexity that operators need to understand for debugging (e.g., which vault stores which credentials)
- Platform lock-in: atomic bundles are easy to create but hard to migrate to another platform
- No partial rollback: if vault creation fails, the agent and environment may already be created, creating an inconsistent state
