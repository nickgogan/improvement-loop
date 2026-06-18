---
name: "Context Degradation at 40-50% Utilization Threshold"
summary: "Practitioner-observed: Claude enters 'completion mode' (rushing, cutting corners, losing plan fidelity) at ~40-50% context utilization — not at the 80% technical limit. The model sees context mounting and begins degrading before actual capacity pressure. Actionable response: limit plans to 2-3 tasks max, use fresh context sessions per phase, and treat 40% as the effective ceiling for quality work."
implementation_notes: "MetaSystem's GSD system dispatches phases to subagents, which partially mitigates this. But the main orchestrator session can still accumulate context. The 40-50% threshold suggests more aggressive context hygiene — compact or dispatch earlier than current heuristics assume."
category: "Context Engineering"
evidence_strength: "Anecdotal"
adoption_status: "Not Yet Started"
priority: "P2 (Design Required)"
applicability:
  - "S3 (Claude Code Build)"
adopted_in: []
sources:
  - "taches-claude-code-resources-commands-skills-thinki.md"
  - "claude-code-hidden-settings-aiabs.md"
  - "gstack-gsd-superpowers-orchestrator-headless.md"
proposals: null
date_discovered: "2026-05-24"
last_updated: "2026-05-25"
related_findings:
  - file: "context-rot-attention-budget-depletion.md"
    rel: "extends"
  - file: "proactive-compaction-before-intelligence-degradation.md"
    rel: "same-problem"
  - file: "orchestrator-headless-dispatch-context-isolation.md"
    rel: "same-problem"
pipeline_status: "extracted"
consumed_by:
  - "rules/context-degradation-40-percent-threshold.md"
tags:
  - "context-engineering"
  - "claude-code"
---

# Context Degradation at 40-50% Utilization Threshold

## What It Is

A practitioner-documented observation: Claude enters "completion mode" — rushing responses, cutting corners, losing plan fidelity — at approximately 40-50% context window utilization, well before the technical 80% limit. The degradation is triggered by the model perceiving context mounting, not by actual capacity exhaustion.

## Why It Matters

If the effective quality ceiling is 40-50% rather than 80%, plans and phases must be scoped smaller than current assumptions. The actionable response: limit plans to 2-3 tasks max, dispatch work to fresh context sessions aggressively, and treat 40% as the planning ceiling. This also validates the orchestrator-delegates-to-headless pattern — fresh context per phase isn't just nice-to-have, it's necessary for quality.

## How It Could Fail

The threshold is a single practitioner's observation without controlled measurement. Context degradation may be task-dependent (complex reasoning degrades earlier; simple file edits tolerate higher utilization). Model improvements may shift the threshold upward.

## Extraction Note — 2026-05-24
Extracted as **rule**: [[context-degradation-40-percent-threshold]] in `extracts/rules/`
