---
name: Agent Proof-of-Work UI Builds User Trust for Invisible Steps
summary: An agent that surfaces which sources it visited, what it examined, and what reasoning led to its output builds user trust in the parts of the system they cannot directly inspect. Utori's Scouts
  product includes a UI button that exposes the full agent trace alongside final reports. Framed as trust-building mechanism, not a debugging tool.
implementation_notes: MetaSystem's governance agents could expose their traversal path (which DDs they read, which findings they loaded) to reduce Nick's need to manually audit agent outputs. The existing
  delta report pattern partially serves this function but is session-scoped, not per-action.
category: Evaluation
evidence_strength: "Medium (practitioner-documented)"
adoption_status: Not Yet Started
priority: P3 (Monitor)
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources:
- problem-with-ai-agents-utori-compound-errors.md
proposals: null
date_discovered: '2026-05-24'
last_updated: '2026-05-25'
related_findings:
- file: chain-of-thought-reasoning-output-divergence.md
  rel: same-problem
- file: interpretive-boundary-layer-fact-vs-judgment.md
  rel: same-problem
- file: reviewer-skill-elevation-for-agentic-output.md
  rel: same-problem
- file: test-driven-development-as-counterweight-to-agenti.md
  rel: same-problem
- file: tool-shaped-object-evaluation-lens.md
  rel: same-problem
- file: trust-calibration-progressive-autonomy-ramp.md
  rel: same-problem
- file: visible-quality-as-trust-proxy-for-invisible-work.md
  rel: same-problem
pipeline_status: raw
tags:
- evaluation
- governance
- transparency
---

# Agent Proof-of-Work UI Builds User Trust for Invisible Steps

## What It Is

A design principle: agents that show their work — surfacing traversal paths, sources examined, and reasoning chains — build user trust in the parts of the system they cannot directly inspect. Utori implements this as an "inspect" button exposing the full agent trace alongside the final report.

## Why It Matters

When users can verify that attention to detail exists in visible parts of the product, they extend trust to invisible parts. Grad-CAM (30,000 citations) is an earlier manifestation — showing what the model attended to, not just the answer. For agent systems where most work happens invisibly, proof-of-work is a trust primitive, not a debugging feature.

## How It Could Fail

Exposing full agent traces can overwhelm users with irrelevant detail. The design challenge is selecting which trace elements to surface. Also, a well-formatted trace on a wrong answer can create false confidence.
