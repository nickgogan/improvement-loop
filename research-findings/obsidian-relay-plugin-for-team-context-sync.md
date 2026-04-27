---
name: Obsidian Relay Plugin for Team Context Sync
summary: The Obsidian Relay community plugin syncs local vault changes across team members in real time, with per-folder sync control. Custom permission layering (read-only flags on files) enables owner-managed
  access control. Viable for teams up to 3 people on the free tier. Alternative options include GitHub sync and Obsidian Sync (paid).
implementation_notes: MetaSystem currently operates as a single-user vault. If the system expands to multi-contributor contexts, Relay is the lowest-friction team sync path. The per-folder sync granularity
  aligns with MetaSystem's system-scoped folder architecture — different systems could sync to different contributor subsets. GitHub is the natural alternative given MetaSystem is already a git repo.
category: Agentic Systems
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P3 (Monitor)
applicability:
- General
adopted_in: []
sources:
- seven-levels-context-infrastructure-ai-agents.md
proposals: []
date_discovered: '2026-04-19'
last_updated: '2026-04-19'
related_findings:
- file: context-infrastructure-seven-level-maturity-model.md
  rel: part-of
- file: obsidian-as-transparent-frontend-vs-rag-black-box.md
  rel: extends
- file: context-layer-operator-role-and-maintenance-cadence.md
  rel: same-problem
pipeline_status: synthesized
consumed_by:
  - "building-agentic-systems.md"
---
# Obsidian Relay Plugin for Team Context Sync

## What It Is
Obsidian Relay is a community plugin (Settings → Community Plugins → Browse → "relay") that provides real-time, per-folder sync of Obsidian vault changes across team members. Key characteristics:

- **Per-folder sync control**: Choose which folders sync to which team members. Not all content needs to be shared with all members.
- **Real-time propagation**: Any change any team member makes to a synced context document is immediately reflected in other team members' vaults.
- **Free tier**: Up to 3 people free.
- **Permission layering**: Native Relay does not enforce write permissions. A custom extension on top of Relay can mark files as read-only for specific members (shown as a lock icon). The Relay founder confirmed permission controls are on their roadmap.

**Sync alternatives** (in order of setup complexity):
1. GitHub (already familiar to technical teams, requires git discipline)
2. Obsidian Sync (official paid feature, simpler but no per-folder control)
3. Self-hosted sync solution
4. Relay (best balance of granularity and ease for non-technical teams)

## Why It Matters
Local-first context vaults (the second brain pattern) solve individual context management but create a forking problem for teams: each person has their own copy and updates don't propagate. Without sync, the team's collective context diverges over time. Relay closes this gap while preserving the local-first, Obsidian-native architecture. The per-folder sync granularity is important because not all team context should be universally writable — strategic docs, core ICP, and brand context should be owner-controlled.

## Why People Are Using It
Beni's team adopted Relay after evaluating GitHub and Obsidian Sync. The deciding factors were real-time sync (vs. git's commit-pull cycle) and per-folder control (vs. Obsidian Sync's vault-level granularity). The custom read-only permission layer was built on top because native Relay lacked it.

## Potential Improvements
When Relay ships native permission settings, the custom plugin workaround becomes unnecessary. A future standard may emerge around local-first context sync as the pattern becomes more common — watch for Anthropic or Obsidian-native solutions.

## Potential Failure Modes
Relay is a community plugin — subject to maintenance abandonment or breaking changes with Obsidian updates. Custom permission layers built on top of Relay create a dependency on a non-standard fork that may not receive updates. Real-time sync can propagate bad edits (hallucinated content, incorrect updates) instantly to all team members before detection. At team scale, merge conflicts on heavily-edited shared files become frequent without write discipline.
