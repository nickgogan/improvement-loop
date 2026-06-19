---
title: "Structuring and Loading Agent Context"
type: "guideline"
category: "Context Engineering"
target_system:
  - "improvement-loop"
stage: "draft"
created: "2026-05-25"
updated: "2026-05-25"
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

You are designing the information environment an agent operates inside. This guide covers the structural decisions: what content to include, how to organize it into tiers, how to shard large documents, and how to retrieve context at runtime. The companion guide *Defending Against Context Degradation* (G2b) covers the lifecycle concerns -- rot defense, compaction strategy, and session persistence.

## When to Use This Guide

- You are creating context files (CLAUDE.md, system prompts, skill definitions, agent briefs) for a new agent or refactoring existing ones
- Token costs are higher than expected and you suspect the agent is loading content it does not need
- You are scaling from a single context file to a multi-file architecture and need a tiering strategy
- You are choosing a retrieval approach for a knowledge base the agent will query at runtime
- You are dispatching work to sub-agents and need to decide what context to pass
- You are designing a knowledge base where the primary reader is an AI agent, not a human
- You are bootstrapping a new system and need to decide what goes into the initial context package

**Do not use for:** defending against context rot over time (see G2b: *Defending Against Context Degradation*), defining what the agent should do (see G1: *Writing Agent Specifications*), or designing the agent's tool set (see G5: *Designing Agent Tools*).

## Key Concepts

**1. Less context usually means better output.** ETH Zurich (2026) proved that LLM-generated context files reduce agent success by 3% and increase cost by 20%. The mechanism: irrelevant or contradictory context dilutes attention, creates conflicting signals, and forces the model to resolve ambiguities that should have been resolved by the human during curation. Context files also amplify reasoning token usage by 14-22%, meaning agents spend compute processing instructions rather than solving the task. The discipline is curation -- deciding what not to include -- not coverage.

**2. Structure determines cost more than volume does.** The same knowledge base queried with different structures can cost 15x more per query (9,000 vs 600 tokens). Flat documents force the agent to load everything to find anything. Tiered documents with summaries, typed metadata, and progressive loading let the agent filter cheaply before committing tokens to full reads. Structure is a first-class architectural constraint, not a formatting preference.

**3. Progressive loading is a converged best practice.** Six independent implementations (BMAD, OpenViking, DeerFlow, Beads, Claude Code tool-search, MCP progressive discovery) arrive at the same principle: load minimal metadata first, expand on demand. When unrelated teams independently converge on the same pattern, it is likely a genuine solution rather than a trend.

**4. Retrieval strategy depends on corpus size.** For small knowledge bases (under 1000 documents), file search tools (grep, glob, file traversal) outperform vector-based RAG. For larger corpora, semantic search becomes more accurate and cheaper than exhaustive file search. For relationship-heavy domains, graph traversal handles queries neither method can answer. The right approach is to give the agent multiple retrieval tools and let it choose per query, not to hardcode a single strategy.

**5. When the primary reader is an AI, optimize for machines.** Humans benefit from simplicity (4 folders, untyped links). AI agents navigate richer taxonomies (16 node types, 10 edge types) and use that structure for more precise retrieval and traversal pruning. Typed metadata, one-sentence summaries, and explicit relationship labels are cheap overhead for an agent that reads metadata faster than prose.

---

## Step 1: Decide What Belongs in Context

Before structuring anything, audit what your agent actually needs versus what it currently receives.

### The Inclusion/Exclusion Test

For each element currently in (or being considered for) the context window, apply three questions:

1. **Can the agent discover this on its own?** Codebase overviews, directory trees, and file structure descriptions are empirically redundant -- agents discover these by reading the repo. ETH Zurich found that including them adds steps without improving success. Only include non-inferable information: custom tooling, unusual build commands, project-specific constraints.

2. **Is this stable or volatile?** Stable elements (identity, safety rules, tool definitions) belong in the upfront layer and should be cached. Volatile elements (task-specific docs, conversation history) should be retrieved just-in-time or managed dynamically. Mixing the two in a single file wastes cache efficiency and forces full re-reads on any change.

3. **Does removing this make the current task worse?** If the answer is "probably not" or "I don't know," remove it and measure. Reversing a removal is cheap; carrying dead context indefinitely is expensive.

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

This principle scales to skills. Once a centralized knowledge base exists (Obsidian vault, internal wiki, shared-context folder), each skill's SKILL.md should contain only (1) the workflow the agent follows, and (2) path references to where it reads shared context. When an ICP document or brand-voice guide lives in one canonical location, every skill that references it picks up changes automatically. Teams running 30+ skills with embedded copies of shared context experience version drift that the pointer pattern eliminates.

### Design for Your Actual Reader

When the primary consumer of a knowledge base is an AI agent, optimize for machine processing:

- **More node types are better.** A single "note" type forces the agent to read content to understand what kind of knowledge it is. A typed taxonomy (decision, concept, pattern, source) lets the agent filter by type before reading.
- **More edge types are better.** Untyped links ("these are related") force the agent to read both endpoints to understand the relationship. Typed edges (supports, contradicts, depends-on) let the agent prune traversal paths without loading documents.
- **Metadata density should increase.** YAML frontmatter, one-sentence summaries, and typed edges are cheap overhead for an agent that reads metadata faster than prose.

This does not mean abandoning human readability. The solution is dual-layer: rich metadata for agent consumption, with human-friendly views (Dataview, generated summaries) rendered from the same underlying data. But when human navigability and agent efficiency conflict, bias toward agent efficiency -- the agent is the primary reader.

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

### 3d: Progressive Skill Loading

Bulk-loading 16+ skills at boot consumes 8-32k tokens before the first user message. The progressive pattern:

1. **At boot:** Scan all enabled skills and inject only their `name` + `description` (~50 tokens each) as metadata elements.
2. **On demand:** When a task matches a skill, load the full SKILL.md (~500-2000 tokens) via `read_file`.

Skills are higher-level than tools -- they contain multi-step workflows, references, and templates -- making progressive loading even more valuable than deferred tool loading.

**Tradeoff:** Agents may not recognize when a skill is relevant if the description is too terse. Write descriptions for discoverability, not just identity.

### 3e: Scope MCP Servers to Sub-Agents

MCP servers can be defined inline in a sub-agent's frontmatter so the server connects when the sub-agent starts and disconnects when it finishes. The MCP tools and their descriptions never enter the parent conversation's context:

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

### 3f: Enforce Hard Ceilings on Memory Files

Memory files without size limits balloon silently. Apply hard character ceilings with tiered architecture:

| Tier | Behavior | Example Ceiling |
|------|----------|-----------------|
| **Hot (always-injected)** | Loaded verbatim into every session; highest-signal entries compete for space | MEMORY.md: 2,200 chars |
| **Warm (retrieved on demand)** | Full-text search surfaces relevant entries; LLM-summarized before injection | SQLite FTS5 over prior sessions |
| **Cold (archival)** | Raw timestamped records for auditing and re-promotion; not loaded at runtime | JSONL transcripts |

Writes should be triggered by conversation-pattern inference, not explicit "remember this" commands. A Curator step runs on overflow: it reads the current file, consolidates/evicts low-signal entries, and rewrites the hot-tier file to fit within the ceiling. Fixed ceilings + inference-driven writes + LLM curation = self-maintaining user model that degrades gracefully.

---

## Step 4: Design Your Retrieval Strategy

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

### Use Summary Gates for Inter-Document Navigation

Each knowledge-base node carries a mandatory one-sentence summary (~50 tokens) that the agent reads before deciding whether to load the full document (~500+ tokens). This creates a two-phase retrieval:

1. **Scan:** Agent reads node summaries and edge types from the current node's neighbors.
2. **Select:** Agent decides which neighbors are relevant to the current query.
3. **Load:** Agent reads full content of selected nodes only.

One practitioner reports that summary gates combined with typed edges reduced token consumption from ~9,000 to ~600 for equivalent queries -- a ~93% reduction. Write summaries for agent triage, not human readability. A formulaic summary ("This is about X") is less useful than a discriminating summary ("X differs from Y because Z").

### Offload to External Knowledge Bases

When reference material exceeds what fits efficiently in the context window:

- **NotebookLM** for project-specific research, YouTube transcripts, and accumulated reference material. The agent queries it on demand, keeping the context window lean. The "grounded" aspect is critical -- NotebookLM uses only sources you provide, eliminating hallucination from the knowledge layer.
- **Obsidian wiki with index navigation** for internal codebase memory and institutional knowledge. Effective for under 1000 documents with zero infrastructure overhead.
- **Personal knowledge hoards** for worked examples, solved problems, and domain-specific idioms. A distributed personal corpus (blog posts, small repos, TIL notes, single-page tools) becomes raw material the agent recombines into new artifacts. The hoard is cheap to maintain and expensive to replace -- your idioms, your frameworks, your worked examples give the agent your priors on tap rather than generic output.

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

## Step 5: Curate Context for Downstream Agents

When dispatching work to sub-agents, do not pass your full context window. Produce a self-contained context package with exactly what the sub-agent needs:

- Relevant architecture sections (not the full doc)
- Task-specific constraints (not all system constraints)
- Carry-forward notes from prior steps when dependencies exist
- Acceptance criteria for the sub-agent's output
- Purpose, audience, and workflow position (context enrichment)
- Scoped MCP servers declared inline (Step 3e)

The sub-agent should never need to search for information to start working. If it does, the context curation was incomplete. This is the "scrum master" pattern: a curator agent reads multiple sources and produces a context-complete handoff file so the executing agent starts with a focused, complete window.

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

## Step 6: Bootstrap a New System Efficiently

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
| Upfront context files | {{FILES}} | {{COUNT}} | {{PCT}} | {{YES/NO}} | 0-1 |
| Task-specific context | {{ELEMENTS}} | {{COUNT}} | {{PCT}} | No | 1 |
| Conversation history | (accumulated) | {{COUNT}} | {{PCT}} | No | dynamic |
| IDE-injected context | (open files, selections) | {{COUNT}} | {{PCT}} | No | hidden |
| **Total** | | {{TOTAL}} | {{TOTAL_PCT}} | | |

### Budget Rules
- Tier 0 (cached) context: max {{T0_BUDGET}} tokens
- Tier 1 (task-scoped) context: max {{T1_BUDGET}} tokens per call
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
| Upfront context files | Global CLAUDE.md, IL CLAUDE.md, SKILL.md | ~6,000 | 0.6% | Yes | 0-1 |
| Task-specific context | Finding files, source files loaded per-task | ~20,000 | 2.0% | No | 1 |
| Conversation history | Accumulated turns | ~50,000 | 5.0% | No | dynamic |
| IDE-injected context | Open tabs in Cursor | ~10,000 | 1.0% | No | hidden |
| **Total** | | ~98,000 | ~9.8% | | |

### Budget Rules
- Tier 0 (cached) context: max 20,000 tokens
- Tier 1 (task-scoped) context: max 30,000 tokens per call
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

---

## Related Guides

- **Defending against context degradation:** Context rot defense, compaction strategy, session persistence, delta updates, and the ACE playbook pattern are covered in *Defending Against Context Degradation* (G2b).
- **Tool definition tokens and deferred loading:** If tool definitions are a major context consumer, see *Designing Agent Tools* (G5) for dynamic tool pool assembly and deferred loading patterns.
- **Writing agent specifications:** For defining what the agent should do (rather than what it should know), see *Writing Agent Specifications* (G1).
- **Multi-agent composition:** Sub-agent context curation (Step 5) intersects with single-vs-multi-agent decisions; see *Agent Architecture Decisions* (G3) for composition patterns.
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
- Tiered loading preserves token budget -- always-on context is minimal, everything else is loaded on demand.
- Pointers are used instead of embedded copies for any content with a canonical source location.
- Sub-agents receive scoped context appropriate to their task, not the parent's full window.
- Memory files have hard ceilings with tiered hot/warm/cold architecture.
- Skills reference shared context via path, not embedded copies (when a canonical source exists).
- Knowledge base structure is optimized for the primary reader (agent or human) with appropriate metadata density.

### Governance
- Context file owners audit their files against the inclusion/exclusion criteria in this guide at least once per milestone.
- Context architecture changes (new upfront files, changed sharding boundaries, tier reassignments) are documented.
- Model-specific context strategies are re-validated when the underlying model changes.
- Module manifests are owned by module owners and updated as part of any breaking-change PR.
- This guide is owned by the Improvement Loop and deployed to the Meta-System knowledge layer after review.

### Recovery
- If agent output quality degrades: run the inclusion/exclusion test (Step 1) first. Context bloat is the most common root cause.
- If token costs spike: check for context duplication, reasoning token amplification from unnecessary instructions, hidden IDE context injection, or upfront loading of content that should be JIT.
- If retrieval quality drops: audit against the retrieval strategy decision tree (Step 4). Check whether corpus size has crossed the file-search/semantic-search threshold.
- If a new model performs differently: re-audit context files with model-specific sensitivity in mind. What worked for Codex may not work for Claude Code.
- If context loading degrades agent performance, audit against the tiering decision tree and retrieval strategy selection.
