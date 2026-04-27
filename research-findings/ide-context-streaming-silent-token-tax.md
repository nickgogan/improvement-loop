---
name: 'IDE Context Streaming: Silent Token Tax'
summary: When using Claude Code through VS Code or JetBrains, every file opened and every line highlighted gets silently streamed to the model as context. This invisible context injection inflates token
  consumption without the user's awareness. Users can ask the model 'what do you see?' to discover what's being injected.
implementation_notes: Important for cost management. Users should be aware of IDE-injected context and its token cost implications.
category: Context Engineering
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- S3 (Claude Code Build)
adopted_in: []
sources:
- claude-codes-leak-changes-everything.md
related_findings:
- file: git-status-context-injection-token-hygiene.md
  rel: same-problem
- file: context-usage-status-line-visual-budget-tracking.md
  rel: same-problem
- file: agent-context-kiss-commandments-minimum-viable.md
  rel: enables
- file: context-usage-status-line-visual-budget-tracking.md
  rel: same-problem
proposals: null
date_discovered: '2026-04-07'
last_updated: '2026-04-08'
pipeline_status: synthesized
consumed_by:
- managing-agent-context.md
- artifact: close-irrelevant-ide-files-during-agent-sessions
  type: extracted-artifact
  form: rule
  date: 2026-04-27
  session: 83
---

## What It Is

IDE context streaming is the automatic injection of editor state into the model's context window when Claude Code runs inside VS Code or JetBrains. Every open file, highlighted selection, and visible tab gets silently sent as context tokens. The user has no visual indicator of this injection and may not realize it is happening.

## Why It Matters

Invisible context injection inflates token consumption and costs without the user's awareness or consent. It also fills the context window with potentially irrelevant content, reducing the space available for task-relevant information. This is the same class of problem as git-status injection — automatic context sources that consume tokens silently.

## Why People Are Using It

IDE integration is the default mode for many Claude Code users. The context streaming is designed to be helpful by giving the model awareness of what the user is looking at. The discovery technique — asking the model "what do you see?" — reveals the full scope of injected context, but most users never think to ask.

## Potential Improvements

Provide a visible indicator of injected context and its token cost. Allow users to configure which IDE state gets streamed (open files only, active file only, nothing). Add a context budget that caps automatic injection to preserve space for explicit context. Surface token consumption breakdowns showing automatic vs. explicit context.

## Potential Failure Modes

Disabling IDE context streaming may degrade the model's ability to provide contextually relevant responses. Users who optimize aggressively for token savings may lose the ergonomic benefits of IDE-aware assistance. Configuration complexity could create a new source of confusion for users who do not understand context window mechanics.

## Extraction Note — 2026-04-27

Extracted as **rule**: [[close-irrelevant-ide-files-during-agent-sessions]] in `extracts/rules/`. Harvested from the G2 (managing-agent-context) queue per IB-164 / DD-101 promotion path.
