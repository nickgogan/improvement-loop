---
notion_id: 32b1e08b-9b34-8184-b60e-cf39b481123d
name: Context-as-Tree Mental Model with Trunk and Branches
summary: Modeling a Claude Code session as a tree (stable trunk = reusable context; branches = explorations to trim after evaluation) provides an actionable framework for deciding what to keep, what to
  trim, and when — replacing the linear chatbot mental model.
implementation_notes: null
category: Context Engineering
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
proposer_priority: null
applicability:
- S3 (Claude Code Build)
adopted_in: []
sources:
- claude-code-works-better-when-you-do-this.md
proposals: []
date_discovered: '2026-03-22'
last_updated: 2026-04-08
related_findings:
- file: ace-agentic-context-engineering-evolving-playbook.md
  rel: same-problem
- file: agent-context-kiss-commandments-minimum-viable.md
  rel: same-problem
pipeline_status: raw
consumed_by: []
---
# Context-as-Tree Mental Model with Trunk and Branches

## What It Is
Roman's tree metaphor: the session trunk contains stable, reusable context — repository structure, the current implementation plan, key architectural decisions. Branches are explorations: debugging a bug, trying a new approach, generating a variant. Trunk content should be preserved and grown carefully. Branch content should be trimmed once the branch has served its purpose (either the approach worked and its conclusion is added to the trunk, or it failed and can be discarded entirely). The traditional linear chat model lets the tree grow until it 'falls down' (context overflow or severe rot). Trajectory engineers actively maintain trunk integrity by trimming branches immediately after evaluation.

## Why It Matters
The linear chat mental model inherited from chatbot usage leads to passive context accumulation. The tree mental model makes context shape an active design decision with clear rules: trunk grows slowly with important persistent context, branches are cheap to create and should be pruned aggressively.

## Why People Are Using It
Provides clear decision criteria for the /re trimming workflow: 'is this context I'm looking at trunk or branch?' If branch, trim it. This makes trajectory engineering systematic rather than intuitive.

## Potential Alternatives
Handoff documents between sessions (captures the trunk but requires writing), explicit project context files (CLAUDE.md) that act as a persistent artificial trunk.

## Potential Improvements
Connecting this mental model to CLAUDE.md — the trunk of the most important session-persistent context should be captured in CLAUDE.md so it survives across sessions, while in-session trunks handle session-specific but cross-trajectory context.

## Potential Failure Modes
The trunk/branch distinction is conceptually clear but situationally ambiguous — whether a piece of context is 'still relevant' often requires judgment. New practitioners may mistakenly treat all exploratory context as trunk material and never trim.
