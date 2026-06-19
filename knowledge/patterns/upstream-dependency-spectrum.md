---
title: "Upstream Dependency Spectrum"
id: "upstream-dependency-spectrum"
type: "pattern"
category: "system-design"
target_system:
  - "improvement-loop"
stage: "active"
created: "2026-04-07"
updated: "2026-04-07"
author: "nick"
source_dd:
  - "DD-45"
  - "DD-46"
  - "DD-51"
  - "DD-54"
  - "DD-66"
tags:
  - "pattern"
  - "system-design"
  - "dependency-management"
  - "upstream-tracking"
  - "maintenance"
aliases:
  - "Cherry-pick vs Adopt"
  - "Dependency spectrum"
  - "Watched libraries"
---

# Upstream Dependency Spectrum

When external agentic tooling packages (GSD, gstack, BMAT, Mem Zero, Open Claude, etc.) offer capabilities relevant to MetaSystem, the question isn't "cherry-pick or adopt" — it's **where on the spectrum does each capability land?**

## The Problem

External packages each solve real problems and are maintained by communities with more people, more focus, and more testing than a two-person team can match. But none map 1:1 onto MetaSystem's governance model, fractal structure, or constitutional constraints. Adopting wholesale means accepting opinions that may conflict with existing DDs. Cherry-picking everything means maintaining patterns that upstream improves for free.

## The Spectrum

```
Full cherry-pick          Thin wrapper              Adopt wholesale
(extract pattern,         (use the package,         (use it as-is,
 rewrite for our          overlay our config         accept its opinions)
 context)                 and rules)
```

### Full Cherry-Pick (Left)

Extract the pattern, rewrite it for MetaSystem's context. You own it entirely.

- **Upstream changes**: don't help you, can't break you
- **Maintenance**: you carry it all
- **Good for**: things where your context is genuinely different from what the package assumes
- **Example**: memory architecture — MetaSystem's memory model is tied to the fractal pattern and governance layer. Nobody else has that.

### Thin Wrapper (Middle)

Use the package, overlay MetaSystem's governance and configuration. A translation layer maps their concepts to yours.

- **Upstream changes**: you update the wrapper, not the whole system
- **Maintenance**: bounded to the wrapper layer
- **Good for**: things where the package is 80%+ right and your additions are configuration, not redesign
- **Example**: build orchestration — GSD's execution model is good, MetaSystem's governance rules overlay it.

### Adopt Wholesale (Right)

Use it as a dependency. Accept its opinions. Upgrades are free.

- **Upstream changes**: automatic benefit, but breaking changes are all-or-nothing
- **Maintenance**: zero until something breaks
- **Good for**: things where the package's opinions are your opinions, or where you don't have a strong opinion
- **Example**: utility tools where the package is the standard.

## Default Position

**Default to the middle (thin wrapper)** unless there's a specific reason to go left or right.

Why:
- You get upstream upgrades with bounded blast radius
- Your governance layer (DDs, constitution, fractal pattern) stays yours — it wraps, it doesn't get replaced
- When something changes upstream, the research-loop flags it, and you decide if the wrapper needs updating
- If an upstream package dies or diverges, you can migrate the wrapper to a cherry-pick without rebuilding from scratch

## Decision Criteria

| Signal | Leans Left (Cherry-Pick) | Leans Right (Adopt) |
|--------|--------------------------|---------------------|
| Our governance constrains it differently | Yes | No |
| The package is opinionated about things we have DDs for | Yes | No |
| The package is battle-tested by many users | Leans right | Yes |
| We need to modify the core behavior, not just configure it | Yes | No |
| The package updates frequently with valuable improvements | Leans right | Yes |
| The capability is peripheral to our core systems | No | Yes |
| The capability touches constitutional constraints | Yes | No |

## Maintenance Math

Two people. The honest accounting:

- **Cherry-picked patterns**: stable once codified — patterns don't bit-rot the way code does. But they also don't improve unless you actively revisit them.
- **Thin wrappers**: you maintain the wrapper. When upstream changes, you update a mapping layer, not the whole system. Bounded blast radius.
- **Wholesale adoption**: zero maintenance until a breaking change, then it's all-or-nothing.

## Upstream Monitoring

The research-loop provides the monitoring mechanism — each scan can check what's changed in watched libraries. The **watched-libraries registry** (`systems/improvement-loop/watched-libraries/`) tracks:

- What each external project is and what we use from it
- Where it sits on the spectrum
- Which local patterns, skills, or configs derive from it
- Last evaluated version and what changed since

When an upstream change is detected, the triage question depends on spectrum position:

| Position | Triage Question |
|----------|----------------|
| Cherry-pick | "Does this invalidate our version of the pattern?" |
| Thin wrapper | "Does our wrapper need updating?" |
| Wholesale | "Is this a breaking change we need to absorb?" |

## Anti-Patterns

| Anti-Pattern | What Goes Wrong |
|-------------|-----------------|
| **Cherry-pick everything** | Two people can't maintain an entire parallel ecosystem. You miss improvements upstream ships for free. |
| **Adopt everything wholesale** | External opinions override your constitutional constraints. Breaking changes cascade unpredictably. |
| **No tracking** | You cherry-picked a pattern six months ago and forgot where it came from. Upstream shipped a critical fix you never saw. |
| **Clone repos into the vault** | Obsidian indexes their `.md` files (graph noise, search pollution). Git-in-git is painful. You don't need their code — you need to know what changed. |

## Related

- [[capability-type-selection]] — Once you decide *what* to bring in, this pattern decides *what form* it takes (agent, skill, workflow, hook, rule)
- Research-to-Codification Pipeline (guide) — How research findings become codified artifacts in the engine's `knowledge/` layer
