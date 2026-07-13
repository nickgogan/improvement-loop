---
name: "Token-Burn Telemetry as Delegation-Adoption Metric"
summary: |-
  Plain English: your token-consumption curve over time is a receipt showing whether the
  unit of work you hand to AI is actually growing — chat-sized asks stay flat; delegated
  jobs (find sources, produce artifact, verify, keep going) bend the curve. Jones mapped
  his own burn over a year: 510M tokens in one peak day, 300-500M/day sustained, with
  the inflection attributed to computer use + model 5.5 unlocking whole workflows at
  once. The explicit anti-pattern: the number is not a target ("burn half a billion
  tokens" would be a dumb goal) — it is diagnostic evidence that behavior changed from
  asking for answers to assigning jobs.
implementation_notes: null
category: "Governance"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Partially Adopted"
priority: "P3 (Monitor)"
applicability:
  - "IL (session telemetry, delegation-depth tracking)"
  - "General"
adopted_in:
  - "Improvement Loop"
sources:
  - "codex-your-first-personal-ai-agent-delegation-loop.md"
related_findings:
  - file: "token-budget-as-headcount-replacement-resource-model.md"
    rel: "extends"
proposals: null
date_discovered: "2026-07-13"
last_updated: "2026-07-13"
pipeline_status: "raw"
consumed_by: []
---

# Token-Burn Telemetry as Delegation-Adoption Metric

## What It Is

Using longitudinal token-consumption data as a behavioral measure of delegation depth.
Jones's own receipts: a local Codex log showing 510M tokens in one day (2026-05-20,
under one Codex Max account, no marginal billing), sustained 300-500M/day since, mapped
back over a full year. The curve's inflection coincides with computer use + model 5.5
landing — the moment whole workflows (files, browser, rendering, verification) became
delegable at once. His interpretation discipline is the finding's core:

- The number went up because **the unit of work changed**, not because he typed more
  prompts — "if that only meant I was typing more prompts, it would be really
  embarrassing."
- The chart is "a receipt, not a scoreboard" — evidence of changed behavior, never a
  vanity target.

This is the individual-level extension of the KB's org-level "token budget as headcount
replacement" finding (YC: measure token usage directionally to see who is leveraging AI
— with the same explicit anti-gamification warning).

## Why It Matters

Delegation adoption is hard to observe directly; self-reports are unreliable. A burn
curve read *directionally* distinguishes chat-mode usage (flat) from job-mode usage
(step changes on capability unlocks). For the engine, the same lens applies to session
telemetry: tokens-per-session trending with subagent fan-out is evidence the
delegation model is actually being exercised, not just documented.

## Why People Are Using It

First-person measured data (local logs, year-long baseline) from a practitioner running
delegation at unusual volume; the org-level version is corroborated independently by
YC's revenue-per-employee observations already in the KB.

## Potential Improvements

- Normalize by outcome: tokens-per-shipped-artifact or per-accepted-gate, so the metric
  can't be inflated by waste.
- Annotate the curve with capability events (model releases, harness features) to
  attribute inflections, as Jones did informally.

## Potential Failure Modes

- Goodhart risk, called out in the source itself: the moment burn becomes a target,
  agents and people generate busy-work loops (Jevons-style fill).
- Confounds: retries, failed runs, and runaway loops also raise burn — a rising curve
  can mean broken harness, not deeper delegation, without outcome normalization.
- Provider-side accounting bugs make single readings untrustworthy (the KB's
  cost-observability finding recommends independent log-based accounting).
