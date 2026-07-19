---
name: Harness Cost Readouts Are Unreliable — Use Independent Log-Based Accounting
summary: 'On subscription plans, in-harness cost surfaces (Claude Code /cost and /usage, Codex''s

  equivalent) can disagree with each other and with reality — one run showed $99 in one

  readout and $3 in another for the same session, and API-cost lines sometimes don''t

  appear at all. Any cost claim should come from independent log-based accounting

  (e.g. `npx ccusage@latest session` for Claude Code, or pure API metering via a

  gateway), not from the harness''s own display.'
implementation_notes: 'Directly applicable to the engine''s session telemetry (capture_quality is already

  "estimated" for cost/token fields) and to any cost figure entering the KB or the

  model-capability registry: prefer log-derived numbers, and mark harness-readout

  numbers as suspect. Design: a small log-accounting step in telemetry capture rather

  than trusting /cost.'
category: Evaluation
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources:
- i-made-gpt-56-and-fable-5-build-the-same-app.md
related_findings:
- file: claude-code-max-plan-subsidy-vs-api-cost-tool.md
  rel: same-problem
- file: gpt-56-soul-vs-fable-5-one-shot-head-to-head.md
  rel: enables
proposals: null
date_discovered: '2026-07-13'
last_updated: '2026-07-13'
pipeline_status: synthesized
consumed_by:
- verifying-agent-output.md
- rules/log-based-cost-accounting-over-harness-readouts.md
---

# Harness Cost Readouts Are Unreliable — Use Independent Log-Based Accounting

## What It Is

While measuring per-build costs for a model head-to-head, Pat Simmons found the
harnesses' own usage displays inconsistent on subscription plans:

- Claude Code `/cost` and `/usage` disagreed for the same session ($99 vs $3 on one
  build); on another, the API-cost line simply didn't show up.
- Codex offered no findable session-cost surface at all.
- His workaround: run `npx ccusage@latest session` (an independent tool that computes
  usage from local logs; a Codex equivalent exists) via a side agent, and treat those
  numbers as the accurate ones. He still flags all his cost figures with "grain of
  salt" and notes it's only cleanly measurable on pure API metering (e.g. OpenRouter).

The pattern: **cost observability is a harness bug surface** — when usage is
subsidized/abstracted by a subscription, the harness's self-reported cost is a display
feature, not an accounting system. Independent, log-derived accounting is the reliable
source.

## Why It Matters

Cost numbers drive routing decisions (model tiering, plan-vs-API tradeoffs, subagent
budgets), and the KB records such numbers as evidence. If the measurement instrument is
buggy, downstream decisions inherit the error. The engine's own telemetry block records
tokens/cost as "estimated" — this finding says which estimation source to prefer:
log-based accounting over harness readouts.

## Why People Are Using It

Practitioner-documented from a real measurement failure during a recorded comparison;
the ccusage tool exists precisely because the community hit the same gap. Corroborates
the Max-plan-subsidy finding's observation that subscription economics obscure true
usage costs.

## Potential Improvements

- Session-start instrumentation ("track this thoroughly from the start next time" — the
  author's own stated fix) rather than post-hoc log mining.
- Harness vendors reconciling /cost and /usage; until then, treat divergence between
  the two surfaces as the signal to distrust both.

## Potential Failure Modes

- **Log tools drift with harness log formats** — ccusage-style tools break silently
  when the harness changes its log schema.
- **Subscription-plan accounting is inherently notional**: "what it would cost via API"
  is a modeled number even when the token counts are right.
- **n=1 evidence for the specific bug** — the discrepancy pattern is one practitioner's
  observation on one harness version pair.

## Extraction Note — 2026-07-19
Extracted as **rule**: [[log-based-cost-accounting-over-harness-readouts]] in `extracts/rules/`
