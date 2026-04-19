---
name: Independent Evaluation and Scoped Authority as Deployment Commandments
summary: 'Two deployment commandments from Nate B Jones: (1) build observability and independent evaluation from day one — never trust agent self-reports, and (2) scope agent authority with explicit guardrails
  — define what agents can NOT do before expanding what they can do.'
implementation_notes: 'Directly applicable: MetaSystem hooks provide independent eval (linters, tests), and CLAUDE.md constraints provide authority scoping. Could be formalized as a pre-deployment checklist.'
category: Evaluation
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
proposer_priority: P1 (Implement Now)
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources:
- agent-produces-100x-org-reviews-3x.md
date_discovered: '2026-04-07'
last_updated: '2026-04-09'
related_findings:
- file: fix-data-schema-before-automating.md
  rel: same-problem
- file: acceptance-criteria-as-verifiable-eval-anchor.md
  rel: same-problem
- file: builder-validator-chain-pattern.md
  rel: same-problem
pipeline_status: "synthesized"
consumed_by:
  - "agent-safety-and-permissions.md"
  - "building-agent-evaluation-suites.md"
---
## What It Is
Two of Nate B Jones's five commandments for agent deployment, extracted as standalone patterns because they span Evaluation and Sandboxing:

**Commandment 4: Build observability and independent evaluation from day one.** Don't wait until agents fail to add monitoring. Instrument from the start with logging, metrics, and automated quality checks that run independently of the agent. "Stop letting agents tell you whether they are doing a good job."

**Commandment 5: Scope authority with explicit guardrails.** Define the negative space first — what agents explicitly cannot do. Start with minimal permissions and expand deliberately. Every permission expansion should be a conscious decision, not a default.

## Why It Matters
These two commandments address the most common production failure modes: agents that appear to work because they self-report success (Commandment 4), and agents that cause damage because their authority was never bounded (Commandment 5). Together they form the evaluation + sandboxing foundation for safe deployment.

## Why People Are Using It
Nate B Jones derives these from the $14K voice agent failure case study, where the agent functioned correctly but produced unusable data for months because no independent evaluation existed. The scoped authority pattern is reinforced by the "Production Database Wipeout" finding in the KB.

## Potential Improvements
Could be formalized as a pre-deployment checklist or a hook-based verification gate. Commandment 5 maps directly to Claude Code's tiered permission system.

## Potential Failure Modes
Over-constraining authority prevents agents from being useful. Over-instrumenting evaluation adds latency and cost. The balance point depends on the blast radius of failure.

## Extraction Note — 2026-04-19
Extracted as **pattern**: [[independent-eval-and-scoped-authority.md]] in `extracts/patterns/`
