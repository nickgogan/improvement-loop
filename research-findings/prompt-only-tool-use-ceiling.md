---
name: Prompt-Only Tool Use Has a Hard Ceiling
summary: ARTIST demonstrates that prompting base models to use tools yields 3-14% lower accuracy than RL-trained tool policies across all benchmarks. Supervised fine-tuning on tool-use trajectories also
  underperforms outcome-based RL by ~25%. This establishes that prompt engineering alone cannot produce robust tool coordination.
implementation_notes: 'We rely entirely on prompt-based tool use. This finding does not mean our approach is wrong -- we consume models, not train them -- but it sets expectations: prompt-based tool selection
  will always be less reliable than what RL-trained models could achieve. Design compensating controls: verification steps, retry logic, tool output validation.'
category: Tool Integration
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
proposer_priority: P3 (Monitor)
applicability:
- General
adopted_in: []
sources:
- artist-agentic-reasoning-and-tool-integration-via.md
related_findings:
- file: rl-trained-autonomous-tool-selection-artist-pattern.md
  rel: enables
- file: emergent-agentic-behaviors-from-outcome-rl.md
  rel: same-problem
- file: loss-masking-deterministic-tool-outputs.md
  rel: same-problem
- file: agent-architecture-layer-impermanence.md
  rel: same-problem
- file: march-of-nines-compounding-reliability-math-for-m.md
  rel: same-problem
proposals: []
date_discovered: '2026-04-07'
last_updated: '2026-04-08'
pipeline_status: "raw"
consumed_by: []
---
# Prompt-Only Tool Use Has a Hard Ceiling

## What It Is
A comparative finding from ARTIST research: Base-Prompt+Tools (prompting a model to use tools without RL training) consistently underperforms ARTIST by 3-14% across all benchmarks. Open-source supervised tool-augmented models (ToRA, PAL, NuminaMath) average 25.7% lower accuracy than ARTIST across math benchmarks.

The hierarchy is clear: **RL-trained tool policies > supervised tool fine-tuning > prompt-based tool selection**.

## Why It Matters
Most production agentic systems -- including ours -- rely on prompt-based tool selection. This finding quantifies the gap between what prompting can achieve and what RL training enables. It explains why multi-step agentic workflows hit reliability ceilings that no amount of prompt tuning can fix (connecting to the "march of nines" compounding reliability math).

## Why People Are Using It
ARTIST benchmarks provide the first controlled comparison between prompt-based, supervised, and RL-trained tool use on identical tasks. The 3-14% gap on complex tasks and 25.7% gap vs. supervised approaches are statistically significant across multiple benchmarks.

## Potential Improvements
As model providers ship RL-trained tool use natively (rather than requiring custom training), the gap may close for consumers. Monitor frontier model releases for native tool-use RL training announcements.

## Potential Failure Modes
The gap may be smaller or larger depending on tool complexity and domain. Simple tool calls (file read, web fetch) may not benefit much from RL training, while complex multi-turn tool chains benefit significantly.
