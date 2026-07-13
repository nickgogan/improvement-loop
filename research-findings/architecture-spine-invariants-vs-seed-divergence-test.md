---
name: "Architecture Spine: Invariants vs Seed, with a Divergence Admission Test"
summary: |-
  Plain English: an architecture document should permanently fix ONLY the decisions
  that keep independently-built units from diverging incompatibly — everything else is
  scaffolding the code will own. BMAD v6.10.0's bmad-architecture produces
  ARCHITECTURE-SPINE.md under an explicit admission test: a decision enters the spine
  only if "two units one level down, built independently, could choose incompatibly"
  AND the choice is non-obvious AND a real trade-off exists — otherwise it is Deferred.
  Everything structural is marked "seed: true at cold-start, owned by the code once it
  exists." Architecture decisions (AD-n) carry Binds/Prevents/Rule fields; child spines
  inherit parent ADs as binding, read-only constraints — a conflicting local AD is "a
  conflict to surface, not a local override." A deterministic linter (lint_spine.py, 28
  regression tests) checks spine shape before rubric/lens review.
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
  - file: "five-field-spec-kernel-with-typed-companions.md"
    rel: "same-problem"
  - file: "context-partition-as-versioned-architectural-decision.md"
    rel: "same-problem"
proposals: null
date_discovered: "2026-07-13"
last_updated: "2026-07-13"
pipeline_status: "raw"
consumed_by: []
tags:
  - "intent-engineering"
  - "governance"
  - "architecture-decisions"
---

# Architecture Spine: Invariants vs Seed, with a Divergence Admission Test

## What It Is

A minimalism discipline for architecture documents, built from four rules:

1. **The divergence admission test.** A decision is spine-worthy only if independently
   built units one level down could choose incompatibly without it, AND the right
   choice is non-obvious, AND there is a real trade-off. Fail any leg → Deferred, not
   decided.
2. **Invariants vs seed.** Structural content that fails the test but is needed to
   start is marked `seed: true` — authoritative at cold-start, owned by the code once
   it exists. The document does not pretend to govern what the codebase will.
3. **Typed decisions with inheritance.** Each AD-n entry carries Binds / Prevents /
   Rule. Child spines inherit parent ADs as binding, read-only constraints; a
   conflicting local AD must be surfaced as a conflict, never silently overridden.
4. **Deterministic pre-review.** `lint_spine.py` (28 regression tests) structurally
   checks the spine before any rubric walker or reviewer lens runs — shape problems
   never reach judgment-based review.

## Why It Matters

Architecture docs fail by maximalism: they fix everything, so they are wrong about most
things within weeks, so builders stop reading them. The divergence test is a crisp,
askable question that bounds the document to exactly the decisions whose absence causes
incompatibility — the smallest set that still coordinates parallel work, which is what
matters when the parallel workers are context-isolated agents. The seed marking is the
honest complement: cold-start scaffolding is provided without being canonized.

## Why People Are Using It

The spine is the coordination artifact for BMAD's implementation phase, including its
unattended dev loop where builders cannot ask clarifying questions; inheritance +
read-only parent ADs is how multi-level systems keep child designs compatible. Source:
Observed in [BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) v6.10.0 — see
[[bmad-method-analysis]] for structural details.

## Potential Alternatives

- **Full architecture documents** — richer context, but no admission discipline; drift
  and reader distrust follow.
- **ADR logs** — capture decisions with rationale but rarely define an admission bar or
  an inheritance/override semantics.
- **No document, conventions in code** — works until two agents build siblings
  simultaneously; exactly the case the divergence test targets.

## Potential Improvements

- Applying the divergence test retroactively to existing governance sets as a pruning
  audit (which standing decisions would fail admission today?).
- Tooling for seed expiry: detect when code now owns a seeded choice and mark the
  spine entry lapsed.

## Potential Failure Modes

- **Test gaming** — "could they choose incompatibly?" is judgment; a motivated author
  can argue anything in. The non-obvious and real-trade-off legs need honest review.
- **Under-specification** — a spine that defers too much pushes coordination cost into
  discovery-time conflicts between built units.
- **Inheritance rigidity** — binding read-only parent ADs can force a child to build
  around a parent mistake; the surface-the-conflict path must actually lead somewhere.
