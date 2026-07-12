---
name: 'Hub-and-Spoke Two-Tier Skill Taxonomy with the ≥8-Sibling Hub Threshold'
summary: 'Because a harness reads every installed skill''s description on every turn, the always-on index cost is N × description length while skill bodies are free (loaded on demand). the context-hub system''s answer: consolidate any family of ≥8 related skills into one HUB skill whose body is a routing table, with the depth pushed into references/ SPOKES that are never indexed individually. A family of 8–30 topics then costs exactly one description in the always-on index instead of 8–30, and depth stays unbounded.'
implementation_notes: 'Direct input to the engine''s Rule-11 asset-catalog form question (directory convention vs frontmatter-indexed registry vs generated view). The taxonomy''s core claim is orthogonal to physical form: whatever the catalog looks like, the always-on discovery surface must be a small set of routers, with detail reachable only after routing — discoverability is the scarce resource, not storage. The engine''s own skill roster (30+ skills across workspace and IL scopes, each paying an always-on description) is approaching the regime this pattern exists for; the ≥8-sibling threshold gives a concrete, countable trigger for when to consolidate (e.g. the 13 Researcher skills are past it). Below the threshold, the pattern explicitly says do NOT hub — a hub for 3 spokes adds an indirection hop without meaningfully shrinking the index, which matches the engine''s abstractions-earn-their-keep rule.'
category: Context Engineering
evidence_strength: Medium (practitioner-documented, production system at a large enterprise (repo private, author-shared writeup))
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- General
adopted_in: []
sources:
- hub-and-spoke-context-hub.md
proposals: null
date_discovered: '2026-07-12'
last_updated: '2026-07-12'
related_findings:
- file: skill-description-budget-context-overflow.md
  rel: same-problem
- file: intent-based-meta-routing-skill.md
  rel: same-problem
- file: trigger-skip-grammar-peer-deferral-graph.md
  rel: extended-by
- file: skill-as-directory-progressive-disclosure-three-levels.md
  rel: extends
- file: always-on-context-minimalism-pointer-only-entry.md
  rel: same-problem
pipeline_status: raw
consumed_by: []
tags:
- skill-taxonomy
- hub-and-spoke
- context-economy
- skill-index
---

# Hub-and-Spoke Two-Tier Skill Taxonomy with the ≥8-Sibling Hub Threshold

## What It Is

A two-tier organization for a large skill library, built on one harness fact: at session
start the harness reads only the frontmatter `description` of every installed skill and
uses those descriptions to decide what to load. Bodies load on demand. So:

- **The description is the router.** Vague, broad, or colliding descriptions misroute.
- **Descriptions cost context on every turn.** N skills × description length is paid on
  every request, used or not. A growing flat skill list silently inflates the base cost
  of every interaction.
- **Bodies are effectively free.** Detail is cheap; *discoverability* is the scarce
  resource.

The taxonomy's response is two tiers:

- **Hub** — one top-level skill per domain family (e.g. `db-platform-expert`,
  `deep-optimizer`). Its description is a domain router (broad `TRIGGER:` surface plus
  `SKIP: → sibling-hub` handoffs); its body is mostly a routing table.
- **Spoke** — a deep reference at `<hub>/references/<spoke>.md`. Spokes carry the real
  depth and are **never indexed individually**; the agent reaches one only after the hub
  fires and the hub's routing table points at it.

## Why It Matters

Plain English: this is how you keep hundreds of skills' worth of knowledge available
without paying for hundreds of always-on descriptions and without trigger collisions.
Every skill-rich agent system hits this wall — the engine included. The pattern converts
an unbounded per-turn tax (one description per topic) into a bounded one (one description
per *family*), and it does so with a countable rule for when to apply it rather than
taste.

It also names the failure on both sides: too many top-level skills → index bloat and
mushy routing; hubbing too early → pointless indirection. The threshold is the guard
against both.

## How It Works

- **The ≥8-sibling threshold.** A family is consolidated into a hub when it has, or is
  expected to reach, ≥8 sibling skills. Below that, skills stay standalone top-level
  entries — a hub over 3 spokes adds an indirection hop without meaningfully shrinking
  the index. This is the core rule of the strategy's `HUB-STRATEGY.md`.
- **Index arithmetic.** A family of ~8–30 related topics costs one description in the
  always-on index instead of 8–30. The hub absorbs the trigger surface; the spokes absorb
  the detail.
- **Adding a topic to an existing domain** (worked example: a database-encryption
  topic) writes a spoke under the matching hub, broadens the hub's `TRIGGER:`, and
  bumps the hub version — index cost added: zero.
- **Spawning a hub** happens when a new family is expected to clear the threshold (worked
  example: "vector databases" mapped to ~12 gaps → first build spawns the hub, the rest
  land as spokes).
- **Meta-tools are excluded.** The taxonomy tooling itself (`skill-tree-architect`,
  `concept-family-explorer`) sits on an exclude list so the hubbing machinery never tries
  to hub its own operators.

## How It Could Fail

- **Over-stuffed hubs.** A hub that grows to 30+ spokes gets a mushy routing table; the
  strategy handles this with a whole-tree audit that flags split candidates (see the
  skill-tree-architect finding).
- **Hidden spokes.** Because spokes are unindexed, a spoke under the wrong hub is
  unreachable — cross-hub placement is a first-class audit category, not a cosmetic one.
- **Premature hubbing.** Consolidating 3–4 skills buys almost no index savings and costs
  a routing hop on every use.
