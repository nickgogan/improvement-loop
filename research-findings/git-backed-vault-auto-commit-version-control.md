---
name: Git-Backed Vault with Auto-Commit for Free Version Control
summary: Cloning a GitHub repository as the Obsidian vault root gives free version control and cloud sync. The Obsidian Git community plugin then auto-commits changes after a configurable idle period (e.g., 1 minute) and pulls on startup — eliminating manual commit discipline.
implementation_notes: MetaSystem vault is already Git-backed. The auto-commit plugin could close the gap between edit and commit, reducing risk of lost work between manual commits.
category: Agentic OS
evidence_strength: Strong (production-tested)
adoption_status: Partially Adopted
proposer_priority: P3 (Monitor)
applicability:
- General
- S3 (Claude Code Build)
adopted_in:
- General / Cross-System
sources:
- claude-code-obsidian-second-brain-project-onboarding.md
related_findings:
- file: file-over-app-philosophy-for-knowledge-permanence.md
  rel: same-problem
- file: post-session-hooks-autonomous-version-control.md
  rel: same-problem
- file: obsidian-as-transparent-frontend-vs-rag-black-box.md
  rel: extends
proposals: null
date_discovered: '2026-04-19'
last_updated: '2026-04-19'
pipeline_status: raw
consumed_by: []
---
# Git-Backed Vault with Auto-Commit for Free Version Control

## What It Is
The setup is two parts. First, create a private GitHub repository and clone it locally, then open that clone as an Obsidian vault — all vault files are now tracked by Git. Second, install the **Obsidian Git** community plugin (Settings → Community Plugins → browse "Git"). Configure two options: (1) "auto commit and sync after stopping file edits" with a short interval (e.g., 1 minute), so edits commit automatically after each idle period; (2) "pull on startup" so the vault always opens with the latest remote state. The result is a fully automated version control loop that requires zero manual discipline.

This pattern sidesteps Obsidian Sync (paid) entirely. GitHub provides storage, history, and rollback for free on private repositories.

## Why It Matters
Obsidian's free tier has no sync or version control. Users who rely on local files alone risk data loss and have no history for rollback. Connecting to GitHub gives: (1) off-device backup on every auto-commit, (2) full diff history for reviewing what changed and when, (3) rollback capability to any previous vault state, and (4) multi-device access by pulling on each device. For AI-assisted vaults where Claude Code is also modifying files, version control is especially important — Claude edits are indistinguishable from human edits in the filesystem, so Git history is the audit trail.

## Why People Are Using It
Eric (EricTech) demonstrates this as the first step in his Second Brain build, framing it as the prerequisite before any Claude Code integration. The argument: before giving an AI agent write access to your knowledge base, you need a recovery mechanism. Git provides that. The auto-commit plugin then closes the loop so the safety net doesn't require human memory.

## Potential Alternatives
Obsidian Sync (paid, $4–10/month). iCloud or Dropbox sync (no version history). Manual git commits (discipline-dependent). Post-session Claude Code hooks that commit on session end (see related finding — hooks fire on session close, not on idle).

## Potential Improvements
Configure the auto-commit message template to include a timestamp and change summary rather than a default message. Add a pre-push hook to validate vault integrity. Use branch-per-major-change for larger restructuring work so the main branch always reflects a clean state.

## Potential Failure Modes
If Claude Code and the auto-commit plugin both try to commit simultaneously, race conditions can produce conflicts or corrupted commits. The 1-minute interval means up to 59 seconds of work is at risk between commits. Pushing to GitHub from multiple devices without coordination can cause merge conflicts, especially if Claude Code modifies files on one device while the human edits on another.
