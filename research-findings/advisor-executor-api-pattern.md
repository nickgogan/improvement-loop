---
name: Advisor-Executor API Pattern (Opus Advises, Sonnet Executes)
summary: 'Anthropic''s Advisor Strategy pairs Opus as a reasoning-only advisor with Sonnet or Haiku as the tool-calling executor. Unlike plan-then-execute (one-shot), the advisor relationship is dynamic
  — Sonnet consults Opus whenever it hits a decision it can''t solve. Opus retains full shared context but never makes tool calls. Benchmarks: SWE-Bench 74.8 (with advisor) vs 72.1 (Sonnet alone), at lower
  cost ($0.96 vs $1.89 per task).'
implementation_notes: 'This is an API feature, not a Claude Code feature. Set type: ''advisor'' and max_uses in API calls. Relevant for any web application using Anthropic APIs.'
category: Model Selection
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
priority: P1 (Implement Now)
applicability:
- General
adopted_in: []
sources:
- anthropic-advisor-strategy-api.md
related_findings:
- file: multimodel-routing-architecture-specialized.md
  rel: same-problem
- file: planner-executor-deterministic-guardrails.md
  rel: same-problem
- file: task-specific-model-routing-table-march-2026-bench.md
  rel: same-problem
proposals: null
date_discovered: '2026-04-09'
last_updated: '2026-04-09'
pipeline_status: synthesized
consumed_by:
- agent-architecture-decisions.md
- model-resilient-prompt-engineering.md
---
# Advisor-Executor API Pattern (Opus Advises, Sonnet Executes)

## What It Is
Anthropic's Advisor Strategy is an API-level feature that pairs a powerful reasoning model (Opus) with a cheaper execution model (Sonnet or Haiku). The executor handles all tool calls and code generation. When it hits a decision point it can't resolve, it consults the advisor. The advisor has full shared context of what the executor is doing but never makes tool calls itself — it only provides reasoning guidance. This is more sophisticated than Claude Code's plan-then-execute mode: it's not a one-shot plan followed by execution, but an ongoing dynamic relationship where the executor consults the advisor as needed. The `max_uses` parameter controls how many advisory consultations are allowed per task. Benchmark results: SWE-Bench 74.8 (Sonnet + Opus advisor) vs 72.1 (Sonnet alone); Terminal-Bench 60.4 vs 58.1. Cost: ~$0.96 per task (with advisor) vs ~$1.89 (Sonnet alone) — better AND cheaper.

## Why It Matters
This creates a practical middle ground between Sonnet (good, cheap) and Opus (great, expensive). For API-based applications, it's strictly better than using Sonnet alone — higher quality at lower cost. It fills the "I want something between Sonnet and Opus" gap that many practitioners have expressed.

## Why People Are Using It
API developers building web applications report it as a "no-brainer" — better results for less money. The key insight is that Opus is overkill for most steps, but having it available for hard decisions dramatically improves the executor's output.

## Potential Alternatives
- Manual model routing (use Opus for planning, Sonnet for execution — more control but manual)
- Claude Code's plan mode (similar concept but one-shot, not dynamic)
- Single-model with higher temperature for exploration (cheaper but less reliable)

## Potential Improvements
- Automatic max_uses tuning based on task complexity
- Multiple advisor tiers (Opus for hard decisions, Sonnet for medium, Haiku for easy)
- Advisor transparency — logging which decisions required advisory consultation

## Potential Failure Modes
- max_uses set too low — executor makes bad decisions it should have consulted on
- max_uses set too high — unnecessary advisor calls, increasing cost
- Advisor context may drift from executor reality if the conversation is very long

## Extraction Note — 2026-04-19
Extracted as **pattern**: [[advisor-executor-api-pattern]] in `extracts/patterns/`
