---
id: "owner-instantiated-step-f-roadmap-drafted"
title: "MetaSystem Step F — Owner instantiated (IB-167), capability roadmap drafted"
date: "2026-06-12"
session: 112
system: "meta-system"
type: "milestone"
agents:
  - "Owner"
tags:
  - "step-f"
  - "owner-instantiation"
  - "ib-167"
  - "ib-168"
  - "dd-86"
  - "rule-11"
  - "capability-roadmap"
  - "harness-discovery"
related_artifacts:
  - "agents/owner/agent.md"
  - ".claude/agents/owner.md"
  - "agents/CLAUDE.md"
  - "CLAUDE.md"
  - "project-management/capability-roadmap.md"
  - "project-management/implementation-backlog/IB-168.md"
roadmap_step: "Cross-system Step F"
---

# MetaSystem Step F — Owner instantiated, capability roadmap drafted

Cross-system roadmap step F completed. Closes IB-167; produces the working draft for step G's gate.

## What landed

| Artifact | Path | Purpose |
|----------|------|---------|
| MetaSystem Owner full constitution | `agents/owner/agent.md` | Core Truths, Boundaries, Vibe, Continuity, Disposition, Scope, Autonomy Table, Skill Inventory (honest status), Communication, Contract |
| Engine subagent | `.claude/agents/owner.md` (`name: meta-system-owner`) | Fractal/system-scoped engine file; workspace-root mirror decision deferred pending harness discovery test |
| Agents MOC refreshed | `agents/CLAUDE.md` | From "deferred" status to active; Owner listed; vault-curator + knowledge-indexer marked planned (IB-142) |
| MetaSystem CLAUDE.md updated | `CLAUDE.md` | Owner agent reference + key paths |
| Capability roadmap draft | `project-management/capability-roadmap.md` | Step-G build targets (`/audit-system`, `/design-harness`), dependencies, open design questions, acceptance criteria |
| Deferred operational-skill IB | `project-management/implementation-backlog/IB-168.md` | Per-skill parameterize-vs-equivalent decisions, triggered by recurring evidence |

## Three gate decisions resolved (with Nick)

1. **Skill reuse strategy.** Honest inventory with per-skill status markers in the Owner's Skill Inventory section, plus a single deferred IB item (IB-168) capturing the per-skill parameterize-vs-equivalent decision. Rule-11 compliant: no duplication built; no premature parameterization; each decision triggered by recurring evidence when MetaSystem Owner reaches for that capability.

2. **Engine subagent placement.** Surfaced an architectural tension Nick raised: the harness discovery model is optimized for "one project, one agent root" but the MetaSystem design intent is per-system ownership. Anthropic's `code.claude.com/docs/en/sub-agents` confirms: subagents are discovered by walking UP from cwd to find a `.claude/agents/` root, then scanning that root recursively into subfolders. `name:` is globally unique within scope. Not yet settled empirically: whether walk-up unions all `.claude/agents/` along the chain or stops at first match.

   **Decision:** Build the canonical engine file at its fractal home (`systems/meta-system/.claude/agents/owner.md`). Defer workspace-root mirror/symlink decision pending the empirical test next session. A probe file (`systems/improvement-loop/.claude/agents/test-discovery.md`) was placed for the test.

3. **Write scope and governance authority.** Owner writes to `governance/proposals/` (agent-initiated proposals only; `governance/proposals/CLAUDE.md` already documented the agent-only semantic), `operations/system-log/`, `operations/handoffs/`, `agents/owner/reflections/`, and `agents/CLAUDE.md`. Governance source writes (constitution, values, principles, vocabulary, fractal-pattern) are Proposal-First with explicit handling of inline-collaborative vs agent-initiated paths — when Owner collaborates with Nick inline, gate conversationally and write directly to source; when Owner initiates without Nick present, draft in `governance/proposals/`. DD creation remains Human-Required per DD-44.

## Notable design notes

- **MetaSystem Owner differs structurally from IL Owner.** IL Owner translates MetaSystem governance → IL operational rules. MetaSystem Owner stewards the source itself — there is no higher layer to translate from. The Skill Inventory honestly records this: `/translate-governance` is not directly applicable at MetaSystem scope.
- **`/translate-governance` reverse direction** (verify downstream system translations match the MetaSystem source) is flagged as a potential MetaSystem-specific need, but rule 11 — wait for recurring evidence (2-3+ instances of IL governance drifting from MetaSystem source) before building.
- **Honest acknowledgment that several IL skills are non-applicable at MetaSystem scope today**: `/process-feedback` (no `feedback/` folder yet), `/solicit-proposals` (only 1 MetaSystem agent — Owner). These become applicable as MetaSystem grows.

## Harness discovery test setup

A probe subagent file is placed at `systems/improvement-loop/.claude/agents/test-discovery.md`. In a fresh session opened with `cwd = systems/improvement-loop/`, check `/agents`:

- If `test-discovery` appears AND `owner` (workspace-root) also appears → walk-up unions both scopes.
- If only `test-discovery` appears → walk-up stops at first match (per-system scope shadows workspace-root).
- If only `owner` appears (no `test-discovery`) → nested `.claude/agents/` paths are not discovered.

Test result determines the workspace-root mirror/symlink decision for `meta-system-owner` engine file. Delete the probe file after resolution.

## What did not change (and why)

- **No DD created.** Following the proposals MOC and the "governance/proposals/ is for agents only" memory, Owner+Nick inline collaboration writes to DDs/source directly; this session's work didn't surface a new architectural rule warranting a DD. The honest-inventory pattern, the asymmetric naming choice, and the harness-discovery treatment are session-specific applications of existing rules (10, 11) — not new ones.
- **No vault-curator or knowledge-indexer authored.** IB-142 sequenced after Owner; deferred to a future session.
- **No `/audit-system` or `/design-harness` built.** Those are step G, gated on roadmap acceptance.
- **No promotion of rules 10/11 to MetaSystem constitution.** Nick standing: defer until second cross-system instance surfaces.
- **No mirror/symlink at workspace-root `.claude/agents/` for meta-system-owner.** Decision deferred to empirical test.
- **No edits to IL Owner agent.md or IL CLAUDE.md.** Cross-boundary write; not in MetaSystem Owner's scope.

## Followups for session 113

- Run harness discovery test; resolve workspace-root mirror decision.
- Delete `systems/improvement-loop/.claude/agents/test-discovery.md` probe after resolution.
- Begin step G: build `/audit-system` and `/design-harness` per roadmap; Nick gates the roadmap's open design questions first.
