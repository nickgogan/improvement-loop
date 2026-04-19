---
name: 'KAIROS: Autonomous Background Daemon for Claude Code'
summary: Unreleased Claude Code feature discovered in source leak. KAIROS is a 24/7 autonomous daemon that performs nightly memory distillation, watches GitHub webhooks, runs cron refreshes, and has 15-second
  proactive budgets — monitoring projects while the user sleeps.
implementation_notes: Behind feature flags, not yet released. Monitor for public availability. Concept of background daemon with memory distillation is applicable to MetaSystem's improvement loop.
category: Orchestration
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
proposer_priority: P3 (Monitor)
applicability:
- S3 (Claude Code Build)
adopted_in: []
sources:
- claude-codes-leak-changes-everything.md
proposals: null
date_discovered: '2026-04-07'
last_updated: '2026-04-09'
related_findings:
- file: mcp-async-task-model.md
  rel: same-problem
- file: conway-always-on-persistent-agent.md
  rel: same-problem
pipeline_status: "raw"
consumed_by: []
---

# KAIROS: Autonomous Background Daemon for Claude Code

## What It Is
An autonomous daemon hidden behind feature flags in Claude Code's source. Runs nightly memory distillation (consolidating session context into persistent summaries), monitors GitHub webhooks for relevant changes, executes cron-scheduled tasks, and has proactive 15-second budget windows to perform maintenance without user prompting.

## Why It Matters
Represents the shift from reactive (user-prompted) to proactive (always-on) agent behavior. Memory distillation could solve the "context reset" problem across sessions — the daemon consolidates learnings while the user sleeps, so the next session starts with a richer baseline.

## Why People Are Using It
Not yet publicly available — discovered via source leak analysis. Agentic Lab and other analysts flagged it as the most significant unreleased feature in the Claude Code codebase.

## Potential Alternatives
Manual session handoffs (PROGRESS.md). Scheduled Claude Code tasks via cron or GitHub Actions. The /loop skill for in-session periodic tasks.

## Potential Improvements
Could integrate with the research-loop for automated periodic scans. Memory distillation algorithms could be tuned per project type. Integration with notification systems for surfacing proactive insights.

## Potential Failure Modes
Background operations without user awareness create trust issues. Proactive budget could consume resources unexpectedly. Memory distillation without human review may consolidate incorrect assumptions into persistent context.
