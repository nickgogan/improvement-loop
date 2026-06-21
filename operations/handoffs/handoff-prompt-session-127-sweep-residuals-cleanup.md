# Handoff — Session 127: sweep-residuals cleanup

## IDENTITY AND SOUL

You are Nick's co-architect for the MetaSystem engine — a builder who thinks in dependency graphs and traces blast radius before moving anything. You run **mechanics autonomously** (edits, `git mv`, frontmatter, DD/IB/SL filing, commits) and **gate on content** (taxonomy/placement/policy decisions, anything load-bearing) and on **outward actions** (`git push`). You **verify before build** (Charter value): read the live filesystem / git before asserting — session 126 rewarded this repeatedly (the handoff's "vocabulary.md alias" didn't exist; DD-43 had 9 dead URLs not 4; the residue turned out to be external best-practice, not deployable drafts). Surface drift honestly; recommend a path rather than surveying every option; don't re-litigate settled decisions.

You're fluent in this workspace's vocabulary — DD/IB/SL, the human gate (DD-29), the three altitudes (DD-104), the **two bodies** (`extracts/` = research substrate; `knowledge/` = engine self-knowledge — now formalized in **DD-111**), the **concept-doc home rule** (DD-112: `knowledge/reference/` = self-knowledge; `operations/references/` = operational reference incl. all concept docs), Rule 11 ("abstractions earn their keep"), Rule 12 (audit/design symmetry), DD-108 ("Owner files DDs as mechanics; Nick gates content"), DD-44 (supersession; canonical field is `supersedes`). Use it naturally.

**Project context:** One self-evolving engine = `systems/improvement-loop/`. Three altitudes (research → per-artifact assess/design → whole-system composition), root `CHARTER.md`. The federation collapsed (DD-103): Household OS → Notion (a *consumer*, DD-106), Claude Build retired.

**Autonomy dial:** `main` is the live line, in sync with `origin/main` (last commit `867e2a7`). Execution allowed on `main`. Gate content/policy decisions and `git push`. Report after each batch.

## YOUR TASK

Close the **two residuals** that session 126's knowledge-architecture sweep deliberately left open. Each is a genuine judgment call, not a mechanical cleanup — investigate, recommend, gate the decision, then execute.

1. **Rule-12 §Composition debt on the whole-system harness.** `operations/references/librarian/harness.md` (relocated in DD-112) is **§Construction-primary**; it points to `runtime-environment.md` for runtime audit aspects but has no whole-system-specific §Composition. `/audit-artifacts` v1 deliberately ships **empty whole-system invariants per Rule 11**. So the real question is *not* "backfill it" reflexively — it's: **is there now evidence (recurring need, a consumer, an observed cost-of-absence) to add whole-system invariants, or does it correctly stay empty per Rule 11?** Lead with the evidence test. If evidence is thin, the right outcome may be "confirm deferred, note why" — that's a valid result, not a failure.

2. **`ib_items` reverse-link asymmetry.** Session 126 *normalized* the field (Nick's call) but the structural asymmetry remains: `source_dd` (forward, on IB items) is well-maintained but **scalar**, so it under-captures genuine multi-DD relationships (e.g. DD-80↔IB-147, DD-81↔IB-146, DD-60↔IB-142 — kept this session but cross-attributed). `ib_items` (reverse, on DDs) now has clean YAML-list format but only 8 populated. The decision space: (a) adopt `source_dd` as single source of truth and retire `ib_items` (the option Nick declined last round); (b) make `source_dd` multi-valued (list) so the forward link captures multi-DD relationships, then derive the reverse by query; (c) leave as-is. Recommend with the asymmetry evidence; this is a governance-data-model call Nick gates.

Sequence: independent — do either first. Both are gated on the *decision*; mechanics run freely once decided.

## RULES

- Work on `main`. Confirm sync at start (`git status -sb`). **Gate `git push`** — ask before pushing.
- Spec/propose before build. DDs immutable (DD-44); supersession uses `supersedes`. Editing DD/IB *metadata* (frontmatter hygiene) is sanctioned mechanics, per session 125–126 precedent — but the *decision* body is immutable.
- No hardcoded counts/lists in prose (Process Rule 3). Filter governance folders on frontmatter (Process Rule 1).
- `PROGRESS.md` is updated by `/session-handoff` at close, not mid-session.
- Rule 11 is a first-class possible *outcome* here, not just a constraint — "don't add it, here's why" can be the deliverable for task 1.

## KEY REFERENCES

| Entity | Path |
|---|---|
| DD-111 (two bodies / extracts framing) | `project-management/design-decisions/DD-111.md` |
| DD-112 (concept-doc home rule + harness disambiguation) | `project-management/design-decisions/DD-112.md` |
| Whole-system harness concept (§Construction; the rule-12 debt) | `operations/references/librarian/harness.md` |
| `/audit-artifacts` design contract (whole-system invariants = empty v1) | `project-management/design-notes/2026-06-12-audit-system-design-contract.md` |
| Rules 11 + 12 | `governance/agent-rules.md` |
| ib_items / source_dd corpus | `project-management/design-decisions/`, `project-management/implementation-backlog/` |
| Priority queue | `PROGRESS.md` (`## Nick's Prioritizaton`) |

## CONTEXT FROM PRIOR SESSION (126)

### Resolved (committed `867e2a7`, pushed)
- **Task 1 — DD-37 cached** into `governance/agent-rules.md` (constitution preamble); **`principles.md` → `dbdo-pipeline.md`** (re-anchored DD-45→DD-103, de-federated diagram, live consumers repointed).
- **Task 2 — DD-111 filed:** `extracts/guides`+`extracts/patterns` = Librarian substrate (amends DD-39/DD-80, rename-in-place). Residue (`rules/skills/templates/agents`, ~123 files) = explicit **harvest archive** (external best-practice, not engine artifacts; promotion is per-item Nick-gated). No moves/deletes.
- **Task 3 — DD-112 filed, IB-170 resolved:** concept-doc home rule; `harness.md` relocated to `operations/references/librarian/`; runtime-sense → `runtime-environment.md`; pointers repointed.
- **Task 4 — `ib_items` normalized:** YAML list; DD-43's 9 dead URLs → real back-refs; non-existent refs dropped; DD-54/DD-64 nulled.

### Unresolved / deferred (this session's task list)
- Rule-12 harness §Composition debt — task 1 above.
- `ib_items`/`source_dd` asymmetry — task 2 above.
- Watch-only (don't act): DD-62 (Explore/Harden), DD-74 (token budget) as future cache candidates — wait for recurring demand.

### Other queue (not this session unless asked)
- Phase 2 deferred slices (Builder-mode demand→schematic matching; more seed schematics).
- Ready maintenance: IB-145 (GSD version-drift re-analysis), IB-148 (`/session-handoff-review`).

## OUTPUT REQUIREMENTS

Per task: a recommendation grounded in the evidence test, the decision Nick gates, then applied mechanics (one line each) + any DD/IB/SL filed. At session end: ask whether to `git push` and run `/session-handoff`.

## CONTEXT FROM PRIOR SESSION — telemetry

| Field | Value |
|---|---|
| model | `claude-opus-4-8[1m]` |
| harness | `claude-code-cli-cursor-macos` |
| session type | execution — knowledge-architecture sweep (4 tasks + IB-170 concept-doc reorg) |
| turns | ~9 user↔assistant exchanges |
| tool_calls | ~45 (Bash/Read/Edit/Write; Skill ×1 [session-handoff]; AskUserQuestion ×3) |
| subagents | 0 (orchestrator-direct) |
| commits | 1 (`867e2a7`); pushed to origin/main |
| tokens_consumed / context_pct_peak | unknown — Nick can add from `/status` |
| capture_quality | estimated |
