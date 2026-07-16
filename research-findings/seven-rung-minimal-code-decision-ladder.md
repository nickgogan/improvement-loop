---
name: Seven-Rung Minimal-Code Decision Ladder (Reuse Before Write)
summary: 'Plain English: the biggest token savings in AI coding come from not writing code — a

  fixed decision ladder the agent must climb before generating anything new. The Ponytail

  skill''s seven checks, in order: (1) is this needed at all (YAGNI), (2) does it already

  exist in the codebase / can existing components be reused, (3) does a standard library

  cover it, (4) does a native platform feature cover it, (5) can an installed/installable

  dependency cover it, (6) can it be a one-line fix (call an existing function), (7) only

  then write minimal new code. This is a token-economy mechanism distinct from the KB''s

  brevity findings: code reuse and feature refusal, not terse output — same effectiveness,

  fewer lines, and the codebase gets more reusable over time. Vendor-claimed reductions

  (94%-class, lines/tokens/cost/time vs the Caveman skill) are Haiku-4.5-only; the one

  independent-ish replication (Chase AI) measured ~22% cost reduction on Fable 5 medium

  and better-than-claimed results on Opus 4.8.'
implementation_notes: 'P2: the ladder is model-independent prompt/skill content and a candidate rule for any

  engine surface that generates code (kb-maintenance scripts, app tools) — reuse-before-

  write also echoes the engine''s rule-11 abstraction discipline applied to code. Ponytail

  itself is a watched-libraries CANDIDATE (Nick-gated; vendor benchmarks + one

  independent-ish corroboration) — no registry entry written this session.'
category: Prompt Craft
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- IL (code-writing surfaces)
- General
adopted_in: []
sources:
- claude-code-cuts-token-usage-by-94-percent.md
- make-fable-5-80-percent-cheaper.md
related_findings:
- file: token-economics-as-architecture-driver.md
  rel: same-problem
- file: brevity-constraints-reverse-llm-performance.md
  rel: same-problem
- file: stupid-button-six-question-token-audit-diagnostic.md
  rel: same-problem
- file: surgical-change-constraint-agent-scope.md
  rel: same-problem
- file: measured-delta-and-staging-clone-for-ai-refactors.md
  rel: same-problem
- file: on-demand-vs-always-on-skill-activation.md
  rel: same-problem
proposals: null
date_discovered: '2026-07-12'
last_updated: '2026-07-12'
pipeline_status: synthesized
consumed_by:
- model-resilient-prompt-engineering.md
---

# Seven-Rung Minimal-Code Decision Ladder

## What It Is

An ordered pre-generation checklist the coding agent works through on every request: need
check (YAGNI), codebase reuse check (existing components — e.g., reuse the receipt-page
table for the transactions page instead of a new table), standard library, native platform
feature, installable dependency, one-line fix, and only at the bottom rung, new minimal
code. Shipped as the Ponytail Claude Code plugin with on-demand subcommands: `ultra`
(simplify an over-engineered codebase), `review` (trim before commit), `audit`
(repo-wide over-engineering scan — dead code, unused flags/configs, over-abstract
services/types, hand-rolled reimplementations of standard libraries,
single-implementation interfaces and factories), `debt` (defer consciously), `gain`
(measure the with/without delta), `off`.

## Why It Matters

It attacks token cost at the source that brevity skills miss: generated volume is mostly
*unnecessary code*, not verbose prose. Every rung climbed is 100% of that code's tokens
saved — at write time and again at every future read of the codebase — while also
countering the known agentic failure mode of reinventing what exists (the audit list is
effectively a taxonomy of AI over-engineering). Distinct from and composable with brevity
constraints and effort-level tuning.

## Why People Are Using It

Plugin adoption plus one cross-model replication: Chase AI measured ~22% cost reduction on
Fable 5 (medium effort) — better than the vendor's own Haiku claim — and improved
speed/token numbers on Opus 4.8. Demonstrated on a 200k-line, 1,000-file production
repo audit in the Eric Tech source.

## Potential Alternatives

Caveman (predecessor skill, same goal, weaker reported numbers); house style/lint rules
enforcing reuse (deterministic but can't judge need); the KB's surgical-change constraints
(scope-limiting rather than volume-limiting).

## Potential Failure Modes

YAGNI applied by an agent can silently drop genuinely needed scope — the "does it need
this?" judgment is delegated to the model. Aggressive reuse couples unrelated features to
shared components. Repo-wide simplification refactors carry real regression risk (see the
measured-delta/staging-clone finding — the source itself doesn't trust the audit output
unverified). Vendor benchmark numbers are single-model and self-reported; treat the 94%
headline as marketing until replicated.
