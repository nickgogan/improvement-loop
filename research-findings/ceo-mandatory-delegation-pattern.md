---
name: CEO Mandatory Delegation Pattern
summary: Top-level agent persona explicitly told 'You MUST delegate, do NOT write code yourself.' Defines what the agent should NOT do as architectural intent engineering. CEO creates subtasks with parentId/goalId
  and routes to domain specialists via chain of command.
implementation_notes: null
category: Intent Engineering
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P3
applicability:
- S3 (Claude Code Build)
adopted_in: []
sources: []
related_findings:
- file: org-chart-hierarchy-as-scalable-claude-code.md
  rel: extends
proposals: null
date_discovered: '2026-04-08'
last_updated: '2026-04-19'
pipeline_status: raw
consumed_by: []
---

# CEO Mandatory Delegation Pattern

## What It Is
Paperclip's CEO persona is explicitly told "You MUST delegate work rather than doing it yourself" and "Do NOT write code, implement features, or fix bugs yourself." The CEO creates subtasks with parentId + goalId and assigns them to reports (CTO for code/bugs/infra, CMO for marketing/content, UXDesigner for design). This is intent engineering at the architectural level — defining what the agent should NOT do is as important as what it should do. Chain of command routing ensures work flows to the appropriate domain specialist.

## Why It Matters
Most agent intent engineering focuses on what to do. This pattern focuses on what NOT to do. Without explicit delegation constraints, the most capable agent tends to do everything itself — becoming a bottleneck and producing lower-quality work outside its designated role. The CEO role exists to coordinate, not execute. Negative constraints ("do not write code") are often more effective than positive ones ("focus on coordination") because they create hard boundaries.

## Why People Are Using It
Observed in [Paperclip](https://github.com/paperclipai/paperclip) v2026.403.0 — see [[paperclip-analysis]] for structural details. Most agent intent engineering focuses on what to do. This pattern focuses on what NOT to do. The CEO role exists to coordinate, not execute. This prevents the most capable agent from becoming a bottleneck by doing everything itself.

## Potential Alternatives
Capability-limited agents (no code tools given to coordinator). Soft preference ("prefer to delegate"). Role descriptions without negative constraints. Flat team structure without a coordinator.

## Potential Improvements
Dynamic delegation based on agent load and availability. Delegation quality scoring to improve routing over time. Escalation paths when delegates fail or are unavailable.

## Potential Failure Modes
Over-delegation of trivial tasks that the CEO could resolve faster inline. Delegation overhead for simple coordination that doesn't need subtasks. Loss of context as requirements pass through the delegation chain. CEO becoming a pure routing bottleneck if all work must flow through it.
