---
name: reassess-priorities
description: >-
  Retroactive priority re-evaluation for research findings. Scans the KB for
  findings whose evidence base has grown (new related_findings links, additional
  repo corroboration, evidence_strength upgrades) since their last priority
  assignment. Produces a reassessment report with proposed priority changes.
  Use after batch repo analyses, large research-loop sessions, or periodically.
user-invocable: true
allowed-tools: Read Grep Glob Write
argument-hint: "[--category <cat>] [--dimension <dim>] [--dry-run]"
---

# Reassess Priorities

Retroactive priority re-evaluation for the Research Findings KB. Scans findings for accumulated evidence that may warrant a priority bump — corroborating repo analyses, new related_findings links, evidence_strength upgrades, or adoption changes in the ecosystem.

## When to Use This Skill

- After a batch of repo analyses via `/repo-analyzer` + `/promote-findings`
- After a large `/research-loop` session that added many new findings
- Periodically (monthly or per-milestone) as a KB hygiene pass
- When Nick asks "what findings have gotten stronger since we last looked?"

Do NOT use this skill for:
- Initial priority assignment on new findings — Researcher triage owns this (`/promote-findings` for repo-analysis intake, `/research-loop` for web-source intake)
- Inline priority curation during classification — Curator inline-review owns this (`/identify-artifacts` Step 3.5)
- Classifying findings into forms (that's `/identify-artifacts`)
- Drafting artifacts from findings (that's `/extract-artifacts`)
- Modifying analysis docs (that's `/repo-analyzer --force`)

## Cognitive Disposition

The Reassessor thinks like an evidence auditor — systematic, conservative, evidence-first.

- **Evidence accumulation is the signal.** A finding that was P3 when observed in one blog post may warrant P2 when independently implemented in 3 production repos. Count the sources, not the words.
- **Independence matters.** Three findings from the same author's repos count as one source. Three findings from unrelated orgs (ByteDance, Gastown Hall, Volcengine) count as three.
- **Conservative on upgrades.** Only propose a bump when the evidence genuinely crosses a threshold. "Slightly more evidence" is not a bump — "qualitatively different evidence class" is.
- **Never downgrade without cause.** This skill proposes upgrades. Downgrades require explicit user request and a documented reason (e.g., pattern deprecated, repo abandoned).
- **The user decides.** Present evidence and propose. Never auto-change priorities.
- **Authority hierarchy.** Researcher sets initial priority at intake based on single-finding signal. Curator (Codifier) revises during classification (`/identify-artifacts` Step 3.5) and periodically via this skill. Curator authority dominates — Researcher triage is a useful first guess, not the final word. This skill is the Curator's periodic deep-pass instrument.

## Paths

| Path | Purpose |
|------|---------|
| `systems/improvement-loop/research-findings/` | Research Findings KB (input + output) |
| `systems/improvement-loop/watched-libraries/analysis/` | Analysis docs (evidence source) |
| `systems/improvement-loop/research-sources/` | Research sources (evidence source) |
| `systems/improvement-loop/operations/research-reports/` | Reassessment report (output) |

---

## Arguments

| Argument | Effect |
|----------|--------|
| (none) | Scan all findings in the KB |
| `--category <cat>` | Only scan findings in the specified category (e.g., `Context Engineering`, `Governance`) |
| `--dimension <dim>` | Only scan findings mapped to the specified research dimension |
| `--dry-run` | Produce the report but do not prompt for changes |

---

## Re-evaluation Criteria

A finding is a **reassessment candidate** if any of the following are true:

### Criterion 1: Evidence Accumulation
The finding now has corroborating evidence from **3+ independent sources** (repos, blog posts, papers, production reports) but its `priority` is `null`, `"Not Flagged"`, or `"P3 (Monitor)"`.

**How to count:**
- Each unique repo in `related_findings` or source attribution counts as one source
- Each unique entry in `sources:` frontmatter counts as one source
- Cross-references from analysis doc findings candidates count as one source per repo
- Same author/org across multiple repos counts as **one** source (not independent)

**Threshold:** 3+ independent sources → propose P2. 5+ independent sources with production evidence → propose P1.

### Criterion 2: Evidence Strength Upgrade
The finding's `evidence_strength` is `"Weak (theoretical)"` but it now has evidence from 2+ production-deployed repos (repos with significant star counts, documented production usage, or enterprise backing).

**Threshold:** Weak + 2 production repos → propose upgrade to `"Medium (practitioner-documented)"`.

### Criterion 3: Adoption Signal
The finding's `adoption_status` is `"Not Yet Started"` but MetaSystem has since partially or fully adopted a variant of the pattern. Check by searching the MetaSystem codebase for the pattern name or core concept.

**Threshold:** If MetaSystem now uses a variant → propose `adoption_status: "Partially Adopted"` and flag for priority review.

### Criterion 4: Convergent Implementation
The same pattern appears independently in 3+ analyzed repos with no common ancestry (different authors, different orgs, different tech stacks). This signals genuine convergence rather than copy-paste adoption.

**Threshold:** 3+ independent implementations → propose priority bump of one tier (P3→P2, null→P3, Not Flagged→P3).

### Criterion 5: Related Findings Cluster
The finding has 3+ `related_findings` links with relationship type `extends` or `enables`. A cluster of mutually reinforcing findings suggests the pattern is more significant than any individual finding indicates.

**Threshold:** 3+ extending/enabling links → flag for priority review (no automatic tier proposal — clusters need human judgment).

---

## Procedure

### Step 1: Load and Parse Findings

1. Use `Glob` to find all `*.md` files in `systems/improvement-loop/research-findings/` (excluding `_index.md`).
2. For each finding, use `Read` to extract frontmatter fields:
   - `name`, `category`, `evidence_strength`, `priority`, `adoption_status`
   - `sources` (list), `related_findings` (list with `file` and `rel` fields)
   - `date_discovered`, `last_updated`
3. If `--category` or `--dimension` specified, filter to matching findings only.

### Step 2: Count Evidence Per Finding

For each finding:

1. Count entries in `sources:` frontmatter (unique source files).
2. Count entries in `related_findings:` frontmatter.
3. Use `Grep` to search analysis docs (`watched-libraries/analysis/*.md`) for the finding name or core concept. Count distinct analysis docs that reference it.
4. Deduplicate by author/org — same author across multiple repos = 1 independent source.
5. Record: `total_evidence_count`, `independent_source_count`, `repo_count`, `has_production_evidence`.

### Step 3: Apply Criteria

For each finding, evaluate all 5 criteria. Record which criteria triggered and the proposed change.

### Step 4: Produce Reassessment Report

Write a report to `systems/improvement-loop/operations/research-reports/priority-reassessment-{date}.md`:

```yaml
---
title: "Priority Reassessment Report — {date}"
type: "research-report"
category: "priority-reassessment"
created: "{date}"
author: "improvement-loop"
findings_scanned: {count}
candidates_flagged: {count}
---
```

Report body:

```markdown
# Priority Reassessment Report — {date}

## Summary
- Findings scanned: {count}
- Reassessment candidates: {count}
- Proposed priority bumps: {count}
- Proposed evidence upgrades: {count}
- Proposed adoption status changes: {count}

## Candidates

### {Finding Name}
- **Current priority:** {current}
- **Proposed priority:** {proposed}
- **Criteria triggered:** {list}
- **Evidence summary:** {independent sources, repos, production evidence}
- **Rationale:** {why this warrants a bump}

... (repeat for each candidate)

## No Change (Confirmed)
Findings reviewed but not flagged: {count}
(List omitted — grep the KB for current priorities if needed)
```

### Step 5: Present for User Approval

If not `--dry-run`:
1. Present the candidates table to the user.
2. For each approved change, use `Edit` to update the finding's frontmatter:
   - Update `priority` field
   - Update `evidence_strength` field (if criterion 2 triggered)
   - Update `adoption_status` field (if criterion 3 triggered)
   - Update `last_updated` to today's date
3. Do NOT modify any other fields or body content.

### Step 6: Summary

Report to the user:
- How many findings were scanned
- How many were flagged as candidates
- How many were approved and updated
- How many evidence_strength upgrades were applied
- How many adoption_status changes were applied

---

## Rules

1. **Never auto-change priorities.** Always present proposals for user approval. Human gate is mandatory.
2. **Independence is the key metric.** Three sources from one author = 1 independent source. Count authors/orgs, not documents.
3. **Conservative on upgrades.** Only propose when evidence genuinely crosses a threshold. "Slightly more" is not enough.
4. **Never downgrade.** This skill only proposes upgrades. Downgrades require explicit user request.
5. **Evidence strength follows the existing scale.** Strong (production-tested) > Medium (practitioner-documented) > Weak (theoretical). Don't invent new tiers.
6. **Report is always produced.** Even with `--dry-run`, the report is written. It serves as an audit trail.
7. **Do not modify finding body content.** Only frontmatter fields are updated by this skill.
8. **Respect the Codifier boundary.** This skill reads findings but does not classify forms, draft artifacts, or synthesize guides. Those are other Codifier skills.
