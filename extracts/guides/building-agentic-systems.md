---
title: "Building Agentic Systems"
type: "guideline"
category: "Agentic Systems"
target_system:
  - "cross-system"
stage: "draft"
created: "2026-04-27"
updated: "2026-05-25"
author: "claude"
source_findings:
  - "ai-delegated-knowledge-organization"
  - "ai-managed-vault-separate-from-human-vault"
  - "ai-shepherding-anti-pattern-manual-workflow-sequencing"
  - "claude-code-daily-brief-multi-source-inbox-obsidian"
  - "coding-agent-sdk-as-non-coding-agent-foundation"
  - "compounding-knowledge-loop-internal-data"
  - "context-assembly-cost-as-strategy-blocker"
  - "context-first-build-sequencing-for-agentic-systems"
  - "context-infrastructure-seven-level-maturity-model"
  - "context-layer-operator-role-and-maintenance-cadence"
  - "five-layer-recursive-ai-loop-architecture"
  - "five-pillar-agentic-os-framework"
  - "implementation-is-strategy-for-agentic-systems"
  - "karpathy-llm-knowledge-base-obsidian-rag"
  - "learn-plan-act-review-loop-closing-the-knowledge-gap"
  - "monitoring-agent-failure-detection-autonomous-repair"
  - "morning-routine-skill-active-experiment-check-in"
  - "multi-agent-proportional-content-summarization"
  - "notebooklm-mcp-claude-code-cited-knowledge-layer"
  - "obsidian-as-transparent-frontend-vs-rag-black-box"
  - "obsidian-experiment-notes-personal-health-tracking"
  - "open-brain-personal-knowledge-store-pattern"
  - "org-world-model-three-architecture-patterns"
  - "pr-acceptance-rate-harness-multiplier-evidence"
  - "progressive-adoption-path-compounding-extensions"
  - "project-onboarding-skill-multi-source-ingestion-dashboard"
  - "scheduled-tasks-for-real-time-context-maintenance"
  - "sdk-to-framework-graduation-path"
  - "signal-capture-as-byproduct-of-work"
  - "time-window-proactive-agent-loop"
source_dd:
  - "DD-81"
tags:
  - "guide"
  - "agentic-systems"
  - "vault-as-os"
  - "second-brain"
  - "personal-knowledge-management"
contract:
  preconditions: "File-based vault with markdown notes; AI agent with file read/write access; Git (or equivalent) for version control; a designated context operator (you, at single-user; explicit role at L7)."
  invariants: "Vault remains plain-text and portable across AI vendors. Human gates remain in place at every loop boundary. Capture happens as a byproduct of work, not a separate documentation act. Implementation feasibility is assessed before strategic commitment."
  governance: "Owner: the practitioner running the system, or the designated context layer operator at L6+. Updated when new architectural patterns surface in research-findings/ under category: Agentic Systems."
  recovery: "Vault corruption -> git history rollback. Operator unavailability -> cadence pause + L7 sync flag. Tool deprecation -> vault is plain text; swap tools without data migration. SDK lock-in -> skills and MCP servers port to framework; agent loop rebuilds."
---

# Building Agentic Systems

## When to Use This Guide

You are building a system -- not a prompt, not an agent, not a chatbot -- where one or more AI agents serve recurring workflows on top of a persistent knowledge store you own.

Reach for this guide when:

- You want a "second brain" or "personal/business OS" that compounds over time rather than resetting each session.
- You are standing up an agent stack for yourself, a small team, or a business and need decisions about substrate, ingestion, querying, proactive loops, and operations.
- You already have a file-based vault (Obsidian or equivalent) and want to graduate it from a static notes archive into an operational layer.
- You need to decide between a markdown-and-files approach versus a RAG/vector-DB approach and want a defensible decision rule.
- You are choosing between an SDK-based prototype and a framework-based production build and want a graduation path.

This guide does NOT cover: individual agent identity (see *Agent Design Patterns*), agent specifications (see *Writing Agent Specifications*), context management within a single agent's session (see *Managing Agent Context*), or tool integration mechanics (see *Designing Agent Tools*).

---

## Key Concepts

Seven ideas underpin every section that follows. Skip ahead if you already hold them; come back if a downstream decision feels ungrounded.

1. **The system IS the vault.** Plain-text markdown files in a regular folder are the substrate. Every other capability -- ingestion, querying, proactive loops, team sync -- sits on top. The vault outlives the AI vendor; the AI does not own the data.

2. **Capture must be a byproduct of work, not a separate act.** Knowledge systems that demand a distinct documentation step fail to accumulate the highest-value context. People with the most valuable knowledge are strategic about withholding it; even well-intentioned contributors skip documentation under time pressure. Tools and workflows must produce signal as a side effect of doing the work.

3. **Compounding requires outcome encoding.** A system that records *what happened* but not *what was done about it* and *what resulted* will plateau. Month six looks like month one. Encoding outcomes -- successes and failures -- is the difference between a knowledge archive and a system that gets smarter with use.

4. **Maturity has two structural inflection points.** Going from L1-L2 (manual chat, fixed projects) to L3 (portable, testable skills) is the first jump. Going from L4-L5 (file access, area-bound projects) to L6 (centralized second brain) is the second. Skipping either creates fragile structure that will not carry the next level's load. Reach L6 *yourself* before attempting L7 (team OS).

5. **The operator role is structural, not optional.** At L6+, one human owns the context layer -- checking duplicates, fixing misplaced files, resolving conflicts, evolving structure. Without an operator running a cadence, vaults accumulate entropy faster than they accumulate value. This is not deferred work; it is the difference between a compounding system and a degrading one.

6. **Implementation feasibility IS strategy.** For agent-based systems, implementation constraints -- authentication, permissions, context assembly cost, auditability -- are not downstream of strategic decisions. They are the strategic decisions. If the agent cannot authenticate, cannot audit, or produces unsustainable token costs, the strategy does not work. Assess feasibility before committing architecture, not after.

7. **Self-improvement requires all five layers to run.** A truly self-improving system has five ordered layers: sensor (raw input), policy (autonomy rules), tool (deterministic APIs), quality gate (evals, safety, human review), and learning mechanism (feeds failures back to sensor). Every layer must be present and connected. Missing any single layer breaks the loop -- the system either stops improving or accumulates errors rather than correcting them.

---

## 1. Where You Are on the Maturity Curve

Two complementary frameworks let you locate yourself and pick a next move.

### The Seven-Level Context Infrastructure Model

| Level | What it is | Primary limit |
|-------|-----------|---------------|
| **L1** | Manual chat context -- copy/paste each session | No persistence |
| **L2** | Project-bound context files | Agent cannot self-update; isolated chats |
| **L3** | Portable skills (`SKILL.md` + reference folder) | First inflection: static to portable + testable |
| **L4** | File access + `CLAUDE.md` routing | Context grows naturally; agent reads/writes |
| **L5** | Co-work projects pre-bound to area folders | Per-area memory and rules |
| **L6** | Centralized second brain (one vault) | Second inflection: distributed to centralized |
| **L7** | Business OS -- second brain synced across team with permissions | Operator becomes a role, not just a person |

### The Five-Pillar Capability Check

Independent of level, an Agentic OS provides five capabilities. Map your current setup against them to see what is load-bearing and what is missing:

1. **Persistent memory** -- layered context (operating instructions / business knowledge / agent personality / project memory). Hard ceiling: keep `CLAUDE.md`-style files small and use reference files loaded on demand.
2. **Self-improving skills** -- skills + a `learnings.md` feedback loop that codifies non-negotiable rules from each use.
3. **Interaction layer** -- beyond chat: a supervisor surface (kanban-style or equivalent) where business *goals* -- not tasks -- are tracked.
4. **Scheduled workflows** -- skill chaining on cron with explicit human checkpoints. Empirically, fully autonomous chaining hits ~20% failure rates; "80% automated + checkpoint before publish" is the practitioner-validated threshold.
5. **Business context** -- a foundation folder (voice, ICP, positioning, brand) referenced by every skill. "Start with the business brain, not the agents."

### Decision tree: what to build next

```
Are you at L1-L2?
  -> Get to L3 first. Build one durable, testable skill. Don't skip.

Are you at L3-L4 with no centralized vault?
  -> Stop adding skills. Centralize first (L6 vault).
  -> Multiple area-folders without a central root will fork your context.

Are you at L6 (single-user)?
  -> Audit the five pillars. Whichever is missing is the next move.
  -> Don't move to L7 (team) until your personal cadence is working.

Are you at L6 considering L7?
  -> Designate an operator. Define the weekly cadence. Then turn on sync.
  -> Backwards order is the most common failure pattern.
```

### Context-first build sequencing

When extending the system, build in this order -- each layer multiplies the next:

1. **Business brain** -- shared context folder containing brand voice, ICP, positioning, client details, domain knowledge.
2. **Skills that reference the business brain** -- not skills that embed their own context.
3. **Interaction layers** -- UI, channels, dashboards.
4. **Scheduled workflows** -- chain context-aware skills on cron.
5. **Multi-agent orchestration** -- last, not first.

The common mistake is starting with multi-agent orchestration or autonomous workflows and bolting on context later. This produces generic outputs requiring constant manual correction. Three months of "getting this wrong" is the practitioner-documented learning cost. The context layer has the highest marginal return of any investment -- once it exists, every subsequent skill automatically produces contextually relevant outputs.

### Compounding extensions, not flat capabilities

When extending the system (new domains, new agent skills), prefer a **progressive adoption path** over a flat capability menu. Each extension should make the next one more powerful:

- Household knowledge -> home maintenance -> family calendar -> meal planning -> professional CRM -> job hunt pipeline.
- The CRM knows about thoughts captured earlier; the meal planner checks who is home this week (via calendar); job-hunt contacts become professional network contacts (via CRM).

Flat menus give flexibility but no compound effects. Compounding paths reduce decision paralysis, build skill incrementally, and surface integrations no one would have designed if extensions were built independently.

---

## 2. Assessing Viability Before Committing Architecture

Before choosing substrate, building skills, or designing loops, run four viability tests. Each can independently disqualify a strategy. Committing capital before testing these constraints means discovering failure six months in.

### The four viability tests

1. **Authentication** -- Can the agent authenticate against every system it needs to touch? If not, the strategy does not work.
2. **Permission model** -- Does the permissions model account for agents, not just humans clicking through screens? If not, the strategy does not work.
3. **Context assembly cost** -- Does every agent run reassemble business context from scratch? If token costs scale linearly with run count rather than amortizing across runs, the strategy may be economically non-viable. A persistent context layer (cached business context, pre-assembled data views) is not optimization -- it is a viability requirement at enterprise scale.
4. **Auditability** -- Can you prove to a regulator what the agent did on behalf of which user? If not, the strategy will not pass legal review.

These are not "implementation details to be worked out later." Each is sufficient to change the shape of the roadmap.

### The economics of context assembly

For a single agent run (e.g., "prepare the renewal brief for our largest customer"), the agent queries CRM data, support tickets, contract terms, usage data, call transcripts, and internal wiki. Without persistent context, each query consumes tokens for both the request and the response processing. At enterprise scale, this cost scales with run frequency, not data-change frequency -- the opposite of what you want.

- Human consultant: reads screens once, builds context mentally, no marginal cost per review.
- Agent without persistent context: pays full token cost per run.
- Agent with persistent context: pays marginal cost per run (only changed data).

The gap between the second and third models can be the difference between viable and non-viable. Design the context layer to persist and invalidate, not to rebuild from scratch.

### Template -- Pre-design viability checklist

```markdown
# Viability Assessment — {{SYSTEM_NAME}}

## Authentication
| System | Auth method | Agent-compatible? | Notes |
|--------|------------|-------------------|-------|
| {{SYSTEM_1}} | {{AUTH_TYPE}} | {{YES_NO}} | {{NOTES}} |

## Permissions
| System | Agent identity model | Audit trail? | Notes |
|--------|---------------------|--------------|-------|
| {{SYSTEM_1}} | {{IDENTITY}} | {{YES_NO}} | {{NOTES}} |

## Context Assembly Cost
- Estimated queries per run: {{QUERY_COUNT}}
- Estimated tokens per run (context assembly only): {{TOKEN_EST}}
- Data-change frequency: {{FREQ}} (daily/hourly/real-time)
- Context persistence strategy: {{NONE_CACHE_PRECOMPUTE}}
- Projected monthly cost at {{RUN_FREQUENCY}} runs: {{COST}}

## Auditability
- Can every agent action be attributed to a user? {{YES_NO}}
- Audit log format: {{FORMAT}}
- Regulatory requirements: {{REQS}}

## Verdict
{{PROCEED | BLOCKED_BY | REDESIGN_NEEDED}}
```

| Variable | Type | Description | Required |
|----------|------|-------------|----------|
| `{{SYSTEM_NAME}}` | string | Name of the agentic system being assessed | yes |
| `{{SYSTEM_1}}` | string | Each downstream system the agent must access | yes |
| `{{AUTH_TYPE}}` | string | OAuth, API key, service account, etc. | yes |
| `{{IDENTITY}}` | string | How the agent is represented in the system's permission model | yes |
| `{{QUERY_COUNT}}` | integer | Number of external queries per agent run | yes |
| `{{TOKEN_EST}}` | integer | Estimated input+output tokens for context assembly | yes |
| `{{RUN_FREQUENCY}}` | string | Expected frequency of agent runs | yes |
| `{{COST}}` | currency | Monthly projected token cost for context assembly | yes |

### Worked example -- MetaSystem research-loop viability

**Authentication:** Git (local filesystem -- no auth barrier), Perplexity (API key), web fetch (open). All agent-compatible.

**Permissions:** Claude Code reads/writes files in the vault. No multi-user permission model needed (single operator). Audit trail: git history captures every edit.

**Context assembly cost:** Each research-loop run reads dimension definitions, existing findings, and authority lists. Estimated ~15K tokens of stable context per run. At 2-3 runs per week, total context assembly cost is modest. The stable context (dimensions, authorities) changes infrequently -- caching or summarizing would reduce per-run cost but is not yet a viability blocker.

**Auditability:** Every change is a git commit. System Log entries record what happened per session. Full attribution chain from finding to source to session.

**Verdict:** Proceed. No viability blockers. Context assembly cost is a future optimization, not a current constraint.

---

## 3. Choosing Your Architectural Foundations

Three substrate decisions determine almost everything downstream: transparency, knowledge organization, and ownership separation.

### Obsidian as transparent frontend vs RAG as black box

The trust property is asymmetric. A markdown vault is inspectable: every entry is human-readable, human-correctable, human-organizable. A vector store or graph DB is not -- even visual graph-RAG is less efficient for human review than reading and editing files.

**Decision rule (the scale threshold):**

| If... | Use... |
|-----|------|
| Solo operator or small team, < ~1000 documents, primarily markdown, cost-sensitive | **File-based vault** (Obsidian, Logseq, plain Git repo) + AI file traversal |
| Thousands-millions of documents, sub-second retrieval needs, multiple concurrent users, heterogeneous content (PDFs/images/structured data) | **True RAG** (vector DB + embeddings) |

The advice from practitioners deploying this in production: *just try the simpler version*. Migration from Obsidian to RAG is non-trivial only if the wiki structure is deeply coupled to the workflow -- and that coupling is usually a sign that the substrate is doing its job.

### LLM-compiled wiki vs vector DB vs structured ontology

When the vault grows past raw notes, three patterns are available for *organizing* what is in it:

1. **LLM-compiled wiki** (Karpathy pattern) -- Raw sources go into a `raw/` folder. The LLM compiles index files (summaries as query entry points), concept articles, and cross-references. Query by file traversal, not vector search. Works well under ~1000 docs. Knowledge linting (gap detection, stale-data flags, broken-link repair) is a *core* pipeline stage, not optional.

2. **Vector DB / semantic retrieval** -- Embed everything; agents retrieve by similarity. Fast deploy. Failure mode: never draws the information/judgment boundary. Semantic ranking *is* an interpretation, but nothing flags it as such. At small scale, humans override bad rankings; at scale, the ranking *becomes* organizational reality. Breaks at ~10K documents or when users can no longer apply independent judgment.

3. **Structured ontology** (Palantir-style) -- Explicitly define domain objects, relationships, actions. AI reasons within the schema; cannot hallucinate relationships outside it. Failure mode: blind to emergent patterns. Precise within its schema, silent about what it does not know -- and what it does not know may be what matters most.

A fourth pattern, **signal fidelity**, applies when the business produces a high-quality data exhaust (transactions, sensor data). Build the world model around the cleanest signal; "money is honest." Failure mode: the signal *looks* like it interprets itself, but causal inference still requires judgment the signal does not carry.

**Sizing guidance for organizational world models:**

| Org type | Start with |
|----------|------------|
| < 100 people, strong senior team | Vector DB -- seniors supply the judgment |
| Enterprise / regulated | Structured ontology -- high upfront cost; captures surprises |
| Platform with clean transactional signal | Signal fidelity -- invest heavily in interpretive boundary labeling |
| Knowledge-work company (docs + conversations) | Vector DB -> migrate to structured before 10K docs; build interpretive layer on top |

### AI-delegated knowledge organization

For systems where the AI handles the organizational work -- classifying notes, typing edges, decomposing documents into atomic units, generating summaries, and cross-linking -- the human role shifts from organizer to input provider and quality reviewer. This resolves the historical bottleneck of personal knowledge management: the human effort required to organize knowledge. Specific AI-delegated tasks include:

- **Node typing** -- classify raw input into node types (decision, concept, hypothesis, pattern, source) from a predefined taxonomy.
- **Atomic decomposition** -- break large documents or conversations into atomic notes of 50-300 lines.
- **Edge typing** -- assign relationship types between nodes (supports, contradicts, depends-on, derived-from).
- **Summary generation** -- write one-sentence summaries enabling triage.
- **Cross-linking** -- identify connections between new and existing nodes.

The delegation boundary matters: define which organizational decisions the AI makes autonomously versus which require human review. A sensible default: the AI types nodes and generates summaries freely; humans review edge types on contradiction and depends-on edges, where misclassification has the highest downstream cost.

### AI-managed vault separate from human vault

For systems where the AI generates substantial content (summaries, entity pages, project docs), maintain **two distinct vaults**:

- **Human vault** -- personal notes, hand-written thinking. AI never writes.
- **AI vault** -- all AI-generated content. Human reads only.

Mixed-provenance vaults (humans editing AI-written areas) are the most common quality-degradation pattern. Strict separation enforces clean ownership and makes trust verification possible (the human can read the AI vault to see what the AI knows).

For *organizational* knowledge with shared editing, this separation is harder to enforce -- use Git history + version control as a fallback audit trail (every edit is attributable).

### The middle-ground knowledge store

For multi-agent systems where context needs to travel across agent boundaries (one agent learns; another needs to know), consider a **lightweight MCP-accessible knowledge store** between flat memory files and full RAG. Costs ~10c/month at small scale; structured enough to be searchable; cheap enough to maintain casually. This is the "Open Brain" pattern: any MCP-speaking agent can read or write, so context accumulated in one role is retrievable by another without re-provisioning.

---

## 4. Choosing Your Build Infrastructure

Two decisions about the agent stack itself: what to build on, and how to avoid the manual-sequencing trap.

### SDK prototyping with framework graduation

Coding agent SDKs (Claude Agent SDK, Codex SDK) ship with infrastructure that any agent needs: tool registries, sub-agent orchestration, skills directories, MCP server integration, hooks, permission systems, and conversation history management. Rather than building this infrastructure from scratch, build non-coding agents (second brains, integration hubs, domain assistants) as thin layers on top of a coding SDK.

The economics are compelling: a single TypeScript file with SDK calls can replace hundreds of lines of framework code that manually wires up tools, manages conversation history in a database, configures RAG pipelines, and handles state. The SDK manages all of this by default.

But SDKs have graduation triggers. When the agent needs to serve multiple users, meet sub-second latency, reduce token costs at scale, or provide production observability, rebuild the agent loop using a framework (Pydantic AI, LangGraph). The key insight: **skills and MCP servers are the portable assets that survive graduation**. The agent loop and state management are disposable infrastructure that gets rebuilt. This means investing in high-quality skills and MCP servers is the highest-ROI activity regardless of current infrastructure choice.

| Phase | What to use | When to graduate |
|-------|------------|-----------------|
| **Prototype** | SDK (Claude Agent SDK, Codex SDK) -- minimal code, subscription economics, batteries included | When any graduation trigger fires |
| **Production** | Framework (Pydantic AI, LangGraph) -- custom agent loop, API-key economics, full observability | N/A -- this is the destination |

**Graduation triggers:**
1. Multi-user deployment (subscription ToS restricts SDK to single user)
2. Speed requirements (SDK reasoning overhead makes sub-second responses impossible)
3. Cost sensitivity (API-key usage at scale makes SDK agents prohibitively expensive)
4. Observability needs (production agents need custom conversation history storage and monitoring)

### Eliminating AI shepherding

"AI shepherding" is the practice of a human manually invoking skills in sequence, remembering what comes next, and kicking off each phase. It is the default working mode with coding agents, and it is the problem that harness engineering solves.

The diagnostic question: are you the orchestrator? If you are remembering the process order, deciding when to proceed, and kicking off each step, you are shepherding. The alternative is encoding the full sequence as a workflow that runs end-to-end, with the human intervening only at explicit gates.

**The ROI of harnessing is empirically large.** Raw LLM-generated code has a 6.7% PR acceptance rate. Adding a harness (structured workflow with validation, context curation, review steps) raises this to approximately 70% -- a 10x improvement. At production scale, harnessed workflows enable volume that no manual shepherding could sustain (Stripe ships 1,300 AI-only PRs per week via harness). 40% of Claude Code's own codebase is dedicated to harness infrastructure.

**When to harness:**
- If a manual sequence runs more than 3 times and the steps are stable, encode it as a workflow.
- Start by harnessing the 2-3 most common sequences; keep shepherding for rare or novel tasks.
- Hybrid mode (harness runs, pauses at every step for review) is the training-wheels path.

**When NOT to harness:**
- Exploratory or novel work where the sequence is not yet stable.
- Workflows where every step genuinely requires human judgment (some manual sequencing is appropriate).
- Before individual skills are reliable -- automating unreliable steps faster does not help.

---

## 5. Feeding the System (Ingestion)

Five patterns cover the ingestion surface area, anchored by one design principle.

### The signal-as-byproduct principle

A knowledge system only compounds if **signal capture is a byproduct of doing the work** -- not a separate documentation step. If feeding the system requires extra effort, two failure modes follow:

- *Strategic withholding* -- people with the most valuable context are the most strategic about not feeding a system that erodes their information advantage.
- *Benign forgetfulness* -- even well-intentioned contributors skip documentation under time pressure.

The result is a system that accumulates low-stakes, easy-to-document information and *misses* the judgment-rich context that would make it useful.

**Design implication**: prefer commit messages over documentation files, ticket updates over status emails, structured decisions made in-system over decisions made elsewhere and pasted in. Tool integrations should produce signal as side effects of normal work -- auto-logging, hook-based capture, byproduct artifacts.

### AI-delegated organization as continuous intake

Rather than batch-processing knowledge into the vault on a schedule, delegate the organizational work to the AI continuously. As raw input arrives (conversations, documents, data), the AI classifies it, decomposes it into atomic notes, types the relationships, and cross-links it against the existing graph. The human provides raw input and periodically reviews the AI's organizational decisions -- but the organizational effort is near-zero for the human.

This shifts the maintenance model from "Saturday-morning coffee sessions" to continuous incremental organization. Knowledge bases can actually reach sufficient scale to be useful because the compilation bottleneck (raw input to structured graph) is handled cheaply and tirelessly.

### Long-form content summarization with sub-agents

For 2-3 hour podcasts, books, or papers that will not fit in a single context window:

1. Download transcript (or Whisper-transcribe).
2. Chunk for sub-agent context windows.
3. Sub-agents summarize chunks in parallel.
4. Orchestrator assembles into a structured note: TLDR callout, timestamped topic index, key quotes, mentioned-people/concepts/tools sections.
5. Each mentioned entity gets a stub page -- entity references accumulate cross-links over time.

**Proportionality rule**: summary depth scales with content length. 15-minute video -> concise overview; 500-page book -> 15-20 minute read. The entity-page pattern is what differentiates this from flat summarization -- it converts isolated artifacts into a growing interconnected knowledge base.

### Project intake skill

For project-shaped work (client engagements, research projects, sales pipelines, job searches), build a one-command intake skill:

1. Prompt for project name; check for existence (update path) or create new.
2. Collect from multiple sources -- email thread/label, local files (PDF/DOCX/images), pasted text/screenshots.
3. Filter static documents (contracts, NDAs) from conversational content.
4. Create a standardized folder: `overview.md`, `conversation-log.md`, `links.md`, `documents/`, plus an entry in a `projects.base` (table tracking all projects + status).
5. Generate an import summary.

The skill encodes the *taxonomy* of project knowledge (status, conversations, documents, contacts), not just the raw data. After intake, an agent can answer "what is the status of project X and what should I do next?" by reading the folder.

### Daily multi-source brief

For replacing reactive notification-checking with a single intentional read: build a scheduled task that aggregates Gmail + Calendar + messaging (Beeper or equivalent) + tasks (Things, Todoist, etc.) into one Obsidian note each morning. Add inbox triage -- rule-trained auto-archive of cold outreach and spam. The brief is overwritten daily (not appended); the human reads, checks off, moves on.

The secondary discovery practitioners report is behavioral: when all communications are laid out at once rather than arriving as interrupts, *most do not require urgent response*. The brief makes that visible.

### Scheduled tasks for real-time context maintenance

A second brain seeded with static context (ICP, brand, strategy docs) becomes a historical snapshot as the business evolves. Recurring scheduled agent tasks close the gap:

- Meeting transcript ingestion (Firefly or equivalent -> structured vault folder)
- Team task rollup (daily scan, summarized, filed)
- Analytics updates (CRM pipeline, key metrics)
- A morning *synthesis* task that reads current priorities, to-do state, and recent updates, producing a daily prioritized overview

Goal: keep the gap between "what the vault knows" and "what is happening" under 24 hours.

### Template -- Daily brief skill

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
- Failure modes: API credential rotation; messaging API instability; over-aggressive archival.
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

## 6. Querying the System

Two patterns cover the query surface, ordered by sophistication.

### The vault as query engine

After data is structured in the vault, the AI agent (Claude Code or equivalent) becomes the interactive query layer:

- *Status queries* -- "What is the status of project X?" -> agent reads the folder, synthesizes.
- *Action item generation* -- "What should I do next on X?" -> agent reads conversation log, identifies open threads, prioritizes.
- *Draft generation* -- "Help me reply to the client" -> agent reads context, drafts.
- *Cross-project synthesis* -- "Which projects need attention this week?" -> agent scans the index/base table.

This pattern requires no infrastructure beyond the vault and a file-reading agent. The constraint: the vault must be *current*. Stale conversation logs produce confidently-wrong answers.

### NotebookLM (or equivalent) as a cited knowledge layer

For external knowledge -- domain expertise (Huberman health, Lenny PM, etc.) you do not author yourself -- connect a citation-grounded KB tool via MCP:

- List notebooks programmatically.
- Query any notebook in natural language; receive citation-tagged answers.
- Run multiple queries in parallel (e.g., 6 sub-agents querying 6 dimensions simultaneously).
- Save responses *with citations* directly to the vault.

The key property is **citation traceability** -- every recommendation traces to a specific source (timestamp in a video, section in a doc). Built-in citation verification: have the agent score citation quality; surface low-confidence matches.

---

## 7. Proactive Agent Loops

The system stops being reactive and starts acting on its own behalf. Five patterns cover the proactive surface.

### Time-window proactive loop (the canonical structure)

A scheduled agent that runs a time-aware decision loop:

```
0. Date anchor       -- establish exact date/time. Store as anchor_date / anchor_time.
                       All date arithmetic is calculated from this. Never use vague terms ("recently").
1. Time check        -- classify into a window (early morning / pre-meeting / midday / evening / late).
2. Duplicate check   -- query the briefings table; don't repeat what's already been sent today.
3. Decide            -- based on window, what should be delivered?
4. External pull     -- fetch live data (calendar, weather, attendees).
5. Internal enrich   -- search vault for context on what was just pulled.
                       (External BEFORE internal -- can't enrich what you haven't seen.)
6. Deliver           -- channel tools (Telegram/Discord). Concise, mobile-friendly. Silence > noise.
7. Log               -- record what was sent. Next cycle reads this.
```

Seven briefing types in the OB1 reference implementation: morning, pre_meeting, checkin, evening, habit_reminder, weekly_review, custom. Five time windows.

### Morning routine skill

The bridge from "experiments designed" to "experiments tracked": a `daily` skill that runs at session start and:

1. **Goal check** -- read goals file from vault; surface current goals.
2. **Experiment discovery** -- scan for `type: experiment` and `status: in_progress`; list.
3. **Observation collection** -- for each active experiment, ask a targeted question. ("How is the morning sunlight experiment going? What was your wake-up time?")
4. **Data logging** -- write responses to the experiment note's observation section; update numeric tracking fields (mood 1-10, energy 1-10, sleep, gym sessions, etc.).
5. **Next-action scheduling** -- based on observations, suggest or schedule the day's actions.

The skill reads live from the vault, so adding a new experiment automatically adds it to the morning check-in. The user shows up and answers; structured logging is automatic.

### Learn-Plan-Act-Review (the closure loop)

Most people consume expert knowledge but never translate it into changed behavior. The loop forces closure:

1. **Learn** -- ingest expert content into a citation-grounded KB.
2. **Plan** -- run a cited interview against the KB; conduct a personal gap assessment; identify highest-leverage experiments.
3. **Act** -- design experiments with explicit hypotheses + success criteria; schedule calendar events; embed into the morning routine skill.
4. **Review** -- daily morning check-in captures observations; data logs to structured experiment notes; a dashboard surfaces progress.

The pattern's leverage is that it inverts the discipline requirement. Instead of you remembering to check experiments, the agent asks every morning. You only show up and answer.

### Experiment notes as a personal data layer

For longitudinal personal tracking, structure experiments as Obsidian markdown files:

- **Frontmatter**: `type: experiment`, `status: in_progress | proposed | complete`, dashboard link.
- **Body sections**: Hypothesis (explicit), Protocol (step-by-step), Success Criteria (measurable, e.g., "80% of days within 30min of target wake-up time"), Observations (filled daily).
- **Numeric fields**: Tracked metrics (mood, energy, sleep quality, gym volume).
- **Dashboard link**: aggregator note showing all active experiments + plotted data.

The vault *is* the database. No schema migration; no API; no special memory mechanism. A new agent session picks up exactly where the last one ended by reading the experiment files.

### The compounding knowledge loop (with outcome encoding)

The fully self-reinforcing pattern: agent answers question -> synthesizes across wiki -> answer filed in session log -> log eventually promoted to wiki -> wiki grows -> future queries get better answers. The loop runs automatically via session hooks (`session_start`, `pre_compact`, `session_end`) plus a daily flush.

**The non-negotiable invariant: encode outcomes, not just events.** A loop that records what happened but not *what was done about it* and *what resulted* will plateau. Most implementations skip outcome encoding, which is why compounding fails to materialize in practice. This requires organizational readiness -- willingness to record results honestly, including failures.

### The five-layer recursive self-improvement architecture

For a system that does not just compound passively but actively detects and corrects its own failures, five layers must all be present and connected:

| Layer | Function | Failure when missing |
|-------|----------|----------------------|
| **1. Sensor** | Raw input -- monitors outputs, errors, performance metrics | System is blind; failures go undetected |
| **2. Policy** | Autonomy rules -- decides what the system can act on without human approval | System either acts unsafely or escalates everything |
| **3. Tool** | Deterministic APIs -- takes concrete actions (file writes, PR opens, deployments) | Recommendations accumulate but nothing executes |
| **4. Quality gate** | Evals, safety checks, human review checkpoints | Errors compound rather than resolve |
| **5. Learning mechanism** | Feeds failures back to the sensor layer; updates rules and weights | System repeats the same failures; no improvement |

**The all-or-nothing property:** Partial implementations produce a system that either stops acting (if the tool or learning layers are missing) or acts dangerously (if the quality gate is missing). A three-layer system that lacks a quality gate is worse than a manual process because it acts with false confidence.

### The monitoring agent pattern

A dedicated monitoring agent sits above the primary system and observes every interaction. When the primary agent fails to satisfy a request, the monitoring agent activates a diagnostic and repair cycle: detect the failure, diagnose the root cause (missing tool, outdated skill, missing database index), write a fix, submit it for review, and deploy. A second agent reviews the fix for correctness and safety before merge.

This closes the gap between passive compounding (the knowledge loop) and active self-repair. The key architectural insight is separation of concerns: the primary agent serves users; the monitoring agent improves the primary agent. Neither role is burdened with the other's responsibilities.

**Production evidence:** A YC-stage system running this pattern detected failures overnight, deployed fixes, and users found queries working the next morning without human intervention. Every layer of the five-layer architecture was active: sensor (monitoring), policy (auto-act on severity < threshold), tool (git + PR APIs), quality gate (agent review before merge), learning mechanism (failure patterns fed back to monitoring rules).

### Template -- Time-window proactive loop

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

### Worked example -- Fitness Learn-Plan-Act-Review loop

**Learn**: Bulk-ingested Huberman Lab episodes into a NotebookLM notebook via the bulk-ingest skill.

**Plan**: Spawned 6 parallel Claude Code sub-agents querying the notebook on sleep, exercise, supplements, stress, light exposure, and biomarkers. Each returned a citation-grounded Q&A. The user answered each question; the agent compared answers against existing fitness data already in the vault. Output: a current-state-vs-target gap assessment ranking top 3 experiments by leverage.

**Act**: For each top experiment, the agent created an experiment note (`type: experiment`, `status: in_progress`, hypothesis, protocol, success criterion). Calendar events were scheduled for time-bound protocol steps (e.g., "morning sunlight 7-10am for 14 days"). The morning routine skill auto-detected the new experiments because it scans for `status: in_progress`.

**Review**: Each morning, the routine skill asked targeted questions per experiment, wrote responses to the observation section, updated numeric tracking. After 14 days, the dashboard showed the experiment closed (success criterion met) or rolled forward (hypothesis revised).

---

## 8. Operating Long-Term

Two roles, one cadence, one failure-detection loop.

### The context layer operator

At L6+, designate one human as **the context operator**. The role covers:

1. **Weekly vault review** -- duplicates, misplaced files, conflicting context (two files with contradictory ICP definitions).
2. **Quality assurance** -- scheduled-task output landing correctly (not generating noise).
3. **Structural evolution** -- updating `CLAUDE.md` routing and per-subfolder index files as the vault grows.
4. **Permission management** (L7 only) -- controlling write access per folder via the team-sync layer.
5. **Onboarding new contributors** -- sharing the vault, establishing contribution norms.

The role is informal in single-user setups (you are the operator). It must be **explicitly designated** at L7 -- diffused accountability is the most reliable path to vault degradation.

### Maintenance cadence

The cadence is the difference between a compounding system and a degrading one. Concrete weekly checklist:

- [ ] Vault health: duplicate-finder report (any file >=80% similar to another).
- [ ] Misplaced files: anything in the root that should be in `references/`, `attachments/`, or a system-scoped folder.
- [ ] Conflicting context: documents that contradict each other (esp. ICP, brand, governance).
- [ ] Scheduled-task output spot-check: are recurring tasks writing the right things to the right places?
- [ ] Stale entries: anything with `last_updated > N days` that should be current.
- [ ] Routing drift: does `CLAUDE.md` still reflect actual structure?

Track a **context health score** over time -- number of issues found per cadence run. A rising score is the leading indicator of structural strain.

### Automated failure detection

For systems that have graduated beyond manual maintenance, add a monitoring agent that watches for failures in the primary system's interactions. The monitoring agent's diagnostic taxonomy:

- Missing tools (the primary agent could not find a required capability)
- Outdated skills (a skill's instructions no longer match the system state)
- Missing indexes or views (a query path that should exist but does not)
- Incorrect query strategy (the agent used the wrong approach for the data shape)

The monitoring agent writes fixes, submits them for review, and a second agent reviews and deploys. This creates a system that improves while no human is actively maintaining it -- the compounding loop runs overnight.

### Template -- Operator weekly cadence

```markdown
# Vault Health -- Week of {{WEEK_OF}}

**Operator:** {{OPERATOR}}
**Vault:** {{VAULT_PATH}}
**Health score:** {{ISSUE_COUNT}} (delta from last week: {{DELTA}})

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

| Variable | Type | Description | Required |
|----------|------|-------------|----------|
| `{{WEEK_OF}}` | date | Start date of the reporting week | yes |
| `{{OPERATOR}}` | string | Name of the context layer operator | yes |
| `{{VAULT_PATH}}` | path | Absolute path to the vault root | yes |
| `{{ISSUE_COUNT}}` | integer | Total issues found this cadence | yes |
| `{{DELTA}}` | signed integer | Change from last week's issue count | yes |

---

## Pitfalls

Synthesized failure modes from across the cluster. Every one of these has been observed in production by at least one practitioner.

### Strategy and sequencing failures

- **Implementation details deferred until too late** -- Treating authentication, permissions, context cost, and auditability as implementation details rather than strategic constraints. Six months of architecture committed before discovering the agent cannot reach the data.
- **Agents before context** -- Building multi-agent orchestration or autonomous workflows before the business brain exists. Produces generic outputs requiring constant manual correction.
- **L7 before L6** -- Team sync turned on before personal cadence is working. Synchronization complexity multiplies before context quality is established.
- **Premature harnessing** -- Encoding workflows as harnesses before individual skills are reliable. Automating unreliable steps faster produces unreliable results faster.

### Compounding failures

- **No outcome encoding** -- System records events but not results. Compounding never materializes; month six looks like month one.
- **Garbage-in-garbage-out** -- Compounding loop runs at low session quality. Wiki bloat without value. Add quality gates before promotion.
- **Static seed corpus** -- Knowledge store seeded once and never refreshed. Becomes a historical snapshot disguised as current truth.

### Capture failures

- **Active documentation requirement** -- The system demands a separate documentation step. The most valuable context (judgment-rich, high-stakes) is the most likely to be withheld.
- **Passive-capture noise** -- Over-correcting toward passive capture floods the vault with low-signal data. Quantity does not equal quality.
- **AI classification drift** -- Without periodic human review of AI organizational decisions, the AI drifts in how it applies node types and edge types, creating inconsistency across the knowledge graph.

### Architecture failures

- **Premature RAG migration** -- Building vector DB infrastructure for < 1000 documents. Significant overhead for negligible gain.
- **Architecture-by-deployment-speed** -- Picking the fastest-to-deploy architecture (vector DB) without org-size and risk-profile inputs.
- **Mixed-provenance vaults** -- Humans editing AI-written areas (or vice versa). Most common quality-degradation pattern.
- **SDK lock-in** -- Building too much on a coding SDK before graduation, making the framework rewrite expensive. Skills that work in SDK may silently break in framework due to implicit SDK dependencies.

### Operations failures

- **Informal operator role** -- Cadence skipped when the operator is busy. Vault drift accumulates invisibly until output quality drops perceptibly.
- **Single-operator bottleneck (L7)** -- One operator, no succession plan. Vault quality depends on one person's availability.
- **AI shepherding as default** -- Manually invoking skills in sequence because "it works." Process amnesia (forgotten steps), inconsistency (varied sequences), and human bottleneck (process runs only when the human is active).
- **Routing drift** -- `CLAUDE.md` not updated as vault grows. Agent traverses to dead paths.
- **Context assembly cost ignored** -- Each agent run reassembles the same business context from scratch. Token costs scale with run frequency instead of data-change frequency. Viable at low volume; non-viable at scale.

### Proactive-loop failures

- **Notification fatigue** -- Proactive agents that talk too much get muted. Silence > noise.
- **Date anchor drift** -- System clock wrong; all time-window logic fails silently.
- **State table corruption** -- Briefings log is the deduplication mechanism; corruption produces repeated messages.
- **Experiment overload** -- Too many active experiments; morning check-in feels like work; observation quality degrades.
- **Five-layer checkbox implementation** -- Sensor, policy, tool, quality gate, and learning mechanism are all nominally present but not end-to-end connected. The system looks self-improving but repeats failures because the learning mechanism does not feed back to the sensor.
- **Missing quality gate** -- Three-layer automation (sensor + policy + tool) without a quality gate acts with false confidence; errors compound rather than resolve.
- **Monitoring agent misdiagnosis** -- The monitoring agent deploys "fixes" that break other functionality because the review agent rubber-stamps changes it does not fully understand.

---

## Contract

### Preconditions
- File-based vault with markdown notes (Obsidian, Logseq, plain Git repo, or equivalent).
- AI agent with file read/write access (Claude Code, or any agent that supports file I/O).
- Git or equivalent version control on the vault root.
- A designated context operator (you, at single-user; explicit role at L7).
- Viability assessment passed for authentication, permissions, context cost, and auditability.

### Invariants
- The vault remains plain text and portable across AI vendors.
- Human gates remain at every action loop boundary (no fully-autonomous chains in production).
- Capture happens as a byproduct of work, not a separate documentation act.
- Compounding loops encode outcomes, not just events.
- Implementation feasibility is assessed before strategic commitment.
- The maintenance cadence runs.

### Governance
- **Owner** -- the practitioner running the system; or, at L6+, the designated context layer operator.
- **Updated when** -- new architectural patterns surface in `research-findings/` under `category: Agentic Systems`; new sub-patterns graduate; failure modes accumulate enough to warrant an addition to *Pitfalls*.
- **Source** -- Improvement Loop research, Dimension 11 (Agentic Systems). Findings under that dimension are the ground-truth corpus.

### Recovery
- **Vault corruption** -> git history rollback. Auto-commit means the worst-case loss is the configured idle interval (<=1 minute on typical setups).
- **Operator unavailability** -> cadence pause; flag at L7. Designate a backup before the operator becomes unreachable.
- **Tool deprecation** (Obsidian, Claude Code, NotebookLM, messaging apps) -> vault is plain text; swap tools without data migration. Skills referencing the deprecated tool are the only thing that needs rewriting.
- **AI vendor change** -> disconnect the current AI; connect a different one. The vault is the persistence layer, not the AI.
- **SDK lock-in** -> skills and MCP servers are portable; the agent loop and state management rebuild on the target framework. Plan the graduation before over-investing in SDK-specific infrastructure.
- **Compounding loop drift** (wiki contradicts itself; quality degrades) -> run a vault audit; surface conflicts; resolve via operator cadence; consider knowledge-linting pipeline (gap detection, stale-data flags, broken-link repair) as a recurring task.
- **Monitoring agent drift** -> audit the monitoring agent's fix history; if fix quality degrades, tighten the quality gate or reduce the monitoring agent's autonomy tier.

---

## Related Guides

- **[[structuring-agent-context]]** (G2a) -- context structuring and loading primitives that this guide assumes (`CLAUDE.md` size limits, reference files loaded on demand, tiered retrieval).
- **[[defending-agent-context]]** (G2b) -- context degradation defense (context rot mitigations, compaction timing, session discipline).
- **[[agent-design-patterns]]** (G3a) -- agent identity and composition patterns. Section 4 (Build Infrastructure) references harness engineering and SDK decisions that G3a covers in depth.
- **[[agent-workflow-and-execution]]** (G3b) -- operational mechanics for scheduled tasks, durable workflows, observability. Section 5 (Ingestion) and Section 7 (Proactive Loops) sit on top of G3b's primitives.
- **[[designing-agent-tools]]** (G5) -- MCP integration patterns referenced in Section 6 (Querying) live here in detail.
- **[[agent-governance-and-trust]]** (G9) -- human-gate placement and review workflows that apply to the proactive-loop checkpoint discipline in Section 7.
- **[[agent-architecture-decisions]]** (G3) -- topology and infrastructure decisions that determine how multi-agent orchestration (the last step in context-first sequencing) is structured.
