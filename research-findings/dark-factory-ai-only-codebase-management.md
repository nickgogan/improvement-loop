---
name: 'Dark Factory: AI-Only Autonomous Codebase Management'
summary: A "dark factory" codebase is one where AI is the sole author of all code — every issue triage, implementation, PR, code review, and merge is managed by automated agent workflows with no human-authored
  commits. Named after the 1990s manufacturing concept of fully robotized factories that need no lights because no humans work there.
implementation_notes: The dark factory pattern is the logical endpoint of harness engineering — when your workflows are reliable enough to own the full SDLC. Requires high-confidence issue classification,
  automated test validation, and a PR review workflow before human gate at merge only. Not currently viable without human review of PRs in most codebases.
category: Orchestration
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
proposer_priority: P2 (Design Required)
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources:
- archon-live-stream-agent-workflows-dark-factory.md
- dark-factory-archon-autonomous-coding.md
related_findings:
- file: archon-yaml-defined-harness-workflows.md
  rel: enabled-by
- file: self-evolving-loop-pattern.md
  rel: same-problem
- file: worktree-isolation-for-parallel-agent-sessions.md
  rel: enabled-by
- file: specialized-harness-engineering-deterministic-rail.md
  rel: enabled-by
- file: holdout-validation-pattern-blind-regression.md
  rel: enabled-by
- file: github-label-as-workflow-state.md
  rel: enabled-by
proposals: null
date_discovered: '2026-04-19'
last_updated: '2026-04-20'
pipeline_status: raw
consumed_by: []
---

# Dark Factory: AI-Only Autonomous Codebase Management

## What It Is
A "dark factory" is a codebase where AI agent workflows are the sole authors of all code changes. The concept originates in 1990s manufacturing where fully robotized factories needed no lights because no humans worked there. Applied to software: every GitHub issue is automatically triaged (is this worth addressing for this codebase?), implemented, reviewed, and PR-merged by Archon-style harness workflows — with the human only approving final merges or monitoring via dashboard.

The concept was named/framed by Dan Shapiro (January 2026 blog post: "Five Levels from Spicy Autocomplete to the Dark Factory"). The levels: 0 (AI as search), 1 (coding intern/cruise control), 2 (pair programmer), 3 (hands-off but monitoring — recommended for most), 4 (engineering team with harnesses), 5 (dark factory — no human steering wheel).

**StrongDM** runs a production dark factory: shipping AI-authored PRs continuously with no human code review before merge. They open-sourced their PRD/architecture approach but not the full implementation. Key StrongDM innovation: the **holdout validation pattern** — the validation agent runs full regression testing without knowing what was just implemented, preventing sycophantic confirmation bias.

Cole Medin's public dark factory implementation uses:
- **Archon workflows on a VPS** (not local) with a cron job orchestrator that checks every N minutes for unlabeled GitHub issues
- **MiniMax M2.7** as the underlying LLM (Anthropic-compatible API endpoint, ~Claude Haiku cost, better quality) — bypasses Claude subscription rate limits for high-volume public workload
- **4 workflows**: triage → implement → validate-PR → fix
- **GitHub labels as state machine**: `factory-accepted`, `in-progress`, `needs-fixed`, `needs-human`, `factory-rate-limit`
- **Batch size cap**: 10 issues per orchestrator cycle (prevents token runaway on issue spikes)
- **Governance layer**: mission.md + factory-rules.md injected into every workflow as shared context

## Why It Matters
The dark factory represents the ceiling of harness engineering maturity. It forces every part of the SDLC to be defined as an explicit, testable workflow: issue classification, research, implementation, testing, PR review, and merge gating. Attempting to build one surfaces every assumption about workflow reliability and human oversight. Even if not pursued to completion, defining "what would a dark factory require?" clarifies which harness workflows need the most hardening.

## Why People Are Using It
Cole Medin framed this as a "build in public" experiment — a live demonstration that Archon workflows are composable enough to cover the full SDLC without human code authorship. The motivating observation: Stripe Minions ships 1,300 AI-only PRs/week via harness. A dark factory extends this to all code — not just fixes, but the complete software lifecycle. Early testing is using MiniMax M2.7 through Claude Code's provider substitution to avoid Anthropic rate limits while running many parallel workflows.

## Potential Alternatives
- Human-in-the-loop at every stage (standard harness) — much more common, more reliable
- Automated PR generation but human code review (middle ground — Stripe Minion approach)
- Autonomous agents with broad permissions (e.g., Devin) — different trust model

## Potential Improvements
- Issue quality classifier to reject low-quality or out-of-scope issues before spending tokens
- Automated merge confidence score based on test pass rate, code review comments addressed, and diff size
- Rollback workflow for reverting dark factory merges that introduce regressions
- Human escalation path: if the workflow fails 2+ times on an issue, page a human

## Potential Failure Modes
- Prompt injection via GitHub issues (external users crafting issues to manipulate the agent)
- Unchecked token spending if issue volume spikes or workflows loop
- Quality drift — successive AI-authored changes build on previous AI choices, compounding suboptimal patterns
- Security vulnerabilities introduced without human security review
