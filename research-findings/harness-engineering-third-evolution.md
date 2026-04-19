---
name: Harness Engineering as Third Evolution Beyond Context Engineering
summary: The progression from prompt engineering (single LLM, single output) to context engineering (single agent, curated context) to harness engineering (multiple agent sessions, orchestrated workflow)
  represents the maturation of AI-assisted development. Harness engineering makes AI coding deterministic and repeatable by wrapping agent sessions in structured workflows.
implementation_notes: null
category: Orchestration
evidence_strength: Medium (practitioner-documented)
adoption_status: Partially Adopted
proposer_priority: P2
applicability:
- General
adopted_in: []
sources:
- archon-open-source-harness-builder.md
related_findings:
- file: agent-sprawl-anti-pattern-microservices-redux.md
  rel: same-problem
- file: legitimate-multi-agent-domains-taxonomy.md
  rel: same-problem
- file: org-chart-hierarchy-as-scalable-claude-code.md
  rel: same-problem
proposals: null
date_discovered: '2026-04-09'
last_updated: '2026-04-19'
pipeline_status: raw
consumed_by: []
---

## What It Is
A framing for the evolution of AI development practices: (1) Prompt engineering (2022-2024): crafting single prompts for single outputs. (2) Context engineering (2024-2025): curating the full context window for a single agent session — CLAUDE.md, skills, tools, memory. (3) Harness engineering (2025-2026): orchestrating multiple agent sessions into reproducible workflows with deterministic validation steps. Each evolution built on the previous. Harness engineering doesn't replace context engineering — it requires good context engineering at each node.

## Why It Matters
This framing helps practitioners understand where to invest effort. Most teams are still at the context engineering stage. The harness engineering stage unlocks reproducibility — you can run the same workflow across projects, across teams, with consistent quality. It's what separates demo-quality agents from production systems.

## Why People Are Using It
40% of Claude Code's codebase is harness infrastructure. Stripe ships 1,300 AI PRs/week via harness. The pattern has convergent adoption across both commercial (Anthropic, Stripe) and open-source (Archon, GSD, BMAD) ecosystems.

## Potential Failure Modes
- Premature harness engineering before context engineering is solid (bad inputs → bad outputs, faster)
- Over-engineering workflows for simple tasks where a single session suffices
- Conflating harness complexity with harness quality
