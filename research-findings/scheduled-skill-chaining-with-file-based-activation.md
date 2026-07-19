---
name: Scheduled Skill Chaining with File-Based Activation
summary: 'Scheduled agent workflows should chain multiple skills in sequence rather than running single prompts, controlled by file-based active/inactive flags. Example: a weekly content digest runs skill
  A (pull videos) -> skill B (analyze) -> skill C (generate posts using voice profile) -> drop in review folder. File-based activation means toggling a flag in a config file starts or stops a scheduled
  job — no infrastructure, no VPS, no cloud connectors required.'
implementation_notes: null
category: Orchestration
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources:
- agentic-os-five-pillars-claude-code.md
related_findings:
- file: five-pillar-agentic-os-framework.md
  rel: enables
- file: claude-routines-webhook-triggered-pipeline-chaining.md
  rel: same-problem
- file: scheduled-task-dashboard-observability-layer.md
  rel: extends
- file: context-aware-routing-skill-classifier-sub-skill.md
  rel: enables
- file: time-window-proactive-agent-loop.md
  rel: same-problem
- file: scheduled-tasks-for-real-time-context-maintenance.md
  rel: extends
proposals: null
date_discovered: '2026-05-25'
last_updated: '2026-05-25'
pipeline_status: synthesized
consumed_by:
- autonomous-scheduled-agent-operation.md
tags:
- session-95-reextract
---
# Scheduled Skill Chaining with File-Based Activation

## What It Is

A local-first pattern for autonomous agent workflows that combines two design decisions:

**1. Skill Chaining over Single-Prompt Scheduling**

Most practitioners create scheduled jobs that insert a single prompt. The more effective pattern chains multiple skills in sequence within a single scheduled execution:

- **Input:** Weekly content digest scheduled for Monday 9 AM
- **Step 1:** Run "YouTube Video Pull" skill — fetches last week's videos
- **Step 2:** Run "Content Analysis" skill — analyzes themes, extracts key insights
- **Step 3:** Run "LinkedIn Post Generator" skill — generates 3 posts using voice profile from shared context folder
- **Step 4:** Drop results in review folder for human approval

Each skill in the chain references the shared business context, and each step's output feeds the next step's input. The chain produces a single business-ready deliverable rather than requiring manual assembly of partial outputs.

**2. File-Based Activation Control**

Scheduled jobs are controlled by configuration files with active/inactive flags. When a job is marked active in its config file, the scheduler runs it. When inactive, it's skipped. This eliminates the need for:
- Virtual private servers
- Cloud infrastructure
- Complex orchestration platforms
- Anthropic's built-in Routines connectors (which have limited ecosystem)

The entire scheduling system runs locally using the OS's native scheduling (launchd on macOS, cron on Linux) with Claude Code's headless mode (`claude -p`).

## Why It Matters

The distinction between single-prompt scheduling and skill-chained scheduling is the difference between automating a task and automating a workflow. Single prompts produce raw outputs; skill chains produce business-ready deliverables. Combined with file-based activation, this creates a scheduling system that is fully transparent (every step is visible), locally controlled (no cloud dependency), and cheaply operated (subscription pricing, no API costs).

For MetaSystem, this pattern maps to composing IL skills (research-loop, identify-artifacts, extract-artifacts) into automated pipelines that could run on schedule with human gates between stages.

## Why People Are Using It

The practitioner describes Anthropic's Routines feature as "limited to built-in connectors," making it difficult to interact with apps outside the native connector ecosystem. Building locally with file-based activation and `claude -p` provides access to the full OS capability set (file system, CLI tools, scripts) while maintaining subscription pricing.

## Potential Improvements

The file-based activation pattern would benefit from a standard schema: job name, schedule (cron expression), skill chain (ordered list), activation flag, last-run timestamp, last-run status. This enables the scheduled task dashboard pattern to visualize all jobs. Error handling between chain steps (what happens when step 2 fails?) is not addressed — the practitioner's "human checkpoint before publish" handles this implicitly but does not address mid-chain failures.

## Potential Failure Modes

File-based activation is fragile: a typo in the config file silently disables a job. No alerting when a scheduled job fails or when the entire scheduler stops running (laptop closed, machine rebooted). Skill chaining without error propagation means a failed early step produces garbage input for subsequent steps. The practitioner's 20% failure rate in fully autonomous workflows likely includes chain-propagation failures.
