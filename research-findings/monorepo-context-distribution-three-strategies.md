---
name: "Monorepo Context Distribution — Three Strategies"
summary: "Three monorepo repos solve package-level AI context differently: n8n distributes CLAUDE.md→AGENTS.md chain-loaders per package (~44 packages), Archon uses path-scoped .claude/rules/*.md files that auto-load by directory (11 rules), and LangGraph uses a single global CLAUDE.md for all 8 libraries. Tradeoff: context precision vs. authoring effort vs. simplicity."
implementation_notes: null
category: "Context Engineering"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
proposer_priority: null
applicability:
  - "S3 (Claude Code Build)"
  - "General"
adopted_in: []
sources: []
related_findings:
  - {file: "seven-context-loading-mechanisms-no-convergence.md", rel: "extends"}
  - {file: "tiered-context-injection-over-monolithic-files.md", rel: "same-problem"}
  - {file: "cross-platform-context-file-strategy.md", rel: "same-problem"}
proposals: null
date_discovered: "2026-04-09"
last_updated: "2026-04-09"
pipeline_status: "raw"
consumed_by: []
---

## What It Is

Three repos with monorepo architectures each solve package-level context distribution differently:

1. **Per-package chain-loaders (n8n):** Each of ~44 monorepo packages gets its own `CLAUDE.md` → `@AGENTS.md` pair. The `AGENTS.md` in each package contains domain-specific conventions — frontend has CSS variable references, nodes-base has INodeType patterns, database has migration DSL rules. When working in a package directory, Claude Code auto-loads that package's context.

2. **Path-scoped rules (Archon):** 11 `.claude/rules/*.md` files auto-load based on which directory the agent is editing. Each rule file covers a domain concern (orchestrator, workflows, isolation, adapters, database, etc.). No per-package CLAUDE.md files needed — the rules system handles distribution.

3. **Single global file (LangGraph):** One `CLAUDE.md` at the monorepo root (~58 lines) serves all 8 libraries. No package-level context files exist. The content is brief enough that global loading is not wasteful.

## Why It Matters

As projects grow into monorepos, the question of "how does each package get its own relevant context?" becomes architectural. A single monolithic CLAUDE.md with everything doesn't scale — an agent editing the frontend shouldn't load database migration rules. But maintaining per-package context files is an authoring and maintenance burden.

The three strategies represent a tradeoff spectrum: n8n maximizes context precision at the cost of maintaining 44+ file pairs; Archon balances precision and effort via the rules auto-loading system; LangGraph prioritizes simplicity by accepting that all packages share the same (minimal) context.

## Why People Are Using It

Observed across [n8n](https://github.com/n8n-io/n8n) v2.16.0, [Archon](https://github.com/coleam00/archon) v0.3.2, and [LangGraph](https://github.com/langchain-ai/langgraph) v1.1.6 — see [[n8n-analysis]], [[archon-analysis]], and [[langgraph-analysis]] for structural details.

n8n's approach is the most thorough and is viable because each package has genuinely distinct conventions. Archon's path-scoped rules are more maintainable for smaller monorepos. LangGraph's minimalism works for a Python framework with uniform conventions across libraries but wouldn't scale for a platform like n8n.

## Potential Alternatives

Directory-convention-based context (files named by directory structure). MCP-based context serving (a context server that returns relevant context based on the current file path). Build-step-generated context files from a single source definition.

## Potential Improvements

A hybrid: global CLAUDE.md with path-scoped overrides that inject additional rules for specific packages. Auto-detection of which packages have drifted from the global conventions, flagging where package-level context is needed.

## Potential Failure Modes

Maintenance burden with per-package files (n8n). Stale rules that reference deleted packages or renamed directories (Archon). Context gaps when a single global file doesn't cover package-specific patterns (LangGraph).
