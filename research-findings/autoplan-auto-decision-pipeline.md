---
name: Autoplan Auto-Decision Pipeline
summary: 'Chains CEO, design, eng, and devex reviews with 6 auto-decision principles. Auto-resolves clear findings (obvious fixes, standard patterns). Surfaces only ''taste decisions'' at the human gate:
  close approaches, borderline scope calls, and Codex disagreements.'
implementation_notes: null
category: Orchestration
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- S3 (Claude Code Build)
adopted_in: []
sources:
- gstack-planning-multi-persona-spec-review.md
related_findings:
- file: gstack-office-hours-socratic-discovery-pipeline.md
  rel: feeds-into
- file: gstack-spec-team-parallel-research-agents.md
  rel: feeds-into
- file: planning-session-bias-separate-context-windows.md
  rel: same-problem
- file: agui-human-control-layer-not-ui.md
  rel: same-problem
proposals: null
date_discovered: '2026-04-08'
last_updated: '2026-05-24'
pipeline_status: "classified"
consumed_by: []
---

# Autoplan Auto-Decision Pipeline

## What It Is
gstack's `/autoplan` chains CEO, design, engineering, and devex reviews with 6 auto-decision principles for resolving review findings automatically. Clear findings (obvious fixes, standard patterns) are auto-resolved without human involvement. Only "taste decisions" surface at the final human gate: close approaches where either option is valid, borderline scope calls, and Codex disagreements (when a second AI opinion differs from the first). This creates a filtered review experience where the human sees only the decisions that require aesthetic judgment.

## Why It Matters
Most review systems present all findings to the human, causing review fatigue and decision overload. Autoplan filters the signal: only taste decisions — where human aesthetic judgment genuinely matters — reach the gate. This reduces review fatigue while preserving human authority over subjective calls. The distinction between automatable decisions and taste decisions is a useful classification for any human-in-the-loop system.

## Why People Are Using It
Observed in [gstack](https://github.com/garrytan/gstack) v0.15.16.0 — see [[gstack-analysis]] for structural details. Balances automation with human judgment. Most review systems present all findings to the human. Autoplan filters: only taste decisions (where human aesthetic judgment matters) reach the gate. This reduces review fatigue while preserving human authority over subjective calls.

## Potential Alternatives
Full human review of all findings. Severity-based filtering (only show high-severity). Confidence-based filtering (only show low-confidence findings). No review pipeline — trust the implementation directly.

## Potential Improvements
Learning from human gate decisions to improve auto-resolution over time. Configurable auto-decision thresholds per project. Audit trail of auto-resolved decisions for periodic human spot-checks.

## Potential Failure Modes
Auto-resolution of findings that were actually taste decisions (false confidence). Codex disagreements being noisy rather than signal-bearing. Review pipeline overhead for small changes that don't warrant multi-role review. Human gate atrophy if most decisions are auto-resolved and the human rubber-stamps the remainder.

## Update — 2026-04-20
Live demonstration on BookZero (brownfield SaaS) clarifies the mechanics and scale. The sequential review chain runs CEO → Design → Engineering, each as a dedicated sub-agent. Observed output: 41 total findings (10 from CEO, 15 from Design, 16 from Engineering), 22 auto-decisions made, plus a small number of flagged human decisions. Token cost for the auto-plan phase: ~200k. The pattern runs on a spec file (markdown in the backlog directory) produced by the spec-team phase — not on code. This distinguishes it from the review-army pattern (which reviews diffs): autoplan reviews a spec document before any implementation begins. The three-role sequential chain (CEO → Design → Eng) maps cleanly to GStack's specialist role architecture, with each sub-agent operating with role blinders per the 5-layer governance system.
