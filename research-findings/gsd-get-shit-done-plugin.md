---
notion_id: 32b1e08b-9b34-816a-b1e2-d8c61423620b
name: GSD (Get Shit Done) Plugin
summary: Wave-based execution orchestration that spawns up to 15 subagents with fresh context per executor. Handles IB queues as batched waves with Nyquist validation between each wave.
implementation_notes: null
category: Orchestration
evidence_strength: Medium (practitioner-documented)
adoption_status: Partially Adopted
priority: P2
applicability:
- S3 (Claude Code Build)
adopted_in:
- S3 (Claude Code Build)
sources:
- these-3-frameworks-make-claude-code-unstoppable.md
- claude-code-works-better-when-you-do-this.md
proposals: null
date_discovered: '2026-03-15'
last_updated: '2026-04-19'
related_findings:
- file: planner-executor-deterministic-guardrails.md
  rel: enables
- file: archon-yaml-defined-harness-workflows.md
  rel: same-problem
pipeline_status: "synthesized"
consumed_by:
  - "agent-architecture-decisions.md"
---
# GSD (Get Shit Done) Plugin

## What It Is
GSD (Get Shit Done) is an orchestration plugin designed for processing large IB backlogs through wave-based subagent spawning. Each wave launches up to 15 parallel executors, each with a fresh context window. Between waves, a Nyquist validation step checks system state before the next wave begins — preventing compounding errors from cascading across waves.

## Why It Matters
Serial IB execution is the bottleneck in most build workflows. GSD reframes execution as a throughput problem: parallelize aggressively across a wave, validate between waves, then repeat. This is the breadth counterpart to deep single-item execution patterns like Ralph Wiggum.

## Why People Are Using It
S3's IB backlog frequently contains many independent items that don't need to be executed sequentially. GSD's wave model maps well to this structure. The reference file exists in the vault, indicating it has already been evaluated and staged for deployment in Phase 2.5 of the S3 migration.

### Context Window Accuracy Degradation (2026-04-07)

Practitioner-observed accuracy degradation curve for context window utilization:
- **0-20%** of context: High accuracy
- **40%**: Noticeable degradation begins
- **60-80%**: Significant hallucination risk, software bugs increase

This data supports GSD's sub-50% rule as a hard constraint rather than a guideline. A complementary **status line progress bar** tool displays real-time context window consumption in the Claude Code terminal, allowing developers to see exactly when the 50% threshold is approaching.

### Automatic Milestone Sizing (2026-04-07)

GSD calculates project size and determines milestone boundaries based on context budget, ensuring each milestone fits under 50% context utilization. This is not a guideline — GSD actively performs the calculation and sets milestone scope accordingly.

### MD-File State Persistence (2026-04-07)

GSD saves state inside markdown files on the local machine between orchestrator switches. The next orchestrator reads the state file to restore context and continue. This is a middle ground between JSON session persistence (crash recovery) and PROGRESS.md (human-readable session bridge) — structured enough for machine consumption, readable enough for human inspection.

## Potential Improvements
Wave sizing (currently up to 15 agents) could be tuned dynamically to Notion API rate limits rather than set as a fixed ceiling. An adaptive wave governor that monitors MCP connection health and throttles accordingly would make the system more robust under load.

## Potential Failure Modes
Spawning too many parallel agents simultaneously can overwhelm MCP connections, causing tool call failures that cascade into partial or incorrect IB completions. Without tight Nyquist validation criteria, waves can proceed on a corrupted state, amplifying errors rather than containing them.
