---
title: "Five-Neighborhood Coverage Checklist"
type: "extracted-artifact"
assigned_form: "template"
source_finding: "concept-family-explorer-five-neighborhood-gap-mapping"
extraction_date: "2026-07-19"
last_change_session: 152
last_change_report: "production-agent-execution.harvest-queue"
identification_report: "production-agent-execution.harvest-queue.md::concept-family-explorer-five-neighborhood-gap-mapping::template::five-neighborhood-coverage-checklist"
deployed: false
deployed_to: null
context:
  applies_to:
    - "a research or knowledge-base team that wants to check whether a subject's coverage is lopsided (deep in one direction, blind in another) before committing more research budget"
    - "a planner deciding what to research next in an unfamiliar or partially-mapped domain, who needs a repeatable procedure rather than an ad hoc list of ideas"
    - "any operator building a topic map or content outline who wants a mechanical prompt for 'what am I missing' with an explicit stopping condition"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "specify"
  reversibility: "trivial — a five-row question checklist filled in text; results can be discarded or redone with no downstream migration cost"
  auditability: "high — each neighborhood's answer is a discrete, reviewable list; a human can check the checklist against the existing corpus row by row to confirm nothing in a given direction was skipped"
  evidence_strength: "Medium"
  adoption:
    status: "Not Yet Started"
    notes: "Demonstrated in one production research system at a large enterprise; a worked example mapped a subject across all five neighborhoods and produced roughly a dozen scored, viable gaps from one pass."
contract:
  preconditions: "A subject or domain is named. Some existing coverage of that subject already exists (a corpus, knowledge base, or outline) to diff the discovered concepts against — otherwise every discovered concept trivially counts as a gap and the checklist just becomes a domain outline. The person filling the checklist has enough domain familiarity to name at least a first pass at each neighborhood, even if incomplete."
  invariants: "All five neighborhoods are checked before concluding the subject is covered — skipping a neighborhood (most often Adjacent/cross-over or Frontier, the two least habitual directions) reintroduces the lopsided-coverage failure this checklist exists to prevent. Each neighborhood's answer is diffed against what already exists, not just listed in isolation. The checklist terminates a mapping pass — it does not itself decide which gaps to act on; that is a separate scoring or prioritization step."
  governance: "Owner: whoever maintains the corpus or knowledge base being mapped. The filled checklist is reviewed by a human before any of the discovered gaps are acted on — the checklist surfaces candidates, it does not authorize work on them. Re-run periodically for domains that evolve, since a checklist run today can go stale as the field's frontier moves."
  recovery: "If a neighborhood produces an unmanageable flood of candidates (most common in Adjacent/cross-over for broad subjects): narrow the subject and re-run, or hand-cap the number of candidates carried forward per neighborhood before the next step. If the checklist's answers turn out subjective or inconsistent across runs: have a second reviewer fill it independently and reconcile disagreements rather than trusting a single pass. If a completed checklist is later found to have been run against a stale corpus snapshot: re-diff against current state before treating any gap as still open."
tags:
  - "extracted-artifact"
  - "template"
  - "gap-analysis"
  - "concept-mapping"
  - "research-planning"
---

# Five-Neighborhood Coverage Checklist

**Source:** [[concept-family-explorer-five-neighborhood-gap-mapping]]
**Form:** template
**Extraction date:** 2026-07-19

A five-question checklist that forces coverage of a subject to be checked in every direction — up, sideways, down, diagonal, and forward — rather than the lopsided pattern ad hoc research tends to produce (deep on sub-concepts, blind on neighboring fields and what's emerging). Each neighborhood asks one plain question; answering all five and diffing the answers against existing coverage turns "what am I missing?" into a mechanical, repeatable pass with a natural stopping point.

## Variables

| Variable | Type | Description |
|----------|------|-------------|
| `{{SUBJECT}}` | string | The subject or domain being mapped (e.g., "vector databases"). |
| `{{EXISTING_COVERAGE}}` | reference | Pointer to whatever corpus, knowledge base, or outline the discovered concepts are diffed against. |
| `{{PARENT_CONCEPTS}}` | list, repeating | Broader domain(s) that contain `{{SUBJECT}}`. |
| `{{SIBLING_CONCEPTS}}` | list, repeating | Peers that sit alongside `{{SUBJECT}}` under the same parent. |
| `{{CHILD_CONCEPTS}}` | list, repeating | What `{{SUBJECT}}` decomposes into. |
| `{{ADJACENT_CONCEPTS}}` | list, repeating | Neighboring fields that overlap with or feed into `{{SUBJECT}}`. |
| `{{FRONTIER_CONCEPTS}}` | list, repeating | What is emerging or next at the edge of `{{SUBJECT}}`. |
| `{{GAP_FLAG}}` | boolean, per concept | Whether a discovered concept is already present in `{{EXISTING_COVERAGE}}` (not a gap) or absent (a gap candidate). |

## Body

```markdown
# Coverage Check — {{SUBJECT}}

Diffed against: {{EXISTING_COVERAGE}}

| Neighborhood | Question | Discovered Concepts | Gap? |
|---|---|---|---|
| **Parent** | What broader domain contains this? | {{PARENT_CONCEPTS}} | {{GAP_FLAG}} |
| **Sibling** | What peers sit alongside it under the same parent? | {{SIBLING_CONCEPTS}} | {{GAP_FLAG}} |
| **Child / sub-concept** | What does this decompose into? | {{CHILD_CONCEPTS}} | {{GAP_FLAG}} |
| **Adjacent / cross-over** | What neighboring fields overlap or feed in? | {{ADJACENT_CONCEPTS}} | {{GAP_FLAG}} |
| **Frontier** | What is emerging / next at the edge of the field? | {{FRONTIER_CONCEPTS}} | {{GAP_FLAG}} |

## Coverage Verdict

- Neighborhoods checked: 5 of 5 (all required — do not conclude coverage from a partial pass)
- Gap candidates found: <count of rows flagged as gaps>
- Recommended next step: <score/prioritize gap candidates, or declare this subject saturated for now>
```

## Usage

Fill one row per neighborhood for the named subject, working outward from what is already well-known (Sibling, Child) toward what is habitually skipped (Adjacent, Frontier) — the two directions most likely to be under-covered in ad hoc research. Diff every discovered concept against `{{EXISTING_COVERAGE}}` as you go, not after the fact, so the Gap column reflects the state of the corpus at checklist time. Treat this checklist as the map-first step: complete it before committing research or writing budget to any of the discovered concepts, and hand the flagged gaps to a separate scoring or prioritization step rather than acting on all of them.

## Variation Axis

What drives different renderings of this template:

- **Domain breadth** — narrow subjects produce a short, tractable list per neighborhood; broad subjects can flood the Adjacent/cross-over row in particular, which is the row most prone to unbounded expansion.
- **Corpus maturity** — a young or sparse existing-coverage corpus turns most discovered concepts into gaps; a mature corpus turns the checklist into a smaller, more targeted diff.
- **Rerun cadence** — fast-moving fields need the Frontier row re-checked on a cadence (the frontier moves even when the rest of the family is stable); slow-moving fields can treat a completed checklist as durable for longer.
- **Solo vs. reconciled fill** — a single pass is faster but more subject to one reviewer's blind spots; a second independent fill-and-reconcile pass costs more but catches disagreement in what counts as a gap.

## Contract

### Preconditions
A subject or domain is named. Some existing coverage of that subject already exists (a corpus, knowledge base, or outline) to diff the discovered concepts against — otherwise every discovered concept trivially counts as a gap and the checklist just becomes a domain outline. The person filling the checklist has enough domain familiarity to name at least a first pass at each neighborhood, even if incomplete.

### Invariants
All five neighborhoods are checked before concluding the subject is covered — skipping a neighborhood (most often Adjacent/cross-over or Frontier, the two least habitual directions) reintroduces the lopsided-coverage failure this checklist exists to prevent. Each neighborhood's answer is diffed against what already exists, not just listed in isolation. The checklist terminates a mapping pass — it does not itself decide which gaps to act on; that is a separate scoring or prioritization step.

### Governance
Owner: whoever maintains the corpus or knowledge base being mapped. The filled checklist is reviewed by a human before any of the discovered gaps are acted on — the checklist surfaces candidates, it does not authorize work on them. Re-run periodically for domains that evolve, since a checklist run today can go stale as the field's frontier moves.

### Recovery
If a neighborhood produces an unmanageable flood of candidates (most common in Adjacent/cross-over for broad subjects): narrow the subject and re-run, or hand-cap the number of candidates carried forward per neighborhood before the next step. If the checklist's answers turn out subjective or inconsistent across runs: have a second reviewer fill it independently and reconcile disagreements rather than trusting a single pass. If a completed checklist is later found to have been run against a stale corpus snapshot: re-diff against current state before treating any gap as still open.
