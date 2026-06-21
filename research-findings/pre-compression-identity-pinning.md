---
name: Pre-Compression Identity Pinning (Soul.md Survives Compaction)
summary: When the token buffer nears capacity, compression aggressively drops early chat history. SOUL.md is structurally pinned at the top of context and survives compression. The token tax of re-injecting
  core identity files is "the only mechanical method to guarantee an autonomous agent survives context compaction."
implementation_notes: MetaSystem's compaction currently has no pinning guarantee for CLAUDE.md or constitution.md. Investigate whether Claude Code's compaction can be configured to preserve specific files.
category: Agent Design
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources:
- openclaw-soul-md-explained.md
proposals: []
date_discovered: '2026-04-07'
last_updated: '2026-04-07'
related_findings:
- file: context-file-taxonomy-claudemd-soulmd-agentsmd.md
  rel: enabled-by
pipeline_status: "synthesized"
consumed_by:
  - "agent-design-patterns.md"
  - "rules/pre-compression-identity-pinning.md"
---
# Pre-Compression Identity Pinning (Soul.md Survives Compaction)

## What It Is
A structural technique where the agent's identity file (SOUL.md in OpenClaw's terminology) is pinned at the top of the context window and explicitly preserved during compression. Unlike Claude Code's built-in compaction (which is lossy with no file pinning), OpenClaw uses a forced disk-read at session start (4-10K token cost) and structural pinning during compression. The identity file is always the first thing in context.

## Why It Matters
Context compaction is inherently lossy. Without explicit pinning, core identity, boundaries, and rules can be silently dropped during long sessions. This is especially dangerous for autonomous agents where behavioral drift can lead to safety violations or off-task execution.

## Why People Are Using It
OpenClaw demonstrates that structural pinning ensures personality, boundaries, and core rules persist even in very long sessions. The technique is mechanical and deterministic -- it does not rely on the model "remembering" to preserve important context.

## Potential Improvements
MetaSystem could implement pinning for CLAUDE.md and constitution.md during compaction. This would require understanding Claude Code's compaction mechanism and whether it supports user-specified preservation rules.

## Potential Failure Modes
The 4-10K upfront token cost is significant for short sessions -- only worthwhile for agents that run extended conversations. Over-pinning (too many files marked as preserved) would reduce the effective context window for actual work.

## Extraction Note — 2026-04-19
Extracted as **rule**: [[pre-compression-identity-pinning]] in `extracts/rules/`
