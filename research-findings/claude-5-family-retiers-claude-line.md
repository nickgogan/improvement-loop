---
name: Claude 5 Family (Fable/Mythos) + Sonnet 5 Re-Tier the Claude Line
summary: 'Anthropic''s 2026 releases restructure Claude model routing, superseding the March-2026 consensus

  for the Claude entries. Claude Fable 5 (GA; Mythos 5 = same model, restricted release) is a new

  tier above Opus: SWE-Bench Pro 80.3% vs Opus 4.8''s 69.2% and GPT-5.5''s 58.6%; #1 on FrontierCode;

  distinctive long-horizon gains (3x Opus improvement in file-memory game harness; Stripe: 50M-line

  codebase migration in a day; Hex analytics >90% vs ~80%); 1M default context, 128k output; priced

  $10/$50 per M — 2x Opus 4.8''s $5/$25. Meanwhile Sonnet 5 (Jun 30, 2026) nearly closes the gap to

  Opus 4.8 on agentic benchmarks (Terminal-Bench 2.1: 80.4 vs 82.7; OSWorld-Verified: 81.2 vs 83.4;

  SWE-Bench Pro 63.2) at $3/$15 (intro $2/$10 through Aug 31). Net coarse routing: Sonnet 5 =

  default agent workhorse; Opus 4.8 = hard-reasoning value point; Fable 5 = long-horizon frontier

  at 2x Opus cost.'
implementation_notes: 'Registry impact: replaces the "Opus by default is a cost mistake, route to Sonnet 4.6" guidance

  from task-specific-model-routing-table-march-2026-bench for the Claude line (that finding''s

  non-Claude rows stand). Caveats for routing: (1) community reports Sonnet 5 at max effort can be

  worse AND costlier than Opus 4.8 at low/medium effort — effort-level tuning matters more than tier

  choice at the margin; (2) Sonnet 5''s new tokenizer inflates token counts 1.0-1.35x, so nominal

  price parity with Sonnet 4.6 is not effective-cost parity; (3) Fable 5 benchmark set is

  announcement-adjacent and should be re-anchored when independent numbers accumulate; (4)

  CodeRabbit: Fable 5''s "price and limited access kept it off our default review path" — practitioner

  default remains Opus/Sonnet with Fable for long-horizon jobs specifically.'
category: Model Selection
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
priority: null
applicability:
- General
adopted_in: []
sources:
- finout-claude-fable-5-mythos-5-benchmarks.md
related_findings:
- file: task-specific-model-routing-table-march-2026-bench.md
  rel: extends
- file: frontier-release-compression-march-2026.md
  rel: extends
- file: claude-code-max-plan-subsidy-vs-api-cost-tool.md
  rel: same-problem
- file: kimi-k2-line-near-opus-coding-with-safety-gap.md
  rel: same-problem
- file: center-vs-edge-of-distribution-task-classification.md
  rel: same-problem
- file: effort-level-tuning-as-first-order-cost-lever.md
  rel: extended-by
- file: gpt-56-soul-vs-fable-5-one-shot-head-to-head.md
  rel: extended-by
proposals: []
date_discovered: '2026-07-11'
last_updated: '2026-07-13'
pipeline_status: raw
consumed_by: []
---
# Claude 5 Family (Fable/Mythos) + Sonnet 5 Re-Tier the Claude Line

## What It Is

Two 2026 Anthropic releases that together restructure Claude-line model selection:

**Claude Fable 5 / Mythos 5** (Mythos-class tier above Opus; same underlying model — Fable GA with
additional dual-use safety measures, Mythos restricted to approved organizations):
- SWE-Bench Pro 80.3% (Opus 4.8: 69.2%; GPT-5.5: 58.6%); #1 FrontierCode
- Long-horizon differentiators: with file-based memory, 3× the improvement of Opus 4.8 in a
  long-horizon game harness; Stripe ran a 50M-line Ruby codebase migration in one day (est. two
  team-months); Cursor: "a class of long-horizon problems that were out of reach for earlier models"
- 1M-token default context, up to 128k output tokens
- $10/$50 per M tokens — 2× Opus 4.8, 3–5× Sonnet

**Claude Sonnet 5** (Jun 30, 2026): "most agentic Sonnet yet" — Terminal-Bench 2.1 80.4% (Sonnet 4.6:
67.0%; Opus 4.8: 82.7%), OSWorld-Verified 81.2% (Opus 4.8: 83.4%), SWE-Bench Pro 63.2% (Sonnet 4.6:
58.1%). Priced $3/$15 (intro $2/$10 through Aug 31, 2026), new tokenizer (+1.0–1.35× token counts).

## Why It Matters

The March-2026 routing consensus ("Sonnet 4.6 for coding; Opus by default is a cost mistake") is now
stale for the Claude line. The new coarse tiering: **Sonnet 5** for most agent workloads (near-Opus
at Sonnet price), **Opus 4.8** for the hardest reasoning when Fable's cost/access isn't justified,
**Fable 5** when long-horizon capability is the constraint. Skill↔model coupling note: skills
authored against Sonnet 4.6-era behavior should be re-validated on Sonnet 5 (new tokenizer, adaptive
thinking, different effort semantics).

## Why People Are Using It

Fable 5: long-horizon jobs previously infeasible (multi-week engineering compressed to a day).
Sonnet 5: near-Opus agentic capability at 1/3–1/5 the cost; safety profile improved over Sonnet 4.6
in agentic contexts per Anthropic's own assessment.

## Potential Failure Modes

- Fable 5 numbers are early/announcement-adjacent (Finout synthesis of Anthropic + partner cases);
  independent replication pending.
- Sonnet 5 at high effort can invert the value proposition vs Opus 4.8 at low effort (community
  reports) — effort level is a hidden routing variable.
- Tokenizer change breaks naive cost comparisons and possibly prompt-length-sensitive skills.
- Mythos 5 access (Project Glasswing) is not generally plannable-for.
