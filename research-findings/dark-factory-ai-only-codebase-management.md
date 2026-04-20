---
name: 'Dark Factory: AI-Only Autonomous Codebase Management'
summary: A "dark factory" codebase is one where AI is the sole author of all code — every issue triage, implementation, PR, code review, and merge is managed by automated agent workflows with no human-authored
  commits. Named after the 1990s manufacturing concept of fully robotized factories that need no lights because no humans work there.
implementation_notes: The dark factory pattern is the logical endpoint of harness engineering — when your workflows are reliable enough to own the full SDLC. Requires high-confidence issue classification,
  automated test validation, and a PR review workflow before human gate at merge only. Not currently viable without human review of PRs in most codebases.
category: Orchestration
evidence_strength: Low (theory + early experiment)
adoption_status: Not Yet Started
proposer_priority: P3
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources:
- archon-live-stream-agent-workflows-dark-factory.md
related_findings:
- file: archon-yaml-defined-harness-workflows.md
  rel: enabled-by
- file: self-evolving-loop-pattern.md
  rel: same-problem
- file: worktree-isolation-for-parallel-agent-sessions.md
  rel: enabled-by
- file: specialized-harness-engineering-deterministic-rail.md
  rel: enabled-by
proposals: null
date_discovered: '2026-04-19'
last_updated: '2026-04-19'
pipeline_status: raw
consumed_by: []
---

# Dark Factory: AI-Only Autonomous Codebase Management

## What It Is
A "dark factory" is a codebase where AI agent workflows are the sole authors of all code changes. The concept originates in 1990s manufacturing where fully robotized factories needed no lights because no humans worked there. Applied to software: every GitHub issue is automatically triaged (is this worth addressing for this codebase?), implemented, reviewed, and PR-merged by Archon-style harness workflows — with the human only approving final merges or monitoring via dashboard. Cole Medin described building this as a public experiment using Archon workflows on a VPS: anyone can open an issue, Archon classifies it, handles it end-to-end through an issue → implementation → PR → review → merge pipeline. MiniMax M2.7 was being tested as the underlying model (rate-limit workaround vs. Claude Opus) to enable scale.

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
