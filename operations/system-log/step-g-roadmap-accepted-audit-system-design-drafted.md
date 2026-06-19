---
id: "step-g-roadmap-accepted-audit-system-design-drafted"
title: "Step G — capability roadmap accepted; /audit-system design contract drafted; harness discovery resolved (symlink)"
date: "2026-06-12"
session: 113
system: "meta-system"
type: "milestone"
agents:
  - "Owner"
tags:
  - "step-g"
  - "audit-system"
  - "design-contract"
  - "harness-discovery"
  - "symlink"
  - "capability-roadmap"
  - "rule-10"
  - "rule-11"
related_artifacts:
  - "agents/CLAUDE.md"
  - ".claude/agents/owner.md"
  - "project-management/capability-roadmap.md"
  - "project-management/design-notes/2026-06-12-audit-system-design-contract.md"
roadmap_step: "Cross-system Step G (in progress)"
---

# Step G — roadmap accepted, /audit-system design drafted

Session 113 advanced the cross-system roadmap into step G by resolving the three sub-tasks the session 112 handoff defined: harness discovery placement, capability roadmap gate, and `/audit-system` research/design phase.

## What landed

| Artifact | Path | Purpose |
|---|---|---|
| Workspace-root engine symlink | `.claude/agents/meta-system-owner.md → ../../systems/meta-system/.claude/agents/owner.md` | Cross-context invocability of MetaSystem Owner subagent; relative path; survives full-repo moves |
| Pattern Notes updated | `systems/meta-system/agents/CLAUDE.md` | Records the symlink decision + the empirical walk-up union discovery model |
| Capability roadmap accepted | `systems/meta-system/project-management/capability-roadmap.md` | All five acceptance criteria ruled; stage advanced from `draft` to `accepted` |
| `/audit-system` design contract | `systems/meta-system/project-management/design-notes/2026-06-12-audit-system-design-contract.md` | Discovery contract, composition model, three-artifact output (manifest, per-artifact findings, summary), boundaries, sequencing for session 114+ |
| New design-notes folder | `systems/meta-system/project-management/design-notes/` | Convention mirrored from IL; home for MetaSystem deliberative specs |
| Probe deleted | `systems/improvement-loop/.claude/agents/test-discovery.md` | Session 112 probe; resolved |

## Sub-task 1 — Harness discovery resolution

Empirical test (Nick ran `/agents` from three cwds, screenshots reviewed):

| cwd | Visible agents | Interpretation |
|---|---|---|
| `MetaSystem/` (workspace root) | librarian, notion-explorer, owner, meta-system-owner (via symlink) | Symlink followed; cross-cwd invocability works |
| `systems/improvement-loop/` | librarian, notion-explorer, owner, **test-discovery**, meta-system-owner (via symlink) | Walk-up unions IL-nested + workspace-root; symlink gives MetaSystem Owner cross-system reach |
| `systems/meta-system/` | librarian, notion-explorer, owner, meta-system-owner (once, no warning) | Despite symlink + fractal-home file both reachable, harness dedupes silently (likely inode-based) |

**Discovery model established:** Claude Code walks UP from cwd and **unions** every `.claude/agents/` directory along the ancestor chain, scanning each recursively. Sibling-system `.claude/agents/` directories are NOT discovered. Workspace-root placement (or a workspace-root symlink) is the only way to make a system-scoped subagent invocable from outside its own subtree.

**Decision:** symlink at workspace root (`./.claude/agents/meta-system-owner.md` → fractal home), relative path, single source of truth on disk. Empirically validated: no name collision, harness follows symlink, cross-context discoverable. Recorded in `systems/meta-system/agents/CLAUDE.md` Pattern Notes alongside the discovery model itself.

## Sub-task 2 — Capability roadmap gate resolutions

Five acceptance criteria, all ruled (see roadmap file for full text):

1. **Targets confirmed:** `/audit-system` and `/design-harness` are step-G targets, no scope changes.
2. **Open design questions gated:** `/audit-system` decisions ruled (see sub-task 3); `/design-harness` decisions deferred to when that build begins (session 115+).
3. **Soft-prereq decisions:**
   - **Harness `§Construction` backfill:** **before** `/design-harness` build (priority queue item 3 elevated to side-quest preceding `/design-harness`). `/audit-system` may proceed in parallel.
   - **IL Owner skill parameterization (IB-168):** keep deferred; trigger on recurring evidence.
   - **Workspace-root mirror:** resolved sub-task 1.
4. **Audience archetypes:** default 1–5 (Nick-builder, portfolio-presenter, practitioner-friend, builder-friend, employer-evaluator).
5. **Sequencing approved:** `/audit-system` before `/design-harness`; discovery contract is the load-bearing first decision for `/audit-system`; harness `§Construction` backfill lands before `/design-harness`.

Notable: Nick's initial pick of "Require explicit manifest" for the discovery contract reframed the manifest as an audit *output* (structural inventory deliverable), not an input precondition. This converted what looked like a friction-introducing choice into a richer output shape. Design contract now ships three artifacts (manifest, per-artifact findings, summary) and includes re-audit-via-manifest-diff as a known pattern.

## Sub-task 3 — `/audit-system` design contract

Drafted; no SKILL.md written (build is session 114+).

Key stances codified:

- **Input:** local path; optional `--scope`, `--variant`, `--manifest-only`, `--diff <prior-manifest>` flags.
- **Discovery:** shape-based glob auto-detect for skills, agents (subagent + fractal), CLAUDE.md (variant A default; human override), standalone prompts. Symlinks not followed beyond target tree (avoids workspace-root → fractal-home loop). When `<path>` is a system root, audit is system-only; no auto-recurse into sibling systems.
- **Composition:** Librarian as subagent per artifact (IL `/assess-*` are skills, not subagents; Librarian invokes them in fresh context). Rule-10 inverted application — MetaSystem orchestrates, IL Librarian assesses. Parallelizable.
- **Output:** three artifacts (manifest, per-artifact findings, whole-system summary). Default location `.audit/manifest-<date>.md` if writable; conversation-only otherwise. Audience archetypes 1–5 consume different layers.
- **Whole-system invariants:** empty in v1 per rule 11. Candidate list deferred (cross-reference integrity, fractal compliance, audit/design symmetry, governance-source freshness, discoverability invariants). Each gated on 2-3+ recurring concrete instances.
- **Out of scope v1:** re-audit visualization beyond `--diff`, remediation suggestions, cross-system aggregation, deployment gating, custom check authoring, audit of IL substrate itself.

Six deferred implementation questions flagged for session 114 build conversation (spawn payload shape, output location convention, CLAUDE.md ambiguity dispatch, subagent concurrency, manifest schema versioning, `--recurse` for nested systems).

## Design-notes folder placement

Owner created `systems/meta-system/project-management/design-notes/` (didn't exist) mirroring IL's convention. The memory `project_owner_design_artifacts_in_governance.md` flags an unsettled question about Owner design output going to `governance/` vs `project-management/`. Owner ruled pragmatically: the design contract is tightly paired with `capability-roadmap.md` already in `project-management/`, so co-location is more discoverable than splitting. Easy to relocate if Nick prefers otherwise; flagged as a session 114 sanity-check question.

## What did not change (and why)

- **No SKILL.md for `/audit-system`.** Per handoff: research/design phase only this session; SKILL.md is session 114+.
- **No `/design-harness` design work.** Sequenced after `/audit-system`; harness `§Construction` backfill is its precondition.
- **No new DDs.** No architectural rule emerged that warrants a DD beyond existing rules (10, 11). Symlink approach + walk-up union discovery are findings about the harness, not new IL/MetaSystem governance.
- **No promotion of rules 10/11 to MetaSystem constitution.** Standing: defer until second cross-system instance.
- **No cross-boundary writes to IL.** Read IL `/assess-*` SKILL.md files, consumer-abstractions-map; did not modify any IL artifact.
- **No mid-session PROGRESS.md updates.** Per governance rule; single update at session close.

## Followups for session 114

- Begin `/audit-system` SKILL.md implementation per design contract sequencing (steps 1–6).
- Resolve six deferred open questions in build conversation.
- Test against IL (first real audit target) and MetaSystem (second target).
- Sanity-check design-notes folder placement (governance/ vs project-management/) with Nick.
- Harness `§Construction` backfill may begin as parallel side-quest if Nick gates it.

## Telemetry

```yaml
model: claude-opus-4-7[1m]
context_window_size: 1000000
turns: ~25
tool_calls: ~30
subagents: 0
capture_quality: estimated
harness: claude-code-cli-cursor-macos
```
