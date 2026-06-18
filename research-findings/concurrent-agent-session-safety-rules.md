---
name: "Concurrent Agent Session Safety Rules"
summary: "Explicit governance rules for multiple agent sessions running concurrently in the same working directory. Key rules: only stage files you changed, never git add -A, never destructive git operations, abort on rebase conflicts in files you didn't modify. Treats concurrent agents as first-class concern requiring explicit coordination protocol."
implementation_notes: null
category: "Governance"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: "P3 (Monitor)"
applicability:
  - "S3 (Claude Code Build)"
  - "General"
adopted_in: []
sources: []
related_findings:
  - file: "worktree-isolation-for-parallel-agent-sessions.md"
    rel: "same-problem"
proposals: null
date_discovered: "2026-05-24"
last_updated: "2026-05-24"
pipeline_status: "raw"
---

# Concurrent Agent Session Safety Rules

## Pattern

When multiple agent sessions may operate in the same working directory simultaneously, explicit rules prevent them from corrupting each other's work:

**Committing:**
- Only commit files YOU changed in THIS session
- Stage explicit paths (`git add <path1> <path2>`); never `git add -A` / `git add .`
- Before committing, verify you are only staging your files

**Never run (destroys other agents' work):**
- `git reset --hard`, `git checkout .`, `git clean -fd`, `git stash`, `git add -A`, `git commit --no-verify`

**Conflict resolution:**
- Resolve only in files you modified
- If conflict in a file you didn't modify, abort and ask the user
- Never force push

## Why It Matters

As agent teams become common (multiple agents working on the same codebase), the default assumption of exclusive file access breaks down. Without explicit coordination rules, agents will stomp on each other's work via global git operations. This is an alternative to worktree isolation — sharing a directory with behavioral constraints rather than physical isolation.

## How It Could Fail

- Rules are advisory (encoded in AGENTS.md), not enforced by the tool
- Agents may not track which files they've modified across many turns
- Race conditions between `git status` check and `git add`
- Doesn't handle non-git state (temp files, caches, running processes)

## Evidence

Pi agent harness (earendil-works/pi) — explicit Git section in AGENTS.md documenting concurrent session rules. Comment: "Multiple pi sessions may be running in this cwd at the same time, each modifying different files."
