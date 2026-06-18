---
name: "Headless-Cron Composition for Autonomous Scheduled Workflows"
summary: "Combining claude -p (headless mode) with OS-level scheduling (cron/launchd) creates fully autonomous agent workflows that execute without human presence. Best suited for batch tasks with easily verifiable output. The --allowed-tools flag constrains headless permissions as a trust guardrail. The Ralph loop variant chains headless invocations so the agent iterates on its own work across cycles."
implementation_notes: null
category: "Orchestration"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: "P2 (Design Required)"
applicability:
  - "S3 (Claude Code Build)"
adopted_in: []
sources:
  - "five-agentic-patterns-claude-code.md"
related_findings:
  - file: "claude-p-headless-mode-as-openclaw-replacement.md"
    rel: "extends"
  - file: "claude-code-loop-in-session-cron-scheduling.md"
    rel: "same-problem"
  - file: "orchestrator-headless-dispatch-context-isolation.md"
    rel: "same-problem"
  - file: "ralph-loop-brute-force-security-and-ui-testing.md"
    rel: "same-problem"
  - file: "headless-multi-pass-iterative-review.md"
    rel: "same-problem"
  - file: "five-pattern-complexity-escalation-ladder.md"
    rel: "enables"
proposals: null
date_discovered: "2026-05-25"
last_updated: "2026-05-25"
pipeline_status: "classified"
consumed_by: []
tags:
  - "session-95-reextract"
---

## What It Is

The headless pattern (`claude -p "<prompt>"`) removes the human from the loop entirely — no conversation, no terminal window, no approvals. Claude processes the prompt autonomously and returns the result. Three composition layers make this powerful:

1. **OS scheduling**: Plugging `claude -p` into cron (Linux/Mac) or Task Scheduler (Windows) creates recurring autonomous workflows. Example: "At 7 AM every day, run `claude -p 'review yesterday's commits and write a summary to morning-report.md'`". The agent reads, analyzes, writes, and exits before the developer wakes up.

2. **Permission guardrails via --allowed-tools**: Constrains what the headless agent can do. For read-only tasks, restrict to read tools only. This addresses the trust limitation — the agent has autonomy but within a bounded permission envelope.

3. **Ralph loop chaining**: The same prompt is fed back repeatedly so Claude iterates on its own work until convergence. Each iteration inherits the previous cycle's output (via files on disk). Practitioners report using this to ship entire projects overnight.

Use cases cited:
- Morning summary reports from previous day's work
- Content pipeline: fetch video transcript, generate social media posts, save to file
- Skill invocation within headless prompts for specialized workflows

## Why It Matters

This is where Claude Code transitions from "tool you sit with" to "team member that works independently." The decision criterion for going headless is **output verifiability**: only use headless mode for tasks where the output is easy to verify after the fact. Hard-to-undo operations should not run headless.

The composition with OS scheduling is significant because it moves beyond Claude Code's built-in `/loop` (session-bound, expires after 3 days) to infrastructure-level scheduling that persists across reboots, survives session termination, and integrates with existing DevOps tooling.

## Why People Are Using It

Converts idle time (nights, weekends) into productive agent time. The developer reviews output rather than directing work, which is a fundamental shift in the human-agent workflow. Combined with `--allowed-tools` for read-only constraints, the risk profile becomes acceptable for many batch tasks.

## Potential Improvements

- Standardized output format for headless results (JSON, markdown report template) to enable downstream automation
- Failure notification mechanism (email, Slack webhook) when a headless run errors out
- Incremental trust escalation: start read-only, expand permissions as confidence in the workflow grows
- Composing headless runs with git branch isolation (headless + worktree) for maximum safety

## Potential Failure Modes

- No human review means errors compound across scheduled runs — a bad morning report template produces bad reports every day until someone notices
- The Ralph loop can enter infinite iteration if convergence criteria are not well-defined
- `--allowed-tools` constraints require the user to know which tools are needed upfront; too restrictive and the task fails silently
- Cron-scheduled runs may conflict with interactive sessions using the same workspace (file locking, git state)
- Cost accumulation: scheduled runs burn tokens continuously, and without budget caps a misconfigured cron job can be expensive
