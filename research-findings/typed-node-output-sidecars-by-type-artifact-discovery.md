---
name: "Typed Node-Output Sidecars for By-Type Artifact Discovery"
summary: |-
  Plain English: when one workflow step produces a file another step needs, have the
  engine write the output under a declared *type* instead of making downstream steps
  guess filenames. In Archon v0.5.0, any workflow node can declare `output_type`; the
  executor then writes a typed sidecar pair — `$ARTIFACTS_DIR/nodes/<id>.md` (content)
  plus `<id>.meta.json` (metadata) — so downstream nodes and even later runs locate
  outputs by declared type rather than by filename convention or prompt-encoded
  agreements. A small, generalizable contract for cross-step (and cross-run) artifact
  handoff that removes a whole class of "the next step couldn't find the file" failures.
implementation_notes: null
category: "Orchestration"
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
  - file: "archon-yaml-defined-harness-workflows.md"
    rel: "extends"
proposals: null
date_discovered: "2026-07-13"
last_updated: "2026-07-13"
pipeline_status: "raw"
consumed_by: []
tags:
  - "orchestration"
  - "artifact-handoff"
  - "context-engineering"
  - "archon"
---

# Typed Node-Output Sidecars for By-Type Artifact Discovery

## What It Is

Archon v0.5.0 lets any workflow node (command, prompt, bash, script, loop) declare an `output_type`. When set, the executor writes a **typed sidecar pair** alongside normal execution:

- `$ARTIFACTS_DIR/nodes/<id>.md` — the node's output content
- `$ARTIFACTS_DIR/nodes/<id>.meta.json` — machine-readable metadata including the declared type

Downstream consumers — later nodes in the same run, or later runs entirely — locate outputs **by declared type**, not by hardcoded filename conventions or prompt-level agreements ("write your plan to plan.md"). The mechanism complements `$nodeId.output` variable substitution (in-band, within-run) with an out-of-band, filesystem-durable channel that survives across runs.

## Why It Matters

File-mediated handoff between agent steps usually rests on fragile naming conventions: the producing prompt says "save as prd.md", the consuming prompt says "read prd.md", and any drift in either prompt silently breaks the chain. Registering the artifact's *type* with the engine moves the discovery contract from prose (unenforceable) to metadata (queryable). It is the artifact-as-contract idea with an addressing scheme attached: contracts are only as good as the consumer's ability to find the right instance, and `meta.json` sidecars make artifacts self-describing rather than convention-located. The pattern is engine-agnostic — any file-mediated multi-step pipeline (including file-handoff agent pipelines generally) can adopt "content file + typed meta sidecar" without adopting anything else.

## Why People Are Using It

Observed in [Archon](https://github.com/coleam00/archon) v0.5.0 — see [[archon-analysis]] for structural details. Introduced alongside the matured loop nodes and the schema-strict `$nodeId.output` data flow — the sidecars serve the cases substitution can't: large artifacts, cross-run consumption, and UI surfacing (the run console links artifact paths directly).

## Potential Alternatives

Filename conventions in prompts (the status quo it replaces). In-band variable substitution only (bounded by context size, within-run only). A full artifact store/database (heavier; loses plain-filesystem inspectability).

## Potential Improvements

Schema validation per output type (typed today means *labeled*, not *validated*). Type registries so producers and consumers share a vocabulary. Retention/GC policy for cross-run artifacts.

## Potential Failure Modes

Type labels without validation can lie — a node declaring `output_type: prd` can still emit garbage that downstream nodes trust because the sidecar exists. Two nodes declaring the same type in one run reintroduce ambiguity (which `prd` is current?). Cross-run consumption couples runs implicitly, complicating reproducibility.
