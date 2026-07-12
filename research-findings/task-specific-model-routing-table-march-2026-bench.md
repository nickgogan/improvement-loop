---
notion_id: 3351e08b-9b34-81f5-9dcf-fc527630b039
name: Task-Specific Model Routing Table (March 2026 Benchmark Consensus)
summary: 'Emerging consensus across multiple March 2026 benchmarks on task-to-model routing: Claude Sonnet 4.6 for repository-level coding and knowledge work; GPT-5.4 for computer-use/orchestration/browser
  tasks; Gemini 3.1 Pro for long-horizon abstract reasoning; Gemini Flash for extraction/transformation batch tasks at cost floor. Opus 4.6 costs 3.5x Sonnet with no accuracy premium.'
implementation_notes: 'The KB has no current model selection guidance. March 2026 model releases create wide enough gaps to warrant structured routing. Opus by default is a documented cost mistake (3.5x
  cost, no quality gain). Multiple independent benchmarks converge on same routing tiers. Sources: https://www.lorka.ai/knowledge-hub/gemini-vs-chatgpt-vs-claude / https://ianlpaterson.com/blog/llm-benchmark-2026-38-actual-tasks-15-models-for-2-29/'
category: Model Selection
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
priority: P1 (Implement Now)
applicability:
- S3 (Claude Code Build)
adopted_in: []
sources:
- llm-benchmark-2026-38-actual-tasks-ian-l-paterson.md
- gemini-vs-gpt-vs-claude-benchmark-comparison-lorka.md
related_findings:
- file: arc-agi-3-zero-percent-abstract-reasoning.md
  rel: enabled-by
- file: frontier-release-compression-march-2026.md
  rel: same-problem
- file: open-source-model-parity-mistral-small-4.md
  rel: enabled-by
- file: advisor-executor-api-pattern.md
  rel: same-problem
- file: auxiliary-model-slot-architecture.md
  rel: same-problem
- file: claude-5-family-retiers-claude-line.md
  rel: extended-by
- file: deepseek-v4-frontier-parity-mit-license.md
  rel: extended-by
- file: qwen-bfcl-tool-calling-leadership-efficient-coding.md
  rel: extended-by
- file: kimi-k2-line-near-opus-coding-with-safety-gap.md
  rel: extended-by
- file: center-vs-edge-of-distribution-task-classification.md
  rel: enabled-by
- file: data-normalization-as-cheap-model-enabler.md
  rel: same-problem
- file: effort-level-tuning-as-first-order-cost-lever.md
  rel: same-problem
- file: prototype-at-frontier-then-downshift.md
  rel: enabled-by
proposals: []
date_discovered: '2026-04-01'
last_updated: '2026-07-12'
pipeline_status: synthesized
consumed_by:
- agent-architecture-decisions.md
- model-resilient-prompt-engineering.md
---
# Task-Specific Model Routing Table (March 2026 Benchmark Consensus)

## What It Is
A four-tier task routing table derived from converging March 2026 benchmark data:

| Task Type | Recommended Model | Key Evidence |
|---|---|---|
| Repository-level coding, knowledge work | Claude Sonnet 4.6 | GDPval Elo 1633, SWE-bench ~79.6% |
| Computer use, orchestration, browser automation | GPT-5.4 | WebArena-Verified 67.3% |
| Abstract reasoning, long-horizon math | Gemini 3.1 Pro | ARC-AGI-2 77.1% |
| Extraction/transformation, batch processing | Gemini Flash | $0.003 per task, 97.1% quality |

**Key cost finding:** Opus 4.6 costs 3.5x Sonnet 4.6 with no accuracy premium.

## Why It Matters
Benchmark divergence between models is now wide enough that routing by task type yields material quality gains.

## Why People Are Using It
Multiple independent benchmarks converge on the same routing tiers.

## Potential Failure Modes
Benchmarks are snapshots. Task classification requires its own routing model or rules. ARC-AGI-3 finding (all models score 0%) is a ceiling reminder.

## Extraction Note — 2026-04-19
Extracted as **pattern**: [[task-specific-model-routing-table.md]] in `extracts/patterns/`
