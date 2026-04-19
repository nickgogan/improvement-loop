---
name: "Git Status Context Injection and Token Hygiene"
summary: "Claude Code injects git status (up to 2000 chars / ~500 tokens) into every conversation start. Messy repos with many untracked files waste tokens and distract the model. IDE integrations (VS Code, JetBrains) silently stream open files and highlighted lines. Practitioners recommend frequent commits and post-session hooks for autonomous cleanup."
implementation_notes: "Directly applicable to MetaSystem. Current .gitignore and commit hygiene directly affect Claude Code token efficiency. Post-session hooks can auto-push to branches."
category: "Context Engineering"
evidence_strength: "Strong (production-tested)"
adoption_status: "Not Yet Started"
proposer_priority: "P1 (Implement Now)"
applicability:
  - "S3 (Claude Code Build)"
adopted_in: []
sources: ["claude-codes-leak-changes-everything.md"]
related_findings:
  - file: "post-session-hooks-autonomous-version-control.md"
    rel: "same-problem"
  - file: "agent-context-kiss-commandments-minimum-viable.md"
    rel: "same-problem"
    rel: "same-problem"
date_discovered: "2026-04-07"
last_updated: 2026-04-08
pipeline_status: "raw"
consumed_by: []
---

## What It Is

Claude Code's source code leak confirmed that every conversation begins with invisible context injection including: (1) the current date, and (2) the full git status output, capped at 2000 characters (~500 tokens). In IDE integrations (VS Code, JetBrains), every highlighted line and every open file is also silently streamed to the model.

The practical implication: a messy repo with 50 untracked files burns ~500 tokens of context on every single message, potentially distracting the model from the actual task. The fix is token hygiene -- keeping git status clean through frequent commits. Post-session hooks that automatically push to a branch after every Claude Code session are recommended as an autonomous version control pattern.

The transcript also reveals that in IDE integrations (VS Code, JetBrains), every highlighted line and every open file tab is silently streamed to the model alongside the git status, compounding the invisible context cost. The git status injection was independently discoverable before the leak -- Agentic Lab confirmed it by simply asking Claude Code "what's in your context" -- but the leak provided the exact implementation details including the 2000-character cap.

## Why It Matters

500 tokens per message is a small but constant tax. Over a long session with many turns, this adds up. More importantly, a cluttered git status can bias the model's attention toward irrelevant files. This is a concrete, measurable context engineering concern with a simple fix.

## Why People Are Using It

Agentic Lab confirmed this pattern through source code analysis. The 2000-character cap and ~500 token cost are exact figures from the codebase. Post-session hooks for auto-pushing are an emerging best practice in the Claude Code power user community.

## Potential Improvements

Implement a post-session hook in MetaSystem that auto-commits work-in-progress to a branch. Add .gitignore entries for common noise files. Consider a pre-session hook that warns if git status exceeds a token threshold.

## Potential Failure Modes

Over-aggressive .gitignore can hide legitimate untracked files. Auto-commit hooks can create noisy commit history. Post-session push to wrong branch could overwrite work.

## Extraction Note — 2026-04-19
Extracted as **pattern**: [[git-status-context-injection-token-hygiene.md]] in `extracts/patterns/`
