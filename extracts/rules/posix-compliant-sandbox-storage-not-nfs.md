---
title: "POSIX-Compliant Sandbox Storage, Not NFS"
type: "extracted-artifact"
assigned_form: "rule"
source_finding: "posix-tiered-cache-persistence-over-object-storage"
identification_report: "session-persistence-and-memory.harvest-queue.md::posix-tiered-cache-persistence-over-object-storage::rule::posix-compliant-sandbox-storage-not-nfs"
extraction_date: "2026-07-19"
last_change_session: 152
last_change_report: "session-persistence-and-memory.harvest-queue"
deployed: false
deployed_to: null
context:
  applies_to:
    - "anyone choosing the filesystem-mount mechanism for a sandboxed or isolated code-execution environment that a coding or agentic model will read and write inside"
    - "infrastructure builders backing an execution volume with durable cloud storage and deciding how to expose it to the guest environment"
    - "teams evaluating NFS as a convenient default for durable, shared, network-backed storage in an agent-facing environment"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "build"
  reversibility: "medium — swapping the underlying mount mechanism after a sandbox environment is live touches the storage layer and any code that depends on its filesystem semantics, not just a config value"
  auditability: "medium — POSIX compliance can be checked against a conformance test suite or by exercising known POSIX-only operations (file locking, atomic rename, permission semantics) against the mount; reliability degradation from a non-POSIX mount otherwise surfaces indirectly as elevated agent file-operation failure rates"
  evidence_strength: "Strong"
  adoption:
    status: "Not Yet Started"
    notes: "Production system at OpenAI, powering always-on sandbox disk persistence for ChatGPT and Codex Web at scale, with NFS evaluated and explicitly rejected in favor of a POSIX-compliant tiered-cache-over-object-storage design. No equivalent adoption signal outside that source at time of extraction; no live code-execution sandbox exists in this workspace to adopt it into today, so this is design-stage grounding for if/when one is built."
contract:
  preconditions: "A system exposes persistent, durable disk storage to a sandboxed or isolated code-execution environment (a microVM, container, or similar) in which a coding or agentic model reads and writes files. The storage is backed by, or intended to be backed by, some form of durable network-attached or cloud-object storage rather than purely local disk."
  invariants: "The mount exposed inside the sandbox behaves as a standard POSIX-compliant filesystem — supporting the file-locking, atomic-rename, and permission semantics that coding/agentic models are trained to expect from ordinary filesystem behavior. NFS (or any other non-POSIX-compliant or lower-performance network filesystem) is not used as the underlying mount mechanism for agent-facing sandbox storage."
  governance: "Owner: whoever designs or maintains the sandbox/execution-environment storage layer. The POSIX-compliance requirement should be stated explicitly as a design constraint, with the rationale (model reliability on standard filesystem behavior, not just raw performance) documented alongside it, before a storage-backing mechanism is chosen."
  recovery: "If NFS or another non-POSIX-compliant mount has already been selected for an agent-facing sandbox → treat elevated or unexplained file-operation failure/flakiness reports from agent sessions as a signal to re-evaluate the mount mechanism, not as an unrelated model-reliability problem. If POSIX compliance cannot be fully guaranteed on a chosen storage backend → document the specific deviations and their expected impact on agent file-operation reliability rather than presenting the mount as fully standard."
tags:
  - "extracted-artifact"
  - "rule"
  - "sandboxing"
  - "infrastructure"
  - "persistence"
---

# POSIX-Compliant Sandbox Storage, Not NFS

**Source:** [[posix-tiered-cache-persistence-over-object-storage]]
**Form:** rule
**Extraction date:** 2026-07-19

## Condition

A system exposes persistent, durable disk storage to a sandboxed or isolated code-execution environment (a microVM, container, or comparable isolation boundary) in which a coding or agentic model performs ordinary file operations — reads, writes, renames, locks.

## Action

**Required:** Back the sandbox's storage with a mechanism that presents standard POSIX-compliant filesystem semantics to the guest (e.g., a POSIX-compliant filesystem layered over durable object storage, exposed as a block device).

**Forbidden:** Using NFS, or any other network filesystem with weaker performance or non-standard POSIX semantics, as the underlying mount mechanism for storage the agent directly reads and writes.

## Boundary

Enforced at the point where the storage-backing mechanism for a sandboxed execution environment is chosen and implemented — the decision of what filesystem type and mount mechanism the guest sees. Not a runtime check on individual file operations; a design-time architectural constraint.

## Enforcement

- **Mechanism:** Select and implement a storage-backing approach (e.g., a POSIX filesystem over durable object storage exposed via a block-device interface) rather than reaching for NFS as the default "easy durable network storage" choice.
- **Check (observable):** Exercise standard POSIX operations against the mount — file locking, atomic rename, permission semantics — and confirm they behave per POSIX rather than degrading or requiring workarounds. Elevated, otherwise-unexplained file-operation failure rates in agent sessions are a signal to re-examine the mount mechanism.
- **Violation response:** An already-deployed NFS-backed (or other non-POSIX) sandbox mount is a design defect to correct, not a performance tradeoff to accept — the source evidence names both a performance cost and a reliability cost (models are trained overwhelmingly on standard POSIX behavior, so a non-standard mount degrades their reliability on routine operations).

## Rationale

The choice of storage-backing mechanism is not just a performance decision — it is a model-reliability decision. Coding and agentic models are pre-trained overwhelmingly on standard POSIX filesystem behavior; when the guest environment they operate inside deviates from that (as NFS does, being both less performant and not fully POSIX-compliant), the model's reliability on ordinary file operations degrades, independent of whatever raw I/O throughput the network filesystem delivers. NFS is a common convenient default for "durable, shared, network-backed storage," which makes it worth naming explicitly as the rejected option rather than leaving the requirement implicit as "use something durable."

## Failure Modes

- **NFS chosen for convenience.** NFS is a well-understood, widely available mechanism for network-backed durable storage, making it an easy default to reach for without evaluating its POSIX-compliance or performance cost against agent-facing requirements specifically.
- **Performance-only evaluation.** Evaluating a candidate storage mechanism purely on throughput/latency benchmarks and missing the POSIX-semantics dimension — a mount can be fast and still degrade agent reliability if it isn't POSIX-compliant.
- **Write-back durability window.** In a tiered-cache architecture (writes land in an in-cluster cache before being written back to durable object storage), a node failure inside the window before write-back completes can lose writes the sandbox believed were already durable. This is a property of the tiered-cache design choice, not of the POSIX-vs-NFS decision itself, but it applies to any implementation of this rule and should be accounted for.
- **Under-specified cache-tier sizing and eviction.** Tiered-cache architectures are the kind of "boring infrastructure" that is easy to under-invest in until it becomes load-bearing at scale; capacity and eviction policy are not automatically solved by choosing a POSIX-compliant design.

## Contract

### Preconditions
A system exposes persistent, durable disk storage to a sandboxed or isolated code-execution environment (a microVM, container, or similar) in which a coding or agentic model reads and writes files. The storage is backed by, or intended to be backed by, some form of durable network-attached or cloud-object storage rather than purely local disk.

### Invariants
The mount exposed inside the sandbox behaves as a standard POSIX-compliant filesystem — supporting the file-locking, atomic-rename, and permission semantics that coding/agentic models are trained to expect from ordinary filesystem behavior. NFS (or any other non-POSIX-compliant or lower-performance network filesystem) is not used as the underlying mount mechanism for agent-facing sandbox storage.

### Governance
Owner: whoever designs or maintains the sandbox/execution-environment storage layer. The POSIX-compliance requirement should be stated explicitly as a design constraint, with the rationale (model reliability on standard filesystem behavior, not just raw performance) documented alongside it, before a storage-backing mechanism is chosen.

### Recovery
If NFS or another non-POSIX-compliant mount has already been selected for an agent-facing sandbox → treat elevated or unexplained file-operation failure/flakiness reports from agent sessions as a signal to re-evaluate the mount mechanism, not as an unrelated model-reliability problem. If POSIX compliance cannot be fully guaranteed on a chosen storage backend → document the specific deviations and their expected impact on agent file-operation reliability rather than presenting the mount as fully standard.
