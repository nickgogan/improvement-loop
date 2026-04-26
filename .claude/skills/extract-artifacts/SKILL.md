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

---

## Procedure

### Step 0: Load Report

1. Parse the argument to find the identification report:
   - Named file: read `systems/improvement-loop/operations/pattern-identification-reports/{arg}`
   - `--latest`: glob for `*-identification-report*.md` in `operations/pattern-identification-reports/`, sort by date, take the most recent
2. Read the report. Parse the Details section to extract per-finding entries: `id`, `assigned_form`, `confidence`, `tier`, `reason_codes`, `co_occurrence`, `rationale`, `Status`.
3. Report: "Loaded identification report: {filename}. {N} findings total."

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

### Step 2: Draft Artifacts (Subagents)

**Filter out extension-proposed findings.** Per Step 1.7, any rule or skill finding tagged `extension_status: "proposed"` is routed to the extension-proposals report and does NOT proceed to drafting. Template and agent findings, plus rule/skill findings tagged `extension_status: "no_match"`, proceed normally.

For each approved finding **not flagged for extension proposal**:

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
   - **Default mode (no `--update`):** if an existing artifact has the same `source_finding`, skip per Rule #4 (dedup-at-write). If a different artifact uses the same filename, append `-2`, `-3` to the new artifact's filename.
   - **Update mode (`--update`):** if an existing artifact has the same `source_finding`, this is a re-extraction. Read the existing artifact's frontmatter to capture preserve-on-update fields: `extraction_date`, `deployed`, `deployed_to`. The new body + ContractSpec + ContextSpec replace the existing ones. The two preserved fields are written back verbatim. `last_change_session` + `last_change_sl` are overwritten with the active session's values from Step 2.7 (no preservation; the SL chain carries the prior pointer). Filename is unchanged.

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
