---
name: Three-Tier Costed Eval System
summary: 'Three eval tiers with explicit costs: Tier 1 free static validation (<1s), Tier 2 E2E via claude -p (~$3.85/run), Tier 3 LLM-as-judge (~$0.15/run). Diff-based test selection. Gate tier (blocks
  merge) vs periodic tier (weekly cron) classification.'
implementation_notes: null
category: Evaluation
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
proposer_priority: null
applicability:
- S3 (Claude Code Build)
adopted_in: []
sources: []
related_findings:
- file: four-layer-production-eval-stack-with-golden-traces.md
  rel: same-problem
proposals: null
date_discovered: '2026-04-08'
last_updated: '2026-04-08'
pipeline_status: raw
consumed_by: []
---

# Three-Tier Costed Eval System

## What It Is
gstack implements three eval tiers with explicit costs: Tier 1 is free static validation (under 1 second, skill structure checks), Tier 2 is end-to-end testing via `claude -p` (approximately $3.85 per run, full skill execution), and Tier 3 is LLM-as-judge scoring (approximately $0.15 per run, output quality evaluation). Diff-based test selection runs only tests touching changed files. Evals are classified as either gate tier (blocks merge) or periodic tier (weekly cron). Eval runs are persisted with comparison across runs to track quality trends.

## Why It Matters
Most eval discussions focus on what to test, not what it costs. Explicit cost awareness enables rational tier classification — expensive evals run periodically rather than blocking every commit. Diff-based selection prevents running the full suite when only one skill changed. Gate vs periodic classification balances quality assurance with development velocity.

## Why People Are Using It
Observed in [gstack](https://github.com/garrytan/gstack) v0.15.16.0 — see [[gstack-analysis]] for structural details. Explicit cost awareness for evaluation. Most eval discussions focus on what to test, not what it costs. Tier classification (gate vs periodic) prevents expensive evals from blocking every commit while ensuring they run regularly.

## Potential Alternatives
Single-tier eval (run everything on every change). Cost-unaware tiering (fast vs slow without dollar tracking). Manual testing only. Production monitoring as eval replacement.

## Potential Improvements
Dynamic tier promotion (move periodic evals to gate tier when failure rate increases). Cost optimization by batching Tier 2/3 runs. Eval cost budgeting alongside agent execution budgets.

## Potential Failure Modes
Tier 1 static checks giving false confidence (passing structure checks with bad logic). Periodic tier missing regressions between cron runs. Cost estimates drifting from actual costs as model pricing changes. Diff-based selection missing cross-skill interaction regressions.
