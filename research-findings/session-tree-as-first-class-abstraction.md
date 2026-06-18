---
name: "Session Tree as First-Class Abstraction"
summary: "Agent sessions modeled as a tree data structure with branching, compaction, and navigation. Users can fork from any point, navigate to any node (with automatic summarization of skipped branches), and label entries as bookmarks. Enables exploratory work without losing prior context — like git for conversations."
implementation_notes: null
category: "Context Engineering"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: "P2 (Design Required)"
applicability:
  - "S3 (Claude Code Build)"
  - "General"
adopted_in: []
sources: []
related_findings:
  - file: "worktree-isolation-for-parallel-agent-sessions.md"
    rel: "same-problem"
  - file: "context-degradation-40-50-percent-threshold.md"
    rel: "enables"
proposals: null
date_discovered: "2026-05-24"
last_updated: "2026-05-24"
pipeline_status: "synthesized"
consumed_by:
  - "defending-agent-context.md"
---

# Session Tree as First-Class Abstraction

## Pattern

Agent sessions are modeled as a tree (not a linear transcript):
- **Branching**: Fork from any entry point to explore alternatives
- **Compaction**: Summarize branches to reclaim context window
- **Tree navigation**: Jump to any node; skipped branches get automatic summaries
- **Labels**: User-defined bookmarks on specific entries
- **Branch summaries**: When navigating away, the current branch gets a summary entry for future reference

Sessions persist as files. The tree structure is the persistence format.

## Why It Matters

Linear conversation history forces a single path. When the agent tries something that doesn't work, the failed attempt still occupies context. Tree-structured sessions let users branch (explore alternatives), prune (compact dead branches), and navigate (jump back to productive points) — all without losing the ability to return to any previous state.

This directly addresses context degradation by allowing selective compaction of low-value branches while preserving high-value paths in full.

## How It Could Fail

- Tree complexity grows exponentially — need good UX for navigation
- Summarization quality determines whether pruned branches can be recovered
- Merge conflicts when branched work needs to converge
- Storage overhead for many branches

## Evidence

Pi agent harness (earendil-works/pi) — `session-manager.ts`, tree navigation events (`session_before_tree`, `session_tree`), branch summarization module (`compaction/branch-summarization.ts`). Test suite covers concurrent sessions, branching, compaction, and tree navigation.
