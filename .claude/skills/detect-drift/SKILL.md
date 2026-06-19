---
name: detect-drift
description: >-
  On-demand source-drift scanner for non-guide extracts (rules, skills, templates,
  agents) and curated schematics (DD-107). For extracts, reads each artifact's scalar
  source_finding pointer and flags drift when the finding's last_updated post-dates the
  artifact's extraction_date. For schematics, reads the array grounded_in pointers and
  flags drift when any grounding finding's last_updated post-dates the schematic's
  updated (curation) date. Emits a per-run drift report with a closed Recommendation
  enum. Read-only by contract: never modifies artifacts, never invokes /extract-artifacts
  or /identify-artifacts. Nick gates re-evaluation on the report. Use after large finding
  intakes, dimension rebalances, before a planned /extract-artifacts run, or on Nick request.
user-invocable: true
allowed-tools: Bash Read Grep Glob Write
argument-hint: "[--include rules,skills,templates,agents,schematics] [--exclude ...] [--context <invocation-context>]"
---

# Detect Drift

Detect source drift in non-guide extracts and curated schematics. The scanner walks two roots:

1. **Extracts** — `extracts/{rules,skills,templates,agents}/`. Resolves each artifact's scalar `source_finding` and flags it when `finding.last_updated > artifact.extraction_date`.
2. **Schematics** (DD-107) — `knowledge/schematics/`. Schematics are *curated, not extracted*, so they carry no `extraction_date` and point at evidence through an **array** `grounded_in` rather than a scalar `source_finding`. The scanner resolves each grounding finding and flags the schematic when **any** `finding.last_updated > schematic.updated` (the schematic's last-curation date). One schematic yields at most one drift hit, listing every grounding that moved.

Output is a single drift report at `operations/drift-reports/<YYYY-MM-DD>-source-drift.md`.

The skill produces visibility, not action. **Nick gates re-extraction (extracts) and re-evaluation (schematics)** — the scan never re-runs `/extract-artifacts`, never re-curates a schematic, and never modifies any artifact's frontmatter or body.

## When to Use This Skill

- After a large research-finding intake (Researcher session) where source content has materially evolved.
- After `/dimension-rebalance` reclassifies findings — recheck whether downstream artifacts still align with their (possibly-updated) sources.
- As a precondition to a planned `/extract-artifacts` run, to know whether existing artifacts should be updated alongside new extractions.
- After a finding that a schematic is `grounded_in` is edited — to surface whether the schematic should be re-evaluated against its moved evidence (DD-107; schematics enter the self-evolution loop here).
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
- **Strict comparison semantics.** Drift = source updated **strictly post-dates** the artifact's baseline date — `extraction_date` for extracts, `updated` for schematics. Equal dates are NOT drift. Comparison is on date strings (`YYYY-MM-DD`); no timestamps, no timezones.
- **Recommendation, not decision.** Each drift entry carries one of three closed-enum recommendations — these are Codifier's suggestions, not directives. Nick rules per entry.
- **Per-run reporting.** Each invocation produces its own dated report. Reports accumulate in `operations/drift-reports/`; they are not overwritten across runs.

---

## Arguments

| Argument | Effect |
|----------|--------|
| `--include FORM,FORM,...` | Restrict scan to listed forms. Valid values: `rules`, `skills`, `templates`, `agents`, `schematics`. Comma-separated. Default: all five. |
| `--exclude FORM,FORM,...` | Skip listed forms. Same valid values as `--include`. Cannot be combined with `--include`. |
| `--context "<short string>"` | One-line invocation-context tag for the report's top-matter (e.g., `"post-research-loop sweep"`, `"pre-extract sanity check"`, `"Nick request"`). Default: `"manual scan"`. |

**No arguments:** scan all five forms (the four non-guide non-pattern extracts + schematics) with default context tag `"manual scan"`.

---

## Paths

| Path | Purpose |
|------|---------|
| `systems/improvement-loop/extracts/rules/` | Input — rule artifacts to scan |
| `systems/improvement-loop/extracts/skills/` | Input — skill artifacts to scan |
| `systems/improvement-loop/extracts/templates/` | Input — template artifacts to scan |
| `systems/improvement-loop/extracts/agents/` | Input — agent artifacts to scan |
| `systems/improvement-loop/knowledge/schematics/` | Input — schematic artifacts to scan (array `grounded_in`, `updated` date basis) |
| `systems/improvement-loop/research-findings/` | Input — source findings (read for `last_updated` field) |
| `systems/improvement-loop/operations/drift-reports/` | Output — per-run drift reports |
| `.claude/skills/detect-drift/scan.py` | Helper script — codifies Steps 1+2 (enumeration, frontmatter parse, source resolution, strict-greater-than compare). Called from Step 1. |

The output directory is created on first scan (it does not exist by default).

The helper script is the deterministic part of this skill. The LLM-driven part is Step 2 onwards (recommendation per hit, report construction). Smoke-tested session 73; codified after the first run surfaced a quote-style heterogeneity bug in inline LLM parsing — see `operations/system-log/session-73-codifier-detect-drift-smoke-test.md`.

---

## Procedure

### Step 0: Resolve Scan Scope

1. Parse `--include` / `--exclude` / `--context` arguments. Validate enum values for include/exclude.
2. Reject combinations: `--include` + `--exclude` together is an argument error (use one or the other).
3. Build the `forms` list — the subset of {`rules`, `skills`, `templates`, `agents`, `schematics`} to scan. Default if no flag: all five.
4. Resolve `invocation_context` — value of `--context` or default `"manual scan"`.
5. Report: "Scanning {len(forms)} form(s): {forms_list}. Context: {invocation_context}."

### Step 1: Run Helper Script and Load Results

Invoke the codified enumeration helper from the IL system root (`systems/improvement-loop/`):

```bash
python3 .claude/skills/detect-drift/scan.py \
    [--include rules,skills,templates,agents] \
    [--exclude ...] \
    --context "<invocation_context>" \
    [--out /tmp/drift-scan-<date>.json]
```

Pass through the `--include`/`--exclude`/`--context` arguments resolved in Step 0. The script prints the output JSON path on stdout.

Read the JSON file. The shape:

```jsonc
{
  "scan_date": "<YYYY-MM-DD>",
  "invocation_context": "<string>",
  "forms_scanned": ["rules", ...],
  "total_scanned": <int>,
  "drift_hits": [
    {
      "path": "extracts/<form>/<file>.md",
      "stem": "<artifact-stem>",
      "form": "<form>",
      "source_finding": "<finding-stem>",
      "extraction_date": "<YYYY-MM-DD>",
      "source_last_updated": "<YYYY-MM-DD>",
      "assigned_form": "<form-singular>",
      "has_lifecycle_ptr": <bool>,
      "has_deployed": <bool>
    }
  ],
  "schematic_drift_hits": [
    {
      "path": "knowledge/schematics/<file>.md",
      "stem": "<schematic-stem>",
      "form": "schematics",
      "schematic_updated": "<YYYY-MM-DD>",
      "moved_groundings": [
        {"finding": "<finding-stem>", "last_updated": "<YYYY-MM-DD>"}
      ]
    }
  ],
  "clean_count": <int>,
  "enumeration_gaps": [{"path": ..., "stem": ..., "reason": ...}],
  "unresolvable_sources": [{"path": ..., "stem": ..., "source": ..., "reason": ...}],
  "per_form": {"rules": {"scanned": ..., "drift_hits": ...}, ...},
  "smoke_test_signals": {
    "lifecycle_ptr_present": <int>,
    "lifecycle_ptr_total": <int>,
    "deployed_marker_present": <int>,
    "findings_with_legacy_updated": [{"finding": ..., "legacy_updated": ...}],
    "form_dir_mismatches": [{"path": ..., "assigned_form": ..., "expected": ...}],
    "extraction_date_quote_styles": {"double": ..., "single": ..., "unquoted": ...}
  }
}
```

The helper handles enumeration (both roots), frontmatter parse (single+double quote styles; scalar `source_finding` for extracts, array `grounded_in` for schematics), source resolution, missing-field gap-logging, and the strict-greater-than `YYYY-MM-DD` compare. The skill body is responsible only for: judging recommendations per hit (Step 2), constructing the report (Step 3), and writing it (Step 4).

`drift_hits` carries extract hits; `schematic_drift_hits` carries schematic hits (a separate list because their shape differs — `moved_groundings` array, no `source_finding`/`extraction_date`). `total_scanned` and `clean_count` are combined across both roots; `per_form["schematics"]` reports the schematic scanned/hit counts.

Report: "Enumerated {total_scanned} artifacts across {len(forms_scanned)} form(s). {len(drift_hits)} extract drift hit(s), {len(schematic_drift_hits)} schematic drift hit(s). {len(enumeration_gaps)} enumeration gap(s). {len(unresolvable_sources)} unresolvable source(s)."

### Step 2: Codifier Recommendation per Hit

For each **extract** drift hit, the Codifier emits a recommendation from the closed three-value enum (DD-96 §The Constraint):

| Value | When to use |
|---|---|
| `re-run /extract-artifacts on this finding` | Default suggestion when the source content's update appears materially relevant — new evidence that shifts the artifact's claim, refined wording that supersedes the artifact's framing, expanded applicability. |
| `dismiss as cosmetic` | When the source update is cosmetic — typo fix, tag adjustment, link repair, no change in substance. The artifact is still faithful. |
| `reclassify` | When the source's update suggests its form may have changed. Example: a rule-classified finding now reads more like a pattern (problem/forces/solution emerging). The recommendation routes back to `/identify-artifacts` before `/extract-artifacts`. |

For each **schematic** drift hit, the Codifier emits one of two values (schematics are curated, not extracted — `/extract-artifacts` does not apply):

| Value | When to use |
|---|---|
| `re-evaluate this schematic against its moved grounding` | Default suggestion when one or more grounding findings moved materially — the moved evidence may change the demand/configuration/eval mapping the schematic asserts. Routes to a manual schematic re-curation (not a pipeline skill); Nick gates. |
| `dismiss as cosmetic` | When every moved grounding's update is cosmetic (typo, tag, link) and does not disturb what the schematic rests on. The schematic is still faithful. |

The recommendation is the Codifier's first-pass judgment based on a quick read of the source's recent state. It is NOT a directive — Nick rules per entry on the report. If the Codifier cannot judge a schematic hit confidently, default to `re-evaluate this schematic against its moved grounding` with a one-line note.

If the Codifier cannot judge confidently (e.g., the source content has changed substantially and could be either re-extract or reclassify), default to `re-run /extract-artifacts on this finding` with a one-line note in the entry's body explaining the ambiguity.

### Step 3: Construct Report

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
schematic_drift_hits: <int>
clean_count: <int>
enumeration_gaps: <int>
unresolvable_sources: <int>
forms_scanned:
  - "<form>"
  - "..."
---

# Source Drift Report — <YYYY-MM-DD>

**Invocation context:** <invocation_context>

**Scan summary:** <total_scanned> artifacts scanned across forms (<forms list>); <drift_hits> extract drift hit(s); <schematic_drift_hits> schematic drift hit(s); <clean_count> drift-clean; <enumeration_gaps> enumeration gap(s); <unresolvable_sources> unresolvable source(s).

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

## Schematic Drift Hits

[One block per schematic with at least one moved grounding, in schematic-stem alphabetical order. Omit this section header if zero schematic hits.]

### <schematic-stem>
- Schematic last curated: <YYYY-MM-DD> (`updated`)
- Moved grounding(s):
  - [[<finding-stem>]] — last_updated <YYYY-MM-DD> (post-curation)
  - [[<finding-stem>]] — last_updated <YYYY-MM-DD> (post-curation)
- Recommendation: <schematic closed-enum value>

[Optional one-line note if Codifier flagged ambiguity in the recommendation.]
```

The `Recommendation` line uses one of the closed-enum values verbatim (the three-value extract enum for extract hits, the two-value schematic enum for schematic hits). No free-form text in that field.

### Step 4: Write Report and Summarize

1. **Atomic write** the report file at `operations/drift-reports/<filename>`. The directory is created if absent (first scan ever).
2. **Report to user:**
   ```
   ## Drift Scan Summary — <YYYY-MM-DD>

   Forms scanned: <list>
   Total artifacts scanned: <N>
   Extract drift hits: <H>
   Schematic drift hits: <S>
   Clean: <C>
   Enumeration gaps: <G>
   Unresolvable sources: <U>

   Report: operations/drift-reports/<filename>

   Next: Nick reviews the report and rules per entry. Re-extraction
   (extracts) and re-evaluation (schematics) on flagged artifacts
   require explicit ruling — this skill does not invoke
   /extract-artifacts and does not re-curate schematics.
   ```

---

## Rules

1. **Read-only invariant.** The scan never modifies any artifact's frontmatter, body, `pipeline_status`, or any other state outside `operations/drift-reports/`. The only file the skill creates or writes is the dated report.
2. **No autonomous re-extraction.** The skill never invokes `/extract-artifacts`, `/identify-artifacts`, or any other state-changing skill. Re-extraction requires Nick's ruling on the report.
3. **Strict comparison semantics.** Extracts: drift = `finding.last_updated > artifact.extraction_date`. Schematics: drift = `finding.last_updated > schematic.updated` for any grounding finding (DD-107 — schematics carry no `extraction_date`; `updated` is the last-curation date basis). Equal dates are NOT drift in either case. Lexical compare on `YYYY-MM-DD` strings.
4. **Closed Recommendation enum.** Extract hits: only `re-run /extract-artifacts on this finding`, `dismiss as cosmetic`, `reclassify`. Schematic hits: only `re-evaluate this schematic against its moved grounding`, `dismiss as cosmetic`. Free-form text in the Recommendation field is a contract violation; surface as a procedural failure.
5. **Guides and patterns excluded.** The scan does not enumerate `extracts/guides/` or `extracts/patterns/`. Their drift surfaces through different mechanisms (DD-93/94 for guides; DD-81 + `/synthesize-guide` for patterns).
6. **Per-run reports.** Each invocation produces its own dated file. Reports accumulate; they are never overwritten across runs.
7. **Source field is `last_updated`.** Per DD-96 §Rules #2 (as amended 2026-04-26 / session 71). The original DD-96 filing named the field `updated`; the session-71 amendment corrected it to match the live finding schema. Skill and contract are aligned — no reconciliation required at the implementation layer.
8. **Schematics are curated, not extracted (DD-107).** A schematic hit never routes to `/extract-artifacts` or `/identify-artifacts`; re-curation is a manual Nick-gated edit. The scan reads the array `grounded_in` (not a scalar `source_finding`) and compares each grounding's `last_updated` against the schematic's `updated` (not `extraction_date`). On the schematic side, the field read for the baseline date is `updated`.

---

## Failure Modes

| Failure | Detection | Recovery |
|---------|-----------|----------|
| `--include` and `--exclude` both passed | Step 0 argument validation | Reject with structured error; require one or the other (not both). |
| `--include` / `--exclude` value not in valid form set | Step 0 enum check | Reject with structured error naming the invalid value and the valid set. |
| Artifact missing `source_finding` or `extraction_date` | scan.py frontmatter parse | Log to `enumeration_gaps`; skip from drift comparison. Surface in report's Enumeration Gaps section. |
| Schematic missing `grounded_in` or `updated` | scan.py frontmatter parse | Log to `enumeration_gaps` (reason `missing grounded_in` / `missing updated` / malformed `updated`); skip. DD-107 requires `grounded_in` to resolve — a gap here flags an incomplete schematic. |
| Schematic `grounded_in` finding not found | scan.py source resolution | Log to `unresolvable_sources` citing the schematic and the missing finding stem; skip that grounding (others still checked). Charter trajectory signal: `grounded_in` links must resolve. |
| Source finding file not found | scan.py source resolution | Log to `unresolvable_sources`; skip from drift comparison. Surface in report's Unresolvable Sources section. May indicate finding deletion or rename — Nick reviews. |
| Source finding missing `last_updated` field | scan.py source resolution | Log to `unresolvable_sources` with reason `missing-last-updated`; skip from drift comparison. |
| Date strings malformed (not `YYYY-MM-DD`) | scan.py date compare | Log to `unresolvable_sources` with reason `malformed-date`; skip from drift comparison. |
| Codifier cannot confidently choose a recommendation | Step 2 judgment | Default to `re-run /extract-artifacts on this finding` with a one-line note in the entry body explaining the ambiguity. |
| Skill attempts to write outside `operations/drift-reports/` | Step 4 path check | Procedural violation — read-only invariant breached. Abort the run; surface in next governance audit. |
| Multiple scans on the same date | Step 4 collision check | Append hyphen-numeric suffix (`-2.md`, `-3.md`) to the report filename. Each scan keeps its own report. |

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
| DD-107 | Schematic artifact form — adds `knowledge/schematics/` as a second scan root with array `grounded_in` pointers and `updated` date basis. This slice brings schematics into the drift loop (the slice DD-107 §"What this does NOT decide" deferred to "next slice"). |
