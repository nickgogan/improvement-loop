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

---

# Second Run — 2026-07-13 (BMAD + superpowers)

Second scoped pass, same day, separate invocation: **BMAD Method** and **superpowers** — the two registries flagged ~3 months stale by the named-deps gap-check ahead of restructure-program Phases 4/5. Not a full-registry sweep.

## Summary

| Library | Spectrum | Last Version | Current Version | Delta | Action |
|---------|----------|--------------|-----------------|-------|--------|
| BMAD Method | cherry-pick | v6.2.2 (2026-04-07) | v6.10.0 (2026-07-03) | 8 minor versions, ~3 months | update-entry + recommend /repo-analyzer re-run |
| Superpowers | thin-wrapper | v5.0.7 (2026-04-07) | v6.1.1 (2026-07-02) | 1 major + patches | update-entry + conditional /repo-analyzer re-run |

## Changes Detail

### BMAD Method — update-entry (+ repo-analyzer recommendation)

- **Version delta:** v6.2.2 → v6.10.0 (v6.3.0 Apr 10 → v6.10.0 Jul 3; confirmed via GitHub releases, 2026-07-13)
- **Changes:** New critical-thinking skill layer — `bmad-forge-idea` (Socratic pressure-testing), `bmad-investigate` (evidence-graded forensics), `bmad-prfaq` (Working Backwards), party-mode anti-consensus room with persistent memory. Governance primitives — canonical decision-log across workflows, shared `memlog.py` working memory, four-layer TOML config resolver, `bmad-checkpoint-preview` human review. Product layer rebuilt — `bmad-spec` five-field kernel, `bmad-prd`/`bmad-product-brief` three-intent restructure, `bmad-ux` two-spine contract, `bmad-architecture` lean-spine rewrite. Agent-team change: three personas consolidated into one Developer agent (Amelia). `bmad-loop` autonomous dev module with adversarial review (bmad-automator deprecated). 42 supported platforms on `.agents/skills/` standard.
- **Relevance:** high — the direction-note asks (high-level/critical-thinking skills; governance + product layers) map one-to-one onto what shipped since v6.2.2. The agent-team consolidation also revises the agent-composition pattern in `what_we_use`.
- **Recommended action:** entry updated this pass. **A full `/repo-analyzer` re-run IS warranted before Phases 4/5** — the stored v6.2.2 analysis predates every surface the direction note asks about.

### Superpowers — update-entry (+ conditional repo-analyzer recommendation)

- **Version delta:** v5.0.7 → v6.1.1 (v6.0.0 major 2026-06-16; v6.1.1 2026-07-02; confirmed via GitHub releases, 2026-07-13)
- **Changes:** v6.0.0 rewrote Subagent-Driven Development: single unified reviewer replaces the two sequential reviewers (spec + quality verdicts in one pass); plans gain Global Constraints + per-task Interfaces blocks; whole-branch review at end; diffs/briefs exchanged as files in `.superpowers/sdd/`; read-only review, explicit model per dispatch. ~50% fewer tokens, ~2x faster in upstream evals. Vendor-neutral skill language + per-harness tool maps; behavior tests split to a separate evals repo. Brainstorming changes are companion-app security only.
- **Relevance:** high for `what_we_use` (the recorded "two-stage review" pattern is now superseded upstream); **none for the direction-note asks** — no documented changes to brainstorming HARD-GATE enforcement or thinking skills since v5.0.7.
- **Recommended action:** entry updated this pass. `/repo-analyzer` re-run **conditionally warranted**: required if Phases 4/5 rely on review/orchestration patterns (they're stale); not required if they only need the brainstorming/thinking-skill surfaces (unchanged upstream, stored analysis still valid).

## Action Queue (second run)

### Update Entry (done this pass)
- BMAD Method — v6.10.0, 2026-07-13, Upstream Delta section + Change Log row (`watched-libraries/bmad-method.md`)
- Superpowers — v6.1.1, 2026-07-13, Upstream Delta section + Change Log row (`watched-libraries/superpowers.md`)

### Extract Findings (queue for /research-loop)
- None queued autonomously. Candidate if Nick wants them: BMAD decision-log/memlog governance primitives and the superpowers unified-reviewer + file-mediated SDD rewrite (the latter corroborates our file-mediated handoff protocol and would supersede parts of `superpowers-plugin-spec-driven-sub-agent-orchestration.md`). Gate with the repo-analyzer decision below.

### Investigate (manual review needed)
- Superpowers finding `superpowers-plugin-spec-driven-sub-agent-orchestration.md` and the DD-62 quality-tier citation of two-stage review describe an architecture upstream replaced in v6.0.0 — flag for reconciliation whenever the re-analysis runs.

## Follow-ups (second run)

1. **Nick decision:** greenlight `/repo-analyzer` re-run on BMAD before Phases 4/5 (recommended: yes, unconditionally).
2. **Nick decision:** greenlight `/repo-analyzer` re-run on superpowers (recommended: yes if Phases 4/5 touch review/orchestration patterns; skippable if only brainstorming/thinking-skill surfaces matter — those are unchanged upstream).
