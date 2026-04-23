---
name: "Time-Window Proactive Agent Loop"
summary: "A scheduled agent that runs a time-aware decision loop: date anchor → duplicate check → time window classification → external pull (calendar, weather) → internal enrich (knowledge base search) → deliver via channel → log. OB1's Life Engine implements 7 briefing types across 5 time windows with habit tracking, weekly self-improvement reviews, and channel delivery (Telegram/Discord)."
implementation_notes: "MetaSystem has no proactive agent. The pattern could inform Household OS daily operations — morning briefings, pre-meeting prep, evening reviews. The date anchoring and duplicate checking are critical implementation details that summaries miss."
category: "Agentic Systems"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: P2 (Design Required)
applicability:
  - "S3 (Claude Code Build)"
  - "General"
adopted_in: []
sources: []
related_findings:
  - file: "kairos-autonomous-background-daemon.md"
    rel: "same-problem"
  - file: "scheduled-tasks-for-real-time-context-maintenance.md"
    rel: "same-problem"
  - file: "claude-code-channels-telegramdiscord-as-agent-inte.md"
    rel: "enables"
  - file: "five-pillar-agentic-os-framework.md"
    rel: "extends"
date_discovered: "2026-04-20"
last_updated: "2026-04-20"
pipeline_status: raw
consumed_by: []
---

## What It Is
A proactive personal assistant that runs on a recurring loop, making time-aware decisions about what the user needs. The core loop has 7 steps:

0. **Date anchor** — Establish exact date/time via `date` command or API response. Store as `anchor_date` and `anchor_time`. All date arithmetic is calculated from this anchor — never use vague terms like "recently."
1. **Time check** — Classify current time into a window (early morning, pre-meeting, midday, late afternoon, evening).
2. **Duplicate check** — Query the briefings table for entries already sent on `anchor_date`. Don't repeat.
3. **Decide** — Based on time window, what should be delivered?
4. **External pull** — Fetch live data (calendar events, weather, attendee lists).
5. **Internal enrich** — Search the knowledge base for context on what was just found (attendee history, meeting topics, related notes). External before internal — can't enrich what you haven't seen.
6. **Deliver** — Send via channel tools (Telegram/Discord). Concise, mobile-friendly, bullet points. Silence is better than noise.
7. **Log** — Record what was sent so the next cycle knows what's been covered.

Seven briefing types: morning, pre_meeting, checkin, evening, habit_reminder, weekly_review, custom. Five time windows with specific actions for each.

## Why It Matters
Most agent systems are reactive — they respond to user prompts. A proactive agent loop inverts this: the agent initiates based on time, context, and history. The implementation details (date anchoring, duplicate checking, external-then-internal enrichment, channel delivery) are the critical patterns that distinguish a production proactive agent from a conceptual one.

## Why People Are Using It
Observed in [OB1 (Open Brain)](https://github.com/NateBJones-Projects/OB1) — see [[ob1-analysis]] for structural details. The Life Engine recipe (`recipes/life-engine/life-engine-skill.md`) is a community contribution that runs via Telegram or Discord. It includes habit tracking with streak management, weekly self-improvement reviews, and a state table for tracking evolution goals.

## Potential Alternatives
- **KAIROS background daemon** (Claude Code): Platform-level daemon with 15-second proactive budgets. More powerful but behind feature flags and unreleased.
- **Cron-triggered skills** (GSD, Superpowers): External scheduler invokes skills on a schedule. Less sophisticated — no time-window logic or duplicate checking.
- **Calendar-driven triggers** (Google Calendar → webhook → agent): Event-based rather than time-based. Good for meetings but misses morning briefings and habit nudges.

## Potential Improvements
- Location awareness — different briefings at home vs. office vs. travel
- Priority-based delivery — suppress low-priority briefings during focus time
- Cross-agent coordination — proactive agent informs other agents about upcoming context needs
- User preference learning — adjust briefing frequency and content based on engagement patterns

## Potential Failure Modes
- Notification fatigue — proactive agents that talk too much get muted
- Date anchor drift — if the system clock is wrong, all time-window logic fails
- Channel tool reliability — Telegram/Discord API failures need graceful handling
- State table corruption — the briefings log is the deduplication mechanism; corruption means repeated messages
