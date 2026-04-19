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
| `P1` | All findings with `proposer_priority: "P1 (Implement Now)"` |
| `P2` | All findings with `proposer_priority: "P2 (Design Required)"` |
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

1. **Priority filter:** `P1`, `P2`, or both — use `Grep` to search `systems/improvement-loop/research-findings/` for matching `proposer_priority:` values.
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

1. **Frontmatter fields:** `name`, `category`, `proposer_priority`, `evidence_strength`, `summary`
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
- **Priority:** [proposer_priority]
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

### Step 6: Guide Cluster Check (DD-81)

After classification, check each **pattern-classified** finding against the guide routing table at `systems/improvement-loop/operations/references/guide-routing-table.md`:

1. Read the routing table.
2. For each pattern finding, match its `category` to a research dimension, then look up the dimension's primary guide cluster.
3. If a guide cluster exists → the finding is **routed**. No action needed.
4. If no guide cluster maps → add the finding to the **Unrouted Bucket** section of the routing table.
5. After processing all findings, check: does the unrouted bucket now contain 5+ findings with `same-problem` relationships? If yes, flag a **candidate cluster** in the identification report summary.

Report addition:
```
Guide routing: {routed_count} pattern findings mapped to guide clusters, {unrouted_count} unrouted.
{If candidate cluster detected:} ⚠ Candidate guide cluster detected in unrouted bucket ({count} related findings). Review for new guide creation.
```

### Step 7: Back-Annotate Finding Files

After the identification report is written, update each classified finding file's frontmatter:

1. Set `pipeline_status: "classified"` on every finding that was classified in this run.
2. Leave `consumed_by: []` — this field is populated later by `/extract-artifacts` or `/synthesize-guide`.

This enables unified pipeline tracking. A finding's `pipeline_status` field answers "where is this finding in the pipeline?" without checking multiple locations.

---

## Rules

1. **Classification only.** Do not draft artifacts, do not write to `extracts/`.
2. **Rubric is the decision spec.** Apply it mechanically. The rubric was calibrated against 50 findings (session 22).
3. **Single form per finding** (DD-77). Note co-occurrence but do not classify as both.
4. **Dedup is mandatory.** Check `extracts/` before classifying. Don't re-identify already-extracted findings.
5. **Weak evidence stays as findings.** Skip `evidence_strength: "Weak (anecdotal)"` unless explicitly named.
6. **Report format is a contract.** The Status/Form fields in the report are what `/extract-artifacts` reads. Don't change the format without updating `/extract-artifacts`.
7. **One report per run.** If a report already exists for today's date, append a sequence number (`-2`, `-3`).

---

## Failure Modes

| Failure | Detection | Recovery |
|---------|-----------|----------|
| Subagent returns malformed JSON | JSON parse error in Step 3 | Log the batch, re-run with smaller batch size |
| All findings classify as pattern | >95% pattern rate | Expected — 92% pattern is the calibration baseline. Only flag if named non-pattern findings are misclassified. |
| Subagent ignores rubric exclusions | Form assignment contradicts clear exclusion signal | Flag in report with a note; Nick decides at review time |

---

## Design Decisions

| DD | Relevance |
|---|---|
| DD-75 | Override drops to guided tier |
| DD-76 | Role count > 1 biases toward pattern |
| DD-77 | Single-form classification; co-occurrence noted only |
| DD-80 | Pipeline simplification — this skill + /extract-artifacts replace the Proposer |
