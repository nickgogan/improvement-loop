---
name: Research Dimensions
description: Researcher-side scan topics — dimensions (top-level) and sub-dimensions (second-level) naming what the Researcher scans for in the world. Read by /research-loop at scan start. Not a consumer routing layer; consumer-facing navigation is the Librarian's reference layer.
last_updated: "2026-06-18 (session 122 — D7/D9 downstream-signal notes: scans here route to schematic re-evaluation via /detect-drift, DD-107)"
---

# Research Dimensions

This file is the **active query source** for the `/research-loop` skill. The Researcher reads it at Step 0 of every scan and proposes refinements at Step 6. Edit queries here to steer future scans — no need to touch the skill definition.

---

## What these dimensions are (and are not)

**These are Researcher-side scan topics.** Each dimension names *what the Researcher goes looking for in the world* — an aspect of agent systems where external practice is worth harvesting. The dimensions partition the frontier so scans stay bounded and the KB stays indexable by topic of origin.

**These are not consumer categories.** They are not how the Librarian routes a user's question ("audit my agent.md", "how do I handle memory?", "compare MongoDB single-store vs triple-storage"). Consumer-facing navigation is the Librarian's job — it decomposes a query into reads against guides, patterns, findings, and watched-library repos, using concept files (noun-keyed) and operation files (verb-keyed) in `operations/references/librarian/`. A single consumer question typically spans multiple dimensions and guides; the dimension registry does not pre-solve that composition and is not meant to.

**Consequences of this framing:**
- **Drift signal:** a dimension that begins to index by *what consumers build* rather than *what the Researcher scans* is drifting. Dimension 11 (Agentic Systems) is the edge case that forced this clarification — it names a class of operational systems the Researcher scans in the world, not a consumer artifact class. Scan-topic framing preserved.
- **Do not grow the registry for cross-cutting consumer themes.** "Harness," "Context Rot," "Second Brain," "MCP" are consumer concepts that span aspects — they belong in the Librarian reference layer as concept files, not here. The registry grows only when a new *scan topic* surfaces with enough external research mass to need its own query shape.
- **Findings still carry a `category:` from this registry.** That stays Researcher-side metadata (origin-of-finding). It is not a consumer-visible route.

---

## Taxonomy shape (dimensions + sub-dimensions)

Dimensions are top-level scan topics. A **sub-dimension** is a second-level scan topic under a parent dimension — introduced only when a topic has accumulated enough external research mass to deserve its own queries, but is still best understood as a facet of a broader parent. Sub-dimensions carry their own query shape and seed-finding cluster; they do not fork a new `category:` in frontmatter.

**When to elevate a sub-dimension to its own top-level dimension:** the sub-dimension's findings no longer compose primarily within the parent — they are referenced by multiple sibling dimensions, have an independent consumer concept in the Librarian reference layer, and have ≥10 findings. Until then, keep it nested.

**Current taxonomy:**
- Dimension 1: Context Engineering
  - Sub-dimension 1.A: Memory Decay, Forgetting, and Compaction *(added 2026-04-24)*
  - Sub-dimension 1.B: Memory Isolation and Topology *(added 2026-04-24)*
- Dimension 2: Model Selection
- Dimension 3: Prompt Craft
- Dimension 4: Tool Integration
- Dimension 5: Intent Engineering
- Dimension 6: Orchestration
- Dimension 7: Evaluation
- Dimension 8: Sandboxing
- Dimension 9: Governance
- Dimension 10: Agent Design
- Dimension 11: Agentic Systems

---

## Dimension 1: Context Engineering

**What to search for:**
- New techniques for managing what agents see at runtime
- Dynamic context injection patterns
- Memory architectures (episodic, semantic, structured notes)
- RAG improvements, GraphRAG, hybrid retrieval
- Context window management and compaction strategies

**Web queries:**
- `context engineering AI agents [current year]`
- `agent memory architecture production [current year]`
- `dynamic context injection agentic systems`

**arXiv queries:**
- `agent memory architecture`
- `episodic memory language model agents`
- `retrieval augmented generation agent`
- `long-term memory autonomous agents`
- `cognitive architecture LLM`

### Sub-dimension 1.A: Memory Decay, Forgetting, and Compaction

**Why this sub-dimension.** Human memory's defining characteristic is its *selectivity* — forgetting is architecturally fundamental, not a failure mode. Agent memory systems are independently converging on the same conclusion: what gets written, what gets preserved, what gets superseded, and what expires is as load-bearing as what gets retrieved. The KB already has a three-strategy decay cluster (Memongo importance-based, Memongo surprisal-gated writes, Supermemory content-derived expiration). Elevating this as a named sub-dimension gives future scans an explicit query shape and a home for the cluster, without forking a new top-level dimension.

**What to search for:**
- Write-time filters: surprisal/novelty gates, deduplication at ingestion, contradiction detection at write
- Decay functions: importance-based, recency-weighted, reinforcement-based (access-count), hybrid
- Permanent-exemption patterns: identity/preference/constitution memories that bypass decay
- Content-derived expiration: date-parsing from content, event-bound TTL, referenced-entity expiry
- Memory versioning & supersession: Updates relationships, `isLatest` flags, superseded-but-retained history, archive-on-Nth-generation pruning
- Cross-session compaction: when to summarize vs. drop vs. merge; two-threshold compaction strategies
- Cognitive architecture models: ACT-R activation decay, Soar chunking, working-memory capacity, interference-based forgetting
- Failure modes: stale-importance bloat, permanent-tag abuse, false-positive contradiction resolution, embedding-nearby-but-semantically-distinct collisions, timezone drift in content-derived dates

**Web queries:**
- `agent memory forgetting decay strategies [current year]`
- `LLM agent memory compaction supersession [current year]`
- `memory novelty surprisal write gating production`
- `content-derived TTL semantic expiration agent memory`
- `memory importance score provenance recomputation`

**arXiv queries:**
- `memory decay forgetting language model agent`
- `continual learning memory consolidation LLM`
- `importance-weighted memory neural network`
- `cognitive architecture activation decay`
- `interference-based forgetting episodic memory`

**KB cluster (seed findings, 2026-04-24):**
- `importance-based-decay-permanent-exemption` (Memongo)
- `surprisal-novelty-as-memory-write-gate` (Memongo)
- `content-derived-temporal-expiration-contradiction-resolution` (Supermemory)
- `semantic-memory-decay-compaction`
- `memory-decay-compaction-convergence`
- `two-threshold-compaction-strategy`
- `proactive-compaction-before-intelligence-degradation`
- `dreaming-memory-consolidation` (referenced via same-problem from the cluster)
- `memory-field-immutability-via-merge-operations`

**Graduation criteria (when to elevate to a top-level dimension):** ≥10 findings specifically about decay mechanics (not retrieval, not storage topology), multiple sibling-dimension references to these findings (e.g., Governance using forgetting as a compliance primitive), and an independent Librarian concept file that routes consumer questions to this cluster. Until then, keep nested under Dimension 1.

### Sub-dimension 1.B: Memory Isolation and Topology

**Why this sub-dimension.** Memory *selectivity* (1.A) and memory *isolation* (1.B) are orthogonal concerns. Decay asks "what gets forgotten?"; isolation asks "whose memory sees what?" Multi-agent, multi-project, and multi-tenant agent systems are independently converging on isolation primitives — bank IDs, per-agent directories, tenant tags, channel-scoped recall — that prevent cross-contamination between contexts sharing a memory substrate. Extracted findings from session 63's guide-routing check revealed that `category: Memory Architecture` was orphaned — not registered as a dimension, yet admitted by the routing table. Elevating isolation as a named sub-dimension gives these findings a registered home without forking a new top-level dimension.

**What to search for:**
- Bank-ID and channel-based isolation primitives (Hindsight, mem0, Supermemory)
- Per-agent persistent memory directories (Claude Code agent-memory pattern)
- Per-project memory scopes; per-session vs cross-session boundaries
- Multi-tenant memory tagging and hierarchical container schemes
- Cross-agent memory sharing protocols; opt-in vs opt-out defaults
- Memory access-control patterns (permissions on memory entries, ACLs on recall)
- Scope-boundary alignment with system boundaries (system-scoped memory mirroring system-scoped governance)
- Collision and contamination failure modes (embedding-near collisions, channel leakage, tag drift)

**Web queries:**
- `agent memory isolation per-agent per-project [current year]`
- `multi-tenant agent memory bank id channel`
- `multi-agent memory sharing protocol opt-in`
- `agent memory scope boundary system`
- `memory access control agent permissions`

**arXiv queries:**
- `multi-agent memory isolation language model`
- `hierarchical memory scope LLM agent`
- `cross-agent knowledge sharing protocol`
- `multi-tenant retrieval augmented generation`

**KB cluster (seed findings, 2026-04-24):**
- `memory-bank-isolation-per-agent-per-project` (Hindsight)
- `subagent-persistent-memory-directory` (Claude Code)
- `hierarchical-container-tag-multi-tenancy`
- `multi-client-context-isolation-with-shared-skills`
- additional neighbors via same-problem links on the above

**Graduation criteria (when to elevate to a top-level dimension):** Same threshold as 1.A — ≥10 findings specifically about isolation/topology mechanics (not decay, not storage medium, not retrieval algorithm), multiple sibling-dimension references to these findings, and an independent Librarian concept file that routes consumer questions here. Until then, keep nested under Dimension 1.

---

## Dimension 2: Model Selection

**What to search for:**
- New model releases and capability changes relevant to agent tasks
- Benchmark shifts for tool calling, long context, reasoning
- Cost/performance tradeoffs for different model tiers
- Model-specific prompting guidance

**Web queries:**
- `new AI model releases agent capabilities [current year]`
- `Claude Opus Sonnet comparison agent tasks [current year]`
- `LLM benchmark tool calling reasoning [current year]`

---

## Dimension 3: Prompt Craft

**What to search for:**
- New instruction patterns and structural conventions
- Few-shot and many-shot technique developments
- Chain-of-thought, self-correction, and verification patterns
- Agent-specific prompting (tool use guidance, multi-turn stability)
- System prompt architecture patterns

**Web queries:**
- `AI agent prompt engineering best practices [current year]`
- `system prompt architecture patterns [current year]`
- `self-correcting agent prompts production`

---

## Dimension 4: Tool Integration

**What to search for:**
- New capabilities in agent platforms (Claude Code, MCP, Notion Custom Agents, etc.)
- New tool integrations, API changes, capability expansions
- CLI tools and platform-specific features
- MCP server ecosystem developments

**Web queries:**
- `Claude Code new features [current year]`
- `MCP protocol updates [current year]`
- `Notion custom agents capabilities [current year]`
- `AI agent CLI tools integrations [current year]`

---

## Dimension 5: Intent Engineering (Meta-Dimension)

**What to search for:**
- Goal encoding and alignment for agents
- Constraint architecture patterns (musts, must-nots, preferences, escalation triggers)
- Autonomy boundary frameworks
- Human-in-the-loop design patterns

**Web queries:**
- `intent engineering AI agents [current year]`
- `agent autonomy boundaries human in the loop [current year]`
- `AI agent goal alignment production systems`

---

## Dimension 6: Orchestration

**What to search for:**
- Multi-agent coordination and delegation patterns
- Workflow composition (relay vs marathon, fan-out/fan-in, chained pipelines)
- Sub-agent isolation, context boundaries between agents
- Agent sprawl prevention and complexity management
- State management across agent handoffs
- Scheduling, parallelization, and sequencing strategies

**Web queries:**
- `multi-agent orchestration production patterns [current year]`
- `AI agent workflow composition delegation [current year]`
- `sub-agent coordination state management [current year]`
- `agent sprawl complexity management`

**arXiv queries:**
- `multi-agent LLM orchestration`
- `agentic workflow planning`
- `task decomposition multi-agent systems`

---

## Dimension 7: Evaluation

**What to search for:**
- Verification patterns for agent outputs (independent eval, not self-reporting)
- Reliability engineering for multi-step agent workflows
- Quality gates, test-driven development with agents
- Benchmarking and eval frameworks (SWE-bench, SWECI, custom evals)
- Binary evals, skill self-improvement loops
- Failure mode detection and compounding reliability math

**Web queries:**
- `AI agent evaluation verification production [current year]`
- `agent reliability testing quality gates [current year]`
- `LLM agent benchmark evaluation framework [current year]`
- `independent verification AI agent outputs`

**arXiv queries:**
- `autonomous agent evaluation benchmark`
- `LLM agent reliability verification`
- `self-improving AI agent evaluation`

**Downstream signal (not a consumer route):** findings here ground the **Evaluation & feedback layer** of schematics (`knowledge/schematics/`). When a D7 finding's `last_updated` moves, `/detect-drift` re-flags every schematic `grounded_in` it for re-evaluation (DD-107) — this is how a schematic's eval layer stays current.

---

## Dimension 8: Sandboxing

**What to search for:**
- Execution environment isolation for agents (containers, VMs, ephemeral sandboxes)
- Safe code execution patterns (E2B, Daytona, Docker-based sandboxes)
- Permission boundaries and blast radius containment
- File system isolation, network restrictions, resource limits
- Sandbox-as-a-service platforms for agent workflows
- Rollback and checkpoint patterns for destructive operations

**Web queries:**
- `AI agent sandboxing execution environment [current year]`
- `safe code execution LLM agents production [current year]`
- `agent sandbox isolation containers [current year]`
- `E2B Daytona agent sandbox comparison`

**arXiv queries:**
- `safe execution environment language model agents`
- `sandboxed code generation LLM`
- `agent environment isolation security`

---

## Dimension 9: Governance

**What to search for:**
- Human-agent authority boundaries and delegation frameworks
- Autonomy tiering (when agents act vs. when humans gate)
- Review and approval workflows for agent outputs
- Organizational redesign for agentic throughput (review bottlenecks, compliance)
- Audit trails, accountability, and traceability for agent actions
- Regulatory and compliance patterns for autonomous systems
- Build/operate separation and ownership boundaries

**Web queries:**
- `AI agent governance human oversight framework [current year]`
- `agent autonomy tiering approval workflow production [current year]`
- `AI agent compliance audit trail enterprise [current year]`
- `human in the loop agent review bottleneck [current year]`

**arXiv queries:**
- `AI agent governance oversight framework`
- `autonomous agent accountability audit`
- `human AI delegation authority boundary`

**Downstream signal (not a consumer route):** findings here ground the **autonomy / authority-boundary** choices in schematics (`knowledge/schematics/`). When a D9 finding's `last_updated` moves, `/detect-drift` re-flags every schematic `grounded_in` it for re-evaluation (DD-107).

---

## Dimension 10: Agent Design

**What to search for:**
- Agent identity definition patterns (SOUL.md, persona files, constitution files)
- Boot sequence and initialization architecture (what loads first, forced disk-reads, cold start prevention)
- Agent persona engineering (behavioral overrides, negative constraints for personality, vibe sections)
- Context file taxonomy and separation of concerns (WHO the agent is vs. WHAT it does vs. WHAT it sees)
- Agent onboarding and interview-based context generation
- Identity persistence through context compaction (pinning, survival mechanics)
- Agent capability boundary definition (what the agent can/cannot do, operational immune systems)
- Agent template design and reusable agent archetypes
- Agent self-description and meta-reasoning system files (agents.md as meta-reasoning, not just rules)

**Web queries:**
- `SOUL.md agent identity persona design [current year]`
- `AI agent boot sequence initialization architecture [current year]`
- `agent persona engineering context file taxonomy [current year]`
- `agent template design reusable archetypes production [current year]`

**arXiv queries:**
- `agent persona identity language model`
- `agent initialization context architecture`
- `cognitive agent identity persistence`

---

## Dimension 11: Agentic Systems

**Scope.** Personal, team, and business *operational systems* in which multiple agents serve user workflows. The unit of analysis is the system-level assembly — vault-as-OS, daily-brief pipeline, team context-sharing setup, business operations agent stack — not an individual agent. (Renamed from "Agentic OS" on 2026-04-21 to reflect that the scan topic covers team and business systems, not only personal OS.)

**What to search for:**
- Personal knowledge management with AI agents (second brain, vault-as-OS)
- Obsidian + AI agent integration patterns (CLI, terminal plugins, graph views)
- Scheduled agent tasks for life/business operations (morning briefs, meeting transcript ingestion, analytics rollups)
- File-based personal/team OS architecture (folder structure, index files, CLAUDE.md as routing layer)
- Context infrastructure maturity models (chat → projects → skills → file access → second brain → business OS)
- Team context sharing and permission patterns (sync, relay plugins, access control, shared memory layers)
- Multi-agent business operations in production orgs (cross-agent protocols, shared state, delegation topologies across roles)
- Experiment/ritual tracking and daily routine automation with agent assistance

**Web queries:**
- `AI agent personal OS second brain [current year]`
- `obsidian claude code knowledge management workflow [current year]`
- `agentic business OS scheduled tasks automation [current year]`
- `personal productivity AI agent operations [current year]`
- `team AI agent shared context collaboration [current year]`
- `multi-agent business operations production [current year]`

**arXiv queries:**
- `personal knowledge management AI agent`
- `AI assistant daily workflow automation`
- `human AI collaborative knowledge system`
- `multi-agent team knowledge sharing`
