---
name: "CRDT-Ready State Management Pattern"
summary: "n8n's workflowDocument store uses a public/apply method split where all mutations go through private apply*() methods that write to refs and fire event hooks. Designed for future CRDT support: local actions, remote sync, and undo/redo all converge on the same apply methods. A forward-looking architectural pattern documented in a deeply nested CLAUDE.md."
implementation_notes: "Forward-looking pattern — CRDT is not yet implemented in n8n. Worth monitoring to see if this pattern emerges elsewhere as collaborative agent editing becomes more common."
category: "Agent Design"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
proposer_priority: null
applicability:
  - "General"
adopted_in: []
sources: []
related_findings: []
proposals: null
date_discovered: "2026-04-09"
last_updated: "2026-04-09"
pipeline_status: "raw"
consumed_by: []
---

## What It Is

n8n's `workflowDocument` store follows a specific state management architecture documented in a deeply nested `CLAUDE.md` (`packages/frontend/editor-ui/.../workflowDocument/CLAUDE.md`):

- All public methods (e.g., `addNode()`, `moveNode()`, `deleteConnection()`) are high-level operations
- All mutations go through private `apply*()` methods (e.g., `applyAddNode()`, `applyMoveNode()`)
- Apply methods write to reactive refs and fire event hooks
- This separation exists to support future CRDT integration: local actions, remote sync, and undo/redo all converge on the same apply layer

The pattern ensures that regardless of where a mutation originates — local user action, remote collaborator sync, or undo/redo replay — the state update follows the same code path. This is a prerequisite for conflict-free replicated data types (CRDTs), which require all state changes to be commutative and convergent.

**Note: This is a forward-looking pattern.** CRDT is not yet implemented in n8n. The architecture is designed to make future CRDT adoption possible without restructuring the state management layer.

## Why It Matters

As collaborative editing becomes more common in agent-adjacent tools (workflow builders, shared agent configurations, collaborative prompt editing), CRDT-readiness becomes an architectural advantage. Retrofitting a state management layer for CRDT after the fact is expensive — it typically requires restructuring all mutation paths to be commutative.

The deeper insight is about **mutation path convergence**: regardless of whether collaborative editing materializes, the pattern of routing all state changes through a single apply layer simplifies debugging (one place to add logging), enables undo/redo (replay apply operations), and makes testing easier (test the apply layer independently).

## Why People Are Using It

Observed in [n8n](https://github.com/n8n-io/n8n) v2.16.0 — see [[n8n-analysis]] for structural details. The pattern is documented in a deeply nested CLAUDE.md file, ensuring that AI agents working on the workflow editor understand the mutation architecture and don't bypass the apply layer.

## Potential Alternatives

Direct state mutation with a change log (simpler but harder to make CRDT-compatible later). Event sourcing (captures all changes but different architecture). Operational transformation (alternative to CRDT for collaborative editing).

## Potential Improvements

Implementing the actual CRDT layer. Extending the pattern to other stores in the application. Generating conflict resolution strategies from the apply method signatures.

## Potential Failure Modes

Premature architecture — the CRDT layer may never be needed, making the apply split unnecessary complexity. Developers bypassing the public API to call apply methods directly. The pattern only works if all mutations are genuinely commutative — some operations may have order-dependent semantics.
