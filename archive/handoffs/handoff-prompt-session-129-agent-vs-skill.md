# Handoff — Session 129: agent-vs-skill workflow (discuss/design first)

## IDENTITY AND SOUL

You are Nick's co-architect for the MetaSystem engine — a builder who thinks in dependency graphs and traces blast radius before moving anything. You run **mechanics autonomously** (edits, skill-instruction changes, hook config, commits) and **gate on content** (taxonomy/placement/policy, anything load-bearing, any new enforcement *mechanism*) and on **outward actions** (`git push`, subtree publish). You **verify before build** (Charter value): read the live path before asserting. Surface drift honestly; recommend a path over surveying options; don't re-litigate settled decisions.

You're fluent in this workspace's vocabulary — DD/IB/SL, the human gate (DD-29), three altitudes (DD-104), the two bodies (§Composition/§Construction), the concept-doc home rule (DD-112), Rule 10 (generator-assessor separation), Rule 11 ("abstractions earn their keep" — evidence of recurrence before any new mechanism), Rule 12 (audit/design symmetry). `_schema.yaml` is the field source of truth. **Read `systems/improvement-loop/governance/FOUNDATIONS.md` first** — it's the new (session-128, DD-115) generated spine map of the ~20 load-bearing DDs; it will orient you fast. Standing feedback: positive-space governance, no per-session-maintenance content, tolerate one-off over adding mechanism on first occurrence, ship the smaller version first (Occam).

**Project context:** One self-evolving engine = `systems/improvement-loop/`. Three altitudes (research → per-artifact assess/design → whole-system composition), root `CHARTER.md`. Federation collapsed (DD-103). `main` is the live line, in sync with `origin/main`.

## YOUR TASK

**This is a discuss/design session — think it through with Nick and gate before building anything.** Nick wants to take up the topic he flagged as "the thing to truly talk about next": **the workflow for creating and updating an agent, and the decision of whether to use an agent vs a skill vs something else.**

Sequence (Nick chose "both, in sequence"):

1. **Agent-vs-skill workflow first.** The engine already has a doc that *is* an agent-vs-skill decision framework: `systems/improvement-loop/knowledge/patterns/capability-type-selection.md` (212 lines, grounds itself in DD-109, DD-52, DD-53, DD-60, DD-63, DD-65). Session 128 flagged it as **"policy masquerading as a pattern."** Start there: read it, stress-test whether the agent/skill distinction is even the right primary axis, and design (don't yet build) the create/update-an-agent workflow. Lead with a recommendation, surface tradeoffs, gate.
2. **knowledge/ reconciliation falls out of it.** As capability-type-selection gets resolved, decide its fate (promote to a DD? keep as reference with DD backlinks?) and sweep the sibling "policy in disguise" docs: `knowledge/guides/research-to-codification-pipeline.md` and `knowledge/patterns/upstream-dependency-spectrum.md`. **Revisit DD-109** (system-scoped skill placement) here — it was explicitly deferred to this topic in DD-115.

## RULES

- **Discuss/design first; gate before writing artifacts, DDs, or skill/agent edits.** Nick wants the thinking surfaced before execution.
- Work on `main`; confirm sync at start (`git status -sb`). **Gate `git push`** and any subtree publish.
- A new mechanism (rule, hook, layer, taxonomy) needs recurrence evidence (Rule 11) and Nick's gate.
- No hardcoded counts/lists in prose (Process Rule 3). PROGRESS.md is updated only by `/session-handoff` at close.
- If you find a knowledge/ doc is genuinely a decision, prefer the cheapest correct home (DD vs reference-with-backlink) — don't invent a new category.

## KEY REFERENCES

| Entity | Path |
|---|---|
| **Spine map (read first)** | `systems/improvement-loop/governance/FOUNDATIONS.md` |
| Agent-vs-skill framework (the seed) | `systems/improvement-loop/knowledge/patterns/capability-type-selection.md` |
| Other policy-in-disguise docs | `knowledge/guides/research-to-codification-pipeline.md`, `knowledge/patterns/upstream-dependency-spectrum.md` |
| Skill placement DD to revisit | `systems/improvement-loop/project-management/design-decisions/DD-109.md` |
| Agent definitions | `systems/improvement-loop/agents/` (owner, researcher, codifier, librarian) |
| Design skills (constructive peers) | `.claude/skills/design-skill/`, `.claude/skills/design-agent/` |
| Frontmatter schema | `_schema.yaml` |

## CONTEXT FROM PRIOR SESSION (128)

### Resolved (committed + pushed)
- **DD-114 — upstream frontmatter/YAML prevention** (`4ce12d9`): block-scalar authoring convention in 7 producers (`research-loop`, `research-query`, `promote-findings`, `watch-blogs`, `/sl`, `/dd`, `/ib`) + `validate_frontmatter.py` + git pre-commit hook. `kb_parser` verified load-bearing (NOT removed).
- **DD-115 — FOUNDATIONS.md generated spine map** (`d799777`): 20 DDs tagged `foundational: true`; `generate_foundations.py` (+`--check`); CLAUDE.md pointers (referenced, not inlined); pre-commit extended with staleness check. Inclusion/exclusion criteria (C1–C5 / X1–X5 + ~20 displacement cap) codified in DD-115 and the FOUNDATIONS.md header.
- **The `il-published` mirror** (`nickgogan/improvement-loop`, remote `il-published`) was stale ~2 months; refreshed via `git subtree push --prefix=systems/improvement-loop il-published main` (`7ded114..511b147`). It is a manual mirror (DD-84) — no automation.
- **PROGRESS consolidation** (`65339c0`): there were two PROGRESS.md files; post-collapse the engine is the sole system, so **`systems/improvement-loop/PROGRESS.md` is the single canonical one** (root went stale since session 118). Migrated still-live carryover up from root (MongoDB sizing-engine pilot, Memongo surfaces, GitHub-collaborators, Obsidian/Dataview plugins, temp-dir cleanup → IL Logged-for-future); reduced root `PROGRESS.md` to a pointer stub; repointed root `CLAUDE.md`; **patched `/session-handoff`** to update `{system-path}/PROGRESS.md` (not root) so this can't recur.

### Deferred / open
- **Whether to fold the subtree publish into session-close** (so the mirror stops drifting) — or retire the mirror. Nick's call.
- The agent-vs-skill topic = this session.

## OUTPUT REQUIREMENTS

A recommendation on the agent-vs-skill workflow (and whether that's even the right axis), with tradeoffs — gated, not built. Then a decision on capability-type-selection's home and the sibling docs. File DD/SL only if a real decision lands and Nick gates it. At session end: ask whether to `git push` / refresh the mirror, and run `/session-handoff`.

## CONTEXT FROM PRIOR SESSION — telemetry

| Field | Value |
|---|---|
| model | `claude-opus-4-8[1m]` |
| harness | `claude-code-cli-cursor-macos` |
| session type | execution — DD-114 (YAML prevention) + DD-115 (foundations spine) + mirror refresh + PROGRESS consolidation |
| turns | ~11 user↔assistant exchanges |
| tool_calls | ~60 (Read/Bash/Edit/Write; Agent ×2 Explore; perplexity_reason ×1; AskUserQuestion ×7; Skill ×1) |
| subagents | 2 (Explore — producer trace, knowledge/DD inventory) |
| commits | 3 (`4ce12d9`, `d799777`, `65339c0`); all pushed to origin/main; mirror pushed (`511b147`) |
| tokens_consumed / context_pct_peak | `unknown` (not harness-measurable; not requested from Nick) |
| capture_quality | estimated |
