---
name: "Agentic Repo-Maintenance Fleet with Typed Safe-Outputs"
summary: |-
  Plain English: a repo can run a fleet of scheduled maintenance agents (bug hunting,
  docs-drift detection, regression sweeps) safely by giving each agent read-only
  permissions and a typed, structurally-capped write path — e.g. "may create at most 1
  issue, which expires in 7 days" — so the worst a misbehaving agent can do is file one
  bounded artifact for human review. Pydantic AI runs 10 gh-aw agentic workflows
  (bug-hunter, docs-drift, regression-detector, three provider-conformance sweeps,
  ui-security-review, stale-issues-finder, pr-review) as isolated scheduled singletons;
  writes happen only through declared `safe-outputs` contracts (max counts, title
  prefixes, expiry), agents never push directly, and shared prompt fragments
  (adversarial-review, rigor) are composed via frontmatter `imports:`.
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
  - file: "headless-cron-composition-autonomous-scheduled-workflows.md"
    rel: "same-problem"
  - file: "advisory-only-for-persistent-mutations.md"
    rel: "same-problem"
  - file: "agent-action-reversibility-as-design-requirement.md"
    rel: "extends"
proposals: null
date_discovered: "2026-07-13"
last_updated: "2026-07-13"
pipeline_status: "raw"
consumed_by: []
tags:
  - "governance"
  - "orchestration"
  - "autonomous-maintenance"
---

# Agentic Repo-Maintenance Fleet with Typed Safe-Outputs

## What It Is

A production pattern for autonomous repository maintenance with structural (not
prose-based) write containment:

- **Fleet shape:** 10 scheduled, mutually independent agent workflows defined as
  markdown files with YAML frontmatter (GitHub's gh-aw format), compiled to locked
  workflow files. Each is an isolated singleton — no inter-agent communication.
- **Write containment:** agents get read-only GitHub permissions; the only write path
  is a declared `safe-outputs` contract typed per output kind — e.g.
  `create-issue: max 1, expires 7d`, title prefixes for attribution. Nothing an agent
  produces lands anywhere except as an issue/comment/PR for maintainer review.
- **Prompt composition:** shared fragments (adversarial-review posture, rigor rules,
  vendor domain lists) are imported by name into each workflow's prompt via `imports:`
  lists, so fleet-wide behavior rules are maintained once.

(`.github/workflows/*.md`, `shared/`, guarded further by `pr-guard.yml` and `bots.yml`)

## Why It Matters

The hard problem in autonomous maintenance is not capability but blast radius. This
fleet demonstrates the containment answer at production scale: cap the write surface in
the *infrastructure's type system* (max counts, expiry, output kinds) rather than in the
agent's instructions, so a prompt-injected or confused agent still cannot exceed one
expiring issue. It is the repo-maintenance instantiation of advisory-only mutations and
reversibility-proportional gating — every fleet output is trivially reversible and
human-gated by construction.

## Why People Are Using It

Operating on one of the most active Python repos; the workflows carry evidence of real
use (issue/PR traffic from the fleet, per-workflow schedules and caps tuned per job).
Source: Observed in [pydantic-ai](https://github.com/pydantic/pydantic-ai) v2.9.0 — see
[[pydantic-ai-analysis]] for structural details.

## Potential Alternatives

- **Single periodic "maintenance agent"** — less isolation; one prompt handles many
  jobs, so failures and permissions blur together.
- **Headless cron + skill composition** (KB precedent) — same scheduling shape,
  typically without typed output contracts; containment is prose.
- **Human-triggered audits** — no standing cost, but drift accumulates between runs.

## Potential Improvements

- Fleet-level observability: cross-workflow dashboards of what the agents filed vs what
  humans accepted (acceptance rate is the fleet's real quality metric).
- Output contracts beyond GitHub artifacts (typed writes to registries, docs).

## Potential Failure Modes

- **Noise fatigue** — ten agents filing bounded issues can still exceed maintainer
  review bandwidth; caps bound blast radius, not attention cost.
- **Expiry losses** — auto-expiring outputs silently drop true positives nobody
  triaged in time.
- **Shared-fragment coupling** — one bad edit to an imported prompt fragment shifts
  behavior across the whole fleet at once.
