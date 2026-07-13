---
title: "Derived Artifacts, Single Writer — Write Discipline for Log-Rendered Documents"
type: "extracted-artifact"
assigned_form: "rule"
source_finding: "derive-dont-edit-artifacts-as-log-renders"
identification_report: "defending-agent-context.harvest-queue.md::derive-dont-edit-artifacts-as-log-renders::rule::derived-artifacts-single-writer-rule"
extraction_date: "2026-07-13"
last_change_session: 146
last_change_report: "defending-agent-context.harvest-queue"
deployed: false
deployed_to: null
context:
  applies_to:
    - "multi-stage pipelines that produce shared documents (spec, PRD, architecture, design) which several stages contribute to"
    - "agent workflows built on an append-only decision log where polished documents should be re-rendered from that log rather than hand-patched"
    - "teams wanting order-independent pipeline stages, cheap resumes, and an automatic audit trail over agent-produced documents"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "build"
  reversibility: "medium — reverting to hand-editable canonical artifacts is a process change (contributors relearn where to write) but needs no data migration; the accumulated log stays readable either way"
  auditability: "high — single-writer ownership is verifiable (exactly one code path writes each artifact file); derive-don't-edit is checkable by re-deriving the artifact from the log and diffing — any divergence means a hand-edit slipped in or the derive is nondeterministic"
  evidence_strength: "Medium"
  adoption:
    status: "Not Yet Started"
    notes: "Applied across the flagship product skills (spec, PRD, architecture) of a widely used open-source agent method as of its v6.7–v6.10 line; the project's changelog credits this write discipline for enabling its order-independent pipeline."
contract:
  preconditions: "A pipeline produces one or more shared artifacts (spec, PRD, architecture doc, or equivalent) that multiple stages or skills contribute to. An append-only decision log (run log / working memory) exists, or is being introduced, as the canonical record. A derive/render step can regenerate each artifact from the log."
  invariants: "Each artifact is DERIVED from the log at finalize, never hand-edited — a hand-edit is not merged, it is overwritten on the next derive. Each artifact has exactly one writer: the single skill that renders it. All other stages contribute by appending to the shared log, never by writing the artifact directly. The log is the only writable canonical surface; every artifact is a render of it."
  governance: "Owner: the single writer skill designated for each artifact. Contributing stages hold read-only access to artifacts they do not own and write access only to the shared log. Adding a second writer to an artifact, or a policy that lets hand-edits persist through a derive, breaks the invariant the whole pattern rests on and requires review."
  recovery: "Hand-edit discovered in a derived artifact → treat it as already lost (the next derive overwrites it); re-express the intent as a log entry so it survives. Render drift (artifact does not match a fresh derive of its log) → re-derive from the log and investigate the divergence (a stray hand-edit, or a nondeterministic derive procedure). Decision made but never logged → it vanishes from every future render; capture it in the log retroactively."
tags:
  - "extracted-artifact"
  - "rule"
  - "context-engineering"
  - "derived-artifacts"
  - "single-writer"
  - "event-sourcing"
---

# Derived Artifacts, Single Writer — Write Discipline for Log-Rendered Documents

**Source:** [[derive-dont-edit-artifacts-as-log-renders]]
**Form:** rule
**Extraction date:** 2026-07-13

A write-discipline rule pair over shared, pipeline-produced documents. The two clauses are separable but mutually reinforcing: the first makes the log the canonical truth, the second protects that truth from concurrent corruption. Together they turn a stack of hand-maintained documents into event-sourced renders.

## Condition

Fires whenever a multi-stage or multi-contributor pipeline produces shared documents (a spec, a PRD, an architecture doc, a design record) and an append-only decision log is available — or is being chosen — as the working-memory substrate. Applies from the moment two or more stages need to contribute to the same artifact.

## Action

**Required — clause 1 (derive, don't edit):** Treat the append-only log as the canonical record. Produce each polished artifact by *deriving* (re-rendering) it from the log at finalize. When new information arrives, append it to the log and re-derive — never hand-patch the rendered artifact.

**Required — clause 2 (one writer per artifact):** Assign exactly one writer to each artifact — the single skill or step that renders it. Every other stage contributes by appending to the shared log, so the owning writer can later derive the artifact "without merge drift: the log only accumulates, the artifact is re-rendered."

**Forbidden:** Hand-editing a derived artifact and expecting the edit to survive (it is overwritten on the next derive). Letting a second stage write directly into an artifact it does not own. Treating the rendered document, rather than the log, as the surface where contributions land.

## Boundary

Enforced at two points: (1) the derive/finalize step, where the artifact is regenerated from the log — the overwrite makes hand-edits structurally futile; and (2) write-time on each artifact file, where only the designated owner's code path is permitted to write.

## Enforcement

- **Single writer (deterministic):** exactly one code path writes each artifact file. Checkable by inspecting which skills/steps open the file for write — cardinality must be 1. `(writers_of(artifact) == 1)`; any branch >1 → violation.
- **Derive-don't-edit (drift check):** re-derive the artifact from its log and diff against the on-disk file. A non-empty diff means either a hand-edit slipped in (violation) or the derive procedure is nondeterministic (a separate defect to fix). `(rerender(log) == artifact_on_disk)` → compliant.
- **Contribution channel:** contributing stages write to the shared log only; a stage that writes an artifact it does not own is a violation regardless of intent.

## Rationale

Multi-stage pipelines usually serialize because each stage edits the shared artifact and edits conflict — ordering becomes load-bearing. Inverting the canonical truth from the rendered document into an accumulate-only log dissolves the conflict: contributions append in any order, and the artifact is just the latest render. That buys three properties at once — order-independent stages, cheap resumes (re-render, don't reconcile), and an automatic audit trail (the artifact can always be explained by the log that produced it). It is event-sourcing applied to agent-produced documents. The single-writer clause is what keeps the render deterministic in ownership: many appenders to the log, exactly one renderer per artifact.

## Failure Modes

- **Silent hand-edit loss.** The overwrite-on-derive rule destroys human edits made directly in the artifact. Contributors must know the log is the only writable surface — otherwise good edits vanish at the next derive with no warning.
- **Render nondeterminism.** An LLM-performed derive can render the same log differently across runs; the "same truth" guarantee is only as stable as the derive procedure. Pin or constrain the render step, and use the drift check to catch wobble.
- **Log-quality ceiling.** Artifacts can only be as good as what was logged; a decision made but not written to the log vanishes from every future render. The discipline pushes correctness upstream into log hygiene.

## Contract

### Preconditions
A pipeline produces one or more shared artifacts (spec, PRD, architecture doc, or equivalent) that multiple stages or skills contribute to. An append-only decision log exists, or is being introduced, as the canonical record. A derive/render step can regenerate each artifact from the log.

### Invariants
Each artifact is derived from the log at finalize, never hand-edited — a hand-edit is not merged, it is overwritten on the next derive. Each artifact has exactly one writer: the single skill that renders it. All other stages contribute by appending to the shared log, never by writing the artifact directly. The log is the only writable canonical surface; every artifact is a render of it.

### Governance
Owner: the single writer skill designated for each artifact. Contributing stages hold read-only access to artifacts they do not own and write access only to the shared log. Adding a second writer to an artifact, or a policy that lets hand-edits persist through a derive, breaks the invariant and requires review.

### Recovery
Hand-edit discovered in a derived artifact → treat it as already lost; re-express the intent as a log entry so it survives. Render drift (artifact does not match a fresh derive of its log) → re-derive from the log and investigate the divergence. Decision made but never logged → it vanishes from every future render; capture it in the log retroactively.
