---
name: "Anthropic First-Party Capability-Trend Stats (mid-2026)"
summary: |-
  Why it matters for us: these are the dated, first-party numbers behind "profiles age
  fast" — they quantify how quickly any model-capability claim in our registry goes stale
  and set the baseline for what frontier lab-internal agent throughput looks like.
  Anthropic reports task-horizon doubling roughly every 4 months (previously ~7): ~4-minute
  autonomous tasks (Claude 3 Opus, Mar 2024) → ~90-minute (3.7 Sonnet, Mar 2025) → ~12-hour
  (Opus 4.6, Mar 2026). Operationally: >80% of Anthropic's merged code Claude-authored as of
  May 2026; typical engineer merging 8× as much code per day in Q2 2026 vs 2024; ~52×
  speedup on code-optimization research tasks (Mythos Preview, Apr 2026) vs ~3× (Opus 4,
  May 2025); 76% success on open-ended problems May 2026 (+50pp in six months).
implementation_notes: null
category: "Model Selection"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: "P3 (Monitor)"
applicability:
  - "General"
adopted_in: []
sources:
  - "anthropic-when-ai-builds-itself-rsi-essay.md"
related_findings:
  - file: "frontier-release-compression-march-2026.md"
    rel: "same-problem"
proposals: null
date_discovered: "2026-07-11"
last_updated: "2026-07-11"
---

## What It Is

A cluster of first-party capability-trend statistics from Anthropic's "When AI Builds
Itself" essay (recursive-self-improvement strategy piece), intaken narrowly as registry
citation material: task-horizon doubling every ~4 months (accelerated from ~7); the
Opus-line trajectory from ~4-minute autonomous tasks (Mar 2024) to ~12-hour tasks
(Mar 2026); >80% Claude-authored merged code at Anthropic (May 2026, from low single
digits before Claude Code's Feb 2025 preview); 8× per-engineer merged-code throughput
(Q2 2026 vs 2024); ~52× code-optimization research speedup (Mythos Preview, Apr 2026);
76% open-ended task success (May 2026, +50pp in six months).

## Why It Matters

The model-capability registry treats undated claims as wrong claims waiting to happen.
These numbers put a first-party doubling clock on that: a capability profile written today
describes a model whose autonomous task horizon doubles in ~4 months. They also anchor
what "AI-authored codebase" means at the frontier lab operating the harness we run on —
relevant context for calibrating our own autonomy expectations and for the agentic-OS
direction's assumption that harnessed agents carry most execution.

## Why People Are Using It

The task-horizon doubling framing (originating in METR's measurements, here confirmed
first-party with an accelerated rate) has become the standard capability-forecast axis in
2026 planning discussions; Anthropic's essay is the first time the lab published its own
internal code-authorship and throughput ratios at this specificity.

## Potential Improvements

Cross-check the doubling rate against METR's independent measurements at next D2 refresh;
watch for the same stats refreshed in later Anthropic publications (the essay is undated
prose — the individual stats carry their own as-of dates, which is what makes them
citable).

## Potential Failure Modes

Self-reported, unaudited, and selection-prone: "merged code Claude-authored" says nothing
about review burden or defect rates; the 52× research-task speedup is a narrow task class;
extrapolating the 4-month doubling linearly ignores that the rate itself changed once
already (7→4 months) and could change again in either direction. Treat as trend context,
never as a routing input.
