---
name: Token Waste Taxonomy and Two-Mode Workflow (Gather vs Focus)
summary: Identifies five token waste patterns from ChatGPT habits (raw PDF ingestion, conversation sprawl, plugin overhead, model mixing, accumulated junk) and prescribes a two-mode workflow — Gather mode
  for short info-collection threads, Focus mode for synthesized execution — to cut costs 10x.
implementation_notes: MetaSystem already uses session boundaries but lacks explicit gather/focus mode separation. PDF pre-processing and plugin auditing are directly actionable.
category: Context Engineering
evidence_strength: Strong (production-tested)
adoption_status: Partially Adopted
priority: P1 (Implement Now)
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources:
- your-claude-limit-burns-in-90-minutes.md
proposals: null
date_discovered: '2026-04-07'
last_updated: 2026-04-08
related_findings:
- file: ace-delta-updates-over-monolithic-rewrites.md
  rel: same-problem
- file: agent-context-kiss-commandments-minimum-viable.md
  rel: same-problem
pipeline_status: raw
consumed_by: []
---

# Token Waste Taxonomy and Two-Mode Workflow (Gather vs Focus)

## What It Is
Five waste patterns identified from ChatGPT habits applied to Claude: (1) raw PDF ingestion (100K tokens vs 5K pre-processed), (2) 30+ turn conversation sprawl, (3) 66K token plugin overhead per session, (4) unnecessary model switching, (5) accumulated context junk. The fix is a two-mode separation: Gather mode uses short, disposable threads for information collection; Focus mode starts fresh with pre-processed, synthesized context for execution.

Specific cost breakdown: a sloppy session runs 800K-1M input + 150-200K output tokens = $8-10; a clean session runs 100-150K input + 50-80K output tokens = ~$1. Fresh conversation cadence heuristic: start a new conversation every 10-15 turns. Use the `/context` command in Claude Code to audit loaded context and identify waste. The "Stupid Button" is a 6-question token waste self-audit diagnostic for rapid assessment. Plugin audit discipline: periodically drop plugins that were enabled months ago but never used — dead plugins still consume token budget every session.

## Why It Matters
Subscription users burn daily limits in 90 minutes. Optimized users who apply the two-mode workflow "forget limits exist." The waste patterns compound — a single session with raw PDFs, active plugins, and 30+ turns can consume 10x what a disciplined session requires.

## Why People Are Using It
Nate B Jones documents 10x cost reduction from applying these patterns. Maps directly to usage-based pricing models where waste compounds financially. The gather/focus separation aligns with how expert practitioners naturally work — research and execution are distinct cognitive modes.

## Potential Alternatives
Single-session workflows with aggressive context pruning. Automated context summarization between turns. Plugin-free workflows using CLI tools instead.

## Potential Improvements
Automated mode detection — the system could recognize when a user is gathering vs. focusing and adjust context strategy accordingly. Context budget dashboards showing real-time token consumption per source.

## Potential Failure Modes
Over-separation loses cross-thread insights — sometimes gather and focus benefit from sharing context. Pre-processing PDFs may strip formatting, tables, or layout information needed for accurate analysis.

## Extraction Note — 2026-04-19
Extracted as **pattern**: [[token-waste-taxonomy-and-two-mode-workflow.md]] in `extracts/patterns/`
