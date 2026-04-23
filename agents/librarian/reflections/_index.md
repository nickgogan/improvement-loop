---
title: "Librarian Reflections"
type: "index"
target_system:
  - "improvement-loop"
tags:
  - "reflections"
  - "librarian"
  - "agent-private"
---

# Librarian Reflections

Agent-private reflections produced by the Librarian over time. Append-only. One file per reflection event.

## Privacy

Librarian reflections are **agent-private**. Only the Librarian and Nick read this folder; Owner reads during `/solicit-proposals` runs. Other agents do not read.

**Note on the read-only invariant:** The Librarian is otherwise strictly read-only on the KB. Reflections are agent-private self-knowledge, not KB content, so writes to this folder do not break the read-only-on-KB invariant. This is the sole write exception in the Librarian's boundaries.

## Files

Currently empty. First reflection lands in the first solicitation round or Librarian-initiated reflection.
