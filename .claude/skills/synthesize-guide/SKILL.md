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

---

## Design Decisions

| DD | Relevance |
|---|---|
| DD-81 | Pattern findings route to guide synthesis, not extraction |
| DD-80 | Pipeline architecture (amended by DD-81 for patterns) |
| DD-78 | ContractSpec on every artifact, including guides |
| DD-45 | Knowledge architecture — guides live in meta-system/knowledge/guides/ |
| DD-46 | Pull model — guides are pulled by consuming systems |
