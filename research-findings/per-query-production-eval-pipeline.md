---
name: "Per-Query Production Eval Pipeline"
summary: "Every single production query from a user runs through a comprehensive eval suite inline, not just during development or periodic audits. This continuous per-request evaluation identifies which domains and action types agents handle well versus poorly, enabling targeted improvement rather than blanket tuning."
implementation_notes: null
category: "Evaluation"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: P2
applicability:
  - "S3 (Claude Code Build)"
  - "General"
adopted_in: []
sources:
  - "problem-with-ai-agents-utori-compound-errors.md"
related_findings:
  - file: "four-layer-production-eval-stack-with-golden-traces.md"
    rel: "extends"
  - file: "eval-driven-development-autonomous-quality.md"
    rel: "extends"
  - file: "agent-self-reporting-unreliability-independent-eval.md"
    rel: "same-problem"
  - file: "march-of-nines-compounding-reliability-math-for-m.md"
    rel: "same-problem"
proposals: null
date_discovered: "2026-05-25"
last_updated: "2026-05-25"
tags:
  - "session-95-reextract"
pipeline_status: synthesized
consumed_by:
  - verifying-agent-output.md
---

# Per-Query Production Eval Pipeline

## What It Is

A production architecture where every user query that an agent processes is simultaneously evaluated by a comprehensive eval suite running inline. Not sampled, not periodic -- every single request. The eval output identifies which agents are performing well versus poorly, which domains need more work, and surfaces failure patterns in real time.

Abhishek Das describes Utori's approach: "Every single production query that a user runs goes through a fairly comprehensive set of evals that lets us quickly identify where these agents are doing well versus not, which domains need more work, and so on."

This is distinct from development-time eval-driven development (which tests before shipping) and the four-layer production eval stack (which describes the architecture). This is the operational discipline of running eval on 100% of production traffic, not a statistical sample.

## Why It Matters

Sampling-based evaluation misses rare but catastrophic failures. Long-tail domains and edge cases only surface at scale. Per-query eval provides a complete picture of agent behavior across the full distribution of real user requests, not just the curated test set.

For MetaSystem's skills, this suggests: every skill invocation should produce machine-readable quality signals (not just human-visible output) that can be aggregated to reveal which skills and which domains are underperforming. Currently, skill quality is assessed by Nick's ad-hoc review -- there is no systematic per-invocation quality signal.

## Why People Are Using It

Utori operates in the web agent space where the domain surface is unbounded (any website). They cannot anticipate all failure modes in advance. Per-query eval is their mechanism for discovering failure modes as they appear in real traffic and feeding that signal back into model improvement.

## Potential Improvements

Layered eval cost management: run cheap syntactic/structural checks on every query and expensive LLM-as-judge evals on a confidence-gated subset. Eval result feedback loop: automatically route low-scoring queries into retraining pipelines or human review queues.

## Potential Failure Modes

Eval overhead adds latency to every request. Eval criteria that don't correlate with actual user satisfaction create misleading quality signals. Alert fatigue if the eval surfaces too many low-confidence warnings.
