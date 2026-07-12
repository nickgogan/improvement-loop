---
title: "Composable Agent Teams"
id: "composable-agent-teams"
type: "pattern"
category: "agent-design"
target_system:
  - "improvement-loop"
stage: "active"
created: "2026-07-12"
updated: "2026-07-12"
author: "claude"
source_dd:
  - "DD-120"
  - "DD-60"
  - "DD-53"
  - "DD-63"
tags:
  - "pattern"
  - "agent-design"
  - "team-composition"
  - "methodology"
aliases:
  - "Agent team model"
  - "Project agent roles"
---

# Composable Agent Teams

**Provenance:** re-homed from DD-60 (2026-07-12, substrate-audit gate G3, via DD-120). This is a methodology the engine *teaches* — a pattern for composing project agent teams — not a rule the engine obeys. The engine's own actor model is the four-agent architecture (DD-82).

## The Pattern

Each project gets a composable agent team: project-scoped personas — markdown agent files in the project's `.claude/agents/` directory, instantiated from templates (`knowledge/templates/agent-templates/`) at bootstrap.

### The Mental Model

Agents are the employees of the project. Each has a distinct role, cognitive disposition, and responsibility boundary. They do not overlap. The human is always the final decision-maker and quality gate — not a participant in the agent loop.

### Core Roles

| Role | Owns | Produces | Does NOT | Cognitive Disposition |
|------|------|----------|----------|----------------------|
| **Product Owner** | what + why | PRD, acceptance criteria, prioritized backlog | Make technical/architectural decisions | Investigative. Treats every feature as a hypothesis. Asks "why does the user need this?" before "what should we build?" |
| **Systems Architect** | how (high-level) | Architecture doc, ADRs, phase breakdown | Write implementation code | Designs for longevity. Thinks in interfaces and boundaries. Biased toward simplicity — proposes the simplest architecture that works, justifies added complexity. |
| **Technical PM** | sequencing + risk | Task list, milestone defs, exit criteria | Make design or architecture decisions | Practical. Optimizes for forward momentum. Prefers working thing over perfect plan. Surfaces risks early. |
| **Engineer(s)** | implementation | Code + tests + implementation notes | Redesign architecture or reprioritize unilaterally | Craftsperson. Values clean, maintainable code. Treats tests as first-class deliverables. |
| **Tester** | verification | Test results, bug reports, compliance checks | Implement features or make design changes | Adversarial. Same competencies as engineers but different POV and incentives. Actively tries to break things. |

### Composability

Not every project needs every role:

- **Minimal team:** PO + Engineer (small utility projects)
- **Standard team:** PO + Architect + TPM + Engineer + Tester (software projects)
- **Extended team:** Standard + domain-specific engineers (backend, frontend, middleware)

Domain-specific engineers share the Engineer cognitive disposition but have specialized knowledge scopes. A backend engineer does not modify frontend code, and vice versa.

### Agent Persona Specification

Every agent is defined with these fields:

| Field | Purpose |
|-------|---------|
| **Role** | One-line identity |
| **Cognitive Disposition** | How this agent thinks — risk tolerance, trade-off stance |
| **Intention** | What this agent optimizes for |
| **Access Model** | What it can read and write — strict boundaries |
| **Handoff Artifact** | What it produces for downstream agents |
| **Escalation Triggers** | When it stops and asks for human input or escalates to another role |

### Project Scoping vs Workspace Scoping

- **Templates** are the canonical role definitions (`knowledge/templates/agent-templates/`).
- **Instances** live in each project's `.claude/agents/` — customized with project context.
- Agents do NOT share state across projects. Each project's team is independent.

## Related

- [[explore-then-harden]] — role behavior varies by development phase
- [[capability-type-selection]] — agent vs. skill decision framework
- DD-82 (the engine's own four-agent architecture), DD-63 (file-mediated handoffs), DD-29 (human gate), DD-64 (bootstrap instantiation)
