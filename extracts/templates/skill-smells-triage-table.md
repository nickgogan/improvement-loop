---
title: "Skill Smells Triage Table"
type: "extracted-artifact"
assigned_form: "template"
source_finding: "skill-smells-triage-layer-before-full-audit"
extraction_date: "2026-07-19"
last_change_session: 152
last_change_report: "eval-driven-improvement-loops.harvest-queue"
identification_report: null
deployed: false
deployed_to: null
context:
  applies_to:
    - "reviewers who need a cheap 30-second pre-check before committing to a full scored audit of a growing roster of skills, agents, or prompts"
    - "teams whose deterministic validators catch structural problems but miss behavioral or editorial ones"
    - "authors deciding whether a symptom they've noticed warrants a local patch or a full re-audit"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "verify"
  reversibility: "trivial — the table is a review artifact; discarding or revising a row has no migration cost. Growing the table past one page is the one costly-to-reverse drift to watch for."
  auditability: "high — each row states a plainly observable symptom, a named cause, and a pointer to a deep-dive reference; a reviewer can check the verdict rule mechanically (count smells, count categories, check for a category-E hit) without re-deriving judgment"
  evidence_strength: "Medium"
  adoption:
    status: "Not Yet Started"
    notes: "Documented and used in a production skill-authoring reference layer as the first of three audit stages (smells table, then anti-pattern catalog, then scored rubric); no adoption recorded in this system yet."
contract:
  preconditions: "A roster of artifacts (skills, agents, prompts, or similar) exists that is large or growing enough that a full scored audit on every item is too expensive to run routinely. A deterministic structural validator already exists or is planned as a separate, cheaper first pass. Someone has enumerated observable, easy-to-notice symptoms and can map each to a likely cause and a deeper reference."
  invariants: "The table stays scannable in under a minute — one page, one row per symptom. Every row's 'go to' pointer resolves to a maintained deep-dive reference; a pointer to a moved or deleted reference is treated as a defect, not tolerated. The verdict rule is quantified and mechanical (smell count, category count, any-category-E-hit), not left to per-reviewer judgment. Any smell in the safety/side-effects category blocks shipment outright — it is never treated as a patch-and-proceed case."
  governance: "Owner: whoever maintains the roster's audit process (a review lead, an audit-tooling maintainer, or the team collectively). New smell rows are added when a recurring problem is observed at least a few times across the roster, not spun up speculatively. The deep-dive references a row points to are owned by whoever owns that diagnosis area; broken pointers are a maintenance defect assigned back to that owner."
  recovery: "If the table grows past one page → split it, demote rarely-hit rows, or promote them into the full audit rubric instead — a table that's grown to completeness has stopped being the cheap layer it was meant to be. If a 'go to' pointer is found broken → fix or remove the row immediately; an orphaned pointer silently erodes trust in every other row. If the quantified threshold (smell count / category count) proves miscalibrated for this roster → adjust the threshold explicitly and document why, rather than letting reviewers informally override it case by case."
tags:
  - "extracted-artifact"
  - "template"
  - "evaluation"
  - "skill-authoring"
  - "triage"
  - "audit"
---

# Skill Smells Triage Table

**Source:** [[skill-smells-triage-layer-before-full-audit]]
**Form:** template
**Extraction date:** 2026-07-19

A one-page, scannable symptom→cause→pointer table that acts as a 30-second pre-check layered in front of a full scored audit. It doesn't replace the audit — it decides whether the audit is needed and where to look, catching behavioral/editorial problems that deterministic structural validators miss.

## Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `{{ROSTER_NAME}}` | The artifact roster this table triages (e.g., "skills", "agents", "prompts") | Yes |
| `{{CATEGORY_N_NAME}}` | Name of smell category N (e.g., triggering, sizing, authoring craft, evaluation/governance, safety) | Yes (≥1) |
| `{{SMELL_N_SYMPTOM}}` | An observable symptom a reviewer can notice without instrumentation | Per smell |
| `{{SMELL_N_CAUSE}}` | The likely root cause behind that symptom | Per smell |
| `{{SMELL_N_REFERENCE}}` | Pointer to the deep-dive reference that diagnoses this cause in depth | Per smell |
| `{{PATCH_THRESHOLD}}` | Smell count within one category that triggers a local patch (e.g., "1-2") | Yes |
| `{{FULL_AUDIT_THRESHOLD}}` | Smell count/spread that triggers a mandatory full audit (e.g., "3+ across categories") | Yes |
| `{{BLOCKING_CATEGORY}}` | The category (if any) where a single hit blocks shipment outright, never patch-and-proceed | Optional |

## Body

```markdown
# Smells Triage Table: {{ROSTER_NAME}}

A 30-second pre-check before the full audit. Skim each row against the artifact in front of you.

## {{CATEGORY_1_NAME}}
| Symptom | Likely cause | Go to |
|---------|--------------|-------|
| {{SMELL_1_SYMPTOM}} | {{SMELL_1_CAUSE}} | {{SMELL_1_REFERENCE}} |
| {{SMELL_2_SYMPTOM}} | {{SMELL_2_CAUSE}} | {{SMELL_2_REFERENCE}} |

<!-- repeat one section per category -->

## Verdict Rule
- 0 smells → run the deterministic validator and proceed.
- {{PATCH_THRESHOLD}} in one category → patch that smell locally, re-check the category.
- {{FULL_AUDIT_THRESHOLD}} → do not patch in place; run the full scored audit before shipping.
- Any {{BLOCKING_CATEGORY}} smell → block until resolved. Never ship-and-fix-later.

## This Check's Verdict
- Smells found: [list]
- Category spread: [count]
- Verdict: [proceed / patch / full audit / blocked]
```

## Usage

1. **Keep it to one page.** If the table can't be skimmed in under a minute, it has stopped being the cheap layer it was meant to be — split it or promote overgrown sections into the full audit instead.
2. **State the symptom as something noticeable without instrumentation.** Each row's symptom should be checkable by reading the artifact, not by running it — that's what keeps the check at 30 seconds.
3. **Never leave a "go to" pointer unmaintained.** A pointer into a reference that moved or was deleted silently kills trust in the whole table; treat broken pointers as defects, not cosmetic issues.
4. **Make the verdict rule mechanical.** Count smells, count categories, check for a blocking-category hit — the routing decision should not require re-deriving judgment per artifact.
5. **Treat the blocking category as non-negotiable.** A hit in the blocking category (e.g., safety/side-effects) is not eligible for the patch-and-proceed path regardless of how few other smells are present.
6. **Calibrate thresholds to the roster, not import them wholesale.** The patch/full-audit cutoffs are heuristics tuned on the system that originated them — recalibrate for a different roster size or risk profile rather than assuming the same numbers transfer.

## Variation Axis

What drives different renderings of this scaffold:

- **Roster type.** Skills, agents, and prompts surface different smell categories (a prompt roster may not need a "sizing/attention: `wc -l`" row; an agent roster may need a category for tool-scope creep that a skill roster doesn't).
- **Number of categories.** A narrow roster might collapse to two or three categories; a broad, multi-team roster might need five or more.
- **Blocking category presence.** Rosters with side-effecting artifacts (commit/deploy/delete-capable) need an explicit non-negotiable blocking category; purely advisory rosters may not need one at all.
- **Maintenance model.** A single-maintainer roster can keep the deep-dive references informal (a doc section); a multi-team roster needs owned, versioned references per category to avoid orphaned pointers.

## Contract

### Preconditions
A roster of artifacts (skills, agents, prompts, or similar) exists that is large or growing enough that a full scored audit on every item is too expensive to run routinely. A deterministic structural validator already exists or is planned as a separate, cheaper first pass. Someone has enumerated observable, easy-to-notice symptoms and can map each to a likely cause and a deeper reference.

### Invariants
The table stays scannable in under a minute — one page, one row per symptom. Every row's 'go to' pointer resolves to a maintained deep-dive reference; a pointer to a moved or deleted reference is treated as a defect, not tolerated. The verdict rule is quantified and mechanical (smell count, category count, any-category-E-hit), not left to per-reviewer judgment. Any smell in the safety/side-effects category blocks shipment outright — it is never treated as a patch-and-proceed case.

### Governance
Owner: whoever maintains the roster's audit process (a review lead, an audit-tooling maintainer, or the team collectively). New smell rows are added when a recurring problem is observed at least a few times across the roster, not spun up speculatively. The deep-dive references a row points to are owned by whoever owns that diagnosis area; broken pointers are a maintenance defect assigned back to that owner.

### Recovery
If the table grows past one page → split it, demote rarely-hit rows, or promote them into the full audit rubric instead — a table that's grown to completeness has stopped being the cheap layer it was meant to be. If a 'go to' pointer is found broken → fix or remove the row immediately; an orphaned pointer silently erodes trust in every other row. If the quantified threshold (smell count / category count) proves miscalibrated for this roster → adjust the threshold explicitly and document why, rather than letting reviewers informally override it case by case.
