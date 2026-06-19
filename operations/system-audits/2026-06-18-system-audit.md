---
title: "IL System Audit — 2026-06-18"
type: "audit-report"
target_system:
  - "improvement-loop"
created: "2026-06-18"
author: "agent"
tags:
  - "audit"
  - "system-health"
---

# IL System Audit — 2026-06-18

First full `/system-audit` since the engine-collapse restructure (DD-103–107). Run across all 9
inspection surfaces via four parallel read-only branches; every Critical/load-bearing finding was
re-verified against source before inclusion.

## Executive Summary

- **Overall status:** Structurally sound — **0 Critical**, post-collapse clean on the things that
  matter (no live skill/rule/CLAUDE.md path points at a dead `meta-system/` or `incubator/`
  location; fractal-complete; all 4 schematics' groundings resolve).
- **Critical findings:** 0
- **Warnings:** 9 (documentation drift + one tooling-declaration bug)
- **Info:** 10

The dominant theme is **post-collapse residue** — a handful of governance/CLAUDE.md docs still
carry pre-collapse framing (Claude Build as live, Household OS as an agent peer) or cite
retired-system DDs as live authority. None block operation. The single functional bug is the
`design-skill`/`design-agent` `allowed-tools` declaration (`Task` vs the `Agent` tool their bodies
actually invoke).

> **Verification correction:** one branch flagged `CLAUDE.md:32` (subagents via
> `.claude/agents/owner.md`) as Critical. Re-verified: this is **correct** — the line says "from
> anywhere in the workspace," and workspace-root `.claude/agents/` is exactly where Claude Code
> registers subagents (`owner.md`, `librarian.md` both present there). **Not a finding.**

## Findings by Category

### Agents (Step 1)

| Agent | Sections Complete | Skill Inventory Matches | Paths Valid | DD Valid |
|-------|-------------------|-------------------------|-------------|----------|
| Owner | Yes | **No** — missing `/audit-system`, `/solicit-proposals` | Yes | Yes |
| Researcher | Yes | **No** — missing `/research-query` | Yes | Yes |
| Codifier | Yes | **No** — missing `/reassess-priorities` | Yes | Yes |
| Librarian | Yes | Yes | Yes | Yes |

All four agent.md files have the full required section set. The drift is skill-inventory: three
agents omit a skill that exists on disk and is assigned to their role in `CLAUDE.md` /
`handoff-protocol.md`. **[Warning]**

`handoff-protocol.md` has two stale spots **[Warning]**: (a) line ~148 claims the Librarian has "no
dedicated skills" — it now has 8 (`/assess-*`, `/design-*`, `/ask-kb`, `/compare-repos`,
`/detect-drift`); (b) the `pipeline_status` model is the current 4-state (`raw→classified→
extracted` / `raw→synthesized`) but `researcher/agent.md` and `codifier/agent.md` still describe a
3-state model omitting `classified`.

### Skills (Step 2)

29 of 34 skills clean. Problem rows:

| Skill | Issue | Severity |
|-------|-------|----------|
| `design-skill` | `allowed-tools: …Task` but body (line 206) invokes the **`Agent`** tool | Warning |
| `design-agent` | Same — declares `Task`, body (line 276) invokes `Agent` | Warning |
| `synthesize-guide` | Over-declares `Agent` (no spawn in body) | Info |
| `cleanup-cache` | References `app/pdf-to-markdown/_downloads/` (not-yet-created, gitignored — benign) | Info |
| `research-proposer` | Carries stale S2/S3 + `improvement-proposals/` refs — but correctly `user-invocable: false`, DD-80 deprecated | Info |

Verified: peer spawning skills (`source-triage`, `identify-artifacts`, `extract-artifacts`)
correctly declare `Agent`. The `Task`/`Agent` mismatch in the two `design-*` skills could block the
rule-10 fresh-context audit delegation if `allowed-tools` is enforced. **[Warning]**

### CLAUDE.md (Step 3)

| Finding | Where | Severity |
|---------|-------|----------|
| Broken pointer `agents/il-agent-handoff-protocol.md` (actual: `handoff-protocol.md`); line 34 cites it correctly | `CLAUDE.md:91` | Warning |
| `/audit-system` exists on disk but is in **no** skill table (only prose, line 15) | `CLAUDE.md` skill tables | Warning |
| Hardcoded count "5 historical proposals" — violates no-hardcoded-counts (governance Process Rule 3) | `CLAUDE.md:69` | Warning |
| Blanket "Each directory contains an `_index.md`" contradicts governance Process Rule 1 (`_index.md` retirement) | `CLAUDE.md:74` | Warning |
| Stale data-source path `improvement-proposals/*.md` (only `archive/improvement-proposals/` exists) | `CLAUDE.md:175` | Warning |
| `knowledge/schematics/` (DD-107) omitted from the knowledge row + Fractal Compliance table | `CLAUDE.md:67,207` | Warning |
| `docs/` and `audit-reports/` are undocumented top-level dirs | `CLAUDE.md` dir table | Info |

### Governance (Step 4)

| Finding | Where | Severity |
|---------|-------|----------|
| **Stale federation framing** — "Schema changes go through Claude Build. Notion operations go through Household OS agents" + "IL does not receive automated feedback from Household OS or Claude Build." Treats Claude Build as live and Household OS as an agent-bearing peer; contradicts DD-103/106. | `governance/boundary-rules.md:38,47` | Warning (highest value) |
| Workspace rule "Schema changes only through Claude Build" — stale (Claude Build retired) | `../../.claude/rules/governance.md:26` (workspace scope — see Out of Scope) | Warning |
| Federation reference inside a dated proposal (historical artifact) | `governance/proposals/2026-04-24-*.md:53` | Info |

`governance/` has real content (agent-rules, boundary-rules, knowledge-rules, pipeline-rules,
proposals/). The `meta-system` mentions in IL `CLAUDE.md` are deliberate negative-space framing
("no separate meta-system above the engine") — correct, not drift.

### Structure / Fractal (Step 5)

Engine is **fractal-complete**: `app/`, `governance/`, `knowledge/` (patterns/guides/templates/
reference + schematics), `agents/`, `project-management/`, `operations/`, `archive/` all present.
Charter exception (`CHARTER.md` at root, DD-105) confirmed. Extra dirs (`docs/`, `audit-reports/`,
research-data dirs) permitted under fractal-pattern Exemptions; `docs/`+`audit-reports/` are just
undocumented (above). No structural defect. **[Info]**

### Cross-References (Step 6)

| Finding | Where | Severity |
|---------|-------|----------|
| **DD-49 dangling but cited as live authority** for IL-scoped skills — no resolvable DD-49 in live IL governance | `CLAUDE.md:67,108`, `knowledge/guides/skill-authoring-guide.md:14`, `knowledge/patterns/capability-type-selection.md`, `knowledge/templates/_index.md` | Warning |
| DD-34 dangling in live knowledge docs | `skill-authoring-guide.md:13`, `capability-type-selection.md:13,146` | Warning |
| DD-33 dangling (only in immutable DD bodies — lower priority) | `DD-47.md:101`, `DD-51.md:45` | Info |
| `dd-66.md` lowercase filename (sole case-inconsistent governance file) | `project-management/design-decisions/dd-66.md` | Info |
| DD-01..DD-28 dangling — former Household OS DDs, expected post-collapse residue (distributed to Notion/archive, DD-58) | `knowledge/reference/household-os/…`, immutable DD bodies | Info |
| Inter-file links in 4 key nav docs (CLAUDE.md, schematics/_index.md, handoff-protocol.md, fractal-pattern.md) all resolve | — | Info (clean) |
| No live doc points at a dead `meta-system/` or `incubator/` path (all hits are immutable DDs amended in-place by DD-103, or historical design-notes/SL) | — | Info (clean) |

### Feedback (Step 7)

`feedback/` is empty — **no unprocessed feedback. [Clean]**

### Recent History (Step 8)

| Finding | Severity |
|---------|----------|
| SL frontmatter date-field drift — mixed `date:` / `timestamp:` / neither across recent entries; breaks chronological tooling/Dataview | Info |
| Stale `system: "meta-system"` in pre-collapse SL frontmatter (sessions 113–116) — historical residue, source of some dangling `meta-system/` paths | Info |
| session-121 `/detect-drift` schematic date-basis contract lives only in an SL entry, not a DD/skill spec — minor governance-durability gap | Info |
| `workspace-restructure-executed.md` lists IB-129/136/137/138 as Queued — confirm closed or moot post-restructure | Info |

Recent structural changes are well-covered by governance (collapse → DD-103/104/105/106; schematic
form → DD-107). No change went unrecorded.

## Prioritized Remediation

| # | Finding | Severity | Fix Via | Effort |
|---|---------|----------|---------|--------|
| 1 | `boundary-rules.md:38,47` stale Claude Build / Household-OS-peer framing | Warning | `/translate-governance` or manual edit | Low |
| 2 | DD-49 (and DD-34) cited as live authority but unresolvable — repoint to surviving IL DD or refile | Warning | manual / `/dd` | Med |
| 3 | `design-skill` + `design-agent` `allowed-tools: Task` → `Agent` | Warning | manual edit (2 lines) | Low |
| 4 | 4 agent.md skill-inventory omissions (Owner ×2, Researcher, Codifier) | Warning | `/maintain-docs --update` | Low |
| 5 | `handoff-protocol.md` Librarian "no skills" + 3-vs-4-state `pipeline_status` | Warning | `/maintain-docs --update` | Low |
| 6 | CLAUDE.md drift cluster: line 91 filename, audit-system untabled, line 69 count, line 74 `_index` claim, line 175 path, schematics omission | Warning | `/maintain-docs --update` | Med |
| 7 | `dd-66.md` → `DD-66.md` case fix | Info | `git mv` | Low |
| 8 | SL frontmatter date-field schema (pick one of `date:`/`timestamp:`) | Info | convention + backfill | Med |
| 9 | session-121 drift date-basis contract → durable spec (DD or skill note) | Info | `/dd` or skill edit | Low |

## Out of Scope Observations

- Workspace `../../.claude/rules/governance.md:26` ("schema changes only through Claude Build") and
  the embedded copy in workspace `CLAUDE.md` carry the same retired-Claude-Build framing — workspace
  scope, not IL, but worth fixing in the same pass as remediation #1.
- `/audit-system` writes whole-system reports to top-level `audit-reports/`; `/system-audit` (this
  skill) writes to `operations/audit-reports/`. Two audit-report homes — a naming overlap that could
  confuse. Consider consolidating or documenting the split.

## Comparison with Previous Audit

No prior `/system-audit` report exists in `operations/audit-reports/` (directory created by this
run). The top-level `audit-reports/2026-06-12/` is from `/audit-system` (a different skill — the
whole-system composition assessor), not comparable. This is the baseline IL system audit.
