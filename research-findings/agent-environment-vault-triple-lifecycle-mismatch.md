---
name: "Agent-Environment-Vault Triple Lifecycle Mismatch"
summary: "Hosted agent platforms create three coupled resources (agent definition, execution environment, credential vault) that have independent lifecycles. Archiving an agent does not archive its environment or vault, leading to orphaned resources that consume capacity and cost. The practitioner-recommended workaround is to always create agents through the quickstart flow (which bundles all three) rather than creating environments independently."
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
  - file: "isolation-resolver-worktree-lifecycle-algorithm.md"
    rel: same-problem
  - file: "anthropic-managed-agents-platform.md"
    rel: extends
  - file: "agent-cost-blowup-mitigation-strategies.md"
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

A resource management anti-pattern observed in Anthropic's managed agents platform where three tightly coupled resources -- the agent definition, the execution environment, and the credential vault -- have independent lifecycles despite being created together.

**The problem:**
- Creating an agent also creates an environment and (optionally) a vault
- Archiving an agent does NOT archive or delete the environment
- Archiving an agent does NOT archive or delete the vault
- Each resource type has its own management UI tab (Agents, Environments, Vaults)
- Orphaned environments and vaults continue consuming resources

**The practitioner-discovered workaround:**
"The simplest and easiest way to set all of this stuff up... is not to use this environment tab to create dedicated environments. But basically use either the quick start or the agents tab to create an agent and then alongside the creation of the agent you will create the environment and the credential vault if necessary. Otherwise it'll just have a bunch of additional environments per one agent."

**The cost warning:**
"Eventually this sort of thing is going to be priced in pretty hard. So make sure to get good use price reduction strategies earlier."

## Why It Matters

This is a specific instance of a general infrastructure pattern: when a platform creates coupled resources atomically but requires manual cleanup of each independently, resource sprawl is inevitable. The pattern matters for harness builders because any system that manages agent deployments (environments, credentials, configurations) must decide between:

1. **Cascading lifecycle** -- archiving the agent archives everything it created (simple but inflexible)
2. **Independent lifecycle** -- each resource managed separately (flexible but leak-prone)
3. **Reference-counted lifecycle** -- resources auto-archive when no active agents reference them

The current implementation chose option 2, and the practitioner immediately hit the consequences.

For MetaSystem, this is a cautionary pattern for any future managed agent deployments: lifecycle coupling between the agent definition and its resources must be explicit, or resource drift will accumulate.

## Why People Are Using It

Observed firsthand by a practitioner building multiple agents on Anthropic's managed platform. The practitioner created "a bunch of other proposal generators here as demos" and had to manually clean up orphaned environments.

## Potential Improvements

- Cascading archive: "archive agent" offers to also archive its environment and vault
- Dashboard warning for orphaned environments (environments with no active agents)
- Automatic cleanup policy: environments idle for N days with no active agent are flagged for deletion
- Cost attribution per agent that includes environment and vault costs

## Potential Failure Modes

- Over-aggressive cleanup: cascading deletes that remove environments shared by multiple agents
- Vault deletion removing credentials needed by other agents that share the vault
- "Pricing in" hosting costs making experimentation expensive and discouraging iteration
- Resource sprawl becoming a governance problem at scale (hundreds of orphaned environments across a team)
