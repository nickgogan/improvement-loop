---
name: "Derive-Don't-Edit: Artifacts as Renders of a Decision Log"
summary: |-
  Plain English: make the append-only decision log the canonical truth and treat the
  polished artifact (spec, architecture doc, PRD) as a derived view that is re-rendered
  from the log — never hand-patched. BMAD v6.10.0 applies this across its product
  layer: SPEC.md, ARCHITECTURE-SPINE.md, and the PRD are each distilled from the run's
  `.memlog.md` at finalize; each artifact has a single writer skill; hand-edits are
  overwritten on the next derive. Stated payoff: the surrounding stages (PRD, UX,
  architecture, epics) can run in ANY order against the same spec "without merge
  drift: the log only accumulates, the artifact is re-rendered." The artifact/memory
  inversion — canonical truth moved from the rendered document to the log — is what
  makes the pipeline order-independent and resumes cheap.
implementation_notes: |-
  Relevant to the engine's PROGRESS/HISTORY spine and IB-172: PROGRESS.md is already
  reconciled-in-place by a single writer (/session-handoff), but it is hand-maintained
  truth, not a derived view. The derive-don't-edit inversion is the design question to
  evaluate — whether session-ops artifacts should render from an append-only substrate
  rather than be the substrate.
category: "Context Engineering"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: "P2 (Design Required)"
applicability:
  - "General"
adopted_in: []
sources: []
related_findings:
  - file: "append-only-run-log-as-working-memory.md"
    rel: "enabled-by"
  - file: "artifact-as-contract-pattern.md"
    rel: "same-problem"
  - file: "five-field-spec-kernel-with-typed-companions.md"
    rel: "extended-by"
proposals: null
date_discovered: "2026-07-13"
last_updated: "2026-07-13"
pipeline_status: "synthesized"
consumed_by:
  - "defending-agent-context.md"
  - "session-persistence-and-memory.md"
  - "rules/derived-artifacts-single-writer-rule.md"
tags:
  - "context-engineering"
  - "orchestration"
  - "derived-artifacts"
---

# Derive-Don't-Edit: Artifacts as Renders of a Decision Log

## What It Is

A write-discipline rule pair over shared artifacts:

1. **Artifacts are derived, not edited.** The canonical record is the append-only
   memlog; SPEC.md and its siblings are distilled from it at finalize. The skill prose
   states it directly: "SPEC.md … DERIVED from .memlog.md, never hand-edited." A
   hand-edit is not merged — it is overwritten on the next derive.
2. **One writer per artifact.** bmad-spec is SPEC.md's single writer; adopted companion
   documents are read-only to the adopting skill. Other skills contribute by appending
   to the shared log (bmad-architecture "captures missing answers into a shared spec
   workspace through the same memlog.py, so bmad-spec can later derive SPEC.md without
   drift").

The enforcement is soft (stated rule) plus structural (the derive step's overwrite makes
hand-edits futile).

## Why It Matters

Multi-stage pipelines usually serialize because each stage edits the shared artifact
and edits conflict. Inverting truth into an accumulate-only log dissolves the conflict:
contributions append in any order, and the artifact is just the latest render. That
buys order-independent stages, cheap resumes (re-render, don't reconcile), and an
automatic audit trail — the artifact can always be explained by the log that produced
it. It is event-sourcing applied to agent-produced documents.

## Why People Are Using It

Canonical across BMAD's rebuilt flagship product skills (spec, PRD, architecture) as of
v6.7.0–v6.10.0; the changelog frames the pattern as what enables its order-independent
pipeline. Source: Observed in
[BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) v6.10.0 — see
[[bmad-method-analysis]] for structural details.

## Potential Alternatives

- **Artifact-as-contract with sequential stages** (GSD-style) — artifacts are canonical
  and stages run in order; simpler, but ordering is load-bearing.
- **Merge-based collaboration** (git-style three-way merges on the artifact) — handles
  concurrency but not semantic drift; agents merge text, not decisions.
- **Database-backed structured state** — same inversion with stronger types, heavier
  machinery.

## Potential Improvements

- Deterministic render checks: lint that an artifact matches a fresh derive of its log
  (drift detection between renders).
- Partial re-renders for very large artifacts to bound derive cost.

## Potential Failure Modes

- **Silent hand-edit loss** — the overwrite-on-derive rule destroys human edits made in
  the artifact; contributors must know the log is the only writable surface.
- **Render nondeterminism** — LLM-performed derives can render the same log
  differently; the "same truth" guarantee is only as stable as the derive procedure.
- **Log-quality ceiling** — artifacts can only be as good as what was logged; decisions
  made but not logged vanish from every future render.

## Extraction Note — 2026-07-13
Extracted as **rule**: [[derived-artifacts-single-writer-rule]] in `extracts/rules/` (harvest-queue promotion, DD-101)
