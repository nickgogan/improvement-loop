---
notion_id: 32b1e08b-9b34-8190-adcf-c234d720caec
name: 'SWECI Benchmark: AI Fails at Code Maintenance (75% Break Existing Features)'
summary: The SWECI benchmark (Alibaba) tests AI on maintaining real codebases over time (233-day average, 71 consecutive updates) — 75% of frontier models break previously working features during maintenance,
  revealing that writing code and maintaining code are fundamentally different skills.
implementation_notes: null
category: Evaluation
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
priority: P2
applicability:
- S3 (Claude Code Build)
adopted_in: []
sources:
- your-ai-agent-fails-975-of-real-work-the-fix-isnt.md
proposals: []
date_discovered: '2026-03-22'
last_updated: '2026-04-19'
related_findings:
- file: context-gap-task-vs-job.md
  rel: same-problem
- file: arc-agi-3-zero-percent-abstract-reasoning.md
  rel: same-problem
- file: cross-model-verification-for-bug-finding.md
  rel: same-problem
pipeline_status: raw
consumed_by: []
---
# SWECI Benchmark: AI Fails at Code Maintenance (75% Break Existing Features)

## What It Is
SWECI (team at Alibaba) is the first benchmark measuring AI performance on software maintenance rather than code generation. 100 real codebases, each with 233 days average history and 71 consecutive updates. The agent must evolve the codebase forward — adding features, fixing bugs, adapting to new requirements — the way real software development works over months. Key finding: 75% of frontier models break previously working features during maintenance. The benchmark specifically penalizes agents whose early decisions compound into technical debt. Almost all tested models accumulate technical debt.

## Why It Matters
Most AI coding benchmarks (SWE-bench) test single-session code generation. SWECI reveals that the 90%+ capabilities advertised for coding agents reflect generation performance, not maintenance performance. For production systems that must evolve over months, this gap is existential. The implication: AI-generated code may require human maintenance at high rates, offsetting automation gains.

## Why People Are Using It
Grounds the 'AI will replace software engineers' narrative with concrete measurement. Helps engineering leaders make informed decisions about which coding tasks to automate (greenfield generation: high confidence) vs. which to keep human-led (ongoing maintenance: low confidence).

## Potential Alternatives
Manual code review with AI assistance (human provides maintenance judgment, AI handles implementation), strict architecture constraints that limit AI decision scope, modular codebases with clear boundaries to limit blast radius of agent errors.

## Potential Improvements
Agent harnesses with explicit architectural memory (decisions log, ADR files) could reduce technical debt accumulation. Validation loops that run regression tests after each agent change would catch feature breakage early.

## Potential Failure Modes
Even with regression tests, architectural debt accumulates invisibly until a refactor is needed. Test coverage gaps mean some breakage goes undetected.
