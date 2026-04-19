---
notion_id: 32b1e08b-9b34-81a0-b3e0-d0eb6c161354
name: 'Skills-Inside-Workspace: Contextual Skill Invocation Rather Than Always-Loaded'
summary: Instead of loading all skills globally at session start, the three-layer workspace system maps specific skills to specific task types within specific workspaces — ensuring skills are only invoked
  when contextually appropriate, preventing unintended skill triggering.
implementation_notes: null
category: Tool Integration
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
proposer_priority: null
applicability:
- S3 (Claude Code Build)
adopted_in: []
sources:
- stop-building-ai-agents-use-this-folder-system-ins.md
proposals: []
date_discovered: '2026-03-22'
last_updated: '2026-04-07'
related_findings:
- file: three-layer-folder-as-workspace-architecture.md
  rel: enables
- file: task-to-file-routing-table-in-context-files.md
  rel: same-problem
pipeline_status: "raw"
consumed_by: []
---
# Skills-Inside-Workspace: Contextual Skill Invocation Rather Than Always-Loaded

## What It Is
Jake contrasts two approaches: (1) globally loaded skills — all skills available at all times, agent must decide when to invoke each; (2) contextually mapped skills — the workspace routing table specifies which skills apply to which tasks, and the agent invokes them only in those contexts. He gives examples: the humanizer skill is only in the routing table for writing tasks; the front-end-design skill only for production tasks. Skills can also be referenced in context files as 'you might need this skill' so the agent considers but doesn't automatically trigger them. Jake notes: 'You're putting skills inside of a thought process.'

## Why It Matters
Globally loaded skills create disambiguation problems at scale: with 15+ skills, the agent must reason about which skill applies to the current task, which adds latency and can cause incorrect skill selection. Contextual mapping eliminates this overhead by pre-specifying relevance — the agent doesn't need to reason about skill applicability, only about skill execution.

## Why People Are Using It
Follows the principle of least privilege for capabilities: the agent only has access to the skills that make sense for the current context. Reduces the risk of a writing task accidentally triggering a production skill with side effects.

## Potential Alternatives
Global skill loading with intent detection, semantic skill routing based on task embedding similarity, explicit skill invocation by name in every prompt.

## Potential Improvements
Dynamic skill composition: the routing table specifies base skills, and the agent can request additional skills if the task requires capabilities not in the default set. Skill versioning: routing table references specific skill versions to prevent unexpected behavior changes.

## Potential Failure Modes
Routing table omits a needed skill for an edge-case task combination. Agent invokes a skill from the routing table even when the task doesn't actually require it (over-eager invocation).
