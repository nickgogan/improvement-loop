---
name: promote-findings
description: >-
  Promote findings candidates from repo-analyzer analysis docs into formal
  Research Findings in the KB. Reads analysis docs, deduplicates against existing
  findings, presents candidates for user selection, and writes approved entries
  with full frontmatter and body structure. Use after running /repo-analyzer on
  one or more watched libraries, or after /repo-analyzer --compare.
user-invocable: true
allowed-tools: Read Grep Glob Write Edit
argument-hint: "<library-name|all|comparison> [--auto]"
---

# Promote Findings

Bridge between `/repo-analyzer` analysis docs and the Research Findings KB. Reads findings candidates from analysis docs, checks for duplicates or updates, presents candidates for user approval, and writes formal Research Finding entries.

## When to Use This Skill

- After `/repo-analyzer` has produced analysis docs with Findings Candidates
- After `/repo-analyzer --compare` has produced the cross-repo comparison with its own candidates
- When the user asks to promote specific patterns from watched-library analyses into the KB

Do NOT use this skill for:
- Creating findings from web sources or URLs (use `/research-loop`)
- Generating improvement proposals from findings (use `/research-proposer`)
- Modifying analysis docs themselves (use `/repo-analyzer --force`)

## Cognitive Disposition

The Promoter thinks like a librarian, not a researcher.

- **Deduplication is the primary job.** The KB may already have a finding that covers the same pattern under a different name. Find it, update it, don't create duplicates.
- **Evidence calibration matters.** Analysis docs observe patterns in repos — that's "Medium (practitioner-documented)" evidence at best, not "Strong (production-tested)" unless the repo has documented production usage.
- **Preserve the candidate's insight.** The analysis doc's description of why a pattern is notable is valuable context. Carry it into the finding, don't lose it.
- **The user decides what gets promoted.** Present candidates with dedup status and let the user choose. Never auto-promote without explicit approval (unless `--auto` flag).

## Paths

| Path | Purpose |
|------|---------|
| `systems/improvement-loop/watched-libraries/analysis/` | Analysis docs (input) |
| `systems/improvement-loop/watched-libraries/analysis/cross-repo-comparison.md` | Comparison report (input) |
| `systems/improvement-loop/research-findings/` | Research Findings KB (output) |

---

## Arguments

| Argument | Effect |
|----------|--------|
| `<library-name>` | Promote candidates from a single analysis doc (e.g., `promote-findings gsd`) |
| `all` | Promote candidates from all analysis docs |
| `comparison` | Promote candidates from the cross-repo comparison report |
| `--auto` | Skip user selection — promote all candidates that pass dedup check. Use only when the user has pre-reviewed the analysis and trusts the candidates. |

---

## Research Findings Schema (for reference)

### Frontmatter

```yaml
---
name: "Finding Name"
summary: "Summary text"
implementation_notes: null
category: "Context Engineering"  # Context Engineering, Prompt Craft, Tool Integration, Model Selection, Intent Engineering, Orchestration, Memory Architecture, Evaluation, Sandboxing, Governance, Agent Design
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"  # Already Adopted, Partially Adopted, Not Yet Started
priority: null  # P1 (Implement Now), P2 (Design Required), P3 (Monitor), Not Flagged
applicability:
  - "S3 (Claude Code Build)"
adopted_in: []
sources: []  # filenames of source entries (leave empty — analysis docs are not research sources)
related_findings: []  # [{file: "filename.md", rel: "enables|contradicts|extends|same-problem"}]
proposals: null
date_discovered: "{today}"
last_updated: "{today}"
---
```

### Body Structure

```markdown
## What It Is
[Pattern distilled from the analysis doc's candidate description]

## Why It Matters
[Why this pattern is notable — what problem it solves]

## Why People Are Using It
[Evidence from the analyzed repo: star count, adoption, documented usage]

## Potential Alternatives
[Optional. Other approaches to the same problem observed in other analyzed repos]

## Potential Improvements
[Where the pattern could evolve]

## Potential Failure Modes
[Known limitations or edge cases]
```

### Source Attribution

Since analysis docs are not research sources (they're internal analysis), findings promoted from them should:
- Set `sources: []` (empty) in frontmatter
- Include a "Source" line in the "Why People Are Using It" section: `Observed in [{repo name}]({repo_url}) v{version} — see [[{library-name}-analysis]] for structural details.`
- This creates an Obsidian link back to the analysis doc without polluting the research-sources directory.

---

## Procedure

### Step 1: Load Candidates

1. Parse the argument to determine scope:
   - `promote-findings gsd` → read `watched-libraries/analysis/gsd-analysis.md`
   - `promote-findings all` → read all `*-analysis.md` files
   - `promote-findings comparison` → read `cross-repo-comparison.md`
2. For each target doc, use `Read` to load it. Extract the **Findings Candidates** section (under "## 6. Research Dimension Mapping" → "### Findings Candidates").
3. Parse each candidate: number, name, dimension(s), description.

### Step 2: Deduplication Check

For each candidate:

1. Use `Grep` to search `systems/improvement-loop/research-findings/` for the candidate's key terms (pattern name, core concept).
2. Classify the match:
   - **No match** → New finding. Eligible for promotion.
   - **Partial match** → Existing finding covers a related but distinct pattern. Eligible for promotion as a new finding, but note the relationship (will use `related_findings` field).
   - **Full match** → Existing finding already covers this pattern. Flag as duplicate — candidate may still warrant updating the existing finding with new evidence from the analysis.
3. Record the dedup status for each candidate.

### Step 3: Present Candidates for Selection

Present all candidates in a table:

```
| # | Candidate | Dimension | Dedup Status | Source Analysis |
|---|-----------|-----------|-------------|----------------|
| 1 | Three-layer context chain | Context Eng | New | gsd-analysis |
| 2 | Four-gate taxonomy | Evaluation | Partial (overlaps: "Gate-based verification") | gsd-analysis |
| 3 | Persuasion-engineered constraints | Governance | New | superpowers-analysis |
```

For each candidate, show:
- Candidate name and dimension
- Dedup status (New / Partial match with filename / Full duplicate with filename)
- Which analysis doc it came from

Ask the user to select which candidates to promote (by number). If `--auto` flag is set, auto-select all "New" and "Partial match" candidates.

### Step 4: Map Category

For each selected candidate, map the research dimension to a findings category:

| Research Dimension | Findings Category |
|-------------------|------------------|
| Context Engineering | Context Engineering |
| Model | Model Selection |
| Prompt | Prompt Craft |
| Tools | Tool Integration |
| Intent | Intent Engineering |
| Orchestration | Orchestration |
| Evaluation | Evaluation |
| Sandboxing | Sandboxing |
| Governance | Governance |
| Agent Design | Agent Design |

If the candidate maps to multiple dimensions, use the primary one (listed first in the candidate description).

### Step 5: Write Findings

For each selected candidate:

1. Generate a kebab-case filename from the candidate name.
2. Check if that filename already exists in `research-findings/`. If so, append the repo name (e.g., `four-gate-taxonomy-gsd.md`).
3. Use `Write` to create the finding file with:
   - Full frontmatter per schema above
   - `evidence_strength`: Default to `"Medium (practitioner-documented)"`. Upgrade to `"Strong (production-tested)"` only if the analysis doc notes production usage or significant adoption (e.g., "used by engineers at Amazon, Google").
   - `adoption_status`: Default to `"Not Yet Started"`. Set to `"Partially Adopted"` if the analysis doc notes MetaSystem already uses a variant of this pattern.
   - `priority`: Leave as `null`. The `/research-proposer` assigns priority.
   - Body sections populated from the candidate description and analysis doc context.
4. If dedup status was "Partial match", add a `related_findings` entry linking to the existing finding.

### Step 5b: Priority Re-evaluation Check

For each **partial match** where the existing finding was updated with new evidence:

1. Count how many distinct repo analyses now link to (or corroborate) the existing finding. Check `related_findings` links, source attribution lines, and analysis doc cross-references.
2. If the finding now has corroborating evidence from **3+ independent repos** and its current `priority` is `null`, `P3`, or `"Not Flagged"`:
   - Flag it as a **priority re-evaluation candidate** in the summary output.
   - Note the current priority, new evidence count, and repo sources.
3. Do NOT auto-change the priority — this is a flag for user review. The user decides whether to bump.
4. If evidence_strength is `"Weak (theoretical)"` and the finding now has evidence from 2+ production repos, flag for potential upgrade to `"Medium (practitioner-documented)"`.

Include a **Priority Re-evaluation** section in the Step 8 summary if any candidates were flagged.

### Step 6: Link Back to Analysis Doc

1. For each analysis doc that had candidates reviewed, use `Edit` to add a note under **every** candidate in the Findings Candidates section:
   - Promoted: `→ Promoted to [[finding-filename]] on {date}`
   - Skipped (duplicate): `→ Skipped: duplicate of [[existing-finding]] on {date}`
   - Skipped (weak): `→ Skipped: weak signal / single-source on {date}`
   - Skipped (not actionable): `→ Skipped: observational, not actionable on {date}`
   - Skipped (other): `→ Skipped: {reason} on {date}`

   **Every candidate must have a `→` annotation after review.** A candidate without a `→` prefix means "not yet reviewed." This makes completeness checking trivial: `grep -c "^[0-9]" analysis.md` vs `grep -c "→" analysis.md`.

### Step 7: Summary

Report to the user:
- How many candidates were reviewed
- How many were promoted (new findings created)
- How many were duplicates (skipped or updated)
- How many partial matches were linked
- List of created finding filenames

---

## Rules

1. **Never auto-promote without `--auto` flag.** The user selects which candidates to promote. Human gate is mandatory.
2. **Deduplication is mandatory.** Every candidate gets a dedup check before presentation. One canonical finding per pattern.
3. **Default evidence strength is Medium.** Analysis docs observe patterns in repos — not production telemetry. Only upgrade to Strong with explicit evidence.
4. **Do not create research sources.** Analysis docs are internal artifacts, not external sources. Use inline attribution in the finding body instead.
5. **Preserve the analysis link.** Every promoted finding links back to its source analysis doc via Obsidian wiki-link. Every promoted candidate in the analysis doc links forward to the finding.
6. **Do not modify existing findings without user approval.** If a dedup check finds a full match, present the option to update the existing finding — don't overwrite silently.
