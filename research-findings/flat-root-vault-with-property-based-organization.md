---
notion_id: 32b1e08b-9b34-812a-a4ad-d71812cd362c
name: Flat-Root Vault with Property-Based Organization
summary: Rather than nesting notes in folders by topic, all personal notes live in the vault root and are organized by YAML front-matter properties (categories, tags, date, people, rating), queried via
  Obsidian Bases smart tables. Folders only exist for attachments, templates, references, and daily notes.
implementation_notes: null
category: Agentic Systems
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
priority: Not Flagged
applicability:
- S2 (Notion Operations)
adopted_in: null
sources: []
proposals: null
date_discovered: '2026-03-22'
last_updated: '2026-04-27'
pipeline_status: synthesized
consumed_by:
  - "building-agentic-systems.md"
---
# Flat-Root Vault with Property-Based Organization

## What It Is
Stephango's vault keeps all authored notes in the root directory — no topic folders. Organization is achieved entirely through YAML metadata properties (e.g., `categories: [meetings]`, `people: [[Aisha]]`, `rating: 7`) and Obsidian Bases (database views that query those properties). A 'meetings' category note renders as a smart table listing all notes tagged with `categories: meetings`. References (external things like movies, podcasts, other people) get their own `references/` subfolder as the only meaningful folder separation.

## Why It Matters
Folder hierarchies force a premature classification decision at note-creation time — a note about a meeting with a researcher could belong under 'meetings', 'people', 'research', or 'projects'. Properties allow multi-dimensional tagging without that forced choice. This directly parallels the design challenge in AI memory systems: how to store episodic memories so they can be retrieved via multiple attributes without a rigid taxonomy.

## Why People Are Using It
The system eliminates friction during capture (no folder navigation) while keeping retrieval fast via the quick switcher (Cmd+O) and smart tables. Stephango explicitly cites 'speed and laziness' as design goals. The flat structure also means every file is equally accessible from the root, which aligns with how AI tools like Claude Code naturally traverse filesystem trees.

## Potential Alternatives
PARA method (Projects/Areas/Resources/Archives folders), Zettelkasten numeric IDs, Notion databases with relations. All involve more upfront classification overhead.

## Potential Improvements
Combining flat-root with AI-assisted property suggestion at capture time could further reduce friction. The Bases feature is still maturing; it could evolve toward more powerful relational queries.

## Potential Failure Modes
Root directory becomes visually chaotic with 1000+ notes — this is a feature for Stephango but a blocker for people who rely on visual browsing. Property discipline degrades over time if not enforced by templates.
