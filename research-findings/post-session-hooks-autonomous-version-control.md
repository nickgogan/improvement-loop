---
name: Post-Session Hooks for Autonomous Version Control
summary: Using Claude Code's post-session hooks to automatically commit and push work when a session ends, ensuring no work is lost even if the user walks away. The hook fires on session completion, running
  git add/commit/push without human intervention.
implementation_notes: Already partially captured in hooks finding. This is the specific autonomous version control use case.
category: Tool Integration
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
proposer_priority: P2 (Design Required)
applicability:
- S3 (Claude Code Build)
adopted_in: []
sources:
- claude-codes-leak-changes-everything.md
related_findings:
- file: ide-first-claude-code-with-deterministic-hooks.md
  rel: extends
- file: git-status-context-injection-token-hygiene.md
  rel: same-problem
proposals: null
date_discovered: '2026-04-07'
last_updated: '2026-04-07'
pipeline_status: extracted
consumed_by:
- skills/post-session-hooks-autonomous-version-control.md
---

## What It Is

Post-session hooks are Claude Code lifecycle hooks that fire when a session ends. The autonomous version control use case configures these hooks to run git add, commit, and push automatically, ensuring all work produced during the session is preserved in version control without requiring the user to remember to save.

## Why It Matters

Work loss from abandoned or crashed sessions is a real risk in long-running agentic workflows. If a user walks away or a session times out, any uncommitted changes are at risk. Automatic post-session commits create a safety net that preserves all work regardless of how the session ends.

## Why People Are Using It

Practitioners who run multiple concurrent agent sessions report that manual commit discipline breaks down at scale. The post-session hook pattern extends the existing deterministic hooks infrastructure from pre-execution checks (linting, validation) to post-execution automation (commit, push, cleanup).

## Potential Improvements

Add configurable commit message templates that include session metadata (duration, files changed, task summary). Support conditional commits that only fire when meaningful changes exist. Integrate with branch management to push to feature branches rather than main.

## Potential Failure Modes

Automatic commits may capture incomplete or broken work that pollutes git history. Push without review violates the human-gate principle for repositories with production impact. Conflicts with pre-commit hooks or CI checks could cause silent failures where the user believes work was saved but the push was rejected.

## Extraction Note — 2026-04-19
Extracted as **skill**: [[post-session-hooks-autonomous-version-control]] in `extracts/skills/`
