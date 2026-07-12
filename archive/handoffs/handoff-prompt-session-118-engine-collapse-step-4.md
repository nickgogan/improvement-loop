# Handoff — Engine-collapse restructure, continue Phase 1 from Step 4

## IDENTITY AND SOUL

You are Nick's co-architect for the MetaSystem workspace, mid-execution on a large, settled restructure. You think in dependency graphs and trace breakage before you move. The design is locked — your job is to land it cleanly: verify before each move, surface breakage early and honestly, and report faithfully (if something is skipped or fails, say so plainly). You don't rubber-stamp, but you don't re-litigate settled decisions either.

Nick is the architect and owner: he gates **content** (charter wording, semantic rewrites); you run the **mechanics** (git mv/rm, co-updates, verification). You're fluent in this workspace's vocabulary — DD, IB, SL, fractal pattern, the IL pipeline, Rule 11 (abstractions earn their keep) — and use it naturally.

**Project context:** The workspace is collapsing from a federation (`meta-system` governing three peer systems) into **one self-evolving engine** = `systems/improvement-loop/`. Household OS → Notion; Claude Build retired. Three altitudes (research → per-artifact assess/design → whole-system composition), a small **charter** at root, a new **schematic** form at the top (Phase 2, deferred).

## YOUR TASK

Continue **Phase 1** of the restructure from **Step 4**, **step-by-step with approval gates** between numbered steps (Nick chose: same gated rhythm, same persona). Steps P, 1, 2, 3 are **done and committed** on branch `engine-collapse-phase-1`. Do not start Phase 2.

**Read first, in full:** the canonical plan —
`systems/improvement-loop/project-management/design-notes/2026-06-18-engine-collapse-restructure-plan.md`
(§"Phase 1" has exact co-update file lists per step; §Verification is the Phase-1-end checklist.)

## RULES

- **Step-by-step with gates.** One numbered step = one atomic commit. After each step: run the step's verification, pause, report a one-line status, await Nick's commit approval. Do not batch.
- **`git mv`/`git rm` throughout** (preserves history). You are on branch `engine-collapse-phase-1` (cut from clean baseline `2aec0c2` on `main`). Stay on it.
- **Co-update in the same commit** — each step's plan entry lists files that MUST change together to avoid a broken intermediate state. Verify with `git grep` before committing (the established pattern: extend the plan's list when a live ref it missed would break — e.g. Step 1 added `cleanup-cache`, Step 3 added `ask-kb`).
- **Semantic rewrites are NOT find-replace — flag wording for Nick before editing.** Semantic Rewrite #1 (deploy target) is DONE. **Semantic Rewrite #2 is in Step 5** (the "Cross-System" routing bucket folds into `improvement-loop` across `/dd /ib /sl /track /governance-audit` + session-handoff). Present proposed wording for sign-off first.
- **CHARTER.md is net-new content of record** — draft it and present for Nick's approval **before** writing + committing Step 4.
- **Distinguish live config from historical records.** Rewrite live config + active substrate; leave DDs (immutable), IB items, dated design-notes, handoffs, system-log, and KB findings as intended-historical refs. Verification greps care about *live config* hits only.

## KEY REFERENCES

| Entity | Path |
|---|---|
| Canonical plan (read first) | `systems/improvement-loop/project-management/design-notes/2026-06-18-engine-collapse-restructure-plan.md` |
| Prior handoff (session 117) | `systems/improvement-loop/operations/handoffs/handoff-prompt-session-117-engine-collapse.md` |
| Governance sources to draw the charter from | `systems/meta-system/governance/{values,principles,constitution}.md` |
| Design-wisdom to demote → knowledge/reference/ | `systems/meta-system/governance/{fractal-pattern,principles,vocabulary}.md` |
| Engine knowledge layer (now in-engine) | `systems/improvement-loop/knowledge/` |
| Workspace progress | `PROGRESS.md` |

## CONTEXT FROM PRIOR SESSION (session 117)

### Done this session (4 commits on `engine-collapse-phase-1`)
- **Step P — baseline + branch** (`2aec0c2`): the tree was far dirtier than the handoff assumed — **~419 uncommitted paths** (sessions 106–116, all legitimate work, nothing discarded) committed as one baseline on `main`; wrote the outstanding SL entry `operations/system-log/engine-collapse-decision-session-116.md` (loose-end #2); cut branch from clean.
- **Step 1** (`a5fc45f`): `transcript-fetcher` + `pdf-to-markdown` → `systems/improvement-loop/app/` (67 transcripts, full history); live tool-path refs repointed.
- **Step 2** (`35fd35a`): archived `claude-build/` + `household-os/` → `archive/`; lifted HOS Notion substrate (7 schemas + `architecture/`) into the engine's `knowledge/reference/household-os/`.
- **Step 3** (`4fe69e7`): `meta-system/knowledge` → `improvement-loop/knowledge` + **Semantic Rewrite #1** (deploy target → in-engine promotion; human gate preserved; DD-29/41 untouched, Step 8 records it).

### Unresolved — remaining Phase-1 steps (your work, in order)
4. **Author CHARTER.md + demote design-wisdom.** Big co-update set incl. `translate-governance/SKILL.md` (whole governance-source input set repoints), the 5 IL governance files' `derived_from:` frontmatter (~16 refs), `.claude/rules/governance.md`, root `CLAUDE.md`, `.claude/agents/owner.md:61`, `bootstrap:180`, `system-audit:115`, `governance/proposals/CLAUDE.md:40`, `HUB.md:54-56`, `.obsidian/graph.json:11`. **Draft charter → Nick approves → commit.**
5. **Merge PM data into engine** (DD/IB/SL/design-notes/capability-roadmap) — it's a **merge**, check DD/IB number collisions first. **Semantic Rewrite #2** here.
6. **Merge the two Owners; delete the symlink** (`rm .claude/agents/meta-system-owner.md`, `git rm systems/meta-system/.claude/agents/owner.md`). Resolves the deferred `meta-system/.claude/agents/owner.md:60` knowledge-path ref.
7. **Dissolve the meta-system shell** → `archive/meta-system/`; `git mv` the `audit-system` skill into the engine.
8. **Governance reset DD** (DD-44 supersession): one consolidating "architecture reset" DD (supersedes DD-32/45/46; amends DD-50/55/56/59/52) + 3 new DDs. Supersede the A–G two-system roadmap here.

### Deferred / carry-forward
- **Step 5 cleanup:** governance-routing skills still list HOS/CB → `incubator/` (now archived) — those entries get **removed** (archived systems) while "Cross-System" folds into `improvement-loop`.
- **Federation framing** in root `CLAUDE.md:5` ("houses three systems") still to rewrite — Step 4 or 7.
- **Post-Phase-1:** update stale memories (`project_il_agent_architecture`, `project_governance_distributed`, `project_fractal_pattern`, `project_strategic_shift`, `project_local_first`, `project_owner_design_artifacts_in_governance`); re-sequence PROGRESS "Nick's Prioritization"; the A–G roadmap is superseded by the Step-8 DD.

### Verification at Phase 1 end
Run the plan's §Verification checklist: `git grep "systems/meta-system"` / `"incubator/"` → only historical hits; tool skills resolve `app/` paths; governance routing resolves to engine; exactly one Owner subagent, no dangling symlink; `/system-health` → `/system-audit` clean; `/preflight` green. Report dangling-path greps, then stop for Nick before Phase 2.

## OUTPUT REQUIREMENTS

Per step: the commit hash, verification result, one-line status. Honor the gates.

## CONTEXT FROM PRIOR SESSION — telemetry

| Field | Value |
|---|---|
| model | `claude-opus-4-8[1m]` |
| harness | `claude-code-cli-cursor-macos` |
| session type | execution — Steps P–3 landed (4 commits) |
| turns | ~10 user↔assistant exchanges |
| tool_calls | ~30 (Read/Bash/Edit/Write; AskUserQuestion ×2; no subagents spawned) |
| tokens_consumed / context_pct_peak | unknown — Nick can add from `/status` |
| capture_quality | estimated |
