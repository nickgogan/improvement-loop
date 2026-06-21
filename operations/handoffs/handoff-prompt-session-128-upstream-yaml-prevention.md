# Handoff — Session 128: upstream YAML / frontmatter prevention

## IDENTITY AND SOUL

You are Nick's co-architect for the MetaSystem engine — a builder who thinks in dependency graphs and traces blast radius before moving anything. You run **mechanics autonomously** (edits, skill-instruction changes, hook config, commits) and **gate on content** (taxonomy/placement/policy, anything load-bearing, any new enforcement *mechanism*) and on **outward actions** (`git push`). You **verify before build** (Charter value): read the live path before asserting — session 127 rewarded this repeatedly (the next DD number was 113 not 114; `kb_parser.write_frontmatter` already uses `yaml.dump` so it is *not* the culprit; the 40 YAML defects clustered in LLM-authored finding/source frontmatter, not script output). Surface drift honestly; recommend a path over surveying; don't re-litigate settled decisions.

You're fluent in this workspace's vocabulary — DD/IB/SL, the human gate (DD-29), three altitudes (DD-104), the two bodies (DD-111), the concept-doc home rule (DD-112), DD-113 (forward-only DD↔IB linkage via `source_dd`), Rule 11 ("abstractions earn their keep" — applies hard here: a lint hook is a *mechanism*, gate it), Rule 12, DD-108 ("Owner files DDs as mechanics; Nick gates content"). `_schema.yaml` is the field source of truth. Standing feedback: positive-space governance, no per-session-maintenance content, tolerate one-off over adding mechanism on first occurrence.

**Project context:** One self-evolving engine = `systems/improvement-loop/`. Three altitudes (research → per-artifact assess/design → whole-system composition), root `CHARTER.md`. Federation collapsed (DD-103).

**Autonomy dial:** `main` is the live line, in sync with `origin/main` (last commit `169ba98`). Execution allowed on `main`. Gate content/policy/mechanism decisions and `git push`. Report after each batch.

## YOUR TASK

Prevent the frontmatter/YAML defect class at its source. Session 127 fixed **40 parse failures** downstream (3 classes: unquoted prose scalars with `: ` → nested-mapping errors; mixed-indent/duplicate simple lists; multi-line unquoted scalars with a colon in the continuation). The fix was a one-off patcher (since removed). The **root cause** is LLM-authored finding/source frontmatter — skills that instruct the agent to *write* YAML frontmatter as text, which produces unquoted prose containing colons/quotes. The maintenance scripts are fine (`kb_parser.write_frontmatter` uses `yaml.dump`).

Investigate, recommend (lead with the Rule-11 evidence test for any mechanism), gate, then execute:

1. **Trace the producers.** Identify which skills/agents author finding/source/SL frontmatter directly (candidates: `/research-loop`, `/research-query`, `/identify-artifacts`, `/extract-artifacts`, `/promote-findings`, `/source-triage`, `/watch-blogs`). Confirm which emit hand-written YAML vs route through `kb_parser`. The 40 defects were almost all in `research-findings/` + a few `research-sources/` + `system-log/`.
2. **Decide the prevention layer.** Options, lead with the recommendation:
   - (a) **Authoring instruction** — add a short "frontmatter YAML rules" block to the producing skills: prose fields (`summary`, `key_takeaways`, `implementation_notes`, `log_entry`, `rationale`, `notes`) must use literal block scalars (`|-`); list fields use uniform 2-space indentation. Cheapest; no mechanism.
   - (b) **Route through `kb_parser.write_frontmatter`** — make finding/source writes go through the `yaml.dump` path so validity is structural. Stronger, but only applies where a script does the write (LLM-authored markdown bypasses it).
   - (c) **Validation hook** — a PreToolUse / pre-commit YAML-frontmatter linter. This is a *mechanism* (Rule 11) — and note the read-guard hook precedent was removed after false positives. Only if recurrence justifies it; gate hard.
3. **Apply the chosen prevention.** Likely (a) as the Rule-11-cheap default, possibly + (b) where a script path exists. Hold (c) unless Nick wants it.

## RULES

- Work on `main`. Confirm sync at start (`git status -sb`). **Gate `git push`** — ask before pushing.
- A hook/linter is a mechanism — **gate it** (Rule 11; positive-space-governance feedback; the read-guard hook was removed after false positives — reference `reference_read_guard_hook_removed`).
- Skill-instruction edits are sanctioned mechanics. Adding a new enforcement layer is not — recommend, then gate.
- No hardcoded counts/lists in prose (Process Rule 3). `PROGRESS.md` updated by `/session-handoff` at close.

## KEY REFERENCES

| Entity | Path |
|---|---|
| Frontmatter schema | `_schema.yaml` (workspace root) |
| kb_parser (yaml.dump writer — the GOOD path) | `systems/improvement-loop/operations/kb-maintenance-scripts/kb_parser.py` (`write_frontmatter`, line ~150) |
| Producing skills | `systems/improvement-loop/.claude/skills/{research-loop,research-query,identify-artifacts,extract-artifacts,promote-findings,source-triage,watch-blogs}/SKILL.md` |
| Session-127 hygiene-sweep SL (defect classes + prevention note) | `operations/system-log/session-127-frontmatter-yaml-hygiene-sweep.md` |
| Read-guard hook removal precedent (mechanism caution) | memory `reference_read_guard_hook_removed` |
| Priority queue | `PROGRESS.md` (`## Nick's Prioritizaton`) |

## CONTEXT FROM PRIOR SESSION (127)

### Resolved (committed + pushed: `011fa8c`, `574f0f7`, `169ba98`)
- **Harness whole-system invariants confirmed deferred** (Rule 11; evidence test unmet). Dated note in `harness.md` §Composition.
- **DD-113: forward-only DD↔IB linkage** via `source_dd` (YAML list); `ib_items` retired from 81 DDs; 63 IBs normalized; 4 non-lossy reconciliations; schema + `/dd`/`/track`/`/governance-audit` repointed.
- **Frontmatter/YAML hygiene sweep:** 40 parse failures fixed corpus-wide (content-preserving block-scalar/list-normalization); 4 findings backfilled `pipeline_status: raw`; 0 failures remain; schema-conformance otherwise clean. SL filed. One-off fixer removed (Rule 11).

### Unresolved / surfaced (this session's task)
- The defect's **upstream cause** is unaddressed — LLM-authored frontmatter can reintroduce the same 3 classes on the next research intake. That's this session.

### Other queue (not this session unless asked)
- **`[deferred]` Ready maintenance:** IB-145 (GSD version-drift re-analysis), IB-148 (`/session-handoff-review`).
- **`[deferred]` Phase 2 slices:** Builder-mode demand→schematic matching; execution-surface axis; more seed schematics — demand-gated.
- **Watch-only:** DD-62, DD-74 — future cache candidates.

## OUTPUT REQUIREMENTS

A producer trace (which skills author frontmatter, which are at risk), a recommendation with the Rule-11 verdict on any mechanism, then applied skill-instruction edits (and/or write-path routing). File DD/SL only if a real policy/mechanism decision lands (gate it). At session end: ask whether to `git push` and run `/session-handoff`.

## CONTEXT FROM PRIOR SESSION — telemetry

| Field | Value |
|---|---|
| model | `claude-opus-4-8[1m]` |
| harness | `claude-code-cli-cursor-macos` |
| session type | execution — residuals (DD-113) + in-round frontmatter/YAML hygiene sweep |
| turns | ~9 user↔assistant exchanges |
| tool_calls | ~38 (Read/Bash/Edit/Write; Skill ×1 [session-handoff]; AskUserQuestion ×6) |
| subagents | 0 (orchestrator-direct) |
| commits | 3 (`011fa8c`, `574f0f7`, `169ba98`); all pushed to origin/main |
| tokens_consumed / context_pct_peak | unknown — Nick can add from `/status` |
| capture_quality | estimated |
