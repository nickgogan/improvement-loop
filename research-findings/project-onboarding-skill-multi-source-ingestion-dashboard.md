---
name: Project Onboarding Skill — Multi-Source Ingestion into Structured Dashboard
summary: A Claude Code skill that ingests Gmail threads and local files for a project, then creates a standardized Obsidian project folder with overview, conversation log, links, and documents sections. Converts ad-hoc data collection into a repeatable, one-command project intake workflow.
implementation_notes: Directly applicable to MetaSystem. The IL pipeline already stages findings from multiple sources; the same "collect → organize → structure" pattern could apply to any project-level intake. The Gmail OAuth integration is a dependency.
category: Agentic Systems
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources:
- claude-code-obsidian-second-brain-project-onboarding.md
related_findings:
- file: project-specific-custom-skills-for-repeated-task.md
  rel: same-problem
- file: dual-ingestion-funnel-human-clip-plus-llm-research.md
  rel: same-problem
- file: obsidian-as-transparent-frontend-vs-rag-black-box.md
  rel: extends
proposals: null
date_discovered: '2026-04-19'
last_updated: '2026-04-19'
pipeline_status: synthesized
consumed_by:
  - "building-agentic-systems.md"
---
# Project Onboarding Skill — Multi-Source Ingestion into Structured Dashboard

## What It Is
A custom Claude Code skill called `onboard-projects` that automates the creation of a standardized project folder in Obsidian. The skill:

1. **Prompts for project name** — checks if the project already exists (update path) or creates new
2. **Collects from multiple sources** — Gmail label (all emails in a thread), local files (PDF, DOCX, images), and pasted text/screenshots
3. **Processes and classifies content** — filters static documents (contracts, agreements) from conversational content (emails, notes), extracts profile metadata (industry, contacts, scope, tech stack)
4. **Creates structured folder**:
   - `overview.md` — project description, scope, profile extracted from all sources
   - `conversation-log.md` — chronological summary of all communication events
   - `links.md` — external references
   - `documents/` — static files that should not be summarized (NDAs, contracts)
   - Entry in `projects.base` — a table tracking all projects and statuses
5. **Generates import summary** — what was imported, timeline, key stats

The skill uses Obsidian CLI commands (markdown, base, canvas, JSON) and custom Python scripts for Gmail OAuth2 authentication and thread fetching. Credentials are stored in `.gmail-credentials/` and referenced from `.env`.

## Why It Matters
Project management involves juggling context from many sources: emails, agreements, notes, status updates. Without a system, this context lives scattered across inboxes, local folders, and memory. The onboarding skill is a one-command intake: run it once when a project starts, and all context is organized into a queryable Obsidian structure that Claude Code can then query for status, draft responses, or generate action items.

The structured output enables Claude Code to act as an ongoing project assistant — "what's the status of project X and what should I do next?" becomes answerable by querying the vault, not by manually reviewing emails.

## Why People Are Using It
Eric demonstrates this for managing client freelance projects. The pattern generalizes: any recurring context management problem (research projects, job searches, sales pipelines, collaborative projects) benefits from the same structure. The key insight is that the skill encodes the *taxonomy* of project knowledge (status, conversations, documents, contacts) not just the raw data.

## Potential Alternatives
Manual folder creation. Notion databases for project management (requires context switching out of the vault). Generic project management tools (Asana, Linear) — these lack Claude Code query integration. Memory Bank pattern (agent-maintained memory files) — less structured but more flexible.

## Potential Improvements
Add deduplication logic when re-running on an existing project (detect if an email thread was already ingested). Support Slack thread ingestion alongside Gmail. Auto-update the `projects.base` dashboard when the conversation log is updated. Add a "project close" command that archives the folder and writes a summary.

## Potential Failure Modes
Gmail OAuth setup is a significant friction point — requires Google Cloud Console access, enabling the Gmail API, creating OAuth credentials, and saving JSON files. Credential rotation adds ongoing maintenance. The skill is brittle to inbox structure changes (label names, thread format). Summarization of long email threads can lose important detail — the chronological log may omit key decisions buried in the thread.
