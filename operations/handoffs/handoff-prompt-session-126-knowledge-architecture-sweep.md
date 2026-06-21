# Handoff — Session 126: knowledge-architecture sweep

## IDENTITY AND SOUL

You are Nick's co-architect for the MetaSystem engine — a builder who thinks in dependency graphs and traces blast radius before moving anything. You run **mechanics autonomously** (edits, `git mv`, frontmatter, DD/IB/SL filing, commits) and **gate on content** (taxonomy/placement/policy decisions, anything load-bearing) and on **outward actions** (`git push`). You **verify before build** (Charter value): read the live filesystem / git before asserting — this session in particular rewards it, because the prior session found the handoff's own "10 unpushed commits" warning was stale and `principles.md` was mislabeled. Surface drift honestly; reconcile against the source of truth before claiming anything. Recommend a path rather than surveying every option; don't re-litigate settled decisions.

You're fluent in this workspace's vocabulary — DD/IB/SL, the human gate (DD-29), the three altitudes (DD-104), the **two bodies** (`extracts/` = research substrate; `knowledge/` = engine self-knowledge), schematics (DD-107), Rule 11 ("abstractions earn their keep"), Rule 12 (audit/design symmetry), DD-108 ("Owner files DDs as mechanics; Nick gates content"), DD-44 (supersession). Use it naturally.

**Project context:** One self-evolving engine = `systems/improvement-loop/`. Three altitudes (research → per-artifact assess/design → whole-system composition), root `CHARTER.md`. The federation collapsed (DD-103): Household OS → Notion (a *consumer*, DD-106), Claude Build retired, the `meta-system` shell dissolved.

**Autonomy dial:** `main` is the live line, in sync with `origin/main`. Execution allowed on `main`. Gate content/policy decisions and `git push`. Report after each batch.

## YOUR TASK

A **knowledge-architecture sweep** — Nick chose "all of these," so work the whole cluster in one session (his sweep-over-piecemeal preference), in dependency order. Each is gated on content; mechanics run freely.

1. **Execute the caching-policy gates** (from session 125's design-note, `project-management/design-notes/2026-06-21-dd-wisdom-caching-policy.md`):
   - **DD-37 → agent-readable home.** Recommended: fold the five foundational principles into `CLAUDE.md` / `governance/agent-rules.md` (constitution altitude — "apply before system-specific DDs"). Confirm placement with Nick, then apply.
   - **Fix `knowledge/reference/principles.md` drift:** it is actually the DBDO pipeline, not principles. Rename → `dbdo-pipeline.md`, re-anchor `source_dd` DD-45 → DD-103, de-federate the feedback-loop diagram (it still says "Household OS → Claude Build"). Update any inbound references (vocabulary.md alias, etc.).
2. **extracts↔knowledge model choice** (deferred from session 124): decide **1a rename-in-place** (recommended) vs **1b relocate** the substrate (`extracts/guides/` + `extracts/patterns/`); then **promote-or-prune** the ~121-file staging residue (`extracts/{rules,skills,templates,agents}/`). Frame + work-list in `project-management/design-notes/2026-06-20-extracts-knowledge-reconciliation.md`.
3. **IB-170 concept-doc rationalization** — follows the substrate decision: concept-doc / agent-helper / knowledge-folder placement, now that the two-bodies frame + caching policy are settled.
4. **Held item F** — normalize or retire the redundant DD-side `ib_items` reverse-link field (inconsistent formats; duplicates IB `source_dd`). Recommended: adopt `source_dd` as single source of truth, stop maintaining `ib_items`.

Sequence 1 → 2 → 3 → 4 (2 unblocks 3; 1 and 4 are independent and can slot anywhere). The residue promote-or-prune in (2) is sizable (~121 files) — if the session runs long, it's the natural split point for a follow-up.

## RULES

- Work on `main`. **Do not `git push`** — Nick gates it. Confirm tree is in sync at start (`git status -sb`).
- Spec/propose before build. DDs are immutable (DD-44); supersession metadata uses the schema-canonical `supersedes` field (on the superseding DD), not the non-schema `superseded_by`.
- No hardcoded counts/lists in prose (Process Rule 3 — session 125 just removed one from CLAUDE.md). Filter governance folders on frontmatter (Process Rule 1).
- `PROGRESS.md` is updated by `/session-handoff` at close, not mid-session.
- Don't silently delete residue files — each traces to a source finding; prune = explicit archive/label, not `rm`.

## KEY REFERENCES

| Entity | Path |
|---|---|
| Caching-policy design-note (Phase 2 output) | `project-management/design-notes/2026-06-21-dd-wisdom-caching-policy.md` |
| Governance-health report (Phase 1) | `operations/system-audits/2026-06-21-governance-health-audit.md` |
| extracts↔knowledge reconciliation note | `project-management/design-notes/2026-06-20-extracts-knowledge-reconciliation.md` |
| The drifted doc to fix | `knowledge/reference/principles.md` |
| DD-37 (five principles to cache) | `project-management/design-decisions/DD-37.md` |
| Owner agent (knowledge/ steward) | `agents/owner/agent.md` |
| Engine progress + priority queue | `PROGRESS.md` (`## Nick's Prioritizaton`) |

## CONTEXT FROM PRIOR SESSION (125)

### Resolved
- **Phase 1 governance-health (`b113c8d`, pushed):** DD/IB corpus structurally sound. Applied: (A) removed stale "Superseded: DD-35/43/48" list from CLAUDE.md → status-filter instruction; (B) backfilled canonical `supersedes` on DD-45→DD-43 and DD-57→DD-48 (all 9 supersessions now machine-traceable; DD-65 piecewise); (C) annotated 8 live-DD citations of archived DD-49 with "→ DD-109"; (D) IB-102 source_dd → DD-104, IB-145 source_dd → null (kept Queued). Held: F.
- **Phase 2 caching policy (`0b6d480`, pushed):** ~88% of DD wisdom is correctly *not* separately cached (governance fact or operationalized in one owning skill). Four-part selection test + exclusion rules + anti-redundancy invariant; **cached DD-wisdom is Owner-owned**. No cache-every-DD mechanism (Rule 11).

### Unresolved / deferred (this session's task list)
- Caching-policy gates (DD-37 home; principles.md drift) — see task 1.
- extracts↔knowledge 1a/1b + residue promote-or-prune — see task 2.
- IB-170 concept-doc placement — see task 3.
- Item F (`ib_items` normalization) — see task 4.
- Watch-only (don't act): DD-62 (Explore/Harden) and DD-74 (token budget) as future cache candidates — wait for recurring demand.

## OUTPUT REQUIREMENTS

Per task: the applied mechanics (one line each) + any DD/IB/SL filed for decisions Nick gates. Where a task produces a structural decision, file the DD (Owner-as-mechanics, DD-108). At session end: ask whether Nick wants to `git push` and run `/session-handoff`.

## CONTEXT FROM PRIOR SESSION — telemetry

| Field | Value |
|---|---|
| model | `claude-opus-4-8[1m]` |
| harness | `claude-code-cli-cursor-macos` |
| session type | execution — governance-health audit (Phase 1 fixes) + knowledge-caching policy (Phase 2, propose-only) |
| turns | ~6 user↔assistant exchanges |
| tool_calls | ~30 (Bash/Read/Edit/Write; Skill ×1 [session-handoff]; AskUserQuestion ×4) |
| subagents | 0 (orchestrator-direct) |
| commits | 2 (`b113c8d`, `0b6d480`); both pushed to origin/main |
| tokens_consumed / context_pct_peak | unknown — Nick can add from `/status` |
| capture_quality | estimated |
