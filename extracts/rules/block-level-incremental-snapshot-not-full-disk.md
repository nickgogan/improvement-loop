---
title: "Block-Level Incremental Snapshot, Not Full-Disk"
type: "extracted-artifact"
assigned_form: "rule"
source_finding: "incremental-snapshotting-copy-on-write-block-diffing"
identification_report: "session-persistence-and-memory.harvest-queue.md::incremental-snapshotting-copy-on-write-block-diffing::rule::block-level-incremental-snapshot-not-full-disk"
extraction_date: "2026-07-19"
last_change_session: 152
last_change_report: "session-persistence-and-memory.harvest-queue"
deployed: false
deployed_to: null
context:
  applies_to:
    - "anyone designing durable, restartable disk state for a sandboxed code-execution or agent-runtime environment"
    - "infrastructure builders evaluating checkpoint/restore mechanisms for long-running or fleet-distributed workloads"
    - "teams choosing between full-copy backup and incremental-diff persistence for any writable execution volume"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "build"
  reversibility: "medium — a full-disk-snapshot implementation can be replaced with incremental block-level diffing later, but the swap touches the storage layer, snapshot-ID format, and lineage/restore logic, not just a config flag"
  auditability: "high — a snapshot's payload size is directly observable and verifiable against the actual changed-block set; a full-disk snapshot masquerading as incremental would show anomalously large diffs on small edits"
  evidence_strength: "Strong"
  adoption:
    status: "Not Yet Started"
    notes: "Production system at OpenAI, powering sandbox disk persistence for ChatGPT and Codex Web at scale. No equivalent adoption signal outside that source at time of extraction; no live code-execution sandbox exists in this workspace to adopt it into today, so this is design-stage grounding for if/when one is built."
contract:
  preconditions: "A system provisions writable, persistent disk state for a sandboxed or isolated execution environment (a microVM, container, or similar) that must survive across restarts, node failures, or branching/checkpoint operations. The underlying filesystem exposes some form of changed-extent or changed-block tracking (e.g., Linux FIEMAP), or an equivalent copy-on-write layer is available."
  invariants: "Every save/checkpoint operation captures only the blocks that changed since the last snapshot — never a full copy of the disk. Snapshot granularity is block-level, not file-level, to avoid write amplification on large files that change only slightly. Snapshot scope is configurable (e.g., whole root filesystem vs. a specific subdirectory) rather than hardcoded to 'everything.' A restore operation can reconstruct the full disk state by replaying a snapshot's diff lineage on top of the base image."
  governance: "Owner: whoever designs or maintains the sandbox/execution-environment storage layer. The incremental, block-level requirement should be stated explicitly as a design constraint before implementation begins — not left as an assumed property of whatever snapshot library is picked first. Any code-execution or agent-sandbox capability this workspace builds in the future inherits this as a stated precondition, per the source finding's implementation note."
  recovery: "If an implementation defaults to full-disk snapshots (the common first-pass shape) → treat this as a design defect once discovered, not an acceptable interim state; the source evidence states full snapshots are cost-prohibitive at any meaningful scale ('would bankrupt the company'). If block-level diffing is unavailable on the target filesystem (no extent-tracking support) → fall back to file-level diffing as an explicitly acknowledged degradation, not a silent substitute, since file-level diffing reintroduces write amplification on large, slightly-changed files. If snapshot lineages grow unbounded with no compaction — a gap the source finding itself flags as undiscussed — treat it as an open design question to resolve before production use, not an oversight to ignore."
tags:
  - "extracted-artifact"
  - "rule"
  - "sandboxing"
  - "infrastructure"
  - "persistence"
---

# Block-Level Incremental Snapshot, Not Full-Disk

**Source:** [[incremental-snapshotting-copy-on-write-block-diffing]]
**Form:** rule
**Extraction date:** 2026-07-19

## Condition

A system provisions persistent, writable disk state for a sandboxed or isolated code-execution environment (a microVM, container, or comparable isolation boundary) and needs that state to survive node failure, support long-running or multi-day tasks, or support branching/checkpoint-style exploration (try a path, restore, try another).

## Action

**Required:** Snapshot only the blocks that changed since the last snapshot, using block-level (not file-level) diffing, with a configurable scope (whole filesystem vs. specific directories). Restore by replaying the chain of incremental diffs onto the base image.

**Forbidden:** Snapshotting the entire disk on every save. Diffing at file granularity when files are large and change only slightly (this reintroduces the write-amplification problem block-level diffing exists to avoid). Hardcoding snapshot scope to "everything" when a narrower scope would suffice.

## Boundary

Enforced at the point where the storage/persistence layer for a sandboxed execution environment is designed and implemented — specifically at the `save()`/checkpoint call and the corresponding restore path. This is an infrastructure design constraint, not a runtime check on individual agent actions.

## Enforcement

- **Mechanism:** The save/checkpoint implementation must use extent- or block-level change tracking (e.g., Linux `FIEMAP` or an equivalent copy-on-write layer) to compute a diff, and must upload/persist only that diff.
- **Check (observable):** Snapshot payload size scales with the amount of data actually changed, not with total disk size. A snapshot after a small edit should be small; a snapshot whose size is roughly constant regardless of how much changed is evidence of a full-copy implementation masquerading as incremental.
- **Violation response:** A full-disk snapshot design that has already shipped is a defect to be corrected, not a tradeoff to be accepted — the cost curve is described as prohibitive at scale in the source evidence, and retrofitting after storage costs bite is a known repeated failure shape.

## Rationale

Full-disk snapshots are viable at small scale or low snapshot frequency, but they fail exactly where sandboxed agent execution needs them most: fleet-wide reliability (restoring a checkpoint on a different node after failure), long-running tasks (checkpointing a multi-day run repeatedly), and Monte-Carlo-style exploration (checkpoint, try, backtrack, try again — potentially many times per task). Each of these use cases depends on snapshot/restore being cheap enough to call constantly. Full-disk copying breaks that economics at scale; file-level diffing degrades on large files that change incrementally. Block-level, incremental, configurably-scoped snapshotting is the specific combination that keeps checkpointing cheap enough to be a routine operation rather than an expensive one reserved for rare moments.

## Failure Modes

- **Scope creep toward full snapshots.** Defaulting to "snapshot the whole root filesystem" instead of scoping to the directories that actually change is a real design temptation, even after the incremental/block-level requirement is met — configurable scope exists specifically to counter this.
- **Unbounded lineage growth.** If snapshots chain as diffs against prior diffs with no compaction or garbage collection, a long-lived sandbox accumulates an ever-longer restore chain, and every restore eventually pays for downloading and replaying the full history. Not resolved in the source evidence; treat as an open design question.
- **Retrofitting after the fact.** Building a full-disk-snapshot implementation first and attempting to convert to incremental block-level diffing later is costlier than designing for it from the first version, because the snapshot-ID format, diff-chain/lineage model, and restore logic are all shaped by the choice.
- **Missing extent-tracking support.** Block-level diffing depends on the underlying filesystem exposing changed-extent information (e.g., `FIEMAP`); this is not a universal capability across all storage backends or operating systems, and its absence forces a fallback (see Recovery).

## Contract

### Preconditions
A system provisions writable, persistent disk state for a sandboxed or isolated execution environment (a microVM, container, or similar) that must survive across restarts, node failures, or branching/checkpoint operations. The underlying filesystem exposes some form of changed-extent or changed-block tracking (e.g., Linux FIEMAP), or an equivalent copy-on-write layer is available.

### Invariants
Every save/checkpoint operation captures only the blocks that changed since the last snapshot — never a full copy of the disk. Snapshot granularity is block-level, not file-level, to avoid write amplification on large files that change only slightly. Snapshot scope is configurable (e.g., whole root filesystem vs. a specific subdirectory) rather than hardcoded to "everything." A restore operation can reconstruct the full disk state by replaying a snapshot's diff lineage on top of the base image.

### Governance
Owner: whoever designs or maintains the sandbox/execution-environment storage layer. The incremental, block-level requirement should be stated explicitly as a design constraint before implementation begins — not left as an assumed property of whatever snapshot library is picked first. Any code-execution or agent-sandbox capability this workspace builds in the future inherits this as a stated precondition, per the source finding's implementation note.

### Recovery
If an implementation defaults to full-disk snapshots (the common first-pass shape) → treat this as a design defect once discovered, not an acceptable interim state; the source evidence states full snapshots are cost-prohibitive at any meaningful scale ("would bankrupt the company"). If block-level diffing is unavailable on the target filesystem (no extent-tracking support) → fall back to file-level diffing as an explicitly acknowledged degradation, not a silent substitute, since file-level diffing reintroduces write amplification on large, slightly-changed files. If snapshot lineages grow unbounded with no compaction — a gap the source finding itself flags as undiscussed — treat it as an open design question to resolve before production use, not an oversight to ignore.
