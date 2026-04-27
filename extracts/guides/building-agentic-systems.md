---
title: "Building Agentic Systems"
type: "guideline"
category: "Agentic Systems"
target_system:
  - "cross-system"
stage: "draft"
created: "2026-04-27"
updated: "2026-04-27"
author: "claude"
source_findings:
  - "compounding-knowledge-loop-internal-data"
  - "karpathy-llm-knowledge-base-obsidian-rag"
  - "ai-managed-vault-separate-from-human-vault"
  - "claude-code-daily-brief-multi-source-inbox-obsidian"
  - "context-infrastructure-seven-level-maturity-model"
  - "context-layer-operator-role-and-maintenance-cadence"
  - "five-pillar-agentic-os-framework"
  - "learn-plan-act-review-loop-closing-the-knowledge-gap"
  - "morning-routine-skill-active-experiment-check-in"
  - "multi-agent-proportional-content-summarization"
  - "notebooklm-mcp-claude-code-cited-knowledge-layer"
  - "obsidian-experiment-notes-personal-health-tracking"
  - "open-brain-personal-knowledge-store-pattern"
  - "org-world-model-three-architecture-patterns"
  - "progressive-adoption-path-compounding-extensions"
  - "project-onboarding-skill-multi-source-ingestion-dashboard"
  - "scheduled-tasks-for-real-time-context-maintenance"
  - "signal-capture-as-byproduct-of-work"
  - "time-window-proactive-agent-loop"
  - "claude-code-as-vault-query-engine-project-assistant"
  - "git-backed-vault-auto-commit-version-control"
  - "obsidian-as-transparent-frontend-vs-rag-black-box"
  - "obsidian-relay-plugin-for-team-context-sync"
  - "scale-threshold-heuristic-obsidian-vs-rag"
  - "bulk-youtube-ingestion-notebooklm-via-terminal"
  - "cited-health-interview-pattern-parallelized-kb-qa"
  - "composable-templates-for-lazy-capture"
  - "file-over-app-philosophy-for-knowledge-permanence"
  - "flat-root-vault-with-property-based-organization"
source_dd:
  - "DD-81"
tags:
  - "guide"
  - "agentic-systems"
  - "vault-as-os"
  - "second-brain"
  - "personal-knowledge-management"
contract:
  preconditions: "File-based vault with markdown notes; AI agent with file read/write access; Git (or equivalent) for version control."
  invariants: "Vault remains plain-text and portable across AI vendors. Human gates remain in place at every loop boundary. Capture happens as a byproduct of work, not a separate documentation act."
  governance: "Owner: the practitioner running the system, or the designated context layer operator at L6+. Updated when new architectural patterns surface in research-findings/ under category: Agentic Systems."
  recovery: "Vault corruption → git history rollback. Operator unavailability → cadence pause + L7 sync flag. Tool deprecation → vault is plain text; swap tools without data migration."
---

# Building Agentic Systems

## When to Use This Guide

You're building a system — not a prompt, not an agent, not a chatbot — where one or more AI agents serve recurring workflows on top of a persistent knowledge store you own.

Reach for this guide when:

- You want a "second brain" or "personal/business OS" that compounds over time rather than resetting each session.
- You're standing up an agent stack for yourself, a small team, or a business and need decisions about substrate, ingestion, querying, proactive loops, and operations.
- You already have a file-based vault (Obsidian or equivalent) and want to graduate it from a static notes archive into an operational layer.
- You're trying to choose between a markdown-and-files approach versus a RAG/vector-DB approach and want a defensible decision rule.

This guide does NOT cover: individual agent identity (see *Agent Design Patterns*), agent specifications (see *Writing Agent Specifications*), context management within a single agent's session (see *Managing Agent Context*), or memory architecture mechanics like decay/isolation (see *Session Persistence and Memory*).

---

## Key Concepts

Five ideas underpin every section that follows. Skip ahead if you already hold them; come back if a downstream decision feels ungrounded.

1. **The system IS the vault.** A pile of plain-text markdown files in a regular folder is the substrate. Every other capability — ingestion, querying, proactive loops, team sync — sits on top. The vault outlives the AI vendor; the AI does not own the data.

2. **Capture must be a byproduct of work, not a separate act.** Knowledge systems that demand a distinct documentation step fail to accumulate the highest-value context. The people with the most valuable knowledge are the most strategic about withholding it; even well-intentioned contributors skip when documentation is friction. Tools and workflows must produce signal as a side effect of doing the work.

3. **Compounding requires outcome encoding.** A system that records *what happened* but not *what was done about it* and *what resulted* will plateau. Month six looks like month one. Encoding outcomes — successes and failures — is the difference between a knowledge archive and a system that gets smarter with use.

4. **Maturity has two structural inflection points.** Going from L1–L2 (manual chat, fixed projects) to L3 (portable, testable skills) is the first jump. Going from L4–L5 (file access, area-bound projects) to L6 (centralized second brain) is the second. Skipping either creates fragile structure that won't carry the next level's load. Reach L6 *yourself* before attempting L7 (team OS).

5. **The operator role is structural, not optional.** At L6+, one human owns the context layer — checking duplicates, fixing misplaced files, resolving conflicts, evolving structure. Without an operator running a cadence, vaults accumulate entropy faster than they accumulate value. This is not "we'll get to it" work; it's the difference between a compounding system and a degrading one.

---

## 1. Where You Are on the Maturity Curve

Two complementary frameworks let you locate yourself and pick a next move.

### The Seven-Level Context Infrastructure Model

| Level | What it is | Primary limit |
|-------|-----------|---------------|
| **L1** | Manual chat context — copy/paste each session | No persistence |
| **L2** | Project-bound context files | Agent can't self-update; isolated chats |
| **L3** | Portable skills (`SKILL.md` + reference folder) | First inflection: static → portable + testable |
| **L4** | File access + `CLAUDE.md` routing | Context grows naturally; agent reads/writes |
| **L5** | Co-work projects pre-bound to area folders | Per-area memory and rules |
| **L6** | Centralized second brain (one vault) | Second inflection: distributed → centralized |
| **L7** | Business OS — second brain synced across team with permissions | Operator becomes a role, not just a person |

### The Five-Pillar Capability Check

Independent of level, an Agentic OS provides five capabilities. Map your current setup against them to see what's load-bearing and what's missing:

1. **Persistent memory** — layered context (operating instructions / business knowledge / agent personality / project memory). Hard ceiling: keep `CLAUDE.md`-style files small and use reference files loaded on demand.
2. **Self-improving skills** — skills + a `learnings.md` feedback loop that codifies non-negotiable rules from each use.
3. **Interaction layer** — beyond chat: a supervisor surface (kanban-style or equivalent) where business *goals* — not tasks — are tracked.
4. **Scheduled workflows** — skill chaining on cron with explicit human checkpoints. Empirically, fully autonomous chaining hits ~20% failure rates; "80% automated + checkpoint before publish" is the practitioner-validated threshold.
5. **Business context** — a foundation folder (voice, ICP, positioning, brand) referenced by every skill. "Start with the business brain, not the agents."

### Decision tree: what to build next

```
Are you at L1–L2?
  → Get to L3 first. Build one durable, testable skill. Don't skip.

Are you at L3–L4 with no centralized vault?
  → Stop adding skills. Centralize first (L6 vault).
  → Multiple area-folders without a central root will fork your context.

Are you at L6 (single-user)?
  → Audit the five pillars. Whichever is missing is the next move.
  → Don't move to L7 (team) until your personal cadence is working.

Are you at L6 considering L7?
  → Designate an operator. Define the weekly cadence. Then turn on sync.
  → Backwards order is the most common failure pattern.
```

### Compounding extensions, not flat capabilities

When extending the system (new domains, new agent skills), prefer a **progressive adoption path** over a flat capability menu. Each extension should make the next one more powerful:

- Household knowledge → home maintenance → family calendar → meal planning → professional CRM → job hunt pipeline.
- The CRM knows about thoughts captured earlier; the meal planner checks who's home this week (via calendar); job-hunt contacts become professional network contacts (via CRM).

Flat menus give flexibility but no compound effects. Compounding paths reduce decision paralysis, build skill incrementally, and surface integrations no one would have designed if extensions were built independently.

---

## 2. Choosing Your Architectural Foundations

Three substrate decisions determine almost everything downstream: file-over-app, transparency-over-RAG, and ownership separation.

### File-over-app (default, almost always)

All notes are `.md` files in a regular folder. The Obsidian (or equivalent) software reads and renders them but does not own or transform them. If the software disappears, every note is still a readable text file.

**Why this matters for AI agents:** plain-text in a filesystem is the most universally accessible format. No API, no database connector — just file I/O, which every agent framework supports natively. The vault and its accumulated memories persist across AI model transitions: disconnect Claude Code, connect a different model, continue. Vendor-hosted memory (ChatGPT memory, Claude Projects) lacks this property.

### Obsidian as transparent frontend vs RAG as black box

The trust property is asymmetric. A markdown vault is inspectable: every entry is human-readable, human-correctable, human-organizable. A vector store or graph DB is not — even visual graph-RAG is less efficient for human review than reading and editing files.

**Decision rule (the scale threshold):**

| If… | Use… |
|-----|------|
| Solo operator or small team, < ~1000 documents, primarily markdown, cost-sensitive | **File-based vault** (Obsidian, Logseq, plain Git repo) + AI file traversal |
| Thousands–millions of documents, sub-second retrieval needs, multiple concurrent users, heterogeneous content (PDFs/images/structured data) | **True RAG** (vector DB + embeddings) |

The advice from practitioners deploying this in production: *just try the simpler version*. Migration from Obsidian to RAG is non-trivial only if the wiki structure is deeply coupled to the workflow — and that coupling is usually a sign that the substrate is doing its job.

### LLM-compiled wiki vs vector DB vs structured ontology

When the vault grows past raw notes, three patterns are available for *organizing* what's in it:

1. **LLM-compiled wiki** (Karpathy pattern) — Raw sources go into a `raw/` folder. The LLM compiles index files (summaries as query entry points), concept articles, and cross-references. Query by file traversal, not vector search. Works well under ~1000 docs. Knowledge linting (gap detection, stale-data flags, broken-link repair) is a *core* pipeline stage, not optional.

2. **Vector DB / semantic retrieval** — Embed everything; agents retrieve by similarity. Fast deploy. Failure mode: never draws the information/judgment boundary. Semantic ranking *is* an interpretation, but nothing flags it as such. At small scale, humans override bad rankings; at scale, the ranking *becomes* organizational reality. Breaks at ~10K documents or when users can no longer apply independent judgment.

3. **Structured ontology** (Palantir-style) — Explicitly define domain objects, relationships, actions. AI reasons within the schema; cannot hallucinate relationships outside it. Failure mode: blind to emergent patterns. Precise within its schema, silent about what it doesn't know — and what it doesn't know may be what matters most.

A fourth pattern, **signal fidelity**, applies when the business produces a high-quality data exhaust (transactions, sensor data). Build the world model around the cleanest signal; "money is honest." Failure mode: the signal *looks* like it interprets itself, but causal inference still requires judgment the signal doesn't carry.

**Sizing guidance for organizational world models:**

| Org type | Start with |
|----------|------------|
| < 100 people, strong senior team | Vector DB — seniors supply the judgment |
| Enterprise / regulated | Structured ontology — high upfront cost; captures surprises |
| Platform with clean transactional signal | Signal fidelity — invest heavily in interpretive boundary labeling |
| Knowledge-work company (docs + conversations) | Vector DB → migrate to structured before 10K docs; build interpretive layer on top |

### AI-managed vault separate from human vault

For systems where the AI generates substantial content (summaries, entity pages, project docs), maintain **two distinct vaults**:

- **Human vault** — personal notes, hand-written thinking. AI never writes.
- **AI vault** — all AI-generated content. Human reads only.

Mixed-provenance vaults (humans editing AI-written areas) are the most common quality-degradation pattern. Strict separation enforces clean ownership and makes trust verification possible (the human can read the AI vault to see what the AI knows).

For *organizational* knowledge with shared editing, this separation is harder to enforce — use Git history + version control as a fallback audit trail (every edit is attributable).

### The middle-ground knowledge store

For multi-agent systems where context needs to travel across agent boundaries (one agent learns; another needs to know), consider a **lightweight MCP-accessible knowledge store** between flat memory files and full RAG. Costs ~10¢/month at small scale; structured enough to be searchable; cheap enough to maintain casually. This is the "Open Brain" pattern: any MCP-speaking agent can read or write, so context accumulated in one role is retrievable by another without re-provisioning.

---

## 3. Setting Up the Storage Substrate

Three structural decisions when you stand up the vault itself.

### Flat root + property-based organization

Avoid deep folder hierarchies. Folder paths force premature classification — a meeting note about a researcher could go under `meetings/`, `people/`, `research/`, or `projects/`. YAML frontmatter properties (`categories: [meetings]`, `people: [[Aisha]]`, `rating: 7`) allow multi-dimensional tagging without that forced choice.

Use folders only for: attachments, templates, references (external entities like books/movies/companies), and daily notes. Everything else lives in the root, queryable by smart-table views over frontmatter properties.

This parallels a deep design choice in agent memory: how to store episodic memories so they retrieve via multiple attributes without a rigid taxonomy. Flat-with-properties is the file-system answer.

### Composable templates for lazy capture

For each note type (meeting, person, book, quote, project, experiment, evergreen), maintain a dedicated template that pre-populates frontmatter. Templates are designed to be *composable* — a note can apply both `person` and `author` templates without overlap because their property sets are non-conflicting.

This makes downstream querying reliable: agents can filter by structured properties rather than parse free text. It also reduces cognitive overhead at capture time, which is the only reliable way to keep capture-volume high.

### Git-backed vault with auto-commit

Make the vault root a private GitHub repo. Open the clone as the vault. Install the auto-commit plugin (e.g., Obsidian Git): commit after a short idle period (1 minute), pull on startup. Result: free version control, off-device backup on every save, full diff history for rollback, and an *audit trail when AI is also editing files* — Claude's edits and yours are indistinguishable in the filesystem otherwise.

Before giving an AI write access to your knowledge base, you need a recovery mechanism. Git is that. Auto-commit closes the discipline gap.

### Template — Vault scaffolding

```
{{VAULT_ROOT}}/
├── .git/                          # version control (auto-commit)
├── CLAUDE.md                      # routing layer for the AI
├── _schema.yaml                   # frontmatter conventions for all notes
├── README.md                      # human onboarding
│
├── attachments/                   # images, PDFs, binary files
├── templates/                     # one per note type
│   ├── meeting.md
│   ├── person.md
│   ├── project.md
│   ├── experiment.md
│   └── evergreen.md
├── references/                    # external entities (books, movies, people-not-you-know)
├── daily/                         # daily notes (one per day)
│
└── (flat root)                    # all authored notes live here
    ├── {{notes by property, queried via smart tables}}
    └── ...
```

| Variable | Type | Description | Required |
|----------|------|-------------|----------|
| `{{VAULT_ROOT}}` | path | Absolute path to vault. Should be a git working tree. | yes |

### Worked example — MetaSystem itself

MetaSystem uses this scaffold at L6/L7. The root is a git repo. `CLAUDE.md` is the routing layer; `_schema.yaml` defines frontmatter; system-scoped folders (`systems/`, `incubator/`) carry the fractal-unit pattern. Governance documents (DDs, IB items, System Log) live in system-scoped subfolders rather than a root catalog. Templates live under `systems/meta-system/knowledge/templates/`. The vault is consumed by Claude Code via file traversal — no vector DB, no embeddings.

---

## 4. Feeding the System (Ingestion)

Six patterns cover the ingestion surface area, anchored by one design principle.

### The signal-as-byproduct principle

A knowledge system only compounds if **signal capture is a byproduct of doing the work** — not a separate documentation step. If feeding the system requires extra effort, two failure modes follow:

- *Strategic withholding* — people with the most valuable context are the most strategic about not feeding a system that erodes their information advantage.
- *Benign forgetfulness* — even well-intentioned contributors skip documentation under time pressure.

The result is a system that accumulates low-stakes, easy-to-document information and *misses* the judgment-rich context that would make it useful.

**Design implication**: prefer commit messages over documentation files, ticket updates over status emails, structured decisions made in-system over decisions made elsewhere and pasted in. Tool integrations should produce signal as side effects of normal work — auto-logging, hook-based capture, byproduct artifacts.

### Bulk ingestion of source corpora

For standing up an expert knowledge base from a YouTube channel, a Substack archive, or a podcast back-catalog: use Claude Code (or equivalent) to bulk-fetch the source list, present for collaborative filtering, and bulk-upload to NotebookLM or your KB layer. Practitioners report ~200 sources ingested in a single session, replacing hours of manual link-by-link work.

Critical: keep the human in control of *what* enters the KB. Show the candidate list, take a selection, then ingest. Blindly ingesting "everything" creates noise that will degrade every downstream query.

### Long-form content summarization with sub-agents

For 2–3 hour podcasts, books, or papers that won't fit in a single context window:

1. Download transcript (or Whisper-transcribe).
2. Chunk for sub-agent context windows.
3. Sub-agents summarize chunks in parallel.
4. Orchestrator assembles into a structured note: TLDR callout, timestamped topic index, key quotes, mentioned-people/concepts/tools sections.
5. Each mentioned entity gets a stub page — entity references accumulate cross-links over time.

**Proportionality rule**: summary depth scales with content length. 15-minute video → concise overview; 500-page book → 15–20 minute read. The entity-page pattern is what differentiates this from flat summarization — it converts isolated artifacts into a growing interconnected knowledge base.

### Project intake skill

For project-shaped work (client engagements, research projects, sales pipelines, job searches), build a one-command intake skill:

1. Prompt for project name; check for existence (update path) or create new.
2. Collect from multiple sources — email thread/label, local files (PDF/DOCX/images), pasted text/screenshots.
3. Filter static documents (contracts, NDAs) from conversational content.
4. Create a standardized folder: `overview.md`, `conversation-log.md`, `links.md`, `documents/`, plus an entry in a `projects.base` (table tracking all projects + status).
5. Generate an import summary.

The skill encodes the *taxonomy* of project knowledge (status, conversations, documents, contacts), not just the raw data. After intake, an agent can answer "what's the status of project X and what should I do next?" by reading the folder.

### Daily multi-source brief

For replacing reactive notification-checking with a single intentional read: build a scheduled task that aggregates Gmail + Calendar + messaging (Beeper or equivalent) + tasks (Things, Todoist, etc.) into one Obsidian note each morning. Add inbox triage — rule-trained auto-archive of cold outreach and spam. The brief is overwritten daily (not appended); the human reads, checks off, moves on.

The secondary discovery practitioners report is behavioral: when all communications are laid out at once rather than arriving as interrupts, *most don't require urgent response*. The brief makes that visible.

### Scheduled tasks for real-time context maintenance

A second brain seeded with static context (ICP, brand, strategy docs) becomes a historical snapshot as the business evolves. Recurring scheduled agent tasks close the gap:

- Meeting transcript ingestion (Firefly or equivalent → structured vault folder)
- Team task rollup (daily scan, summarized, filed)
- Analytics updates (CRM pipeline, key metrics)
- A morning *synthesis* task that reads current priorities, to-do state, and recent updates, producing a daily prioritized overview

Goal: keep the gap between "what the vault knows" and "what is happening" under 24 hours.

### Template — Daily brief skill

```yaml
# {{SKILL_NAME}}.md
---
name: {{SKILL_NAME}}
description: {{ONE_LINE_PURPOSE}}
schedule: {{CRON_EXPRESSION}}
---

# Procedure
1. Pull from sources: {{SOURCE_LIST}}
2. Apply triage rules: {{TRIAGE_RULES}}
3. Compose the brief in this shape:
   - Calendar
   - Weather (optional)
   - Email (actionable only)
   - Messages (requiring response)
   - Tasks (today)
4. Write to: {{OUTPUT_PATH}}
5. (Optional) Push to: {{NOTIFICATION_CHANNEL}}

# Rules
- Output is one persistent note (overwrite daily, do NOT create new file per day).
- Silence is better than noise. Suppress empty sections.
- Failure modes: API credential rotation; Beeper API instability; over-aggressive archival.
```

| Variable | Type | Description | Required |
|----------|------|-------------|----------|
| `{{SKILL_NAME}}` | string | Skill identifier (kebab-case) | yes |
| `{{ONE_LINE_PURPOSE}}` | string | What this brief is for | yes |
| `{{CRON_EXPRESSION}}` | string | Schedule (e.g., `0 7 * * *` for 7am daily) | yes |
| `{{SOURCE_LIST}}` | list | Integrations: Gmail, Calendar, Beeper, Things, etc. | yes |
| `{{TRIAGE_RULES}}` | text | Rule-trained archival heuristics | yes |
| `{{OUTPUT_PATH}}` | path | Vault path for the brief note | yes |
| `{{NOTIFICATION_CHANNEL}}` | string | Telegram/Discord channel ID for mobile push | optional |

---

## 5. Querying the System

Three patterns cover the query surface, ordered by sophistication.

### The vault as query engine

After data is structured in the vault, the AI agent (Claude Code or equivalent) becomes the interactive query layer. Workflow:

- *Status queries* — "What is the status of project X?" → agent reads the folder, synthesizes.
- *Action item generation* — "What should I do next on X?" → agent reads conversation log, identifies open threads, prioritizes.
- *Draft generation* — "Help me reply to the client" → agent reads context, drafts.
- *Cross-project synthesis* — "Which projects need attention this week?" → agent scans the index/base table.

This pattern requires no infrastructure beyond the vault and a file-reading agent. The constraint: the vault must be *current*. Stale conversation logs produce confidently-wrong answers.

### NotebookLM (or equivalent) as a cited knowledge layer

For external knowledge — domain expertise (Huberman health, Lenny PM, etc.) you don't author yourself — connect a citation-grounded KB tool via MCP:

- List notebooks programmatically.
- Query any notebook in natural language; receive citation-tagged answers.
- Run multiple queries in parallel (e.g., 6 sub-agents querying 6 dimensions simultaneously).
- Save responses *with citations* directly to the vault.

The key property is **citation traceability** — every recommendation traces to a specific source (timestamp in a video, section in a doc). Built-in citation verification: have the agent score citation quality; surface low-confidence matches.

This is the integration layer that turns NotebookLM from a chat tool into a queryable knowledge API.

### Parallelized KB Q&A for personalized output

Combining the vault and the cited KB layer enables a powerful pattern: turn an expert KB into a *personalized protocol*.

**Phase 1 — Expert interview (parallel):**
- Spawn N sub-agents, each querying the KB on a different dimension (sleep, exercise, nutrition, stress, etc. — or whatever decomposition fits the domain).
- Each returns a question + citation-grounded answer.
- Save results to vault as individual Q&A notes plus a dashboard.

**Phase 2 — Personal gap assessment:**
- The user answers the interview questions in natural language.
- The agent reads existing data from the vault ("go grab my fitness data") to enrich the assessment.
- Output: current-state vs target-state gap with priority ratings.
- Top-priority gaps become candidate experiments with explicit hypotheses, protocols, and measurable success criteria.

This pattern bridges two gaps: *coverage* (one question gives a generic answer; six dimension-specific questions give comprehensive coverage) and *personalization* (generic expert advice + your actual current state = a prioritized protocol).

---

## 6. Proactive Agent Loops

The system stops being reactive and starts acting on its own behalf. Five patterns cover the proactive surface.

### Time-window proactive loop (the canonical structure)

A scheduled agent that runs a time-aware decision loop:

```
0. Date anchor       — establish exact date/time. Store as anchor_date / anchor_time.
                       All date arithmetic is calculated from this. Never use vague terms ("recently").
1. Time check        — classify into a window (early morning / pre-meeting / midday / evening / late).
2. Duplicate check   — query the briefings table; don't repeat what's already been sent today.
3. Decide            — based on window, what should be delivered?
4. External pull     — fetch live data (calendar, weather, attendees).
5. Internal enrich   — search vault for context on what was just pulled.
                       (External BEFORE internal — can't enrich what you haven't seen.)
6. Deliver           — channel tools (Telegram/Discord). Concise, mobile-friendly. Silence > noise.
7. Log               — record what was sent. Next cycle reads this.
```

Seven briefing types in the OB1 reference implementation: morning, pre_meeting, checkin, evening, habit_reminder, weekly_review, custom. Five time windows.

### Morning routine skill

The bridge from "experiments designed" to "experiments tracked": a `daily` skill that runs at session start and:

1. **Goal check** — read goals file from vault; surface current goals.
2. **Experiment discovery** — scan for `type: experiment` and `status: in_progress`; list.
3. **Observation collection** — for each active experiment, ask a targeted question. ("How is the morning sunlight experiment going? What was your wake-up time?")
4. **Data logging** — write responses to the experiment note's observation section; update numeric tracking fields (mood 1–10, energy 1–10, sleep, gym sessions, etc.).
5. **Next-action scheduling** — based on observations, suggest or schedule the day's actions.

The skill reads live from the vault, so adding a new experiment automatically adds it to the morning check-in. The user shows up and answers; structured logging is automatic.

### Learn-Plan-Act-Review (the closure loop)

Most people consume expert knowledge but never translate it into changed behavior. The loop forces closure:

1. **Learn** — ingest expert content into a citation-grounded KB.
2. **Plan** — run a cited interview against the KB; conduct a personal gap assessment; identify highest-leverage experiments.
3. **Act** — design experiments with explicit hypotheses + success criteria; schedule calendar events; embed into the morning routine skill.
4. **Review** — daily morning check-in captures observations; data logs to structured experiment notes; a dashboard surfaces progress.

The pattern's leverage is that it inverts the discipline requirement. Instead of you remembering to check experiments, the agent asks every morning. You only show up and answer.

### Experiment notes as a personal data layer

For longitudinal personal tracking, structure experiments as Obsidian markdown files:

- **Frontmatter**: `type: experiment`, `status: in_progress | proposed | complete`, dashboard link.
- **Body sections**: Hypothesis (explicit), Protocol (step-by-step), Success Criteria (measurable, e.g., "80% of days within 30min of target wake-up time"), Observations (filled daily).
- **Numeric fields**: Tracked metrics (mood, energy, sleep quality, gym volume).
- **Dashboard link**: aggregator note showing all active experiments + plotted data.

The vault *is* the database. No schema migration; no API; no special memory mechanism. A new agent session picks up exactly where the last one ended by reading the experiment files.

### The compounding knowledge loop (with outcome encoding)

The fully self-reinforcing pattern: agent answers question → synthesizes across wiki → answer filed in session log → log eventually promoted to wiki → wiki grows → future queries get better answers. The loop runs automatically via session hooks (`session_start`, `pre_compact`, `session_end`) plus a daily flush.

**The non-negotiable invariant: encode outcomes, not just events.** A loop that records what happened but not *what was done about it* and *what resulted* will plateau. Most implementations skip outcome encoding, which is why compounding fails to materialize in practice. This requires organizational readiness — willingness to record results honestly, including failures.

### Template — Time-window proactive loop

```yaml
# {{LOOP_NAME}}-loop.md
---
name: {{LOOP_NAME}}
schedule: {{CRON_EXPRESSION}}
---

# Loop
0. Date anchor:        date_now = $(date)
1. Time window:        window = classify(date_now, {{TIME_WINDOWS}})
2. Duplicate check:    if window in briefings_table[date_now]: return
3. Decide:             briefing_type = {{WINDOW_TO_TYPE_MAP}}[window]
4. External pull:      pull_data = {{EXTERNAL_SOURCES}}
5. Internal enrich:    context = vault.search(pull_data.entities)
6. Deliver:            {{CHANNEL}}.send(compose(briefing_type, pull_data, context))
7. Log:                briefings_table.append(date_now, window, briefing_type)
```

| Variable | Type | Description | Required |
|----------|------|-------------|----------|
| `{{LOOP_NAME}}` | string | Loop identifier | yes |
| `{{CRON_EXPRESSION}}` | string | Schedule (frequent enough to hit each time window) | yes |
| `{{TIME_WINDOWS}}` | list | Named windows (e.g., `[early_morning, pre_meeting, midday, evening, late]`) | yes |
| `{{WINDOW_TO_TYPE_MAP}}` | dict | Maps each window to a briefing type | yes |
| `{{EXTERNAL_SOURCES}}` | list | Calendar, weather, news, etc. | yes |
| `{{CHANNEL}}` | string | Delivery channel: Telegram, Discord, Slack, vault-only | yes |

### Worked example — Fitness Learn-Plan-Act-Review loop

**Learn**: Bulk-ingested 200 Huberman Lab episodes into a NotebookLM notebook via the bulk-YouTube skill.

**Plan**: Spawned 6 parallel Claude Code sub-agents querying the notebook on sleep, exercise, supplements, stress, light exposure, and biomarkers. Each returned a citation-grounded Q&A. The user answered each question; the agent compared answers against existing fitness data already in the vault. Output: a current-state-vs-target gap assessment ranking top 3 experiments by leverage.

**Act**: For each top experiment, the agent created an experiment note (`type: experiment`, `status: in_progress`, hypothesis, protocol, success criterion). Calendar events were scheduled for time-bound protocol steps (e.g., "morning sunlight 7–10am for 14 days"). The morning routine skill auto-detected the new experiments because it scans for `status: in_progress`.

**Review**: Each morning, the routine skill asked targeted questions per experiment, wrote responses to the observation section, updated numeric tracking. After 14 days, the dashboard showed the experiment closed (success criterion met) or rolled forward (hypothesis revised).

---

## 7. Operating Long-Term

Two roles, one cadence, one sync model.

### The context layer operator

At L6+, designate one human as **the context operator**. The role covers:

1. **Weekly vault review** — duplicates, misplaced files, conflicting context (two files with contradictory ICP definitions).
2. **Quality assurance** — scheduled-task output landing correctly (not generating noise).
3. **Structural evolution** — updating `CLAUDE.md` routing and per-subfolder index files as the vault grows.
4. **Permission management** (L7 only) — controlling write access per folder via the team-sync layer.
5. **Onboarding new contributors** — sharing the vault, establishing contribution norms.

The role is informal in single-user setups (you are the operator). It must be **explicitly designated** at L7 — diffused accountability is the most reliable path to vault degradation. When context quality is good, agents perform well; when it degrades, there is a single responsible party rather than a team-wide diagnosis.

### Team sync (L7)

Local-first vaults solve individual context but create a forking problem for teams: each person has a copy; updates don't propagate. Three sync paths, ordered by setup complexity:

| Path | Pros | Cons |
|------|------|------|
| GitHub (with discipline) | Already in place if technical; full audit trail | Commit/pull cycle, not real-time; merge conflicts |
| Obsidian Sync (paid) | Simplest setup | No per-folder granularity; vendor-locked |
| **Relay** (community plugin) | Real-time, per-folder sync; free under 3 users | Community plugin (maintenance risk); no native write permissions yet |
| Self-hosted | Maximum control | Maximum operator overhead |

For mixed-permission needs (strategic docs read-only, working folders writable), Relay's per-folder sync + a custom read-only permission layer is the lowest-friction path today. Native permission settings are on Relay's roadmap.

### Maintenance cadence

The cadence is the difference between a compounding system and a degrading one. Concrete weekly checklist:

- [ ] Vault health: duplicate-finder report (any file ≥80% similar to another).
- [ ] Misplaced files: anything in the root that should be in `references/`, `attachments/`, or a system-scoped folder.
- [ ] Conflicting context: documents that contradict each other (esp. ICP, brand, governance).
- [ ] Scheduled-task output spot-check: are recurring tasks writing the right things to the right places?
- [ ] Stale entries: anything with `last_updated > N days` that should be current.
- [ ] Routing drift: does `CLAUDE.md` still reflect actual structure?

Track a **context health score** over time — number of issues found per cadence run. A rising score is the leading indicator of structural strain.

### Template — Operator weekly cadence

```markdown
# Vault Health — Week of {{WEEK_OF}}

**Operator:** {{OPERATOR}}
**Vault:** {{VAULT_PATH}}
**Health score:** {{ISSUE_COUNT}} (Δ from last week: {{DELTA}})

## Findings
- Duplicates: {{DUPLICATE_COUNT}}
- Misplaced files: {{MISPLACED_COUNT}}
- Conflicting documents: {{CONFLICT_COUNT}}
- Scheduled-task issues: {{TASK_ISSUES}}
- Stale entries: {{STALE_COUNT}}

## Actions taken
{{ACTIONS}}

## Carried forward
{{CARRIED}}
```

---

## Pitfalls

Synthesized failure modes from across the cluster. Every one of these has been observed in production by at least one practitioner.

### Compounding failures

- **No outcome encoding** — System records events but not results. Compounding never materializes; month six looks like month one.
- **Garbage-in-garbage-out** — Compounding loop runs at low session quality. Wiki bloat without value. Add quality gates before promotion.
- **Static seed corpus** — Knowledge store seeded once and never refreshed. Becomes a historical snapshot disguised as current truth.

### Capture failures

- **Active documentation requirement** — The system demands a separate documentation step. The most valuable context (judgment-rich, high-stakes) is the most likely to be withheld.
- **Passive-capture noise** — Over-correcting toward passive capture floods the vault with low-signal data. Quantity ≠ quality.
- **Ingestion noise** — Meeting transcripts (small talk, off-topic) ingested without filtering. Pollutes vault.

### Architecture failures

- **Premature RAG migration** — Building vector DB infrastructure for < 1000 documents. Significant overhead for negligible gain.
- **Stuck-on-Obsidian** — Refusing to migrate when documents > 10K and queries are slow. Some teams stay too long; the threshold is fuzzy on the upside.
- **Mixed-provenance vaults** — Humans editing AI-written areas (or vice versa). Most common quality-degradation pattern.
- **Architecture-by-deployment-speed** — Picking the fastest-to-deploy architecture (vector DB) without org-size and risk-profile inputs.

### Operations failures

- **Informal operator role** — Cadence skipped when the operator is busy. Vault drift accumulates invisibly until output quality drops perceptibly.
- **Single-operator bottleneck (L7)** — One operator, no succession plan. Vault quality depends on one person's availability.
- **L7 before L6** — Team sync turned on before personal cadence is working. Synchronization complexity multiplies before context quality is established.
- **Routing drift** — `CLAUDE.md` not updated as vault grows. Agent traverses to dead paths.

### Proactive-loop failures

- **Notification fatigue** — Proactive agents that talk too much get muted. Silence > noise.
- **Date anchor drift** — System clock wrong; all time-window logic fails silently.
- **State table corruption** — Briefings log is the deduplication mechanism; corruption produces repeated messages.
- **Experiment overload** — Too many active experiments; morning check-in feels like work; observation quality degrades.

### Skill / vault failures

- **Hardcoded vault paths** — Skill references vault path explicitly; vault reorganization breaks the skill.
- **Inconsistent frontmatter** — Field naming drifts across templates; agent reads break. Enforce templates.
- **Template proliferation** — Too many templates → choice paralysis → defeats the laziness goal.
- **Race conditions** — Auto-commit + AI commits + human commits without coordination. Use proper Git discipline; one writer at a time per session.

---

## Contract

### Preconditions
- File-based vault with markdown notes (Obsidian, Logseq, plain Git repo, or equivalent).
- AI agent with file read/write access (Claude Code, or any agent that supports file I/O).
- Git or equivalent version control on the vault root.
- A designated context operator (you, at single-user; explicit role at L7).

### Invariants
- The vault remains plain text and portable across AI vendors.
- Human gates remain at every action loop boundary (no fully-autonomous chains in production).
- Capture happens as a byproduct of work, not a separate documentation act.
- Compounding loops encode outcomes, not just events.
- The maintenance cadence runs.

### Governance
- **Owner** — the practitioner running the system; or, at L6+, the designated context layer operator.
- **Updated when** — new architectural patterns surface in `research-findings/` under `category: Agentic Systems`; new sub-patterns graduate; failure modes accumulate enough to warrant an addition to *Pitfalls*.
- **Source** — Improvement Loop research, Dimension 11 (Agentic Systems). Findings under that dimension are the ground-truth corpus.

### Recovery
- **Vault corruption** → git history rollback. Auto-commit means the worst-case loss is the configured idle interval (≤1 minute on typical setups).
- **Operator unavailability** → cadence pause; flag at L7. Designate a backup before the operator becomes unreachable.
- **Tool deprecation** (Obsidian, Claude Code, NotebookLM, Beeper) → vault is plain text; swap tools without data migration. Skills referencing the deprecated tool are the only thing that needs rewriting.
- **AI vendor change** → disconnect the current AI; connect a different one. The vault is the persistence layer, not the AI.
- **Compounding loop drift** (wiki contradicts itself; quality degrades) → run a vault audit; surface conflicts; resolve via operator cadence; consider knowledge-linting pipeline (gap detection, stale-data flags, broken-link repair) as a recurring task.

---

## Related Guides

- **[[managing-agent-context]]** (G2) — context-engineering primitives that this guide assumes (`CLAUDE.md` size limits, reference files loaded on demand, context rot mitigations).
- **[[session-persistence-and-memory]]** (G7) — memory architecture mechanics underneath the vault-as-OS pattern. Several findings (open-brain, ai-managed-vault, signal-capture, compounding-knowledge-loop, org-world-model) appear in both guides; G7 covers the substrate-level memory questions, G11 covers the system-shape questions.
- **[[agent-workflow-and-execution]]** (G3b) — operational mechanics for scheduled tasks, durable workflows, observability. Section 4 (Ingestion) and Section 6 (Proactive Loops) sit on top of G3b's primitives.
- **[[designing-agent-tools]]** (G5) — MCP integration patterns referenced in Section 5 (Querying) live here in detail.
- **[[agent-governance-and-trust]]** (G9) — human-gate placement and review workflows that apply to the proactive-loop checkpoint discipline in Section 6.
