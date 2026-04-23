---
title: "Owner Reflections"
type: "index"
target_system:
  - "improvement-loop"
tags:
  - "reflections"
  - "owner"
  - "agent-private"
---

# Owner Reflections

Agent-private reflections produced by the Owner over time. Append-only. One file per reflection event.

## Privacy

Owner reflections are **agent-private**. Only the Owner itself and Nick read this folder. Other agents (Researcher, Codifier, Librarian) do not read Owner reflections. This is enforced by convention, not permission — the filesystem permits all reads; the invariant is maintained by agent disposition.

## Trigger

Reflections fire in two ways:
- **Owner-solicited round:** `/solicit-proposals` run checks reflection freshness; prompts re-reflection if stale.
- **Agent-initiated:** Owner reflects when it notices something worth capturing (drift, ambiguity, friction).

## Cadence

Freshness threshold: reflection considered fresh if `updated` is within 21 days OR 3 Owner sessions, whichever is shorter. Re-reflect when thresholds breach or when focus areas of a new solicitation round differ materially from prior reflection.

## Files

Currently empty. First reflection lands in session 52 or later.
