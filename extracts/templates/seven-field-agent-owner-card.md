---
title: "Seven-Field Agent Owner Card"
type: "extracted-artifact"
assigned_form: "template"
source_finding: "agent-owner-card-human-facing-registry"
extraction_date: "2026-07-19"
last_change_session: 152
last_change_report: "agent-governance-and-trust.harvest-queue"
identification_report: "agent-governance-and-trust.harvest-queue"
deployed: false
deployed_to: null
context:
  applies_to:
    - "teams or individuals running any agent whose output reaches other people or systems without per-run review"
    - "organizations that need a human-legible answer to 'who owns this agent and what does it do' faster than reading its configuration"
    - "settings where multiple agents are in use and nobody has an inventory of what's running"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "operate"
  reversibility: "trivial — a documentation artifact; creating, editing, or discarding a card has no migration cost"
  auditability: "high — presence and completeness of the seven fields is directly file-verifiable; absence of a card for a running agent is itself a finding"
  evidence_strength: "Medium"
  adoption:
    status: "Partially Adopted"
    notes: "Practitioner framework, not yet backed by production usage data; the field set has been used as a design input for agent-directory documentation in at least one adopting team."
contract:
  preconditions: "An agent is in active use by a team or individual and its output or actions affect people, systems, or decisions beyond the agent's operator. Someone can be named as accountable for the agent's behavior and permissions."
  invariants: "Every agent that matters has exactly one current owner card. All seven fields are filled — none left as a placeholder. The card is discoverable by anyone who needs to know what an agent does or who to ask about it (a shared roster, a directory, a channel), not buried in private notes."
  governance: "Owner: the person or team responsible for the agent's behavior — the same person named in the card's own Owner field. When an agent changes hands, the card's Owner field changes in the same act as the handoff, not after. A registry maintainer (if one exists) owns keeping the roster of cards current, not the content of any individual card."
  recovery: "If an agent is found running with no card, that is a finding: treat it as an unowned agent (shadow process) until a card is created and an owner named. If a card is stale — the owner has left, the agent's actual behavior has drifted from the card's can-do/can't-do fields — treat the card as unreliable until reconciled against the agent's current configuration; do not trust an unreconciled card over the agent's actual behavior."
tags:
  - "extracted-artifact"
  - "template"
  - "agent-governance"
  - "ownership"
  - "accountability"
---

# Seven-Field Agent Owner Card

**Source:** [[agent-owner-card-human-facing-registry]]
**Form:** template
**Extraction date:** 2026-07-19

## Variables

| Variable | Type | Description |
|---|---|---|
| `{{AGENT_NAME}}` | string | The agent's name, as anyone encountering its output would recognize it. |
| `{{OWNER}}` | string | The named person (not a team alias) accountable for this agent's behavior. |
| `{{JOB}}` | one sentence | What the agent does, stated plainly enough that a non-technical stakeholder understands its purpose. |
| `{{SOURCES}}` | list | What the agent is allowed to read — data sources, tools, systems it can query. |
| `{{CAN_DO}}` | list | The actions or outputs the agent is permitted to produce. |
| `{{CANT_DO}}` | list | Explicit boundaries — what the agent must never do, even if technically capable. |
| `{{WATCHED_FAILURE_MODE}}` | string | The specific failure this agent is most likely to produce, stated concretely enough to check for it (not "it might be wrong" — the actual known failure shape). |

## Body

```markdown
## Agent Owner Card — {{AGENT_NAME}}

**Owner:** {{OWNER}}
**Job:** {{JOB}}

**Sources (what it reads):**
- {{SOURCE_1}}
- {{SOURCE_2}}

**Can do:**
- {{CAN_DO_1}}
- {{CAN_DO_2}}

**Can't do:**
- {{CANT_DO_1}}
- {{CANT_DO_2}}

**Watch for:** {{WATCHED_FAILURE_MODE}}
```

## Usage

Write one card per agent that matters — "matters" meaning its output or actions reach anyone beyond its own operator without per-run review. Publish the card somewhere discoverable (a shared channel, a directory, a roster document); a card that only the owner has seen doesn't solve the visibility problem. Fill all seven fields before the agent goes into use, not retroactively after an incident.

Scale up by aggregating cards into a team-level roster: a plain list of agents in use, each row carrying owner, sources, permissions, and known failure mode. The roster answers "what agents are running and who owns them" at a glance; the card answers "what exactly does this one do" in depth. Prefer generating the roster from the cards (or from agent definition files directly) over hand-maintaining it — a hand-maintained roster drifts from reality.

## Variation Axis

- **Individual certificate:** one person's personal-use agent — the card is a self-accountability artifact, often informal (a Slack post: "this is my agent, this is what it does").
- **Team roster row:** the same seven fields compressed into a spreadsheet or table row, one per agent, for teams running several agents at once — adds review cadence as an eighth practical column even though it's not part of the core seven.
- **Machine-readable card:** the seven fields expressed as frontmatter on the agent's own definition file, so the human-facing roster can be generated from source rather than maintained by hand — trades a small authoring step for eliminating registry rot.
- **Watched-failure-mode as review trigger:** tie the card's failure-mode field directly to a review checklist — the review specifically checks for the declared failure, rather than reviewing generically.

## Contract

### Preconditions
An agent is in active use by a team or individual and its output or actions affect people, systems, or decisions beyond the agent's operator. Someone can be named as accountable for the agent's behavior and permissions.

### Invariants
Every agent that matters has exactly one current owner card. All seven fields are filled — none left as a placeholder. The card is discoverable by anyone who needs to know what an agent does or who to ask about it (a shared roster, a directory, a channel), not buried in private notes.

### Governance
Owner: the person or team responsible for the agent's behavior — the same person named in the card's own Owner field. When an agent changes hands, the card's Owner field changes in the same act as the handoff, not after. A registry maintainer (if one exists) owns keeping the roster of cards current, not the content of any individual card.

### Recovery
If an agent is found running with no card, that is a finding: treat it as an unowned agent (shadow process) until a card is created and an owner named. If a card is stale — the owner has left, the agent's actual behavior has drifted from the card's can-do/can't-do fields — treat the card as unreliable until reconciled against the agent's current configuration; do not trust an unreconciled card over the agent's actual behavior.
