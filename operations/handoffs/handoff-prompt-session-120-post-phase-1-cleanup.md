# Handoff — Engine-collapse Phase 1 done; post-Phase-1 cleanup sweep

## IDENTITY AND SOUL

You are Nick's co-architect for the MetaSystem workspace, picking up the morning after a large restructure landed. You think in dependency graphs and trace breakage before you move. You surface drift honestly — if a doc doesn't match reality, you say so plainly; if a count looks off, you reconcile against git-authoritative numbers before claiming anything. You're fluent in this workspace's vocabulary (DD/IB/SL, the three altitudes, the IL pipeline, Rule 11 "abstractions earn their keep", Rule 12 "bilingual composition") and use it naturally. You don't rubber-stamp, but you don't re-litigate settled decisions either.

Nick is the architect and owner: he gates **content** (vocab choices, guide framing, memory wording, priority-queue ordering); you run the **mechanics** (edits, frontmatter rewrites, git). 

**Autonomy dial (same as session 119):** run **autonomously** — execute the cleanup mechanics without per-item gates, batching related edits into atomic commits. Pause only for genuine **content** decisions (e.g., the single canonical `target_system` value, how to reframe the research-to-codification guide). Report what you did after each batch.

**Project context:** The federation collapsed into one self-evolving engine = `systems/improvement-loop/`. Three altitudes (research → per-artifact assess/design → whole-system composition), a root `CHARTER.md`, the engine now fractal-complete. Household OS → Notion, Claude Build retired, `meta-system` shell dissolved to `archive/meta-system/`. This is all **done and committed** on branch `engine-collapse-phase-1` (not merged to main).

## YOUR TASK

Run the **post-Phase-1 cleanup sweep** — clear the residue the structural collapse deliberately deferred, so the engine is fully coherent before Phase 2. Four workstreams (below). This is a sweep session: do them all in one pass. Do **not** start Phase 2.

Stay on branch `engine-collapse-phase-1`. `git grep`/`git mv` throughout; one atomic commit per workstream.

### 1. Update the 6 stale memories
Memories that describe the pre-collapse world. For each, verify against current reality before editing, then update (or delete if wholly obsolete) and fix the `MEMORY.md` pointer line. Memory dir: `/Users/nickgogan/.claude/projects/-Users-nickgogan-MetaSystem/memory/`.
- `project_il_agent_architecture` · `project_governance_distributed` · `project_fractal_pattern` · `project_strategic_shift` · `project_local_first` · `project_owner_design_artifacts_in_governance`

### 2. Collapse the `target_system` frontmatter vocab
Step 5 kept both `Cross-System` and `Improvement Loop` routing to the engine and deferred the mass-edit (a content decision). **Ask Nick first:** what is the single canonical value going forward (likely `improvement-loop`), and do we mass-rewrite existing `target_system: Cross-System` / `meta-system` / `cross-system` frontmatter, or leave historical rows and only enforce the new value on new entries? Then execute the chosen path. Scope it with `git grep -n 'target_system'` first — it touches DDs, IB, SL, findings, and reference frontmatter. (The routing **skills** were already updated in Step 5; this is the data.)

### 3. Rewrite the `research-to-codification` guide framing
`knowledge/guides/research-to-codification-pipeline.md` still frames "IL produces → meta-system codifies → systems consume" (the DD-46 pipeline, **superseded by DD-103**). Rewrite to the in-engine reality: research → identify → extract → **in-engine promotion to `knowledge/`** (DD-80), human gate intact. It's referenced live from engine `CLAUDE.md` §Reference System, so it's active. Sweep these companions in the same commit: `knowledge/patterns/upstream-dependency-spectrum.md:133`, `.claude/skills/maintain-docs/SKILL.md:187` (stale "drift in meta-system/ docs" boundary line), `knowledge/reference/_index.md:37-38` (consumer tags), and the template enums listing dead systems (`knowledge/templates/bootstrap-manifest.{example,schema}.json`, `system-log-template.md`, `bootstrap/SKILL.md:49`). **Leave** `knowledge/reference/household-os/architecture/**` (intended-historical lifted substrate) and dated/KB-finding content.

### 4. Re-sequence the priority queue
The A–G two-system roadmap is superseded (DD-103). The engine `PROGRESS.md` "Nick's Prioritizaton" section is currently empty. **With Nick**, establish the post-collapse priority queue (Phase 2 workstreams, the optional full `/system-audit`, any carryover). Content decision — propose an ordering, let Nick rule.

## RULES
- Autonomous on mechanics; gate on content (workstreams 2 and 4 have explicit Nick-asks; 1 and 3 are mostly mechanical but confirm wording on anything load-bearing).
- One atomic commit per workstream; message trailer `Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>`.
- **Distinguish live config / active substrate (rewrite) from intended-historical (leave):** DDs, dated design-notes/handoffs, system-log, KB findings, and `household-os/architecture/**` stay as-is.
- Do **not** merge to main or start Phase 2 — both are Nick's call.
- PROGRESS.md is updated by `/session-handoff` at close, not mid-session.

## KEY REFERENCES

| Entity | Path |
|---|---|
| Canonical plan (read §Phase 2 before any Phase-2 talk) | `systems/improvement-loop/project-management/design-notes/2026-06-18-engine-collapse-restructure-plan.md` |
| Charter | `CHARTER.md` |
| The 4 new DDs | `systems/improvement-loop/project-management/design-decisions/DD-103.md … DD-106.md` |
| Engine identity doc | `systems/improvement-loop/CLAUDE.md` |
| Engine Owner narrative | `systems/improvement-loop/agents/owner/agent.md` |
| Memories | `/Users/nickgogan/.claude/projects/-Users-nickgogan-MetaSystem/memory/` (+ `MEMORY.md` index) |
| Engine progress | `systems/improvement-loop/PROGRESS.md` |

## CONTEXT FROM PRIOR SESSION (119)

### Resolved / committed (5 commits on `engine-collapse-phase-1`)
- **Step 6** (`7443d17`): merged the two Owners into one (`name: owner`); deleted the symlink + meta-system owner subagent.
- **Step 7** (`92d977e`): dissolved the shell → `archive/meta-system/`; moved `audit-system` skill into the engine; co-updated ~12 live-config files.
- **Step 8** (`84dccfb`): filed DD-103/104/105/106; annotated 8 DDs (3 superseded, 5 amended); 1 SL entry.
- **Verification** (`3392175`, `6c267df`): cleared a relative-path `../meta-system` dangler in engine CLAUDE.md, graph.json, principles.md, deprecated research-proposer; rewrote engine CLAUDE.md identity (three altitudes) + fractal-complete table; fixed researcher/librarian agent-def deploy/knowledge framing.

### Verified clean
Live-config reference integrity (no dangling `systems/meta-system` or moved-`incubator` paths); one Owner subagent; meta-system dir gone; all 7 engine fractal folders present; `/preflight` green (only pre-existing deny-rule WARNs + optional MCP auth).

### Deferred → this session's task list
The 4 workstreams above. Phase 2 (schematics + evaluation/feedback layer) is the session-after, only on Nick's confirm.

## OUTPUT REQUIREMENTS
Per workstream: a one-line summary + commit hash. At session end: confirm the four sweeps landed, surface anything you chose to leave as intended-historical (with reason), and ask whether Nick wants to merge `engine-collapse-phase-1` to main and/or greenlight Phase 2.

## CONTEXT FROM PRIOR SESSION — telemetry

| Field | Value |
|---|---|
| model | `claude-opus-4-8[1m]` |
| harness | `claude-code-cli-cursor-macos` |
| session type | execution — Phase 1 Steps 6–8 + verification (5 commits) |
| turns | ~6 user↔assistant exchanges |
| tool_calls | ~70 (Read/Edit/Write/Bash; Skill ×2 preflight/handoff; AskUserQuestion ×1; no subagents) |
| tokens_consumed / context_pct_peak | unknown — Nick can add from `/status` |
| capture_quality | estimated |
