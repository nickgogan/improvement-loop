---
name: Capability vs Regression Eval Suite Lifecycle
summary: Organize evals into capability suites (measuring new abilities, starting at low pass rates) and regression suites (maintaining near-100% to catch backsliding). Capability evals graduate to regression
  as they saturate.
implementation_notes: 'MetaSystem has no formal eval suites yet. When building, design the lifecycle from the start: capability evals for new features, graduation threshold, regression monitoring.'
category: Evaluation
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
proposer_priority: P2 (Design Required)
applicability:
- S3 (Claude Code Build)
- General / Cross-System
adopted_in: []
sources:
- anthropic-demystifying-evals-for-ai-agents.md
related_findings: []
proposals: null
date_discovered: '2026-04-09'
last_updated: '2026-04-09'
pipeline_status: synthesized
consumed_by:
- building-agent-evaluation-suites.md
---

## What It Is

Capability evals target areas where the agent currently struggles — pass rates start low and climb with improvement. Regression evals lock in known-good behaviors at near-100% pass rates. When a capability eval hits 100%, it graduates to the regression suite and new, harder evals replace it.

## Why It Matters

Without this separation, teams conflate improvement signal with stability signal. Saturated capability evals make progress appear artificially slow. Unmaintained regression suites let previously-working features silently degrade.

## Why People Are Using It

SWE-Bench Verified went from ~40% to >80% in one year, now approaching saturation. Qodo found one-shot evals masked substantial progress on longer agentic tasks.

## Potential Improvements

Automated graduation criteria based on consecutive pass rate thresholds. Difficulty scaling that generates harder variants automatically.

## Potential Failure Modes

Over-graduating — moving evals to regression too early based on a few good runs rather than sustained performance. Under-investing in new capability evals once regression suite grows large.
