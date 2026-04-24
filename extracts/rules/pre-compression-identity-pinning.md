---
title: "Pre-Compression Identity Pinning (Soul.md Survives Compaction)"
type: "extracted-artifact"
assigned_form: "rule"
source_finding: "pre-compression-identity-pinning"
extraction_date: "2026-04-19"
identification_report: "2026-04-19-identification-report-4.md"
deployed: false
deployed_to: null
context:
  applies_to:
    - "autonomous agents with defined identity files running long sessions where context compaction is possible"
    - "agent harness designs that implement or customize context compaction"
    - "safety-sensitive agent deployments where behavioral drift from identity loss is a concern"
  platform_coupling: "agnostic"
  autonomy: "autonomous-only"
  stage: "operate"
  reversibility: "medium — removing pinning requires modifying session initialization and compaction configuration; behavioral drift may be observed before the gap is caught"
  auditability: "medium — post-compaction context can be inspected to confirm identity file presence; requires tooling or harness-level assertion"
  evidence_strength: "Medium"
  adoption:
    status: "Not Yet Started"
    notes: "OpenClaw implements this as structural pinning with forced disk-read at session start; no equivalent mechanism deployed in this context as of extraction date."
contract:
  preconditions: "The agent has a designated identity file on disk. The execution environment supports explicit context ordering. A compaction routine exists or is possible."
  invariants: "Identity file is always the first element in the context window. Identity content is never altered by compaction. Pinning is re-applied after every compaction event."
  governance: "Owner: MetaSystem / Claude Build system. Changes to pinning mechanism require a DD. Human gate required before modifying pinning architecture."
  recovery: "If identity file missing post-compaction: halt agent immediately, reload from disk, reconstruct context, resume only after human review."
tags:
  - "extracted-artifact"
  - "rule"
---

# Pre-Compression Identity Pinning

**Source:** [[pre-compression-identity-pinning]]
**Form:** rule
**Extraction date:** 2026-04-19

## Condition

When any agent with a defined identity file operates in a session long enough to trigger context compaction, or when compaction is architecturally possible.

## Action

The agent's identity file MUST be:
1. Pinned at the top of the context window at session start via a forced disk-read.
2. Explicitly preserved (not subject to lossy summarization) during every compaction event.

No compaction routine may drop, summarize, or truncate the identity file's contents.

## Boundary

Enforced at two points: (1) session initialization — identity file is the first context element loaded; (2) compaction trigger — identity file is excluded from compaction scope and re-injected at the top.

## Enforcement

- Session startup sequence must include an explicit disk-read of the identity file before any other context.
- Compaction implementation must have an explicit exclusion list; the identity file must appear on it.
- Post-compaction context must be inspected to confirm identity file is present and unmodified.
- Anti-pattern flag: Using built-in compaction without a custom pinning layer is non-compliant for agents where behavioral drift is a safety concern.
- Cost note: Upfront disk-read incurs 4-10K tokens per session. This cost is accepted as the price of identity stability.

## Rationale

Context compaction is inherently lossy. Without explicit pinning, core identity, behavioral boundaries, and governance rules can be silently dropped during long sessions. For autonomous agents, silent behavioral drift from identity loss can produce safety violations with no observable signal.

## Contract

### Preconditions
The agent has a designated identity file on disk. The execution environment supports explicit context ordering. A compaction routine exists or is possible.

### Invariants
Identity file is always the first element in the context window. Identity content is never altered by compaction. Pinning is re-applied after every compaction event.

### Governance
Owner: MetaSystem / Claude Build system. Changes to pinning mechanism require a DD. Human gate required before modifying pinning architecture.

### Recovery
If identity file missing post-compaction: halt agent immediately, reload from disk, reconstruct context, resume only after human review.
