---
name: extract-artifacts
description: >-
  Draft and write staged artifacts from an approved identification report. Works off the
  output of /identify-artifacts — no classification logic. Reads the report, drafts artifacts
  for approved findings, writes them to extracts/ with ContractSpec (DD-78) and ContextSpec (DD-92).
  Human gate before writing unless --auto.
user-invocable: true
allowed-tools: Read Grep Glob Write Edit Agent
argument-hint: "<report-filename|--latest> [--auto]"
---

# Extract Artifacts

Draft and write staged artifacts from an approved identification report produced by `/identify-artifacts`. This skill does not classify findings — it reads pre-classified, pre-approved entries from the report and produces the actual artifact files.

## When to Use This Skill

- After `/identify-artifacts` has produced an identification report AND Nick has reviewed it
- After Nick has edited the report to set Status fields (APPROVED / REJECTED / REDIRECTED)
- To batch-draft all approved findings from a report

## What This Skill Does NOT Do

- **Does not classify findings.** That's `/identify-artifacts`'s job. This skill reads the assigned form from the report.
- **Does not deploy artifacts.** Extracted artifacts stage in `extracts/`. Deployment is a separate act.
- **Does not produce guides.** Guides are out of scope (IB-146).

## Cognitive Disposition

The Extractor thinks like an artifact author — opinionated, form-appropriate, contract-conscious.

- **Form-appropriate drafting.** A rule should be crisp and enforceable (condition/action/boundary). A template should have clear variables and a fillable body. A pattern should have problem/forces/solution/consequences. Don't write everything in pattern prose.
- **ContractSpec is mandatory.** Every artifact carries `preconditions / invariants / governance / recovery` (DD-78). No exceptions. Think about what breaks, not just what works.
- **ContextSpec is mandatory.** Every artifact carries consumer-fit metadata (DD-92): `applies_to`, `platform_coupling`, `autonomy`, `stage`, `reversibility`, `auditability`, `evidence_strength`, `adoption`. Think about who adopts this, at what stage, at what cost, with what reversibility.
- **Universal vocabulary.** ContextSpec fields must be readable by consumers outside MetaSystem. No IL-internal labels (`S2`, `S3`, `General`, `Perplexity Skills`), no IL-internal skill names (`/identify-artifacts`, `/assess-skill`), no IL-specific paths. `applies_to` is re-derived in universal vocabulary — it is NOT a mechanical copy of `source_finding.applicability` (which is IL-internal bookkeeping).
- **Source-faithful.** The artifact should faithfully represent the finding's insight. Don't add interpretations the finding doesn't support.
- **Self-contained.** A reader should understand the artifact without needing to read the source finding. Link back, but don't depend on it.
- **Reference implementation.** `extracts/rules/confirm-failure-first-tdd.md` is the canonical ContextSpec example. Consult it before drafting when in doubt about field shape.

---

## Arguments

| Argument | Effect |
|----------|--------|
| `<report-filename>` | The identification report to process (e.g., `2026-04-19-identification-report.md`) |
| `--latest` | Find and use the most recent identification report in `operations/pattern-identification-reports/` |
| `--session NN` | Active IL session number for the lifecycle-pointer fields (DD-95). Required on every write of a non-guide artifact (rule, skill, template, agent). Skill prompts if missing (unless `--auto`, which aborts). Ignored for guide writes (this skill does not write guides; defensive). |
| `--sl STEM` | Active session's SL filename stem (no path, no `.md`). Required on every write of a non-guide artifact (DD-95). Skill prompts if missing (unless `--auto`, which aborts). Validated against `operations/system-log/<stem>.md` before any artifact is written. |
| `--update` | Re-extraction mode (DD-95). When set, the skill OVERWRITES existing artifacts whose `source_finding` matches a finding in the current run, rather than skipping them per the default dedup-at-write rule. Triggers: post-drift-report Nick ruling (DD-96), Nick-requested re-extraction, dimension-rebalance regen. On update, body + ContractSpec + ContextSpec are regenerated; `last_change_session` + `last_change_sl` are overwritten with the current session's values; `extraction_date` is preserved (the original extraction date — not the update date); `deployed` + `deployed_to` are preserved. |
| `--version-bump <agent-stem>` | Explicit agent version-bump invocation (DD-100, DD-82). Required when bumping an agent: agent forms are flag-and-exit by default per DD-82's never-auto-create invariant (Step 1.8 agent branch); Nick's prior approval is structural, not skill-resolvable from corpus scan. When set, the named agent stem is treated as a Nick-approved version-bump candidate and routed through the version-bump write path (Item 3 of Step 1.8) rather than flagged-and-exited. Templates do NOT use this flag — template version bumps are auto-proposed by the corpus scan and Nick rules per proposal in the standard flow. |
| `--harvest-row <finding-stem>::<target-form>::<headline-slug>` | Harvest-queue row promotion mode (DD-101). Argument shape is the canonical row-heading ID per IB-163 (`<finding-stem>` is the source pattern finding's stem; matches the literal `### ` heading in the queue file). Queue-file resolution is auto-located by scanning `extracts/guides/*.harvest-queue.md` for a literal heading match (`### <finding-stem>::<target-form>::<headline-slug>`); defensive abort on multi-match (cross-guide same-row collision is OOS per IB-163 closure note c, but the abort surfaces it if it occurs). Verifies row Status is `nick-approved`; treats the row's source_finding as the artifact's source, the row's target form as the artifact's assigned_form, and the row's source excerpt + Codifier's reading + suggested headline as the drafting input. Routes through DD-97 (Step 1.7) for `rule`/`skill` targets; DD-100 (Step 1.8 Branch A) for `template` targets; defensive abort for `agent` targets. On successful write, Step 4.8 updates the originating queue row's Status to `extracted` and Resolution to `extracted to [[<artifact-stem>]]` (or DD-97 merge / DD-100 version-bump variant). The skill never auto-polls harvest queues; this flag is the only entry path to harvest-queue input. Mutually exclusive with `<report-filename>` and `--latest`. Optional `--guide <guide-stem>` disambiguates if multi-match is ever encountered. |
| `--harvest-dismiss <finding-stem>::<target-form>::<headline-slug>` | Harvest-queue row dismissal mode (DD-101). Argument shape matches `--harvest-row`. Queue-file resolution auto-locates by literal heading match across `extracts/guides/*.harvest-queue.md`. Reads the named row and updates Status to `nick-dismissed`, Resolution to `dismissed`. Row is retained in the queue file for audit. Queue-only operation — no drafting, no artifact write. Accepted on rows with Status `queued` or `nick-approved`; rejected on `extracted` or `superseded` rows (terminal states; dismissal would be incoherent). Mutually exclusive with `<report-filename>`, `--latest`, and `--harvest-row`. Optional `--guide <guide-stem>` disambiguates multi-match. |
| `--guide <guide-stem>` | Optional disambiguation for `--harvest-row` / `--harvest-dismiss` (DD-101 amendment per IB-166). Restricts queue-file resolution to `extracts/guides/<guide-stem>.harvest-queue.md`. Required only if a literal heading match across all queue files yields ≥2 hits (cross-guide same-row collision); otherwise the auto-locate scan is sufficient and this flag is ignored. |
| `--auto` | Skip human selection — draft all APPROVED and all non-HITL PENDING findings. Use only when user has pre-reviewed the report. |

**No arguments:** prompt for the report filename.

---

## Paths

| Path | Purpose |
|------|---------|
| `systems/improvement-loop/operations/pattern-identification-reports/` | Input — identification reports |
| `systems/improvement-loop/research-findings/` | Input — full finding files (read for drafting) |
| `systems/improvement-loop/extracts/` | Output — staged artifacts by form |
| `systems/improvement-loop/extracts/{rules,templates,agents,skills,patterns}/` | Per-form output directories |
| `systems/improvement-loop/operations/extension-proposals/` | Output — DD-97 extension-proposal reports (created on first run; not pre-created) |
| `systems/improvement-loop/operations/version-bump-proposals/` | Output — DD-100 template version-bump-proposal reports (created on first run; not pre-created) |

---

## Procedure

### Step 0: Load Input — Dispatch on Invocation Mode

The skill operates in three mutually-exclusive invocation modes. Validate that exactly one of the input flags is provided; abort with a structured error on multi-mode invocations (e.g., `<report> --harvest-row …` is ill-formed).

| Mode | Input flag | Input shape | Pipeline path |
|------|-----------|-------------|---------------|
| **Identification-report (default)** | `<report-filename>` or `--latest` | Identification report from `/identify-artifacts` | Steps 1, 1.7, 1.8, 2, 2.5, 2.7, 3, 4, 5 — full pipeline |
| **Harvest-queue promotion (DD-101)** | `--harvest-row <id>` | One Nick-approved row from `extracts/guides/<stem>.harvest-queue.md` | Step 0a → Steps 1.7 (if rule/skill) or 1.8 (if template), 2, 2.5, 2.7, 3 → Step 4.8 (queue write-back) |
| **Harvest-queue dismissal (DD-101)** | `--harvest-dismiss <id>` | One row from `extracts/guides/<stem>.harvest-queue.md` | Step 0a (resolve) → Step 4.8 (queue-only update); skip drafting entirely |

**Identification-report-mode procedure:**

1. Parse the argument to find the identification report:
   - Named file: read `systems/improvement-loop/operations/pattern-identification-reports/{arg}`
   - `--latest`: glob for `*-identification-report*.md` in `operations/pattern-identification-reports/`, sort by date, take the most recent
2. Read the report. Parse the Details section to extract per-finding entries: `id`, `assigned_form`, `confidence`, `tier`, `reason_codes`, `co_occurrence`, `rationale`, `Status`.
3. Report: "Loaded identification report: {filename}. {N} findings total."

**Harvest-queue-mode procedure:** skip the report-load above and proceed to Step 0a.

### Step 0a: Resolve Harvest Queue Row (DD-101) — harvest mode only

Fires only when `--harvest-row` or `--harvest-dismiss` is set. Skip entirely in identification-report mode.

1. **Parse the row ID.** Argument shape: `<finding-stem>::<target-form>::<headline-slug>` (the canonical compound row-heading ID established by IB-163's Step 4.7; `<finding-stem>` is the source pattern finding's stem — same prefix used in the queue file's `### ` headings). Validate three components separated by `::`. Reject ill-formed IDs with a structured error citing the expected format.

2. **Resolve the queue file (auto-locate per IB-166).** Scan `systems/improvement-loop/extracts/guides/*.harvest-queue.md` for a per-row details block whose heading matches `### <finding-stem>::<target-form>::<headline-slug>` exactly. If `--guide <guide-stem>` is provided, restrict the scan to `extracts/guides/<guide-stem>.harvest-queue.md` only.
   - **Zero matches:** abort with a structured error: "Row `<finding-stem>::<target-form>::<headline-slug>` not found in any harvest queue. Recovery: verify the finding-stem, target-form, and headline-slug match a queue file's per-row block heading; if `--guide` was passed, verify the guide-stem matches an existing queue file."
   - **Multi-match (≥2 queue files contain the same heading):** abort with a structured error listing the matched queue file paths. Recovery: pass `--guide <guide-stem>` to disambiguate. Cross-guide same-row collision is OOS per IB-163 closure note (c) but the defensive abort surfaces it if it ever occurs.
   - **Single match:** record the queue file path for downstream Step 4.8 write-back.

3. **Locate the row in-file.** From the resolved queue file, the per-row details block whose heading matches `### <finding-stem>::<target-form>::<headline-slug>` exactly was identified in Step 2. If no per-row block exists in the file at this heading (defensive recheck after a fresh re-read of the queue file at this step's start), abort with a structured error citing the expected heading and listing the queue file's existing row IDs. Likely cause: typo, stale row-id, headline-slug drift between regens (the duplicate-suppression key is `(source_finding, target_form)`, so a re-detected candidate may carry a different headline-slug than the cited row even though the row stands; verify the cited row's headline-slug against the current queue file).

4. **Read row fields.** Parse the per-row details block to extract: Date queued, Status, Target form, Source finding, Source excerpt, Codifier's reading, Suggested headline, Recommendation, Resolution. Validate Target form is in the closed enum `{rule, skill, template}` — if `agent`, abort with a structured error citing DD-82 + DD-101 §Rules for `/synthesize-guide` item 3 (agent rows are impossible by upstream construction; defensive abort on encountering one).

5. **Status check (mode-specific).**
   - **`--harvest-row` mode:** Status MUST be `nick-approved`. If `queued`, abort with a structured error: "Row Status is `queued`; Nick has not approved this candidate. Recovery: edit the queue file to set Status `nick-approved` (or use `--harvest-dismiss` to dismiss as inline)." If `extracted` or `superseded`, abort: "Row Status is `<status>`; the candidate is already resolved. No further extraction needed." If `nick-dismissed`, abort: "Row Status is `nick-dismissed`; the candidate has been ruled inline-only. No artifact will be created."
   - **`--harvest-dismiss` mode:** Status must be `queued` or `nick-approved`. Reject `extracted` (artifact exists; dismissal is incoherent) and `superseded` (structural status; dismissal would mask the supersession reason). Reject `nick-dismissed` (already dismissed; idempotent re-flip is informational, not actionable; abort with a no-op note).

6. **Build synthetic finding entry.** For `--harvest-row` mode only: construct an in-memory entry that downstream Steps 1+ can consume:
   - `id` = row's Source finding stem (the original pattern finding); the harvested artifact's `source_finding` per DD-101 §Promotion ("source_finding = the original pattern finding").
   - `assigned_form` = row's Target form.
   - `Status` = `APPROVED` (Nick has already gated via the `nick-approved` queue Status; the synthetic identification-report-style Status is set to APPROVED so the Step 1 filter passes the entry through).
   - `harvest_row_id` = the compound `<finding-stem>::<target-form>::<headline-slug>` ID; cached for Step 4.8's write-back. The resolved queue file path (from Step 0a step 2 auto-locate) is also cached for Step 4.8's atomic-write target.
   - `harvest_source_excerpt`, `harvest_codifier_reading`, `harvest_suggested_headline` — cached as drafting input alongside (or in lieu of) the source finding's body. The downstream subagent prompt (Step 2) MAY use the row's excerpt as supplementary context to the source finding's full body; the row's suggested headline MAY seed the artifact title.
   Tag the entry: this is a single-entry "report" for downstream filter consistency.

7. **Single-entry contract.** Harvest-mode invocations process EXACTLY one queue row per invocation. Multi-row batching is not supported — each row is a Nick-gated decision; conflating multiple rows into one invocation would erode the per-row gate. Multi-row processing is achieved by sequential `/extract-artifacts --harvest-row <id1>` then `/extract-artifacts --harvest-row <id2>` invocations.

8. **Report to user:** "Harvest queue row resolved: source_finding=`<finding-stem>`, target_form=`<form>`, suggested headline=`<headline>`. Routing through {DD-97 corpus scan (Step 1.7) | DD-100 corpus scan (Step 1.8 Branch A)} per target form."

### Step 1: Filter to Approved

Filter the report entries by Status:

| Status | Action |
|--------|--------|
| `APPROVED` | Include — draft this artifact |
| `REJECTED` | Skip |
| `REDIRECTED` | Include — use the user-edited `assigned_form` instead of the original |
| `PENDING` | Skip unless `--auto` is set |
| `PENDING` + `--auto` + tier `auto` or `guided` | Include |
| `PENDING` + `--auto` + tier `hitl` | Skip (HITL always needs human decision) |

Report: "{M} findings approved for extraction (A approved, R redirected, P auto-pending). {S} skipped."

If 0 findings are approved, report and exit.

**Pattern filter (DD-81):** After filtering by status, remove all entries where `assigned_form == "pattern"`. Pattern findings route to `/synthesize-guide` for guide synthesis — they are not extracted as individual artifacts. Log: "{P} pattern findings routed to guide synthesis, {E} non-pattern findings proceeding to extraction."

If 0 non-pattern findings remain after the pattern filter, report and exit — suggest running `/synthesize-guide` for the pattern findings.

### Step 1.7: Corpus Scan + Extension Proposal (DD-97) — rule and skill forms only

Before drafting any new rule or skill artifact, the skill scans the matching corpus directory for semantic overlap with the candidate finding. On match, the skill emits a structured extension proposal and routes the finding away from drafting; Nick rules per proposal. On no-match, the finding proceeds to Step 2 drafting per current behavior.

**Scope.** This step fires only when `assigned_form ∈ {rule, skill}`. Templates and agents skip this step entirely (out of scope per DD-97 §Scope and Non-Goals: templates version per future DD-X8; agents never auto-create per spec §2.3). Patterns are already filtered in Step 1 (DD-81).

**Calibration — LLM judgment, loose (DD-97 calibration (i)).** No structured threshold (e.g., ContractSpec invariant overlap by N fields). The LLM reads the candidate finding's name, summary, body, and ContextSpec context plus each candidate-corpus artifact's title, summary, ContractSpec content, and body language. False-positive volume is acceptable; the Nick gate catches them. Promotion to (ii) ContractSpec-overlap-structured or (iii) hybrid requires a future DD if false-positive volume becomes burdensome.

**Procedure:**

1. **Partition findings by form.** Build `rule_findings` (subset with `assigned_form == "rule"`) and `skill_findings` (subset with `assigned_form == "skill"`). Templates / agents pass through untouched.

2. **Glob corpus.** For rule findings, enumerate `extracts/rules/*.md` (skip `_index.md`). For skill findings, enumerate `extracts/skills/*.md` (skip `_index.md`). For each corpus artifact, read the title, summary or first body paragraph, and ContractSpec block.

3. **Per-finding similarity check.** For each candidate in `rule_findings ∪ skill_findings`, compare against every artifact in the matching corpus using LLM judgment. Identify zero, one, or many semantic-overlap candidates. The judgment runs on title + summary + body + ContractSpec; no structured threshold.

4. **Categorize each finding:**
   - **No match:** finding proceeds to Step 2 drafting per current behavior. Tag as `extension_status: "no_match"`.
   - **Single match:** emit one extension proposal (see step 5). Tag as `extension_status: "proposed"`. Skip from Step 2 drafting.
   - **Multiple plausible matches:** surface the strongest match in the proposal's primary block + flag the other candidates as secondaries (see step 5). Tag as `extension_status: "proposed"`. Skip from Step 2 drafting. Nick rules merge target.

5. **Construct extension proposal block** for each `proposed` finding:

   ```markdown
   ### <candidate-finding-stem>

   **Form:** rule | skill
   **Existing artifact (primary match):** [[<existing-artifact-stem>]]
   **Secondary matches:** [[<other-artifact-stem>]], [[<other-artifact-stem>]]   (omit line if zero)

   **Codifier recommendation:** extend existing | create new (false positive) | parameterize as mode variant

   **Why this match:** <1–2 lines explaining the semantic overlap the LLM observed.>

   **Diff sketch:**

   <For rule extensions: the proposed appended Evidence row, with the new source finding cited alongside the original. Body wording delta is proposed if the new evidence shifts the rule's claim; otherwise body unchanged.>

   <For skill parameterization: the proposed mode flag (e.g., `--strict` / `--loose`), how the new variant differs from the original behavior, the documentation block to add to the existing skill's body, and the ContractSpec invariant additions covering the new mode.>

   **Notes:** <Optional one-liner — ambiguity, edge case, why the recommendation is what it is.>
   ```

6. **Aggregate and write the extension-proposals report.** Path: `operations/extension-proposals/<YYYY-MM-DD>-extension-proposals.md`. The report opens with a one-paragraph summary (total candidates scanned, proposals emitted, no-match passthroughs, forms scanned, source identification report) followed by per-proposal blocks in candidate-stem alphabetical order. If no proposals were emitted, the report file is NOT written — the skill reports "No extension proposals; all rule/skill findings proceed to drafting."

   **Report frontmatter:**
   ```yaml
   ---
   type: "extension-proposals-report"
   target_system:
     - "improvement-loop"
   generated_by: "/extract-artifacts"
   date: "<YYYY-MM-DD>"
   identification_report: "<source identification report filename>"
   total_rule_skill_candidates: <int>
   proposals_emitted: <int>
   no_match_passthrough: <int>
   forms_scanned:
     - "rules"
     - "skills"
   ---
   ```

7. **Report to user (always — even with `--auto`).** Surface a one-line summary: "Extension proposals: {P} emitted (rules: {R}, skills: {S}); {NM} findings passing through to drafting. Report: operations/extension-proposals/<filename>." If `P > 0`, surface a Nick-gate prompt: "Review the proposals report. To execute an extension, Nick rules per proposal; this skill does not auto-merge."

**Auto-merge prohibition.** The skill MUST NOT modify any existing artifact in this step. The only file written by Step 1.7 is the extension-proposals report. Application of an extension (appending Evidence rows, adding mode flags) is downstream of Nick's ruling and is not a Step 1.7 behavior. Extension-application via `/extract-artifacts` is left for a future IB; for v1, applying the proposal is a manual edit guided by Nick's ruling and the proposal's diff sketch.

### Step 1.8: Template Version-Bump + Agent Flag-Only (DD-100) — template and agent forms only

Before drafting any new template or agent artifact, the skill enforces DD-100's writer-side rubric: templates auto-scan for evolution and propose a version bump when a candidate matches an existing template; agents NEVER auto-scan and NEVER auto-bump per DD-82's never-auto-create invariant — agent-classified findings are flagged for Nick's review and exit. Nick gates every bump.

**Scope.** This step fires only when `assigned_form ∈ {template, agent}`. Rules and skills are routed through Step 1.7's DD-97 path (out of DD-100 scope per DD-100 §Scope and Non-Goals). Patterns are filtered in Step 1 (DD-81). Each form takes a different branch — templates auto-scan; agents flag-and-exit.

**Calibration — LLM judgment, loose (DD-97 calibration parity).** No structured threshold. The LLM reads the candidate finding's name, summary, body, and ContextSpec context plus each candidate-corpus template's title, summary, ContractSpec content, and body language. False-positive volume is acceptable; the Nick gate catches them. Calibration matches DD-97's loose-trigger philosophy.

**Branch A — Templates (auto-scan + version-bump proposal).**

For each candidate finding with `assigned_form == "template"`:

1. **Glob template corpus.** Enumerate `extracts/templates/<name>.md` and `extracts/templates/<name>-v*.md` siblings (skip `_index.md`). For each baseline `<name>` stem, group its versioned siblings together — the "current" template is the highest-version member of the group (computed as `max(integers extracted from -v<N> suffixes; treat unsuffixed file as v1)`). Read each baseline's title, summary or first body paragraph, and ContractSpec block. The corpus-scan target is the highest-version member of each group; lower versions are historical and not scan-targets (DD-100 §The Constraint: each version is independent; the latest version is the "current" template for evolution comparison).

2. **Per-finding similarity check.** For each candidate template-finding, compare against each baseline group's current template using LLM judgment (parity with Step 1.7). Identify zero, one, or many semantic-overlap candidates. Judgment runs on title + summary + body + ContractSpec; no structured threshold.

3. **Categorize each finding.**
   - **No match:** finding proceeds to Step 2 drafting per current behavior — a brand-new template at unsuffixed `<name>.md`. Tag as `version_bump_status: "no_match"`.
   - **Single match:** emit one version-bump proposal block (see step 4). Tag as `version_bump_status: "proposed"`. Skip from Step 2 drafting.
   - **Multiple plausible matches:** surface the strongest match in the proposal's primary block; flag the other candidates as secondaries. Tag as `version_bump_status: "proposed"`. Skip from Step 2 drafting. Nick rules version-bump target.

4. **Construct version-bump proposal block** for each `proposed` finding:

   ```markdown
   ### <candidate-finding-stem>

   **Form:** template
   **Existing template (primary match):** [[<existing-template-stem>]] (current version: v<N>)
   **Secondary matches:** [[<other-template-stem>]] (v<M>), [[<other-template-stem>]] (v<P>)   (omit line if zero)

   **Proposed filename:** `<existing-template-stem>-v<N+1>.md`

   **Codifier recommendation:** version-bump | create new (false positive) | defer

   **Why this match:** <1–2 lines explaining the semantic overlap the LLM observed.>

   **Diff sketch:**

   <How the new finding's content evolves the existing template — schema/vocabulary/scaffold changes, new placeholders, removed sections, restructured backbone. Cite specific deltas at the structural level (frontmatter blocks, body sections, variable names) rather than narrative summaries.>

   **Notes:** <Optional one-liner — ambiguity, edge case, why the recommendation is what it is.>
   ```

5. **Aggregate and write the version-bump-proposals report.** Path: `operations/version-bump-proposals/<YYYY-MM-DD>-version-bump-proposals.md`. The report opens with a one-paragraph summary (total template candidates scanned, proposals emitted, no-match passthroughs, source identification report) followed by per-proposal blocks in candidate-stem alphabetical order. If no proposals were emitted, the report file is NOT written — the skill reports "No version-bump proposals; all template findings proceed to drafting as new templates."

   **Report frontmatter:**
   ```yaml
   ---
   type: "version-bump-proposals-report"
   target_system:
     - "improvement-loop"
   generated_by: "/extract-artifacts"
   date: "<YYYY-MM-DD>"
   identification_report: "<source identification report filename>"
   total_template_candidates: <int>
   proposals_emitted: <int>
   no_match_passthrough: <int>
   ---
   ```

**Branch B — Agents (flag-and-exit; DD-82 invariant).**

For each candidate finding with `assigned_form == "agent"` AND `--version-bump` is NOT set:

1. **Never scan corpus.** Do NOT enumerate `extracts/agents/`; do NOT compare against existing agents; do NOT emit a version-bump proposal.

2. **Flag for Nick review.** Emit a structured note in the run report citing:
   - The candidate finding stem.
   - The candidate's agent shape (1–2 lines from the finding's body summarizing the proposed agent's disposition + scope).
   - The DD-82 + DD-100 §Rules #4 prior-approval requirement.
   - Recommended next action: "Nick reviews the candidate; if version-bump is approved, re-invoke `/extract-artifacts --version-bump <agent-stem>` against this finding to write `<agent-stem>-v<N+1>.md`. Otherwise, the finding remains classified as `agent` but stages no artifact."

3. **Tag and exit.** Tag the finding `version_bump_status: "agent-flagged"`. Skip from Step 2 drafting. The skill never auto-bumps an agent.

**Branch B' — Explicit agent version-bump (`--version-bump <agent-stem>` set).**

When the operator passes `--version-bump <agent-stem>`, an agent-classified finding is treated as Nick-approved for version bump:

1. **Bypass flag-and-exit.** The candidate skips the Branch B exit and routes to the version-bump write path (same write mechanics as templates — Item 3 below).

2. **Verify baseline existence.** Check `extracts/agents/<agent-stem>.md` (or any `<agent-stem>-v<N>.md` siblings) exists. If no baseline, abort with structured error per Item 3 (c).

3. **Single-target enforcement.** `--version-bump` accepts exactly one stem; the skill aborts if more than one agent-classified finding in the run targets that stem (ambiguous: which finding drives the bump?). Recovery: scope the identification report to the one finding via `--findings`.

4. **Tag.** Tag the finding `version_bump_status: "agent-approved-bump"`. Routes through Step 2 drafting — but the writer-side (Step 3) treats it as a versioned write per Item 3 below.

**Item 3 — Compute-N + collision + missing-baseline rules (writer-side).**

These rules apply at write time (Step 3) for any artifact whose tag is `version_bump_status ∈ {"proposed" (post Nick-rules-version-bump), "agent-approved-bump"}` — i.e., a versioned write rather than a new-baseline write. They are codified here to keep the version-bump rubric self-contained:

(a) **Compute next N.** Enumerate `<name>.md` and `<name>-v*.md` siblings in the directory. Treat the unsuffixed `<name>.md` as v1 (implicit). Take `N = max(existing version integers) + 1`. The new file is `<name>-v<N>.md`.

(b) **Filename collision check.** Before writing `<name>-v<N>.md`, verify the path is unused. Collision aborts the write with a structured error citing the colliding filename and the most likely cause (N-computation race, manual file creation, or filesystem state drift between scan and write). Recovery: human review.

(c) **Missing-baseline check.** Verify `<name>.md` (the implicit v1 baseline) exists before writing any v2+ sibling. If missing (deleted in error), abort the write with a structured error: "v1 baseline `<name>.md` missing; cannot version-bump from a non-existent baseline. Recovery: restore v1 from git, then re-run."

(d) **No in-place version overwrite.** Once `<name>-v<N>.md` exists, `/extract-artifacts` NEVER overwrites it. Subsequent regen of an even-newer version produces `<name>-v<N+1>.md`, never an in-place rewrite of any prior version. The `--update` flag (DD-95 re-extraction path) does NOT apply to versioned files — `--update` overwrites the unsuffixed baseline only. A `--version-bump`+`--update` combination is ill-formed; the skill aborts with a structured error.

(e) **Full independent frontmatter on every version.** Each version carries its own `source_finding` (typically the version-bumping finding; can differ by Nick direction), own `extraction_date` (current write date; never inherited), own `last_change_session` + `last_change_sl` (per DD-95), own `contract` (DD-78), own `context` (DD-92), own `version: <N>` (per DD-100 + IB-161 schema field). Cross-version frontmatter inheritance is forbidden — every version writes fresh from the current run's resolved values.

**Disposition table** (summary of branch outcomes per form):

| Form | --version-bump | Branch | Outcome |
|------|----------------|--------|---------|
| template | not set | A — auto-scan | proposal emitted on match; or pass-through to Step 2 (new template) on no_match |
| template | set | (ill-formed) | abort: --version-bump applies only to agents per the IB scope; templates auto-propose |
| agent | not set | B — flag-and-exit | run report flags candidate; no draft, no proposal, no write |
| agent | set | B' — explicit bump | proceed to Step 2 drafting and Step 3 versioned write |

**Run report.** Always surface a one-line summary: "Template version-bump proposals: {P} emitted; {NM} template findings passing through to drafting. Agent flags: {F} agent findings flagged for Nick review; {AB} agent findings treated as approved bumps via --version-bump." If `P > 0`, surface a Nick-gate prompt: "Review the version-bump-proposals report. To execute a bump, Nick rules per proposal; this skill does not auto-write versioned templates." If `F > 0`, surface a Nick-review prompt: "Agent candidates flagged: {list}. To approve a bump, re-invoke `/extract-artifacts --version-bump <stem>` against the flagged finding's identification report." Surface always — even with `--auto`.

**Auto-bump prohibition.** The skill MUST NOT write any versioned file in Step 1.8. Step 1.8's only side-effects are: (a) the version-bump-proposals report (templates with matches); (b) inline run-report flags (agents); (c) tag-on-finding for Step 2 routing. Versioned writes happen in Step 3 after Nick has ruled (templates) or after `--version-bump` is explicitly passed (agents). A versioned write triggered by Step 1.8 alone, without Nick's intervening rule or explicit flag, is a procedural violation.

### Step 2: Draft Artifacts (Subagents)

**Filter out extension-proposed findings.** Per Step 1.7, any rule or skill finding tagged `extension_status: "proposed"` is routed to the extension-proposals report and does NOT proceed to drafting.

**Filter out version-bump-proposed and agent-flagged findings.** Per Step 1.8, any template finding tagged `version_bump_status: "proposed"` is routed to the version-bump-proposals report and does NOT proceed to drafting; any agent finding tagged `version_bump_status: "agent-flagged"` is routed to the run-report flag list and does NOT proceed to drafting. Findings tagged `version_bump_status: "no_match"` (templates with no evolution match) proceed normally to draft as a new template at unsuffixed filename. Findings tagged `version_bump_status: "agent-approved-bump"` (explicit `--version-bump` invocation) proceed to drafting AND route through Step 3's versioned-write path per Step 1.8 Item 3.

For each approved finding **not flagged for extension proposal AND not flagged for version-bump proposal AND not flagged-and-exited as agent**:

1. **Read the full finding file** from `systems/improvement-loop/research-findings/{id}.md`. The identification report only had a summary — drafting needs the full body.

2. **Launch a subagent** to draft the artifact. Batch into groups of 3-5 (smaller than identification batches because drafting is heavier). Each subagent gets:

**Subagent prompt template:**

```
You are drafting codified artifacts for the MetaSystem knowledge layer. Each finding has
already been classified into a form. Your job is to draft the artifact in the correct
form-appropriate structure.

## ContractSpec (DD-78) — Required on Every Artifact

Every artifact MUST include a ContractSpec with four sub-blocks:
- preconditions: What must be true before this artifact is used
- invariants: What must remain true while this artifact is active
- governance: Who owns, who can modify, what gates apply
- recovery: What happens when preconditions or invariants are violated

## ContextSpec (DD-92) — Required on Every Artifact

Every artifact MUST include a ContextSpec with consumer-fit metadata. All 8 fields required (`adoption.notes` is optional):

- **applies_to:** List of plain-English strings describing what kind of consumer situation fits this artifact. Narrative, not enum. Universal vocabulary only.
- **platform_coupling:** "agnostic" | "specific:<platform>" (e.g., "specific:claude-code")
- **autonomy:** "all" | "hitl-only" | "autonomous-only"
- **stage:** "specify" | "build" | "verify" | "secure" | "operate"
- **reversibility:** "trivial — <note>" | "low — <note>" | "medium — <note>" | "high — <note>" | "irreversible — <note>"
- **auditability:** Plain-English description of how externally verifiable compliance is.
- **evidence_strength:** "Low" | "Medium" | "Strong" — inherit from the source finding's `evidence_strength` field.
- **adoption.status:** "Not Yet Started" | "Partially Adopted" | "Adopted" — inherit from the source finding.
- **adoption.notes:** Plain-English past-signal — where applied, with what outcomes. Optional; set null if unknown.

### Universal Vocabulary — Hard Constraint

ContextSpec fields must be readable by consumers OUTSIDE MetaSystem. Forbidden tokens:

- MetaSystem scope labels: `S2`, `S3`, `General`, `Perplexity Skills` (IL bookkeeping, not consumer-facing)
- IL-internal skill names: `/identify-artifacts`, `/extract-artifacts`, `/assess-skill`, `/assess-agent`, `/research-loop`, `/promote-findings`, etc. Use generic descriptors instead ("classification tooling", "skill-assessment rubrics")
- IL-specific paths: `systems/improvement-loop/...`, `extracts/...`, `research-findings/...`

`CLAUDE.md` is borderline — Anthropic-canonical, acceptable as a concrete example.

### Mechanical-Copy Prohibition

`applies_to` MUST be re-derived in universal vocabulary based on what the finding describes. Do NOT mechanically copy `source_finding.applicability`. Source `applicability` is IL-internal bookkeeping (which of our systems to attend to). ContextSpec `applies_to` is consumer-facing description (what kind of consumer situation fits). These are distinct layers. Translate, do not paste.

Reference implementation: consult the ContextSpec block in `extracts/rules/confirm-failure-first-tdd.md` before drafting.

## Form-Specific Structure

### Pattern
- **Problem:** What recurring problem does this address?
- **Forces:** What competing concerns make this hard?
- **Solution:** What is the reusable shape?
- **Consequences:** What are the tradeoffs (positive and negative)?
- **Known Uses:** Where has this been observed in practice?

### Rule
- **Condition:** Under what circumstances does this rule fire?
- **Action:** What is required or forbidden?
- **Boundary:** Where is this enforced (tool call, commit, session start, etc.)?
- **Enforcement:** How is this checked (regex, enum, format, cardinality)?
- **Rationale:** Why this constraint exists.

### Template
- **Variables:** Named slots with types and descriptions.
- **Body:** The scaffold with {{VARIABLE}} placeholders.
- **Usage:** How and when to render this template.
- **Variation Axis:** What drives different renderings.

### Skill
- **Inputs:** What the skill requires to run.
- **Outputs:** What the skill produces.
- **Steps:** Ordered procedure.
- **Failure Modes:** How the procedure degrades.

### Agent
- **Disposition:** How this agent thinks — its cognitive style.
- **Scope:** What this agent owns and is responsible for.
- **Responsibilities:** Specific duties.
- **Communication:** How it interacts with other agents (artifacts, channels).

## Findings to Draft

[For each finding in this batch:]
- **ID:** [finding file stem]
- **Name:** [name]
- **Assigned Form:** [form from report]
- **Reason Codes:** [from report — drafting rationale only; do NOT emit in the written artifact]
- **Co-occurrence:** [from report, or null — drafting rationale only]
- **Source applicability (IL-internal — DO NOT COPY into `applies_to`):** [source finding's `applicability` field]
- **Source evidence_strength:** [Strong|Medium|Low — inherit verbatim into `context.evidence_strength`]
- **Source adoption.status:** [Not Yet Started|Partially Adopted|Adopted — inherit verbatim into `context.adoption.status`]
- **Full Finding Body:**
[entire finding body text]

## Output Format (one JSON object per finding, strict)

IMPORTANT: Output ONLY valid JSON objects, one per line. No markdown fencing, no commentary.

{"id": "finding-file-stem", "title": "Artifact Title", "assigned_form": "pattern|skill|rule|template|agent", "body": "The full artifact body in markdown, using the form-appropriate structure above. Use actual newlines (not \\n) within the body.", "contract": {"preconditions": "...", "invariants": "...", "governance": "...", "recovery": "..."}, "context": {"applies_to": ["...", "..."], "platform_coupling": "agnostic|specific:<platform>", "autonomy": "all|hitl-only|autonomous-only", "stage": "specify|build|verify|secure|operate", "reversibility": "trivial|low|medium|high|irreversible — <note>", "auditability": "...", "evidence_strength": "Low|Medium|Strong", "adoption": {"status": "Not Yet Started|Partially Adopted|Adopted", "notes": "... or null"}}}
```

**Batch launch:** Use the `Agent` tool for each batch. Launch all batches in parallel.

### Step 2.5: Validate Drafts

For each drafted artifact, run three checks BEFORE writing. Any artifact failing a check is flagged and NOT written — surface in the Step 6 summary.

1. **ContextSpec presence (DD-92).** Verify all 8 required fields are present and non-null: `applies_to`, `platform_coupling`, `autonomy`, `stage`, `reversibility`, `auditability`, `evidence_strength`, `adoption.status`. (`adoption.notes` may be null.) If any required field is missing or null, flag.

2. **Mechanical-copy guard (DD-92).** Read the source finding's `applicability` field from its frontmatter. Compare each string against every entry in `context.applies_to`. If any source-`applicability` string appears verbatim (or as an obvious near-paraphrase) in `applies_to`, flag. Require re-draft with explicit instruction: re-derive in universal consumer-facing vocabulary, do not paste.

3. **Forbidden-vocabulary scan (DD-92).** Scan all ContextSpec field values (all of `applies_to`, plus `platform_coupling`, `autonomy`, `stage`, `reversibility`, `auditability`, `adoption.notes`) for forbidden tokens:
   - MetaSystem scope labels: `S2`, `S3`, `General` (when used as scope shorthand), `Perplexity Skills`
   - IL-internal skill name patterns: any `/identify-artifacts`, `/extract-artifacts`, `/assess-skill`, `/assess-agent`, `/research-loop`, `/promote-findings`, `/synthesize-guide`, `/reassess-priorities`, etc.
   - IL-specific path prefixes: `systems/improvement-loop/`, `extracts/`, `research-findings/`, `research-sources/`, `research-authorities/`

   If any forbidden token found, flag. Require re-draft with universal-vocabulary instruction.

Report: "Validation: {V} artifacts passed, {F} flagged ({M} missing-fields, {C} mechanical-copy, {B} forbidden-vocab)."

### Step 2.7: Resolve Lifecycle Pointer (DD-95) — non-guide artifacts only

Every non-guide artifact (rule, skill, template, agent) carries two required frontmatter fields per DD-95:

- `last_change_session: <integer>` — the active IL session number.
- `last_change_sl: "<sl-filename-stem>"` — the bare filename stem of the active session's System Log entry (no path, no `.md` extension).

This step resolves both values before any artifact is written. The skill never auto-derives the session number from git or filesystem state — both fields are explicit inputs.

1. **Resolve session number.**
   - Read `--session NN`. If absent and not `--auto`, prompt the user (e.g., "Active IL session number?"). If absent and `--auto`, abort with a structured error naming the missing argument.
   - Validate it is a positive integer. Reject otherwise.

2. **Resolve SL filename stem.**
   - Read `--sl STEM`. If absent and not `--auto`, prompt. If absent and `--auto`, abort.
   - Strip any leading `operations/system-log/` and any trailing `.md` if the user passed a path or filename — store the bare stem.

3. **Validate SL stem resolves.**
   - Check that `systems/improvement-loop/operations/system-log/<stem>.md` exists. If absent, abort the write with a structured error: missing-file path, recommended fix path ("write the SL entry first, then re-run /extract-artifacts; or correct the --sl argument").
   - This validation runs ONCE per skill invocation. The same `(session, sl-stem)` pair is used for every non-guide artifact written in this run.

4. **Hold for Step 3.** Cache `(active_session, active_sl_stem)` for use during the per-artifact write loop. Both fields are written verbatim into the frontmatter of every non-guide artifact created or updated in this run.

5. **Pattern artifacts excluded — bookkeeping note.** Pattern findings are filtered out in Step 1 (DD-81 pattern routing) and never reach the write step. Guides are not written by this skill at all. Lifecycle-pointer fields apply ONLY to rule, skill, template, agent forms. The writer must not emit either field on a guide artifact under any circumstance — defense in depth, even though no current code path leads to guide writes from this skill.

### Step 3: Write Artifacts

For each drafted artifact:

1. **Generate filename:** kebab-case from the artifact title. E.g., `absolute-filepath-rule.md` for a rule about absolute filepaths.

2. **Check for filename collision and dedup behavior** in the target directory:
   - **Default mode (no `--update`, no versioned write):** if an existing artifact has the same `source_finding`, skip per Rule #4 (dedup-at-write). If a different artifact uses the same filename, append `-2`, `-3` to the new artifact's filename.
   - **Update mode (`--update`):** if an existing artifact has the same `source_finding`, this is a re-extraction. Read the existing artifact's frontmatter to capture preserve-on-update fields: `extraction_date`, `deployed`, `deployed_to`. The new body + ContractSpec + ContextSpec replace the existing ones. The two preserved fields are written back verbatim. `last_change_session` + `last_change_sl` are overwritten with the active session's values from Step 2.7 (no preservation; the SL chain carries the prior pointer). Filename is unchanged. `--update` does NOT apply to versioned writes — see versioned-write branch below.
   - **Versioned-write branch (DD-100 — finding tagged `version_bump_status: "proposed"` post Nick-rules-version-bump, OR `version_bump_status: "agent-approved-bump"` via `--version-bump`):** apply the Step 1.8 Item 3 rules (a)–(e). Compute `N = max(existing version integers) + 1` from `<existing-stem>.md` and `<existing-stem>-v*.md` siblings; pre-write filename collision check (abort on collision); missing-baseline check (abort if `<existing-stem>.md` missing); never overwrite an existing version. Filename is `<existing-stem>-v<N>.md`. Frontmatter is fully independent (own `source_finding`, own `extraction_date` = current date, own `last_change_*`, own `contract`, own `context`, own `version: <N>`); never inherit fields from prior versions. Combining `--update` with a versioned write is ill-formed — abort.

3. **Write the artifact file** to `systems/improvement-loop/extracts/{assigned_form}s/`:

```yaml
---
title: "[Artifact Title]"
type: "extracted-artifact"
assigned_form: "[pattern|skill|rule|template|agent]"
source_finding: "[finding-file-stem]"
extraction_date: "[YYYY-MM-DD]"
last_change_session: [active session integer — DD-95]
last_change_sl: "[active session SL stem — DD-95]"
version: [integer — DD-100; required for template/agent v2+; optional v1 (omit for v1 if writing as new baseline; emit explicit "version: 1" only on retroactive backfill); omit for rule/skill/pattern/guide]
identification_report: "[report-filename]"
deployed: false
deployed_to: null
context:
  applies_to:
    - "[universal-vocabulary consumer-context string]"
    - "[another universal-vocabulary string]"
  platform_coupling: "[agnostic | specific:<platform>]"
  autonomy: "[all | hitl-only | autonomous-only]"
  stage: "[specify | build | verify | secure | operate]"
  reversibility: "[trivial|low|medium|high|irreversible] — [note]"
  auditability: "[plain-English: how externally verifiable is compliance]"
  evidence_strength: "[Low | Medium | Strong]"
  adoption:
    status: "[Not Yet Started | Partially Adopted | Adopted]"
    notes: "[plain-English past-signal, or null]"
contract:
  preconditions: "[...]"
  invariants: "[...]"
  governance: "[...]"
  recovery: "[...]"
tags:
  - "extracted-artifact"
  - "[assigned_form]"
---

# [Artifact Title]

**Source:** [[finding-file-stem]]
**Form:** [assigned_form]
**Extraction date:** [YYYY-MM-DD]

[Form-appropriate body from subagent draft]

## Contract

### Preconditions
[preconditions text]

### Invariants
[invariants text]

### Governance
[governance text]

### Recovery
[recovery text]
```

### Step 4: Back-Annotate Source Findings

For each written artifact, use `Edit` to append an extraction note to the source finding's body:

```markdown
## Extraction Note — [YYYY-MM-DD]
Extracted as **[assigned_form]**: [[artifact-filename]] in `extracts/[form]s/`
```

### Step 4.8: Harvest-Queue Row Write-back (DD-101) — harvest mode only

Fires only in harvest-queue invocation modes (`--harvest-row` or `--harvest-dismiss`). Skip entirely in identification-report mode.

For `--harvest-dismiss` mode, this step is invoked DIRECTLY after Step 0a (skip Steps 1, 1.7, 1.8, 2, 2.5, 2.7, 3, 4 — there is no drafting, no artifact write, and no source-finding back-annotation; the operation is queue-only).

For `--harvest-row` mode, this step runs after Step 4 (back-annotate source) and before Step 5 (back-annotate finding files).

**Inputs.** The cached `harvest_row_id` from Step 0a (compound `<finding-stem>::<target-form>::<headline-slug>`) and the cached resolved queue file path (from Step 0a step 2 auto-locate); the active `(active_session, active_sl_stem)` pair from Step 2.7 (cached even though no DD-95 artifact-write occurs in dismiss mode — Step 2.7 still resolves both fields when `--session` and `--sl` are passed; in dismiss mode the SL stem is used to annotate the queue-row footer); the outcome of Steps 1.7 / 1.8 / 3 (whether an artifact was written, whether an extension or version-bump proposal was emitted, or no-op).

**Branch dispatch.**

| Branch | Trigger | Action |
|--------|---------|--------|
| **A — Dismissal** | `--harvest-dismiss` set | Update row Status → `nick-dismissed`; Resolution → `dismissed`; append dismissal footer. |
| **B — New artifact written** | `--harvest-row` + finding NOT tagged `extension_status: "proposed"` AND NOT tagged `version_bump_status: "proposed"` AND artifact written in Step 3 | Update row Status → `extracted`; Resolution → `extracted to [[<artifact-stem>]]`; append extraction footer. |
| **C — DD-97 extension proposal emitted (rule/skill)** | `--harvest-row` + finding tagged `extension_status: "proposed"` (Step 1.7 multi-or-single-match path) | Status remains `nick-approved`; Resolution remains blank; append pending-merge annotation citing the extension-proposals report and the primary-match artifact stem. |
| **D — DD-100 version-bump proposal emitted (template)** | `--harvest-row` + finding tagged `version_bump_status: "proposed"` (Step 1.8 Branch A multi-or-single-match path) | Status remains `nick-approved`; Resolution remains blank; append pending-version-bump annotation citing the version-bump-proposals report and the proposed `<existing-stem>-v<N+1>.md` filename. |
| **E — Defensive abort (agent target)** | Step 0a step 4 detected `target form: agent` (should be unreachable per IB-163 suppression invariant) | Step 0a already aborted; Step 4.8 never runs in this case. Documented for completeness. |

**Branch A — Dismissal (queue-only update):**

1. Read the queue file at the cached path from Step 0a step 2 (auto-located by literal heading match; per IB-166 amendment).
2. Locate the matching summary-table row (by source finding + target form) and the matching per-row details block (by compound heading `### <finding-stem>::<target-form>::<headline-slug>`).
3. Update the summary-table row's Status column to `nick-dismissed` and Recommendation/Resolution column display to reflect dismissal.
4. Update the per-row details block: change `**Status:** <prior>` to `**Status:** nick-dismissed`; change/set `**Resolution:** dismissed`.
5. Append a footer line to the per-row details block: `Dismissed YYYY-MM-DD — Session NN — [[<active_sl_stem>]] — per --harvest-dismiss invocation.`
6. Atomic write: read existing → modify in-place for the named row → write the result. All other rows unchanged.
7. Report: "Harvest queue row dismissed: `<row-id>`. Status → `nick-dismissed`. Row retained in `<resolved-queue-filename>` for audit."

**Branch B — New artifact written:**

1. Read the queue file.
2. Locate the row by compound ID.
3. Update summary table: Status → `extracted`; Recommendation/Resolution display → `extracted to [[<artifact-stem>]]`.
4. Update per-row details: `**Status:** extracted`; `**Resolution:** extracted to [[<artifact-stem>]]`.
5. Append footer: `Extracted YYYY-MM-DD — Session NN — [[<active_sl_stem>]] — to [[<artifact-stem>]].`
6. Atomic write.
7. Report: "Harvest queue row promoted to extracted artifact: `<row-id>` → `[[<artifact-stem>]]`. Status → `extracted`."

**Branch C — DD-97 extension proposal emitted (rule/skill, no artifact written this invocation):**

1. Read the queue file.
2. Locate the row.
3. Status remains `nick-approved`; Resolution remains blank in summary table and per-row details (do NOT pre-fill — the merge has not yet applied).
4. Append a pending annotation footer to the per-row details block: `Pending merge YYYY-MM-DD — Session NN — [[<active_sl_stem>]] — DD-97 extension proposal emitted at [[operations/extension-proposals/<extension-proposals-filename>]]; primary match [[<existing-artifact-stem>]]. Manual apply per DD-97 v1 (Step 1.7 auto-merge prohibition); after apply, row Status flips to `extracted` and Resolution to `merged into [[<existing-artifact-stem>]]` via manual queue edit (or future skill mode).`
5. Atomic write.
6. Report: "Harvest queue row routed to DD-97 extension path: `<row-id>`. Extension proposal emitted at `operations/extension-proposals/<filename>`. Row Status remains `nick-approved`; manual merge per DD-97 v1 (Step 1.7 auto-merge prohibition); update queue row Status manually after apply, or await future skill-mode that closes the merge loop."

**Branch D — DD-100 version-bump proposal emitted (template, no artifact written this invocation):**

1. Read the queue file.
2. Locate the row.
3. Status remains `nick-approved`; Resolution remains blank.
4. Append annotation footer: `Pending version-bump YYYY-MM-DD — Session NN — [[<active_sl_stem>]] — DD-100 version-bump proposal emitted at [[operations/version-bump-proposals/<version-bump-proposals-filename>]]; primary match [[<existing-template-stem>]] (current version v<N>); proposed filename `<existing-template-stem>-v<N+1>.md`. On Nick ruling: re-invoke `/extract-artifacts --harvest-row <row-id>` AFTER updating the existing template (or with the proposal-applied-as-instruction) — at that point Step 1.8 Branch A's match-disambiguation will route to the version-bump write path; row Status flips to `extracted` and Resolution to `version-bumped to [[<existing-template-stem>-v<N+1>]]` post-write.`
5. Atomic write.
6. Report: "Harvest queue row routed to DD-100 version-bump path: `<row-id>`. Version-bump proposal emitted at `operations/version-bump-proposals/<filename>`. Row Status remains `nick-approved`; await Nick ruling on the version-bump proposal."

**Atomic-write invariants (all branches).** Step 4.8 reads the entire queue file, mutates only the named row's Status / Resolution / footer block, and writes the entire file back. All other rows (regardless of their state) are preserved byte-equivalent. Failure mid-write leaves the file in a known prior-or-new state per filesystem atomicity; a partial-write recovery is captured in the failure-modes table below. The queue file's `## Per-row details` section ordering is preserved (no reordering during update).

**Run-report summary (always).** "Harvest queue write-back: row `<row-id>` updated. Branch: <A|B|C|D>. Status: `<old>` → `<new>` (or unchanged with pending annotation)."

### Step 5: Back-Annotate Finding Files

For each extracted finding, update its frontmatter:

1. Set `pipeline_status: "extracted"`
2. Set `consumed_by:` to include the artifact filename (e.g., `"rules/file-read-deduplication.md"`)

If the finding already has `pipeline_status: "synthesized"` (consumed by a guide), keep `synthesized` and append the artifact to `consumed_by`.

### Step 6: Summary

Report to the user:

```
## Extraction Summary — [date]

**Report:** {report-filename}
**Artifacts drafted:** {M}
  - patterns: {count}
  - rules: {count}
  - templates: {count}
  - skills: {count}
  - agents: {count}
**Skipped:** {S} (rejected: {R}, hitl-pending: {H})

Files written:
  - extracts/rules/artifact-name.md
  - extracts/patterns/artifact-name.md
  [...]

Findings annotated: {list}

Next: Review staged artifacts in extracts/. Deploy to enforcement locations when ready.
```

---

## Rules

1. **Never classify.** This skill reads forms from the identification report. If a finding has no report entry, it cannot be extracted.
2. **ContractSpec on every artifact** (DD-78). If a subagent omits it, flag the artifact for manual review — do not write without a contract.
3. **DD-92 ContextSpec requirements.** Every artifact carries a complete ContextSpec in universal vocabulary. Specifically:
   a. All 8 required fields present: `applies_to`, `platform_coupling`, `autonomy`, `stage`, `reversibility`, `auditability`, `evidence_strength`, `adoption.status`. `adoption.notes` optional. Missing field → flag, do not write.
   b. No MetaSystem scope labels (`S2`, `S3`, `General`, `Perplexity Skills`), no IL-internal skill names (`/identify-artifacts`, `/assess-skill`, etc.), no IL-specific paths. Forbidden-vocab scan runs in Step 2.5.
   c. `applies_to` re-derived in universal vocabulary; NEVER a mechanical copy of `source_finding.applicability`. Mechanical-copy guard runs in Step 2.5.
   d. IL classification meta (`confidence`, `tier`, `reason_codes`, `co_occurrence`) NOT emitted in the written artifact — IL-internal bookkeeping only. These are read from the report for drafting rationale, stripped at write.
   e. Reference implementation: `extracts/rules/confirm-failure-first-tdd.md` — consult when in doubt about field shape.
4. **Dedup at write time.** Check if an artifact for this finding already exists in `extracts/`. In default mode, skip. In `--update` mode (DD-95 re-extraction path: post-drift-report ruling, Nick-requested re-extraction, dimension-rebalance), overwrite the existing artifact per Step 3 update-mode rules — body + ContractSpec + ContextSpec regenerated; `extraction_date`, `deployed`, `deployed_to` preserved; `last_change_session` + `last_change_sl` overwritten with current session values.
5. **Do not deploy.** Write to `extracts/` only. Deployment is a separate act.
6. **Back-annotate after writing.** The source finding gets a note linking to the extracted artifact.
7. **Respect REDIRECTED status.** If the user changed the form in the report, use the user's form, not the original classification.

---

## Failure Modes

| Failure | Detection | Recovery |
|---------|-----------|----------|
| Report not found | File doesn't exist at path | Prompt user for correct filename |
| Report has no APPROVED entries | Filter in Step 1 returns 0 | Report and exit — suggest user review the report |
| Subagent returns malformed JSON | JSON parse error | Log the batch, re-run with smaller batch size |
| ContractSpec missing from draft | `contract` field is null or empty | Flag artifact, do not write. Report in summary. |
| ContextSpec missing or incomplete | Step 2.5: `context` field absent, or any required sub-field (except `adoption.notes`) null | Flag artifact, do not write. Report in summary. |
| Mechanical copy of source.applicability detected | Step 2.5: source `applicability` strings appear verbatim in `context.applies_to` | Flag artifact, request re-draft with explicit re-derivation instruction. Do not write original. |
| Forbidden vocabulary in ContextSpec | Step 2.5: token scan finds MetaSystem scope labels, IL-internal skill names, or IL-specific paths | Flag artifact, request re-draft with universal-vocabulary instruction. Do not write original. |
| Finding file not found | Read returns error | Skip this finding, report in summary |
| `--session` missing on non-guide write | Step 2.7 session resolution | Prompt unless `--auto`. With `--auto`, abort with structured error naming the missing argument. |
| `--sl` missing on non-guide write | Step 2.7 SL stem resolution | Prompt unless `--auto`. With `--auto`, abort with structured error naming the missing argument. |
| `--sl` stem does not resolve to existing SL file | Step 2.7 SL existence check | Abort the write; structured error names missing-file path; recommend writing the SL entry first or correcting the `--sl` argument. |
| `--update` mode targets a finding with no existing artifact | Step 3 dedup check | Treat as create — write the artifact normally; surface an informational note in the summary so the operator knows update mode found no prior artifact. |
| Skill auto-merges an extension instead of proposing | Step 1.7 auto-merge prohibition | Procedural violation — DD-97 §Rules #3 forbids auto-merge. The only file Step 1.7 writes is the extension-proposals report. Surface in next governance audit. |
| Extension proposal emitted for template or agent finding | Step 1.7 scope filter | Procedural violation — DD-97 §Scope excludes templates and agents. Surface and log; the proposal is invalid. |
| Multiple plausible matches and Codifier silently picks one | Step 1.7 multi-match handling | The proposal must surface the strongest match as primary AND flag secondaries; Nick rules merge target. Single-match-without-secondaries on a multi-match input is a procedural failure. |
| Versioned write attempted but v1 baseline `<name>.md` is missing | Step 1.8 Item 3 (c) / Step 3 versioned-write branch missing-baseline check | Abort the write with structured error naming the missing baseline. Never silently re-create v1 from a non-v1 source. Recovery: restore v1 from git (or recreate from prior session's commit), then re-run. |
| Filename collision: `<name>-v<N>.md` already exists when skill computes N | Step 1.8 Item 3 (b) / Step 3 versioned-write branch pre-write check | Abort with structured error naming the colliding filename and likely cause (N-computation drift, manual file creation, filesystem state drift). Recovery: human review of the directory state. |
| Auto-bump attempt for agent form (no `--version-bump` set) | Step 1.8 Branch B agent flag-and-exit invariant | Procedural violation — DD-82's never-auto-create invariant + DD-100 §Rules #4 forbid auto-bump for agents. The skill MUST flag-and-exit when an agent-classified finding is encountered without `--version-bump`. Surface in next governance audit. |
| In-place overwrite of an existing `<name>-v<N>.md` body | Step 1.8 Item 3 (d) / Step 3 versioned-write branch invariant | Procedural violation — DD-100 §Rules #7 forbids in-place version overwrite. Subsequent regen MUST produce `<name>-v<N+1>.md`, not a re-write. Surface and revert from git. |
| Template version-bump-proposed but corpus scan finds NO match | Step 1.8 Branch A categorization (no_match path) | Expected behavior — finding tagged `version_bump_status: "no_match"` proceeds to Step 2 drafting as a brand-new template at the unsuffixed filename. The "no match → proceed to draft new template" path is regression-equivalent to the pre-IB-162 baseline; documented to disambiguate from the "match → proposal" path. |
| `--version-bump` passed for a template form | Step 1.8 Branch A guard / argument validation | Ill-formed invocation — `--version-bump` applies only to agents (DD-82 invariant). Templates auto-propose via the corpus scan; Nick rules per proposal. Abort with structured error citing the form-mismatch. |
| `--version-bump <stem>` set but more than one agent finding in the run targets that stem | Step 1.8 Branch B' single-target enforcement | Ambiguous: which finding drives the bump? Abort with structured error. Recovery: re-scope the identification report to one finding via `--findings`. |
| `--version-bump` combined with `--update` | Step 3 versioned-write branch ill-formed-combination check | Abort with structured error. `--update` overwrites the unsuffixed baseline (DD-95 re-extraction); versioned writes produce a new sibling file (DD-100 version bump). The combination is structurally incoherent. |
| Harvest-row invocation with Status `queued` (not yet `nick-approved`) | Step 0a step 5 status check (`--harvest-row` mode) | Abort with structured error: "Row Status is `queued`; Nick has not approved this candidate." Recovery: edit the queue file to flip Status `queued` → `nick-approved` (Nick's gate decision; manual or via Obsidian), or use `--harvest-dismiss` to dismiss as inline. Procedural violation if the skill auto-extracts on a `queued` row — DD-101 §Rules for `/synthesize-guide` item 7 + this skill's Step 0a Status check are the structural enforcement. |
| Harvest-row reference resolves to non-existent row | Step 0a step 2 auto-locate scan returns zero matches | Abort with structured error citing the expected compound heading `### <finding-stem>::<target-form>::<headline-slug>` and listing existing row IDs across all queue files (or just the `--guide`-restricted file if that flag was passed). Likely cause: typo in finding-stem or headline-slug, stale row-id (cluster departed and row was superseded; check for a `superseded` row matching the source_finding), or wrong target-form. |
| Harvest-row reference matches multiple queue files | Step 0a step 2 auto-locate scan returns ≥2 matches | Abort with structured error listing the matched queue file paths. Recovery: pass `--guide <guide-stem>` to disambiguate (per IB-166 amendment). Cross-guide same-row collision is OOS per IB-163 closure note (c) but the defensive abort surfaces it if it ever occurs. |
| Harvest-queue row target form is `agent` | Step 0a step 4 closed-enum target-form check | Abort with structured error citing DD-82 + DD-101 §Rules for `/synthesize-guide` item 3 (agent rows are impossible by upstream IB-163 suppression invariant; defensive abort on encountering one indicates contract violation upstream). Surface in next governance audit. |
| Harvest-row invocation with Status `extracted` or `superseded` | Step 0a step 5 status check (`--harvest-row` mode) | Abort with informational note: "Row Status is `<status>`; the candidate is already resolved. No further extraction needed." For `extracted`: artifact exists; consult the row's Resolution for the artifact pointer. For `superseded`: source finding departed cluster; the candidate was rendered moot before extraction. |
| Harvest-row invocation with Status `nick-dismissed` | Step 0a step 5 status check (`--harvest-row` mode) | Abort with informational note: "Row Status is `nick-dismissed`; Nick ruled the candidate inline-only. No artifact will be created." If Nick later changes posture, edit the queue file to flip back to `nick-approved` and re-invoke. |
| Harvest-dismiss invocation on `extracted` or `superseded` row | Step 0a step 5 status check (`--harvest-dismiss` mode) | Abort: dismissal is incoherent on terminal-status rows. `extracted` rows have a written artifact; `superseded` rows reflect structural cluster movement. Dismissal as inline only applies to candidates not yet resolved. |
| Harvest-dismiss invocation on `nick-dismissed` row | Step 0a step 5 status check (`--harvest-dismiss` mode) | No-op informational note: row is already dismissed. The skill exits without modifying the row. Idempotent re-flip is not actionable. |
| Multiple input modes set simultaneously (e.g., `<report>` + `--harvest-row`) | Step 0 dispatch validation | Abort with structured error citing the conflicting flags. The three input modes are mutually exclusive — pick one per invocation. |
| Queue-write-back failure mid-extraction (Branch B; artifact written but row update failed) | Step 4.8 atomic-write fails post Step-3 artifact write | Recovery is human-mediated re-run of the row update. The artifact is on disk in `extracts/<form>s/`; the queue row remains in its prior status. Recovery: locate the artifact, manually edit the queue row to Status `extracted` + Resolution `extracted to [[<artifact-stem>]]` + extraction footer; OR re-run the same `/extract-artifacts --harvest-row <id>` invocation, which will detect the existing artifact via Step 3 dedup and skip drafting, then complete Step 4.8 to update the row. (Idempotent recovery path; no second artifact created.) |
| Queue-write-back failure mid-dismiss (Branch A; queue file partial-write) | Step 4.8 atomic-write fails in dismiss mode | Filesystem atomicity preserves the file in a known prior-or-new state. Recovery: re-run `/extract-artifacts --harvest-dismiss <id>` — the operation is idempotent in dismiss mode (re-flipping `nick-dismissed` → `nick-dismissed` is a no-op). |

---

## Design Decisions

| DD | Relevance |
|---|---|
| DD-77 | Single-form classification — one artifact per finding |
| DD-78 | ContractSpec on every artifact |
| DD-80 | Pipeline simplification — /identify-artifacts + this skill replace the Proposer |
| DD-92 | ContextSpec on every artifact; universal-vocab constraint; mechanical-copy prohibition; IL classification meta stripped at extraction. Reference: `extracts/rules/confirm-failure-first-tdd.md` |
| DD-95 | Lifecycle pointer (`last_change_session` + `last_change_sl`) on every non-guide create AND update; SL stem validated at write time; both fields overwritten on update; guides excluded. Step 2.7, Step 3 frontmatter template, Step 3 update-mode dedup behavior. |
| DD-97 | Corpus scan + extension proposal before drafting rule or skill artifacts; calibration (i) LLM-loose; propose-don't-decide invariant; closed Codifier-recommendation enum; templates and agents excluded; auto-merge prohibition. Step 1.7. |
| DD-100 | Template version-bump rubric + agent flag-only path. Templates auto-scan + propose to `operations/version-bump-proposals/`; Nick gates per proposal; on rule, write `<name>-v<N+1>.md` with full independent frontmatter (own `source_finding`, own `extraction_date`, own `last_change_*`, own `contract`, own `context`, own `version: <N+1>`). Agents flag-and-exit per DD-82 invariant; explicit `--version-bump <stem>` flag is required for any agent version-bump write. Compute-N from filename enumeration; collision-abort; missing-baseline-abort; never overwrite an existing version. `--version-bump` + `--update` is ill-formed. Step 1.8 + Step 2 filter + Step 3 versioned-write branch + Step 3 frontmatter `version` field. |
| DD-82 | Agent never-auto-create invariant — multi-layer enforcement on this skill: (1) Step 1.8 Branch B flag-and-exit on any agent-classified finding without `--version-bump`; (2) `--version-bump <stem>` requires explicit operator scoping (Nick's prior approval is structural, not skill-resolvable from corpus scan); (3) Branch A guard rejects `--version-bump` on template forms (templates auto-propose); (4) Step 0a defensive abort on any harvest-queue row with `target form: agent` (IB-163 should have suppressed at write-side; defensive abort catches a contract violation upstream). Defensive: any path that would write an agent file without explicit Nick approval is a procedural violation. |
| DD-101 | Harvest-queue row consumer mode. `--harvest-row <id>` accepts a Nick-approved row from `extracts/guides/<stem>.harvest-queue.md` as input; routes through DD-97 (Step 1.7) for rule/skill targets, DD-100 (Step 1.8 Branch A) for template targets; defensive abort for agent targets. `--harvest-dismiss <id>` performs queue-only Status update to `nick-dismissed`. Step 0 input-mode dispatch (mutually exclusive with identification-report mode); Step 0a row resolution + Status check (closed-enum `nick-approved` for promotion; `queued` or `nick-approved` for dismissal); Step 4.8 queue write-back with four branches (A dismissal, B extracted-new, C DD-97 extension proposal pending, D DD-100 version-bump proposal pending) plus defensive Branch E for agent (unreachable per upstream invariants). Atomic-write preserves all other rows byte-equivalent. The skill never auto-polls harvest queues — explicit `--harvest-row` / `--harvest-dismiss` is the only entry path. Single-row-per-invocation contract; multi-row processing via sequential invocations. The original pattern finding (the row's source_finding) remains pattern-classified throughout per DD-101 §Promotion; its `consumed_by[]` array gains the new harvested artifact's pointer alongside the original guide's via Step 5's existing back-annotation logic. DD-77's "Router picks one form, full stop" preserved — harvest is consumer-side resolution at extract time; never Router-side flagging. **IB-166 amendment (session 82):** argument shape canonicalized to `<finding-stem>::<target-form>::<headline-slug>` (matches IB-163's row-heading shape); Step 0a step 2 queue-file resolution auto-locates by literal heading match across `extracts/guides/*.harvest-queue.md`; optional `--guide <guide-stem>` flag disambiguates multi-match. Replaces IB-164's original `<guide-stem>::...` argument shape, which did not survive contact with actual queue-file row headings. |
