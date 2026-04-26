---
name: synthesize-guide
description: >-
  Synthesize multiple research findings into an end-directed guide with embedded templates
  and prompt scaffolds. Produces actionable playbooks — the consumable product of the
  Improvement Loop for pattern-classified findings. Human gate before writing.
user-invocable: true
allowed-tools: Read Grep Glob Write Edit Agent
argument-hint: "<topic|--dimension DIM|--findings ID1,ID2,...> [--auto]"
---

# Synthesize Guide

Aggregate pattern-classified research findings into end-directed guides with embedded templates, prompt scaffolds, decision trees, and worked examples. This skill produces the actionable output of the Improvement Loop — the guidance and reusable assets that practitioners use when building agent systems.

## When to Use This Skill

- After `/identify-artifacts` has classified findings and Nick has reviewed the report
- When a cluster of pattern findings share a theme (e.g., "context management", "evaluation design")
- When Nick requests a guide on a specific topic
- To convert raw research into usable playbooks with templates

## What This Skill Does NOT Do

- **Does not classify findings.** That's `/identify-artifacts`'s job.
- **Does not extract rules/skills/templates/agents.** That's `/extract-artifacts`'s job (DD-81).
- **Does not deploy guides.** Draft guides stage in `extracts/guides/`. Deployment to `meta-system/knowledge/guides/` is a separate human act.

## Cognitive Disposition

The Guide Author thinks like a technical writer and practitioner — not a researcher, not an analyst.

- **End-directed.** Every section answers "how do I do X?" not "what is the theory of X?" If a reader can't act on it, it's not guide material.
- **Template-rich.** Every major concept should have a fillable scaffold. A guide about agent specifications should include a template with `{{OBJECTIVE}}`, `{{HEALTH_METRICS}}`, `{{STOP_RULES}}` slots — not just a description of what those fields are.
- **Example-driven.** Templates are abstract; examples make them concrete. At least one worked example per template showing what a filled-in version looks like.
- **Synthesis over compilation.** Don't list patterns sequentially. Synthesize them into a coherent procedure. The reader shouldn't need to know which findings were sourced — the guide should read as a unified document.
- **Failure-aware.** Every guide includes a Pitfalls section synthesized from finding failure modes. What goes wrong when people try this?

---

## Arguments

| Argument | Effect |
|----------|--------|
| `<topic>` | A topic string (e.g., "agent context management"). Skill finds relevant findings by category and related_findings graph. |
| `--dimension DIM` | A research dimension name (e.g., "Context Engineering"). Collects all P1 findings in that dimension. |
| `--findings ID1,ID2,...` | Explicit comma-separated finding file stems. Most precise input. |
| `--trigger TAG` | Re-synthesis trigger tag for the companion changelog entry (DD-94). Required on re-synthesis. Closed enum: `staleness-threshold` \| `nick-request` \| `dimension-rebalance` \| `finding-removed` \| `structural-edit`. The skill rejects any other value. Ignored on initial synthesis. |
| `--session NN` | Active session number for the changelog entry (DD-94). Required on re-synthesis. Skill prompts if missing (unless `--auto`, which aborts). Ignored on initial synthesis. |
| `--auto` | Skip human confirmation of finding selection — draft immediately. Use only when the finding set is pre-curated. |

**No arguments:** prompt for topic or dimension.

---

## Paths

| Path | Purpose |
|------|---------|
| `systems/improvement-loop/research-findings/` | Input — source finding files |
| `systems/improvement-loop/operations/references/research-dimensions.md` | Input — dimension definitions for `--dimension` mode |
| `systems/improvement-loop/operations/references/guide-routing-table.md` | Input — dimension→guide mapping, unrouted bucket, trigger keywords |
| `systems/improvement-loop/extracts/guides/` | Output — staged guide drafts |
| `systems/improvement-loop/extracts/patterns/` | Reference — pattern artifacts from initial extraction (optional enrichment) |
| `systems/meta-system/knowledge/guides/` | Reference — existing deployed guides (match format) |

---

## Procedure

### Step 0: Resolve Finding Set

1. **Read the guide routing table** at `systems/improvement-loop/operations/references/guide-routing-table.md`. This is the authoritative mapping between dimensions, guide clusters, findings, and **synthesis status** (last synthesized date, finding count at synthesis, output path, status).

2. **Check synthesis status.** If the target cluster has been synthesized before, report the prior run date, finding count at that time, and current finding count. If current count exceeds prior count by 3+, note that the guide is stale and should be re-synthesized. If the guide already exists and the finding count hasn't changed, confirm with the user before re-running.

3. Parse the argument to determine input mode:
   - **Topic:** Match the topic against the routing table's trigger keywords to identify the target guide cluster. Use the cluster's dimensions to query findings by `category:`. Also traverse `related_findings:` links (rel: `same-problem`) from matches to expand the set. Filter to `priority: P1`.
   - **Dimension:** Look up the dimension in the routing table to find its primary and secondary guide clusters. Grep finding files for matching category. Filter to P1.
   - **Finding list:** Read each specified finding file directly.

3. **Check unrouted bucket.** Scan the routing table's Unrouted Bucket for findings that share `same-problem` links with the resolved set. Offer these as candidates for inclusion.

4. Report: "Found {N} findings for topic/dimension '{X}'. {U} unrouted findings may also be relevant."

5. Display the finding list with names and categories.

6. Unless `--auto`: ask Nick to confirm, add, or remove findings from the set.

7. **Flag unroutable findings.** If any findings in the confirmed set don't map to the target guide cluster via the routing table, note them. After the guide is written, add them to the routing table's Unrouted Bucket if they truly don't fit, or update the routing table if the guide's scope has expanded.

### Step 0.5: Pre-Regen Preservation Capture (re-synthesis only) — DD-93

If the target guide file does **not** yet exist in `extracts/guides/`, this step is a no-op — proceed to Step 1.

If the target guide already exists, this is a re-synthesis. Two surfaces are preserved verbatim across the regen (DD-93):

1. **Canonical named section.** The body of any `## Nick's Annotations` section (heading not included; body only — every line between the heading and the next `^## ` heading or EOF).
2. **Marked regions.** The body of every block bounded by `<!-- PRESERVE -->` and `<!-- /PRESERVE -->` HTML comments. Multiple regions are supported. Markers are not preserved; only the content between them is preserved.

**Capture procedure:**

1. Read the existing guide file at `systems/improvement-loop/extracts/guides/<guide-stem>.md`.
2. Parse and extract:
   - **Annotations capture:** locate `^## Nick's Annotations\s*$`. If found, capture (a) the byte-content of the section body (everything from the line after the heading up to but excluding the next `^## ` heading or EOF), and (b) the section's **ordinal position** among `^## ` headings (1-indexed, including the title `# ` heading? — no: count only `## ` level-2 headings). If absent, mark `annotations_present: false`.
   - **Marked-region capture:** scan the file for every `<!-- PRESERVE -->` … `<!-- /PRESERVE -->` pair in document order. For each region, capture (a) the byte-content between the markers (excluding the markers themselves), (b) the **anchor section** — the `^## ` heading immediately preceding the opening marker (by name), and (c) the ordinal index of the region within that anchor section (1st, 2nd, … marked region under that heading).
3. Validate marker structure:
   - Every `<!-- PRESERVE -->` must have a matching closing `<!-- /PRESERVE -->`. Unmatched markers are an error — abort the synthesis with a structured error report (which marker is unmatched, line number, recommended fix).
   - Markers MUST NOT nest. A second `<!-- PRESERVE -->` before the first `<!-- /PRESERVE -->` is an error — abort.
4. Hold all captured content in memory under a `preserved` structure:
   ```
   preserved = {
     annotations: { present: bool, body: str, ordinal: int },
     regions: [
       { anchor_section: str, ordinal_in_section: int, body: str },
       ...
     ]
   }
   ```
   This structure is the input to Step 3.5 (re-insertion) and Step 3.7 (regression test).
5. **Report to user (unless `--auto`):** "Re-synthesis detected. Preserved surfaces captured: annotations={present|absent}, marked-regions=N." This is informational; no human gate.

A guide with no `## Nick's Annotations` section and no marked regions has `preserved` empty — Steps 3.5 and 3.7 are no-ops, and behavior is identical to the legacy full-regenerate path.

### Step 0.7: Split-Trigger Detection (DD-98) — re-synthesis only

Read-only detection step. Evaluates the DD-98 split trigger against the resolved finding set + routing-table cluster identity (from Step 0). On match, emits a split-proposal artifact at `operations/split-proposals/<YYYY-MM-DD>-<guide-stem>-split-proposal.md`. Never auto-executes a split; never writes destination guide files; never updates the routing table; never modifies DD-94 changelog files. The regen of the source guide continues regardless — the proposal is a side-channel artifact for Nick's gate.

If the target guide does not yet exist (initial synthesis), this step is a no-op — the trigger evaluates against an existing cluster's finding mass + question bifurcation; a brand-new guide has neither yet.

**Trigger evaluation (conjunction; both required per DD-98 §The Constraint):**

1. **Finding-count threshold.** The resolved cluster's `source_findings[]` (or its routed cluster as enumerated by the routing table) contains ≥25 findings. Use the resolved count from Step 0 (post finding-set confirmation; not the routing table's snapshot count, which may lag).

2. **Practitioner-question threshold.** The findings cluster around ≥2 distinct practitioner questions. Detection is LLM-judgmental, calibrated like DD-97 — read the findings' `summary` and body sections; identify the questions readers would bring (e.g., 'How do I structure my agent?' vs. 'How do I evaluate it?'). False-positives caught at Nick's gate. The judgment runs over the absorbed finding set; reasonable confidence is sufficient.

**Outcome dispatch:**

| Trigger result | Action |
|----------------|--------|
| **Both thresholds met** | Emit split-proposal file (procedure below). Regen continues against existing structure. |
| **Count ≥25 only (single coherent question)** | NO proposal file. Surface inline in synthesis report: "G-`<stem>` at <count> findings; remains single-question. Monitor for question bifurcation on next regen." |
| **Question count ≥2 only (count <25)** | NO proposal file. Surface inline: "G-`<stem>` at <count> findings; touches `<N>` practitioner questions but below volume threshold. Monitor for volume crossing." |
| **Neither threshold met** | No-op. No surface in run report. |

**Proposal file path:** `operations/split-proposals/<YYYY-MM-DD>-<guide-stem>-split-proposal.md`. The directory is created lazily on first proposal emission (not pre-created).

**Proposal file shape (per DD-98 §Response):**

```markdown
---
type: "split-proposal"
target_system:
  - "improvement-loop"
generated_by: "/synthesize-guide"
date: "<YYYY-MM-DD>"
source_guide: "<guide-stem>"
finding_count: <int>
practitioner_question_count: <int>
session: <int>
sl: "<active-sl-stem>"
---

# Split Proposal — <Guide Title>

## Source guide identity

- **Guide stem:** `<guide-stem>`
- **Current title:** "<Guide Title>"
- **Finding count:** <N> (post-resolution; ≥25)
- **Routing-table row:** [link to row in `operations/references/guide-routing-table.md`]

## Practitioner-question analysis

The source cluster covers <K> distinct practitioner questions:

1. **Q1:** "<question text>"
   - Findings clustering against Q1: [[finding-stem-1]], [[finding-stem-2]], ...
2. **Q2:** "<question text>"
   - Findings clustering against Q2: [[finding-stem-X]], [[finding-stem-Y]], ...

(Repeat for K questions; ≥2 by trigger condition.)

## Proposed bifurcation

Destination guide names (working draft; per-split DD codifies finals):

- **Destination A:** `<proposed-stem-A>` — practitioner question: "<Q1>"
- **Destination B:** `<proposed-stem-B>` — practitioner question: "<Q2>"

Per-finding routing (every finding routed; no implicit handling per DD-98 §Rules #4):

| Finding | Disposition |
|---------|-------------|
| [[finding-stem-1]] | A |
| [[finding-stem-2]] | A |
| [[finding-stem-X]] | B |
| [[finding-stem-shared]] | shared (route to both) |
| [[finding-stem-contested]] | contested (Codifier cannot route confidently) |

## Preserved-section disposition (DD-93)

Source guide's preserved surfaces, per region (every region disposed explicitly per DD-98 §Rules #5):

- **`## Nick's Annotations` block:** route to A | route to B | duplicate to both | (rationale)
- **`<!-- PRESERVE -->` region #1 (anchor: "<section name>"):** route to A | route to B | duplicate to both | (rationale)
- **`<!-- PRESERVE -->` region #2 (anchor: "<section name>"):** route to A | route to B | duplicate to both | (rationale)

(Repeat for every captured region; if no preserved surfaces, write "Source guide has no preserved sections per DD-93 capture.")

## Routing-table impact

- **Source guide:** proposed deprecation (`stage: deprecated`) post-split.
- **New rows:**
  - `<proposed-stem-A>` — practitioner question, dimensions, lifecycle stage = `draft`.
  - `<proposed-stem-B>` — practitioner question, dimensions, lifecycle stage = `draft`.
- **Dimension → Guide mapping changes:** [list any dimension routing updates].

## Codifier recommendation

Closed enum: `proceed with split as proposed` | `defer pending more findings` | `re-evaluate practitioner-question bifurcation` | `absorb into adjacent guide instead`

**Recommendation:** <one of the four enum values>

**Rationale:** <1–3 lines explaining why this recommendation. Cite the bifurcation precision (% routed cleanly vs. shared vs. contested), the preservation disposition complexity, or any structural concerns.>

## Notes

(Optional: edge cases, ambiguity, follow-ups.)
```

**Atomic write.** Construct the proposal file content; check for filename collision (rare but possible if two regens of the same guide run on the same day; append `-2`, `-3` if needed); write the file. Do NOT write any other artifact in this step. Do NOT update the source guide, routing table, or any changelog.

**Report to user (always):** "Split-trigger detection: <outcome>. " followed by:
- If proposal emitted: "Proposal at `operations/split-proposals/<filename>`. Nick rules per proposal — execution requires a per-split DD per DD-98."
- If single-condition observation: the inline note text from the dispatch table.
- If no-op: omit (no run-report surface).

**Idempotency.** Re-running a regen on the same day with the same finding set may re-emit a proposal — but the proposal file's filename collision check appends `-2` etc. Subsequent proposals are not duplicates of prior content (regen captures may differ); they're additional artifacts. Nick reads the latest one.

### Step 1: Read and Analyze Findings

1. Read all confirmed finding files in full.
2. If corresponding pattern artifacts exist in `extracts/patterns/`, read those too (they contain structured Problem/Forces/Solution that enriches synthesis).
3. Identify subtopic clusters within the finding set. Group findings that address the same concern or form a natural sequence.
4. Report: "Organized into {M} subtopic clusters: {list}."

### Step 2: Determine Guide Structure

Based on the finding clusters, design the guide outline:

```markdown
# [Guide Title]

## When to Use This Guide
[Who is this for? What problem does it solve? When do you reach for it?]

## Key Concepts
[Synthesized from findings — the 3-5 essential ideas the reader needs]

## [Procedure/Decision Sections — one per subtopic cluster]
[End-directed: "Here's how to do X"]
[Include decision trees where choices exist]

## Templates
[Fillable scaffolds with {{VARIABLE}} placeholders]
[One template per major concept]

## Worked Examples
[At least one filled-in template showing a real-world instance]

## Pitfalls
[Synthesized from finding failure modes and potential improvements]

## Contract
### Preconditions
### Invariants
### Governance
### Recovery
```

Present the outline to the user for approval (unless `--auto`).

### Step 3: Draft Guide

Draft the full guide body. Key principles:

1. **Synthesize, don't compile.** The guide should read as a unified document, not a list of finding summaries. Cross-reference findings internally but don't expose the source structure.
2. **Templates are first-class.** Every template should be a fenced code block with `{{VARIABLE}}` slots, preceded by a variable table (name, type, description, required/optional).
3. **Examples are mandatory.** At least one worked example per template. Use MetaSystem or a realistic project as the example context.
4. **Decision trees for choices.** When findings describe competing approaches (e.g., single-agent vs. multi-agent), present a decision tree with criteria, not a description of both options.
5. **Pitfalls from failure modes.** Every finding has potential failure modes — synthesize these into a practical "what goes wrong" section.
6. **ContractSpec per DD-78.** The guide carries preconditions (what must be true to use this guide), invariants (what the guide assumes stays true), governance (who owns and updates the guide), and recovery (what to do when assumptions break).

### Step 3.5: Re-Insert Preserved Content (re-synthesis only) — DD-93

If `preserved` from Step 0.5 is empty, skip. Otherwise:

1. **Annotations re-insertion.** If `preserved.annotations.present` is true:
   - Scan the candidate body for an existing `## Nick's Annotations` heading. If the structural template emitted one, replace its body with the captured `preserved.annotations.body` byte-for-byte.
   - If the structural template did not emit a `## Nick's Annotations` heading, append the section to the tail of the candidate body (after all other `^## ` sections, before the file's closing newline) using the canonical heading `## Nick's Annotations` followed by the captured body.
   - Position MUST be either (a) the original ordinal location if the structural template still reserves a slot at that ordinal, or (b) tail of the body otherwise. Never silently relocate to a different mid-body slot.

2. **Marked-region re-insertion.** For each captured region, in document order:
   - Locate the candidate body's anchor section by name (`preserved.regions[i].anchor_section`).
   - Within that section, find the closest semantically-equivalent insertion point. The default heuristic: insert the region (wrapped in fresh `<!-- PRESERVE -->` … `<!-- /PRESERVE -->` markers) at the start of the anchor section's body, after any subheading-free intro paragraph and before any `### ` subheading. If multiple regions targeted the same anchor section, preserve their captured ordinal order.
   - If the anchor section no longer exists in the candidate body (renamed, removed, or merged), do NOT silently drop the region. Append it to the tail of the candidate body wrapped in markers, with a leading HTML comment `<!-- preserved-region: anchor "<original-section-name>" no longer present in regen; appended at tail -->`. The post-regen regression test (Step 3.7) will still confirm byte-equality of the region body.

3. **Output is the candidate body.** The candidate body is the input to Step 3.7 (regression test). The skill does NOT write the file in this step.

### Step 3.7: Post-Regen Regression Test (fail-closed) — DD-93

If `preserved` is empty, skip. Otherwise this is a hard gate before Step 4.

1. **Re-extract preserved surfaces** from the candidate body using the same procedure as Step 0.5. Build a candidate-side `preserved_after` structure with the same shape.
2. **Byte-compare** every captured surface against its candidate-side counterpart:
   - Annotations: `preserved.annotations.body` vs `preserved_after.annotations.body` — byte-equality required.
   - Each region: `preserved.regions[i].body` vs `preserved_after.regions[i].body` — byte-equality required, in original document order. Region count MUST match.
3. **On any inequality (drift):**
   - **Abort the write.** The candidate body is NOT written to disk. The existing guide file is unchanged.
   - **Emit a structured drift report** to stdout containing:
     - Which preserved surface drifted (`annotations` or `regions[i] (anchor: "<section-name>")`)
     - The byte-level diff (unified diff format, captured-vs-candidate)
     - The recommended fix path (one of: "skill bug — re-insertion logic dropped or transformed bytes", "structural template removed the anchor section without fallback", "marker validation passed pre-regen but post-regen extraction lost a region")
   - **Exit non-zero.** The session does not proceed to Step 4. Nick re-runs after the skill-side bug is fixed.
4. **On full byte-equality across all surfaces:** proceed to Step 4. The candidate body is now the writable body.

This regression test is the enforcement mechanism for DD-93. It must run on every re-synthesis where `preserved` is non-empty. A skill that writes a guide without running this check has violated the contract.

### Step 4: Write Guide

1. **Generate filename:** kebab-case from the guide title. E.g., `managing-agent-context-budgets.md`.
2. **Check for collision** in `extracts/guides/`. Append `-2`, `-3` if needed.
3. **Write the guide file** to `systems/improvement-loop/extracts/guides/`:

```yaml
---
title: "[Guide Title]"
type: "guideline"
category: "[research dimension or topic]"
target_system:
  - "cross-system"
stage: "draft"
created: "[YYYY-MM-DD]"
updated: "[YYYY-MM-DD]"
author: "claude"
source_findings:
  - "[finding-stem-1]"
  - "[finding-stem-2]"
source_dd:
  - "DD-81"
tags:
  - "guide"
  - "[topic-tag]"
contract:
  preconditions: "[...]"
  invariants: "[...]"
  governance: "[...]"
  recovery: "[...]"
---
```

### Step 4.5: Append Companion Changelog Entry (re-synthesis only) — DD-94

If this is an **initial synthesis** (the guide file did not exist before Step 4), skip — no changelog entry is written. The companion changelog file is only created on the first re-synthesis after DD-94 lands; new guides accrue history starting from their first re-synthesis.

If this is a **re-synthesis** (the guide existed pre-Step-4 and was rewritten), write a companion changelog entry. The companion file lives at `systems/improvement-loop/extracts/guides/changelog/<guide-stem>.changelog.md` (one-to-one with the guide; same stem).

1. **Resolve trigger tag.**
   - Read `--trigger TAG`. If absent and not `--auto`, prompt the user; if absent and `--auto`, abort with a structured error naming the missing argument.
   - Validate against the closed enum: `staleness-threshold`, `nick-request`, `dimension-rebalance`, `finding-removed`, `structural-edit`, `guide-split` (DD-98). Any other value (including `initial-synthesis`, which is reserved for the one-time IB-155 backfill) MUST be rejected with a structured rejection report (offending tag, valid enum, recommended fix). New tags require a DD amendment, not ad-hoc invention.

2. **Resolve session number.** Read `--session NN`. If absent and not `--auto`, prompt; if absent and `--auto`, abort.

3. **Resolve date.** Use the current date in `YYYY-MM-DD` format.

4. **Compute entry fields.**
   - **Findings count and delta.** Total = length of `source_findings[]` in the freshly-written guide frontmatter. Delta = compare the new `source_findings[]` against the prior version's `source_findings[]` (read from the on-disk guide before Step 4 wrote over it; cache during Step 0.5). Compute `added` (new stems not in prior set) and `removed` (prior stems not in new set).
   - **Structural line.** 1–2 lines describing what changed at the guide-architectural level (e.g., "Added Step 8 on harness engineering; Pitfalls expanded with three new failure modes."). If the only change is finding-set churn, write "no structural changes; finding-set churn only." If multiple triggers apply, name secondary triggers here.
   - **Preserved line.** Derived from Step 3.7 output. One of: `\`## Nick's Annotations\` untouched`, `<!-- PRESERVE --> regions intact (N regions)`, `\`## Nick's Annotations\` untouched + <!-- PRESERVE --> regions intact (N regions)`, or `none`.
   - **SL link.** The current session's SL stem (e.g., `session-71-codifier-ib-154-ib-155-synthesize-guide-update`). Wrapped in wikilink syntax: `[[session-71-codifier-ib-154-ib-155-synthesize-guide-update]]`. The SL entry will be authored at session close; the link is forward-pointing.

5. **Construct the entry block** in this exact shape:
   ```markdown
   ## YYYY-MM-DD — Session NN — <trigger-tag>

   - Findings: <N> (+<added>, -<removed> since last synthesis)
   - Added: [[finding-stem-1]], [[finding-stem-2]]
   - Removed: [[finding-stem-x]]
   - Structural: <1–2 lines>
   - Preserved: <preservation status>
   - SL: [[session-NN-<descriptor>]]
   ```
   Omit the `Added:` line if the added list is empty; omit the `Removed:` line if the removed list is empty. The header line and the five remaining bullets (Findings, Structural, Preserved, SL — minus any omitted Added/Removed) MUST be present.

6. **Enforce line cap.** Count non-header lines (everything after the `## ` header line, excluding the trailing newline). Bands:
   - **≤10 lines: clean.** Write the entry.
   - **11–15 lines: warning.** Write the entry; surface a warning in skill output naming the over-budget bullet(s) and recommending narrative content move to SL.
   - **>15 lines: abort.** Do NOT write the entry. Emit a structured report (line count, offending bullets, recommended fix path: "move narrative to SL; keep structural line to 1–2 lines"). Skill exits non-zero. Nick re-runs after slimming.

7. **Locate or create the companion file.**
   - Check `systems/improvement-loop/extracts/guides/changelog/<guide-stem>.changelog.md`.
   - If absent, create it with a single-line title heading: `# Changelog — <guide title>` (the guide title from frontmatter, not the kebab-case stem) followed by a blank line. Then proceed to insert the new entry directly below the title heading.
   - If present, locate the title heading (`^# `). Insert the new entry directly below it, separated by a blank line, **above all existing entries**. Most-recent-first ordering is invariant.

8. **Atomic write.** Read the current file (or treat as empty if absent), construct the new file content (title + blank line + new entry + blank line + existing entries), write the result. Do not mutate existing entries.

9. **Report to user (unless `--auto`):** "Changelog entry appended at `extracts/guides/changelog/<stem>.changelog.md` — trigger: <tag>, lines: N (clean|warning)." Warnings are surfaced; aborts have already exited the skill non-zero before reaching this point.

This step runs after Step 4 (guide write) and before Step 5 (synthesis status / cross-references). The guide file is already on disk at this point; if Step 4.5 fails on a >15-line entry, the guide is on disk but the changelog has no entry — Nick re-runs Step 4.5 after slimming the entry, or invokes a manual append.

### Step 4.7: Co-occurrence Harvest Scan + Queue Write — DD-101

For each pattern finding absorbed into this guide body, scan the finding for embedded artifact-shaped content of a non-pattern form, and append rows to a per-guide harvest queue file. Read-only by contract: never auto-extract; never modify the finding's classification; never create the harvested artifact. Extraction is downstream via Nick's ruling and `/extract-artifacts`'s queue-row promotion path (DD-101 §Promotion + IB-164).

This step runs after Step 4.5 (changelog write) and before Step 5 (synthesis status). It is a no-op if no embedded artifact-shaped content is detected AND no prior queue rows would be superseded.

**Item 1 — Per-finding co-occurrence scan.**

For each pattern finding in the absorbed set (the same set used for Step 3 drafting; the finding bodies were loaded in Step 1):

1. Examine the finding's body for prose that reads as artifact-shaped content of one of three target forms (closed enum):
   - **rule shape** — imperative directive ("never X", "always Y"); machine-enforceable; fits rule artifact form per the form-classification rubric.
   - **skill shape** — a procedure with input/output, invocation contract, step-by-step structure.
   - **template shape** — a structural scaffold meant for rendering (frontmatter blocks, placeholder fields, structural form).
2. Detection is **LLM-loose**, calibrated like DD-97 and Step 1.8 of `/extract-artifacts` — false-positives tolerable (cost: one Nick gate per row); false-negatives tolerable (cost: embedded artifact stays embedded; another consumer may surface it per DD-77).

**Agent-shape suppression invariant (DD-82).** If detection would surface agent-shaped content (a candidate for the `agent` form), the candidate is logged inline in the run report (NOT the queue) for Nick's separate review. The queue NEVER carries agent-form rows. This is structural, not advisory: the row-write path enforces a closed-enum target-form check (`rule` | `skill` | `template`; agent rejected — abort the row write and surface a procedural violation if encountered). Three-layer enforcement of DD-82's never-auto-create invariant: (1) Item 1's enum-target check; (2) the inline-narrative path for agent-shaped detections; (3) `/extract-artifacts`'s defensive abort on agent-target queue rows per IB-164.

**Item 2 — Per-guide queue file location and shape.**

Queue file location: `systems/improvement-loop/extracts/guides/<guide-stem>.harvest-queue.md` (one-to-one with the guide; same stem). Mirrors DD-94's companion changelog convention at `<guide-stem>.changelog.md` — same per-guide-locality structural pattern.

If the queue file does NOT exist AND at least one row would be appended this regen, create it with this header:

```markdown
# Co-occurrence Harvest Queue — <Guide Title>

Embedded artifact candidates surfaced during `/synthesize-guide` runs. Per DD-101.
Nothing here is auto-extracted; rows feed `/extract-artifacts` only after Nick rules.

| Date queued | Status | Target form | Source finding | Suggested headline | Recommendation |
|---|---|---|---|---|---|

## Per-row details
```

If the queue file exists, parse the existing summary table and per-row details blocks to enable duplicate suppression (Item 2.b) and supersession (Item 2.c).

**Item 2.a — Per-row content fields (required, per DD-101 §The Constraint).**

Each detected candidate appends one summary-table row AND one per-row details block. Required fields:

- **Date queued** — ISO date of the regen run.
- **Status** — closed enum: `queued` | `nick-approved` | `nick-dismissed` | `extracted` | `superseded`. New rows are `queued`; status transitions are downstream of this skill (Nick rulings + IB-164 extractions + Item 2.c supersession).
- **Target form** — closed enum: `rule` | `skill` | `template`. Agent excluded by the Item 1 suppression invariant.
- **Source finding** — the pattern finding whose body contained the embedded prose; wikilink `[[<finding-stem>]]`.
- **Source excerpt** — verbatim quote of the embedded prose, ≤8 lines. Long candidates use ellipsis with the structural anchor preserved.
- **Codifier's reading** — 1–3 lines explaining why this prose reads as the target form (cites form-rubric criteria when relevant).
- **Suggested headline** — Codifier's proposed artifact title.
- **Recommendation** — closed enum: `extract via /extract-artifacts` | `dismiss as inline` | `merge into existing [[<artifact-stem>]]`.
- **Resolution** — filled by IB-164 / Nick rulings; closed enum: `extracted to [[<artifact-stem>]]` | `dismissed` | `merged into [[<artifact-stem>]]` | `superseded`. New rows leave this field blank.

Per-row details block heading: `### <finding-stem>::<target-form>::<headline-slug>` where `<headline-slug>` is a kebab-case slug of the suggested headline (≤6 words). This compound heading is the row's structural ID for IB-164's queue-row references and for duplicate-suppression matching.

**Item 2.b — Duplicate suppression at write.**

Before appending a new row, check the existing queue file for any row with the same `(source_finding, target_form)` tuple:

- If a row exists with status `queued`, `nick-dismissed`, `extracted`, or `superseded`: NO new row is appended — the prior row stands. Even terminal-status rows (`nick-dismissed`, `extracted`, `superseded`) suppress re-emission: the candidate has been resolved (or marked-as-resolved) and re-detection on regen does NOT re-emit. This prevents queue-bloat from regen cycles re-detecting the same embedded prose.
- The duplicate-suppression key is `(source_finding, target_form)`; the headline-slug is NOT part of the key (the same finding's same target-form prose with a slightly different proposed headline is the same candidate).

**Item 2.c — Supersession on cluster departure.**

Before scanning the absorbed set, compare the prior `source_findings[]` from the on-disk guide (cached during Step 0.5) against the current regen's absorbed set. For each pattern finding that was previously in the cluster but is NO longer in this regen's absorbed set (e.g., dimension-rebalance moved it elsewhere — see IB-153 path):

- For every queue row whose `source_finding` matches the departed finding AND whose status is `queued` or `nick-approved`: mark the row's Status as `superseded` AND the Resolution as `superseded`. Append a footer line to the per-row details block: `Superseded YYYY-MM-DD — Session NN — [[session-NN-<descriptor>]] — source finding departed cluster.` The row is NOT deleted (audit trail).
- Leave `extracted` rows as `extracted`: the artifact exists; the source's later cluster-movement does not invalidate it.
- Leave `nick-dismissed` rows as `nick-dismissed`: Nick's ruling stands.
- Supersession is structural, NOT Nick-judgmental; do NOT flip rows to `nick-dismissed` for departure reasons.

**Item 3 — Append-only across regen cycles.** New rows append to the summary table (most-recent-last) AND to the per-row details section (in document order). Existing rows persist with their current Status and Resolution — `/synthesize-guide` NEVER mutates a row's Status or Resolution except via Item 2.c's supersession path. Status transitions for Nick's rulings (`nick-approved` / `nick-dismissed`) + IB-164's extractions (`extracted`) are downstream of this skill; this step writes new rows and supersession-marks departed-source rows only. Rows are NEVER deleted.

**Item 4 — Initial-synthesis behavior.** If this is an initial synthesis (the guide file did not exist before Step 4), the queue file is also new; create it on first detection per Item 2. If no candidates are detected on initial synthesis, the queue file is NOT created — companion files materialize on first detection, not on first synthesis. (Mirrors DD-94's changelog initial-synthesis behavior: companion file created lazily on first qualifying event.)

**Atomic write.** Read the current queue file (or treat as empty if absent); construct the updated content (header + summary table with new rows appended + existing rows preserved + per-row details with new blocks appended + existing blocks preserved + Item 2.c supersession annotations); write the result. Do not mutate prior rows except for Item 2.c.

**Report to user (unless `--auto`):** "Co-occurrence harvest scan: {N} embedded artifact candidates detected ({R} rule, {S} skill, {T} template; {A} agent-shape suppressed and inline-noted). {Q} new rows appended to `<guide-stem>.harvest-queue.md`; {D} suppressed as duplicates of prior rows. {SU} prior rows superseded due to source-finding cluster departure." If no candidates detected, no prior rows superseded, AND no queue file existed beforehand, report "No co-occurrence harvest candidates detected; no queue file written."

### Step 5: Update Synthesis Status and Cross-References

1. **Update the Synthesis Status table** in `systems/improvement-loop/operations/references/guide-routing-table.md`. Set the cluster's row to: last synthesized date, finding count, output path, and status (`draft`). If re-synthesizing an existing guide, update the row in place.

2. **Cross-reference adjacent guides.** Check the Related Guides sections of other cluster guides for cross-references to add. If the new or updated guide connects to existing guides, add bidirectional Related Guides entries in both the new guide and the adjacent guides.

3. **Back-annotate finding files.** For each finding consumed by this guide, update its frontmatter:
   - Set `pipeline_status: "synthesized"`
   - Add the guide filename to `consumed_by:` (e.g., `"managing-agent-context.md"`)
   - If the finding already has `consumed_by` entries (e.g., from individual extraction), append rather than replace.

### Step 6: Summary

Report to the user:

```
## Guide Synthesis Summary — [date]

**Guide:** [title]
**Findings synthesized:** {N}
**Subtopic clusters:** {M}
**Templates included:** {count}
**Worked examples:** {count}

Written to: extracts/guides/[filename]

Source findings: [list]

Next: Review the staged guide. Deploy to meta-system/knowledge/guides/ when ready.
```

---

## Rules

1. **Synthesize, never compile.** A guide that reads as a list of pattern summaries has failed. The reader should not need to know the source findings to use the guide.
2. **Templates are mandatory.** Every guide must include at least one fillable template with `{{VARIABLE}}` placeholders. Guides without templates are descriptions, not tools.
3. **Examples are mandatory.** Every template must have at least one worked example.
4. **ContractSpec on every guide** (DD-78). Guides carry the same contract as extracted artifacts.
5. **Stage, don't deploy.** Write to `extracts/guides/`, not to `meta-system/knowledge/guides/`.
6. **Respect finding boundaries.** Source only from the confirmed finding set. Don't inject external knowledge not grounded in the KB.
7. **Minimum finding count.** A guide synthesizing fewer than 3 findings is likely too narrow. Flag to the user and suggest expanding the finding set.

---

## Failure Modes

| Failure | Detection | Recovery |
|---------|-----------|----------|
| Topic matches 0 findings | Step 0 returns empty set | Suggest alternative topics based on available categories |
| Topic matches too many findings (>20) | Step 0 returns >20 | Suggest subtopic decomposition — split into 2-3 guides |
| Findings are too unrelated to synthesize | Step 1 clustering produces singletons | Flag to user — these may need separate guides or aren't guide material |
| No templates produced | Step 3 produces no `{{VARIABLE}}` blocks | Fail — return to Step 3 with explicit template extraction instruction |
| Guide is too long (>5000 words) | Word count check after Step 3 | Split into multiple guides or extract reference sections into appendices |
| Unmatched / nested `<!-- PRESERVE -->` markers in existing guide | Step 0.5 marker validation | Abort synthesis with structured marker error (line, recommended fix). Nick repairs the guide; re-run. |
| Preserved-section drift on regen | Step 3.7 byte-diff fails | Abort write; emit structured drift report (which surface, diff, recommended fix). No file change. Re-run after skill bug fixed. |
| `--trigger` tag missing on re-synthesis | Step 4.5 trigger resolution | Prompt unless `--auto`. With `--auto`, abort with structured error naming the missing argument. |
| `--trigger` tag not in closed enum | Step 4.5 enum validation | Reject with structured report (offending tag, valid enum). Skill exits non-zero. New tags require DD amendment. |
| Changelog entry exceeds 15 non-header lines | Step 4.5 line-cap check | Abort entry write (entry is not appended; guide file already on disk). Emit structured report; recommend moving narrative to SL. Re-run Step 4.5 after slimming. |
| Changelog entry 11–15 non-header lines | Step 4.5 line-cap check | Write with warning; warning identifies over-budget bullets. Caller may slim and reissue, or accept the verbose entry. |
| Harvest queue write failure mid-regen | Step 4.7 atomic-write step fails | Procedural failure — Step 4.7 is expected to write the queue alongside the guide draft. The guide file is already on disk at this point (Step 4 completed); the queue file is partial or missing. Recovery: re-run Step 4.7 manually, or accept the missed-emission and let the next regen re-detect (duplicate-suppression will not fire because the prior row was never written). Flag as governance audit item if recurring. |
| Agent-shape content detected during Step 4.7 scan | Step 4.7 Item 1 agent-suppression check | Suppress queue emission per the Item 1 invariant; log the candidate inline in the run report (NOT the queue) for Nick's separate review. The queue NEVER carries agent-form rows. If a queue row write is attempted with `target form: agent`, abort the row write with structured error citing DD-82 + DD-101 §Rules for `/synthesize-guide` item 3. Surface the procedural violation. |
| Duplicate-suppression collision (existing row with same `(source_finding, target_form)`) | Step 4.7 Item 2.b pre-write check | Suppress the new row write — the prior row stands regardless of its current status (`queued`, `nick-dismissed`, `extracted`, or `superseded`). This is expected behavior, not a failure mode; documented here for verification that the suppression path activates on duplicate detection. Run report's `D` count surfaces the suppressed-as-duplicate rows. |
| Source-finding cluster departure path (status update for `queued`/`nick-approved`; non-update for `extracted`/`nick-dismissed`) | Step 4.7 Item 2.c supersession check | Mark `queued` and `nick-approved` rows whose departed source matches as `superseded` with cited regen session + SL stem; leave `extracted` and `nick-dismissed` rows unchanged. This is expected behavior, not a failure mode; documented here for verification that supersession does NOT over-write Nick's terminal rulings or live extractions. |
| Split-trigger fires (≥25 findings AND ≥2 practitioner questions) but practitioner-question bifurcation is unclear in proposal | Step 0.7 emission | Codifier flags the proposal's `Codifier recommendation` field as `re-evaluate practitioner-question bifurcation`. Nick rules: defer (re-cluster on next intake), absorb shared findings into one destination by judgment, or split with explicit duplication. The proposal IS still emitted — the recommendation captures the structural concern. |
| Split-trigger fires; >20% of findings flag as `shared` or `contested` | Step 0.7 bifurcation precision check | Same as above — recommendation `re-evaluate practitioner-question bifurcation` with the bifurcation precision summary noted in the proposal's per-finding routing table. Nick rules sequencing: re-evaluate, defer, or accept the imprecise split. |
| Single-condition split observation (count crosses but practitioner-question stays at 1, or vice versa) | Step 0.7 dispatch table single-condition path | NO proposal file emitted. Inline informational note in run report only ("G-`<stem>` at <count> findings; remains single-question" or analogous). Monitor on next regen cycle. |
| Split-trigger fires but source guide is mid-`/synthesize-guide` regen | Step 0.7 detection runs at Step 0.7; regen continues regardless | Regen completes against existing source structure. Split-proposal is emitted at the end of Step 0.7 (BEFORE Step 1 drafting begins); regen proceeds with the proposal as a side-channel artifact. The regen's changelog entry (Step 4.5) uses its normal trigger (`staleness-threshold`, etc.); the split-proposal is a separate artifact. |
| Split-proposal filename collision (two regens of the same guide on the same day) | Step 0.7 atomic write filename collision check | Append `-2`, `-3` to the colliding filename. Both proposals retained for audit; Nick reads the latest. |
| Initial-synthesis triggers split-proposal emission | Step 0.7 initial-synthesis no-op gate | Defensive: Step 0.7 is no-op on initial synthesis (no existing cluster to split). If somehow triggered (e.g., a guide whose finding-set was pre-curated to ≥25 with ≥2 questions on first synthesis), the proposal is still emitted — DD-98's threshold semantics apply regardless of synthesis history. Edge case; document if observed. |

---

## Design Decisions

| DD | Relevance |
|---|---|
| DD-81 | Pattern findings route to guide synthesis, not extraction |
| DD-80 | Pipeline architecture (amended by DD-81 for patterns) |
| DD-78 | ContractSpec on every artifact, including guides |
| DD-45 | Knowledge architecture — guides live in meta-system/knowledge/guides/ |
| DD-46 | Pull model — guides are pulled by consuming systems |
| DD-93 | Preserved sections on guide regen (`## Nick's Annotations` + `<!-- PRESERVE -->` regions); post-regen byte-equality regression test; fail-closed on drift. Steps 0.5 / 3.5 / 3.7. |
| DD-94 | Companion changelog file per guide at `extracts/guides/changelog/<stem>.changelog.md`; one entry per re-synthesis with closed trigger-tag enum, ~10-line cap (≤10 clean / 11–15 warn / >15 abort), most-recent-first append. Step 4.5. |
| DD-101 | Per-guide co-occurrence harvest queue file at `extracts/guides/<stem>.harvest-queue.md`. Per-finding scan during regen for embedded artifact-shaped content (target forms: rule \| skill \| template; agent suppressed inline per DD-82). LLM-loose calibration. Closed-enum Status, Target form, Recommendation, Resolution. Duplicate suppression on `(source_finding, target_form)`. Append-only across regen; supersession-on-departure for `queued`/`nick-approved` rows; `extracted` and `nick-dismissed` rows unchanged on departure; rows never deleted. Read-only by contract — extraction is downstream via Nick's ruling + IB-164's `/extract-artifacts` queue-row promotion path. Step 4.7. |
| DD-98 | Guide split procedure. Step 0.7 evaluates the conjunction (count ≥25 AND practitioner-question count ≥2) at routing-table read; on match, emits a split-proposal artifact at `operations/split-proposals/<YYYY-MM-DD>-<guide-stem>-split-proposal.md` with per-finding bifurcation, preserved-section disposition (DD-93), routing-table impact, and Codifier recommendation from closed enum (`proceed with split as proposed` \| `defer pending more findings` \| `re-evaluate practitioner-question bifurcation` \| `absorb into adjacent guide instead`). Read-only by contract — never auto-executes; never modifies the source guide or routing table; never modifies DD-94 changelog files based on its own proposal. Initial-synthesis is no-op. Single-condition observations surface inline only. Both `/synthesize-guide` Step 0.7 AND `/identify-artifacts` Step 6.a share identical emission semantics. Step 4.5 enum extended to accept `guide-split` for source-final + destination-first changelog entries (per-split DD execution path; not at Step 0.7 emission time). |
| DD-82 | Agent never-auto-create invariant — three-layer enforcement at the harvest layer: (1) Step 4.7 Item 1 closed-enum target-form check rejects `agent` target; (2) agent-shaped detections are logged inline in the run report only, never queued; (3) `/extract-artifacts` defensive abort on agent-target queue rows per IB-164 (defense-in-depth). |
