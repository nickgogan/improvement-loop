---
name: dimension-rebalance
description: >-
  Review and reclassify existing research findings after adding new research dimensions.
  Reads all findings, evaluates each against the new dimension definition, proposes
  reclassifications and splits, then executes approved changes. Use after adding a new
  dimension to research-dimensions.md, or when category distribution feels off.
user-invocable: true
allowed-tools: Read Grep Glob Edit
argument-hint: "<dimension-name> [--dry-run]"
---

# Dimension Rebalance

Review existing research findings after a dimension change and reclassify or split findings that belong in the new dimension(s).

## When to Use This Skill

- A new dimension has been added to `systems/improvement-loop/operations/references/research-dimensions.md`
- An existing dimension has been split or renamed
- The category distribution across findings feels unbalanced or forced
- Periodic audit of category accuracy (e.g., after a large batch of findings)

## Procedure

### Step 0: Load Context

1. Read `systems/improvement-loop/operations/references/research-dimensions.md` — get the full set of dimensions and their "What to search for" descriptions. These descriptions are the classification rubric.
2. Identify the **target dimension(s)** — either from the user's argument or by diffing against the last known dimension set. If the user specifies a dimension name, focus on that one. If not, evaluate all dimensions.

### Step 1: Scan Findings

1. Use `Glob` to list all findings in `systems/improvement-loop/research-findings/*.md` (excluding `_index.md`).
2. For each finding, read the `category` field from frontmatter (use `Grep` for efficiency — don't read every full file).
3. Build a category distribution count. Report it.

### Step 2: Identify Candidates

For each target dimension, identify candidate findings that may belong there. Two types:

**Type A — Reclassify:** The finding's current category is wrong. The finding wholly belongs in the new dimension.
- Example: A finding categorized as "Tool Integration" that is actually about multi-agent workflow composition → should be "Orchestration"

**Type B — Split:** The finding covers multiple concerns, one of which belongs in the new dimension. The finding should be split into two findings.
- Example: A finding covering both "Tiered Permission System" (Tool Integration) and "blast radius containment via sandboxing" (Sandboxing) → split into two findings, each with its own category

**How to identify candidates:**
1. For the target dimension, extract key terms from its "What to search for" description.
2. Use `Grep` to search finding bodies for those terms.
3. For each match, read the full finding and evaluate:
   - Does the finding's **primary subject** match the new dimension? → Type A (reclassify)
   - Does the finding **partially overlap** with the new dimension? → Type B (split candidate)
   - Is the match superficial (the term appears but the finding is really about something else)? → Skip

### Step 3: Propose Changes

Present a structured report:

```markdown
## Dimension Rebalance Report: [Dimension Name]

### Current Distribution
[Category counts table]

### Proposed Reclassifications (Type A)
| Finding | Current Category | Proposed Category | Rationale |
|---------|-----------------|-------------------|-----------|

### Proposed Splits (Type B)
| Original Finding | Keep As | New Finding | New Category | Rationale |
|-----------------|---------|-------------|--------------|-----------|

### Borderline Cases (Review Needed)
| Finding | Current Category | Consideration | Why It's Borderline |
|---------|-----------------|---------------|---------------------|
```

**Stop here if `--dry-run` was specified.** Report the proposals and exit.

### Step 4: Human Gate

Present the report to the user. Wait for approval before making any changes. The user may:
- Approve all changes
- Approve selectively (specify which to apply)
- Reject all
- Modify proposals

### Step 5: Execute Approved Changes

**For Type A (reclassify):**
1. Use `Edit` to update the finding's `category` field in frontmatter.
2. Use `Edit` to update the finding's `last_updated` field to today.

**For Type B (split):**
1. Read the original finding fully.
2. Use `Edit` to narrow the original finding to its primary concern:
   - Update `name`, `summary`, body sections to focus on the retained category
   - Update `last_updated` to today
3. Use `Write` to create the new finding file:
   - Derive the name from the split-off concern
   - Copy relevant `sources`, `applicability`, `adopted_in` from the original
   - Set `date_discovered` to the original's date (the pattern was discovered then, just miscategorized)
   - Set `last_updated` to today
   - Write body sections focused on the new dimension's concern
   - Set `priority` based on triage rules
4. Update the original finding's source entries to also reference the new finding.

### Step 6: Report

Report final category distribution. Use `rg -c '^category: "' systems/improvement-loop/research-findings/*.md | cut -d: -f1 | xargs -I{} sh -c 'printf "%s  " "$(basename {})"; rg "^category: " {}'` or similar to get live counts directly from frontmatter.

## Classification Rubric

When deciding which dimension a finding belongs to, use this decision tree:

1. **Is it about what the agent sees at runtime?** → Context Engineering
2. **Is it about which model to use or model capabilities?** → Model Selection
3. **Is it about how instructions are written or structured?** → Prompt Craft
4. **Is it about a specific tool, platform, CLI, or API integration?** → Tool Integration
5. **Is it about goal encoding, autonomy boundaries, or human-agent alignment?** → Intent Engineering
6. **Is it about how agents coordinate, delegate, compose, or manage workflow state?** → Orchestration
7. **Is it about verifying outputs, measuring quality, or testing reliability?** → Evaluation
8. **Is it about execution isolation, permission boundaries, or safe environments?** → Sandboxing
9. **Is it about who decides what, when humans gate, authority delegation, or compliance?** → Governance
10. **Is it about who the agent IS — identity, persona, boot sequence, onboarding, or capability boundary definition?** → Agent Design

If a finding could fit two categories, the **primary subject** (what the finding is *about*) wins. The secondary concern is a candidate for a split.

## Calibration Notes

- **Don't over-split.** A finding that mentions sandboxing in passing while being primarily about orchestration should stay in Orchestration. Only split when both concerns are substantial enough to warrant standalone KB entries.
- **Preserve evidence.** When splitting, both resulting findings should reference the same sources. Don't lose provenance.
- **Category is not a tag.** A finding has one category. If it touches multiple dimensions, the category reflects its primary concern. Tags (in source entries) can reflect secondary concerns.
- **Respect existing priority.** Reclassification doesn't change priority. Splits may need priority re-evaluation for the new finding.
- **The dimension descriptions in research-dimensions.md are authoritative.** If there's ambiguity, re-read the "What to search for" section for each candidate dimension.
