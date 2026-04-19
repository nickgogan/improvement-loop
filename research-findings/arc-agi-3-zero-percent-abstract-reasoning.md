---
name: 'ARC-AGI-3: All Frontier Models Score 0% on Abstract Reasoning'
summary: ARC-AGI-3 benchmark results show GPT-5.4, Claude Opus 4.6, and Gemini 3.1 all scoring 0% on novel abstract reasoning tasks, while untrained humans score 100%. The benchmark is specifically designed
  to defeat extended chain-of-thought reasoning and brute-force search. This quantifies a fundamental gap between current model capabilities and genuine abstract reasoning.
implementation_notes: This is a ceiling reminder for any agent design that assumes models can generalize to truly novel patterns. Our agent workflows should not rely on the model inventing novel abstractions
  -- they should provide explicit patterns, templates, and examples. Design for pattern-matching strength, not for general reasoning.
category: Evaluation
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
proposer_priority: P2 (Design Required)
applicability:
- General
adopted_in: []
sources:
- arc-agi-3-gpt-54-claude-opus-46-gemini-31-all-scor.md
related_findings:
- file: benchmark-signal-mismatch-optimization-gap.md
  rel: enables
- file: cot-fails-without-inductive-generalization.md
  rel: enables
- file: sweci-benchmark-ai-fails-at-code-maintenance.md
  rel: same-problem
- file: task-specific-model-routing-table-march-2026-bench.md
  rel: enables
proposals: []
date_discovered: '2026-04-07'
last_updated: '2026-04-08'
pipeline_status: synthesized
consumed_by:
- building-agent-evaluation-suites.md
---
# ARC-AGI-3: All Frontier Models Score 0% on Abstract Reasoning

## What It Is
ARC-AGI-3 presents visual grid puzzles where solvers must infer underlying rules from 2-5 input-output examples and apply them to new inputs. Tasks require identifying compositional patterns (e.g., "the blue cluster mirrors itself horizontally while the red pattern scales proportionally"). Version 3 is specifically designed to defeat:
- Extended chain-of-thought reasoning
- Brute-force search methods
- Synthetic data generation approaches (which defeated v2)

Results: GPT-5.4 (0%), Claude Opus 4.6 (0%), Gemini 3.1 (0%). Ordinary humans with no special training: 100%, typically solving each puzzle in under two minutes.

## Why It Matters
A model scoring 90% on the bar exam and 0% on ARC-AGI-3 is a "capable specialist" not a "general reasoner." This distinction is critical for agent system design: current models excel at pattern-matching against training data but cannot perform few-shot causal generalization to truly novel patterns. Any agent design that assumes general reasoning capability will fail on tasks outside the model's training distribution.

## Why People Are Using It
ARC-AGI is the primary benchmark for measuring progress toward genuine abstract reasoning (as distinct from training-set interpolation). The 0% result across all frontier models provides a clear, unambiguous signal that the gap between specialist and generalist capability remains total.

## Potential Improvements
The benchmark itself is well-designed. The improvement opportunity is in agent architecture: designing workflows that compensate for this limitation by providing explicit pattern libraries, decomposing novel problems into familiar sub-problems, and routing genuinely novel reasoning to human judgment.

## Potential Failure Modes
ARC-AGI measures a specific kind of abstract reasoning (visual grid patterns). Models may have abstract reasoning capabilities that this benchmark does not measure. Overreacting to 0% by dismissing model reasoning capabilities entirely would be a mistake -- they remain strong on trained-distribution tasks.
