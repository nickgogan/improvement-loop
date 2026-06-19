---
title: "Schematic Library"
id: "schematics-index"
type: "governance"
category: "governance"
target_system:
  - "improvement-loop"
stage: "active"
created: "2026-06-18"
updated: "2026-06-18"
author: "claude"
source_dd:
  - "DD-104"
  - "DD-107"
tags:
  - "catalog"
  - "schematic"
  - "moc"
aliases:
  - "Schematics MOC"
  - "Schematic Library"
---

# Schematics

The engine's **top-altitude content** (DD-104): evidence-grounded `demand → configuration`
blueprints for agentic systems. A schematic answers "for *this* kind of need, here is a
configuration that works, why it works, and how you'd know it's working." Each carries a
**required evaluation/feedback layer** — the part that makes a configuration self-evolving
rather than a static recipe (DD-107).

## How Schematics Get Here

Schematics are **curated, not pipeline-extracted** (DD-107). They are authored by capturing a
**recurring named cluster** — a configuration the engine has seen work two or more times — not
by walking the full axis cross-product (the design space is sparse). The flow:

1. A cluster recurs (in research, in builds, in the engine's own operation).
2. Someone drafts it against `knowledge/templates/schematic-template.md`.
3. `grounded_in` links are filled with real findings; the evaluation/feedback layer is mandatory.
4. Nick gates promotion (DD-29). Validated schematics become `composed_of` material for new builds.

## Staying Current (Self-Evolution)

A schematic is self-evolving, not a static recipe (DD-107). Two mechanisms keep one honest, and
both route through the same drift scanner:

1. **Grounding moved.** When any `grounded_in` finding's `last_updated` post-dates a schematic's
   `updated` (curation) date, `/detect-drift` flags it for re-evaluation; Nick gates the re-check.
   (Phase 2 Slice 2 — `/detect-drift` reads `knowledge/schematics/` as a scan root.)
2. **Eval layer stays current.** New evaluation/feedback knowledge enters the KB through
   **Dimension 7 (Evaluation)** scans, new autonomy/governance knowledge through **Dimension 9
   (Governance)** scans (`operations/references/research-dimensions.md`). Because every schematic's
   *required* Evaluation & feedback layer — and its autonomy choice — is `grounded_in` such
   findings, a D7/D9 scan that updates one of them routes straight back to schematic re-evaluation
   through mechanism (1). The D7 route is well-exercised: the audit and research seeds ground their
   eval layers in [[agent-self-reporting-unreliability-independent-eval]] and
   [[llm-as-judge-pattern-for-verification-agents]] (both D7). The D9 route is exercised too — the
   coding workcell grounds its autonomy/review layer in [[compound-review-debt-from-deferred-inspection]]
   (D9) and the operations assistant grounds its autonomy contract in
   [[advisory-only-for-persistent-mutations]] (D9). So a scan that bumps any of these re-flags the
   schematic that leans on it.

So `/detect-drift` is the "grounding moved" half and the D7/D9 scan→drift route is the "eval layer
stays current" half — together they keep the self-evolving promise live, not aspirational.

## Catalog

| Schematic | Altitude | Maturity | Function |
|-----------|----------|----------|----------|
| [[research-scanning-agent\|Research-Scanning Agent]] | middle | seed | research |
| [[scheduled-operations-assistant\|Scheduled Operations Assistant]] | middle | seed | operations |
| [[codebase-audit-workcell\|Codebase-Audit Workcell]] | top | seed | audit |
| [[project-coding-workcell\|Project-Scoped Coding Workcell]] | top | seed | coding |

## Dataview Query

```dataview
TABLE altitude, maturity, target_system, stage
FROM "systems/improvement-loop/knowledge/schematics"
WHERE type = "schematic"
SORT updated DESC
```
