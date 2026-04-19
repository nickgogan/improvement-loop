---
title: "Three-Tier Agent Primitive Architecture"
type: "extracted-artifact"
assigned_form: "pattern"
source_finding: "claude-code-12-agent-primitives"
confidence: "HIGH"
tier: "auto"
reason_codes: []
co_occurrence: null
extraction_date: "2026-04-19"
identification_report: "2026-04-19-identification-report-3.md"
deployed: false
deployed_to: null
contract:
  preconditions: "The agent system has moved past prototyping into sustained use. A tool registry and at least basic permission controls exist."
  invariants: "Infrastructure primitives are implemented before adding model sophistication. Each tier is complete before the next tier is built on top of it."
  governance: "Tier coverage is audited at each major system milestone. New primitives are added to the appropriate tier with justification."
  recovery: "If a tier is discovered to be incomplete after building higher tiers, pause higher-tier work and backfill the missing primitives before proceeding."
tags:
  - "extracted-artifact"
  - "pattern"
---

# Three-Tier Agent Primitive Architecture

**Source:** [[claude-code-12-agent-primitives]]
**Form:** pattern
**Extraction date:** 2026-04-19

## Problem

Teams building agent systems invest most effort in model selection and prompt engineering (the 20% that is visible) while neglecting the infrastructure primitives that determine whether the system is reliable, observable, and recoverable in production (the 80% that is invisible). Without a structured inventory of required primitives, teams discover gaps reactively -- after a crash loses session state, after a runaway agent exceeds budget, after a failure produces no diagnostic trace.

## Forces

- **Prompt appeal vs. infrastructure discipline.** Better prompts produce immediately visible improvements; infrastructure primitives (logging, budget tracking, crash recovery) are invisible until something breaks.
- **Incremental complexity.** Agent systems grow from simple chat interfaces to multi-tool, multi-session, multi-agent architectures. Each growth stage requires new primitives that were unnecessary at the prior stage.
- **Over-engineering risk.** Small projects do not need all 12 primitives. Implementing everything upfront wastes effort and adds maintenance burden.
- **Observability cost.** Structured event logging and multi-layer verification add latency and token overhead that compete with the agent's primary work.

## Solution

**Organize agent infrastructure into three tiers of primitives, built bottom-up. Each tier must be substantially complete before investing in the next.**

**Tier 1 -- Tools and Permissions (foundation):**
- Tool registry with metadata-first design (capabilities, constraints, safety classification per tool)
- Permission system with trust tiers (graduated from safe-by-default to requires-approval)
- Session persistence surviving crashes (state reconstructable from disk, not just memory)

**Tier 2 -- Persistence and Execution (operational control):**
- Budget tracking with pre-turn projection (know before a turn whether it will exceed budget)
- Execution counts and routing decisions (track what ran, how often, and why)
- Workflow state machine (planned, awaiting_approval, executing, waiting_on_external)

**Tier 3 -- Observability and Verification (production confidence):**
- Structured event logging (actions, not words -- log what happened, not what was intended)
- Multi-layer verification (separate verification agent with read-only permissions)
- Failure recovery with provable rollback (every state transition is reversible)

The key insight is the 80/20 inversion: production agents are 80% infrastructure, 20% model. Teams that invest proportionally -- infrastructure first, model quality second -- build systems that survive contact with real users.

## Consequences

**Positive:**
- Provides a concrete checklist for evaluating agent system maturity at any scale.
- Bottom-up ordering prevents the common failure of building sophisticated model behavior on unreliable infrastructure.
- Each tier is independently valuable -- Tier 1 alone significantly improves reliability over unstructured agent setups.
- The three-tier model maps cleanly to team skill allocation: Tier 1 is systems engineering, Tier 2 is operations, Tier 3 is SRE/observability.

**Negative:**
- All 12 primitives are overkill for small, single-session, single-tool agents. Teams must judge which tier depth is appropriate for their scale.
- Tier 3 primitives (multi-layer verification, structured event logging) add measurable latency and token cost.
- The specific primitives are derived from one production system (Claude Code). Other agent architectures may need different primitives or different tier assignments.
- Cargo-culting the full set without understanding the constraints that motivated each primitive produces bureaucratic infrastructure that slows development without improving reliability.

## Known Uses

- Anthropic's Claude Code (512K lines TypeScript, serving millions of users) -- the primary source of the 12-primitive inventory.
- Independently validated by multiple analysts (Nate B Jones, Agentic Lab, Latent Space) who examined the leaked source.
- MetaSystem partial coverage: tool registry (skills system), permission system (governance rules), session persistence (PROGRESS.md). Missing: budget tracking, structured event logging, multi-layer verification, failure recovery.

## Contract

### Preconditions
The agent system has moved past prototyping into sustained use with real users or real data. At minimum, a tool registry and basic permission controls exist (Tier 1 entry point). The team has committed to treating infrastructure as a first-class concern, not an afterthought.

### Invariants
Infrastructure primitives are implemented before adding model sophistication at the same tier. Each tier is substantially complete before building the next tier on top of it. The 80/20 ratio (infrastructure vs. model) is treated as a design principle, not a precise measurement.

### Governance
Tier coverage is audited at each major system milestone using the 12-primitive checklist. New primitives are added to the appropriate tier with written justification. Primitives are not removed without demonstrating they are unnecessary at the current system scale.

### Recovery
If a tier is discovered to be incomplete after building higher tiers (e.g., session persistence gaps discovered after implementing verification), pause higher-tier work and backfill the missing primitives before proceeding. Document the gap and its impact in the System Log.
