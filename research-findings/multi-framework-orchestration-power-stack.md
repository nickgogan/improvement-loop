---
name: Multi-Framework Orchestration Power Stack (Superpowers + GSD + gstack)
summary: 'Composite orchestration pattern chaining three frameworks: gstack for planning (CEO perspective), GSD for project management (context resets), Superpowers for execution (TDD), gstack QA for testing
  (Playwright). Each constrains a different dimension: perspective, environment, process.'
implementation_notes: P3 — adopt individual frameworks first, revisit composition. Note the Superpowers mega-orchestrator vs GSD fresh-session tension needs resolution.
category: Orchestration
evidence_strength: Weak (theoretical)
adoption_status: Not Yet Started
proposer_priority: P3 (Monitor)
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources:
- these-3-frameworks-make-claude-code-unstoppable.md
proposals: null
date_discovered: '2026-04-07'
last_updated: '2026-04-19'
related_findings:
- file: agent-architecture-layer-impermanence.md
  rel: contradicts
- file: agent-management-tool-landscape-2026.md
  rel: same-problem
- file: archon-yaml-defined-harness-workflows.md
  rel: same-problem
- file: concierge-agent-architecture-slack-notion-claude-c.md
  rel: same-problem
pipeline_status: raw
consumed_by: []
---

## What It Is

A composite orchestration pattern that chains three Claude Code frameworks in sequence, assigning each to the phase where it provides maximum leverage:

| Phase | Framework | Role |
|-------|-----------|------|
| **1. Planning** | gstack (CEO + Engineer Manager roles) | Transform vague idea into validated architecture and requirements |
| **2. Project Management** | GSD | Break the approved architecture into milestones, each scoped to <50% context window |
| **3. Execution** | Superpowers | TDD-driven feature implementation within each GSD milestone |
| **4. QA** | gstack (QA Lead role, Playwright) | Browser-level testing and bug reporting after each milestone |

The three frameworks are designed to be complementary rather than competing:
- gstack constrains **perspective** (who is thinking)
- GSD constrains **environment** (how much context is loaded)
- Superpowers constrains **process** (how work is structured)

## Why It Matters

Each individual framework addresses a different failure mode in long-running agentic coding sessions. Using any one in isolation leaves the other two failure modes unaddressed. The power stack is an attempt to achieve full coverage:

| Failure Mode | Addressed By |
|-------------|--------------|
| Vague/wrong requirements | gstack (CEO planning) |
| Context rot / hallucination | GSD (<50% resets) |
| Code drift / missing tests | Superpowers (TDD) |
| Untested UI / late-stage bugs | gstack (QA Playwright) |

## Why People Are Using It

- Described as a composite recommendation in source-001 (Eric Tech)
- Logical composition of three individually-validated frameworks
- No independent production evidence of the full stack being used as a unified system — this is a proposed combination, not a battle-tested workflow

## Potential Alternatives

| Alternative | Description | When to Prefer |
|-------------|-------------|----------------|
| Single framework adoption | Use only GSD or Superpowers | When complexity of managing three frameworks outweighs benefits |
| Custom pipeline design | Build your own phased workflow from primitives | When the three frameworks don't map cleanly onto your system's structure |

## Potential Improvements

- Create a standardized project bootstrap template that wires up all three frameworks with a single setup command
- Define clear handoff artifacts between phases (gstack → GSD milestone file → Superpowers spec → QA checklist)
- Measure accuracy/bug rate with and without the full stack to validate the composition empirically

## Potential Failure Modes

- **Framework conflicts**: Superpowers' mega-orchestrator conflicts with GSD's per-phase fresh sessions — these two frameworks have fundamentally different orchestrator models and may require reconciliation
- **Setup overhead**: Requiring developers to install and configure three separate frameworks before starting creates friction
- **Phase boundary ambiguity**: It's unclear when planning (gstack) ends and project management (GSD) begins in practice
- **Untested composition**: The three frameworks were designed independently; interaction effects are unknown
