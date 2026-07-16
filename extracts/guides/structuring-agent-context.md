---
title: "Structuring and Loading Agent Context"
type: "guideline"
category: "Context Engineering"
target_system:
  - "improvement-loop"
stage: "draft"
created: "2026-05-25"
updated: "2026-07-16"
author: "claude"
source_findings:
  - "ace-agentic-context-engineering-evolving-playbook"
  - "agent-context-kiss-commandments-minimum-viable"
  - "context-curation-over-context-stuffing"
  - "context-enrichment-for-task-clarity"
  - "context-file-instruction-bloat-eth-zurich"
  - "document-sharding-for-context-efficiency"
  - "fundamental-limits-of-single-vector-embedding-retr"
  - "hybrid-upfront-and-jit-context-architecture"
  - "scrum-master-story-contextualization"
  - "index-file-navigation-as-rag-replacement"
  - "claudemd-as-knowledge-base-traversal-guide"
  - "model-specific-context-file-sensitivity"
  - "one-shot-prd-prompt-for-system-bootstrap"
  - "tiered-context-injection-over-monolithic-files"
  - "notebooklm-as-external-knowledge-base-for-context"
  - "pointers-over-copies-in-context-files"
  - "progressive-tiered-context-loading-convergence"
  - "context-file-taxonomy-claudemd-soulmd-agentsmd"
  - "progressive-skill-loading"
  - "self-describing-codebase-structural-semantic-context"
  - "three-tier-progressive-context-loading"
  - "skills-as-pointers-to-second-brain-files"
  - "write-time-vs-query-time-synthesis-kb-poisoning"
  - "bounded-tiered-memory-inference-driven-curation"
  - "claude-code-context-management-decision-matrix-five-tools"
  - "inline-scoped-mcp-servers-per-subagent"
  - "agentic-rag-multi-strategy-retrieval-2026"
  - "file-search-outperforms-rag-for-small-corpora"
  - "hybrid-retrieval-pattern-semantic-lexical-graph"
  - "summary-gate-agent-traversal-pattern"
  - "personal-knowledge-hoard-as-agent-substrate"
  - "ai-as-primary-reader-design-principle"
  - "environment-grounded-context-as-output-quality-multiplier"
  - "agent-memory-architecture-multi-agent-layered"
  - "interactive-explanations-extend-linear-walkthroughs"
  - "always-on-context-minimalism-pointer-only-entry"
  - "task-to-file-routing-table-in-context-files"
  - "cold-start-chain-and-cold-start-test"
  - "docs-split-by-lifespan-not-topic"
  - "evergreen-vs-volatile-ingestion-rule"
  - "skill-as-directory-progressive-disclosure-three-levels"
  - "skill-content-lifecycle-context-budget"
  - "skill-description-budget-context-overflow"
  - "skill-dynamic-context-injection-shell-prerender"
  - "hub-and-spoke-two-tier-skill-taxonomy"
  - "branch-analysis-externalization-rule-skill-reference"
  - "shared-context-folder-as-cross-skill-update-multiplier"
  - "per-node-context-scoping-skills-mcps-commands"
  - "path-scoped-guardrails-edit-time-prevention"
  - "query-shape-first-storage-design"
  - "per-folder-heterogeneous-retrieval-levels"
  - "structural-outline-before-read-agent-navigation"
  - "untyped-links-as-token-waste-anti-pattern"
  - "knowledge-substrate-standardization-cross-agent-interop"
  - "okf-open-knowledge-format-curated-bundle-spec"
  - "rank-fusion-hybrid-retrieval-mongodb-atlas"
  - "query-decomposition-sub-query-rrf-merge"
  - "post-retrieval-reranking-weighted-signal-composition"
  - "lossy-compression-boundary-headless-return"
  - "self-contained-phase-prompt-pattern"
  - "progressive-diorization-pipeline-raw-to-breadcrumb"
source_dd:
  - "DD-81"
  - "DD-98"
tags:
  - "guide"
  - "context-engineering"
  - "context-structuring"
contract:
  preconditions: "Agent system exists or is being designed; context files are the primary interface between human knowledge and agent behavior"
  invariants: "Context is structured for the agent's retrieval capabilities, not human reading convenience; tiered loading preserves token budget"
  governance: "Owner agent maintains; re-synthesize when source findings change by 3+"
  recovery: "If context loading degrades agent performance, audit against the tiering decision tree and retrieval strategy selection"
---

# Structuring and Loading Agent Context

You are designing the information environment an agent operates inside. This guide covers the structural decisions: what content to include, how to organize it into files and tiers, how to load skills economically, how to shard large documents, and how to retrieve context at runtime. Two companion guides cover the adjacent lifecycles: *Defending Against Context Degradation* (G2b) covers rot defense and compaction strategy within a session, and *Session Persistence and Memory* (G7) covers state that must survive across sessions.

## When to Use This Guide

- You are creating context files (CLAUDE.md, system prompts, skill definitions, agent briefs) for a new agent or refactoring existing ones
- Token costs are higher than expected and you suspect the agent is loading content it does not need
- You are scaling from a single context file to a multi-file architecture and need a tiering strategy
- Your skill library is growing and skills are misfiring, undertriggering, or inflating every request's base cost
- You are choosing a retrieval approach for a knowledge base the agent will query at runtime
- You are deciding how to store knowledge in the first place — markdown files, a wiki, a vector index, a graph
- You are dispatching work to sub-agents and need to decide what context to pass
- You are designing a knowledge base where the primary reader is an AI agent, not a human
- You are bootstrapping a new system and need to decide what goes into the initial context package

**Do not use for:** defending against context rot over time (see G2b: *Defending Against Context Degradation*), persisting memory across sessions (see G7: *Session Persistence and Memory*), defining what the agent should do (see G1: *Writing Agent Specifications*), or designing the agent's tool set (see G5: *Designing Agent Tools*).

## Key Concepts

**1. Less context usually means better output.** ETH Zurich (2026) proved that LLM-generated context files reduce agent success by 3% and increase cost by 20%. The mechanism: irrelevant or contradictory context dilutes attention, creates conflicting signals, and forces the model to resolve ambiguities that should have been resolved by the human during curation. Context files also amplify reasoning token usage by 14-22%, meaning agents spend compute processing instructions rather than solving the task. The discipline is curation -- deciding what not to include -- not coverage.

**2. Structure determines cost more than volume does.** The same knowledge base queried with different structures can cost 15x more per query (9,000 vs 600 tokens). Flat documents force the agent to load everything to find anything. Tiered documents with summaries, typed metadata, and progressive loading let the agent filter cheaply before committing tokens to full reads. Structure is a first-class architectural constraint, not a formatting preference.

**3. Progressive loading is a converged best practice.** Six independent implementations (BMAD, OpenViking, DeerFlow, Beads, Claude Code tool-search, MCP progressive discovery) arrive at the same principle: load minimal metadata first, expand on demand. The Agent Skills standard makes it a platform primitive -- ~100 tokens of metadata always loaded, the full skill body only on activation, bundled files only when read. When unrelated teams independently converge on the same pattern, it is likely a genuine solution rather than a trend.

**4. The always-on layer is the most expensive real estate.** Whatever the harness injects unconditionally -- the entry context file, every skill's description -- is paid for on every request, forever. Detail loaded on demand is nearly free by comparison; *discoverability* is the scarce resource, not storage. This inverts the intuition to "put important things where they're always visible": the always-on layer should carry the irreducible minimum plus pointers, and everything else should be reachable, not resident.

**5. Storage format follows query shape.** How knowledge will be asked for determines how it should be stored. "Summarize the March 5th meeting" fails on vector-chunked storage and succeeds trivially on one whole markdown file; "what was rule 17 of our 1,000 rules?" is wasteful as a whole-file read and ideal as a snippet lookup; "trace X back to A" needs typed relationships. Decide the anticipated query shape -- whole-object synthesis, pinpoint lookup, or relationship trace -- before choosing the storage format, and decide it per corpus, not once for the whole system.

**6. Retrieval strategy depends on corpus size.** For small knowledge bases (under 1000 documents), file search tools (grep, glob, file traversal) outperform vector-based RAG. For larger corpora, semantic search becomes more accurate and cheaper than exhaustive file search. For relationship-heavy domains, graph traversal handles queries neither method can answer. The right approach is to give the agent multiple retrieval tools and let it choose per query, not to hardcode a single strategy.

**7. When the primary reader is an AI, optimize for machines.** Humans benefit from simplicity (4 folders, untyped links). AI agents navigate richer taxonomies (16 node types, 10 edge types) and use that structure for more precise retrieval and traversal pruning. Typed metadata, one-sentence summaries, and explicit relationship labels are cheap overhead for an agent that reads metadata faster than prose.

---

## Step 1: Decide What Belongs in Context

Before structuring anything, audit what your agent actually needs versus what it currently receives.

### The Inclusion/Exclusion Test

For each element currently in (or being considered for) the context window, apply three questions:

1. **Can the agent discover this on its own?** Codebase overviews, directory trees, and file structure descriptions are empirically redundant -- agents discover these by reading the repo. ETH Zurich found that including them adds steps without improving success. Only include non-inferable information: custom tooling, unusual build commands, project-specific constraints.

2. **Is this stable or volatile?** Stable elements (identity, safety rules, tool definitions) belong in the upfront layer and should be cached. Volatile elements (task-specific docs, conversation history) should be retrieved just-in-time or managed dynamically. Mixing the two in a single file wastes cache efficiency and forces full re-reads on any change.

3. **Does removing this make the current task worse?** If the answer is "probably not" or "I don't know," remove it and measure. Reversing a removal is cheap; carrying dead context indefinitely is expensive.

### The Evergreen Test for Knowledge-Base Ingestion

The same discipline applies one level up, at the knowledge store the agent queries. Only ingest data you would still want there in a year: locked-in decisions, quarterly priorities, durable background. Volatile data -- Slack threads, emails, live operational records -- stays in its system of record; the knowledge base gets *access* to those systems (a tool call away), never copies. Copied volatile data is noise that demands recurring deletion sweeps, competes with live truth, and degrades retrieval.

The ingestion-time test: **"In a year, will it be good to have this memory in here?"** Yes → ingest. No → store a pointer to the system of record instead.

### What Belongs In

- **Agent identity and instructions** -- high-signal, stable, cacheable
- **Hard rules and safety constraints** -- cannot be enforced structurally; must be stated
- **Task context enrichment** -- purpose (what the result will be used for), audience (who consumes the output), workflow position (where this step sits in the pipeline), and success criteria with measurable thresholds
- **Navigation instructions** -- for knowledge-base-heavy projects, how to traverse the KB (where to find indexes, how to follow links, what to read first)
- **Scoped tool definitions and permissions** -- only the tools relevant to the current task
- **Pointers to canonical sources** -- file paths, not pasted copies

### What to Exclude or Move Out

- Verbose documentation retrievable on demand
- Historical context irrelevant to the current task
- Information already expressed in conventions or tool definitions
- Codebase structure the agent can discover by reading the repo
- Embedded code snippets or architecture descriptions (use pointers instead)
- Volatile operational data that lives in a system of record (give access, not copies)
- Low-confidence or contradictory sources that create conflicting signals

### The 60-Line Benchmark

Community practice and Anthropic's internal usage converge on 60-80 lines as the sweet spot for context files. Files significantly longer than this should be audited for bloat. One empirical detail worth knowing: tool mentions in context files increase tool usage 160x. Every tool you name in a context file is an implicit instruction to use it.

### Context Sensitivity Is Model-Specific

Claude Code (Sonnet-4.5) was the only agent in the ETH Zurich study where even human-written context files failed to improve performance. Codex benefited from human-written files but was hurt by LLM-generated ones. GPT-5.1 mini exhibited a pathology of repeatedly re-reading context files already in its window. One-size-fits-all context strategies are empirically wrong -- test against your actual model before optimizing.

---

## Step 2: Choose Your Context File Architecture

Context files serve distinct roles. Using a single monolithic file for everything (identity, rules, navigation, conventions, references) creates bloat and prevents selective loading. The emerging taxonomy provides clearer boundaries.

### Context File Taxonomy

| File Type | Purpose | Loaded When | Example |
|-----------|---------|-------------|---------|
| **CLAUDE.md / Project Context** | Project rules, navigation, conventions | Session start (upfront) | Build commands, testing patterns, file conventions |
| **SOUL.md / Agent Identity** | Values, philosophy, behavioral boundaries | Session start (upfront) | Decision principles, communication style, persona |
| **AGENTS.md / Tool-Agnostic Context** | Conventions readable by any AI tool | Session start (upfront) | Cross-platform project conventions |
| **RULES.md / Hard Constraints** | Non-negotiable rules | Session start (upfront) | Safety boundaries, authorization requirements |
| **PROGRESS.md / Session Bridge** | Current state, completed work, next steps | Session start; updated at session end | Task status, blockers, handoff notes |
| **MEMORY.md / Persistent Preferences** | User model, cross-session learnings | Session start (upfront) | User preferences, accumulated observations |
| **SKILL.md / Capability Definition** | Workflow for a specific skill | On-demand (when skill is invoked) | Step-by-step procedure, references, templates |

The practical starting set is three files: CLAUDE.md (project rules + navigation), PROGRESS.md (session bridge), and MEMORY.md (persistent observations). Add others as friction reveals the need, not preemptively.

### Keep the Entry File Minimal and Pointer-Only

The one file the harness injects into *every* request (CLAUDE.md, AGENTS.md, copilot-instructions.md -- whatever the platform's guaranteed entry point is) deserves a stricter rule than the 60-line benchmark: it carries the irreducible minimum and nothing else, because its token cost taxes every request forever. Canon contents:

- **Mission statement** and layer split -- what the system is, in a sentence or two
- **Cold-start load order** -- what a fresh session reads, in what sequence (see below)
- **Standing guards** -- the few rules that can fire on any request (side-effect gates, maintenance rules)
- **Skill and state pointers** -- names and paths, never bodies

Volatile state (active task, current targets, status) appears **pointer-only, never restated** -- "those go stale and leak." A wake-up idiom makes this operational: a bare control-file mention ("PROGRESS", "continue") means *read the named control file and proceed with the recorded next unit of work* -- no recital, no re-priming. The minimalism rule needs an enforcement mechanism (a periodic audit or review gate), or the file regrows: every incident tempts a new always-on paragraph.

### Add a Task-to-File Routing Table

Inside the entry file, a simple markdown table maps task types to exactly what the agent should load -- replacing token-expensive full-directory reads with targeted selective loading:

| Task | Read These Files | Skip These Files | Skills Needed |
|------|-----------------|------------------|---------------|
| Write blog post | voice-context.md, blog-template.md | production-outputs/ | humanizer |

The agent consults the table at the start of any task and loads only the specified files. It is deterministic, human-readable, and trivially maintainable -- a non-technical stakeholder can review what information the agent uses for each task type. Without it, the agent either reads everything (wastes tokens) or guesses wrong about what matters. Keep it honest: a routing table that references renamed or deleted files silently misroutes. The Task-to-File Routing Table Template (Templates section) provides the scaffold.

### Document the Cold-Start Chain -- Then Test It

A fresh session should follow one documented, ordered load path from zero context to working state: entry file → identity/state context → control surfaces → the skill for the task at hand. Two disciplines make the chain durable:

- **Only the first hop is platform-specific.** The chain's first link is whatever file the platform reads unconditionally; every hop after that is a workspace-internal file-to-file pointer that moves unchanged across harnesses. This isolates harness lock-in to a single link.
- **The cold-start test is the standing regression check.** A fresh session, loading only the standard entry points, must be able to state the system's purpose and the next unit of work with zero guidance. Run it after any wiring change; run it as the acceptance test when installing the system on a new harness ("cold-start echo": the fresh session reports what actually composed). Warm sessions mask broken chains for weeks -- context loaded by habit hides missing links until the day a fresh session faceplants.

### Partition Docs by Lifespan, Not Topic

Organize the documentation the agent reads by *how long each document stays true*, not by subject:

| Folder | Contents | Trust Signal |
|--------|----------|--------------|
| `active/` | Living plans, work in flight | Current truth -- follow it |
| `decisions/` | Short records freezing the *why* of each choice | Durable rationale |
| `reference/` | Runbooks, registries, guides | Doesn't expire |
| `archive/` | Finished work, stamped "do not follow" | History only |

The failure this prevents is specific to AI readers and quietly severe: agents weight retrieved docs as current truth, so a shipped plan left in the active pile has the agent "building toward a target you already hit," confidently wrong for sessions on end. Stale docs are worse than no docs -- with no docs the AI asks; with stale docs it charges off certain that it's right. The load-bearing rule is the *transition*: when a plan ships, it moves to `archive/` and gets stamped. Location encodes trust, so the router can say "read active/ for current work" without per-document freshness judgments.

### Pointers Over Copies

Context files should point to canonical sources rather than embedding copies:

```
# Instead of this:
The fractal pattern has 7 folders: app/, governance/, knowledge/,
agents/, project-management/, operations/, archive/...
[300 tokens of description]

# Do this:
See the fractal pattern definition: systems/improvement-loop/knowledge/reference/fractal-pattern.md
```

Copies go stale and create contradictions when the source changes but the copy does not. Pointers always read the current state. The exception: project intent, trade-off philosophy, and other information with no canonical file location genuinely belongs inline.

This principle scales to skills, where it becomes an **update multiplier**. Once a centralized shared-context folder exists (brand voice, domain definitions, client details -- whatever all skills need), each skill references it by path and reads it fresh at execution. Update the folder once and every skill gets the update on its next run. Without it, at 20+ skills, updating one fact means editing 20+ files, and in practice some get updated and others don't -- inconsistent outputs where one channel uses the new voice and another the old. As the skill count grows, the value of the shared folder grows proportionally. Caveat: pointer-only architectures assume the pointed-to surface is reliably loadable -- a broken pointer is worse than a stale copy because nothing visibly fails.

### Design for Your Actual Reader

When the primary consumer of a knowledge base is an AI agent, optimize for machine processing:

- **More node types are better.** A single "note" type forces the agent to read content to understand what kind of knowledge it is. A typed taxonomy (decision, concept, pattern, source) lets the agent filter by type before reading.
- **More edge types are better.** Untyped links ("these are related") force the agent to read both endpoints to understand the relationship -- the primary structural cause of token waste in PARA-style knowledge bases. Typed edges (supports, contradicts, depends-on, part-of, preceded-by) let the agent prune traversal paths without loading documents: the same data and query cost ~9,000 tokens over untyped links versus ~600 over typed edges. Typing costs a moment at write time and pays on every traversal. Two cautions: a *mis-typed* edge is worse than an untyped one (the agent trusts it and prunes wrongly), and vocabularies past ~10-20 types become ambiguous to classify against.
- **Metadata density should increase.** YAML frontmatter, one-sentence summaries, and typed edges are cheap overhead for an agent that reads metadata faster than prose.

This does not mean abandoning human readability. The solution is dual-layer: rich metadata for agent consumption, with human-friendly views (Dataview, generated summaries) rendered from the same underlying data. But when human navigability and agent efficiency conflict, bias toward agent efficiency -- the agent is the primary reader.

### Consider a Standard Knowledge Format

The folder-of-markdown knowledge base now has a vendor-published open spec: OKF (Open Knowledge Format, Google Cloud, June 2026). A "bundle" is a directory of markdown files -- one concept per file, YAML frontmatter with `type` as the only required field, a reserved `index.md` table of contents for navigation, an append-only `log.md` change log, and ordinary markdown links that make the bundle a walkable graph. The category distinction worth internalizing: **RAG is a process, OKF is a format** -- RAG re-derives meaning from raw chunks at query time; a curated bundle stores concepts the agent reads directly, and can also *feed* a RAG pipeline as clean pre-labeled source.

Why standardization matters: every hand-rolled wiki structures metadata differently, so nobody's agent can consume anybody else's knowledge base -- small divergences compound into non-interoperability. A shared format makes knowledge bases consumable and producible by any conformant agent, and turns curated expertise into a shareable, git-cloneable artifact. Practical guidance: for a private KB, a bespoke schema with richer typing is fine (and often better); if the KB will ever be shared, consumed by external agents, or distributed, target the standard -- or the conservative middle, bespoke internals with a conformant export. The spec is v0.1 and single-vendor: bookmark it, don't bet the company on it.

### Self-Describing Codebases

Context engineering extends to the codebase itself. Two structural layers make code legible to agents without tribal knowledge:

- **Structural context (answers "where").** Every module gets a manifest: what it does, what it depends on, what depends on it. Agents read the manifest instead of reverse-engineering import graphs.
- **Semantic context (answers "what").** Every interface carries a behavioral contract: performance expectations, failure modes, retry semantics. This goes beyond data shape -- the agent gets the rules of engagement.

The Module Manifest Template (Templates section) provides a starter format.

---

## Step 3: Tier Your Context for Selective Loading

### 3a: File-Granularity Tiering (Which Files to Load)

Instead of loading everything into every interaction, categorize files by when they are needed:

| Tier | What Goes Here | When Loaded | Token Budget |
|------|---------------|-------------|--------------|
| **Tier 0 (Always-On)** | Identity, safety constraints, hard rules, navigation | Every interaction | < 20 lines |
| **Tier 1 (Task-Scoped)** | Coding conventions when coding, test patterns when testing, review criteria when reviewing | When task type is detected | Varies by task |
| **Tier 2 (On-Demand)** | Architecture docs, dependency references, detailed specifications | When agent signals need | Retrieved JIT |

ETH Zurich data shows task-relevant instruction subsets reduce context by 60-80% while maintaining or improving accuracy. The cost savings alone (20%+ reduction in inference cost) justify the structural investment.

**Path-scoped guardrails** are the sharpest form of Tier 1: conditional instruction files the harness auto-applies only when the agent touches files matching a path pattern. The rule fires exactly when the risk exists -- editing a protected tree -- without paying always-on cost, and prevention at edit time complements post-hoc audit scripts. Where the platform lacks path-conditional injection, the fallback is folding the rules into the always-on file and recording the weaker guarantee.

### 3b: Content-Granularity Tiering (How Much of Each File to Load)

File-granularity tiering (3a) decides *which files* to load. Content-granularity tiering decides *how much of each file* to load. Six independent implementations converge on this three-tier pattern:

| Tier | Size | What It Is | When Read |
|------|------|------------|-----------|
| **L0 -- Abstract** | ~100 tokens | Semantic summary generated at ingest | Initial scoring: "is this relevant at all?" |
| **L1 -- Overview** | ~1-2k tokens | Structural summary, outline, section headings | Reranking: "is this section worth opening?" |
| **L2 -- Full** | Unbounded | Original content | Final read: "I need this content now" |

The retrieval pipeline scores at L0, reranks at L1, reads at L2 only for top-ranked results. Token budget is enforced at each tier boundary. This addresses the fundamental tension: loading full content for all candidates is wasteful, but loading nothing until selected means the selection has no content signal. The three-tier approach provides content-aware scoring without full-content cost.

### 3c: Shard Large Documents

Break monolithic documents into focused shards. Each agent loads only the shards relevant to its current task:

| Instead Of | Shard Into |
|------------|-----------|
| Full PRD (5000 lines) | `coding-standards.md`, `tech-stack.md`, `data-model.md`, `api-contracts.md` |
| Monolithic CLAUDE.md | Global CLAUDE.md (60 lines) + per-system CLAUDE.md files |
| Single architecture doc | One file per subsystem boundary |

**Sharding rule:** Each shard should be loadable independently without losing critical context. If shard A requires shard B to make sense, they should be one file or the dependency should be explicit.

BMad Method reports 90% token savings from sharding versus loading full documents. The tradeoff: over-sharding creates too many small files, and cross-shard dependencies get missed when loading individual shards. Re-generate shards when source documents change.

### 3d: Scope Capabilities to Nodes and Sub-Agents

Context scoping applies to capabilities, not just documents. Two granularities:

**Per-node scoping in workflows.** Specify which skills, MCP servers, and commands load at each workflow node: a validation node loads a linting skill, a planning node connects a documentation MCP server, an implementation node gets full tool access, a classification node gets nothing. In a 10-node workflow, loading everything into every node wastes budget and introduces irrelevant instructions -- "nothing more" applied at workflow granularity.

**Inline MCP servers per sub-agent.** MCP servers can be defined inline in a sub-agent's frontmatter so the server connects when the sub-agent starts and disconnects when it finishes. The MCP tools and their descriptions never enter the parent conversation's context:

```yaml
---
name: browser-tester
description: Tests features in a real browser using Playwright
mcpServers:
  - playwright:
      type: stdio
      command: npx
      args: ["-y", "@playwright/mcp@latest"]
  - github  # reference: reuses session's server
---
```

A typical tool-heavy MCP server is 4K-10K tokens of tool descriptions. Scoping it to a sub-agent eliminates that per-turn cost from the parent conversation. This also provides safety-by-default: tools with destructive capabilities live in specialized sub-agents where the parent cannot accidentally invoke them.

**Tradeoff:** Inline MCP servers connect fresh each invocation, adding cold-start latency for heavyweight servers. Use reference-mode (sharing the parent's connection) for frequently-used servers.

### 3e: Enforce Hard Ceilings on Memory Files

Memory files without size limits balloon silently. Apply hard character ceilings with tiered architecture:

| Tier | Behavior | Example Ceiling |
|------|----------|-----------------|
| **Hot (always-injected)** | Loaded verbatim into every session; highest-signal entries compete for space | MEMORY.md: 2,200 chars |
| **Warm (retrieved on demand)** | Full-text search surfaces relevant entries; LLM-summarized before injection | SQLite FTS5 over prior sessions |
| **Cold (archival)** | Raw timestamped records for auditing and re-promotion; not loaded at runtime | JSONL transcripts |

Writes should be triggered by conversation-pattern inference, not explicit "remember this" commands. A Curator step runs on overflow: it reads the current file, consolidates/evicts low-signal entries, and rewrites the hot-tier file to fit within the ceiling. Fixed ceilings + inference-driven writes + LLM curation = self-maintaining user model that degrades gracefully. (The full write-policy and cross-session design space is G7's territory.)

---

## Step 4: Engineer Skill Loading

Skills are the largest structured loading surface in modern harnesses, and they have concrete, published economics. Design against them.

### 4a: The Three-Level Disclosure Model

A skill is a filesystem directory: a required SKILL.md plus optional `scripts/`, `references/`, and `assets/`. Content loads in three levels:

| Level | Content | Cost | When Loaded |
|-------|---------|------|-------------|
| **1 -- Metadata** | Frontmatter `name` + `description` | ~100 tokens per skill | Always (system prompt at startup) |
| **2 -- Instructions** | Full SKILL.md body | <5K tokens recommended | On activation |
| **3 -- Resources** | Bundled files and scripts | Effectively unbounded | Only when read; scripts execute without entering context |

This decouples *capability presence* (cheap, always visible) from *capability detail* (paid only on invocation) from *capability execution* (decoupled from context entirely for scripts). An agent can carry dozens of skills at the system-prompt cost of a short paragraph each. The pattern has migrated into framework primitives (Pydantic AI 2.0 capabilities implement the same catalog/full-load split) -- treat it as the canonical instance of Key Concept 3.

### 4b: Budget the Description Layer

Level 1 is the router, and it has a hard budget. In Claude Code: ~1% of the context window for all skill descriptions combined (configurable), with a 1,536-character per-entry cap on `description` + `when_to_use`. Do the math for your library: at 1% of a 200K window (~2K chars), only a handful of full descriptions fit; past the budget, least-recently-used descriptions are dropped (names always retained) -- and the keywords the model needs to match a request may be stripped *before it ever sees them*. The skill then appears to undertrigger for no visible reason.

Operational discipline:

- **Front-load the highest-signal use case** in every description -- truncation cuts the tail, so what dies first is whatever you put last (one enterprise system found truncation silently killed its collision-protection clauses, which lived at the end).
- **Author to a soft cap** (~1,000 chars) well under the hard cap.
- **Demote background skills** (`name-only` or `off` overrides) to free budget for the skills the project leans on.
- **Diagnose reactively** with the harness doctor tooling -- but expect no automatic warning when the budget gets tight.

### 4c: Write for the Content Lifecycle

When a skill activates, its rendered body enters the conversation as a single message and stays there -- the harness does not re-read the file on subsequent turns. At auto-compaction, Claude Code preserves the most recent invocation of each skill: the **first 5K tokens per skill, 25K combined budget, oldest invocations dropped first**. Authoring consequences:

- **Front-load critical guidance.** Anything past the first 5K tokens of the body is at risk after compaction. Behavior changes mid-session that look like model drift are often content drift.
- **Write standing instructions, not one-time setup steps.** The body is re-read from context on every turn; phrase guidance as invariants ("always X", "never Y") rather than ordered steps the model may re-execute on turn 12.
- **Treat compaction as soft state-loss** in skill-heavy sessions: 8 loaded skills exceed the 25K budget and the oldest are dropped entirely. Re-invoking a skill is the recovery primitive.

### 4d: Inject Live State at Activation

Skills can embed shell commands (`` !`git diff HEAD` ``) that run at activation time; the output replaces the placeholder before the model sees the prompt. This converts a first-turn tool call ("start by checking the diff") into preprocessing: the skill sees live state with zero round trips. Caveats: substitution happens once at activation -- the captured state freezes and goes stale across turns (re-invoke to refresh); command failures are silently captured; and untrusted skills can abuse activation-time execution, which is why a policy switch to disable it exists.

### 4e: Place Reference Material by Branch Analysis

SKILL.md should be small and reference material externalized -- but not all of it. The decision rule: enumerate the skill's *branches* (the distinct, mutually exclusive things it can do), then:

- Reference used on **every branch** stays inline. Externalizing it just adds a read round-trip that always happens.
- Reference used on **only some branches** moves behind a context pointer: "if you need X, read `references/x.md`."

A one-branch skill (find context → confirm → write output) keeps its template and explainer inline; a skill that does two different things (update a glossary; create ADRs) moves both templates behind pointers.

### 4f: Consolidate Big Families into Hubs

When a family of related skills grows, flat listing inflates the always-on index (Level 1 costs scale linearly) and descriptions start colliding. The hub-and-spoke response: consolidate the family behind one **hub** skill whose description is a domain router and whose body is a routing table, with the depth pushed into `references/` **spokes** that are never indexed individually. A family of 8-30 topics then costs exactly one description in the always-on index, and depth stays unbounded.

The countable trigger: hub at **≥8 siblings** (existing or confidently expected). Below the threshold, do NOT hub -- a hub over 3 spokes adds an indirection hop without meaningfully shrinking the index. Both failure sides are real: flat lists past ~8 siblings bloat the index and mushy-up routing; premature hubs cost a hop on every use for no savings. Watch for over-stuffed hubs (30+ spokes → mushy routing table, split candidate) and hidden spokes (a spoke filed under the wrong hub is unreachable, because spokes are unindexed).

---

## Step 5: Design Your Retrieval Strategy

### Choose Storage Format by Query Shape

Before choosing retrieval, choose storage -- backwards from the questions you will ask. Three query shapes map to three storage answers:

| Anticipated Query Shape | Example | Right Storage | Wrong Storage Fails How |
|------------------------|---------|---------------|------------------------|
| **Whole-object synthesis** | "Summarize the March 5th meeting" | One markdown file, read in full | Vector chunking returns ~5 similarity-matched chunks of a 20-chunk doc; the summary silently covers a quarter of the meeting |
| **Pinpoint lookup in bulk text** | "What was rule 17 of our 1,000 rules?" | Vector/semantic snippet lookup | Whole-file reads waste time and tokens for one line |
| **Relationship trace** | "Trace topic X back to decision A" | Graph with typed edges | Flat files and untyped backlinks force exhaustive multi-hop reads |

The anticipated query shape -- not the data's topic or size -- is the storage-format decision input. Practical procedure: describe the data and intended usage to the agent itself and ask which format fits. Usage drifts, so expect to retrofit per corpus (next section).

### The Retrieval Strategy Decision Tree

```
Is your corpus under ~1000 documents?
  YES --> Default to file search (grep, glob, file traversal)
          Add semantic search only when lexical misses become frequent
  NO  --> Use semantic search as the primary strategy
          Keep file search for exact-term queries (identifiers, error codes)

Do you have relationship-heavy knowledge (dependency graphs, cross-references)?
  YES --> Add graph traversal (wikilink-based, N-level deep)
  NO  --> Lexical + semantic is sufficient

Can you give the agent multiple retrieval tools?
  YES --> Let the agent choose per query (agentic RAG)
  NO  --> Pick the single strategy that matches your dominant query type
```

### Three Complementary Retrieval Modes

| Mode | Mechanism | Best For | Weakness |
|------|-----------|----------|----------|
| **Lexical search** (grep, glob, file traversal) | Exact text matching, directory navigation | Small corpora; exact terms, identifiers, error messages | Misses conceptually related content that does not share lexical terms |
| **Semantic search** (embedding-based vector similarity) | Fuzzy/conceptual queries | Large corpora; conceptual queries ("how does authentication work?") | Under 20% Recall@100 on combinatorial queries; lossy compression inherent in embeddings |
| **Graph traversal** (wikilink-based, relationship queries) | Multi-hop relationship exploration | Connected knowledge; "what depends on X?"; N-level-deep traversal | Requires structured graph; over-linked graphs degrade into noisy crawls |

The practical path is incremental: start with file search (zero infrastructure), add semantic search when corpus scale demands it, add graph traversal when relationship queries become frequent. Cost-aware routing can prefer cheaper retrieval when accuracy is comparable.

### Assign Retrieval Levels Per Folder -- and Upgrade Only on Pain

A knowledge base is not one retrieval architecture. Each folder gets the retrieval level its data shape and query shape deserve, on a five-level ladder:

1. **Routing files + folders** -- find things by exact name; the entry file as router
2. **LLM wiki** -- index files, concept pages, backlinks; whole-page reads
3. **Semantic search** -- meaning-match when you search with different words than you wrote
4. **Knowledge graph** -- typed relationship chains; often cheaper than wikis for entity questions
5. **Always-on autonomous brain** -- constant sync/refresh/ingest pipelines

Two rules govern the ladder. **Per-folder assignment:** one vector-indexed corpus (say, transcripts) can sit beside plain-markdown decision and project folders -- the whole system does not fit one level. **Pain-driven upgrades:** find the *lowest* level that fits, and upgrade a folder only when a concrete symptom is felt. The symptom map: re-explaining your setup → level 1 routing is missing; 30+ notes you keep forgetting → level 2 wiki; whiffing on notes you know exist → level 3 semantic; needing relationship chains → level 4; syncing fleets of agents over huge data → level 5. Production practitioners run entire business brains at level 2 and decline higher levels: "if there's not pain, why create more?" Heterogeneity's coordination cost: the router must record which retrieval mechanism each folder uses, or queries get mis-dispatched -- keep a per-folder retrieval manifest (Templates section).

### The Hybrid Upfront/JIT Architecture

Combine two loading modes for the best tradeoff between speed and efficiency:

| Mode | What Goes Here | Why |
|------|---------------|-----|
| **Upfront (always loaded)** | Small, high-signal files: CLAUDE.md, system prompt, persona, tool definitions | Immediate availability, no retrieval latency, cacheable |
| **Just-in-time (retrieved on demand)** | Everything else: docs, code, reference material, detailed specs | Context efficiency -- load only when needed |

This is Claude Code's production architecture. Anthropic explicitly chose it over RAG/index approaches, citing stale indexing and syntax-tree complexity as problems. The upfront layer should be small enough that it does not crowd out task-specific context. The JIT layer uses filesystem primitives (glob, grep, read) rather than embedding-based retrieval for small-to-medium corpora.

### Use CLAUDE.md as a Traversal Guide

For knowledge-base-heavy projects, CLAUDE.md serves double duty: project rules plus a navigation protocol:

- Where to find the master index
- How to read per-section indexes and follow links
- File structure conventions for new files (so the agent maintains navigability)
- What to read first versus what to retrieve on demand

Without traversal instructions, agents use expensive tool calls (glob, grep) to discover structure on every query. With a navigation protocol, the agent follows a deterministic 2-3 file read path: master index, section index, target file.

### Outline Before Read (Code Corpora)

For codebases, insert a structural step between "find the file" and "read the file": pull a compact outline -- functions, classes, imports, exports with line numbers -- and use it to decide what to actually read. Author-measured benchmarks (ast-grep outline, 7 real repos): 35-55% cost reduction on large repos (VS Code, Django, OkHttp) at 100% of baseline answer coverage. The critical caveat is the **size gate**: on repos under ~1,000 files the pattern inverted and *added* cost -- grep and direct reads were already cheap. Probe corpus size first; choose outline vs grep accordingly. This is content-granularity tiering (Step 3b) applied to source code: shape first, members on demand, full source last.

### Use Summary Gates for Inter-Document Navigation

Each knowledge-base node carries a mandatory one-sentence summary (~50 tokens) that the agent reads before deciding whether to load the full document (~500+ tokens). This creates a two-phase retrieval:

1. **Scan:** Agent reads node summaries and edge types from the current node's neighbors.
2. **Select:** Agent decides which neighbors are relevant to the current query.
3. **Load:** Agent reads full content of selected nodes only.

One practitioner reports that summary gates combined with typed edges reduced token consumption from ~9,000 to ~600 for equivalent queries -- a ~93% reduction. Write summaries for agent triage, not human readability. A formulaic summary ("This is about X") is less useful than a discriminating summary ("X differs from Y because Z").

### Compose a Retrieval Pipeline: Decompose, Fuse, Rerank

When retrieval quality matters more than infrastructure simplicity, production memory systems converge on a three-stage recipe:

1. **Decompose the query.** A lightweight LLM rewrites the user's query into several targeted sub-queries before any expensive semantic work. Sub-queries fan out in parallel across the available indexes.
2. **Fuse ranked lists.** Run each sub-query against both semantic and lexical indexes; merge the result sets with reciprocal rank fusion (RRF) or weighted score fusion. Database-native fusion primitives (e.g., MongoDB Atlas `$rankFusion` over `$vectorSearch` + BM25 `$search`) do this without an external reranker service.
3. **Rerank with inspectable signals.** Score candidates as a weighted sum of explicit signals -- e.g., quoted-phrase match (0.60), temporal proximity (0.40), entity match (0.40), keyword overlap (0.30). Human-inspectable weights make the rerank stage auditable and tunable without retraining a learned reranker.

This pipeline is overkill for a sub-1000-document markdown KB (the decision tree above still applies) -- reach for it when a large corpus must serve fuzzy, multi-faceted queries and single-strategy retrieval measurably misses.

### Offload to External Knowledge Bases

When reference material exceeds what fits efficiently in the context window:

- **NotebookLM** for project-specific research, YouTube transcripts, and accumulated reference material. The agent queries it on demand, keeping the context window lean. The "grounded" aspect is critical -- NotebookLM uses only sources you provide, eliminating hallucination from the knowledge layer.
- **Obsidian wiki with index navigation** for internal codebase memory and institutional knowledge. Effective for under 1000 documents with zero infrastructure overhead.
- **Personal knowledge hoards** for worked examples, solved problems, and domain-specific idioms. A distributed personal corpus (blog posts, small repos, TIL notes, single-page tools) becomes raw material the agent recombines into new artifacts. The hoard is cheap to maintain and expensive to replace -- your idioms, your frameworks, your worked examples give the agent your priors on tap rather than generic output.

For bulk organizational data too large to query directly (recordings, message archives), apply the **progressive distillation pipeline**: raw capture → categorize into semantic areas → synthesize each area into a coherent knowledge artifact (a manual, a decision log) → give the agent *breadcrumbs* (pointers to the synthesized artifacts), never the raw pile. Each stage reduces volume while preserving what matters; YC regenerated a 150-page user manual from 2,000 hours of recordings this way. The agent navigates breadcrumbs to synthesized content on demand.

The principle: keep task context in the window, keep reference context queryable externally.

### Prevent KB Poisoning: Query-Time vs. Write-Time Synthesis

When agents write content back into the knowledge base they query, the chain of custody breaks:

| Strategy | When Synthesis Happens | Trust | Cost |
|----------|----------------------|-------|------|
| **Write-time** (Karpathy pattern) | At ingest: LLM authors summaries stored alongside originals | Lower (agent-authored text in the index) | Lower per-query |
| **Query-time** | At retrieval: LLM synthesizes on demand from originals | Higher (originals intact) | Higher per-query |

Three principles for maintaining KB integrity:
1. **Immutable originals.** Never overwrite source documents with LLM-authored versions.
2. **Structure over prose.** Prefer structured fields (tags, links, dates) over LLM-generated narrative in index entries.
3. **Query-time synthesis as default.** Accept the higher per-query cost to preserve trustworthiness.

---

## Step 6: Curate Context for Downstream Agents

When dispatching work to sub-agents, do not pass your full context window. Produce a self-contained context package with exactly what the sub-agent needs:

- Relevant architecture sections (not the full doc)
- Task-specific constraints (not all system constraints)
- Carry-forward notes from prior steps when dependencies exist
- Acceptance criteria for the sub-agent's output
- Purpose, audience, and workflow position (context enrichment)
- Scoped MCP servers declared inline (Step 3d)

The sub-agent should never need to search for information to start working. If it does, the context curation was incomplete. This is the "scrum master" pattern: a curator agent reads multiple sources and produces a context-complete handoff file so the executing agent starts with a focused, complete window.

### Make Work Packages Fully Self-Contained

For headless or queued dispatch, harden the pattern: each unit of work is a prompt that assumes access to *only* the prompt content plus the filesystem -- no orchestrator conversation history, no prior phases' execution details beyond what's in committed files. A well-crafted package includes the goal and scope, which files to focus on, conventions to follow, verification criteria for "done," and constraints from prior phases expressed as file references, not conversation. This front-loads context engineering into planning time rather than execution time, and it is what makes work units dispatchable to fresh sessions at all.

### Compress the Return Path

The boundary works in both directions. Each completed sub-agent or headless session should return only a **condensed result** -- what was done, what changed, whether verification passed -- never the full execution log or transcript. The orchestrator ingests a few hundred tokens instead of tens of thousands, and uses them only for dispatch decisions (is this done? what's next?). This explicit lossy-compression boundary at every return is what keeps a long-running orchestrator lean across 100+ dispatches; the detail remains recoverable from the filesystem and logs, not from the orchestrator's window.

### Multi-Agent Shared Memory Architecture

In multi-agent systems, agents communicate through shared memory layers rather than direct message passing:

| Layer | Artifact | Purpose | Persistence |
|-------|----------|---------|-------------|
| **Working** | PROGRESS.md | Current task state | Session-scoped; bridged across sessions |
| **Episodic** | agent-log/, system-log/ | History of past runs | Append-only; auditable |
| **Semantic** | reference/, knowledge/ | Durable domain knowledge | Versioned; rarely changes |
| **Procedural** | skills/ | Reusable capabilities | Versioned; evolves with the system |

Shared layered memory decouples agents, makes state inspectable, and enables governance -- you can reconstruct what happened by reading the logs rather than replaying message chains. Design governance logging in from day one.

### Mid-Session Context Management (Decision Matrix)

During a session, five canonical primitives handle different context situations:

| Situation | Technique | Rationale |
|-----------|-----------|-----------|
| Same task, relevant context | **Continue** | Everything in the window is still load-bearing |
| Wrong path taken | **Rewind** (Esc+Esc) | Keep file reads, drop failed attempt |
| Bloated session, stale debugging | **Compact** `/compact <hint>` | Low effort; model decides what mattered |
| Genuinely new task | **Clear** `/clear` | Zero rot; you control what carries forward |
| Next step generates excess output | **Sub-agent** | Intermediate noise stays in child context |

Two decisions this crystallizes: rewind is the default correction (not forward-patching with "that didn't work, try X"), and sub-agent invocation is governed by the test "will I need this tool output again, or just the conclusion?"

---

## Step 7: Bootstrap a New System Efficiently

When starting from zero, a single declarative PRD prompt can scaffold the entire system (folders, scripts, hooks, agents, indexes) in one pass. The PRD captures the "why" alongside the "what," enabling the agent to make intelligent decisions about implementation details that a script would hardcode.

This eliminates the token cost of iterative back-and-forth scaffolding. The Bootstrap Context Template (Templates section) provides a starter format.

For documentation of ongoing behavior -- especially for systems with spatial or temporal algorithms -- consider pairing a linear walkthrough (structure: what is where, how files relate) with an interactive explanation (behavior: what actually happens when the algorithm runs). They are complementary, not substitutes: linear when organization is the question, interactive when behavior in space or time is the question.

---

## Templates

### Context File Template (Tiered)

For designing new context files with built-in tiering:

| Variable | Type | Required | Description |
|----------|------|----------|-------------|
| `CONTEXT_FILE_NAME` | string | Yes | Name of the context file |
| `AGENT_ROLE` | string | Yes | One-sentence role description |
| `RULE_N` | string | Yes (1+) | Hard rules the agent must always follow |
| `NEED_N` / `PATH_N` | string | Yes (1+) | Navigation pairs: what the agent needs and where to find it |
| `CONVENTION_N` | string | Optional | Task-scoped conventions by operation type |
| `CONCEPT_N` / `REF_PATH_N` | string | Optional | Pointer to reference material (not embedded copies) |

```markdown
# {{CONTEXT_FILE_NAME}}

## Identity (Tier 0 -- always loaded)
{{AGENT_ROLE}}

## Hard Rules (Tier 0 -- always loaded)
- {{RULE_1}}
- {{RULE_2}}

## Navigation (Tier 0 -- where to find things)
| Need | Where |
|------|-------|
| {{NEED_1}} | {{PATH_1}} |
| {{NEED_2}} | {{PATH_2}} |

## Task Conventions (Tier 1 -- loaded per task type)
### When Coding
- {{CODING_CONVENTION_1}}

### When Testing
- {{TESTING_CONVENTION_1}}

### When Reviewing
- {{REVIEW_CONVENTION_1}}

## References (Tier 2 -- pointers, not copies)
- {{CONCEPT_1}}: see {{REF_PATH_1}}
```

### Worked Example: Minimal CLAUDE.md for a Code Agent

```markdown
# Code Agent

## Identity (Tier 0)
TypeScript backend developer for the payments service.

## Hard Rules (Tier 0)
- Never modify database schemas without migration files
- All API changes require OpenAPI spec update
- No direct SQL -- use the query builder

## Navigation (Tier 0)
| Need | Where |
|------|-------|
| API contracts | src/api/openapi.yaml |
| Data model | src/db/schema.prisma |
| Test patterns | docs/testing-guide.md |
| Deployment | ops/deploy.md |

## Task Conventions (Tier 1)
### When Coding
- Use Result<T, E> for error handling, never throw
- Integration tests for every new endpoint

### When Testing
- Seed data via fixtures in test/fixtures/
- Mock external services, never call production

## References (Tier 2)
- Architecture decisions: see docs/decisions/
- Service boundaries: see docs/architecture.md
```

---

### Task-to-File Routing Table Template

For deterministic selective loading inside an entry context file:

| Variable | Type | Required | Description |
|----------|------|----------|-------------|
| `TASK_TYPE_N` | string | Yes (1+) | A recurring task category the agent performs |
| `READ_FILES_N` | string | Yes | Files that must be loaded for this task type |
| `SKIP_FILES_N` | string | Optional | Files/directories explicitly not to load |
| `SKILL_N` | string | Optional | Skill(s) to invoke for this task type |

```markdown
## Task Routing (read this table first; load only what your task row lists)

| Task | Read These Files | Skip These Files | Skills Needed |
|------|-----------------|------------------|---------------|
| {{TASK_TYPE_1}} | {{READ_FILES_1}} | {{SKIP_FILES_1}} | {{SKILL_1}} |
| {{TASK_TYPE_2}} | {{READ_FILES_2}} | {{SKIP_FILES_2}} | {{SKILL_2}} |
| Anything not listed | Ask before loading broadly | -- | -- |
```

### Worked Example: Routing Table for a Research Engine

```markdown
## Task Routing (read this table first; load only what your task row lists)

| Task | Read These Files | Skip These Files | Skills Needed |
|------|-----------------|------------------|---------------|
| Process new source URLs | operations/references/research-dimensions.md | research-findings/ (bulk) | /research-loop |
| Answer a KB question | relevant finding files via grep on category | research-sources/ | /ask-kb |
| Re-synthesize a guide | operations/references/guide-routing-table.md, cluster findings | unrelated dimensions | /synthesize-guide |
| Governance change | ../../CHARTER.md, governance/FOUNDATIONS.md | operations/ reports | /dd |
| Anything not listed | Ask before loading broadly | -- | -- |
```

---

### Sub-Agent Context Package Template

For curating context when dispatching work to sub-agents:

| Variable | Type | Required | Description |
|----------|------|----------|-------------|
| `TASK_NAME` | string | Yes | Name of the delegated task |
| `PURPOSE` | string | Yes | What the result will be used for |
| `AUDIENCE` | string | Yes | Who consumes the sub-agent's output |
| `STEP_N` / `TOTAL_STEPS` | string | Yes | Workflow position |
| `PRIOR_STEP` / `NEXT_STEP` | string | Yes | Dependencies in the pipeline |
| `CRITERION_N` | string | Yes (1+) | Measurable success criteria |
| `CONTEXT` | string | Yes | Relevant context -- paste or link only relevant sections |
| `CARRY_FORWARD` | string | Optional | Decisions or constraints from prior steps |
| `CONSTRAINT_N` | string | Optional | Boundaries for the sub-agent |
| `RETURN_SHAPE` | string | Yes | The condensed result the sub-agent must return (not a transcript) |

```markdown
## Context Package -- {{TASK_NAME}}

### Purpose
{{PURPOSE}}

### Audience
{{AUDIENCE}}

### Workflow Position
{{STEP_N}} of {{TOTAL_STEPS}} -- depends on {{PRIOR_STEP}}, feeds into {{NEXT_STEP}}

### Success Criteria
- [ ] {{CRITERION_1}}
- [ ] {{CRITERION_2}}

### Required Context
{{CONTEXT}}

### Carry-Forward Notes
{{CARRY_FORWARD}}

### Constraints
- {{CONSTRAINT_1}}
- {{CONSTRAINT_2}}

### Return
{{RETURN_SHAPE}}
```

### Worked Example: Context Package for Finding Extraction

```markdown
## Context Package -- Extract Pattern from "context-rot-mitigations"

### Purpose
Produce a structured pattern artifact (Problem/Forces/Solution) for guide synthesis.

### Audience
Guide synthesizer agent, then human reviewer.

### Workflow Position
Step 3 of 4 -- depends on identification report (step 2), feeds into guide synthesis (step 4).

### Success Criteria
- [ ] Problem statement captures the silent-degradation mechanism
- [ ] Forces section identifies at least 3 competing tensions
- [ ] Solution section includes all 4 mitigations from the finding
- [ ] ContractSpec present with preconditions, invariants, governance, recovery

### Required Context
Finding file: systems/improvement-loop/research-findings/context-rot-silent-killer-and-mitigations.md
Pattern template: systems/improvement-loop/knowledge/templates/pattern-template.md

### Carry-Forward Notes
Identification report classified this as "pattern" with MED confidence. Co-occurrence with delta-updates finding.

### Constraints
- Write to extracts/patterns/, not to knowledge/patterns/
- Do not modify the source finding file

### Return
Absolute path of the written artifact + a 3-line summary (form, confidence, open questions). No transcript.
```

---

### Module Manifest Template

For self-describing codebases. Drop one into each significant module directory.

| Variable | Type | Required | Description |
|----------|------|----------|-------------|
| `MODULE_PATH` | string | Yes | Path to the module directory |
| `MODULE_PURPOSE` | string | Yes | One-sentence description |
| `DEPENDENCY_N` / `WHY_NEEDED` | string | Yes (1+) | Inbound dependencies with rationale |
| `CONSUMER_N` / `WHAT_CONSUMED` | string | Yes (1+) | Outbound consumers |
| `INTERFACE_NAME` | string | Yes (1+) | Public interface identifier |
| `BEHAVIOR` | string | Yes | How the interface behaves (not just data shape) |
| `PERFORMANCE` | string | Optional | Latency or throughput expectation |
| `FAILURE_MODES` | string | Yes | What breaks and how it surfaces |
| `RETRY_SEMANTICS` | string | Yes | Idempotent or not, and retry guidance |
| `CONSTRAINT_N` | string | Optional | Constraints callers must respect |

```markdown
# Module Manifest -- {{MODULE_PATH}}

## Purpose
{{MODULE_PURPOSE}}

## Dependencies In (this module needs)
- {{DEPENDENCY_1}}: {{WHY_NEEDED}}

## Dependencies Out (these depend on this module)
- {{CONSUMER_1}}: {{WHAT_CONSUMED}}

## Public Interfaces

### {{INTERFACE_NAME}}
- **Behavior:** {{BEHAVIOR}}
- **Performance:** {{PERFORMANCE}}
- **Failure modes:** {{FAILURE_MODES}}
- **Retry semantics:** {{RETRY_SEMANTICS}}

## Constraints
- {{CONSTRAINT_1}}
```

### Worked Example: Module Manifest for a Researcher Agent

```markdown
# Module Manifest -- systems/improvement-loop/agents/researcher/

## Purpose
Stage 1 of the IL pipeline -- intake research sources, extract findings, write to KB.

## Dependencies In
- research-dimensions.md: filters what counts as in-scope research
- _schema.yaml: frontmatter contract for finding/source/authority files
- watched-libraries/, watched-blogs/: source registries for monitoring loops

## Dependencies Out
- agents/codifier/: consumes pipeline_status: classified findings as Stage 2 input
- agents/librarian/: reads the KB to answer queries (no write coupling)

## Public Interfaces

### /research-loop
- **Behavior:** Periodic research scan; produces delta report and writes findings. Idempotent on the same source set.
- **Performance:** ~1-2 minutes per source for Pass 1.
- **Failure modes:** Network failures on Perplexity/WebFetch surface as partial reports; partial writes detectable via missing pipeline_status frontmatter.
- **Retry semantics:** Re-running on the same source set is safe (duplicate detection by source URL).

## Constraints
- WRITE access only to research-findings/, research-sources/, research-authorities/.
- READ-ONLY everywhere else.
```

---

### Bootstrap Context Template (One-Shot PRD)

For bootstrapping a new system with a single declarative document:

| Variable | Type | Required | Description |
|----------|------|----------|-------------|
| `SYSTEM_NAME` | string | Yes | Name of the system being bootstrapped |
| `SYSTEM_PURPOSE` | string | Yes | What the system does |
| `FOLDER_N` / `FOLDER_PURPOSE_N` | string | Yes (1+) | Directory structure with rationale |
| `FILE_N` / `FILE_CONTENT_N` | string | Yes (1+) | Key files and their initial content descriptions |
| `CONVENTION_N` | string | Yes (1+) | Naming, formatting, and structural conventions |
| `CONSTRAINT_N` | string | Optional | Boundaries the scaffold must respect |

```markdown
# Bootstrap PRD -- {{SYSTEM_NAME}}

## Purpose
{{SYSTEM_PURPOSE}}

## Directory Structure
| Directory | Purpose |
|-----------|---------|
| {{FOLDER_1}} | {{FOLDER_PURPOSE_1}} |
| {{FOLDER_2}} | {{FOLDER_PURPOSE_2}} |

## Initial Files
| File | Content |
|------|---------|
| {{FILE_1}} | {{FILE_CONTENT_1}} |
| {{FILE_2}} | {{FILE_CONTENT_2}} |

## Conventions
- {{CONVENTION_1}}
- {{CONVENTION_2}}

## Constraints
- {{CONSTRAINT_1}}
```

---

### Per-Folder Retrieval Manifest Template

For heterogeneous knowledge bases where different folders warrant different retrieval levels:

| Variable | Type | Required | Description |
|----------|------|----------|-------------|
| `FOLDER_N` | string | Yes (1+) | Folder or corpus path |
| `QUERY_SHAPE_N` | string | Yes | Dominant anticipated query shape (whole-object / pinpoint / relationship) |
| `LEVEL_N` | string | Yes | Assigned retrieval level (1 routing / 2 wiki / 3 semantic / 4 graph / 5 autonomous) |
| `UPGRADE_SYMPTOM_N` | string | Yes | The concrete pain that would justify upgrading this folder |

```markdown
## Retrieval Manifest

| Folder | Query Shape | Retrieval Level | Upgrade When |
|--------|------------|-----------------|--------------|
| {{FOLDER_1}} | {{QUERY_SHAPE_1}} | {{LEVEL_1}} | {{UPGRADE_SYMPTOM_1}} |
| {{FOLDER_2}} | {{QUERY_SHAPE_2}} | {{LEVEL_2}} | {{UPGRADE_SYMPTOM_2}} |
```

### Worked Example: Retrieval Manifest for a Research KB

```markdown
## Retrieval Manifest

| Folder | Query Shape | Retrieval Level | Upgrade When |
|--------|------------|-----------------|--------------|
| research-findings/ | Whole-object (read the finding in full) | 2 -- wiki (frontmatter grep + typed related_findings) | Whiffing on findings known to exist despite category filters |
| research-sources/transcripts/ | Pinpoint (one claim in hours of talk) | 3 -- semantic index over transcripts only | -- (already at level) |
| project-management/design-decisions/ | Relationship (what supersedes what) | 2 -- wiki (frontmatter status + supersession links) | Multi-hop supersession chains exceed 2 hops routinely |
| operations/ reports | Whole-object, rarely queried | 1 -- routing only | Re-explaining where reports live |
```

---

### Context Budget Worksheet

For auditing token allocation across context categories:

| Variable | Type | Required | Description |
|----------|------|----------|-------------|
| `AGENT_NAME` | string | Yes | Agent or skill being budgeted |
| `MODEL_NAME` | string | Yes | Model identifier (context sensitivity varies by model) |
| `WINDOW_SIZE` | number | Yes | Model's context window in tokens |
| `TARGET_PERCENT` | number | Yes | Target max utilization (typically 40-60%) |
| `T0_BUDGET` | number | Yes | Max tokens for always-on cached context |
| `T1_BUDGET` | number | Yes | Max tokens for per-call task context |
| `SKILL_DESC_BUDGET` | number | Yes | Character budget for all skill descriptions (harness-enforced) |
| `HISTORY_LIMIT` | number | Yes | Token threshold for compaction/reset |
| `AUDIT_INTERVAL` | string | Yes | How often to check hidden context sources |

```markdown
## Context Budget -- {{AGENT_NAME}}

**Model:** {{MODEL_NAME}}
**Total context window:** {{WINDOW_SIZE}} tokens
**Target utilization:** {{TARGET_PERCENT}}% (leave headroom for reasoning)

| Category | Elements | Tokens | % of Window | Cached? | Tier |
|----------|----------|--------|-------------|---------|------|
| System prompt | {{ELEMENTS}} | {{COUNT}} | {{PCT}} | {{YES/NO}} | 0 |
| Tool definitions | {{ELEMENTS}} | {{COUNT}} | {{PCT}} | {{YES/NO}} | 0 |
| Skill descriptions (Level 1) | {{N}} skills | {{COUNT}} | {{PCT}} | {{YES/NO}} | 0 |
| Upfront context files | {{FILES}} | {{COUNT}} | {{PCT}} | {{YES/NO}} | 0-1 |
| Task-specific context | {{ELEMENTS}} | {{COUNT}} | {{PCT}} | No | 1 |
| Conversation history | (accumulated) | {{COUNT}} | {{PCT}} | No | dynamic |
| IDE-injected context | (open files, selections) | {{COUNT}} | {{PCT}} | No | hidden |
| **Total** | | {{TOTAL}} | {{TOTAL_PCT}} | | |

### Budget Rules
- Tier 0 (cached) context: max {{T0_BUDGET}} tokens
- Tier 1 (task-scoped) context: max {{T1_BUDGET}} tokens per call
- Skill descriptions: max {{SKILL_DESC_BUDGET}} chars total; demote background skills past the cap
- Conversation history: compact or reset at {{HISTORY_LIMIT}} tokens
- Hidden context (IDE, git status): audit at {{AUDIT_INTERVAL}}
```

### Worked Example: Context Budget for a Research Agent

```markdown
## Context Budget -- Research Loop Agent

**Model:** Claude Opus 4.6 (1M context)
**Total context window:** 1,000,000 tokens
**Target utilization:** 40% (leaves 600K for JIT retrieval and reasoning)

| Category | Elements | Tokens | % of Window | Cached? | Tier |
|----------|----------|--------|-------------|---------|------|
| System prompt | Claude Code system prompt | ~8,000 | 0.8% | Yes | 0 |
| Tool definitions | 12 active tools (from 184 available) | ~4,000 | 0.4% | Yes | 0 |
| Skill descriptions (Level 1) | ~30 skills at ~80 tokens each | ~2,400 | 0.2% | Yes | 0 |
| Upfront context files | Global CLAUDE.md, IL CLAUDE.md, SKILL.md | ~6,000 | 0.6% | Yes | 0-1 |
| Task-specific context | Finding files, source files loaded per-task | ~20,000 | 2.0% | No | 1 |
| Conversation history | Accumulated turns | ~50,000 | 5.0% | No | dynamic |
| IDE-injected context | Open tabs in Cursor | ~10,000 | 1.0% | No | hidden |
| **Total** | | ~100,000 | ~10% | | |

### Budget Rules
- Tier 0 (cached) context: max 20,000 tokens
- Tier 1 (task-scoped) context: max 30,000 tokens per call
- Skill descriptions: max 10,000 chars total (1% of window); demote background skills past the cap
- Conversation history: compact or reset at 80,000 tokens
- Hidden context (IDE, git status): audit at session start
```

---

## Pitfalls

### 1. Treating the context window as a bucket
"We have 200K tokens, let's use them." Every unnecessary token degrades attention on the tokens that matter. The attention mechanism creates n-squared pairwise relationships -- cost is quadratic, not linear. Context management is about minimizing waste, not filling capacity.

### 2. LLM-generated context files
ETH Zurich proved these reduce success rates by 3% while increasing cost by 20%. The agent explores more and tests more -- following instructions faithfully but unproductively. When all repo documentation was removed, LLM-generated files actually improved by 2.7%, proving they duplicate what already exists.

### 3. Embedding content instead of pointing to it
Pasted code snippets, architecture descriptions, and directory trees in context files go stale the moment the source changes. The context file says one thing; the actual code says another. The agent must resolve contradictions that should not exist. Use file path references to canonical sources.

### 4. Relying on embeddings for retrieval
Single-vector embeddings achieve under 20% Recall@100 on combinatorial queries while BM25 achieves 85.7%. For small-to-medium knowledge bases, prefer filesystem navigation (glob/grep), index-file traversal, or hybrid retrieval. Give the agent multiple retrieval tools and let it choose per query rather than hardcoding a single strategy.

### 5. Context duplication across layers
The same constraint stated in the global CLAUDE.md, a system CLAUDE.md, and a skill file consumes 3x the tokens for zero added signal -- and creates subtle contradictions when one copy is updated and the others are not.

### 6. Passing full parent context to sub-agents
A planning agent does not need the full codebase. An editing agent does not need the project roadmap. Scope each agent's context to the minimum it needs. Models perform worse when drowning in irrelevant context.

### 7. One-size-fits-all context strategy across models
Claude Code does not benefit from human-written context files. Codex benefits from human-written files but is hurt by LLM-generated files. GPT-5.1 mini wastes tokens re-reading context files already in its window. Test context strategies against your actual model before optimizing.

### 8. Over-pruning safety constraints
The opposite of bloat is starvation. Aggressive context minimization can remove constraints the agent genuinely needs. Test after pruning -- if the agent starts violating boundaries that were previously respected, the constraint was doing work.

### 9. Formulaic summaries on knowledge nodes
Summaries written as "This is about X" do not help agents discriminate between candidates. Write summaries for triage: "X differs from Y because Z" lets the agent decide without loading the full document. Track how often agents load a full document after reading its summary -- high load rates suggest summaries are not discriminating enough.

### 10. Re-indexing LLM-authored content into the knowledge base
Agent-generated summaries stored alongside originals get retrieved as if they were source material. Over time the KB fills with derivative content and the chain of custody from original source to retrieved fact breaks. Keep LLM-authored content in a separate namespace. When in doubt, synthesize at query time from the original.

### 11. Unbounded memory files without hard ceilings
Memory files that grow without limits accumulate outdated facts, superseded preferences, and irrelevant observations -- all loaded at the start of every session. Apply hard character ceilings, use tiered architecture (hot/warm/cold), and run a Curator step on overflow. A file with no ceiling is not a memory system -- it is an accumulating context tax.

### 12. Skills with embedded copies of shared context
Running 30+ skills that each embed their own copy of shared context (ICP, brand voice, audience persona) means version drift the moment shared truth changes. Migrate to the pointer pattern: shared context lives in a canonical location, skills reference it by path.

### 13. Skill descriptions past the harness budget
Skill descriptions share a hard, harness-enforced budget (~1% of the context window in Claude Code; 1,536-char per-entry cap). Past it, descriptions are truncated or dropped -- and the trigger keywords the model needs are stripped before it ever sees them. The skill silently undertriggers, and adding one new skill can degrade unrelated skills' triggering. Front-load the key use case, author to ~1,000 chars, demote background skills.

### 14. Critical skill guidance buried past the compaction budget
After auto-compaction, only the first ~5K tokens of each invoked skill survive (25K combined across skills, oldest dropped first). A 12K-token SKILL.md silently loses its last 7K mid-session -- behavior changes that look like model drift are content drift. Put the load-bearing instructions first; treat re-invocation as the recovery primitive.

### 15. Finished plans left in the active docs pile
Agents weight retrieved docs as current truth. A shipped plan still sitting in `active/` steers the agent at a target you already hit -- confidently wrong for sessions on end. Stale docs are worse than no docs: with no docs, the agent asks; with stale docs, it charges off certain that it's right. Move finished work to a labeled archive stamped "do not follow."

### 16. Flat skill lists and premature hubs
Both sides of the skill-taxonomy decision fail. A flat list past ~8 siblings inflates the always-on index and mushes routing (descriptions collide). Hubbing a 3-skill family adds an indirection hop for near-zero index savings. Apply the ≥8-sibling threshold in both directions, and audit for spokes filed under the wrong hub -- unindexed spokes in the wrong place are unreachable.

### 17. Broken pointers
Pointer-only architectures assume the pointed-to surface loads reliably. A broken pointer is worse than a stale copy because nothing visibly fails -- the agent simply proceeds without the content. Cold-start tests (Step 2) are the standing check that every hop in the load chain still resolves.

### 18. Ingesting volatile data into the curated store
Copying Slack threads, emails, or live records into the knowledge base creates noise that demands monthly deletion sweeps and contradicts live truth. Apply the one-year test at ingestion; give the agent tool access to the system of record instead of copies.

### 19. Upgrading retrieval infrastructure without felt pain
Adding a vector index or knowledge graph "to be safe" pays permanent coordination and maintenance cost for a symptom nobody has. Find the lowest retrieval level that fits each folder; upgrade only when a concrete symptom appears (whiffed lookups, missing relationship chains). Production systems run entire business brains on routing files and wiki indexes.

---

## Related Guides

- **Defending against context degradation:** Context rot defense, compaction strategy, cost control, and session discipline are covered in *Defending Against Context Degradation* (G2b).
- **Session persistence and memory:** Cross-session memory stores, write policies, run logs, and session bridges are covered in *Session Persistence and Memory* (G7). The retrieval-pipeline mechanics in Step 5 (rank fusion, query decomposition, reranking) are shared substrate with G7's memory-retrieval layer.
- **Tool definition tokens and deferred loading:** If tool definitions are a major context consumer, see *Designing Agent Tools* (G5) for dynamic tool pool assembly and deferred loading patterns.
- **Writing agent specifications:** For defining what the agent should do (rather than what it should know), see *Writing Agent Specifications* (G1).
- **Multi-agent composition:** Sub-agent context curation (Step 6) intersects with single-vs-multi-agent decisions; see *Agent Architecture Decisions* (G3) for composition patterns.
- **Model-specific context sensitivity:** The model-specific findings (Step 1) tie into prompt portability across model upgrades; see *Model-Resilient Prompt Engineering* (G8).

---

## Contract

### Preconditions
- You have an agent system where output quality, cost, or reliability is affected by what the agent sees in its context window.
- You can measure or estimate token usage per agent call.
- You have access to modify context files, agent dispatch logic, or system prompts.
- You know which model your agent uses (context sensitivity is model-specific).

### Invariants
- Every context element loaded into an agent's window has a justifiable reason for being there.
- Context is structured for the agent's retrieval capabilities, not human reading convenience.
- Tiered loading preserves token budget -- always-on context is minimal and pointer-only; everything else is loaded on demand.
- Pointers are used instead of embedded copies for any content with a canonical source location.
- Skill descriptions fit within the harness description budget; skill bodies front-load critical guidance within the post-compaction survival window.
- Storage format per corpus matches the anticipated query shape; retrieval levels are assigned per folder and upgraded only on felt pain.
- Only year-durable knowledge is ingested into curated stores; volatile data is accessed in its system of record.
- Sub-agents receive scoped, self-contained context appropriate to their task, and return condensed results, not transcripts.
- Memory files have hard ceilings with tiered hot/warm/cold architecture.
- Knowledge base structure is optimized for the primary reader (agent or human) with appropriate metadata density.

### Governance
- Context file owners audit their files against the inclusion/exclusion criteria in this guide at least once per milestone.
- Context architecture changes (new upfront files, changed sharding boundaries, tier reassignments, skill hub consolidations) are documented.
- The cold-start test runs after any wiring change and as install acceptance on new harnesses.
- Model-specific context strategies are re-validated when the underlying model changes.
- Module manifests are owned by module owners and updated as part of any breaking-change PR.
- This guide is owned by the Improvement Loop and deployed to the engine knowledge layer after review.

### Recovery
- If agent output quality degrades: run the inclusion/exclusion test (Step 1) first. Context bloat is the most common root cause.
- If token costs spike: check for context duplication, reasoning token amplification from unnecessary instructions, hidden IDE context injection, or upfront loading of content that should be JIT.
- If a skill undertriggers or stops influencing behavior: check description-budget truncation first, then post-compaction content loss (re-invoke the skill), before assuming model drift.
- If retrieval quality drops: audit against the query-shape table and retrieval decision tree (Step 5). Check whether corpus size has crossed the file-search/semantic-search threshold, and whether the folder's retrieval level still matches its query shape.
- If a fresh session cannot orient: run the cold-start test and repair the first failing hop in the load chain.
- If a new model performs differently: re-audit context files with model-specific sensitivity in mind. What worked for Codex may not work for Claude Code.
