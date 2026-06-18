---
name: compare-repos
description: >-
  Cross-repo structural comparison across watched libraries. Reads per-repo
  *-analysis.md files produced by /repo-analyzer, the watched-library
  registry entries, and relevant findings; produces a structural comparison
  matrix plus Librarian-layer consumer-oriented insights ("which patterns
  are emerging", "what trends are shared / unique / contradictory",
  "what should I consider adopting for X"). Use when the user asks to
  compare watched libraries, look across the ecosystem, or extract pattern
  clusters across repos. Read-only on the KB; writes the comparison report
  to watched-libraries/analysis/cross-repo-comparison.md only on explicit
  approval.
user-invocable: true
allowed-tools: Read Grep Glob Write
argument-hint: "[--repos lib1,lib2,...] [--dimensions dim1,dim2,...] [--focus <question>] [--write]"
---

# Compare Repos

Librarian-layer cross-repo comparison. Reads the structural analyses
already produced by `/repo-analyzer` (per-repo `*-analysis.md` files) and
synthesizes a comparison that is consumer-oriented — not just "what do
these repos look like", but "what patterns are converging, where do they
diverge, what should you consider adopting".

This skill consolidates the deprecated `/repo-analyzer --compare` mode.
The Researcher's `/repo-analyzer` produces per-repo structural cartography
(input); the Librarian's `/compare-repos` produces cross-repo synthesis
plus Builder-mode recommendations (output).

## When to Use This Skill

- User asks "compare the watched libraries", "what patterns are emerging
  across the ecosystem", "what's converging in the agentic-coding space".
- User asks "which of our watched libraries handles X best", "what should
  we adopt for Y" — Librarian Builder-mode synthesis across repos.
- Periodic ecosystem refresh after multiple repos have been
  (re-)analyzed.
- Targeted comparison on a specific dimension (e.g., "compare governance
  models across repos").

## What This Skill Does NOT Do

- Does not analyze individual repos. Per-repo analysis is `/repo-analyzer`'s
  job. If a repo named in `--repos` has no `*-analysis.md`, the skill
  reports the missing input and asks the user to run `/repo-analyzer`
  first.
- Does not promote findings into the KB. Findings candidates surface in
  the report; promotion is `/promote-findings`.
- Does not modify per-repo analysis docs.
- Does not perform web research. External context comes from KB findings,
  not live web fetches. Use `/perplexity-research --compare` for KB-vs-web
  gap analysis.

## Cognitive Disposition

Librarian — primarily Builder mode (synthesizes recommendations for the
user's stated focus); Teacher mode kicks in for the descriptive matrix
sections.

- **Descriptive layers first (Teacher).** Structural matrix and pattern
  clusters describe what *is* across repos. Citations to specific
  `*-analysis.md` sections.
- **Recommendation layers second (Builder).** When `--focus` is supplied
  or the user asks an adoption question, follow the descriptive matrix
  with a sequenced recommendation set: which repo's pattern fits which
  use case, which pitfalls apply, which trade-offs matter.
- **Patterns over individual details.** Emerging conventions (3+ repos)
  are highlighted; unique-to-one-repo patterns are flagged as
  potential innovation or niche. Contradictory approaches are surfaced
  with both sides.

## Paths

| Path | Purpose |
|------|---------|
| `systems/improvement-loop/watched-libraries/` | Watched library registry entries (input) |
| `systems/improvement-loop/watched-libraries/_index.md` | Library index |
| `systems/improvement-loop/watched-libraries/analysis/` | Per-repo `*-analysis.md` files (input) |
| `systems/improvement-loop/watched-libraries/analysis/_index.md` | Analysis index |
| `systems/improvement-loop/watched-libraries/analysis/cross-repo-comparison.md` | Comparison report output |
| `systems/improvement-loop/operations/references/research-dimensions.md` | Dimension registry (scoping) |
| `systems/improvement-loop/research-findings/` | KB findings (for Builder-mode synthesis) |
| `systems/improvement-loop/agents/librarian/agent.md` | Teacher/Builder mode substrate |

## Arguments

| Argument | Effect |
|----------|--------|
| `--repos lib1,lib2,...` | Limit comparison to specified libraries. Default: all libraries with an analysis doc. |
| `--dimensions dim1,dim2` | Limit comparison to specified analysis dimensions. Values: `structural-inventory`, `context-file-map`, `workflow-topology`, `governance-model`, `cross-agent-protocol`, `research-dimension-mapping`. Default: all 6. |
| `--focus <question>` | Builder-mode lens. The comparison body adds a "Recommendation for `<question>`" section at the end. |
| `--write` | After presenting the report inline, write to `watched-libraries/analysis/cross-repo-comparison.md`. Default: inline only. Existing file is overwritten; previous report appears in the file's Version Log. |

## Procedure

### Step 0: Parse arguments and validate inputs

1. Parse `--repos`, `--dimensions`, `--focus`, `--write`.
2. `Read` `watched-libraries/analysis/_index.md` to enumerate available
   `*-analysis.md` files.
3. Resolve the working set:
   - If `--repos` supplied: intersect with available analyses. If any
     named repo lacks an analysis doc, report missing inputs and stop.
     Ask the user to run `/repo-analyzer <lib>` then re-invoke.
   - If `--repos` omitted: include every library with an analysis doc.
4. If working set has fewer than 2 libraries, stop. Comparison requires
   at least 2 inputs. Report "comparison requires 2+ analyzed repos;
   working set has N".

### Step 1: Load inputs

1. `Read` each `*-analysis.md` in the working set. Capture per-repo:
   - Frontmatter: `analyzed_version`, `analyzed_date`, `repo_url`,
     `dimensions_analyzed`.
   - Section content for the dimensions in scope.
2. `Read` the watched-library entry for each repo (spectrum position,
   stated purpose, version).
3. `Read` `operations/references/research-dimensions.md` for dimension
   definitions used in the Research Dimension Mapping section.

### Step 2: Build the structural comparison matrix (Teacher layer)

Produce comparison tables per dimension in scope. Mirror the dimension
shapes from `/repo-analyzer`'s analysis-doc body:

- **Structural Scale**: total files, MD-to-code ratio, max depth, agent
  count, command/skill count.
- **Context File Patterns**: count, mechanism distribution (Auto-loaded,
  Chain-loader, Hook-injected, Referenced, Injected), audience mix
  (LLM, Human, Both), layering depth.
- **Workflow Topology**: phase count, human-gate count, parallelism,
  workflow shape (sequential pipeline, hub-and-spoke, peer, none).
- **Governance Model**: constitution present?, enforcement style (hard
  vs soft), permission model shape, guardrail mechanism inventory.
- **Cross-Agent Protocol**: agent count, coordination pattern,
  handoff mechanism, shared-state mechanism.
- **Research Dimension Mapping**: relevance grid (10 dimensions × repos
  × High/Medium/Low/None).

Cite each cell to the per-repo analysis doc section (`{name}-analysis.md
§N.subsection`). Do not paraphrase the per-repo analysis into the matrix
without a citation handle.

### Step 3: Identify pattern clusters

For each dimension in scope:

1. **Shared patterns (3+ repos):** name the pattern, list the repos,
   characterize the variance, classify as "emerging convention".
2. **Unique patterns (1 repo):** name the pattern, the repo, why it is
   distinctive, classify as "potential innovation" or "niche".
3. **Contradictory approaches:** repos that solve the same structural
   problem with opposite design choices. Name both sides; do not pick a
   winner — that is the consumer's call given their context.

Patterns must trace to specific analysis-doc sections. Avoid pattern
claims that cannot be verified from the source citations.

### Step 4: Builder-mode recommendation set (only if `--focus` supplied)

If `--focus <question>` was provided:

1. Restate the question. Identify which dimensions it touches.
2. For each touched dimension, pull the relevant patterns from Step 3.
3. Produce a recommendation set:
   - Which repo's pattern fits the user's situation, and the trade-offs.
   - Which pitfalls (from KB findings or the analysis docs) apply.
   - Which guides in `extracts/guides/` are relevant follow-up reading.
4. Citations: every recommendation traces to either a pattern from Step 3
   (with its analysis-doc citation) or a KB finding (`finding-id`,
   `evidence_strength`).

If `--focus` is omitted, skip this step. The report is descriptive only.

### Step 5: Surface findings candidates and gaps

1. **Findings candidates**: patterns from Step 3 that are novel, well-
   evidenced, or fill a gap in the current KB. Tag with the dimension
   they map to. Note: promotion is `/promote-findings`, not this skill.
2. **KB gaps surfaced by the comparison**: areas where the ecosystem
   shows clear patterns but our findings KB has none.
3. **Stale or missing inputs**: analysis docs that are out of date
   relative to the watched-library registry's `last_evaluated_version`,
   or libraries with registry entries but no analysis doc.

### Step 6: Assemble the report

Build the report body. If `--write` is set, present the report inline
first, then ask "Approve writing to `watched-libraries/analysis/cross-repo-comparison.md`? (y/N)".
Write only on explicit `y`. Default is inline-only.

When writing:

- If `cross-repo-comparison.md` exists, read its Version Log and append
  a new row before overwriting the body.
- Update `watched-libraries/analysis/_index.md` if the comparison report
  is newly added or its row needs refreshing.

## Output Shape

### Report frontmatter (when written)

```yaml
---
title: "Cross-Repo Structural Comparison"
id: "cross-repo-comparison"
type: "analysis"
category: "upstream-tracking"
target_system:
  - "cross-system"
stage: "active"
created: "{date if new}"
updated: "{today}"
author: "improvement-loop"
source_dd:
  - "DD-45"
  - "DD-46"
tags:
  - "repo-analysis"
  - "cross-repo"
  - "comparison"
repos_compared: [list of working-set names]
dimensions_compared: [list of dimension slugs]
focus_question: "<from --focus, or null>"
---
```

### Report body

```markdown
# Cross-Repo Structural Comparison

## Metadata
- **Repos compared:** {N libraries}
- **Dimensions compared:** {list}
- **Focus question:** {from --focus or "none"}
- **Date:** {today}

## Comparison Matrix

### Structural Scale
{table}

### Context File Patterns
{table}

### Workflow Comparison
{table}

### Governance Comparison
{table}

### Cross-Agent Comparison
{table}

### Research Dimension Mapping
{table — 10 dimensions × repos × High/Medium/Low/None}

## Pattern Clusters

### Shared Patterns (3+ repos)
- ...

### Unique Patterns (1 repo)
- ...

### Contradictory Approaches
- ...

## Recommendation (only if --focus supplied)

**Question:** {focus question}

### Most relevant repos / patterns
- ...

### Trade-offs
- ...

### Pitfalls
- ...

### Guides to consult next
- ...

## Findings Candidates

{patterns worth promoting to the KB; not auto-promoted}

## Gaps Surfaced

### KB gaps
- ...

### Stale or missing inputs
- ...

## Version Log

| Date | Repos compared | Dimensions | Focus | Notes |
|------|----------------|------------|-------|-------|
```

When presented inline (no `--write`), the same body is produced as a
conversational response without the frontmatter.

## Boundary Conditions

- **Termination — success:** A citation-grounded comparison report has
  been produced (inline by default; written to the standard path if
  `--write` and explicit approval). Findings candidates and gaps are
  surfaced.
- **Termination — abort:** Working set < 2 repos; stop with "comparison
  requires 2+ analyzed repos". Working set has missing inputs that the
  user must fill; stop and request `/repo-analyzer` runs first.
- **Out of scope:**
  - Per-repo structural analysis → `/repo-analyzer <lib>`
  - Updating per-repo analysis docs after upstream version bump →
    `/repo-analyzer <lib> --force`
  - Promoting findings candidates into the KB → `/promote-findings`
  - KB-vs-external-web gap analysis → `/perplexity-research --compare`
  - General KB queries → `/ask-kb`
- **Safety-critical?** No on read; mild on write. The `--write` path is
  guarded by explicit per-invocation approval after seeing the report
  inline. Writes are confined to
  `watched-libraries/analysis/cross-repo-comparison.md` and its
  `_index.md`. No destructive operations; previous comparison body is
  preserved in the Version Log.

## Rules

1. **Inputs are the per-repo analysis docs.** This skill does not
   re-derive structural facts from raw repos; it reads what
   `/repo-analyzer` produced. If inputs are missing or stale, surface
   the gap; do not patch by cloning the repo here.
2. **Cite every comparison cell.** Each matrix entry and each pattern
   claim traces to `{name}-analysis.md §section`. No claims without
   citation handles.
3. **Pattern thresholds:** "shared" = 3+ repos; "unique" = exactly 1.
   2-repo overlaps are noted in the matrix but not promoted to "shared
   pattern" claims (insufficient signal).
4. **Contradictions get both sides.** No winner picked. The consumer
   decides given their context.
5. **No auto-promotion of findings.** Candidates surface in the report
   only. `/promote-findings` is the promotion path.
6. **Focus question requires explicit signal.** Builder-mode
   recommendations only appear when `--focus` is supplied. Without it,
   the report is descriptive; do not invent a focus.
7. **Write is opt-in and approval-gated.** Default is inline-only. The
   `--write` flag enables the write option; explicit approval gates the
   actual write.
8. **Existing comparison report is preserved via Version Log, not
   overwritten silently.**

## Boundary-Case Encounter Logging

On any deviation from the Tier-1 happy path (the 13-type encounter
taxonomy), append a structured record to
`operations/system-log/session-<N>-librarian-encounters.md`. Most
common encounter types for this skill: `missing-input` (analysis doc
absent), `tier-3-read` (oversized analysis doc), `kb-gap` (no findings
to support a pattern), `low-confidence` (pattern claim from 2-repo
overlap).

- Schema and routing:
  `systems/improvement-loop/project-management/design-notes/2026-04-22-librarian-boundary-case-tracking.md`

## Cross-References

- Researcher peer (per-repo analysis input):
  `systems/improvement-loop/.claude/skills/repo-analyzer/SKILL.md`
- Librarian peer (KB-query consumer surface):
  `systems/improvement-loop/.claude/skills/ask-kb/SKILL.md`
- Findings promotion path:
  `systems/improvement-loop/.claude/skills/promote-findings/SKILL.md`
- Librarian agent definition:
  `systems/improvement-loop/agents/librarian/agent.md`
- Consumer abstractions map (cross-repo comparison not currently a
  substrate-bearing abstraction):
  `systems/improvement-loop/operations/references/consumer-abstractions-map.md`
- Governing rules: IL `agent-rules.md` rule 11 (this skill earns its
  keep by separating Researcher per-repo analysis from Librarian
  cross-repo synthesis, eliminating the disposition leak in the
  deprecated `/repo-analyzer --compare` mode), rule 10 (non-applicable
  — analytical report, no constructed artifact spec)
