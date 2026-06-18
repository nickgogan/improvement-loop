---
name: "Tiered Interaction Model: Quick Ask vs. Supervisor Dashboard"
summary: "Agent interaction should be split into two deliberately separate tiers: (1) a mobile/messaging tier for quick asks — fire-and-forget via Channels, Telegram, Discord, iMessage; and (2) a supervisor dashboard tier for managing multiple goals in parallel — kanban-style board with per-goal agent instances, plan visibility, and conversation history. The real interaction question is not 'can I chat from my phone?' but 'how do I manage multiple goals simultaneously?'"
implementation_notes: null
category: "Orchestration"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: P3 (Monitor)
applicability:
  - "S3 (Claude Code Build)"
  - "General"
adopted_in: []
sources:
  - "agentic-os-five-pillars-claude-code.md"
related_findings:
  - file: five-pillar-agentic-os-framework.md
    rel: enables
  - file: goal-first-agent-management-abstraction.md
    rel: extends
  - file: claude-code-channels-telegramdiscord-as-agent-inte.md
    rel: enables
  - file: iterative-turn-based-kanban-for-agent-management.md
    rel: same-problem
  - file: claude-dispatch-native-mobile-to-local-agent-orch.md
    rel: enables
  - file: cloud-plan-parallel-multitasking-pattern.md
    rel: same-problem
  - file: agui-human-control-layer-not-ui.md
    rel: same-problem
proposals: null
date_discovered: "2026-05-25"
last_updated: "2026-05-25"
pipeline_status: "classified"
consumed_by: []
tags:
  - "session-95-reextract"
---
# Tiered Interaction Model: Quick Ask vs. Supervisor Dashboard

## What It Is

A two-tier interaction architecture for agent-operated systems, deliberately splitting human-agent interaction into two modes based on cognitive demand:

**Tier 1: Quick Ask (Mobile/Messaging)**
- Channel: Telegram, iMessage, Discord via Claude Code Channels feature
- Use case: Fire-and-forget single tasks while on the move
- Interaction depth: One message in, one result out
- Example: "Draft a reply to this email" sent from phone while commuting

**Tier 2: Supervisor Dashboard (Multi-Goal Management)**
- Channel: Local web UI ("Command Center") wrapping terminal sessions
- Use case: Managing multiple business goals running in parallel
- Interaction depth: Per-goal agent instances, plan visibility alongside chat, sub-conversations within goals
- Example: Kanban board showing 4-6 goals, each with its own agent, plan on the right side auto-updating as steps complete

The key design insight: most agent frameworks compete on Tier 1 (Telegram integration, mobile access, Discord bots) but miss the Tier 2 problem entirely. "The real question now that agents are so good is how do we manage multiple conversations and multiple goals at the same time." As model capabilities improve, the human role shifts from task executor to supervisor — and the interaction layer must support that shift.

## Why It Matters

Single-conversation interfaces create a scaling bottleneck when running multiple agent workflows. The practitioner describes "flicking between chat threads and trying to remember which one was which" as a real operational problem with 6+ parallel goals. The two-tier split means each tier is optimized for its use case: mobile chat is optimized for speed and accessibility; the dashboard is optimized for visibility, planning, and parallel goal tracking.

For MetaSystem, this maps to the difference between quick operational tasks (single skill invocations) and multi-phase project work (GSD phases, milestone planning). The current terminal-based interaction is effectively Tier 1 only.

## Why People Are Using It

The practitioner built the Command Center after discovering that managing multiple business goals through chat threads was unsustainable. The dashboard implementation: goal as primary unit, each goal spawns a Claude Code instance, kanban columns for status, plan document visible alongside conversation, click-through to full chat history.

## Potential Improvements

The two tiers could be extended to three: Tier 1 (quick ask), Tier 2 (single-goal deep work), Tier 3 (multi-goal supervisor). Claude Desktop's recent updates with multi-plan management are converging toward Tier 2/3 but remain "very technical, very focused on GitHub commits" rather than goal-level abstraction. The practitioner notes this gap.

## Potential Failure Modes

Building a custom dashboard creates maintenance burden — every Claude Code update may break the UI wrapper. The dashboard becomes stale if not kept in sync with the underlying agent capabilities. Also, the "supervisor" metaphor may encourage excessive monitoring rather than trust-based delegation, reducing the autonomy gains that agents provide.
