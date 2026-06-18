---
title: "Scope Skills to Workspace Routing Tables, Never Globally Load"
type: "extracted-artifact"
assigned_form: "rule"
source_finding: "skills-inside-workspace-contextual-skill"
extraction_date: "2026-05-25"
last_change_session: 102
last_change_sl: "session-102-codifier-identify-and-extract-artifacts"
identification_report: null
deployed: false
deployed_to: null
context:
  applies_to:
    - "agents or skill systems that have 15 or more skills available in a session"
    - "any workspace configuration that maps task types to agent behaviors"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "build"
  reversibility: "trivial — routing table entries are text; adding or removing a mapping has no migration cost"
  auditability: "high — routing table is a static file; each mapping is an explicit, inspectable declaration"
  evidence_strength: "Medium (practitioner-documented)"
  adoption:
    status: "Not Yet Started"
    notes: "Jake Browatzki demonstrated contextual skill mapping in his three-layer workspace system. No MetaSystem adoption at time of extraction."
contract:
  preconditions: "A skills directory contains 15 or more skills. A workspace routing table (context file, CLAUDE.md section, or task-type map) exists or can be created. The agent framework supports contextual system prompt construction."
  invariants: "Every skill reference in the routing table names the skill explicitly. No skill is loaded globally for all task types unless it is truly universal. The routing table is the canonical source of which skills apply to which tasks — agent does not infer skill applicability from skill descriptions alone."
  governance: "Routing table is owned by the workspace config layer (CLAUDE.md or equivalent). New skills are added to the routing table at the same time they are added to the skills directory — undeclared skills are invisible to the agent. Skill-to-task mappings are reviewed when a new workspace or task type is added."
  recovery: "If the routing table omits a needed skill for an edge-case task → the agent may surface a gap; the fix is a routing table edit, not a global-load fallback. If the agent invokes a skill not in the current task's routing table entry → treat as a routing table gap; add the mapping explicitly. If routing table and skills directory are out of sync (skill listed but file absent) → log the inconsistency; do not silently skip."
tags:
  - "extracted-artifact"
  - "rule"
  - "skills"
  - "context-engineering"
  - "routing"
---

# Scope Skills to Workspace Routing Tables, Never Globally Load

**Source:** [[skills-inside-workspace-contextual-skill]]
**Form:** rule
**Extraction date:** 2026-05-25

## Condition

An agent has a skill system with 15 or more available skills, or a workspace that maps task types to agent behaviors. The skill catalog is either loaded globally (all skills present for all tasks) or is under consideration for design.

The disambiguation cost increases super-linearly with skill count: at 5 skills the agent self-routes reliably; at 15+ the agent must reason about applicability before acting, adding latency and misrouting risk.

## Action

**Required:** Define a workspace routing table that maps each task type (or workspace context) to the specific skills that apply. Inject only the mapped skills into the agent's context for a given task. Do not load skills globally.

**Permitted variant:** Skills can be referenced in context files as advisory signals ("you might need this skill") without being placed in the active routing table entry — this surfaces the skill for agent consideration without automatically triggering it.

**Forbidden:** Loading all skills for all task types. Delegating skill-applicability reasoning entirely to the agent (agent infers which skill to use from skill descriptions without a routing table). Silently falling back to global load when a routing table entry is incomplete.

## Boundary

Applies from the moment the skill catalog exceeds approximately 15 entries. Below that threshold, global loading is acceptable and the overhead of a routing table may not be warranted.

Scope: workspace configuration layer. Does not govern skill file contents or skill execution behavior — only which skills are visible to the agent at task time.

## Enforcement

- **Mechanism:** Routing table is a static, human-readable file (or CLAUDE.md section). Each workspace or task type has an explicit skill list. Audit by inspecting the table — every active skill appears under at least one task mapping.
- **Check (deterministic):** For each task invocation, `skills_loaded ⊆ routing_table[task_type]`. Any skill loaded outside its mapped task type is a violation. Any skill in the directory with no routing table entry is a dead skill.
- **Violation response:**
  - *Agent invokes an unmapped skill:* halt; record the gap; add the explicit mapping before proceeding.
  - *Routing table missing for a new task type:* define the task type and its skill mappings before the agent is used for that task.
  - *Skills directory and routing table are out of sync:* reconcile immediately; do not allow the agent to operate on stale routing data.
- **Cannot be enforced by the agent itself:** The agent cannot limit its own skill visibility if the catalog is already injected globally. Enforcement is at the prompt-construction layer — the harness or context-file system that builds the system prompt must apply the filter.

## Rationale

Globally loaded skills create disambiguation overhead that scales with skill count. The agent must reason about which skill is appropriate for each task, which is a form of meta-reasoning that adds latency and introduces misrouting risk (writing task accidentally triggers a production deployment skill with side effects).

Contextual mapping applies the principle of least privilege to capabilities: the agent only has access to skills relevant to the current context. This makes behavior more predictable, reduces the risk of unintended side-effect skills being triggered, and makes the skill-to-task contract explicit and auditable.

Jake Browatzki's formulation: "You're putting skills inside of a thought process." The routing table is the externalized, inspectable version of that thought process.

## Failure Modes

- **Routing table omits an edge-case combination.** A task that combines writing and production work has no routing table entry that includes both sets of skills. Mitigation: define composite task types explicitly; or use the advisory-reference pattern ("you might need this skill") for the secondary skill set.
- **Agent over-invokes a mapped skill.** The skill is in the routing table for the task, but the specific subtask doesn't require it. Mitigation: skill invocation triggers are still governed by the skill's own condition — routing table enables, it doesn't mandate.
- **Routing table maintenance lag.** New skill added to directory; routing table not updated; skill is invisible. Mitigation: enforce co-deployment — routing table edit is required in the same operation as skill file creation.
- **Table proliferation.** Many workspaces, each with their own routing table, diverge over time. Mitigation: shared base routing table with workspace-level overrides; review at skill addition time.

## Contract

### Preconditions
A skills directory contains 15 or more skills. A workspace routing table (context file, CLAUDE.md section, or task-type map) exists or can be created. The agent framework supports contextual system prompt construction.

### Invariants
Every skill reference in the routing table names the skill explicitly. No skill is loaded globally for all task types unless it is truly universal. The routing table is the canonical source of which skills apply to which tasks — agent does not infer skill applicability from skill descriptions alone.

### Governance
Routing table is owned by the workspace config layer (CLAUDE.md or equivalent). New skills are added to the routing table at the same time they are added to the skills directory — undeclared skills are invisible to the agent. Skill-to-task mappings are reviewed when a new workspace or task type is added.

### Recovery
If the routing table omits a needed skill for an edge-case task → the agent may surface a gap; the fix is a routing table edit, not a global-load fallback. If the agent invokes a skill not in the current task's routing table entry → treat as a routing table gap; add the mapping explicitly. If routing table and skills directory are out of sync (skill listed but file absent) → log the inconsistency; do not silently skip.
