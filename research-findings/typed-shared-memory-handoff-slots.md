---
name: "Typed Shared-Memory Handoff Slots for Coordinator-Subagent Exchange"
summary: |-
  When a coordinator relays sub-agent results in prose, ticket IDs, assignees, and row-level detail
  get paraphrased and silently corrupted — this pattern removes the coordinator from the data path
  entirely. Agents exchange state through a small set of typed shared-memory slots (plan, findings,
  disambiguation, handoff_payload, goal), each with a declared write mode (replace vs append) and
  TTL scope; the retrieval agent posts exact rows into `findings` and the writer reads them verbatim.
  Weak evidence: single-author zero-star demo — cite only if corroborated elsewhere.
implementation_notes: null
category: "Context Engineering"
evidence_strength: "Weak (theoretical)"
adoption_status: "Not Yet Started"
priority: "P3 (Monitor)"
applicability:
  - "General"
adopted_in: []
sources:
  - "tjslattery-memorydemo-five-memory-patterns.md"
related_findings:
  - file: "verbatim-storage-thesis-for-memory.md"
    rel: "extends"
  - file: "database-as-shared-memory-coordination.md"
    rel: "same-problem"
  - file: "agent-teams-shared-communication-channel.md"
    rel: "same-problem"
proposals: null
date_discovered: "2026-07-11"
last_updated: "2026-07-11"
---

## What It Is

A multi-agent handoff pattern where coordinator and sub-agents communicate through a shared memory
store partitioned into typed slots, each with a fixed contract:

| Slot | Write mode | Writer → Reader | Content |
|------|-----------|-----------------|---------|
| `plan` | replace | Coordinator → sub-agents | Multi-step instructions for the current task |
| `findings` | append | Retrieval agent → Writer agent | Exact rows retrieved from memory stores |
| `disambiguation` | replace | Retrieval agent → Coordinator | Candidate list when a reference is ambiguous |
| `handoff_payload` | replace | Writer agent → Coordinator | Summary of actions taken |
| `goal` | replace, project-scoped, no TTL | Any → any | Cross-session continuity anchor |

Session-scoped slots carry a short TTL (1h in the demo); project-scoped slots persist. The design
intent, per the source: "Retrieval posts the exact rows it found into `findings`, the Writer reads
them verbatim, and the Coordinator stops having to re-state ticket IDs and assignees in prose
between sub-agent calls."

## Why It Matters

The default coordinator topology routes all sub-agent output through the coordinator's context,
where it gets summarized before the next dispatch — every hop is a lossy paraphrase. Typed slots
make the coordinator a control-plane-only participant: it routes *which* slot to read, not the
data itself. The slot typing also gives each channel a single semantics (append for accumulating
evidence, replace for current-state), which is what prevents the shared store from degrading into
an untyped scratchpad. This is the inter-agent analog of the verbatim-storage thesis: preserve
exact content, let structure do the routing.

## Why People Are Using It

Observed in TJSlattery/MemoryDemo, a LangGraph + MongoDB Atlas + Chainlit PM-assistant demo
(Coordinator on Sonnet, Retrieval/Writer specialists on Haiku, all memory ops funneled through a
MemoryManager singleton with a pub/sub event trace). Single-author, zero-star, no-license personal
demo — a working illustration, not production evidence. Treat as a design sketch until the slot
pattern is corroborated by an independent implementation.

## Potential Improvements

- Schema-validate each slot (the demo relies on convention, not enforcement)
- File-based equivalent for Claude Code topologies: one file per slot with append-only vs
  overwrite discipline, which maps onto the engine's existing file-mediated handoff protocol
- Slot-level provenance (which agent wrote, when) for audit

## Potential Failure Modes

- Append-mode slots grow unbounded within a session without compaction
- Replace-mode races if two sub-agents write the same slot concurrently
- Slot taxonomy proliferation — each new slot type is coordination surface that every agent
  prompt must document
- Uncorroborated pattern: the single source may reflect one author's taste, not a converging
  practice
