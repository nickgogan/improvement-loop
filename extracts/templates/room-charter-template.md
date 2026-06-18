---
title: "Room Charter Template"
type: "extracted-artifact"
assigned_form: "template"
source_finding: "oz-multi-agent-room-model"
extraction_date: "2026-05-25"
last_change_session: 102
last_change_sl: "session-102-codifier-identify-and-extract-artifacts"
identification_report: null
deployed: false
deployed_to: null
context:
  applies_to:
    - "multi-agent systems that coordinate inside bounded chat contexts"
    - "orchestrators assigning agents to topic- or project-scoped rooms"
    - "any team designing peer-to-peer agent coordination with human observer access"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "specify"
  reversibility: "trivial — a specification document; changing or discarding it has no migration cost"
  auditability: "high — the charter is a persistent artifact reviewed before and after each room session; all field changes are diffable"
  evidence_strength: "Medium (practitioner-documented)"
  adoption:
    status: "Not Yet Started"
    notes: "Oz Workspace (warpdotdev/oz-workspace) is the reference implementation. Thousands of live Oz sessions observed at build.warp.dev, but the charter document form is inferred from architectural components, not from explicit charter files in the repo."
contract:
  preconditions: "A multi-agent workflow has been decomposed into at least one bounded coordination scope. The orchestrator has identified which agents will participate. The artifact type(s) the room is expected to produce are known. A communication channel (e.g., SSE endpoint) or equivalent is available."
  invariants: "Every room has exactly one scope declaration (one topic/project boundary). The agent roster enumerates each participant with its system prompt reference, skills, and tool bindings. The artifact registry declares every expected output type before work begins. Human observer access is specified — at minimum, whether real-time visibility is provided. The kanban board is initialized with a starting backlog before agents are activated."
  governance: "Owner: the orchestrator or system designer who activates the room. The charter must exist before agents are admitted to the room. Scope changes after activation require a new charter or an explicit amendment. Agent roster changes (add/remove) are logged against the charter version."
  recovery: "If scope drift is detected mid-session → halt new task intake, amend the charter scope, and reconfirm with the human observer before resuming. If an agent goes offline → mark it as inactive in the roster; do not reassign its in-progress tasks without human confirmation. If the kanban is corrupted or lost → reconstruct from agent message history before resuming."
tags:
  - "extracted-artifact"
  - "template"
  - "multi-agent"
  - "orchestration"
  - "coordination"
---

# Room Charter Template

**Source:** [[oz-multi-agent-room-model]]
**Form:** template
**Extraction date:** 2026-05-25

A reusable specification scaffold for defining a bounded multi-agent coordination room before agents are activated. Fill in one charter per room before admitting agents.

## Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `{{ROOM_NAME}}` | Short identifier for the room (used in @mention routing) | Yes |
| `{{ROOM_SCOPE}}` | One-sentence declaration of what this room is for | Yes |
| `{{SCOPE_BOUNDARY}}` | What is explicitly out of scope for this room | Yes |
| `{{AGENT_N_ID}}` | Identifier for each agent (one row per agent) | Yes |
| `{{AGENT_N_SYSTEM_PROMPT_REF}}` | Path or reference to the agent's system prompt | Yes |
| `{{AGENT_N_SKILLS}}` | Comma-separated list of skills available to the agent | Yes |
| `{{AGENT_N_MCP_SERVERS}}` | MCP servers bound to this agent in this room | No |
| `{{AGENT_N_REPO}}` | Associated repository (if applicable) | No |
| `{{ARTIFACT_TYPE_N}}` | Name of an expected output artifact type | Yes (≥1) |
| `{{ARTIFACT_TYPE_N_SCHEMA}}` | Schema or format reference for the artifact type | No |
| `{{SSE_CHANNEL_URL}}` | SSE endpoint for real-time message streaming | Yes |
| `{{AUTH_TOKEN_REF}}` | Reference to the token used for agent authentication | Yes |
| `{{OBSERVER_ACCESS}}` | How human observers connect and what they can see | Yes |
| `{{OBSERVER_CONTROLS}}` | Actions available to the human observer (view/approve/cancel) | Yes |
| `{{INITIAL_BACKLOG}}` | Ordered list of tasks to seed the kanban backlog | Yes (≥1) |
| `{{ACTIVATION_CONDITION}}` | What triggers room activation | Yes |
| `{{TERMINATION_CONDITION}}` | What triggers room closure | Yes |

## Body

```markdown
# Room Charter: {{ROOM_NAME}}

## Scope
**Purpose:** {{ROOM_SCOPE}}
**Out of scope:** {{SCOPE_BOUNDARY}}

## Agent Roster

| Agent | System Prompt | Skills | MCP Servers | Repo |
|-------|--------------|--------|-------------|------|
| {{AGENT_1_ID}} | {{AGENT_1_SYSTEM_PROMPT_REF}} | {{AGENT_1_SKILLS}} | {{AGENT_1_MCP_SERVERS}} | {{AGENT_1_REPO}} |
| {{AGENT_2_ID}} | {{AGENT_2_SYSTEM_PROMPT_REF}} | {{AGENT_2_SKILLS}} | {{AGENT_2_MCP_SERVERS}} | {{AGENT_2_REPO}} |

*Add rows for additional agents.*

## Artifact Type Registry

| Artifact Type | Schema / Format Reference | Producing Agent(s) |
|---------------|--------------------------|-------------------|
| {{ARTIFACT_TYPE_1}} | {{ARTIFACT_TYPE_1_SCHEMA}} | {{AGENT_N_ID}} |
| {{ARTIFACT_TYPE_2}} | {{ARTIFACT_TYPE_2_SCHEMA}} | {{AGENT_N_ID}} |

*Add rows for each expected output type.*

## Communication Channel

- **SSE endpoint:** {{SSE_CHANNEL_URL}}
- **Auth token reference:** {{AUTH_TOKEN_REF}}
- **@mention routing:** agents address each other by `{{AGENT_N_ID}}`

## Human Observer Access

- **Connection:** {{OBSERVER_ACCESS}}
- **Available controls:** {{OBSERVER_CONTROLS}}

## Kanban Initialization

**Backlog (initial):**
- [ ] {{INITIAL_BACKLOG_ITEM_1}}
- [ ] {{INITIAL_BACKLOG_ITEM_2}}
- [ ] {{INITIAL_BACKLOG_ITEM_3}}

*Agents move items: backlog → in progress → done.*

## Activation / Termination

- **Activated when:** {{ACTIVATION_CONDITION}}
- **Closed when:** {{TERMINATION_CONDITION}}

## Charter Version

| Field | Value |
|-------|-------|
| Created | YYYY-MM-DD |
| Last amended | YYYY-MM-DD |
| Amended by | — |
| Amendment reason | — |
```

## Usage

1. Copy the body above into a new file named `room-charter-<room-name>.md` before activating the room.
2. Fill in every required variable. Leave optional fields as `—` if not applicable.
3. Review the charter with the human observer before admitting agents.
4. After the room closes, archive the charter alongside the session artifacts.

## Variation Axis

| Variation | Adaptation |
|-----------|-----------|
| Single-agent room | Roster has one row; remove @mention routing section |
| No SSE (polling) | Replace SSE fields with polling endpoint and interval |
| Async human observer | Set observer controls to `view-only`; add async review checkpoint to termination condition |
| Multi-repo room | Add a `Repos` column to the agent roster; note merge strategy in scope declaration |
| Nested rooms (sub-rooms) | Add a `Parent Room` field at the top; reference the parent charter |

## Contract

### Preconditions
A multi-agent workflow has been decomposed into at least one bounded coordination scope. The orchestrator has identified which agents will participate. The artifact type(s) the room is expected to produce are known. A communication channel (e.g., SSE endpoint) or equivalent is available.

### Invariants
Every room has exactly one scope declaration (one topic/project boundary). The agent roster enumerates each participant with its system prompt reference, skills, and tool bindings. The artifact registry declares every expected output type before work begins. Human observer access is specified — at minimum, whether real-time visibility is provided. The kanban board is initialized with a starting backlog before agents are activated.

### Governance
Owner: the orchestrator or system designer who activates the room. The charter must exist before agents are admitted to the room. Scope changes after activation require a new charter or an explicit amendment. Agent roster changes (add/remove) are logged against the charter version.

### Recovery
If scope drift is detected mid-session → halt new task intake, amend the charter scope, and reconfirm with the human observer before resuming. If an agent goes offline → mark it as inactive in the roster; do not reassign its in-progress tasks without human confirmation. If the kanban is corrupted or lost → reconstruct from agent message history before resuming.
