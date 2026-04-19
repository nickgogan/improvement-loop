---
name: Dependency Graph Module Ordering
summary: 13-column CSV format for module metadata with after/before dependency graph replacing sequential numbering, enabling parallel installation of independent modules.
implementation_notes: null
category: Orchestration
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
proposer_priority: P3 (Monitor)
applicability:
- General / Cross-System
adopted_in: []
sources:
- bmad-v610-v622-changelog.md
related_findings:
- file: bmad-help-adaptive-module-routing.md
  rel: enables
proposals: null
date_discovered: '2026-04-07'
last_updated: '2026-04-08'
pipeline_status: raw
consumed_by: []
---
# Dependency Graph Module Ordering

## What It Is
A module metadata format using a 13-column CSV structure with explicit `after` and `before` dependency fields that form a directed acyclic graph (DAG) for determining module installation and execution order. Introduced in the BMAD Method for module-help to replace simple sequential numbering with a dependency graph. Each module row contains 13 columns of metadata — including dependency relationships — that allow a help system or installer to compute correct ordering, identify independent modules eligible for parallel execution, and detect circular dependencies.

## Why It Matters
Sequential numbering (module 1, module 2, module 3) encodes a total order even when only a partial order exists. This forces serial execution of modules that have no actual dependency relationship, wasting time and preventing parallelism. A dependency DAG encodes only the real constraints, making the implicit dependency structure explicit and machine-readable. For systems with many modules, the difference between serial and parallel installation can be significant.

## Why People Are Using It
The BMAD Method adopted this pattern for its module-help system, where the growing number of modules made sequential ordering increasingly brittle — adding a new module required renumbering or inserting fractional positions. The `after`/`before` fields make insertion of new modules trivial (just declare what it depends on) and removal safe (check for dependents first). The 13-column CSV format keeps the metadata human-readable while being trivially parseable by both LLMs and scripts.

## Potential Improvements
The CSV format could be augmented with optional dependency types (hard vs. soft, build-time vs. runtime) to support more nuanced ordering decisions. A visualization tool that renders the DAG as a graph would aid debugging when dependency chains become complex. Cycle detection should be built into any consumer of this format.

## Potential Failure Modes
Dependency graphs can become stale if module authors forget to update `after`/`before` fields when internal dependencies change. Implicit dependencies (e.g., module A writes a file that module B reads, but neither declares the relationship) will not be captured. The 13-column format may become unwieldy if metadata requirements grow — a structured format (YAML, JSON) might scale better than CSV for high column counts.
