---
title: "Watch Upstream Triage Report — 2026-07-13"
type: "research-report"
category: "operations"
target_system:
  - "improvement-loop"
created: "2026-07-13"
author: "owner-researcher-subagent"
tags:
  - "watch-upstream"
  - "watched-libraries"
  - "triage"
notes: |-
  Scoped pass, not --all: exactly two libraries greenlit at the wave-3 link-intake
  triage gate (2026-07-13-link-intake-triage.md, follow-up queue items 2 and 4).
---

# Watch Upstream Triage Report — 2026-07-13

Scoped run: **Archon** and **n8n** only (wave-3 gate follow-ups 2 and 4). Not a full-registry sweep.

## Summary

| Library | Spectrum | Last Version | Current Version | Delta | Action |
|---------|----------|--------------|-----------------|-------|--------|
| Archon | cherry-pick | v0.3.2 (2026-04-09) | v0.5.0 (2026-06-26) | 2 minor versions, ~11 weeks | update-entry + recommend /repo-analyzer re-run |
| n8n | cherry-pick | v2.16.0 (2026-04-09) | v2.29.10 (2026-07-10) | 13 minor versions | update-entry (changelog note per gate ruling) |

## Changes Detail

### Archon — update-entry (+ repo-analyzer recommendation)

- **Version delta:** v0.3.2 → v0.5.0 (releases: v0.3.4–v0.3.6 Apr, v0.3.9–v0.3.12 Apr–May, v0.4.0/v0.4.1 May 28, v0.5.0 Jun 26)
- **Changes:** First-class Ralph loops (until-conditions, fresh-context iterations, loop-iteration visibility); workflow UI matured (drag-and-drop builder, monitoring hub, step-by-step execution viewer, experimental `/console` run-centric console); provider layer expanded (OpenCode + GitHub Copilot community providers, Codex MCP node); GitHub App auth replacing shared PATs with per-user attribution; Slack UX overhaul; 19 default workflow templates. ~22.9k stars / 3.4k forks. Repo active.
- **Relevance:** high — loop-node semantics, provider abstraction, and workflow composability all sit inside `what_we_use` (DAG engine, mixed node types, multi-platform adapters). Worktree isolation unchanged.
- **Recommended action:** entry updated this pass. **A full `/repo-analyzer` re-run is warranted before the named-deps gap-check** — the stored v0.3.2 structural analysis predates the provider abstraction, loop-node semantics, and console/builder surfaces. Not run in this pass per scope.

### n8n — update-entry

- **Version delta:** v2.16.0 → v2.29.10 (latest stable, 2026-07-10)
- **Changes:** Official **instance-level MCP server built for coding agents** (Claude Code/Desktop, ChatGPT, custom agents). Settings → instance-level MCP; access-token or OAuth2 auth; tools for creating/editing workflows (2.13+), search/run, data tables; per-workflow opt-in for existing workflows. Verified against `docs.n8n.io/build/ways-of-building-workflows/connect-to-n8n-mcp-server`.
- **Transferable pattern:** **typed-IR compile gate** — the model authors the workflow as TypeScript against an SDK; it must type-check and compile before conversion to JSON and deployment to the instance. Structural-validity acceptance gate between generation and deploy (same family as our DD-114 frontmatter parse gate). Mechanism is maintainer-attributed (n8n team LinkedIn post quoted in video Gq0l4IYRIIU); the docs page confirms the server but not the TS internals.
- **Relevance:** medium — does not touch the context-engineering patterns we cherry-pick; the compile-gate pattern is the recorded value.
- **Recommended action:** update-entry only. Gate ruling (2026-07-13 link-intake): changelog note, no source extraction, no finding.

## Action Queue

### Update Entry (version bump only)
- Archon — done (v0.5.0, 2026-07-13, delta section + Change Log added)
- n8n — done (v2.29.10, 2026-07-13, upstream note + Change Log added)

### Extract Findings (queue for /research-loop)
- None. n8n typed-IR compile gate ruled changelog-note-only at the wave-3 gate; Archon patterns already covered by registry + Ralph-loop findings per the same gate.

### Investigate (manual review needed)
- None.

### No Action
- All other registry libraries — out of scope for this pass.

## Follow-ups

1. **Nick decision:** greenlight `/repo-analyzer` re-run on Archon before the named-deps gap-check (recommended: yes).
2. n8n instance-level MCP added to the entry's Change Signals — future `/watch-upstream` passes should track new exposed tools and TypeScript workflow-SDK changes.
