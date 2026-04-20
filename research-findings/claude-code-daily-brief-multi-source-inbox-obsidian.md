---
name: Claude Code Daily Brief with Multi-Source Inbox and Obsidian Output
summary: Claude Code aggregates Gmail, Google Calendar, Beeper (unified messaging), and Things 3 todos into a single Obsidian daily brief note each morning. It also performs inbox triage — auto-archiving
  cold outreach and spam — so the human only sees high-signal items. Replaces reactive notification-checking with a single intentional daily read.
implementation_notes: 'Concrete integrations used: Gmail API, Google Calendar API, Beeper (aggregates X/DMs, WhatsApp, Telegram, Signal), Things 3 todo app. The brief includes: weather, calendar events,
  actionable emails, messages requiring response, today''s tasks. Inbox archival is rule-taught — the user trains Claude Code on what to archive vs. surface. Output is an Obsidian note updated daily (not
  a new note each day).'
category: Agentic OS
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
proposer_priority: P2 (Design Required)
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources:
- claude-code-for-life-daily-briefs-obsidian-memory.md
related_findings:
- file: scheduled-tasks-for-real-time-context-maintenance.md
  rel: extends
- file: time-window-proactive-agent-loop.md
  rel: same-problem
- file: claude-code-as-vault-query-engine-project-assistant.md
  rel: companion
- file: five-pillar-agentic-os-framework.md
  rel: part-of
- file: cited-health-interview-pattern-parallelized-kb-qa.md
  rel: same-problem
- file: concept-graph-support-contradiction-detection.md
  rel: same-problem
- file: gws-cli-full-google-workspace-control-from.md
  rel: enabled-by
proposals: null
date_discovered: '2026-04-20'
last_updated: '2026-04-20'
pipeline_status: raw
consumed_by: []
---
# Claude Code Daily Brief with Multi-Source Inbox and Obsidian Output

## What It Is
A scheduled Claude Code task that runs once per morning and produces a single consolidated Obsidian note:

- **Calendar** — Google Calendar events for the day
- **Weather** — current/forecast
- **Email** — only actionable emails surfaced; cold outreach and spam auto-archived
- **Messages** — Beeper aggregator (X DMs, WhatsApp, Telegram, Signal) filtered to messages requiring response
- **Tasks** — Things 3 active tasks for today

The inbox triage component is rule-trained: the user teaches Claude Code which categories of email/message to auto-archive vs. surface. Once trained, the user no longer needs to open Gmail, Instagram, or any messaging app to get the day's communications picture.

The output is a persistent Obsidian note that is overwritten/updated each morning — not a new note per day. The human reads it once, checks off items, and moves on.

## Why It Matters
Reactive notification-checking fragments attention and pulls users into feed environments (Instagram, Twitter) that surface distracting content alongside the messages they actually care about. Replacing per-app notification checking with a single morning brief eliminates distraction vectors at the source. The practitioner reports needing to check email and messages "much less" after discovering that most communications don't require urgent response — a realization made visible by having all communications laid out at once rather than arriving as interrupts.

## Why People Are Using It
Practitioner uses it daily (15+ minutes per day saved in reactive checking). The unified brief covers 4 communication channels from one document. The secondary discovery — that most messages don't require response — is a behavioral shift that wouldn't happen with per-app notification systems.

## Potential Improvements
- **Digest delivery via mobile** — a Telegram/Discord push of the brief for offline or commute reading (see: time-window-proactive-agent-loop)
- **Smart triage evolution** — the archival rules are currently manually taught; they could be learned from the user's archival history
- **Priority scoring** — not just surface vs. archive, but rank-order the surfaced items by urgency/importance
- **Cross-source correlation** — flag when an email references a calendar event or a message references a todo

## Potential Failure Modes
- API credential rotation (Gmail, Google Calendar) breaks the task silently; brief appears empty rather than failing explicitly
- Beeper's API stability is uncertain — it's an aggregator that depends on unofficial protocol access for some platforms
- Over-aggressive archival rules delete important messages; training the archival heuristics requires careful oversight early on
- Obsidian note overwrites mean the prior day's brief is lost unless the update appends vs. replaces
