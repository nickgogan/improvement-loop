---
name: 'TRIGGER:/SKIP: Description Grammar and the Peer-Deferral Graph'
summary: 'A three-part grammar for skill descriptions — capability statement, TRIGGER: (positive phrasings that should fire the skill), SKIP: (near-miss cases explicitly handed to a named sibling) — turns each description into a tested routing contract. The SKIP edges are hard routing-time deferrals; softer related_skills frontmatter and inline cold-spoke pointers form a second layer of navigation edges. Together the skills form a directed deferral graph, and a repair script (referents.mjs --repair) rewrites dangling edges whenever a skill is created, folded, or moved — so every skill knows what it is NOT and hands those cases off explicitly.'
implementation_notes: 'Directly adoptable authoring discipline for engine skills, and an audit criterion candidate for /assess-skill: engine skill descriptions today state what a skill does and roughly when, but almost none carry explicit negative-space handoffs ("this looks close but belongs to /X"), which is exactly what prevents collisions as the roster grows — e.g. /assess-skill vs /prompt-evaluator vs /assess-prompt, or /design-skill vs the imported /meta-skill-author, are collision surfaces today with no SKIP edges. The two-layer edge model (hard routing edges vs soft navigation edges) plus automated edge repair after moves also speaks to the asset-catalog form question: whatever form the catalog takes, cross-references between assets need typed edges and a mechanized repair path, not prose — the engine already has the KB-level analog in /finding-crosslink''s four typed relations and /linkage-repair.'
category: Agent Design
evidence_strength: Medium (practitioner-documented, production system at a large enterprise (repo private, author-shared writeup))
adoption_status: Not Yet Started
priority: P1 (Direct Adoption)
applicability:
- General
adopted_in: []
sources:
- hub-and-spoke-context-hub.md
proposals: null
date_discovered: '2026-07-12'
last_updated: '2026-07-12'
related_findings:
- file: hub-and-spoke-two-tier-skill-taxonomy.md
  rel: extends
- file: skill-md-frontmatter-as-discovery-trigger-primitive.md
  rel: extends
- file: skill-description-budget-context-overflow.md
  rel: same-problem
- file: two-path-skill-authoring-with-hard-promotion-gates.md
  rel: same-problem
pipeline_status: raw
consumed_by: []
tags:
- skill-descriptions
- routing
- peer-deferral
- collision-prevention
---

# TRIGGER:/SKIP: Description Grammar and the Peer-Deferral Graph

## What It Is

A fixed grammar for the skill `description` field — the only text the harness reads when
deciding which skill to load:

```
description: >-
  <one-line capability statement>.
  TRIGGER: <comma-separated positive phrasings that SHOULD fire this skill>.
  SKIP: <negative case> → <sibling-id>; <other case> → <other-sibling-id>.
```

- **Capability statement** — what the skill *is*, not a workflow summary.
- **`TRIGGER:`** — the positive surface, empirically tested (the optimizer's
  trigger-accuracy eval targets ≥9/10 on positive phrasings).
- **`SKIP:`** — the peer-deferral mechanism. Each `→ <id>` is a routing edge saying "this
  looks close but belongs to that sibling." This is what keeps two adjacent skills from
  both firing (a collision).

Beyond the description, skills carry softer edges: `related_skills:` in frontmatter and
inline `→ <spoke-id>` "cold-spoke pointers" in bodies, used for cross-pollination and
navigation rather than routing.

## Why It Matters

Plain English: as a skill library grows, the failure mode isn't missing knowledge — it's
two skills that both look right for the same prompt, or a skill that quietly stops firing
because a neighbor absorbed its surface. This grammar makes the negative space explicit
and machine-actionable: every skill declares what it is **not** and names who owns those
cases. Routing quality then becomes something you can test and repair instead of
something you feel.

The engine's skill roster already has adjacent pairs with no declared boundary; this is
the cheapest known discipline for keeping a growing roster crisp.

## How It Works

- **Two edge classes.** `SKIP: … → <id>` is a *hard* deferral the harness can act on at
  routing time; `related_skills:` and cold-spoke pointers are *soft* edges for navigation.
  The distinction matters because hard edges must stay inside the always-on description
  budget while soft edges live in bodies (free).
- **Edges are maintained, not trusted.** When a spoke is created, folded into a hub, or
  moved, edges dangle (point at a name that moved). `referents.mjs --repair` rewrites
  every `→ <spoke-id>` and `related_skills:` entry to the hub-aware form after any
  routing change — repair is a scripted post-condition of every reshape, not a periodic
  cleanup.
- **The grammar is tested, not just linted.** Pass H (trigger-accuracy eval, ~60 headless
  probes per skill, ≥9/10 positive and ≤1/10 false-positive) verifies `TRIGGER:`; Pass I
  (collision check) probes the skill against existing siblings and, on collision, the fix
  is to tighten `SKIP:` or fold the skill into a hub rather than ship a colliding
  top-level entry.
- **Budget interaction.** Descriptions are capped (1000 soft / 1536 hard chars) because a
  harness-truncated description loses its *tail* — and `SKIP:` clauses sit at the tail,
  so truncation silently destroys collision protection first. That is why the hard cap is
  a High-severity finding, not a style nit.

## How It Could Fail

- **Stale edges without the repair script.** Adopting the grammar without mechanized edge
  repair yields a graph that rots on every rename — worse than no edges, because agents
  follow them.
- **SKIP bloat.** Enumerating too many negative cases pushes the description over the cap
  and gets the whole tail truncated; SKIP should carry only the *near-miss* cases that
  actually collide.
- **Grammar without eval.** The structure invites confidence; only the trigger/collision
  probes verify it routes as written.
