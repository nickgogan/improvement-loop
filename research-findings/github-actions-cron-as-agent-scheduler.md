---
notion_id: 32b1e08b-9b34-81c9-a305-ffe204095390
name: GitHub Actions Cron as Agent Scheduler
summary: Using GitHub Actions cron jobs as a free, cloud-hosted scheduler to trigger Claude Code orchestrator agents on a fixed interval (e.g., hourly), requiring no dedicated server infrastructure.
implementation_notes: null
category: Orchestration
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
priority: P3
applicability:
- S3 (Claude Code Build)
adopted_in: []
sources: []
proposals: []
date_discovered: '2026-03-22'
last_updated: '2026-04-20'
pipeline_status: raw
consumed_by: []
related_findings:
- file: claude-routines-webhook-triggered-pipeline-chaining.md
  rel: same-problem
---
# GitHub Actions Cron as Agent Scheduler

## What It Is
The orchestrator.py script is stored in a GitHub repository. A .github/workflows/*.yml file defines a cron schedule (e.g., every hour). On each trigger, GitHub Actions spins up a runner, installs dependencies, sets environment variables (API keys stored as GitHub Secrets), and executes the orchestrator. All results are written back to the repo as committed files or to external APIs. Modal is named as an alternative scheduler.

## Why It Matters
Eliminates the need to run a persistent server or manage infrastructure just to schedule a recurring agent. GitHub Actions free tier provides sufficient compute for lightweight orchestrator runs. API keys stay in GitHub Secrets, not in code.

## Why People Are Using It
GitHub Actions is already the CI/CD standard for most developers, so the mental model is familiar. It handles retries, logs, and notifications. Nick deployed the full email optimizer pipeline (including GitHub Actions setup) in a single Claude Code session.

## Potential Alternatives
Modal, Railway, Fly.io, AWS Lambda with EventBridge, or a simple VPS with cron. GitHub Actions has a 6-hour job timeout which could be a constraint for long-running experiments.

## Potential Improvements
Adding Slack webhook notifications on completion (Nick does this) improves observability. Matrix jobs could run multiple experiments in parallel.

## Potential Failure Modes
GitHub Actions free tier has usage limits. Secrets rotation is manual. The 6-hour timeout constrains maximum experiment duration.
