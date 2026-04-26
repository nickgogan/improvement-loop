---
name: identify-artifacts
description: >-
  Scan research findings and classify each into a form (pattern/skill/rule/template/agent)
  using the Form Router rubric. Produces an identification report — no artifact drafting.
  Designed for Sonnet subagent parallelization. The report is the input for /extract-artifacts.
  Use this skill first to classify, review, then run /extract-artifacts to draft and write.
user-invocable: true
allowed-tools: Read Grep Glob Write Agent
argument-hint: "<P1|P2|finding-name...> [--category <cat>]"
---

# Identify Artifacts

Scan research findings from the Improvement Loop KB and classify each into one of 5 forms using the Form Router rubric. Produces a structured identification report. No artifact drafting — that's `/extract-artifacts`'s job.

## When to Use This Skill

- Before `/extract-artifacts` — always run this first to classify, then review the report
- After a batch of new findings has been extracted by `/research-loop`
- When Nick wants to survey what artifact forms a set of findings would produce
- To re-classify findings after rubric amendments

## What This Skill Does NOT Do

- **Does not draft artifacts.** Classification only. Drafting is `/extract-artifacts`.
- **Does not write to `extracts/`.** Output is a report in `operations/research-reports/`.
- **Does not modify research findings.** Read-only access to findings.
- **Does not produce guides.** Guides are out of Router scope. But this skill checks pattern findings against the guide routing table (DD-81) and flags unroutable findings.

## Cognitive Disposition

The Identifier thinks like a strict classifier — mechanical, rubric-first, conservative.

- **Rubric-first.** Apply the form classification rubric mechanically. The exclusion criteria do most of the work. Don't freelance — if the rubric says pattern, it's pattern.
- **Conservative on LOW confidence.** LOW-confidence classifications go to HITL tier. Flag the ambiguity clearly so Nick can decide.
- **Level-of-abstraction is the key discriminator.** Philosophy → pattern. Mechanism → rule. Scaffold → template. Procedure → skill. Named role → agent. This resolves ambiguity faster than running all 5 exclusion tests.
- **Evidence-aware filtering.** Weak evidence with no convergent adoption stays as a finding. Filter before classifying.
- **Co-occurrence is noted, not acted on.** If a pattern has an embedded rule, note it. Don't classify as both. DD-77 applies.

---

## Arguments

| Argument | Effect |
|----------|--------|
| `P1` | All findings with `priority: "P1 (Implement Now)"` |
| `P2` | All findings with `priority: "P2 (Design Required)"` |
| `P1 P2` | Both P1 and P2 findings |
| `<finding-name>...` | Specific finding file stems |
| `--category <cat>` | Filter by category (e.g., `--category "Context Engineering"`) |

**No arguments:** prompt for clarification.

---

## Paths

| Path | Purpose |
|------|---------|
| `systems/improvement-loop/research-findings/` | Input — findings to classify |
| `systems/improvement-loop/operations/references/form-classification-rubric.md` | Decision spec — form classification criteria |
| `systems/improvement-loop/extracts/` | Dedup check — skip already-extracted findings |
| `systems/improvement-loop/operations/pattern-identification-reports/` | Output — identification reports |

---

## Procedure

### Step 0: Determine Scope

Parse arguments to build the finding set:

1. **Priority filter:** `P1`, `P2`, or both — use `Grep` to search `systems/improvement-loop/research-findings/` for matching `priority:` values.
2. **Named findings:** match file stems against `research-findings/*.md`.
3. **Category filter:** `--category` — grep for matching `category:` values.
4. **No args:** prompt user for scope.

**Pre-filter (applied before classification):**
- Skip findings with `evidence_strength: "Weak (anecdotal)"` unless explicitly named. Weak-evidence findings aren't ready for artifact production.
- Skip findings with `adoption_status: "Already Adopted"` unless explicitly named. Already-adopted patterns are codified elsewhere.
- Skip findings that already have an extraction note in their body (already processed by `/extract-artifacts`).

**Dedup check:** Use `Grep` to scan `systems/improvement-loop/extracts/` for `source_finding:` values. Remove any finding that already has a staged artifact.

Report the filtered count: "Found N findings matching scope (M filtered out: D dedup, W weak, A adopted). Classifying N."

### Step 1: Prepare Finding Data

For each finding in scope, read the file and extract:

1. **Frontmatter fields:** `name`, `category`, `priority`, `evidence_strength`, `summary`
2. **Filename stem:** the file name without `.md` extension
3. **Body sections:** Include the finding's "What It Is" and "Why It Matters" sections (or the first two substantive body sections if named differently). These sections capture center of gravity more reliably than raw character truncation. If neither section exists, use the first 800 chars of body content.

Format each finding as shown in the subagent prompt template's "Findings to Classify" section.

### Step 2: Load Classification Context

Read the rubric: `systems/improvement-loop/operations/references/form-classification-rubric.md`. Extract §1 through §5 inclusive (Pattern, Skill, Rule, Template, Agent). Stop before the "Open questions" section — the subagents do not need the open questions, schema drift, or calibration sections. The extracted content will be inserted into the subagent prompt where the `[EMBED]` directive appears.

### Step 3: Batch & Classify (Sonnet Subagents)

Group findings into batches of 5-8. For each batch, launch a subagent (model: sonnet) with:

**Subagent prompt template:**

```
You are a strict classifier for the MetaSystem Improvement Loop. Your ONLY job is to assign each research finding to exactly one of 5 artifact forms. Do NOT draft artifacts. Do NOT add commentary outside the JSON output.

## The 5 Forms

| Form | Shape | Key Signal |
|------|-------|------------|
| pattern | Compositional primitive — reusable design approach | "How should I structure this?" Tradeoffs, forces, it-depends character |
| skill | Procedure with inputs/outputs/steps | Ordered steps, explicit invocation, stateless per run |
| rule | Binary constraint enforced at a boundary | "MUST/MUST NOT", deterministic check, enforcement boundary |
| template | Scaffold with variables and a body | Named variables, repeatable generation, fillable backbone |
| agent | Persona with cognitive disposition and durable scope | Single named role, "how it thinks" is the insight, long-lived |

## Classification Rubric

[INSERT HERE: the §1-§5 content extracted from form-classification-rubric.md in Step 2.
Include inclusion signals, exclusion signals, confidence signals, and prior-session exemplars for each form.
Do NOT include the "Open questions", "Schema drift", or "Calibration findings" sections.]

## Classification Procedure (follow IN ORDER for each finding)

For EACH finding, execute these steps sequentially. Do not skip steps.

**Step 1 — Identify the center of gravity.**
Read the finding and answer: "What is the ONE insight that makes this finding valuable? If I removed it, the finding would be worthless."
- Is the insight a reusable SHAPE (a design approach others could apply differently)? → leans pattern.
- Is the insight a specific MECHANISM (the exact procedure, constraint, scaffold, or role)? → leans skill/rule/template/agent.

**Step 2 — Apply the surface-structure trap test.**
Ask: "Does this finding CONTAIN mechanisms (tool specs, tier tables, step sequences, constraint language) as EXAMPLES of a broader design approach?"
- If yes → the mechanisms are instantiations, NOT the center of gravity. Do NOT classify based on them.
- If no → the mechanism IS the insight. Classify accordingly.

Litmus test: "Could someone apply this finding's core insight WITHOUT using the specific mechanism described?" If yes → it's a pattern, regardless of what mechanisms appear in the body.

**Step 3 — Check exclusions for ALL 5 forms.**
For each form, check its exclusion signals from the rubric. Eliminate forms that fail exclusion tests. Exclusion criteria do most of the work.

**Step 4 — Assign the form matching the center of gravity.**
Among remaining forms, pick the one whose inclusion signals match the CENTER OF GRAVITY identified in Step 1 — not the examples, not the terminology, not the surface structure.

**Step 5 — Apply design decision rules.**
- Role count > 1 in the finding biases toward pattern, not agent (DD-76).
- Single form only (DD-77). Pick one. Note co-occurrence if present.
- Confidence measures FORM-CLASSIFICATION certainty, not evidence strength.

## Level-of-Abstraction Discriminator

When in doubt, this is the fastest tiebreaker:

| Level of abstraction | Form |
|---------------------|------|
| Philosophy / design approach / "how to think about X" | pattern |
| Heuristic / decision framework with tradeoffs | pattern |
| Mechanism / specific binary constraint at a boundary | rule |
| Scaffold / fillable structure with named variables | template |
| Procedure / ordered steps with defined inputs/outputs | skill |
| Named role / durable cognitive disposition | agent |

Pattern is the default. When a finding's shape is stable but its instantiation is project-specific, the form is pattern. The other four forms apply only when the specific mechanism IS the insight.

## Common Traps (study before classifying)

**TRAP 1 — "Rules" that are actually heuristics:**
A finding describes three tiers of task complexity for scaling effort. WRONG classification: rule (because "rules" and tiers look like deterministic constraints). CORRECT: pattern — the tiers are heuristics with tradeoffs (static rules may under-allocate, need periodic recalibration). There is no enforcement boundary. The insight is the design approach of embedding scaling guidance, not the specific tier definitions.

**TRAP 2 — Tool specs that are instantiations of a broader shape:**
A finding describes a tool with defined input/output for mid-chain reasoning. WRONG classification: skill (because it has a tool definition with explicit invocation). CORRECT: pattern — the insight is the reusable shape "reserve an ephemeral scratchpad as a distinct tool." The specific tool spec is one instantiation; the shape applies across different domains with different implementations.

**The pattern behind both traps:** When a finding CONTAINS a mechanism (tool spec, tier table, enforcement rule, step sequence) but the mechanism is an EXAMPLE of a broader approach, the form is pattern. Note the mechanism as a co-occurrence, not as the assigned form.

## Confidence Levels

- **HIGH** — form is unambiguous after exclusion tests. No other form is a plausible fit.
- **MED** — form is likely but one alternative remains plausible.
- **LOW** — genuinely ambiguous across two or more forms.

## Tier Dispatch

- HIGH confidence + no override → auto
- HIGH confidence + override → guided
- MED confidence → guided
- LOW confidence → hitl

## Findings to Classify

[For each finding in this batch:]
- **Filename:** [exact filename]
- **Name:** [name from frontmatter]
- **Category:** [category]
- **Priority:** [priority]
- **Evidence Strength:** [evidence_strength]
- **Summary:** [summary from frontmatter]
- **Body excerpt:** [Include "What It Is" and "Why It Matters" sections, or first two substantive body sections. These capture center of gravity better than raw character truncation.]

## Self-Check (apply to EACH finding before outputting)

Before emitting JSON for a finding, verify:
- Did I identify the center of gravity — the finding's ONE key insight?
- Is my assigned form based on the center of gravity, NOT on surface terminology, names, or examples?
- Did I check all 5 exclusion lists from the rubric?
- If the finding contains a mechanism (tool, procedure, constraint, scaffold) — is that mechanism the insight itself, or an example of a broader design approach?

## Output Format (one JSON object per finding, strict)

IMPORTANT: Output ONLY valid JSON objects, one per line. No markdown fencing, no commentary.

{"id": "finding-file-stem", "name": "Finding Name", "category": "Category", "assigned_form": "pattern|skill|rule|template|agent", "confidence": "HIGH|MED|LOW", "tier": "auto|guided|hitl", "reason_codes": ["code1", "code2"], "co_occurrence": null, "rationale": "2-3 sentence explanation: (1) what is the center of gravity, (2) why this form and not alternatives, (3) what exclusions applied"}
```

**Batch launch:** Use the `Agent` tool with `model: "sonnet"` for each batch. Launch all batches in parallel.

### Step 3.5: Curator Priority Review

After subagent classifications are gathered and before writing the report (Step 4), perform a Curator-authority pass over each classified finding's priority.

**Context.** Each finding entered with a `priority` value set by the Researcher at intake (`/promote-findings` or `/research-loop`, per the shared Triage Rules). The Researcher's triage is a useful first guess based on single-finding signal. The Curator's curation pass brings KB-wide signal — form classification result, cross-finding convergence, evidence visible only at aggregate — that the Researcher could not see at intake.

**Per-finding evaluation.** For each classified finding, ask:

1. Does the assigned form + confidence change the priority fit? (E.g., a rule with LOW-confidence form on weak evidence rarely warrants P2. A pattern with HIGH confidence and convergent adoption across 3+ independent orgs rarely stays at P3.)
2. Does cross-KB signal suggest revision? (Search `related_findings` links, source corroboration, convergent implementations across watched libraries.)
3. Does the intake-time Researcher rubric fit the pattern's actual fit now?

**If revision is warranted**, record it in the identification report as a proposal — do NOT write to frontmatter. Nick gates at report review. The report's Details block gains:

```markdown
- **Current priority:** {current} (Researcher triage)
- **Proposed priority:** {proposed} (Curator revision)
- **Revision rationale:** {1-2 sentences citing the KB-wide signal that drove the change}
```

If no revision is warranted, omit the revision block — the finding stays at Researcher-assigned priority.

**Authority.** Curator revisions are authoritative over Researcher initial triage. The Researcher's role is to produce; the Curator's role is to curate. Priority is a curation call.

### Step 4: Collect & Write Report

1. Gather all subagent outputs.
2. Parse JSON results. Flag any malformed outputs for manual review.
3. Sort by tier: `hitl` first, then `guided`, then `auto`.
4. Within each tier, group by `assigned_form`.

**Write the identification report** to `systems/improvement-loop/operations/pattern-identification-reports/{date}-identification-report.md`:

```markdown
---
title: "Artifact Identification Report"
type: "report"
target_system:
  - "improvement-loop"
created: "{date}"
scope: "{scope description}"
findings_scanned: {N}
findings_filtered: {M}
---

# Artifact Identification Report — {date}

**Scope:** {scope description}
**Findings scanned:** {N} | **Filtered out:** {M} (dedup: {D}, weak: {W}, adopted: {A})
**Classified:** {C}

## Summary

| Form | Count | % | Auto | Guided | HITL |
|------|-------|---|------|--------|------|
| pattern | X | X% | X | X | X |
| rule | X | X% | X | X | X |
| template | X | X% | X | X | X |
| skill | X | X% | X | X | X |
| agent | X | X% | X | X | X |

## Candidates

### HITL — Needs Human Decision

| # | Finding | Form | Confidence | Co-occurrence | Status |
|---|---------|------|------------|---------------|--------|
| 1 | [[finding-name]] | ? | LOW | — | PENDING |

### GUIDED — Review Recommended

| # | Finding | Form | Confidence | Co-occurrence | Status |
|---|---------|------|------------|---------------|--------|
| 2 | [[finding-name]] | pattern | MED | rule | PENDING |

### AUTO — Ready for Extraction

| # | Finding | Form | Confidence | Co-occurrence | Status |
|---|---------|------|------------|---------------|--------|
| 3 | [[finding-name]] | pattern | HIGH | — | PENDING |

## Details

### 1. finding-name

- **Assigned form:** pattern
- **Confidence:** HIGH
- **Tier:** auto
- **Reason codes:** reusable_shape, forces_tradeoffs
- **Co-occurrence:** rule (specific constraint embedded)
- **Rationale:** [2-3 sentence explanation from subagent]
- **Status:** PENDING
- **Current priority:** P3 (Researcher triage)  _[include only if Curator revision is proposed]_
- **Proposed priority:** P2 (Curator revision)  _[include only if Curator revision is proposed]_
- **Revision rationale:** [1-2 sentences citing KB-wide signal]  _[include only if Curator revision is proposed]_
- **Priority-revision status:** PENDING  _[include only if Curator revision is proposed; Nick sets APPROVED/REJECTED]_

[Repeat for each finding]
```

**The Status field** is the contract between `/identify-artifacts` and `/extract-artifacts`:
- `PENDING` — not yet reviewed (default)
- `APPROVED` — approved for extraction (user sets this)
- `REJECTED` — skip this finding (user sets this)
- `REDIRECTED` — user changed the assigned form (user edits the form field and sets this status)

Nick edits the report in Obsidian or a text editor before running `/extract-artifacts`.

### Step 5: Present Summary

Show the summary table and tier counts inline to the user. Point them to the report file for detailed review.

```
Identification report written to: systems/improvement-loop/operations/pattern-identification-reports/{date}-identification-report.md

Summary: {C} findings classified
  - {auto_count} auto (ready for extraction)
  - {guided_count} guided (review recommended)
  - {hitl_count} hitl (needs human decision)
  - Form distribution: {pattern_count} pattern, {rule_count} rule, {template_count} template, {skill_count} skill, {agent_count} agent
  - Co-occurrences noted: {co_count}

Next:
  - Pattern findings → /synthesize-guide (DD-81)
  - Non-pattern findings → /extract-artifacts {date}-identification-report.md
  - {unrouted_count} findings did not map to an existing guide cluster (see Unrouted section in report)
```

### Step 6: Guide Cluster Check (DD-81) + Lifecycle-Trigger Detection (DD-98)

After classification, check each **pattern-classified** finding against the guide routing table at `systems/improvement-loop/operations/references/guide-routing-table.md`. Also evaluate per-cluster lifecycle triggers (DD-98 split-trigger) at the same routing-table read.

1. Read the routing table.
2. For each pattern finding, match its `category` to a research dimension, then look up the dimension's primary guide cluster.
3. If a guide cluster exists → the finding is **routed**. No action needed.
4. If no guide cluster maps → add the finding to the **Unrouted Bucket** section of the routing table.
5. After processing all findings, check: does the unrouted bucket now contain 5+ findings with `same-problem` relationships? If yes, flag a **candidate cluster** in the identification report summary.

**Step 6.a — Split-Trigger Detection (DD-98).** For each Active Cluster in the routing table whose finding-count crosses the threshold:

For each Active Cluster row in the routing table, evaluate the DD-98 split trigger (conjunction; both required):

(i) **Finding-count threshold:** the cluster's current `source_findings[]` count is ≥25. Use the routing table's snapshot count or recompute from the guide's frontmatter — both are acceptable for the heads-up; the proposal artifact (emitted below) cites the recomputed count.

(ii) **Practitioner-question threshold:** the cluster covers ≥2 distinct practitioner questions. Detection is LLM-judgmental, calibrated like DD-97 — read the cluster's findings (or the guide's body if synthesized) and identify the questions readers would bring. False-positives caught at Nick's gate.

**Outcome dispatch (mirrors `/synthesize-guide` Step 0.7):**

| Trigger result | Action |
|----------------|--------|
| **Both thresholds met** | (a) Emit split-proposal file at `operations/split-proposals/<YYYY-MM-DD>-<guide-stem>-split-proposal.md` with the same shape as `/synthesize-guide` Step 0.7 emits. (b) Surface a heads-up in the identification report summary: "⚠ DD-98 split trigger fired for cluster `<guide-stem>` — proposal at `operations/split-proposals/<filename>`." |
| **Count ≥25 only (single coherent question)** | NO proposal file. Surface inline in identification report: "G-`<stem>` at <count> findings; remains single-question. Monitor for question bifurcation on next cycle." |
| **Question count ≥2 only (count <25)** | NO proposal file. Surface inline: "G-`<stem>` at <count> findings; touches `<N>` practitioner questions but below volume threshold. Monitor for volume crossing." |
| **Neither** | No-op. |

**Read-only by contract.** This step never auto-executes a split, never writes destination guides, never updates the routing table, never deprecates the source guide, never modifies DD-94 changelog files. Both detection paths (`/synthesize-guide` Step 0.7 AND `/identify-artifacts` Step 6.a) emit identical proposal artifact shapes — the proposal path and shape are skill-agnostic. If both skills detect on the same trigger in the same cycle, both emissions are written (filename collision triggers `-2`/`-3` suffix); Nick reads the latest and the duplicates are audit-trail.

**Step 6.b — Theme-Graduation Detection (DD-99).** For the Unrouted Bucket section of the routing table, evaluate the DD-99 graduation trigger (conjunction; both required):

(i) **Finding-count threshold:** the bucket holds ≥5 unrouted findings clustered by category, tag, or `same-problem` link.

(ii) **Linkage threshold:** at least one `same-problem` relationship spans the cluster (per the four-relationship type system codified by `/finding-crosslink`). Categorical co-occurrence WITHOUT `same-problem` linkage does NOT trigger graduation — that's a tag mistake, not a coherent emerging theme.

**Outcome dispatch:**

| Trigger result | Action |
|----------------|--------|
| **Both thresholds met** | (a) Flag the cluster in the identification report's 'Candidate Cluster' section per spec §2.4 with a `**DD-99 graduation candidate**` marker. (b) Emit a structured graduation-proposal artifact at `operations/graduation-proposals/<YYYY-MM-DD>-<theme>-graduation-proposal.md` with PROMOTE / ABSORB / DEFER recommendation per the proposal shape below. (c) Surface a heads-up in the identification report summary: "⚠ DD-99 graduation trigger fired for theme `<theme>` — proposal at `operations/graduation-proposals/<filename>`." |
| **Count ≥5 only (no `same-problem` linkage)** | NO proposal. Cluster is categorical co-occurrence; surface inline in the identification report's narrative ("Unrouted bucket has `<count>` findings tagged `<category>`; no `same-problem` linkage detected — likely categorical accident, not an emerging theme.") and continue. |
| **Linkage present but count <5** | NO proposal. Sub-threshold mass; surface inline as informational ("Unrouted bucket has `<count>` findings with `same-problem` linkage; below volume threshold. Monitor for additional findings."). |
| **Neither** | No-op. |

**Cross-dimension flag.** If the cluster's findings span ≥2 existing dimensions per the routing table's Dimension → Guide mapping, set the proposal's cross-dimension flag. **Cross-dimension findings disqualify ABSORB** — Codifier's recommendation MUST be PROMOTE or DEFER; ABSORB-with-cross-dimension is invalid by contract per DD-99 §The Constraint.

**Graduation-proposal artifact shape (per DD-99 §Response):**

```markdown
---
type: "graduation-proposal"
target_system:
  - "improvement-loop"
generated_by: "/identify-artifacts"
date: "<YYYY-MM-DD>"
theme_name: "<proposed-theme-name>"
finding_count: <int>
cross_dimension: <bool>
session: <int>
sl: "<active-sl-stem>"
---

# Graduation Proposal — <Proposed Theme Name>

## Theme identity

- **Proposed theme name:** "<theme name>"
- **Current Unrouted Bucket entries:** [[finding-stem-1]], [[finding-stem-2]], ... (total finding count <int>)

## Linkage map

`same-problem` relationships among the findings:

- [[finding-1]] ↔ [[finding-2]] (same-problem: "<problem statement>")
- [[finding-2]] ↔ [[finding-3]] (same-problem: "<problem statement>")
- ...

(Cross-category and cross-dimension links called out explicitly.)

## Cross-dimension flag

`cross_dimension: <true | false>` — set when findings span ≥2 existing dimensions per the routing table's Dimension → Guide mapping.

## Path recommendation (closed enum)

**Recommendation:** `PROMOTE — new dimension + guide cluster` | `ABSORB — into existing dimension` | `DEFER — sub-threshold linkage`

**Rationale:** <1–3 lines explaining why this recommendation. Cite structural distinctness (PROMOTE), sub-theme-of-existing-dimension fit (ABSORB), or weak linkage / single connector (DEFER).>

**Note on cross-dimension constraint:** if `cross_dimension: true`, ABSORB is INVALID — recommendation MUST be PROMOTE or DEFER per DD-99 §The Constraint.

## Per-path execution sketch

What artifacts the executing path would touch:

- **PROMOTE:** `operations/references/research-dimensions.md` (add new dimension entry); routing table (add new Active Cluster row + new Synthesis Status row + Dimension → Guide mapping update + Unrouted Bucket entries removed + History entry); new guide stub at `extracts/guides/<new-stem>.md` via `/synthesize-guide`; new companion changelog with `theme-graduation` first entry (per DD-94 enum amendment).
- **ABSORB:** routing table (Dimension → Guide mapping updated to reflect absorbed sub-theme; Unrouted Bucket entries removed; History entry; no new Active Cluster row); `/dimension-rebalance` run reclassifies affected findings to destination dimension; destination guide's next regen uses `dimension-rebalance` trigger (DD-94 enum existing tag — no amendment needed for ABSORB path).
- **DEFER:** no execution; cluster monitored on next research-loop cycle.
```

**Stale-proposal hygiene.** If between proposal emission and Nick's ruling the cluster's finding count drops below 5 (a finding gets reclassified, the bucket gets repaired by `/linkage-repair`, etc.), Codifier flags the proposal as stale on the next detection cycle: append `## Stale as of <YYYY-MM-DD>` header below the title heading. The stale proposal is RETAINED for audit (not deleted); a new proposal supersedes if the cluster re-crosses threshold later.

**Read-only by contract.** Step 6.b never auto-executes either path: never edits research-dimensions.md, never updates the routing table, never creates new guide stubs, never invokes `/dimension-rebalance`. Execution requires Nick's ruling — DD for PROMOTE; ruling-on-proposal + routing-table update + `/dimension-rebalance` invocation for ABSORB.

**One proposal, one recommendation.** Per DD-99 §Rules #3, the proposal carries exactly ONE path recommendation. Ambiguity (PROMOTE-vs-ABSORB undecided) defaults to DEFER with explanation; emitting a proposal without a recommendation is a defect.

**Report addition:**
```
Guide routing: {routed_count} pattern findings mapped to guide clusters, {unrouted_count} unrouted.
{If candidate cluster detected:} ⚠ Candidate guide cluster detected in unrouted bucket ({count} related findings). Review for new guide creation.
{If split trigger fired (DD-98):} ⚠ Split trigger fired for {S} cluster(s): {list of guide-stems}. Proposals at operations/split-proposals/.
{If single-condition observation (DD-98):} Monitor: {list of cluster observations from the dispatch table}.
{If graduation trigger fired (DD-99):} ⚠ Graduation trigger fired for theme '{theme}': {finding count} findings with same-problem linkage. Proposal at operations/graduation-proposals/<filename>. Recommendation: {PROMOTE|ABSORB|DEFER}.
{If single-condition graduation observation (DD-99):} Monitor: {bucket-state observation from the dispatch table}.
```

### Step 7: Back-Annotate Finding Files

After the identification report is written AND Nick has gated proposals, update each classified finding file's frontmatter:

1. Set `pipeline_status: "classified"` on every finding that was classified in this run.
2. Leave `consumed_by: []` — this field is populated later by `/extract-artifacts` or `/synthesize-guide`.
3. **If a Curator priority revision was proposed in Step 3.5 AND Nick approved it**, update `priority` to the new value. Do NOT write priority without Nick's approval — revisions are proposals until gated.

This enables unified pipeline tracking. A finding's `pipeline_status` field answers "where is this finding in the pipeline?" without checking multiple locations.

---

## Rules

1. **Classification + curation, not extraction.** This skill classifies form (Step 3) and reviews Researcher priority triage (Step 3.5). Do not draft artifacts, do not write to `extracts/`.
2. **Rubric is the decision spec.** Apply it mechanically. The rubric was calibrated against 50 findings (session 22).
3. **Single form per finding** (DD-77). Note co-occurrence but do not classify as both.
4. **Dedup is mandatory.** Check `extracts/` before classifying. Don't re-identify already-extracted findings.
5. **Weak evidence stays as findings.** Skip `evidence_strength: "Weak (anecdotal)"` unless explicitly named.
6. **Report format is a contract.** The Status/Form fields in the report are what `/extract-artifacts` reads. Don't change the format without updating `/extract-artifacts`.
7. **One report per run.** If a report already exists for today's date, append a sequence number (`-2`, `-3`).
8. **Curator authority on priority.** Initial priority is set by the Researcher at intake (`/promote-findings`, `/research-loop`). Curator revisions proposed in Step 3.5 are authoritative when Nick-approved — Researcher triage is a first guess, not the final word. Periodic bulk re-evaluation belongs to `/reassess-priorities`.

---

## Failure Modes

| Failure | Detection | Recovery |
|---------|-----------|----------|
| Subagent returns malformed JSON | JSON parse error in Step 3 | Log the batch, re-run with smaller batch size |
| All findings classify as pattern | >95% pattern rate | Expected — 92% pattern is the calibration baseline. Only flag if named non-pattern findings are misclassified. |
| Subagent ignores rubric exclusions | Form assignment contradicts clear exclusion signal | Flag in report with a note; Nick decides at review time |
| DD-98 split single-condition observation (count ≥25 only OR question ≥2 only) | Step 6.a dispatch table single-condition path | NO proposal file. Inline informational note in identification report only ("G-`<stem>` at <count> findings; remains single-question" or analogous). Monitor on next routing-table read. Mirrors `/synthesize-guide` Step 0.7's single-condition behavior. |
| DD-99 graduation single-condition observation (count ≥5 with NO same-problem links, OR linkage with count <5) | Step 6.b dispatch table single-condition path | NO proposal file. Inline note in identification report ("Unrouted bucket has `<count>` findings tagged `<category>`; no `same-problem` linkage detected" OR "`<count>` findings with linkage; below volume threshold"). Monitor on next cycle. |
| Cross-dimension graduation cluster + Codifier proposes ABSORB | Step 6.b cross-dimension flag check | INVALID by contract (DD-99 §The Constraint). Codifier MUST set recommendation to PROMOTE or DEFER on cross-dimension clusters. If a proposal with `cross_dimension: true` AND `recommendation: ABSORB` is emitted, it is defective; Nick rejects and re-emission is required. Surface in next governance audit. |
| Stale graduation-proposal cycle: cluster drops below 5 between emission and Nick gate | Step 6.b detection cycle finds finding count <5 for a theme with an open graduation proposal | Append `## Stale as of YYYY-MM-DD` header below the proposal's title heading. Stale proposal RETAINED for audit (not deleted). New proposal emitted if cluster re-crosses threshold later. |
| Split-proposal or graduation-proposal filename collision (same theme/guide, same day) | Step 6.a or Step 6.b atomic-write check | Append `-2`, `-3` to colliding filename. Both proposals retained for audit; Nick reads the latest. |

---

## Design Decisions

| DD | Relevance |
|---|---|
| DD-75 | Override drops to guided tier |
| DD-76 | Role count > 1 biases toward pattern |
| DD-77 | Single-form classification; co-occurrence noted only |
| DD-80 | Pipeline simplification — this skill + /extract-artifacts replace the Proposer |
| DD-98 | Guide split procedure — Step 6.a evaluates the conjunction (count ≥25 AND practitioner-question count ≥2) at routing-table read; on match, emits a split-proposal artifact at `operations/split-proposals/` with per-finding bifurcation, preserved-section disposition (DD-93), routing-table impact, and Codifier recommendation. Read-only by contract — never auto-executes; never modifies the source guide, routing table, or DD-94 changelog files. Both `/identify-artifacts` Step 6.a AND `/synthesize-guide` Step 0.7 share identical emission semantics. Single-condition observations surface inline in the identification report; do NOT emit a proposal file. |
| DD-99 | Theme graduation procedure — Step 6.b evaluates the Unrouted Bucket conjunction (count ≥5 AND ≥1 `same-problem` link spans the cluster) at routing-table read. On both-thresholds match: flags the cluster in the identification report's Candidate Cluster section AND emits a graduation-proposal artifact at `operations/graduation-proposals/<YYYY-MM-DD>-<theme>-graduation-proposal.md` with PROMOTE/ABSORB/DEFER recommendation. Cross-dimension findings disqualify ABSORB (recommendation MUST be PROMOTE or DEFER). One proposal, one recommendation; ambiguity defaults to DEFER. Read-only by contract — never edits research-dimensions.md, never updates routing table, never creates new guide stubs, never invokes `/dimension-rebalance`. Stale-proposal hygiene: append `## Stale as of <date>` header on next detection cycle if cluster drops below 5; proposal retained for audit. PROMOTE path uses DD-94's new `theme-graduation` enum tag on the new guide's first changelog entry (per IB-160 enum amendment); ABSORB path uses the existing `dimension-rebalance` tag on the destination guide's next regen. |
