---
name: "Plans That Carry Their Own Contract: Global Constraints and Per-Task Interfaces"
summary: |-
  Plain English: a plan handed to context-isolated implementers must carry its own
  binding context — project-wide requirements copied verbatim into a Global
  Constraints header, and a per-task Interfaces block (Consumes/Produces with exact
  signatures) so an implementer who sees only its own task still knows its neighbors'
  contracts. Superpowers v6.0.0's writing-plans mandates both blocks plus task
  right-sizing ("the smallest unit that carries its own test cycle and is worth a
  fresh reviewer's gate") and a "No Placeholders" list framed as plan failures.
  Upstream testing: structured plans needed one fix round vs two-to-four for control
  (which also shipped a real bug). The structure downstream agents used to re-derive
  on every dispatch is authored once into the plan. BMAD v6.10.0 converges with sealed
  file contracts: SPEC.md frontmatter lists what downstream MUST read and must NOT
  re-read, with stable IDs surviving updates.
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
    rel: "extends"
  - file: "war-game-plan-format-for-executor-handoff.md"
    rel: "same-problem"
  - file: "five-field-spec-kernel-with-typed-companions.md"
    rel: "same-problem"
  - file: "l-d-hypothesis-information-loss-across-agent-bound.md"
    rel: "extends"
proposals: null
date_discovered: "2026-07-13"
last_updated: "2026-07-13"
pipeline_status: "raw"
consumed_by: []
tags:
  - "intent-engineering"
  - "plan-contracts"
  - "cross-repo-convergence"
---

# Plans That Carry Their Own Contract: Global Constraints and Per-Task Interfaces

## What It Is

Plan-structure requirements that front-load what context-isolated downstream agents
would otherwise re-derive or miss:

1. **Global Constraints header.** Project-wide requirements are copied *verbatim* from
   the spec into a mandatory plan header block — because constraints that live only in
   the spec never reach implementers and reviewers who are handed one task's brief.
2. **Per-task Interfaces block.** Each task declares Consumes and Produces with exact
   signatures, so an implementer who sees nothing but its own task knows what its
   neighbors expect and provide.
3. **Task right-sizing.** A task is "the smallest unit that carries its own test cycle
   and is worth a fresh reviewer's gate" — sized to the review architecture, not to
   effort estimates.
4. **No Placeholders.** TBDs and "figure out later" entries are enumerated as plan
   failures caught by plan self-review.

BMAD's sealed file contracts are the same move at the spec boundary: frontmatter
`companions:`/`sources:` manifests declare what downstream must and must not read,
with stable IDs (CAP-N, AD-n) that survive updates.

## Why It Matters

Information loss at agent boundaries is the documented killer of multi-agent pipelines
(the KB's L-D hypothesis finding). The usual mitigations re-derive context per dispatch
— every implementer re-reads the spec, every reviewer reconstructs the constraints —
paying the derivation cost N times with N chances of divergence. Authoring the
contract *into the plan once* moves that work to the point of maximum context (the
planner) and makes each dispatch cheap and consistent. The upstream A/B evidence (one
fix round vs two-to-four, control shipped a real bug) is unusually direct for a
document-structure change. Two frameworks converging on carried-contract handoffs —
plan blocks in one, sealed frontmatter manifests in the other — marks the pattern, not
the syntax, as the durable part.

## Why People Are Using It

Mandated by Superpowers' writing-plans skill since v6.0.0, feeding its file-mediated
dispatch flow; BMAD's v6.8.0 changelog states the parallel directly ("a sealed file
contract, not a translation layer"). Sources: Observed in
[superpowers](https://github.com/obra/superpowers) v6.1.1 — see
[[superpowers-analysis]] — and [BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD)
v6.10.0 — see [[bmad-method-analysis]].

## Potential Alternatives

- **Artifact-as-contract chains** (GSD) — artifacts are contracts between phases, but
  the contract is the whole artifact; no verbatim-constraint or per-task interface
  extraction.
- **Re-derivation per dispatch** — each subagent reads the full spec; correct but
  expensive and divergence-prone.
- **Shared-context orchestration** — keep everyone in one context; the approach whose
  scaling failure motivated isolation in the first place.

## Potential Improvements

- Mechanical propagation checks: verify every Global Constraint traces to a spec line
  and every Interfaces signature matches its neighbor's Produces.
- Interface-block reuse as integration-test stubs.

## Potential Failure Modes

- **Verbatim staleness** — copied constraints fork from the spec when the spec is
  amended mid-branch; the copy needs an update trigger.
- **Signature lock-in** — exact Consumes/Produces written at plan time can prematurely
  freeze design decisions an implementer would legitimately revise.
- **Plan bloat** — carried contracts grow plans; right-sizing guidance is the
  counterweight that keeps per-task briefs extractable.
