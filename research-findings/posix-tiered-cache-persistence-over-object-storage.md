---
name: "Always-On Persistence via POSIX-Compliant Tiered Cache over Object Storage"
summary: |-
  OpenAI's second persistence paradigm for agent sandboxes — no explicit save call
  needed. A real POSIX-compliant filesystem is built on top of durable object storage
  (GCS/S3/durable block storage) and exposed to the microVM as an ordinary block device
  via NBD (Network Block Device). Writes land first in an in-cluster cache tier, which
  writes back to the object-storage tier — a globally tiered, write-back cached
  architecture. NFS was explicitly rejected as the mechanism because it "isn't as
  performant and is not POSIX-compliant," and coding/agentic models are "very good at
  anything POSIX-compliant and standard" — deviating from ordinary filesystem semantics
  degrades agent reliability on routine file operations.
implementation_notes: |-
  Same "no live sandbox today" caveat as the companion incremental-snapshotting finding
  — but if a code-execution surface is ever built, this is the paradigm to reach for
  when the requirement is "never lose agent work" rather than "restore to a named
  checkpoint"; the source frames the two as complementary, not competing, paradigms.
category: "Sandboxing"
evidence_strength: "Strong (production-tested)"
adoption_status: "Not Yet Started"
priority: "P2 (Design Required)"
applicability:
  - "General"
adopted_in: []
sources:
  - "from-fork-to-fleet-agent-sandbox-cloud.md"
related_findings:
  - file: "incremental-snapshotting-copy-on-write-block-diffing.md"
    rel: "same-problem"
  - file: "sandbox-architecture-by-threat-model-microvm-vs-container.md"
    rel: "same-problem"
proposals: null
date_discovered: "2026-07-18"
last_updated: "2026-07-18"
pipeline_status: "raw"
consumed_by: []
tags:
  - "sandboxing"
  - "infrastructure"
---

## What It Is

The second of two persistence paradigms OpenAI names explicitly for agent sandbox
disks — contrasted directly with the explicit `save()` API of the companion
incremental-snapshotting finding. Here, the harness never has to call anything: the
sandbox's block device is backed end-to-end by durable cloud storage. Mechanism: a
POSIX-compliant filesystem is implemented on top of GCS, S3, or another durable block
store, and exposed inside the microVM as an ordinary block device via NBD (Network
Block Device). Writes inside the sandbox go first to an in-cluster cache tier; that
cache tier writes back to the object-storage tier behind it — a tiered, write-back
cached architecture, transparent to the guest. NFS was considered and explicitly
rejected as the underlying mechanism: it is both less performant and not
POSIX-compliant, and the coding/agentic models being sandboxed are pre-trained
overwhelmingly on standard POSIX filesystem behavior, so a non-standard mount degrades
their reliability on ordinary file operations.

## Why It Matters

This makes durability a property of the storage layer rather than a discipline the
harness has to remember to invoke — every write is persisted without an explicit
checkpoint call. It is the direct complement to the companion explicit-snapshot
finding: explicit snapshots give point-in-time restore, branch, and rollback semantics;
always-on persistence guarantees "never lose anything" without being asked. The same
underlying problem — "give the agent a disk that survives" — has two valid solutions
depending on whether the consuming workflow needs named restore points or just
guaranteed no-data-loss for live work.

## Why People Are Using It

Same OpenAI production talk and team as the companion finding, powering ChatGPT and
Codex Web sandbox disks at scale. The POSIX-compliance requirement is called out
specifically because the models being sandboxed are trained on standard filesystem
behavior — reliability, not just performance, is the stated reason NFS was rejected.

## Potential Alternatives

- **NFS** — explicitly rejected: worse performance and not POSIX-compliant.
- **Explicit-save-only** (the companion incremental-snapshotting finding) — cheaper to
  reason about, but requires the harness to remember to call save; a crash between
  saves loses unsaved state.
- **Local-disk-only, no cloud backing** — fastest, simplest, but no durability across
  node failure; the baseline this pattern replaces.

## Potential Improvements

The source itself frames the two paradigms as complementary rather than exclusive —
always-on for the live working state, explicit snapshots for named restore points or
branches — worth treating as a single integrated persistence layer rather than
choosing only one when designing from scratch.

## Potential Failure Modes

- **Write-back durability window** — data is acknowledged locally by the in-cluster
  cache before it is durable in object storage; a node failure inside that window can
  lose writes that the sandbox believed were already saved. This mirrors the
  async-upload durability window in the companion explicit-snapshot finding, one layer
  down.
- **Block-over-object translation overhead** — NBD-over-object-storage adds a
  translation layer (block-device semantics on top of storage that is not natively
  block-shaped); the source gives no latency/throughput detail under contention.
- **Under-specified capacity and eviction policy** — no detail is given on cache-tier
  sizing or eviction; tiered-cache architectures are exactly the kind of "boring
  infrastructure" that is easy to under-invest in until it becomes load-bearing at
  scale.
