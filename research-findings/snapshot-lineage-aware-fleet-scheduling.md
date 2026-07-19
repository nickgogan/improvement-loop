---
name: "Snapshot-Lineage-Aware Fleet Scheduling"
summary: |-
  A fleet-scheduling policy that uses disk-snapshot lineage metadata as a data-locality
  signal, from the same OpenAI sandbox-cloud talk. Since a saved snapshot resolves to a
  lineage — an ordered chain of layered diffs — the cluster scheduler can score
  candidate nodes by how many of the needed lineage layers each already holds locally,
  and route the restore to whichever node needs to pull the least additional data.
  Worked example given: of three candidate nodes, the one holding the complete lineage
  chain locally wins the routing decision. Paired with two other named low-latency
  techniques — pre-warmed sandbox pools and just-in-time restore from a microVM memory
  snapshot (RAM state, distinct from the disk-lineage mechanism) — as the orchestration
  layer's answer to fast sandbox creation at fleet scale.
implementation_notes: null
category: "Orchestration"
evidence_strength: "Strong (production-tested)"
adoption_status: "Not Yet Started"
priority: "P3 (Monitor)"
applicability:
  - "General"
adopted_in: []
sources:
  - "from-fork-to-fleet-agent-sandbox-cloud.md"
related_findings:
  - file: "incremental-snapshotting-copy-on-write-block-diffing.md"
    rel: "enabled-by"
  - file: "three-tier-sandbox-provisioner.md"
    rel: "same-problem"
proposals: null
date_discovered: "2026-07-18"
last_updated: "2026-07-18"
pipeline_status: "synthesized"
consumed_by:
  - "session-persistence-and-memory.md"
tags:
  - "orchestration"
  - "sandboxing"
  - "infrastructure"
---

## What It Is

A scheduling policy for sandbox-cloud fleets that turns snapshot lineage into a
routing signal. Setup: a top-level control plane picks a cluster (by region/load), and
a cluster-level scheduler picks a node within it — a conventional orchestrator shape.
Three techniques are named for fast sandbox creation at that layer: (1) pre-warmed
sandbox pools, ready instantly at the cost of idle CPU/memory; (2) just-in-time restore
from a **memory snapshot** of the guest (a microVM's RAM state itself can be
snapshotted and restored in milliseconds — distinct from the disk-lineage mechanism
below); (3) a hybrid, where a warm pool grows via memory-snapshot restores. The
scheduling-specific pattern: because a *disk* snapshot resolves to a lineage of layered
diffs (per the companion incremental-snapshotting finding), the scheduler can score
each candidate node by how many of the needed lineage layers it already has cached
locally, and route the restore request to the node requiring the least additional data
transfer. Worked example from the talk: given three candidate nodes, the one already
holding the complete lineage chain locally scores highest and wins the routing
decision, ahead of nodes that would need to pull more layers over the network.

## Why It Matters

Without this, lineage tracking is purely a correctness property — you can always
reconstruct any snapshot, but every restore pays full transfer cost regardless of which
node it lands on. Feeding the same lineage metadata into the scheduler turns it into a
locality/affinity signal, the same way content-addressed build caches or container
registry layer caches route work toward runners that already hold the relevant layers.
It is a concrete example of the persistence layer and the orchestration layer sharing
metadata by design, rather than being built independently and reconciled later.

## Why People Are Using It

Same OpenAI production talk — presented as part of "how to run across many nodes" at
ChatGPT/Codex Web scale, alongside the pre-warm-pool and memory-snapshot latency
techniques it's paired with.

## Potential Alternatives

- **Load-only scheduling** (ignore data locality, route purely by CPU/memory/queue
  depth) — simpler, but every restore pays full lineage-chain transfer cost regardless
  of node history.
- **Sticky sessions** (always return a sandbox to the node it last ran on) — cheaper to
  implement, but fragile to node failure/eviction and doesn't generalize across a
  fleet.
- **Full pre-replication** of all lineage chains to all nodes — eliminates transfer
  cost but defeats the point of incremental, diffed storage in the first place.

## Potential Improvements

A generalized "layer-aware scheduler" could unify this with ordinary container/OCI
registry layer-cache-aware scheduling — an analogous problem container orchestrators
already solve — rather than building bespoke microVM-lineage routing logic from
scratch.

## Potential Failure Modes

- **Only pays off at real fleet scale** — with few nodes or shallow lineage chains, the
  scoring overhead isn't worth it; this is exactly why it applies only speculatively to
  a single-operator system with no fleet to schedule across.
- **Locality can fight load-balancing** — the node with the most cached layers may also
  be the most loaded node; the source does not describe how the scheduler reconciles
  the two competing signals.
- **Staleness** — a node can evict cached layers under memory pressure, making a
  locality-based routing decision wrong by the time the sandbox actually starts.
