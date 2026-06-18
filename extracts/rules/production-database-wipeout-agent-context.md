---
title: "Agents Must Have Explicit Production Environment Markers"
type: "extracted-artifact"
assigned_form: "rule"
source_finding: "production-database-wipeout-agent-context"
extraction_date: "2026-05-25"
last_change_session: 102
last_change_sl: "session-102-codifier-identify-and-extract-artifacts"
identification_report: null
deployed: false
deployed_to: null
context:
  applies_to:
    - "agents that operate on data infrastructure, cloud resources, databases, or any environment with destructive-action capability"
    - "any agent workflow that can delete, overwrite, truncate, or destroy persistent resources"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "operate"
  reversibility: "low — adding environment markers requires infrastructure tagging and agent pre-flight checks; removal is possible but re-exposes the failure mode"
  auditability: "high — environment marker checks can be logged as pre-flight events; absence of a marker in session logs indicates the check was skipped"
  evidence_strength: "Strong (production-tested)"
  adoption:
    status: "Not Yet Started"
    notes: "Derived from a real production incident (1.9M rows destroyed). No adoption in MetaSystem at time of extraction."
contract:
  preconditions: "An agent is about to perform any destructive operation (delete, truncate, overwrite, deprovision) on a persistent resource. The system has at least one environment (production, staging, dev) distinction."
  invariants: "Before any destructive operation, the agent performs a pre-flight check: read and surface the environment marker of the target resource. If no machine-readable marker is present, the agent halts and escalates rather than assuming non-production. The marker is stored in a document the agent can access — not solely in the operator's head."
  governance: "Infrastructure owners are responsible for maintaining machine-readable environment markers (tags, config files, environment variables) on all resources an agent can reach. Agent prompts and skills that permit destructive operations must include an explicit pre-flight check against the environment marker. The check cannot be bypassed by agent reasoning — it is a workflow gate."
  recovery: "If the agent cannot find or read the environment marker, it must halt and ask for explicit human confirmation before proceeding. If the marker indicates production and the operation is destructive, the agent must halt unconditionally — no override by instruction alone. If a destructive operation is executed without a verified non-production marker, treat as an incident: halt further operations, escalate to operator, preserve logs."
tags:
  - "extracted-artifact"
  - "rule"
  - "safety"
  - "production"
  - "agent-discipline"
  - "pre-flight"
---

# Agents Must Have Explicit Production Environment Markers

**Source:** [[production-database-wipeout-agent-context]]
**Form:** rule
**Extraction date:** 2026-05-25

## Condition

An agent is about to perform any operation that is destructive or irreversible on a persistent resource: database rows, cloud infrastructure, file system data, network configuration, or application clusters. The agent has the technical capability to execute the operation.

## Action

**Required:** Before executing, the agent must read a machine-readable environment marker (tag, config file, environment variable, or equivalent) that identifies whether the target resource is production or non-production. The marker must be present in a document or system the agent can access — not solely in the operator's memory. If the marker confirms non-production, proceed. If the marker confirms production, halt unconditionally and require explicit human authorization.

**Forbidden:** Assuming the environment is non-production because it "looks like" a fresh setup, because config files are absent, or because the agent has no contrary information. Treating the absence of a production marker as confirmation of non-production.

## Boundary

Enforced at the decision point immediately before any destructive or irreversible operation. Applies to all agents with write/delete permissions on persistent resources, regardless of the size or apparent risk of the operation. The rule does not apply to read-only operations.

## Enforcement

- **Mechanism:** Agent skills and prompts that permit destructive operations must include a mandatory pre-flight environment check as a declared step — not an optional recommendation. The check reads the resource's environment marker and surfaces the result before any destructive command is issued.
- **Check (deterministic):** `(environment_marker_read == true) AND (environment_marker_value IN ["staging", "dev", "test", "sandbox"])`. Either branch false → halt and escalate.
- **Violation response:** Halt all further operations on the affected resource. Log the halted operation with the attempted action and the reason for halt. Escalate to the operator with the specific resource identifier and the missing/conflicting marker.
- **Cannot be self-certified:** The pre-flight check must read an external marker — not rely on the agent's assessment of whether something "seems like" production. Agent judgment about environment type is the failure mode this rule exists to prevent.

## Rationale

Agent competence (technically correct execution) and agent safety (appropriate for the environment) are independent properties. A highly capable agent operating with incorrect context assumptions can cause worse damage than a less capable one, because it will execute its incorrect assumption precisely and completely. The canonical incident (1.9M rows destroyed) involved no technical errors — every action was logically correct given the agent's context. The failure was a single missing fact: "this infrastructure is production." That fact existed only in the engineer's head.

The fix is not to make agents smarter about inferring environment type — it is to encode the critical fact in a machine-readable artifact the agent can access. When the marker exists, the pre-flight check is a fast no-op. When it does not exist, the halt is the correct response: absence of a safety guarantee is itself a safety signal.

## Failure Modes

- **Tags accidentally removed.** Resource is de-tagged during maintenance, pre-flight check finds no marker, agent assumes non-production (wrong) or halts (correct but disruptive). Mitigation: treat marker absence as production-equivalent; require explicit non-production confirmation.
- **Human confirmation fatigue.** Pre-flight prompts generate operator fatigue; operators begin approving without reading. Mitigation: surface the specific resource identifier and its current marker in every prompt; make ignoring it require deliberate action.
- **Agent reasons around the constraint.** A sufficiently capable agent may interpret "temporary" or "cleanup" framing in its instructions as overriding the production marker. Mitigation: the constraint must be enforced at the workflow level — a gate the agent cannot bypass through reasoning — not solely in the agent's prompt.
- **Marker granularity mismatch.** A single environment has mixed production and non-production resources; a marker on the environment does not distinguish them. Mitigation: markers must be at the resource level (row, table, cluster, bucket), not only at the environment level.

## Contract

### Preconditions
An agent is about to perform any destructive operation (delete, truncate, overwrite, deprovision) on a persistent resource. The system has at least one environment (production, staging, dev) distinction.

### Invariants
Before any destructive operation, the agent performs a pre-flight check: read and surface the environment marker of the target resource. If no machine-readable marker is present, the agent halts and escalates rather than assuming non-production. The marker is stored in a document the agent can access — not solely in the operator's head.

### Governance
Infrastructure owners are responsible for maintaining machine-readable environment markers on all resources an agent can reach. Agent prompts and skills that permit destructive operations must include an explicit pre-flight check against the environment marker. The check cannot be bypassed by agent reasoning — it is a workflow gate.

### Recovery
If the agent cannot find or read the environment marker, it must halt and ask for explicit human confirmation before proceeding. If the marker indicates production and the operation is destructive, the agent must halt unconditionally — no override by instruction alone. If a destructive operation is executed without a verified non-production marker, treat as an incident: halt further operations, escalate to operator, preserve logs.
