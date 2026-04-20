---
name: Oracle + Delta Debugging for Parallelizing Monolithic Tasks
summary: When a single giant task (e.g., kernel compilation) prevents parallelism, randomly compile most files with a known-good oracle (GCC), remainder with the agent's output. Failures isolate bugs to
  the agent's subset. Delta debugging then finds interacting file pairs that fail together but pass independently.
implementation_notes: null
category: Evaluation
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
priority: P3 (Monitor)
applicability:
- S3 (Claude Code Build)
adopted_in: []
sources:
- anthropic-building-c-compiler.md
related_findings: []
proposals: null
date_discovered: '2026-04-09'
last_updated: '2026-04-09'
pipeline_status: raw
consumed_by: []
---

## What It Is

A technique for parallelizing work on monolithic integration tasks that would otherwise serialize all agents. In the C compiler project, Linux kernel compilation was a single giant task where all agents would duplicate work on the same bugs, nullifying parallelism. The solution: randomly compile most kernel files with known-good GCC, compile the remainder with the agent's (Claude's) compiler. If the build succeeds, the bug is not in Claude's file subset. If it fails, refine by recompiling subsets with GCC to isolate the problematic files. Follow with delta debugging to find interacting file pairs that fail together but pass independently.

## Why It Matters

Monolithic integration tasks are the anti-pattern for parallel agent systems. Without a decomposition strategy, all agents converge on the same problem and produce duplicate work. The oracle approach converts a monolithic task into independently addressable chunks by using a known-good implementation as a reference baseline.

## Why People Are Using It

Anthropic developed this for the C compiler project where kernel compilation was the key parallelism bottleneck. The pattern is general: any task where a reference implementation exists can use it as an oracle to isolate agent-specific bugs.

## Potential Improvements

Automated oracle selection based on task type. Intelligent partitioning (rather than random) based on change history or dependency analysis.

## Potential Failure Modes

Requires a known-good oracle -- not always available. Random partitioning may miss systematic issues. Delta debugging is O(n^2) in the worst case for interacting pairs.
