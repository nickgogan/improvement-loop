---
title: "Session Persistence as Crash-Resilient Recoverable State"
type: "extracted-artifact"
assigned_form: "pattern"
source_finding: "session-persistence-crash-resilient"
confidence: "HIGH"
tier: "auto"
reason_codes: []
co_occurrence: null
extraction_date: "2026-04-19"
identification_report: "2026-04-19-identification-report-3.md"
deployed: false
deployed_to: null
contract:
  preconditions: "An agent session runs long enough that crash-induced loss is non-trivial (>10 minutes of work). A persistence target (filesystem, git, database) is available with write access. Session state can be serialized to a structured format."
  invariants: "State is persisted after every significant event, not only on shutdown. The load/reconstruct/restore sequence is deterministic -- the same persisted state always produces the same recovered session. Persistence never blocks the primary work loop for more than a trivially bounded duration."
  governance: "Persistence format is versioned so that schema changes do not silently corrupt recovery. Recovery is tested periodically by simulating crash-and-restore. Persistence overhead is monitored and bounded."
  recovery: "If persisted state is corrupted or unreadable, fall back to the last known-good checkpoint. If the external world has changed since the checkpoint (e.g., files modified by another process), detect the drift and surface it to the user before resuming."
tags:
  - "extracted-artifact"
  - "pattern"
---

# Session Persistence as Crash-Resilient Recoverable State

**Source:** [[session-persistence-crash-resilient]]
**Form:** pattern
**Extraction date:** 2026-04-19

## Problem

Long-running agent sessions (30+ minutes) accumulate significant work state -- conversation history, intermediate results, decisions made, permissions granted. A crash, network failure, or unexpected termination loses all of this, forcing a complete restart. Manual checkpointing (e.g., writing a PROGRESS.md) captures narrative state but misses machine-readable session state needed for deterministic recovery.

## Forces

- **Persistence frequency vs. performance overhead:** Persisting after every event maximizes recoverability but adds I/O cost. Persisting too infrequently risks losing significant work between checkpoints.
- **State completeness vs. state size:** Capturing full session state (messages, token counts, permissions, config) enables exact recovery but produces large persistence artifacts that grow over time. Incremental/diff-based approaches reduce size but add complexity.
- **Deterministic recovery vs. world drift:** Reconstructing a session from persisted state assumes the external world has not changed. If files, APIs, or databases were modified between crash and recovery, the restored session may operate on stale assumptions.
- **Structured state vs. narrative state:** JSON checkpoints capture machine-readable state; changelogs and progress files capture human-readable narrative. Both are needed for full resilience, but maintaining both doubles the persistence surface.

## Solution

Implement a three-phase persistence and recovery protocol:

1. **Persist after every significant event.** Define "significant" for your domain -- after each tool call, after each agent response, after each permission grant, after each commit. Serialize full session state to a structured format (JSON is the common choice): session ID, message history, token usage (input/output), permissions, configuration, and any domain-specific state.

2. **Use the load/reconstruct/restore API pattern.** Recovery follows three deterministic steps:
   - **Load:** Read the most recent persisted state from the persistence target
   - **Reconstruct:** Parse the serialized state back into session objects
   - **Restore:** Resume execution from the reconstructed state, re-establishing any transient connections or permissions

3. **Layer structured and narrative persistence.** Structured state (JSON checkpoints) provides machine-readable recovery. Narrative state (CHANGELOG.md, PROGRESS.md, git commit messages) provides human-readable context. Git commits after every meaningful work unit serve as both a persistence mechanism and a recoverable history.

Implementation details from production systems:
- gstack's Session Intelligence Layer provides `/checkpoint` (save state), `/health` (diagnostics), and context recovery commands
- PID-based lockfiles with stale recovery prevent concurrent session corruption
- `GIT_TERMINAL_PROMPT=0` prevents credential hangs during background persistence operations
- Anthropic's scientific computing workflow uses git-commit-after-every-work-unit as the persistence mechanism for multi-day autonomous sessions, combined with CHANGELOG.md as a narrative lab notebook

## Consequences

**Positive:**
- Crashes, network failures, and unexpected terminations no longer lose accumulated work
- Recovery is deterministic -- the same checkpoint always produces the same restored session
- Git-based persistence provides both recovery and audit trail for free
- Dual-layer persistence (structured + narrative) serves both machines and humans
- Scales to multi-day autonomous sessions, as demonstrated by Anthropic's scientific computing workflows

**Negative:**
- Persistence overhead adds I/O cost to every significant event -- must be bounded to avoid blocking the work loop
- JSON state grows linearly with session length for full-state persistence; long sessions produce large artifacts
- World-drift risk: restoring from a checkpoint after the external environment has changed can produce subtle bugs
- Maintaining two persistence layers (structured + narrative) doubles the surface area for bugs and drift
- Schema versioning for the persistence format adds maintenance overhead

## Known Uses

- Anthropic's production Claude Code -- session state persisted as JSON with load/reconstruct/restore recovery
- gstack v0.15.12.0+ Session Intelligence Layer -- `/checkpoint`, `/health`, context recovery, team-mode auto-update with PID lockfiles
- Anthropic's long-running Claude for scientific computing -- git commits after every meaningful work unit as persistence, running multi-day autonomous sessions on SLURM HPC clusters
- MetaSystem's PROGRESS.md -- manual narrative persistence mechanism (structured persistence would complement this)
- Nate B Jones framing session persistence as Tier 1 infrastructure for agent systems

## Contract

### Preconditions
An agent session runs long enough that crash-induced loss is non-trivial (typically >10 minutes of accumulated work). A persistence target (local filesystem, git repository, database) is available with write access throughout the session. Session state can be serialized to a structured format without loss of information needed for recovery.

### Invariants
State is persisted after every significant event, not only on clean shutdown. The load/reconstruct/restore sequence is deterministic -- the same persisted state always produces the same recovered session. Persistence operations never block the primary work loop for more than a trivially bounded duration. Persistence format includes a version identifier for forward compatibility.

### Governance
Persistence format is versioned so that schema changes do not silently corrupt recovery. Recovery is tested periodically by simulating crash-and-restore under realistic conditions. Persistence overhead (I/O latency, storage growth) is monitored and bounded. The definition of "significant event" is documented and adjustable per deployment context.

### Recovery
If persisted state is corrupted or unreadable, fall back to the last known-good checkpoint and log the corruption for diagnosis. If the external world has changed since the checkpoint (files modified, APIs updated, databases altered), detect the drift and surface it to the user before resuming automated execution. If persistence storage is full or unavailable, degrade gracefully to narrative-only persistence (PROGRESS.md / git commits) and alert the user that structured recovery is unavailable.
