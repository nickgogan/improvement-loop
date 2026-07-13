---
name: "Five-Field Spec Kernel with Typed Companions and Preservation Validation"
summary: |-
  Plain English: distill ANY input — raw idea, PRD, codebase, transcript — into one
  five-field kernel (Problem, Capabilities, Constraints, Non-goals, Success signal),
  route overflow into typed companion documents, and validate the distillation by
  walking the source claim-by-claim so every omission is logged rather than silent.
  BMAD v6.10.0's bmad-spec produces SPEC.md under an eight-rule Spec Law (intent +
  success per capability; WHAT not HOW; constraints must bind; explicit non-goals;
  testable success signal; stable IDs; preservation; lean prose). A load-bearing test
  routes content that matters into companions typed by ownership (spec-authored vs
  adopted read-only); downstream skills discover inputs via frontmatter `companions:`
  and `sources:` lists — a sealed file contract with stable IDs (CAP-N, AD-n) that
  survive updates. Self-validation runs two passes: coherence, then preservation —
  pass 2 walks the source claim-by-claim and logs "wrapper-only content" drops.
implementation_notes: null
category: "Intent Engineering"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: "P3 (Monitor)"
applicability:
  - "General"
adopted_in: []
sources: []
related_findings:
  - file: "artifact-as-contract-pattern.md"
    rel: "same-problem"
  - file: "plans-that-carry-their-own-contract.md"
    rel: "same-problem"
  - file: "derive-dont-edit-artifacts-as-log-renders.md"
    rel: "extends"
  - file: "architecture-spine-invariants-vs-seed-divergence-test.md"
    rel: "same-problem"
proposals: null
date_discovered: "2026-07-13"
last_updated: "2026-07-13"
pipeline_status: "raw"
consumed_by: []
tags:
  - "intent-engineering"
  - "specification"
  - "file-contracts"
---

# Five-Field Spec Kernel with Typed Companions and Preservation Validation

## What It Is

A specification architecture with three load-bearing parts:

1. **The kernel.** Every input shape distills to five fields: Problem, Capabilities
   (each with intent + success), Constraints, Non-goals, Success signal — governed by
   an eight-rule Spec Law (WHAT not HOW; constraints must bind; explicit non-goals;
   testable success signal; stable IDs; preservation; lean prose). "Read the input to
   know the job": a spec package, raw idea, codebase, or existing document each route
   differently into the same kernel.
2. **Typed companions.** Content that is load-bearing but not kernel-shaped goes to
   companion documents typed by ownership — spec-authored (the spec skill may rewrite)
   vs adopted (read-only to the adopting skill). SPEC.md frontmatter seals the
   contract: `companions:` lists what downstream MUST read, `sources:` lists
   fully-absorbed inputs downstream must NOT re-read; process metadata is excluded.
   Stable IDs (CAP-N, AD-n) survive updates so cross-artifact citations hold.
3. **Preservation validation.** Two self-validate passes: coherence, then a
   claim-by-claim walk of the source that logs dropped "wrapper-only content" — so
   omissions are decisions on the record, not silent losses.

## Why It Matters

Spec formats usually fail in one of two ways: they balloon (everything is in the spec,
nothing is authoritative) or they compress lossily (the distillation silently drops
constraints someone needed). The kernel-plus-companions split solves the first with a
hard five-field boundary and typed overflow; the preservation pass solves the second by
making every omission auditable. The sealed frontmatter contract turns the handoff from
"conversation about what to read" into a machine-checkable manifest — what the v6.8.0
changelog calls "a sealed file contract, not a translation layer."

## Why People Are Using It

The spec kernel is the hub of BMAD's rebuilt product layer — PRD, UX, architecture, and
epics all read/write against it, in any order, via the shared memlog. Source: Observed
in [BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) v6.10.0 — see
[[bmad-method-analysis]] for structural details.

## Potential Alternatives

- **Template-driven full specs** (PRD templates) — comprehensive but unbounded; no
  kernel/companion pressure keeps them lean.
- **Artifact-as-contract chains** (GSD) — the contract idea without the fixed kernel or
  the preservation audit.
- **User stories + acceptance criteria only** — lighter, but loses constraints and
  non-goals, the two fields that bind downstream builders.

## Potential Improvements

- Deterministic lint for Spec Law compliance (testable-success-signal presence, ID
  stability across versions).
- Preservation-pass tooling: a diff-based claim extractor would make the
  claim-by-claim walk cheaper and more reliable.

## Potential Failure Modes

- **Kernel overflow into companions** — the five-field discipline can be laundered by
  putting everything load-bearing in companions; the load-bearing test needs teeth.
- **Preservation-pass theater** — an LLM can claim it walked the source; without
  logging the drops per claim, pass 2 degrades to assertion.
- **Stable-ID erosion** — regenerated specs that renumber CAP-N break every downstream
  citation; ID stability is the contract's weakest structural point.
