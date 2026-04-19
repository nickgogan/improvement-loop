---
title: "Git Status Context Injection Token Hygiene"
type: "extracted-artifact"
assigned_form: "pattern"
source_finding: "git-status-context-injection-token-hygiene"
confidence: "MED"
tier: "guided"
reason_codes: []
co_occurrence: null
extraction_date: "2026-04-19"
identification_report: "2026-04-19-identification-report-3.md"
deployed: false
deployed_to: null
contract:
  preconditions: "The workspace uses git version control and is operated via Claude Code or a similar agentic coding tool that injects git status into the model context. The operator understands that untracked and modified files consume context tokens on every message."
  invariants: "Git status output remains below a defined token threshold (target: under 200 tokens). The .gitignore is comprehensive enough to exclude noise files without hiding legitimate work. Commit frequency keeps the working tree clean."
  governance: "Nick owns .gitignore policy and commit hygiene standards. Hook configurations (pre-session, post-session) require approval before deployment. No auto-push to main/master — hooks push to working branches only."
  recovery: "If git status exceeds the token threshold, run a cleanup pass: commit staged work, gitignore noise files, or stash changes. If a pre-session hook flags a dirty tree, the operator decides whether to clean up or proceed with the overhead."
tags:
  - "extracted-artifact"
  - "pattern"
---

# Git Status Context Injection Token Hygiene

**Source:** [[git-status-context-injection-token-hygiene]]
**Form:** pattern
**Extraction date:** 2026-04-19

## Problem

Agentic coding tools like Claude Code inject invisible context into every conversation turn — notably, the full git status output (capped at 2000 characters / ~500 tokens). A messy repository with many untracked or modified files burns this token budget on every single message, creating a constant tax on context capacity and potentially biasing the model's attention toward irrelevant files.

## Forces

- **Invisible cost vs. visible work.** The git status injection is silent — operators don't see it consuming tokens, so they don't manage it. The cost is real but hidden.
- **Commit frequency vs. commit quality.** Frequent commits keep git status clean but can produce a noisy commit history. Infrequent commits preserve clean history but waste tokens.
- **Gitignore breadth vs. visibility.** Aggressive .gitignore rules reduce noise but can hide legitimate untracked files that the operator needs to know about.
- **Automation vs. control.** Post-session hooks that auto-commit and auto-push eliminate manual cleanup but risk committing incomplete work or pushing to the wrong branch.

## Solution

Treat git working tree cleanliness as a context engineering concern, not just a version control hygiene practice. The goal is to keep the injected git status output minimal — ideally under 200 tokens — so the model's context budget is spent on task-relevant information.

**Key mechanics:**

1. **Comprehensive .gitignore.** Exclude all known noise: build artifacts, IDE config, OS files, temporary outputs. Review and update .gitignore at the start of each project.
2. **Frequent commits to working branches.** Commit early and often to feature/working branches. The goal is a clean `git status`, not a perfect commit history — squash on merge if needed.
3. **Pre-session awareness.** Before starting a Claude Code session, check git status. If it's cluttered, clean it up first. Consider a pre-session hook that warns when untracked file count exceeds a threshold.
4. **Post-session hooks.** After a session ends, auto-commit work-in-progress to a branch and optionally push. This prevents stale changes from polluting the next session's context.
5. **IDE tab hygiene (for IDE integrations).** Close unnecessary file tabs before starting a session. In VS Code and JetBrains, every open tab and every highlighted line is streamed to the model as additional invisible context.

## Consequences

**Positive:**
- Reclaims up to 500 tokens per message that would otherwise be wasted on noise.
- Reduces model distraction — fewer irrelevant files in context means better focus on the actual task.
- Over a long session with many turns, cumulative token savings are significant.
- Establishes a habit that improves version control hygiene as a side effect.

**Negative:**
- Over-aggressive .gitignore can hide files the operator needs to track.
- Frequent commits to working branches create a noisier git log (mitigated by squash-on-merge).
- Post-session auto-commit hooks risk committing incomplete or broken work.
- Auto-push hooks risk pushing to the wrong branch if branch management is sloppy.

## Known Uses

- **Agentic Lab** confirmed the git status injection pattern by asking Claude Code "what's in your context" and independently verified it against the source code leak.
- **Claude Code power user community** recommends post-session hooks for auto-pushing work-in-progress to branches as an emerging best practice.
- **MetaSystem** directly benefits — the workspace has many untracked files visible in git status at session start.

## Contract

### Preconditions

- The workspace uses git version control.
- The workspace is operated via Claude Code or a similar tool that injects git status into the model context.
- The operator understands that untracked and modified files consume context tokens on every message.

### Invariants

- Git status output remains below a defined token threshold (target: under 200 tokens of content).
- The .gitignore is comprehensive enough to exclude noise files without hiding legitimate tracked work.
- No auto-push targets main/master — hooks push to working branches only.

### Governance

- Nick owns .gitignore policy and commit hygiene standards.
- Hook configurations (pre-session, post-session) require approval before deployment.
- Changes to auto-commit/auto-push behavior go through a human gate.

### Recovery

- If git status exceeds the token threshold at session start, run a cleanup pass: commit staged work, gitignore noise files, or stash changes before proceeding.
- If a post-session hook commits broken or incomplete work, revert the auto-commit on the working branch before the next session.
- If .gitignore is found to be hiding legitimate files, audit and trim the ignore rules — prefer explicit ignores over broad globs.
