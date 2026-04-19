---
name: "Six-Layer Agent Infrastructure Stack (Named Layers with Maturity Assessment)"
summary: "Six infrastructure layers for agent systems: (1) Compute & Sandboxing, (2) Identity & Communication, (3) Memory & State, (4) Tools & Integration, (5) Provisioning & Billing, (6) Orchestration & Coordination. Each layer has distinct maturity (compute=mature, orchestration=biggest gap)."
implementation_notes: "Use as an audit framework for MetaSystem's own agent infrastructure. Identify which layers are covered, which are shims, and which are gaps."
category: "Orchestration"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
proposer_priority: "P2 (Design Required)"
applicability:
  - "S3 (Claude Code Build)"
  - "General"
adopted_in: []
sources:
  - "building-agents-on-layers-that-wont-exist.md"
proposals: []
date_discovered: "2026-04-07"
last_updated: 2026-04-08
related_findings:
  - file: "agent-architecture-layer-impermanence.md"
    rel: "extended-by"
  - file: "agent-management-tool-landscape-2026.md"
    rel: "same-problem"
pipeline_status: "synthesized"
consumed_by:
  - "agent-architecture-decisions.md"
---

# Six-Layer Agent Infrastructure Stack (Named Layers with Maturity Assessment)

## What It Is
A taxonomy of six infrastructure layers for agent systems, identified by Nate B Jones with market data for each layer. Extends the existing "agent architecture layer impermanence" finding with concrete named layers and maturity analysis:

1. **Compute & Sandboxing** -- E2B firecracker microVMs vs Daytona Docker containers; ephemeral vs persistent design split.
2. **Identity & Communication** -- Email-as-identity is a transitional shim.
3. **Memory & State** -- Mem0 hybrid architecture (graph+vector+KV) outperforms OpenAI by 26%.
4. **Tools & Integration** -- Compose.io managed integration vs direct MCP.
5. **Provisioning & Billing** -- Stripe Projects with 350ms DB provisioning, tokenized payments.
6. **Orchestration & Coordination** -- Biggest gap. Missing scheduling, merge coordination, supervision hierarchies, FinOps, and standard failure/recovery patterns.

## Why It Matters
Without named layers and maturity assessment, teams build on assumptions about infrastructure availability. The stack makes explicit which layers are mature (compute), which are transitional shims (identity), and which have critical gaps (orchestration).

## Why People Are Using It
Provides a concrete audit framework for agent infrastructure decisions. Teams can map their current stack to the six layers, identify where they are using shims vs native solutions, and prioritize investment in the least mature layers.

## Reliability Compounding Across the Stack

Jones highlights a critical infrastructure-level reliability problem: when an agent depends on five different primitives (one per layer), end-to-end reliability is the product of each layer's reliability. Five layers at 99% uptime each = 95% system reliability. Five layers at 97% each = 86%. This means stacking independently maintained infrastructure layers creates compounding liability -- distinct from the per-step reliability math in agent workflows (March of Nines). The March of Nines applies to sequential workflow steps; this applies to parallel infrastructure dependencies that must all be available simultaneously.

## Potential Improvements
MetaSystem could use this as an audit framework: map current infrastructure to the six layers, identify which are covered (e.g., memory via CLAUDE.md and context files), which are shims (e.g., identity via Claude Code sessions), and which are gaps (e.g., orchestration coordination between agents).

## Potential Failure Modes
Building on immature layers creates migration debt when native solutions emerge. The taxonomy itself may shift as the market consolidates -- layers may merge or new ones may appear. Over-investing in a shim layer delays adoption of the eventual standard.
