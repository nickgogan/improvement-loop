---
title: "Managing Agent Context"
type: "guideline"
category: "Context Engineering"
target_system:
  - "cross-system"
stage: "draft"
created: "2026-04-19"
updated: "2026-04-19"
author: "claude"
source_findings:
  - "ace-agentic-context-engineering-evolving-playbook"
  - "ace-delta-updates-over-monolithic-rewrites"
  - "agent-context-kiss-commandments-minimum-viable"
  - "context-curation-over-context-stuffing"
  - "context-enrichment-for-task-clarity"
  - "context-file-instruction-bloat-eth-zurich"
  - "context-rot-attention-budget-depletion"
  - "context-rot-silent-killer-and-mitigations"
  - "document-sharding-for-context-efficiency"
  - "fundamental-limits-of-single-vector-embedding-retr"
  - "hybrid-upfront-and-jit-context-architecture"
  - "prompt-caching-for-stable-agent-context"
  - "scrum-master-story-contextualization"
  - "dynamic-tool-pool-assembly-transcript-compaction"
  - "response-format-enum-for-adaptive-verbosity"
  - "reasoning-token-overhead-from-context-files"
  - "ide-context-streaming-silent-token-tax"
  - "index-file-navigation-as-rag-replacement"
  - "new-chat-per-agent-step-context-hygiene"
  - "claudemd-as-knowledge-base-traversal-guide"
  - "model-specific-context-file-sensitivity"
  - "one-shot-prd-prompt-for-system-bootstrap"
  - "tiered-context-injection-over-monolithic-files"
  - "notebooklm-as-external-knowledge-base-for-context"
  - "pointers-over-copies-in-context-files"
  - "gsd-global-learnings-store-cross-session-persistence"
source_dd:
  - "DD-81"
tags:
  - "guide"
  - "context-engineering"
contract:
  preconditions: "Agent system exists with context files or context injection mechanism"
  invariants: "Context budget stays within model limits; context freshness maintained"
  governance: "IL-owned draft; Nick deploys to meta-system/knowledge/guides/"
  recovery: "If context rot detected, run context audit procedure from this guide"
---

# Managing Agent Context

Your agent is losing context, burning tokens, or drifting from its goals. This guide covers why that happens and what to do about it — from auditing what is in the window to structuring context for selective loading, defending against silent degradation, and controlling costs across sessions.

## When to Use This Guide

- Agent output quality degrades over long sessions or multi-step workflows
- Token costs are higher than expected or growing without clear cause
- You are designing context files (CLAUDE.md, system prompts, skill definitions) for a new agent
- You suspect context rot — the agent forgets constraints, re-derives conclusions, or drifts from requirements
- You are scaling from a single agent to multi-agent pipelines and need context isolation
- You are bootstrapping a new system and need to decide what goes into the initial context package

**Do not use for:** defining what the agent should do (see G1: *Writing Agent Specifications*), designing the agent's tool set (see G5: *Designing Agent Tools*), or evaluation suite design.

## Key Concepts

**1. Context is a finite, depletable resource — not a bucket.** As tokens accumulate, transformer attention budget depletes across n-squared pairwise relationships. Every unnecessary token actively degrades the model's recall of tokens that matter. Context management is not "stay under the limit" — it is "minimize waste at all times."

**2. More context often makes output worse — and the cost is hidden.** ETH Zurich (2026) proved that LLM-generated context files reduce agent success by 3% and increase cost by 20%. But the cost goes deeper: context files increase reasoning token usage by 14-22%, meaning agents spend compute processing irrelevant instructions rather than solving the task. The true cost is input bloat + reasoning amplification + additional steps (2.45-3.92 extra steps per task).

**3. Context rot is the #1 silent killer.** Agents forget constraints, drift from goals, and re-derive nonsensical conclusions over long sessions. The output looks plausible but increasingly deviates from requirements. Standard monitoring (error rates, latency) will not catch it — only explicit state tracking and contract validation detect drift before it compounds.

**4. Structure beats volume.** The difference between effective and wasteful context is not how much you provide but how you organize it: small high-signal files loaded upfront, everything else retrieved just-in-time, evolving documents updated incrementally, and each agent scoped to the minimum it needs.

**5. Context sensitivity is model-specific.** Claude Code (Sonnet-4.5) was the only agent in the ETH Zurich study where even human-written context files failed to improve performance. Different models respond dramatically differently to the same context files. One-size-fits-all context strategies are empirically wrong — optimize for the model you are actually using.

---

## Step 1: Audit Your Current Context

Before changing anything, understand what is in the window and what it costs.

### The Five-Question Token Audit

1. **What is in the window right now?** List every element: system prompt, CLAUDE.md files, tool definitions, conversation history, retrieved docs, injected context. Include invisible sources — IDE context streaming silently injects open files and highlighted selections into the window without visual indication. Ask the model "what do you see?" to discover hidden injections.
2. **What is stable vs. volatile?** Stable elements (system prompt, tool defs, persona) should be cached. Volatile elements (conversation history, task-specific docs) should be minimized and managed.
3. **What can the agent discover on its own?** Codebase overviews, directory trees, and anything the agent can learn by reading the repo should not be in context files. ETH Zurich found these are redundant — agents are surprisingly good at discovering file structures themselves. Only include non-inferable information: custom tooling, unusual build commands, project-specific constraints.
4. **What is duplicated?** The same information stated in the system prompt, a CLAUDE.md file, and a skill definition consumes 3x the tokens for zero added signal — and may create subtle contradictions when one copy is updated and others are not.
5. **What is the per-call cost?** Instrument agent calls to track input tokens, output tokens, model mix, and cost. You cannot improve what you do not measure. Most teams optimize for semantic correctness and ignore cost — until model pricing makes their pipeline unviable.

### The 60-Line Benchmark

Community and Anthropic practice converges on 60-80 lines as the sweet spot for context files. If your CLAUDE.md is significantly longer, audit it for bloat. Remember that tool mentions in context files increase tool usage 160x — every tool you name is an implicit instruction to use it.

---

## Step 2: Curate for Signal, Not Coverage

The goal is not to tell the agent everything — it is to tell the agent exactly what it needs and nothing more.

### What Belongs in the Context Window

- Agent identity, instructions, and persona (high-signal, stable)
- Tool definitions and permissions (scoped to current task, not all available tools)
- Task-specific context enrichment: purpose, target audience, workflow position, success criteria with measurable thresholds
- Active constraints and policies that cannot be enforced structurally
- Cross-session memory that persists across runs — not everything that happened
- Navigation instructions for knowledge bases (where to find indexes, how to follow links)

### What to Move Out or Remove

- Verbose documentation retrievable on demand (use JIT retrieval)
- Historical context irrelevant to the current task
- Information already expressed in conventions or tool definitions
- Codebase structure the agent can discover by reading the repo
- Low-confidence or contradictory sources that create conflicting signals
- Embedded code snippets or architecture descriptions — use pointers to canonical sources instead

### The Curation Test

For each element in the context window, ask: "If I remove this, will the agent's output for this specific task get worse?" If the answer is "probably not" or "I don't know," remove it and measure. Reversing a removal is cheap; carrying dead context indefinitely is expensive.

### Pointers Over Copies

Instead of pasting content into context files, point to the canonical source:

```
# Instead of this:
The fractal pattern has 7 folders: app/, governance/, knowledge/,
agents/, project-management/, operations/, archive/...

# Do this:
See the fractal pattern definition: systems/meta-system/governance/fractal-pattern.md
```

Copies go stale. Pointers always read the current state. The exception: project intent, trade-off philosophy, and other information with no canonical file location genuinely belongs inline.

---

## Step 3: Structure for Selective Loading

### 3a: Tier Your Context

Instead of loading one monolithic file into every interaction, categorize instructions by when they are needed:

| Tier | What Goes Here | When Loaded | Token Budget |
|------|---------------|-------------|--------------|
| **Tier 0 (Always-On)** | Identity, safety constraints, hard rules | Every interaction | < 20 lines |
| **Tier 1 (Task-Scoped)** | Coding conventions when coding, test patterns when testing, review criteria when reviewing | When task type is detected | Varies by task |
| **Tier 2 (On-Demand)** | Architecture overviews, dependency docs, reference material | When agent signals need | Retrieved JIT |

ETH Zurich data shows task-relevant instruction subsets reduce context by 60-80% while maintaining or improving accuracy compared to monolithic file loading. The cost savings alone (20%+ reduction in inference cost) justify the structural investment.

### 3b: Shard Large Documents

Break monolithic documents into focused, role-specific shards. Each agent loads only the shards relevant to its current task.

| Instead of | Shard into |
|------------|-----------|
| Full PRD (5000 lines) | `coding-standards.md`, `tech-stack.md`, `data-model.md`, `api-contracts.md` |
| Monolithic CLAUDE.md | Global CLAUDE.md (60 lines) + per-system CLAUDE.md files |
| Single architecture doc | One file per subsystem boundary |
| Full tool registry | Session-specific tool subsets via mode flags and deny lists |

**Sharding rule:** Each shard should be loadable independently without losing critical context. If shard A requires shard B to make sense, they should be one file or the dependency should be explicit.

### 3c: Use the Hybrid Context Architecture

Combine upfront and just-in-time modes:

| Mode | What Goes Here | Why |
|------|---------------|-----|
| **Upfront (always loaded)** | Small, high-signal files: CLAUDE.md, system prompt, persona, tool defs | Immediate availability, no retrieval latency, cacheable |
| **Just-in-time (retrieved on demand)** | Everything else: docs, code, reference material | Context efficiency — load only when needed |

The upfront layer should be small enough that it does not crowd out task-specific context. The JIT layer uses filesystem primitives (glob, grep, read) rather than embedding-based retrieval. Single-vector embeddings achieve under 20% Recall@100 on combinatorial queries while BM25 achieves 85.7%. For small-to-medium knowledge bases (under 1000 documents), index-file navigation — reading an `_index.md` and following links — outperforms RAG pipelines with zero infrastructure overhead.

### 3d: Use CLAUDE.md as a Traversal Guide

For knowledge-base-heavy projects, the CLAUDE.md file serves double duty: project rules plus a navigation protocol that teaches the agent how to find information efficiently.

Effective traversal instructions:
- Where to find the master index
- How to read per-section indexes and follow links
- File structure conventions for new files (so the agent maintains navigability)
- What to read first vs. what to retrieve on demand

Without traversal instructions, agents use expensive tool calls (glob, grep) to discover structure on every query. With a navigation protocol, the agent follows a deterministic 2-3 file read path: master index, section index, target file.

### 3e: Curate Context for Downstream Agents

When dispatching work to sub-agents, do not pass your full context window. Produce a self-contained context package with exactly what the sub-agent needs:

- Relevant architecture sections (not the full doc)
- Task-specific constraints (not all system constraints)
- Carry-forward notes from prior steps when dependencies exist
- Acceptance criteria for the sub-agent's output
- Purpose, audience, and workflow position (context enrichment)

The sub-agent should never need to search for information to start working. If it does, the context curation was incomplete. This is the "scrum master" pattern: a curator agent reads multiple sources and produces a context-complete handoff file so the executing agent starts with a focused, complete window.

---

## Step 4: Manage Dynamic Context

### 4a: Assemble Tool Pools Dynamically

Do not load all available tools into every session. From a large tool registry, assemble session-specific subsets based on:

- Mode flags (planning mode vs. execution mode)
- Permission levels (read-only vs. read-write)
- Deny lists (tools explicitly excluded for this task type)

Claude Code assembles from 184 available tools per session using this approach. Dynamic tool pools reduce context noise and prevent accidental tool access.

### 4b: Control Tool Output Verbosity

Add a response format parameter to tools that return variable-length results:

- **Detailed** (~206 tokens): Full metadata, IDs, and content for operation chaining
- **Concise** (~72 tokens): High-signal summary for scanning and triage

This yields ~65% token reduction when the agent only needs a summary. Let the agent select format based on current task needs.

### 4c: Compact Conversation History

Long conversations accumulate stale context. Use transcript compaction:

- Auto-compact after a configurable number of turns
- Preserve recent messages and decision-relevant history
- Track compaction state for session persistence
- Align compaction boundaries with task boundaries, not arbitrary turn counts

### 4d: Reset Context at Natural Boundaries

At each workflow phase boundary, start a fresh context window. Information transfers via document artifacts only — the next agent reads the output files, not the conversation history. This prevents multi-step workflows from accumulating noise, outdated instructions, and conflicting context.

Natural reset points: new sessions, workflow phase transitions, completed milestones, and whenever context utilization exceeds 40-50% of window capacity.

---

## Step 5: Defend Against Context Rot

Context rot is silent — the agent's output looks plausible but increasingly deviates from requirements. Five production-tested defenses:

**1. Maintain an explicit state object.** Track active constraints, goals, and accumulated decisions as structured data (YAML/JSON), not conversation history. Prose summarization loses precision. The state object is the source of truth for what the agent should be attending to.

**2. Validate against contracts at each step.** If the agent produces structured output, validate it against its task contract before passing it downstream. Contract violations are early rot indicators.

**3. Use delta updates for evolving documents.** When context documents change over time (playbooks, progress files, accumulated notes), update incrementally — append structured entries, then periodically consolidate. Never rewrite the full document with an LLM, as brevity bias silently drops domain-specific details. The ACE framework (Stanford/SambaNova) demonstrates that structured playbook accumulation with deduplication outperforms compaction by +10.6% on agentic benchmarks.

**4. Persist learnings across sessions.** Hard-won context disappears at every session boundary. A structured global learnings store — with CRUD operations, auto-injection into planner context, and relevance filtering — converts repeated failures into durable institutional knowledge. Without expiry or validation mechanisms, the store degrades into noise, so prune and update.

**5. Reset context at natural boundaries.** New sessions, new workflow phases, and completed milestones are natural reset points. Re-inject the upfront context layer and start with a fresh conversation rather than accumulating stale turns.

---

## Step 6: Optimize for Cost

After context is curated and structured, apply cost optimizations:

### Cache All Stable Context

System prompts, tool definitions, persona instructions, and reference material that does not change between calls should use prompt caching. Cache hits on Claude Opus cost $0.50/M vs $5/M standard — 90% savings. Structure prompts to front-load cacheable content before dynamic content. Any single character change to cached content forces a full-price re-read of the entire block, so stabilize content before enabling caching.

### Account for Hidden Costs

Context files do not just add input tokens — they amplify reasoning tokens by 14-22%. Agents reason more in the presence of context instructions, consuming compute on instruction processing rather than task solving. A 20% reasoning overhead on a 10-turn task means 200% additional reasoning tokens over the session.

IDE context streaming adds another invisible tax: every open file and highlighted selection in VS Code or JetBrains gets silently injected as context tokens. Close irrelevant files during agent sessions.

### Measure Per-Call Token Usage

Instrument input tokens, output tokens, model mix, and cost ratio. Track trends over time. A spike in input tokens usually indicates context duplication or an upfront file that has grown past its budget. Budget context by category and audit when a category exceeds its allocation.

### Bootstrap Efficiently

When bootstrapping new systems, a single declarative PRD prompt can scaffold the entire structure (folders, scripts, hooks, agents, indexes) in one pass. This eliminates the token cost of iterative back-and-forth scaffolding and produces a consistent starting context.

---

## Step 7: Offload to External Knowledge Bases

When your reference material exceeds what fits efficiently in the context window, offload to external query layers:

- **NotebookLM** for project-specific research, YouTube transcripts, and accumulated reference material. Claude Code queries it on demand, keeping the context window lean while maintaining access to extensive documentation. The "grounded" aspect is critical — NotebookLM only uses sources you provide, eliminating hallucination from the knowledge layer.
- **Obsidian wiki with index navigation** for internal codebase memory and institutional knowledge. The LLM maintains an `_index.md` and navigates via wiki-links, achieving effective retrieval for under 1000 documents with zero infrastructure overhead.
- **Context7** (or equivalent) for library documentation, API references, and framework-specific content.

The principle: keep task context in the window, keep reference context queryable externally.

---

## Templates

### Context Budget Worksheet

```markdown
## Context Budget -- {{AGENT_NAME}}

**Model:** {{MODEL_NAME}}
**Total context window:** {{WINDOW_SIZE}} tokens
**Target utilization:** {{TARGET_PERCENT}}% (leave headroom for agent reasoning)

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

### Audit Triggers
- Cost spike > {{COST_THRESHOLD}}% above baseline
- Quality degradation on established tasks
- New context files added to upfront layer
- Model change (context sensitivity is model-specific)
```

**Variable Reference:**

| Variable | Type | Required | Description |
|----------|------|----------|-------------|
| `AGENT_NAME` | string | Yes | Agent or skill being budgeted |
| `MODEL_NAME` | string | Yes | Model identifier (context sensitivity varies by model) |
| `WINDOW_SIZE` | number | Yes | Model's context window in tokens |
| `TARGET_PERCENT` | number | Yes | Target max utilization (typically 60-80%) |
| `T0_BUDGET` | number | Yes | Max tokens for always-on cached context |
| `T1_BUDGET` | number | Yes | Max tokens for per-call task context |
| `HISTORY_LIMIT` | number | Yes | Token threshold for compaction/reset |
| `AUDIT_INTERVAL` | string | Yes | How often to check hidden context sources |
| `COST_THRESHOLD` | number | Yes | Percentage spike that triggers audit |

### Worked Example: MetaSystem Researcher Agent

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

### Audit Triggers
- Cost spike > 30% above baseline
- Quality degradation on finding extraction
- New CLAUDE.md content added
- Model change from Opus 4.6
```

---

### Context Audit Checklist

```markdown
## Context Audit -- {{AGENT_NAME}} -- {{DATE}}

### Signal-to-Noise Check
- [ ] Every context file is under 80 lines
- [ ] No codebase overviews or directory trees (agent discovers these)
- [ ] No duplicated information across context files
- [ ] No instructions for things the agent never does
- [ ] Tool mentions are intentional (tool mentions increase usage 160x)
- [ ] Pointers used instead of embedded copies where possible
- [ ] Navigation instructions present for knowledge base traversal

### Tiering Check
- [ ] Tier 0 contains only identity, safety, and hard rules (< 20 lines)
- [ ] Task-scoped instructions are in Tier 1, not Tier 0
- [ ] Reference material is in Tier 2 (on-demand), not loaded upfront
- [ ] Tool pool is dynamically assembled, not all-tools-always

### Curation Check
- [ ] Each context element has a justifiable reason for being there
- [ ] Volatile content is not in cached/upfront files
- [ ] Sub-agents receive scoped context, not the full parent window
- [ ] Context enrichment present: purpose, audience, workflow position, criteria
- [ ] Retrieved content uses hybrid retrieval (not embeddings alone)

### Rot Defense Check
- [ ] Explicit state object exists for long-running sessions
- [ ] Evolving documents use delta updates, not monolithic rewrites
- [ ] Context resets happen at natural workflow boundaries
- [ ] Output is validated against contracts at each step
- [ ] Cross-session learnings are persisted and injected

### Cost Check
- [ ] Stable context is cached (system prompt, tool defs, persona)
- [ ] Per-call token usage is instrumented
- [ ] Token budgets are assigned by category and tier
- [ ] Cache hit rates are monitored
- [ ] Hidden context sources (IDE, git status) are accounted for
- [ ] Reasoning token overhead is estimated (14-22% amplification)

### Findings
| # | Issue | Severity | Fix |
|---|-------|----------|-----|
| 1 | {{ISSUE}} | {{HIGH/MED/LOW}} | {{ACTION}} |
```

---

### Context File Template

For designing new context files (CLAUDE.md, skill files, agent prompts) with built-in tiering:

```markdown
# {{CONTEXT_FILE_NAME}}

## Identity (Tier 0 -- always loaded)
{{AGENT_ROLE_IN_ONE_SENTENCE}}

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
- {{CONCEPT}}: see {{FILE_PATH}}
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

### Delta Update Entry

For evolving context documents (progress files, playbooks, accumulated notes):

```markdown
## Delta -- {{DATE}}

### Added
- {{NEW_ITEM_1}}
- {{NEW_ITEM_2}}

### Refined
- {{EXISTING_ITEM}}: {{WHAT_CHANGED}}

### Removed (with reason)
- {{REMOVED_ITEM}}: {{WHY_REMOVED}}

### Consolidation Due
- [ ] Last consolidation: {{LAST_CONSOLIDATION_DATE}}
- [ ] Entry count since: {{ENTRY_COUNT}}
- [ ] Consolidate when entry count exceeds {{THRESHOLD}}
```

### Worked Example: PROGRESS.md Delta Update

```markdown
## Delta -- 2026-04-19

### Added
- Completed G2 guide synthesis with full P1+P2 finding set (26 findings)
- Identified hidden cost mechanism: reasoning token amplification (14-22%)

### Refined
- Context tiering model: expanded from 2-tier (upfront/JIT) to 3-tier (always-on/task-scoped/on-demand)

### Removed (with reason)
- Embedding-only retrieval recommendation: removed because LIMIT benchmark proves catastrophic failure mode

### Consolidation Due
- [ ] Last consolidation: 2026-04-15
- [ ] Entry count since: 4
- [ ] Consolidate when entry count exceeds 10
```

---

### Sub-Agent Context Package

For curating context when dispatching work to sub-agents:

```markdown
## Context Package -- {{TASK_NAME}}

### Purpose
{{WHAT_THE_RESULT_WILL_BE_USED_FOR}}

### Audience
{{WHO_CONSUMES_THE_OUTPUT}}

### Workflow Position
{{WHAT_STEP_THIS_IS}} of {{TOTAL_STEPS}} -- depends on {{PRIOR_STEP}}, feeds into {{NEXT_STEP}}

### Success Criteria
- [ ] {{MEASURABLE_CRITERION_1}}
- [ ] {{MEASURABLE_CRITERION_2}}

### Required Context
{{PASTE_OR_LINK_ONLY_RELEVANT_SECTIONS}}

### Carry-Forward Notes
{{DECISIONS_OR_CONSTRAINTS_FROM_PRIOR_STEPS}}

### Constraints
- {{CONSTRAINT_1}}
- {{CONSTRAINT_2}}
```

### Worked Example: Context Package for Finding Extraction

```markdown
## Context Package -- Extract Pattern from "context-rot-silent-killer-and-mitigations"

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
Pattern template: systems/meta-system/knowledge/templates/pattern-template.md

### Carry-Forward Notes
Identification report classified this as "pattern" with MED confidence. Co-occurrence with delta-updates finding.

### Constraints
- Write to extracts/patterns/, not to meta-system/knowledge/patterns/
- Do not modify the source finding file
```

---

## Pitfalls

### 1. Treating the context window as a bucket
"We have 200K tokens, let's use them." Every unnecessary token degrades attention on the tokens that matter. Context management is about minimizing waste, not filling capacity. The attention mechanism creates n-squared pairwise relationships — cost is quadratic, not linear.

### 2. LLM-generated context files
ETH Zurich proved these reduce success rates by 3% while increasing cost by 20%. The agent explores more and tests more — following instructions faithfully but unproductively. When all repo documentation was removed, LLM-generated files actually improved by 2.7%, proving they duplicate what already exists.

### 3. Monolithic document rewrites
Every time an LLM rewrites a full context document, brevity bias silently drops domain-specific details. After a few rewrite cycles, the document retains only generic high-level statements. Use delta updates — append structured entries and consolidate periodically by human review, not LLM summarization.

### 4. Relying on embeddings for retrieval
Single-vector embeddings achieve under 20% Recall@100 on combinatorial queries while BM25 achieves 85.7%. For agent context selection, prefer filesystem navigation (glob/grep), index-file traversal, hybrid retrieval (lexical + semantic), or cross-encoder reranking over pure embedding search.

### 5. Context duplication across layers
The same constraint stated in the global CLAUDE.md, a system CLAUDE.md, and a skill file consumes 3x the tokens for zero added signal — and may create subtle contradictions when one copy is updated and the others are not.

### 6. Passing full parent context to sub-agents
A planning agent does not need the full codebase. An editing agent does not need the project roadmap. Scope each agent's context to the minimum it needs. Models perform worse when drowning in irrelevant context.

### 7. Ignoring hidden context sources
IDE context streaming, git status injection, and automatic tool discovery all consume tokens silently. These hidden sources can account for 10-20% of total context usage. Audit them explicitly.

### 8. Ignoring reasoning token amplification
Context files do not just add input tokens. They amplify reasoning tokens by 14-22% because the model actively reasons about every instruction, even irrelevant ones. A context file that adds 1000 input tokens may cost 3000+ total tokens when reasoning amplification is included.

### 9. One-size-fits-all context strategy
Claude Code does not benefit from human-written context files. Codex benefits from human-written files but is hurt by LLM-generated files. GPT-5.1 mini wastes tokens re-reading context files already in its window. Test context strategies against your actual model.

### 10. Over-pruning safety constraints
The opposite of bloat is starvation. Aggressive context minimization can remove constraints the agent genuinely needs. Test after pruning. If the agent starts violating boundaries that were previously respected, the constraint was doing work.

### 11. Stale cross-session learnings
A persistent learnings store that is never pruned or validated becomes a source of outdated constraints. Without expiry mechanisms, old learnings actively mislead the agent when the codebase has changed.

---

## Related Guides

- **Tool definition tokens and deferred loading:** If tool definitions are a major context consumer, see *Designing Agent Tools* (G5) for dynamic tool pool assembly and deferred loading patterns.
- **Context rot defense via state objects:** The explicit state object pattern is detailed in *Session Persistence and Memory* (G7), which covers structured state tracking, cross-session persistence stores, and session handoff protocols.
- **Context curation for measurement:** To measure whether removing a context element actually improves output, see *Building Agent Evaluation Suites* (G4) for eval-driven context optimization.

---

## Contract

### Preconditions
- You have an agent system where output quality, cost, or reliability is affected by what the agent sees in its context window.
- You can measure or estimate token usage per agent call.
- You have access to modify context files, agent dispatch logic, or system prompts.
- You know which model your agent uses (context sensitivity is model-specific).

### Invariants
- Every context element loaded into an agent's window has a justifiable reason for being there.
- Stable context is cached.
- Evolving documents use delta updates, not monolithic rewrites.
- Context health is measured, not assumed.
- Sub-agents receive scoped context appropriate to their task, not the parent's full window.
- Hidden context sources (IDE injection, git status) are accounted for in the budget.

### Governance
- Context file owners audit their files against the signal-to-noise criteria in this guide at least once per milestone.
- The context budget worksheet is reviewed when agent performance degrades or costs spike unexpectedly.
- Context architecture changes (new upfront files, changed sharding boundaries, tier reassignments) are documented.
- Model-specific context strategies are re-validated when the underlying model changes.
- This guide is owned by the Improvement Loop and deployed to the Meta-System knowledge layer after review.

### Recovery
- If agent output quality degrades: run the context audit checklist first. Context bloat and rot are the most common root causes.
- If token costs spike: check for cache invalidation (any character change forces full-price re-read), context duplication, reasoning token amplification from unnecessary instructions, hidden IDE context injection, or upfront loading of content that should be JIT.
- If context rot is suspected: compare current agent state against the explicit state object or contract to detect drift. If no state object exists, the absence of one is the root cause.
- If a new model performs differently: re-run the context audit with model-specific sensitivity in mind. What worked for Codex may not work for Claude Code, and vice versa.
