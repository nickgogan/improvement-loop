---
name: detect-drift
description: >-
  On-demand source-drift scanner for non-guide extracts (rules, skills, templates,
  agents). Reads each artifact's source_finding pointer, compares the finding's
  last_updated date against the artifact's extraction_date, and emits a per-run
  drift report with a closed three-value Recommendation enum. Read-only by contract:
  never modifies artifacts, never invokes /extract-artifacts or /identify-artifacts.
  Nick gates re-extraction on the report. Use after large finding intakes,
  dimension rebalances, before a planned /extract-artifacts run, or on Nick request.
user-invocable: true
allowed-tools: Read Grep Glob Write
argument-hint: "[--include rules,skills,templates,agents] [--exclude rules,skills,templates,agents] [--context <invocation-context>]"
---

# Detect Drift

Detect source drift in non-guide extracts. The scanner walks `extracts/{rules,skills,templates,agents}/`, resolves each artifact's `source_finding`, and flags artifacts whose source has been updated post-extraction. Output is a single drift report at `operations/drift-reports/<YYYY-MM-DD>-source-drift.md`.

The skill produces visibility, not action. **Nick gates re-extraction** — the scan never re-runs `/extract-artifacts` and never modifies any artifact's frontmatter or body.

## When to Use This Skill

- After a large research-finding intake (Researcher session) where source content has materially evolved.
- After `/dimension-rebalance` reclassifies findings — recheck whether downstream artifacts still align with their (possibly-updated) sources.
- As a precondition to a planned `/extract-artifacts` run, to know whether existing artifacts should be updated alongside new extractions.
- On Nick request — periodic sweep cadence is intentionally NOT codified (DD-96 §Why selects on-demand over periodic for v1).

## What This Skill Does NOT Do

- **Does not modify artifacts.** Read-only by contract. The scan never edits an artifact's frontmatter, body, or `pipeline_status`.
- **Does not invoke `/extract-artifacts`.** Re-extraction requires Nick's explicit ruling on the drift report.
- **Does not invoke `/identify-artifacts`.** Reclassification recommendations surface in the report; reclassification is Nick's call.
- **Does not scan guides.** Guide lifecycle is governed by DD-93 (preservation) + DD-94 (companion changelog). Guides are out of scope.
- **Does not scan patterns.** Pattern findings route to guides per DD-81; their drift surfaces through guide re-synthesis, not through this scanner.
- **Does not scan deployed artifacts.** Once an extract is deployed from `extracts/` per DD-29, drift detection at the live location is a separate concern.

## Cognitive Disposition

The Drift Detector thinks like a quartermaster — count what is, compare against what was, surface deltas without judgment about urgency.

- **Read-only as identity.** The skill produces a report; it does not produce changes. If a step would mutate state outside `operations/drift-reports/`, that's a procedural failure.
- **Strict comparison semantics.** Drift = source updated **strictly post-dates** artifact extraction. Equal dates are NOT drift. Comparison is on date strings (`YYYY-MM-DD`); no timestamps, no timezones.
- **Recommendation, not decision.** Each drift entry carries one of three closed-enum recommendations — these are Codifier's suggestions, not directives. Nick rules per entry.
- **Per-run reporting.** Each invocation produces its own dated report. Reports accumulate in `operations/drift-reports/`; they are not overwritten across runs.

---

## Arguments

| Argument | Effect |
|----------|--------|
| `--include FORM,FORM,...` | Restrict scan to listed forms. Valid values: `rules`, `skills`, `templates`, `agents`. Comma-separated. Default: all four. |
| `--exclude FORM,FORM,...` | Skip listed forms. Same valid values as `--include`. Cannot be combined with `--include`. |
| `--context "<short string>"` | One-line invocation-context tag for the report's top-matter (e.g., `"post-research-loop sweep"`, `"pre-extract sanity check"`, `"Nick request"`). Default: `"manual scan"`. |

**No arguments:** scan all four non-guide non-pattern forms with default context tag `"manual scan"`.

---

## Paths

| Path | Purpose |
|------|---------|
| `systems/improvement-loop/extracts/rules/` | Input — rule artifacts to scan |
| `systems/improvement-loop/extracts/skills/` | Input — skill artifacts to scan |
| `systems/improvement-loop/extracts/templates/` | Input — template artifacts to scan |
| `systems/improvement-loop/extracts/agents/` | Input — agent artifacts to scan |
| `systems/improvement-loop/research-findings/` | Input — source findings (read for `last_updated` field) |
| `systems/improvement-loop/operations/drift-reports/` | Output — per-run drift reports |

The output directory is created on first scan (it does not exist by default).

---

## Procedure

### Step 0: Resolve Scan Scope

1. Parse `--include` / `--exclude` / `--context` arguments. Validate enum values for include/exclude.
2. Reject combinations: `--include` + `--exclude` together is an argument error (use one or the other).
3. Build the `forms` list — the subset of {`rules`, `skills`, `templates`, `agents`} to scan. Default if no flag: all four.
4. Resolve `invocation_context` — value of `--context` or default `"manual scan"`.
5. Report: "Scanning {len(forms)} form(s): {forms_list}. Context: {invocation_context}."

### Step 1: Enumerate Artifacts

For each form in `forms`:

1. Glob `extracts/{form}/*.md`. Exclude `_index.md`.
2. For each artifact file, parse frontmatter and capture:
   - `source_finding` — the finding stem (string)
   - `extraction_date` — `YYYY-MM-DD` string
   - `assigned_form` — for sanity-check (must match the form directory)
3. Skip any artifact missing `source_finding` or `extraction_date` (log under `enumeration_gaps` for the report's top matter — these are not drift hits, they are scan gaps).

Maintain a flat list of artifact records: `[(path, source_finding_stem, extraction_date, assigned_form), ...]`.

Report: "Enumerated {N} artifacts across {len(forms)} form(s). {G} enumeration gaps (missing source_finding or extraction_date)."

### Step 2: Resolve Source Findings and Detect Drift

For each artifact record:

1. **Read the source finding** at `research-findings/<source_finding>.md`. If absent, log under `unresolvable_sources` (not a drift hit; a separate scan gap that may indicate finding deletion/rename — surface in report top matter).
2. **Read the finding's `last_updated` field.** This is the field findings actually carry (the schema's date-of-last-update marker). DD-96 §Rules #2 names the field `updated`; the implementation reads `last_updated` to match the live schema. The semantic intent of DD-96 is preserved — most-recent source-content update — and the field-name reconciliation is logged for a future DD-96 amendment.
3. **Compare.** If `source.last_updated > artifact.extraction_date` (strict greater-than on `YYYY-MM-DD` lexical compare), record a drift hit:
   ```
   {
     artifact_stem: "<artifact-stem-without-.md>",
     artifact_path: "extracts/<form>/<file>",
     source_finding_stem: "<finding-stem>",
     source_last_updated: "<YYYY-MM-DD>",
     artifact_extraction_date: "<YYYY-MM-DD>",
     recommendation: <see Step 3>
   }
   ```
4. If `source.last_updated <= artifact.extraction_date`, this artifact is drift-clean — increment the clean count, no entry recorded.

Maintain a list of drift hits and three counters: `total_scanned`, `drift_hits`, `clean_count`.

### Step 3: Codifier Recommendation per Hit

For each drift hit, the Codifier emits a recommendation from the closed three-value enum (DD-96 §The Constraint):

| Value | When to use |
|---|---|
| `re-run /extract-artifacts on this finding` | Default suggestion when the source content's update appears materially relevant — new evidence that shifts the artifact's claim, refined wording that supersedes the artifact's framing, expanded applicability. |
| `dismiss as cosmetic` | When the source update is cosmetic — typo fix, tag adjustment, link repair, no change in substance. The artifact is still faithful. |
| `reclassify` | When the source's update suggests its form may have changed. Example: a rule-classified finding now reads more like a pattern (problem/forces/solution emerging). The recommendation routes back to `/identify-artifacts` before `/extract-artifacts`. |

The recommendation is the Codifier's first-pass judgment based on a quick read of the source's recent state. It is NOT a directive — Nick rules per entry on the report.

If the Codifier cannot judge confidently (e.g., the source content has changed substantially and could be either re-extract or reclassify), default to `re-run /extract-artifacts on this finding` with a one-line note in the entry's body explaining the ambiguity.

### Step 4: Construct Report

The report file is named `operations/drift-reports/<YYYY-MM-DD>-source-drift.md` where `<YYYY-MM-DD>` is the current date. If a file with that name already exists (multiple scans on the same date), append a hyphen-numeric suffix: `<YYYY-MM-DD>-source-drift-2.md`, `-3.md`, etc.

**Report structure:**

```markdown
---
type: "drift-report"
target_system:
  - "improvement-loop"
generated_by: "/detect-drift"
date: "<YYYY-MM-DD>"
invocation_context: "<value of --context>"
total_scanned: <int>
drift_hits: <int>
clean_count: <int>
enumeration_gaps: <int>
unresolvable_sources: <int>
forms_scanned:
  - "<form>"
  - "..."
---

# Source Drift Report — <YYYY-MM-DD>

**Invocation context:** <invocation_context>

**Scan summary:** <total_scanned> artifacts scanned across forms (<forms list>); <drift_hits> drift hit(s); <clean_count> drift-clean; <enumeration_gaps> enumeration gap(s); <unresolvable_sources> unresolvable source(s).

## Enumeration Gaps

[List of artifacts skipped due to missing source_finding or extraction_date frontmatter — one bullet per artifact with reason. Omit this section entirely if zero.]

## Unresolvable Sources

[List of artifacts whose source_finding does not resolve to an existing finding file — one bullet per artifact citing the missing finding stem. Omit this section entirely if zero.]

## Drift Hits

[One block per hit, in artifact-stem alphabetical order. Omit this section header if zero hits — top-matter summary is the only output for a clean scan.]

### <artifact-stem>
- Source: [[<finding-stem>]]
- Source updated: <YYYY-MM-DD> (post-extraction)
- Artifact extracted: <YYYY-MM-DD>
- Recommendation: <closed-enum value>

[Optional one-line note if Codifier flagged ambiguity in the recommendation.]
```

The `Recommendation` line uses one of the three closed-enum values verbatim. No free-form text in that field.

### Step 5: Write Report and Summarize

1. **Atomic write** the report file at `operations/drift-reports/<filename>`. The directory is created if absent (first scan ever).
2. **Report to user:**
   ```
   ## Drift Scan Summary — <YYYY-MM-DD>

   Forms scanned: <list>
   Total artifacts scanned: <N>
   Drift hits: <H>
   Clean: <C>
   Enumeration gaps: <G>
   Unresolvable sources: <U>

   Report: operations/drift-reports/<filename>

   Next: Nick reviews the report and rules per entry. Re-extraction
   on flagged artifacts requires explicit ruling — this skill does
   not invoke /extract-artifacts.
   ```

---

## Rules

1. **Read-only invariant.** The scan never modifies any artifact's frontmatter, body, `pipeline_status`, or any other state outside `operations/drift-reports/`. The only file the skill creates or writes is the dated report.
2. **No autonomous re-extraction.** The skill never invokes `/extract-artifacts`, `/identify-artifacts`, or any other state-changing skill. Re-extraction requires Nick's ruling on the report.
3. **Strict comparison semantics.** Drift = `source.last_updated > artifact.extraction_date`. Equal dates are NOT drift. Lexical compare on `YYYY-MM-DD` strings.
4. **Closed Recommendation enum.** Only `re-run /extract-artifacts on this finding`, `dismiss as cosmetic`, `reclassify`. Free-form text in the Recommendation field is a contract violation; surface as a procedural failure.
5. **Guides and patterns excluded.** The scan does not enumerate `extracts/guides/` or `extracts/patterns/`. Their drift surfaces through different mechanisms (DD-93/94 for guides; DD-81 + `/synthesize-guide` for patterns).
6. **Per-run reports.** Each invocation produces its own dated file. Reports accumulate; they are never overwritten across runs.
7. **Field-name reconciliation logged.** DD-96 §Rules #2 specifies `source_finding.updated`; the implementation reads `last_updated` to match the live schema. The semantic intent (most-recent source-content update timestamp) is preserved. The field-name discrepancy is logged for a future DD-96 amendment — see the session-71 SL "Logged for future" section.

---

## Failure Modes

| Failure | Detection | Recovery |
|---------|-----------|----------|
| `--include` and `--exclude` both passed | Step 0 argument validation | Reject with structured error; require one or the other (not both). |
| `--include` / `--exclude` value not in valid form set | Step 0 enum check | Reject with structured error naming the invalid value and the valid set. |
| Artifact missing `source_finding` or `extraction_date` | Step 1 frontmatter parse | Log to `enumeration_gaps`; skip from drift comparison. Surface in report's Enumeration Gaps section. |
| Source finding file not found | Step 2 read | Log to `unresolvable_sources`; skip from drift comparison. Surface in report's Unresolvable Sources section. May indicate finding deletion or rename — Nick reviews. |
| Source finding missing `last_updated` field | Step 2 frontmatter parse | Log to `unresolvable_sources` with reason `missing-last-updated`; skip from drift comparison. |
| Date strings malformed (not `YYYY-MM-DD`) | Step 2 compare | Log to `unresolvable_sources` with reason `malformed-date`; skip from drift comparison. |
| Codifier cannot confidently choose a recommendation | Step 3 judgment | Default to `re-run /extract-artifacts on this finding` with a one-line note in the entry body explaining the ambiguity. |
| Skill attempts to write outside `operations/drift-reports/` | Step 5 path check | Procedural violation — read-only invariant breached. Abort the run; surface in next governance audit. |
| Multiple scans on the same date | Step 5 collision check | Append hyphen-numeric suffix (`-2.md`, `-3.md`) to the report filename. Each scan keeps its own report. |

---

## Design Decisions

| DD | Relevance |
|---|---|
| DD-29 | Human gate at stage boundaries — Nick gates re-extraction on this report; skill produces visibility, not action |
| DD-78 | ContractSpec — drift scan operates over artifacts that all carry contract; non-guide extracts |
| DD-80 | Pipeline simplification — `/extract-artifacts` is the writer this report's recommendations route to |
| DD-81 | Pattern findings route to guides — patterns excluded from this scan |
| DD-93 | Guide preservation — guides excluded from this scan; their lifecycle is companion-changelog driven |
| DD-94 | Companion changelogs for guides — guides excluded |
| DD-95 | `last_change_*` lifecycle pointer on non-guide extracts — DD-96's direct counterpart on the producer/consumer pairing; this scan's recommendations feed `/extract-artifacts` --update runs |
| DD-96 | This skill implements DD-96. Read-only, on-demand, propose-don't-decide invariants are codified above. |
