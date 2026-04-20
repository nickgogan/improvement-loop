---
name: Teach Orchestrator to Delegate with Detailed Subtask Descriptions
summary: 'Lead agents must provide each subagent with: objective, output format, tool/source guidance, and task boundaries. Vague instructions like ''research semiconductor shortage'' cause duplication,
  gaps, and misinterpretation. Detailed decomposition is the delegation skill.'
implementation_notes: Applicable to MetaSystem's skill orchestration. Any skill that spawns subagents should include structured subtask descriptions, not just topic keywords.
category: Orchestration
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
priority: P1 (Implement Now)
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources:
- anthropic-multi-agent-research-system.md
related_findings:
- file: orchestrated-execution-one-task-per-sub-agent-wit.md
  rel: extends
- file: sprint-contract-negotiation-pattern.md
  rel: same-problem
- file: effort-scaling-rules-embedded-in-orchestrator.md
  rel: enables
proposals: null
date_discovered: '2026-04-09'
last_updated: '2026-04-09'
pipeline_status: raw
consumed_by: []
---

## What It Is

A prompt engineering pattern for orchestrator agents. When delegating to subagents, the lead agent must provide four elements per subtask: (1) clear objective -- what the subagent should find or produce, (2) output format -- how the result should be structured, (3) tool/source guidance -- which tools to use and which sources to prefer, (4) task boundaries -- what is explicitly out of scope to prevent overlap. Without this structure, subagents given vague instructions like "research semiconductor shortage" all search for the same thing, producing duplicate results or irrelevant 2021 crisis data instead of 2025 supply chain analysis.

## Why It Matters

Delegation quality is the highest-leverage intervention in multi-agent systems. The orchestrator's decomposition determines whether subagents work in parallel on complementary tasks or duplicate effort on the same task. Anthropic's system outperforms single-agent Opus 4 by 90.2% on their internal eval -- but only with properly structured delegation.

## Why People Are Using It

Anthropic's production multi-agent research system. The pattern was discovered through failure analysis: early versions with vague delegation produced duplicate results and missed important angles.

## Potential Improvements

Auto-generation of delegation structures from query analysis. Templates for common delegation patterns (compare, enumerate, analyze).

## Potential Failure Modes

Over-specification constraining subagent creativity. Delegation structure that doesn't match the actual information landscape (e.g., specifying sources that don't have the needed data). Maintenance burden of keeping delegation templates current.

## Extraction Note — 2026-04-19
Extracted as **pattern**: [[teach-orchestrator-to-delegate-pattern.md]] in `extracts/patterns/`
