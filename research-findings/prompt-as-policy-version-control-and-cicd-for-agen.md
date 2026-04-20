---
notion_id: 3351e08b-9b34-816d-b3cf-d0cc063369e5
name: Prompt-as-Policy -- Version Control and CI/CD for Agent Prompts
summary: 'Production discipline treating agent prompts as versioned policy artifacts with: explicit ROLE/AUTHORITY/CONSTRAINT/FAILURE SIGNAL properties; Git-like diff history with commit messages and rollback;
  A/B testing infrastructure with traffic splitting; CI/CD hooks for automated prompt validation before deployment; APO (Automated Prompt Optimization) as policy iteration. Tools: Maxim AI, LaikaTest, Kore.ai.
  Directly extends Skills 2.0 with the change-management layer.'
implementation_notes: 'Currently Skills in the KB are versioned informally. Prompt-as-Policy formalizes this with testable properties and automated optimization. Skills 2.0 Benchmark mode is the evaluation
  layer; version control provides the change management layer. APO operationalizes automated prompt policy iteration. Sources: https://www.reddit.com/r/PromptEngineering/comments/1q8elob/prompting_apo_and_agentic_systems_in_2026/'
category: Prompt Craft
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- S3 (Claude Code Build)
adopted_in: []
sources:
- ai-agent-prompt-engineering-best-practices-inflect.md
proposals: []
date_discovered: '2026-04-01'
last_updated: 2026-04-08
related_findings:
- file: advanced-elicitation-techniques-library.md
  rel: same-problem
pipeline_status: synthesized
consumed_by:
- model-resilient-prompt-engineering.md
---
# Prompt-as-Policy -- Version Control and CI/CD for Agent Prompts

## What It Is
A production discipline that treats agent prompts as versioned policy artifacts. Four explicit properties: ROLE, AUTHORITY, CONSTRAINT, FAILURE SIGNAL. Version control lifecycle includes testing, versioning, A/B deployment, monitoring, and rollback. APO (Automated Prompt Optimization) provides policy iteration.

## Why It Matters
Formalizes skill versioning with testable properties and automated optimization.

## Why People Are Using It
Purpose-built tooling emerging (Maxim AI, LaikaTest, Kore.ai).

## Potential Failure Modes
Requires investment in test harness infrastructure. APO can overfit to narrow eval sets. Version control sprawl without governance.
