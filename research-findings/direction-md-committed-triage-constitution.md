---
name: "direction.md — Committed Triage Constitution for a Scheduled Maintainer Agent"
summary: |-
  Plain English: to make an agent's judgment calls consistent and contestable, commit
  a short constitution stating what the project IS and IS NOT, and require every
  automated decision to cite a clause from it. Archon v0.5.0's maintainer-standup
  system splits the agent's grounding into two layers: shared committed direction
  (`.archon/maintainer-standup/direction.md` — the north-star doc that drives
  automated P1–P4 PR triage, where declines must cite a specific clause, e.g.
  "direction.md §single-tenant-per-install") and personal gitignored memory
  (`profile.md` per-maintainer config, `state.json`, and rolling `briefs/` with the
  last 3 read back into the next run). Judgment criteria are versioned, reviewable,
  and shared across operators; working memory stays private and per-operator.
implementation_notes: null
category: "Governance"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: "P3 (Monitor)"
applicability:
  - "General"
adopted_in: []
sources: []
related_findings:
  - file: "soul-md-agent-constitution-pattern.md"
    rel: "same-problem"
  - file: "time-boxed-automated-pr-compliance.md"
    rel: "same-problem"
  - file: "north-star-drift-loop-trajectory-extrapolation.md"
    rel: "same-problem"
  - file: "review-triage-admissible-scope-authority.md"
    rel: "same-problem"
proposals: null
date_discovered: "2026-07-13"
last_updated: "2026-07-13"
pipeline_status: "raw"
consumed_by: []
tags:
  - "governance"
  - "agent-constitution"
  - "triage"
  - "archon"
---

# direction.md — Committed Triage Constitution for a Scheduled Maintainer Agent

## What It Is

Archon's daily maintainer-standup workflow grounds an automated triage agent in a two-layer memory/judgment architecture under `.archon/maintainer-standup/`:

1. **Shared, committed direction** — `direction.md`, a north-star document stating what Archon IS and IS NOT. The standup workflow uses it to classify open PRs into P1–P4 priority bands, and any recommendation to decline a PR **must cite a specific clause** (e.g. "cite `direction.md §single-tenant-per-install`"). The constitution is versioned in git: changing the project's direction is a reviewable diff, not a prompt tweak.
2. **Personal, gitignored memory** — `profile.md` (per-maintainer preferences/config), `state.json` (run-to-run state), and `briefs/YYYY-MM-DD.md` (daily outputs; the last 3 are read back into the next run as rolling context).

The split makes the *judgment criteria* shared and auditable while the *working memory* stays per-operator and private.

## Why It Matters

Agents making repeated judgment calls (triage, review, prioritization) drift unless their criteria live somewhere durable — and drift differently per operator unless the criteria are shared. The clause-citation requirement is the load-bearing detail: it converts fuzzy "the agent decided" into "the agent applied §X", which is checkable by a human, contestable in review, and diagnosable when wrong (bad clause vs bad application). This is citation-grounded governance for agent decisions — the same move as requiring citations in research synthesis, applied to judgment. The committed/gitignored split cleanly answers "what belongs in the repo vs what belongs to the operator" for scheduled personal agents.

## Why People Are Using It

Observed in [Archon](https://github.com/coleam00/archon) v0.5.0 — see [[archon-analysis]] for structural details. The maintainer standup is a shipped scheduled workflow used to manage Archon's own PR queue; direction.md drives its automated prioritization and its decline recommendations.

## Potential Alternatives

Constitution embedded in the agent's system prompt (invisible to reviewers, unversioned per-decision). Label-based mechanical rules only (opencode's time-boxed PR compliance — deterministic, but can't express directional judgment). Human triage (doesn't scale with contribution volume).

## Potential Improvements

Clause identifiers as stable anchors (numbered sections) so citations survive editing. A feedback loop from contested declines back into constitution amendments. Extending clause citation from declines to accepts (why was this P1?).

## Potential Failure Modes

Constitution rot: direction.md falls behind the maintainers' actual direction and the agent enforces yesterday's strategy with full confidence. Citation theater: the model cites a plausible clause post-hoc rather than reasoning from it. Rolling 3-brief memory can entrench a wrong prior across days.
