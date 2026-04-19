---
notion_id: 32b1e08b-9b34-81d8-9480-f2bd7bf03667
name: 'March of Nines: Compounding Reliability Math for Multi-Step Agents'
summary: Karpathy's reliability framework shows that each additional 9 of reliability in an agentic workflow requires comparable engineering effort to achieve, and multi-step workflows compound step-level
  failure rates -- making even 90% per-step reliability produce multiple daily failures at 10 steps.
implementation_notes: null
category: Evaluation
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
proposer_priority: null
applicability:
- S3 (Claude Code Build)
adopted_in: []
sources:
- andrej-karpathys-math-proves-agent-skills-will-fai.md
proposals: []
date_discovered: '2026-03-22'
last_updated: '2026-04-08'
related_findings:
- file: specialized-harness-engineering-deterministic-rail.md
  rel: enables
- file: prompt-only-tool-use-ceiling.md
  rel: same-problem
pipeline_status: "raw"
consumed_by: []
---
# March of Nines: Compounding Reliability Math for Multi-Step Agents

## What It Is
The 'march of nines' framework: 90% per-step reliability on a 10-step workflow = 0.9^10 ≈ 35% overall success rate = ~6.5 failures per 10 attempts. 99% per-step = 0.99^10 ≈ 90% overall = ~1 failure per 10. 99.9% per-step = 0.999^10 ≈ 99% overall = ~1 failure per 100. Each '9' of improvement requires engineering effort comparable to achieving the previous level. This mathematically proves that prompt-only approaches (skills/instructions) cannot reach enterprise-grade reliability because they cannot guarantee per-step success rates -- they only improve average-case performance.
## Why It Matters
Provides a mathematical framework for product/engineering conversations about AI reliability. Moves the discussion from 'is the AI good enough' to 'what reliability does the use case require' and 'what engineering investment achieves that reliability'. The compounding effect means that for workflows longer than 5 steps, even small per-step reliability gaps create unacceptable overall failure rates.
## Why People Are Using It
Grounds reliability conversations in math rather than subjective impression. Provides a principled argument for investing in harness engineering rather than prompt tuning alone. The SkillsBench evaluation (84 popular skills tested) confirms that skills improve performance but fall 'well shy of what a business would need to reliably use at scale.'
## Potential Alternatives
Human-in-the-loop at each step (guarantees reliability but eliminates automation benefit), deterministic code for all steps except LLM calls (eliminates compounding for non-LLM steps), shorter workflows with fewer steps.
## Potential Improvements
Workflow design optimization: minimize steps, parallelize independent steps, identify which steps have highest failure probability and add targeted validation at those points. Reliability monitoring: track per-step success rates in production to identify which steps need improvement.
## Potential Failure Modes
Reliability math assumes independent step failures; in practice, early failures often cause correlated downstream failures (one wrong assumption propagates). Human-in-the-loop steps break the compounding math but add latency.
