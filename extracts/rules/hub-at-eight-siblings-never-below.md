---
title: "Hub Skills at Eight-or-More Siblings, Never Below"
type: "extracted-artifact"
assigned_form: "rule"
source_finding: "hub-and-spoke-two-tier-skill-taxonomy"
extraction_date: "2026-07-19"
last_change_session: 152
last_change_report: "structuring-agent-context.harvest-queue"
identification_report: "structuring-agent-context.harvest-queue.md::hub-and-spoke-two-tier-skill-taxonomy::rule::hub-at-eight-siblings-never-below"
deployed: false
deployed_to: null
context:
  applies_to:
    - "skill, command, or capability libraries growing past a handful of standalone entries in an always-on index"
    - "agent harnesses that read every available entry's description on each turn, before any entry is invoked"
    - "documentation or capability catalogs organized as a flat list that is starting to feel unwieldy as it grows"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "build"
  reversibility: "low — consolidating a family into a hub is a structural reorganization (new routing entry, detail moved behind it); splitting a hub back into standalone entries requires re-establishing each entry's independent discoverability"
  auditability: "high — sibling count per family is a simple, countable check against the current index; whether a family is hubbed is a binary, inspectable fact"
  evidence_strength: "Medium"
  adoption:
    status: "Not Yet Started"
    notes: "Practitioner-documented at a large enterprise (repo private, author-shared writeup). No broader adoption signal reported at time of extraction."
contract:
  preconditions: "A library of related skills, commands, or capability entries exists, each carrying its own always-on description that the host reads on every turn regardless of use. The boundary of a 'family' (which entries belong together) is defined or definable."
  invariants: "Any family of related entries with 8 or more siblings — existing today, or clearly forecast to reach that count — is consolidated into one hub entry whose description is a routing surface and whose body is a routing table; the family's depth moves into detail files that are never indexed individually and are reached only after the hub fires. Families with fewer than 8 siblings remain standalone top-level entries and are never consolidated into a hub."
  governance: "Owner: whoever curates the skill/capability index (library maintainer, workspace steward). The threshold check applies at the moment a new family is proposed and whenever an existing family gains a member. Periodic index audits re-check sibling counts as the library grows, since a family can cross the threshold gradually."
  recovery: "If a family reaches 8+ siblings without being hubbed: the index is silently paying one description per sibling instead of one per family — consolidate at the next audit. If a hub was created for a family below the threshold: split it back into standalone entries; the indirection hop is unjustified index overhead. If a hub grows far past the threshold (documented risk: 30+ spokes) and its routing table becomes hard to navigate: split the hub — this rule governs the create-vs-standalone decision, not the upper bound, but an audit that surfaces split candidates is the adjacent remedy."
tags:
  - "extracted-artifact"
  - "rule"
  - "skill-taxonomy"
  - "context-engineering"
  - "hub-and-spoke"
---

# Hub Skills at Eight-or-More Siblings, Never Below

**Source:** [[hub-and-spoke-two-tier-skill-taxonomy]]
**Form:** rule
**Extraction date:** 2026-07-19

## Condition

A family of related skills, commands, or indexed capability entries has reached — or is clearly forecast to reach — 8 or more siblings, inside a host that reads every entry's description on every turn as part of deciding what to load.

## Action

**Required:** Consolidate the family into a single hub entry. The hub's description becomes the routing surface (a broad trigger plus handoffs to sibling hubs); its body becomes a routing table. The family's actual depth moves into reference/detail files that are never indexed individually — they are reachable only after the hub fires and its routing table points to them.

**Forbidden:** Creating a hub for a family with fewer than 8 siblings — the indirection hop costs a lookup without meaningfully shrinking the index. Leaving a family at 8 or more siblings unconsolidated — this pays an unbounded per-turn description tax (N descriptions instead of one) for no benefit over the hub form.

## Boundary

Enforced at two points: (1) skill/capability-library authoring time, when a new entry is proposed for an existing or new family; (2) periodic index audits, since a family can cross the threshold gradually as entries accumulate one at a time without anyone re-evaluating the family as a whole.

## Enforcement

- **Mechanism:** Count current (or clearly forecast) siblings per family.
- **Check (deterministic):** `IF sibling_count(family) >= 8 THEN family MUST be hubbed`. `IF family IS hubbed AND sibling_count(family) < 8 THEN violation (premature hub)`.
- **Violation response:**
  - *Under-hubbed (≥8 siblings, still flat):* consolidate into a hub at the next audit; index cost is compounding until fixed.
  - *Over-hubbed (hub exists, <8 siblings):* split back into standalone top-level entries.

## Rationale

A host that reads every installed entry's description on every turn pays a cost proportional to entry count, whether or not the entry is used — bodies are effectively free (loaded on demand) but descriptions are not. A flat, growing list silently inflates the base cost of every interaction. The hub form converts an unbounded per-entry tax into a bounded per-family tax (one description instead of 8–30), but only pays for itself once a family is large enough that the indirection hop is worth it. Below that size, a hub adds a routing step without meaningfully shrinking the index — matching the general principle that new abstractions must earn their keep against a concrete, recurring cost rather than being applied preemptively. The 8-sibling threshold gives that judgment a countable, auditable trigger instead of leaving it to taste.

## Failure Modes

- **Over-stuffed hub.** A hub that keeps absorbing new siblings well past the threshold (documented risk: 30+) gets a routing table that is itself hard to navigate — the fix is splitting the hub, which is outside this rule's scope but is the natural next check in an index audit.
- **Hidden spokes.** Because spoke-level detail is deliberately unindexed, a spoke filed under the wrong hub becomes unreachable — cross-hub placement needs its own audit check, not just the sibling count.
- **Premature hubbing.** Consolidating 3–4 entries "to be tidy" or "in anticipation of growth" buys negligible index savings today and adds a lookup hop on every use until the family actually grows into the threshold.

## Contract

### Preconditions
A library of related skills, commands, or capability entries exists, each carrying its own always-on description that the host reads on every turn regardless of use. The boundary of a "family" (which entries belong together) is defined or definable.

### Invariants
Any family of related entries with 8 or more siblings — existing today, or clearly forecast to reach that count — is consolidated into one hub entry whose description is a routing surface and whose body is a routing table; the family's depth moves into detail files that are never indexed individually and are reached only after the hub fires. Families with fewer than 8 siblings remain standalone top-level entries and are never consolidated into a hub.

### Governance
Owner: whoever curates the skill/capability index (library maintainer, workspace steward). The threshold check applies at the moment a new family is proposed and whenever an existing family gains a member. Periodic index audits re-check sibling counts as the library grows, since a family can cross the threshold gradually.

### Recovery
If a family reaches 8+ siblings without being hubbed: the index is silently paying one description per sibling instead of one per family — consolidate at the next audit. If a hub was created for a family below the threshold: split it back into standalone entries; the indirection hop is unjustified index overhead. If a hub grows far past the threshold (documented risk: 30+ spokes) and its routing table becomes hard to navigate: split the hub — this rule governs the create-vs-standalone decision, not the upper bound, but an audit that surfaces split candidates is the adjacent remedy.
