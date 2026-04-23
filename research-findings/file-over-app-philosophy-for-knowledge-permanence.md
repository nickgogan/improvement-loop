---
notion_id: 32b1e08b-9b34-815d-b78b-d50fcc6ef084
name: File-Over-App Philosophy for Knowledge Permanence
summary: Storing all notes as plain-text markdown files in a local folder — not in a proprietary database — ensures knowledge persists independently of any software, application, or service. This is a deliberate
  architectural constraint that prioritizes longevity and portability.
implementation_notes: null
category: Agentic Systems
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
priority: P3
applicability:
- S2 (Notion Operations)
adopted_in: null
sources:
- claude-code-for-life-daily-briefs-obsidian-memory.md
proposals: null
date_discovered: '2026-03-22'
last_updated: '2026-04-20'
related_findings:
- file: ace-agentic-context-engineering-rag-based.md
  rel: contradicts
pipeline_status: raw
consumed_by: []
---
# File-Over-App Philosophy for Knowledge Permanence

## What It Is
Stephango's first design pillar: all notes are `.md` files in a regular folder. No proprietary database, no cloud lock-in. The Obsidian software reads and renders these files but does not own or transform them. If Obsidian ceased to exist, every note is still a readable text file. This also means the folder is accessible to any tool — including CLI-based AI agents, git version control, grep/search utilities, and file-sync tools.

## Why It Matters
For AI agent workflows that need to read, write, and maintain a knowledge base over time, plain-text files in a filesystem are the most universally accessible and AI-readable format. They don't require special API calls or database connectors — just file I/O, which every agent framework supports natively.

## Why People Are Using It
Protects against software deprecation, data migration nightmares, and vendor lock-in. Also makes the knowledge base trivially accessible to AI tools (Claude Code, grep, etc.) without building integrations.

A second practitioner explicitly articulates the model-agnostic portability rationale: by having Claude Code write exclusively to an Obsidian vault (markdown files on local disk), the user can "disconnect Claude Code and connect this Obsidian vault to a different AI model and continue our workflow." The vault and its accumulated memories persist across AI model transitions — something impossible with vendor-hosted memory systems (ChatGPT memory, Claude Projects). This frames file-over-app not just as a longevity pattern but as an AI vendor independence strategy.

## Potential Alternatives
Notion (proprietary database), Roam Research (proprietary format), Obsidian Sync (cloud), SQLite databases. All involve some form of lock-in or additional access complexity.

## Potential Improvements
Version controlling the markdown files with git adds history and branching to the knowledge base. AI-generated summaries or indexes (themselves stored as markdown) could improve discoverability at scale.

## Potential Failure Modes
Large attachments (images, PDFs) still require external storage. Very large vaults (10k+ files) may have filesystem performance issues without indexing. Conflict resolution during multi-device sync is non-trivial.
