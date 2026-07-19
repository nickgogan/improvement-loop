---
name: "Incremental Disk Snapshotting via Copy-on-Write + Block-Level Diffing"
summary: |-
  OpenAI's explicit "save API" for agent sandbox disks: a copy-on-write writable layer
  sits on top of a base image, and FIEMAP-based extent tracking finds exactly which
  blocks changed since the last snapshot — only that diff is zipped and uploaded, never
  the whole disk. The snapshot call returns immediately while the upload continues in
  the background ("I can actually lie to you while I'm uploading to the cloud"), and
  restores replay a snapshot's full lineage (chain of diffs) back onto the base image.
  Explicit design requirements named: incremental not full (full snapshots "would
  bankrupt the company"), fast save AND fast restore, configurable scope (whole root FS
  vs. specific folders), and block-level over file-level granularity to avoid write
  amplification. This is the infrastructure precondition for three use cases: fleet-wide
  reliability (restore a checkpoint on another node after failure), long-running/
  multi-day agent tasks, and Monte-Carlo-style exploration (checkpoint, try, backtrack,
  try again).
implementation_notes: |-
  No live sandbox/code-execution product exists in MetaSystem today (Claude Build is
  retired); this is design-stage grounding only. If a future code-execution surface is
  ever built, budget for incremental block-level snapshotting (not full-disk) from the
  first version — retrofitting after storage costs bite is the same failure shape the
  same talk's "seven stages of grief" narrative describes for the isolation layer (see
  the UPDATE to sandbox-architecture-by-threat-model-microvm-vs-container.md).
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
  - file: "three-layer-reversible-state-single-undo-surface.md"
    rel: "extends"
  - file: "reversible-forks-enable-parallel-sampling.md"
    rel: "same-problem"
  - file: "posix-tiered-cache-persistence-over-object-storage.md"
    rel: "same-problem"
  - file: "snapshot-lineage-aware-fleet-scheduling.md"
    rel: "enables"
proposals: null
date_discovered: "2026-07-18"
last_updated: "2026-07-18"
pipeline_status: "raw"
consumed_by: []
tags:
  - "sandboxing"
  - "infrastructure"
  - "orchestration"
---

## What It Is

OpenAI's explicit-save mechanism for agent sandbox disks (Abhishek Bhardwaj, RL and
agent infrastructure team — the infra behind ChatGPT and Codex Web sandbox execution).
Each sandbox's disk is a copy-on-write writable layer on top of a shared base image
(the Codex or ChatGPT base image). Copying costs nothing at snapshot time (no blocks
are touched); the cost is only paid when blocks are actually written afterward. On
`save()`, the system uses `FIEMAP` (a Linux ioctl that reports which extents/blocks of
a file have changed) to compute exactly the diff since the last snapshot, zips it, and
uploads it to cloud storage — never the whole disk. A deliberate concurrency trick: the
save call returns success immediately while the upload finishes in the background, so
the harness never blocks on cloud I/O. Snapshots chain into a **lineage**: a snapshot ID
resolves to the ordered sequence of diffs required to reconstruct it. Restoring means
downloading and applying that whole chain on top of the base image, then booting the
microVM — the restored sandbox has the exact block-level state it had when saved.

Four requirements are stated explicitly as the bar any such system must clear:
incremental (not full) snapshots, fast save, fast restore, and configurable scope
(entire root filesystem vs. specific folders like `/workspace`) — plus a deliberate
choice of block-level over file-level diffing specifically to avoid write amplification
on large files that change only slightly.

## Why It Matters

This is the concrete "how" behind giving an agent a disk that survives node failure,
long-running tasks, and branching exploration, without paying gigabytes of I/O at every
checkpoint. Three use cases are named directly:

1. **Fleet reliability** — periodic checkpoints let a sandbox be restored on a different
   node after node/cluster failure, or moved deliberately for cluster upgrades or A/B
   testing.
2. **Long-running tasks** — Codex's continuous-run ("YOLO") mode needs durable,
   resumable checkpoints; one practitioner's cited record was a 3-day continuous run.
3. **Monte-Carlo-style exploration** — checkpoint, attempt a path, restore the
   checkpoint and try a different path if it fails, repeat over many iterations —
   framed explicitly as the infrastructure precondition for multi-day autonomous
   research loops (drug discovery is the aspirational example given).

None of these are viable if snapshot/restore pays full-disk cost or meaningful latency
every time — the incremental, block-level, async-upload design is what makes the
"cheap enough to call constantly" property hold.

## Why People Are Using It

Production system at OpenAI, powering sandbox disks for ChatGPT and Codex Web at scale,
built by the team that also serves the RL training loop (throughput-optimized rollouts).
The talk frames storage as "the next unlock" after compute: once isolated code
execution is solved, durable state is the next constraint agent infrastructure hits
before an agent can function as "a true knowledge worker" rather than a stateless
executor.

## Potential Alternatives

- **Full-disk snapshot every time** — explicitly rejected in the source on cost and
  latency grounds at ChatGPT/Codex scale.
- **File-level diffing** instead of block-level — the source explicitly chose block
  level to avoid write amplification on large files that change only slightly.
- **Always-on / continuous persistence** (the companion NBD/tiered-cache finding) —
  presented as a complementary paradigm, not a competitor: explicit snapshots give
  point-in-time restore/branch semantics; always-on persistence guarantees no data loss
  without an explicit call.
- **git-based checkpointing** (this engine's own markdown+git substrate) — file-shaped,
  not block-shaped; cheaper to reason about but coarser-grained than block-level COW.

## Potential Improvements

No compaction or garbage-collection mechanism for aging snapshot lineages is discussed
in the source — worth flagging as an open question for anyone implementing this
pattern, since lineage chains only grow.

## Potential Failure Modes

- **Scope creep toward full snapshots** — the talk explicitly names configurable scope
  as a requirement precisely because defaulting to "snapshot the whole root FS" instead
  of scoping to the folders that actually change is a real design temptation.
- **Unbounded lineage growth** — no compaction/GC of old diff layers is described; a
  long-lived sandbox could accumulate an ever-longer chain, so every restore pays for
  downloading and applying the full history.
- **Durability window from the async-upload trick** — the "lie and return immediately"
  optimization means there is a window where a snapshot ID exists but its data has not
  actually finished persisting to cloud storage; a node failure inside that window can
  leave a snapshot ID pointing at incomplete data.
- **FIEMAP dependency** — block-level extent-diffing requires the underlying filesystem
  to expose changed-extent tracking; this is not a universal capability across all
  storage backends or operating systems.
