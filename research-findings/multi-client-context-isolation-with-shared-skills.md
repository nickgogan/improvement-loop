---
name: Multi-Client Context Isolation with Shared Skills
summary: Per-client brand context (voice, ICP, strategy, content history) with skills installed at root level shared across all clients. Switching clients filters tasks, docs, and brand context while preserving
  access to the full skill library.
implementation_notes: null
category: Context Engineering
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P3 (Monitor)
applicability:
- General
adopted_in: []
sources:
- stop-using-claude-code-in-terminal.md
date_discovered: '2026-04-07'
last_updated: '2026-04-08'
related_findings:
- file: stacking-paul-with-carl-for-domain-scoped.md
  rel: same-problem
pipeline_status: raw
consumed_by: []
---

## What It Is

An architecture for managing multiple client contexts within a single agent system. Each client gets isolated brand context (brand voice, content strategy, ICP details, target audience, communication style) while all clients share a common skill library installed at the root level. When the operator switches client context, the dashboard filters tasks, output files, documentation, and brand context to show only that client's data -- but skills remain universally available.

Documented by Simon Scrapes as part of a command center built on an "Agentic OS." The system stores business context (brand voice, client details, content strategy, target audience) as part of the agent's operating environment, not as ephemeral conversation context. This is positioned as a gap in all existing agent management tools -- they manage coding sessions in a "complete vacuum" without business context.

## Why It Matters

Most agent management tools treat each session as context-free. The operator must re-establish business context every time. For business users managing multiple clients, this context switching is a major source of error and inefficiency. The isolation pattern prevents cross-contamination (using Client A's brand voice for Client B's content) while the shared skills layer avoids duplication.

## Why People Are Using It

Business owners and agencies using Claude Code to manage multiple client workstreams need a way to maintain context boundaries. The pattern maps to how agencies already think about their work -- each client has a distinct identity, but the agency's capabilities (skills) are shared.

## Potential Improvements

Could integrate with MetaSystem's existing three-tier vault architecture (global/shared/local context). The per-client context layer maps naturally to the "local" tier in that architecture. Automated context verification on task submission could prevent cross-contamination.

## Potential Failure Modes

Context isolation may be incomplete -- agent memory from one client session could bleed into another if session boundaries are not enforced at the memory layer. Shared skills that reference client-specific patterns could produce generic outputs. Scale limit: the number of clients an operator can effectively manage is still constrained by review bandwidth, not agent capacity.
