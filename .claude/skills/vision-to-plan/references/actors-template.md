# Actors: <system name>

<!-- PROCESS: Draft ONE section at a time with approval gates, after the PRD is
approved. Describe the actors as they ARE plus approved direction — no speculative
actors. Delete all ELICIT/PROCESS comments from the final artifact. Actor drafting
is mostly a diff against agents/ — elicit only deltas; do not re-interview settled
contracts. -->

Updated: <date> · Approved by: <human>

## Actor model (decide FIRST — determines this doc's whole shape)

<!-- ELICIT: Present as options with trade-offs. (a) ONE implicit agent — the kernel
is the full description of the single agent, session state scoped to the system;
(b) N named actors (engine: Owner/Researcher/Codifier/Librarian per DD-82/DD-86);
(c) one system-agent whose N dispositions are internal roles, not actors. Record the
choice and why; the sections below follow it. -->

## Actors & boundaries

<!-- ELICIT: Per actor (or per disposition, per the model above): its task boundary
(what it owns), its permission set (read/write scope — the strict boundaries), the
skills it owns, and its disposition/soul in one line. Mostly mechanical from
agents/*/agent.md — capture only deltas from the settled contracts. -->

## The human's seat

<!-- ELICIT: The human gate is an actor with a permission set too. Name what stays
human (the human/AI seam — what should NOT be delegated), which decisions require
the human, and where those map in the governance registry. -->

## Handoffs & control

<!-- ELICIT: How work moves between actors (file-mediated vs direct), what steers
each actor at cold start (load order), and the standing guards every actor obeys
(human gate at stage boundaries, no push, no volatile metrics). Pointers to the
handoff protocol, not a restatement. -->

## Decisions (append-only)

<!-- PROCESS: One line per durable actor-model decision: date, decision, why, what it
superseded. Never silently rewrite; supersede here. -->
