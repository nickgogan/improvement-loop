---
name: "PR Acceptance Rate as Harness Multiplier Evidence (6.7% to 70%)"
summary: "Quantitative evidence that harnessing dramatically improves AI code quality: raw LLM-generated PRs have a 6.7% acceptance rate; harnessed workflows achieve approximately 70%. Corroborated by Stripe Minion shipping 1,300 AI-only PRs/week via harness. 40% of Claude Code's codebase is harness infrastructure. These data points collectively establish the ROI case for harness engineering investment."
implementation_notes: null
category: "Agentic Systems"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: "P2 (Design Required)"
applicability:
  - "S3 (Claude Code Build)"
  - "General"
adopted_in: []
sources:
  - "archon-open-source-harness-builder.md"
related_findings:
  - file: "harness-engineering-third-evolution.md"
    rel: "extends"
  - file: "specialized-harness-engineering-deterministic-rail.md"
    rel: "extends"
  - file: "march-of-nines-compounding-reliability-math-for-m.md"
    rel: "same-problem"
proposals: null
date_discovered: "2026-05-25"
last_updated: "2026-05-25"
pipeline_status: "synthesized"
consumed_by:
  - building-agentic-systems.md
tags:
  - "session-95-reextract"
---

## What It Is

Three quantitative data points that collectively make the ROI case for harness engineering:

1. **6.7% to ~70% PR acceptance rate**: Studies show that raw LLM-generated code has a 6.7% PR acceptance rate. Adding a harness (structured workflow with validation, context curation, and review steps) raises this to approximately 70% — a 10x improvement. Cole Medin references this study without naming it specifically.

2. **Stripe Minion: 1,300 AI PRs/week**: Stripe built a custom harness (similar to Archon but proprietary) around their AI coding workflow — context curation, validation, and enforcement at different workflow steps. The result: 1,300 AI-only generated pull requests shipped every week.

3. **40% of Claude Code is harness code**: The Claude Code source reveals that 40% of Anthropic's codebase for their flagship coding agent is dedicated to harness infrastructure — agent teams, sub-agent orchestration, and workflow management. This signals Anthropic's own investment thesis: harness engineering is where the value is.

Cole Medin uses these data points to argue that building a harness around a capable model (e.g., Opus) makes it "more powerful than [a frontier model] by itself" — the harness amplifies model capability beyond what raw model improvements alone can achieve.

## Why It Matters

These data points shift the investment calculus from "buy a better model" to "build a better harness." If a 10x improvement in PR acceptance rate is achievable through harness engineering, that return exceeds the marginal improvement from model upgrades. This has direct implications for MetaSystem: investing in the IL pipeline's automation (encoding the research-loop as a harness) may yield higher returns than waiting for model improvements.

The Stripe number (1,300 PRs/week) also establishes a scale benchmark: at production scale, harnesses enable volume that no human shepherding workflow could sustain.

## Why People Are Using It

These statistics have become community talking points for harness engineering adoption. Cole Medin, Anthropic's own agent teams feature, and Stripe's public numbers all point in the same direction: the harness is the multiplier, not the model.

## Potential Improvements

- Replicate these metrics internally: measure IL pipeline throughput and quality with vs. without automation
- Track per-step value attribution — which harness steps contribute most to the acceptance rate improvement
- Establish a "harness health" metric for MetaSystem's own workflows

## Potential Failure Modes

- The 6.7% to 70% comparison may not control for task difficulty — harnessed workflows might be applied to easier tasks
- Stripe's numbers are from a proprietary system with significant engineering investment — the cost to build must be weighed against the output
- The 40% harness code figure could indicate over-engineering rather than optimal investment
