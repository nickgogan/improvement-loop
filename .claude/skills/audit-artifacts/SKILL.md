---
name: audit-artifacts
description: >-
  Point at a folder; audit whether the agentic system inside it is well-formed.
  Discovers skills, agents, and prompts via shape-based globs, sizes them,
  bin-packs them into parallel Librarian subagents (250k token ceiling each),
  dispatches each artifact to the appropriate IL /assess-* skill, and emits
  three artifacts: a structural manifest, per-artifact findings, and a
  whole-system summary. Read-only on the audited system. The engine's
  top-altitude composition layer over IL's per-artifact assessors. v1 — empty
  whole-system invariants (rule 11); composition only.
user-invocable: true
allowed-tools: Read Glob Skill Agent Write Bash
argument-hint: "<path> [--scope <types>] [--variant <hint>] [--exclude <patterns>] [--include-mocs] [--manifest-only] [--write] [--diff <prior>]"
---

# Audit Artifacts

Whole-system audit. Composes IL's `/assess-skill`, `/assess-agent`, and
`/assess-prompt` over every shape-detectable artifact inside a target folder,
dispatched in parallel via Librarian subagents under a per-subagent token
ceiling.

The intelligence about *what to look for in each artifact* lives in IL — this
skill is composition: discovery, sizing, bin-packing, dispatch, aggregation.

## When to Use This Skill

- Consumer hands you a local path and asks "is the agentic system inside this
  folder well-formed?" or any rephrase ("audit this system", "review this
  harness", "what's the shape of this folder's agentic surface").
- Consumer wants a snapshot of an external system's agentic surface area before
  consuming it as substrate, vendoring it, or imitating its conventions.
- Re-audit cadence: consumer wants to compare a system's current state against
  a prior manifest (`--diff <prior>`).

## When NOT to Use This Skill

- Consumer wants to audit a *single* artifact — redirect to IL `/assess-skill`,
  `/assess-agent`, or `/assess-prompt` directly.
- Consumer wants the IL system itself audited — IL has its own `/system-audit`.
- Consumer wants code-quality, security, or runtime-behavior review — out of
  scope; redirect to `/security-review` or `/code-review`.
- Consumer wants design proposals or remediation — that's the future
  `/design-harness` (rule 10 constructive peer). `/audit-artifacts` reports only.

## What This Skill Does NOT Do

- Does not modify the audited system. Read-only by contract.
- Does not propose remediation. Reports only; constructive work is
  `/design-harness`'s domain.
- Does not audit code logic, security, runtime behavior, or test coverage.
- Does not cross system boundaries via `--recurse` (v1 omits the flag; single
  target only).
- Does not audit IL substrate itself. If the target IS the IL folder, the audit
  still runs against IL's artifacts as a black-box consumer would see them; it
  does not validate IL's internal Contract substrate.

## Cognitive Disposition

Engine Owner — analytical, declarative, plain-English-first, citation-
grounded. Composition layer: the assessor work is delegated to IL. This skill
reports state as discovered, surfaces gaps as gaps (not failures), and avoids
overreach. Rule 11 governs the whole-system invariants section: empty in v1.

## FAILURE SIGNAL

The run has failed (do not pretend otherwise; surface explicitly) if any of:

- The target path doesn't exist or isn't a directory — reject in Step 0.
- Discovery returns zero in-scope artifacts AND the target appears to be a
  fractal-pattern system (suggesting an exclusion misfire). Emit a manifest
  noting the zero count plus a warning that the discovery may be misconfigured.
- A Librarian subagent returns no parseable reports for its bin (not just one
  artifact's report missing — the whole bin's output is unparseable). Record
  the bin as "report-unparseable", preserve raw output, continue with reduced
  coverage, and surface this in the summary's "At a glance" section.
- More than half of the dispatched bins fail to return parseable output. In
  this case, do not emit a misleading whole-system summary; emit only the
  manifest and a report-failure notice.
- A `--write` was requested but the target is not writable; do not silently
  fall back — surface the fallback in the conversation headline.

## Default exclusions

Discovery applies these path-fragment excludes unconditionally (matched against
the artifact's path relative to `<target>`):

- `archive/` — completed/retired work, by convention not load-bearing
- `_tmp/`, `_cache/` — temporary/working/cache directories
- `node_modules/`, `.git/` — dependency and VCS metadata
- `reflections/` — agent-private working context (e.g., `agents/*/reflections/`)

Additional excludes can be passed via `--exclude <comma-separated-patterns>`.
The default set was derived from MetaSystem session 114 evidence; revise via
design-contract update if the empirical exclude set drifts.

## MOC pre-filter for CLAUDE.md

CLAUDE.md files come in two shapes: **agent-disposition CLAUDE.md** (substantive
behavioral context for an LLM running inside that folder) and **MOC CLAUDE.md**
(folder-orientation index pointing to what lives in the subtree, no behavioral
content). Auditing a MOC under `/assess-agent --variant prompt-based` produces
"all guides latent / shape mismatch" — burning a subagent slot for no signal.

Rule-11 trigger met after MetaSystem (session 114, 3 MOCs) + IL (session 115,
3+ confirmed MOCs). Cumulative ≥6 across 2 systems is the recurrence evidence.

**At discovery time**, after the initial glob for `**/CLAUDE.md`, apply the
MOC heuristic to each hit. Skip dispatch and mark as MOC if **either** of:

1. **Frontmatter has `type: "index"`** (or `category: governance` on a CLAUDE.md
   that's clearly an index — these surface as Codifier-emitted MOC catalogs).
2. **Body word count < 100** (excluding frontmatter). A genuine agent-
   disposition CLAUDE.md is rarely shorter than this; a MOC is rarely longer.

A CLAUDE.md that hits **either** condition is recorded in the manifest's
`## Skipped — MOC` block with its path, classification reason, and word count.
It does NOT dispatch to `/assess-agent`. The artifact still appears in the
manifest for transparency.

**Override**: pass `--include-mocs` to suppress the filter and dispatch all
CLAUDE.md regardless. Use when the consumer suspects a MOC is actually load-
bearing behavioral context.

**Trade-off accepted**: the heuristic may suppress the occasional legitimate
short prompt-based-agent CLAUDE.md. Mitigation: the manifest's skipped block
makes the suppression visible, and `--include-mocs` reverses it in one flag.

The heuristic was committed session 115 after IL surfaced 3 confirmed +
3 strongly-suspected MOC latents (the latter under unaudited bin 4 with word
counts 55–78). Per Nick's session-114 ruling: "filter at discovery, or accept
wasted subagent budget. Likely tolerate v1; revisit after IL audit reveals
frequency." IL frequency confirmed; heuristic now committed.

## Paths

| Path | Purpose |
|------|---------|
| `<target>` | Consumer-provided audit root |
| `<target>/operations/artifact-audits/<YYYY-MM-DD>/` | On-disk output destination (if writable) |
| `.claude/agents/librarian.md` (workspace root, `name: librarian`) | Subagent invoked per bin |
| `systems/improvement-loop/.claude/skills/assess-skill/SKILL.md` | Dispatched for skill-shape artifacts |
| `systems/improvement-loop/.claude/skills/assess-agent/SKILL.md` | Dispatched for agent-shape and CLAUDE.md artifacts |
| `systems/improvement-loop/.claude/skills/assess-prompt/SKILL.md` | Dispatched for prompt-shape artifacts |
| `systems/improvement-loop/project-management/design-notes/2026-06-12-audit-system-design-contract.md` | Design contract |

## Procedure

### Step 0: Parse input

1. Required positional: `<path>`. Resolve to absolute. Confirm it exists and is
   a directory; reject with redirect to `/assess-*` if it's a single file.
2. Optional flags:
   - `--scope skills,agents,prompts` — comma-separated subset of shapes to
     discover. Default: all.
   - `--variant prompt-based|harness-based|autonomous` — passthrough variant
     hint to `/assess-agent`. Default: per-artifact inference.
   - `--exclude <comma-separated-patterns>` — additional path-fragment
     excludes layered on top of the default set in §"Default exclusions".
   - `--include-mocs` — suppress the MOC pre-filter (see §"MOC pre-filter
     for CLAUDE.md"). Default: filter is on; CLAUDE.md files with
     `type: "index"` frontmatter OR body word count < 100 are skipped and
     recorded in the manifest's `## Skipped — MOC` block rather than
     dispatched to `/assess-agent`.
   - `--manifest-only` — produce the manifest; skip dispatch + summary.
   - `--write` — persist manifest/findings/summary to
     `<target>/operations/artifact-audits/<date>/`. **Default: off** (conversation-only).
     This default is the G9.I6 mitigation: writes require explicit consumer
     opt-in.
   - `--diff <prior-manifest-path>` — re-audit mode; surface drift against the
     prior manifest in the summary. Implies the consumer has previously run
     with `--write`.
3. Record the parsed input in an `audit_run` block kept in working state.

### Step 1: Discovery

Glob from `<path>` for each shape (respecting `--scope` filter). Do not follow
symlinks beyond the target tree. Apply the default exclude set (see §"Default
exclusions") plus any `--exclude` additions.

| Shape | Glob (relative to `<path>`) | Dispatched to | Variant |
|---|---|---|---|
| Skill | `**/.claude/skills/*/SKILL.md` | `/assess-skill` | n/a |
| Subagent file | `**/.claude/agents/*.md` | `/assess-agent` | per-artifact inference (or `--variant`) |
| Fractal agent | `**/agents/*/agent.md` | `/assess-agent` | per-artifact inference (or `--variant`) |
| CLAUDE.md | `**/CLAUDE.md` | `/assess-agent` `--variant prompt-based` (default), flag ambiguous in manifest | A (prompt-based); `--variant` overrides |
| Standalone prompt | `**/prompts/*.md`, `**/system-prompts/*.md` | `/assess-prompt` | n/a |

After globbing:
1. De-duplicate by resolved absolute path (an artifact reachable via both a
   workspace-root symlink and its fractal home is counted once).
2. **Apply the MOC pre-filter to all CLAUDE.md hits** (unless `--include-mocs`
   was passed). For each CLAUDE.md, read its frontmatter and body. If
   frontmatter has `type: "index"` OR body word count < 100 (excluding
   frontmatter), mark `skipped: true, skip_reason: "MOC"` on the artifact's
   record. Skipped artifacts appear in the manifest's `## Skipped — MOC`
   block but are NOT dispatched in Step 5. See §"MOC pre-filter for CLAUDE.md".
3. For each discovered artifact, record: relative path, shape, dispatched-to
   skill, variant (if applicable), `ambiguous: true|false`, and (for CLAUDE.md
   hits) `skipped: true|false` per step 2.
4. Record structural gaps: if `<path>/agents/` exists but is empty, if
   `<path>/governance/` is absent on a system following fractal pattern, etc.
   These go into a `not_discovered` block in the manifest. Information, not
   findings.

### Step 2: Sizing

For each discovered artifact **that was not skipped in Step 1** (MOC pre-filter):

1. Get word count via `Bash`: `wc -w <artifact-path>` (fast; one shell call per
   batch via `wc -w <list>` is acceptable).
2. Compute `tokens_estimate = words × 1.33`.
3. Compute `subagent_footprint`:
   ```
   subagent_footprint = tokens_estimate
                      + 25_000   (per-artifact overhead: tool calls, reasoning, report output)
                      + substrate_constant
   ```
4. `substrate_constant` is variant-aware:

   | Dispatched-to | Variant | Constant |
   |---|---|---|
   | `/assess-skill` | n/a | 18_000 |
   | `/assess-agent` | A (prompt-based) | 22_000 |
   | `/assess-agent` | B (harness-based) | 32_000 |
   | `/assess-agent` | C (autonomous) | 28_000 |
   | `/assess-prompt` | n/a | 20_000 |

5. Record `subagent_footprint` against each artifact entry.

Note on the substrate model: a Librarian subagent running multiple
`/assess-*` calls in sequence loads substrate once and reuses it for
subsequent calls of the same variant (cache-warm). The flat per-artifact
constant overestimates for same-variant bins — which is safe (we'd rather
under-pack than blow context). v2 may refine.

### Step 3: Bin packing

First-fit-decreasing into bins with a **250,000 token ceiling each**:

1. Initialize an empty list of bins.
2. Sort artifacts descending by `subagent_footprint`.
3. For each artifact, in order:
   - Try to place into the first existing bin where
     `bin.current_total + artifact.subagent_footprint ≤ 250_000`.
   - If no bin has room, create a new bin and place the artifact there.
4. Edge case: if a single artifact's `subagent_footprint > 250_000`, place it
   in its own bin and flag the bin as `oversized: true`. The Librarian
   subagent runs it anyway; user is warned in the summary that the report may
   be degraded by context pressure.

Output of this step: list of bins, each containing 1+ artifacts plus a running
total. Record the bin count for the summary.

### Step 4: Build manifest

Author the manifest as the first output. If the audit is `--manifest-only`,
write it now and stop.

Manifest frontmatter:

```yaml
---
title: "<system-name> audit manifest"
audit_target: "<absolute path>"
audit_date: "YYYY-MM-DD"
audit_version: "v1"
discovery_mode: "auto-detect"   # or "manifest-only"
bin_count: <N>
artifact_count: <N>
---
```

Manifest body sections:

- `## Discovered artifacts` — one table per shape (Skills, Agents, Prompts).
  Columns: Path, Name (frontmatter `name:` if extractable), Variant (if
  applicable), Bin (#), Footprint estimate (k tokens), Dispatched to.
- `## Skipped — MOC` — CLAUDE.md hits suppressed by the MOC pre-filter
  (§"MOC pre-filter for CLAUDE.md"). One row per skip: Path, skip_reason
  (`frontmatter type=index` or `word_count<100` or both), word count. These
  appear in the manifest for transparency but are not dispatched. Omit the
  section entirely if `--include-mocs` was passed or if no MOC hits occurred.
- `## Structural gaps (not discovered)` — bullet list of expected-but-absent
  structural markers (fractal folders, empty agents/, etc).
- `## Ambiguous classifications` — bullet list with the default classification
  and the override flag the user could pass.
- `## Sizing summary` — bin count, total tokens estimated, largest artifact,
  oversized-bin warnings if any. Sizing is computed only over non-skipped
  artifacts.

### Step 5: Dispatch (parallel)

Skip if `--manifest-only`.

Spawn one Librarian subagent per bin, **in parallel** — emit a single message
containing multiple `Agent` tool calls (one per bin). Each spawn:

- `subagent_type: librarian`
- `description`: `"Audit bin <i>/<N> — <K> artifacts"`
- `prompt`: structured payload (see below)

Spawn payload template (use literal sentinel delimiters — heading-based parsing
proved unreliable in session 114 because `/assess-*` reports carry their own
`##` headings that collide with the orchestrator's path heading):

```
You are running a sub-audit on behalf of /audit-artifacts. For each artifact
below, invoke the named IL skill via the Skill tool and return its full
assessment report verbatim, wrapped in sentinel delimiters.

Artifacts to audit (N=<K>):
1. Run /assess-skill on <path1>
2. Run /assess-agent on <path2> with --variant prompt-based
3. Run /assess-prompt on <path3>
…

For each artifact, emit exactly this structure:

<<<AUDIT-REPORT-START path="<artifact-relative-path>" skill="<dispatched-skill>" variant="<variant-or-none>">>>
<full assessor report verbatim>
<<<AUDIT-REPORT-END>>>

Constraints:
- Process artifacts in the order listed; do not skip, reorder, or audit any
  artifact twice.
- Do not author follow-up findings beyond what the assessors produce.
- Do not write any file (the orchestrator handles persistence).
- If an assessor rejects an artifact's shape or errors, emit the error verbatim
  inside the sentinel block in place of the report — do not retry.

Return a single message containing exactly K sentinel blocks in dispatch
order, with no commentary before, between, or after them.
```

After all subagents return, parse each output by scanning for the sentinel
delimiters (regex: `<<<AUDIT-REPORT-START path="(.+?)" .*?>>>(.*?)<<<AUDIT-REPORT-END>>>`).
Reports are keyed by `path`. If the expected K reports aren't found in a bin's
output, record `report-unparseable` for the missing ones and preserve the raw
output for inspection.

### Step 6: Aggregate

1. **Per-artifact findings file**: concatenate the bin reports in manifest
   order (skills → agents → prompts). Each artifact's section reads:

   ```
   ## <Shape>: <relative-path>
   *Assessed via <skill> (Librarian subagent bin <i>, fresh context)*

   <report verbatim>

   ---
   ```

2. **Whole-system summary**: synthesize from the manifest + findings.

   ```
   # Whole-system summary

   ## At a glance
   - N artifacts assessed across M shapes
   - K critical findings (G9.I6 safety-critical violations; ContextSpec violations)
   - J structural gaps
   - Z ambiguous classifications requiring human override

   ## Critical findings (deployment-blocking)
   <list: pull all G9.I6 + DD-92 ContextSpec violations from per-artifact reports>

   ## Common findings (cross-artifact patterns)
   <de-duplicated themes — e.g., "3 of 5 skills missing argument-hint">

   ## Whole-system invariants
   (v1: none. See design contract §"Whole-system invariants" for candidates
   pending recurrence evidence.)

   ## Re-audit guidance
   <if --diff <prior> was passed: drift summary. Else: "Re-audit by re-running
   /audit-artifacts; use --diff <this-manifest-path> for drift detection.">
   ```

### Step 7: Write outputs

**Default: conversation-only.** Per the G9.I6 mitigation: on-disk writes
require explicit consumer opt-in via `--write`.

If `--write` was passed:
1. Check writability of `<audit_target>`. If writable:
   - Create `operations/artifact-audits/<YYYY-MM-DD>/` (mkdir -p). If the target
     has no `operations/` directory, create it (`mkdir -p`) — all audit output
     lives under `operations/` by contract (DD-110).
   - Write `manifest.md`, `findings.md`, `summary.md`.
   - If a same-date subdir already exists, suffix with `-<HH-MM>` (e.g.,
     `2026-06-12-14-30/`).
   - **Append one line** to `<target>/operations/artifact-audits/runs.md` (audit-trail
     log). Format:
     ```
     <YYYY-MM-DD>  session-<NN>  artifacts=<N>  bins=<M>  critical=<K>  missing=<X>  variant=<short-label>
     ```
     Create the file with header `# Audit run log — append-only` if it
     doesn't exist. This is a rule-11-minimal audit trail (one line per
     run; no schema enforcement, no rotation). Resolves the
     session-114 self-audit finding #22.
2. If `--write` was passed but the target is not writable: do not silently
   fall back; surface the failure in the conversation headline ("requested
   --write but target read-only; emitting conversation-only output").

If `--write` was not passed (default): emit manifest + findings + summary
inline in the conversation only. No `runs.md` append in this mode (the
gate is `--write`, not the run itself).

**Always** print the whole-system summary to the conversation, even when
on-disk write succeeded. The summary is the consumer-facing artifact.

### Step 8: Report

At end:
1. One-line headline: `Audited <path>: N artifacts, M bins, K critical findings.`
2. Output locations (paths if written; "conversation only" otherwise).
3. Whole-system summary (inline).
4. Pointer to manifest + findings for deeper read.

## Output Shape

Three artifacts (manifest, findings, summary) plus conversational headline.
Paths and frontmatter as defined in Step 4 / Step 6 / Step 7. Manifest is YAML-
fronted; findings and summary are markdown.

## Boundaries

- If `<path>` doesn't exist or isn't a directory: reject with the redirect note
  from §"When NOT to Use This Skill".
- If the audit discovers zero artifacts in scope: emit a manifest with empty
  artifact tables and a summary that states "no agentic-system artifacts of
  known shapes detected in `<path>`". Do not invent findings.
- If a Librarian subagent returns an unparseable report (e.g., missing
  `## <path>` heading): record the bin as "report-unparseable" in the manifest,
  preserve the raw output in findings under a `### Bin <i> raw output` heading,
  and continue.
- If the same artifact is discovered by two globs (e.g., a CLAUDE.md that's
  also a subagent file under `.claude/agents/`), de-dup by resolved path and
  dispatch only once. Record the multiple-shape match in the manifest's
  ambiguous classifications block.
- Never write outside `<audit_target>/operations/artifact-audits/`. If `<audit_target>` is
  read-only or a sibling-system root the user shouldn't be modifying, fall
  back to conversation output.

## Cross-References

- Design contract: `systems/improvement-loop/project-management/design-notes/2026-06-12-audit-system-design-contract.md`
- IL `/assess-skill`: `systems/improvement-loop/.claude/skills/assess-skill/SKILL.md`
- IL `/assess-agent`: `systems/improvement-loop/.claude/skills/assess-agent/SKILL.md`
- IL `/assess-prompt`: `systems/improvement-loop/.claude/skills/assess-prompt/SKILL.md`
- IL Librarian agent: `systems/improvement-loop/agents/librarian/agent.md`
- Librarian engine subagent: `.claude/agents/librarian.md` (workspace root, `name: librarian`)
- Consumer abstractions map: `systems/improvement-loop/operations/references/consumer-abstractions-map.md`
- Rules 10 (generator-assessor separation), 11 (abstractions earn keep), 12 (audit/design symmetry): `systems/improvement-loop/governance/agent-rules.md`
- Engine capability roadmap: `systems/improvement-loop/project-management/capability-roadmap.md`
