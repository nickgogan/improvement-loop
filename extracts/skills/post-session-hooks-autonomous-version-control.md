---
title: "Post-Session Hooks for Autonomous Version Control"
type: "extracted-artifact"
assigned_form: "skill"
source_finding: "post-session-hooks-autonomous-version-control"
extraction_date: "2026-04-19"
identification_report: "2026-04-19-identification-report-4.md"
deployed: false
deployed_to: null
context:
  applies_to:
    - "agentic coding systems using version-controlled repositories where session work must be preserved automatically"
    - "multi-session agent workflows where manual commit discipline cannot be relied upon"
  platform_coupling: "specific:claude-code"
  autonomy: "hitl-only"
  stage: "operate"
  reversibility: "medium — hook configuration can be removed, but autonomous commits already pushed to remote are permanent without force-revert"
  auditability: "high — every commit and push produces a git log entry; failure logs are explicitly required by the invariants; hook execution is traceable per session"
  evidence_strength: "Medium"
  adoption:
    status: "Not Yet Started"
    notes: "Pattern documented by practitioners running multiple concurrent agent sessions; no production deployments known within this system at time of extraction."
contract:
  preconditions: "Git repository is initialized with a valid remote. Authorized branch and file scope are defined before hook configuration. Pre-commit hooks have been audited."
  invariants: "Hook never pushes to main or master without explicit per-session authorization. Commit failures are always logged and surfaced. Local commits are never rolled back on push failure."
  governance: "Owner: MetaSystem / Claude Build system. Enabling this hook requires explicit Nick authorization. May not be used to commit governance documents autonomously."
  recovery: "If push fails: preserve the local commit, log the failure, surface at next session start. If pre-commit hook blocks: log the failure, do not bypass hooks."
tags:
  - "extracted-artifact"
  - "skill"
---

# Post-Session Hooks for Autonomous Version Control

**Source:** [[post-session-hooks-autonomous-version-control]]
**Form:** skill
**Extraction date:** 2026-04-19

## Purpose

Configure Claude Code post-session lifecycle hooks to automatically run `git add`, `git commit`, and `git push` when a session ends, preserving all session work in version control without requiring user action.

**Warning:** This skill involves autonomous commits and pushes. It conflicts with human-gate principles unless scoped carefully.

## Inputs

- Claude Code environment with lifecycle hook configuration access
- Git repository initialized and configured with a valid remote
- Commit message template or generation strategy
- Branch targeting policy
- Pre-commit hook configuration (existing hooks must be accounted for)

## Outputs

- Configured post-session hook
- Commit record in version control capturing all session changes
- Hook execution log entry (success or failure)

## Steps

1. **Scope definition.** Define authorized scope: which branches, which file patterns, whether push is to feature branch or staging.

2. **Pre-commit hook audit.** Identify all existing pre-commit hooks. Confirm the autonomous commit will not silently fail.

3. **Commit message strategy.** Select approach: static template, session summary, or hybrid.

4. **Hook configuration.** Configure the post-session hook: `git add {scoped files}` → `git commit -m "{message}"` → `git push origin {authorized-branch}`.

5. **Failure handling configuration.** Log failures explicitly. On push failure, preserve commit locally. Surface failure logs at next session start.

6. **Verification.** Run the hook in a dry-run or test branch context before enabling in production.

## Failure Modes

- **Incomplete or broken work committed.** Mitigate by pushing to non-main branch only; treat auto-commits as drafts.
- **Human-gate violation.** Must not be configured to push to protected branches without review.
- **Pre-commit hook conflicts.** Silent failure leaves work unpreserved. Configure explicit failure logging.
- **Sensitive file inclusion.** Always scope the add command with include or exclude patterns.
- **Conflict on push.** Preserve the local commit and log the conflict without discarding changes.

## Contract

### Preconditions
Git repository is initialized with a valid remote. Authorized branch and file scope are defined before hook configuration. Pre-commit hooks have been audited.

### Invariants
Hook never pushes to main or master without explicit per-session authorization. Commit failures are always logged and surfaced. Local commits are never rolled back on push failure.

### Governance
Owner: MetaSystem / Claude Build system. Enabling this hook requires explicit Nick authorization. May not be used to commit governance documents autonomously.

### Recovery
If push fails: preserve the local commit, log the failure, surface at next session start. If pre-commit hook blocks: log the failure, do not bypass hooks.
