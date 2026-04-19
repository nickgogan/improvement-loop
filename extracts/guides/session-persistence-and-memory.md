---
title: "Session Persistence and Memory"
type: "guideline"
category: "Memory Architecture"
target_system:
  - "cross-system"
stage: "draft"
created: "2026-04-19"
updated: "2026-04-19"
author: "claude"
source_findings:
  - "session-persistence-crash-resilient"
  - "workflow-state-vs-conversation-state"
  - "incremental-one-feature-per-session-pattern"
  - "ground-truth-environmental-feedback-loops"
  - "effort-scaling-rules-embedded-in-orchestrator"
  - "file-based-task-locking-parallel-agents"
  - "scalpel-local-parse-then-llm-cost-optimization"
  - "biomimetic-memory-auto-recall-over-tool-based"
  - "claude-code-long-term-memory-via-pre-prompt-recall"
  - "four-tier-agent-memory-model-with-write-policy"
  - "dual-ingestion-funnel-human-clip-plus-llm-research"
  - "four-layer-enterprise-memory-stack"
  - "structured-fact-extraction-from-conversations"
  - "memory-cross-layer-promotion-governance"
source_dd:
  - "DD-81"
tags:
  - "guide"
  - "memory"
  - "session-persistence"
contract:
  preconditions: "You have an agent system that persists beyond a single prompt-response cycle. You can write to a filesystem or database. You understand the difference between what was said (conversation) and what was done (workflow state)."
  invariants: "Memory is layered with explicit tiers, not a flat persistence target. Workflow state is tracked separately from conversation state. Sessions leave the system in a clean, resumable state. Memory writes are policy-governed -- agents do not freely append to long-term stores. Environmental feedback, not self-assessment, drives decisions."
  governance: "Memory tier boundaries, promotion policies, and retention rules are documented per system. Session boundary conventions are enforced by handoff prompts. This guide is owned by Meta-System knowledge layer."
  recovery: "If an agent crashes mid-task: load the last persisted workflow checkpoint and resume from the last completed step. If session handoff loses context: read the progress file and last handoff prompt. If memory is corrupted: fall back to the last known-good tier and reconstruct. If parallel agents conflict: check the lock directory for abandoned locks."
---

# Session Persistence and Memory

How to build agent memory that survives crashes, scales across sessions, and does not pollute itself. This guide covers five concerns that look separate but are deeply coupled: what to remember, where to store it, how to recover, how to hand off, and how to govern writes across all of it.

## When to Use This Guide

- Your agent sessions run long enough that a crash would lose non-trivial work (>10 minutes)
- You need cross-session continuity where agents build on prior sessions' knowledge
- You are designing a memory architecture with multiple storage layers
- You need to coordinate parallel agents on shared state
- You want to control what agents write to persistent memory and at what quality bar

## Key Concepts

**1. Memory is a four-tier system, not a flat store.** Working memory (current context window), episodic memory (task history with provenance), semantic memory (knowledge graph of entities and policies), and governance memory (append-only audit log). Each tier has distinct read/write policies, retention targets, and ownership. Long context is not memory. A vector store is not automatically memory either. Memory is a deliberate read/write policy system.

**2. Conversation state is not workflow state.** "What was said" (chat transcript) is fundamentally different from "what step am I on and what side effects have occurred" (workflow state machine). Without separation, retrying after a crash re-executes side effects. Workflow state makes operations idempotent and retry-safe. Conversation state is supplementary context, never the source of truth for progress.

**3. Persist after events, not on shutdown.** Crashes happen during execution, not during graceful shutdown. Persist full session state after every significant event -- step completion, tool execution, permission grant, commit. The load/reconstruct/restore pattern enables deterministic recovery from any checkpoint.

**4. Auto-recall beats tool-based memory.** Giving an agent a "search memory" tool fails because the agent must realize it needs information it does not have. Injecting relevant memories into context automatically before every prompt removes this meta-cognitive requirement. The tradeoff is token cost, bounded by a recall budget (default ~1024 tokens).

**5. Memory writes require policy gates.** Unrestricted agent writes to long-term memory produce compounding pollution -- future retrievals return noisy data, which produces worse outputs, which get persisted again. Every write must follow: extract candidate, classify type, check policy, attach provenance, write with TTL and confidence score.

**6. One feature per session, clean state at exit.** Each session implements exactly one focused objective and leaves the system in a production-mergeable state. Context resets fully between sessions. The progress file carries forward what matters; conversation history does not.

**7. Ground truth beats self-assessment.** Agents should obtain concrete environmental feedback (test results, tool outputs, API responses) at each decision point. Self-assessment is unreliable because the same model that made the mistake evaluates whether a mistake was made.

---

## Part 1: Design Your Memory Architecture

Before implementing persistence or session management, decide what your agent needs to remember and where each type of memory lives.

### Step 1.1: Map the Four Tiers

Every agent memory system has four tiers, whether you design them explicitly or let them emerge accidentally. Design them explicitly.

| Tier | What It Stores | Lifespan | Read Policy | Write Policy |
|------|---------------|----------|-------------|-------------|
| **Working** | Current context, active plan, last 6-10 exchanges | Minutes/hours | Always loaded | Compacted aggressively |
| **Episodic** | Task history with provenance (who, what, when, why) | Months (with pruning) | Retrieved by semantic similarity | Append with evidence pointers |
| **Semantic** | Entities, relationships, constraints, policies | Years (curated) | Retrieved by structured query | Policy-gated, schema-owned |
| **Governance** | Audit log of every prompt, retrieval, action, output | Retention by policy | Not in hot path | Append-only, immutable |

The critical insight: most agent memory failures happen at **tier boundaries**, not within a single tier. Over-promotion of noisy events pollutes durable memory. Under-promotion causes repeated misses and wasted context.

### Step 1.2: Define Promotion and Demotion Policies

Every movement of data between tiers must be governed:

**Promotion (upward movement):**
- Working to Episodic: Append events from the current session with evidence pointers and temporal context
- Episodic to Semantic: Distill episodes into durable facts -- this is the highest-risk transition. Gate by explicit policy: only promote when knowledge "truly changed"
- Semantic updates: Schema ownership validation. Not every agent can write to shared semantic memory

**Demotion (pruning/compaction):**
- Working memory: strict token budget + compaction after each session
- Episodic memory: importance/recency scoring for garbage collection
- Semantic memory: small by design, curated, rarely pruned
- Governance memory: never pruned without policy authorization

**Governance questions to answer before building:**
1. Who owns the promotion policy for each tier boundary?
2. Who can override memory pruning?
3. What constitutes a rollback trigger?
4. How quickly can the team reconstruct a corrupted memory state?

### Step 1.3: Choose Your Recall Strategy

Two architectures for memory retrieval, with different failure modes:

| Strategy | How It Works | Failure Mode |
|----------|-------------|-------------|
| **Tool-based** | Agent has a `search_memory` tool it must choose to call | Agent does not realize it needs information it lacks -- silent miss |
| **Auto-recall** | System injects relevant memories into context before every prompt | Token cost on every turn, even when memories are irrelevant |

**Prefer auto-recall.** Tool-based memory fails at exactly the moment it is most needed: when the agent does not know what it does not know. Auto-recall makes memory a system-level concern, not an agent-level decision.

Tuning knobs for auto-recall:
- `recallMaxTokens`: bounds the token cost per turn (default ~1024)
- `recallBudget`: low/mid/high controls retrieval breadth
- Adaptive recall: start low, increase if the agent re-asks previously answered questions or contradicts past decisions

---

## Part 2: Implement Session State and Persistence

### Step 2.1: Separate Workflow State from Conversation State

Define explicit workflow states for your agent's task lifecycle:

```
planned --> awaiting_approval --> executing --> waiting_on_external --> completed
    ^                                                    |
    +-- failed (with retry count and last error) <-------+
```

Persist workflow state as structured data (JSON/YAML), not conversation history. Include:

| Field | Purpose |
|-------|---------|
| `current_step` | Which step in the workflow the agent is on |
| `completed_steps` | What has been done, with outcomes and side effects recorded |
| `pending_side_effects` | Side effects queued but not yet executed |
| `retry_count` | How many times the current step has been attempted |
| `last_error` | What went wrong on the last attempt |

This makes operations retry-safe -- on crash recovery, the agent skips completed steps and resumes from the last incomplete one without re-executing side effects.

### Step 2.2: Implement Crash-Resilient Persistence

Persist full session state after every significant event using a two-layer approach:

**Layer 1 -- Structured state (JSON/YAML):** Machine-readable, enables automated recovery.

**Layer 2 -- Narrative state (progress file, changelog):** Human-readable, enables cross-session context.

Git commits after every meaningful work unit serve as both a persistence mechanism and a recoverable history (demonstrated in multi-day autonomous scientific computing sessions).

**Recovery pattern:** load() -> reconstruct() -> restore(). Load the checkpoint file, reconstruct the workflow state from persisted data, restore the agent to the last known good state. If the external world has changed since the checkpoint, detect the drift and surface it to the user before resuming.

### Step 2.3: Extract Structured Facts, Not Raw Transcripts

Instead of storing conversation history as memory, extract discrete structured facts in the background after each agent turn:

| Fact Type | Example | Recall Trigger |
|-----------|---------|---------------|
| Decision | "Adopted fractal pattern for system organization" | Any discussion of system structure |
| Preference | "User prefers JSON responses" | Any formatted output request |
| Constraint | "DD-44 governs supersession lifecycle" | Any proposal to modify a DD |
| Technical context | "kb_parser.py has write_frontmatter()" | Any finding file write operation |

Facts should include: type, text content, timestamp, entities involved, and confidence score. Semantic ranking at recall time (not keyword matching) enables retrieval by relevance rather than recency.

**The compaction problem:** Claude Code's built-in compaction summarizes away critical decisions. Structured facts survive compaction because they live outside the conversation window. This is not a nice-to-have -- it is essential for any system running long enough to trigger compaction.

---

## Part 3: Manage Session Lifecycle

### Step 3.1: Define Session Boundaries

Each session follows a strict lifecycle:

1. **Read** the progress file and git history to understand current state
2. **Select** exactly one focused objective from the task list
3. **Execute** with environmental verification at each decision point
4. **Leave clean state** -- production-mergeable, no major bugs, documentation updated
5. **Update** the progress file for the next session

**Context resets fully between sessions.** The progress file and git history are the sole bridge. Conversation history does not carry forward.

**Ground truth at every decision point:** The agent obtains concrete environmental feedback (test output, lint results, tool responses) rather than self-assessing "I think this is correct." This prevents dead-end strategies and grounds decisions in observable reality.

### Step 3.2: Scale Effort to Task Complexity

Embed explicit resource allocation rules in orchestrator prompts so agents do not overinvest in simple tasks or underinvest in complex ones:

| Tier | Query Type | Subagents | Tool Calls | Example |
|------|-----------|-----------|------------|---------|
| 1 | Simple factual | 1 | 3-10 | "What is the current config value?" |
| 2 | Comparison / synthesis | 2-4 | 10-15 | "Compare these 3 approaches" |
| 3 | Complex multi-source research | 10+ | Divided roles | "Survey the landscape and produce a report" |

Token usage explains 80% of performance variance in multi-agent systems. Without scaling rules, orchestrators default to spawning as many subagents as possible regardless of task complexity.

### Step 3.3: Coordinate Parallel Agents

For parallel execution, use filesystem locks -- the simplest viable coordination:

```
shared/
+-- upstream/           # Bare git repo (shared state)
+-- locks/              # Task claim directory
|   +-- parse_if.txt    # Agent A claimed this task
|   +-- parse_for.txt   # Agent B claimed this task
+-- agents/
    +-- agent_a/        # Agent A's workspace (cloned from upstream)
    +-- agent_b/        # Agent B's workspace (cloned from upstream)
```

**Per-agent workflow:**
1. Acquire lock: atomic file creation in `locks/` named after the task
2. Pull and merge from upstream
3. Work on the claimed task
4. Push changes to upstream
5. Remove the lock file

No orchestrator, no inter-agent messaging, no central coordinator. Git history shows lock-taking as a natural audit trail. Scales linearly.

---

## Part 4: Design Ingestion Pipelines

### Step 4.1: Establish Dual Ingestion Funnels

Two parallel paths feed the memory system:

| Path | Source | Staging | Quality Gate |
|------|--------|---------|-------------|
| **Human-driven** | Web clipper, manual notes, observations | `raw/` folder for curation | Human review before promotion |
| **LLM-driven** | Autonomous research, structured extraction | Direct to structured format | Automated quality filter + periodic human audit |

The human path captures serendipitous discovery. The LLM path captures structured extraction at volume. Neither should bottleneck the other, but both need deduplication and cross-referencing to avoid contradictory entries on the same topic.

### Step 4.2: Use Local Parsing Before LLM Processing

For document-heavy ingestion, apply the scalpel pattern: local models handle structural decomposition (layout detection, OCR, text extraction) for free, and expensive LLM API calls are reserved for semantic understanding (entity extraction, relationship mapping, summarization). This reduces API costs by an order of magnitude and improves quality because the LLM receives clean, structured input rather than raw pixels.

---

## Templates

### Memory Architecture Specification

```yaml
# Memory Architecture — {{SYSTEM_NAME}}
system: "{{SYSTEM_NAME}}"
created: "{{ISO_8601}}"
owner: "{{OWNER}}"

tiers:
  working:
    store: "{{CONTEXT_WINDOW / IN_MEMORY}}"
    retention: "{{SESSION_DURATION}}"
    compaction: "{{AFTER_EACH_SESSION / EVERY_N_TURNS}}"
    max_tokens: {{TOKEN_BUDGET}}

  episodic:
    store: "{{DAILY_LOGS_DIR / DATABASE}}"
    retention: "{{MONTHS_WITH_PRUNING}}"
    write_policy: "append with evidence pointers"
    gc_scoring: "{{IMPORTANCE_WEIGHT}}% importance + {{RECENCY_WEIGHT}}% recency"

  semantic:
    store: "{{WIKI_DIR / KNOWLEDGE_GRAPH}}"
    retention: "years (curated)"
    write_policy: "policy-gated, schema-owned"
    promotion_gate: "{{WHO_APPROVES_EPISODIC_TO_SEMANTIC}}"

  governance:
    store: "{{AUDIT_LOG_DIR}}"
    retention: "append-only, {{RETENTION_POLICY}}"
    write_policy: "immutable append"

recall_strategy: "{{AUTO_RECALL / TOOL_BASED}}"
recall_budget: "{{recallMaxTokens}}"
retain_cadence: "every {{N}} turns with {{OVERLAP}} turn overlap"

promotion_policies:
  working_to_episodic: "{{CRITERIA}}"
  episodic_to_semantic: "{{CRITERIA — HIGHEST RISK TRANSITION}}"

rollback_triggers:
  - "{{CONDITION_1}}"
  - "{{CONDITION_2}}"
```

#### Worked Example: MetaSystem Memory Architecture

```yaml
# Memory Architecture — MetaSystem
system: "MetaSystem"
created: "2026-04-19"
owner: "Nick"

tiers:
  working:
    store: "context window (CLAUDE.md + PROGRESS.md injection)"
    retention: "session duration"
    compaction: "harness-managed compaction"
    max_tokens: 200000

  episodic:
    store: "MEMORY.md (auto-memory) + PROGRESS.md (session bridge)"
    retention: "indefinite (manual pruning)"
    write_policy: "append with session context"
    gc_scoring: "manual review — no automated scoring yet"

  semantic:
    store: "CLAUDE.md files (project + system), skills, rules"
    retention: "years (curated by Nick)"
    write_policy: "human-gated — Nick deploys all changes"
    promotion_gate: "Nick reviews and approves"

  governance:
    store: "git history + system-log entries"
    retention: "append-only, git-permanent"
    write_policy: "immutable (git commits)"

recall_strategy: "static file injection (CLAUDE.md at session start)"
recall_budget: "~15000 tokens across CLAUDE.md files"
retain_cadence: "session end (PROGRESS.md update)"

promotion_policies:
  working_to_episodic: "session-handoff skill writes to PROGRESS.md"
  episodic_to_semantic: "Nick manually updates CLAUDE.md or deploys rules/skills"

rollback_triggers:
  - "MEMORY.md entry contradicts a Design Decision"
  - "CLAUDE.md instruction produces repeated agent errors"
```

### Session Checkpoint Schema

```yaml
# Checkpoint — {{AGENT_NAME}} — {{SESSION_ID}}
session_id: "{{UUID}}"
agent: "{{AGENT_NAME}}"
started: "{{ISO_8601}}"
last_checkpoint: "{{ISO_8601}}"
objective: "{{WHAT_THIS_SESSION_IS_DOING}}"
workflow_state: "{{planned/awaiting_approval/executing/waiting_on_external/completed/failed}}"
completed_steps:
  - step: "{{STEP_NAME}}"
    outcome: "{{success/failure}}"
    side_effects: ["{{FILE_WRITTEN}}", "{{API_CALLED}}"]
    artifacts: ["{{FILE_PATHS}}"]
    tokens: {input: {{N}}, output: {{N}}}
pending:
  - "{{NEXT_STEP}}"
retry_count: {{N}}
last_error: "{{ERROR_MESSAGE_OR_NULL}}"
constraints_active:
  - "{{CONSTRAINT}}"
progress_summary: "{{ONE_LINE_FOR_NEXT_SESSION}}"
```

#### Worked Example: Research Loop Session Checkpoint

```yaml
# Checkpoint — research-loop — sess-2026-04-19-001
session_id: "sess-2026-04-19-001"
agent: "research-loop"
started: "2026-04-19T09:00:00Z"
last_checkpoint: "2026-04-19T09:45:00Z"
objective: "Scan 5 new sources from watch list, extract findings"
workflow_state: "executing"
completed_steps:
  - step: "fetch_source_1"
    outcome: "success"
    side_effects: ["wrote research-sources/new-source-1.md"]
    artifacts: ["research-sources/new-source-1.md"]
    tokens: {input: 12000, output: 3500}
  - step: "extract_findings_source_1"
    outcome: "success"
    side_effects: ["wrote research-findings/new-finding-1.md", "wrote research-findings/new-finding-2.md"]
    artifacts: ["research-findings/new-finding-1.md", "research-findings/new-finding-2.md"]
    tokens: {input: 8000, output: 6000}
pending:
  - "fetch_source_2"
  - "fetch_source_3"
  - "extract_findings_source_2"
  - "extract_findings_source_3"
retry_count: 0
last_error: null
constraints_active:
  - "max 10 findings per session"
  - "P1 priority sources first"
progress_summary: "2/5 sources processed, 2 findings extracted. Next: source 2 (Anthropic blog post on agent memory)."
```

### Memory Write Policy

```yaml
# Write Policy — {{SYSTEM_NAME}}
system: "{{SYSTEM_NAME}}"

write_pipeline:
  1_extract: "Identify candidate memory from {{SOURCE — conversation / tool output / session summary}}"
  2_classify: "Assign type: {{working / episodic / semantic / user}}"
  3_policy_check: "Is {{AGENT_ROLE}} authorized to write to {{TARGET_TIER}}? {{YES_POLICY / ESCALATE_TO}}"
  4_provenance: "Attach: source={{SOURCE}}, confidence={{HIGH/MED/LOW}}, timestamp={{ISO_8601}}"
  5_write: "Write with TTL={{DURATION}} and confidence={{SCORE}}"

read_ranking:
  weights:
    recency: {{RECENCY_WEIGHT}}
    source_reliability: {{RELIABILITY_WEIGHT}}
    user_relevance: {{RELEVANCE_WEIGHT}}

prohibited_writes:
  - "{{CATEGORY_1 — e.g., raw conversation transcripts to semantic tier}}"
  - "{{CATEGORY_2 — e.g., unvalidated facts to governance tier}}"
```

#### Worked Example: MetaSystem Write Policy

```yaml
# Write Policy — MetaSystem
system: "MetaSystem"

write_pipeline:
  1_extract: "Identify candidate memory from session work (decisions, preferences, constraints discovered)"
  2_classify: "Assign type: working (PROGRESS.md) / episodic (MEMORY.md) / semantic (CLAUDE.md, rules)"
  3_policy_check: "Agent can write to working and episodic. Semantic requires Nick's approval."
  4_provenance: "Attach: source=session-N, confidence=HIGH/MED, timestamp=2026-04-19"
  5_write: "Working: immediate. Episodic: session end. Semantic: after human review."

read_ranking:
  weights:
    recency: 20
    source_reliability: 50
    user_relevance: 30

prohibited_writes:
  - "Raw conversation transcripts to MEMORY.md (extract structured facts instead)"
  - "Unreviewed agent opinions to CLAUDE.md (human gate required)"
  - "Hardcoded counts or volatile data to any persistent tier"
```

### Parallel Coordination Setup

```markdown
## Parallel Agent Setup — {{PROJECT_NAME}}

### Shared Infrastructure
- Upstream repo: {{PATH}}
- Lock directory: {{PATH}}/locks/
- Agent count: {{N}}

### Lock Protocol
- Lock acquisition: atomic file creation in locks/
- Lock timeout: {{MINUTES}} minutes (detect abandoned locks)
- Lock metadata: agent ID, timestamp, task description
- Conflict resolution: {{GIT_MERGE / HUMAN_REVIEW}}

### Per-Agent Configuration
| Agent | Workspace | Task Scope |
|-------|-----------|-----------|
| {{AGENT_1}} | {{PATH}} | {{SCOPE}} |
| {{AGENT_2}} | {{PATH}} | {{SCOPE}} |
```

---

## Worked Example: MetaSystem Current State and Gaps

```
Session Management — MetaSystem (April 2026)

MEMORY TIERS (implicit, not designed):
  Working:  CLAUDE.md files + PROGRESS.md injection at session start  [exists]
  Episodic: MEMORY.md (auto-memory, append-only, unstructured)       [exists, no provenance]
  Semantic: CLAUDE.md, skills, rules                                 [exists, human-gated]
  Governance: git history + system-log entries                       [exists, append-only]

RECALL STRATEGY:
  Static file injection (CLAUDE.md loaded at session start)          [exists]
  Auto-recall from semantic store                                    [gap — no semantic query]
  Tool-based memory search                                           [gap — no search tool]

SESSION BOUNDARY PROTOCOL:
  1. Read PROGRESS.md -> understand current state                    [enforced]
  2. Single focused objective per session                            [enforced via handoff prompts]
  3. Environmental feedback: file reads, grep, frontmatter checks    [enforced]
  4. Clean state: all files written, indexes updated                 [enforced]
  5. Update PROGRESS.md + write handoff prompt                       [enforced]

WRITE POLICY:
  Working: agent writes freely                                       [exists]
  Episodic: agent appends to MEMORY.md                               [exists, no quality filter]
  Semantic: human gate (Nick deploys)                                 [exists, enforced]
  Governance: git commits (automatic)                                [exists]

GAPS IDENTIFIED:
  1. No structured checkpoint (JSON workflow state)
     -> crash recovery requires full session replay
     -> APPLY: Step 2.1 (workflow state separation) + Step 2.2 (persistence)

  2. MEMORY.md lacks provenance, TTL, or confidence scoring
     -> no way to distinguish high-confidence decisions from speculative observations
     -> APPLY: Memory Write Policy template + Step 1.2 (promotion policies)

  3. No auto-recall from episodic or semantic memory
     -> agent relies on static CLAUDE.md injection only
     -> APPLY: Step 1.3 (auto-recall vs tool-based)

  4. No structured fact extraction
     -> decisions embedded in conversation are lost to compaction
     -> APPLY: Step 2.3 (structured fact extraction)

  5. No effort scaling rules in orchestrator prompts
     -> subagent count is ad hoc per skill
     -> APPLY: Step 3.2 (effort scaling)

  6. No parallel coordination (lock-based or otherwise)
     -> single-session only (extract-artifacts uses disjoint dispatch, not locks)
     -> APPLY: Step 3.3 (parallel coordination) when parallel work begins
```

---

## Decision Tree: What Kind of Memory Problem Do You Have?

```
START: What is failing?
  |
  +-- "Agent forgets decisions from prior sessions"
  |     -> Step 2.3: Extract structured facts from conversations
  |     -> Step 1.3: Implement auto-recall for fact injection
  |
  +-- "Agent crashes and loses all progress"
  |     -> Step 2.1: Separate workflow state from conversation state
  |     -> Step 2.2: Implement crash-resilient persistence
  |
  +-- "Agent's memory is full of noise / contradictions"
  |     -> Step 1.2: Define promotion and demotion policies
  |     -> Memory Write Policy template: add provenance and TTL
  |
  +-- "Sessions overrun context and quality degrades"
  |     -> Step 3.1: One feature per session with clean-state exit
  |     -> Step 3.2: Effort scaling rules in orchestrator
  |
  +-- "Parallel agents step on each other's work"
  |     -> Step 3.3: Filesystem locks for coordination
  |
  +-- "Memory retrieval misses relevant information"
  |     -> Step 1.3: Switch from tool-based to auto-recall
  |     -> Step 2.3: Ensure facts are typed and semantically embeddable
  |
  +-- "Document ingestion is too expensive"
        -> Step 4.2: Local parsing before LLM processing
```

---

## Pitfalls

### 1. Conversation history as the only state
Conversation transcripts are not retry-safe, not queryable, and grow unbounded. Separate workflow state (structured, persistent, retry-safe) from conversation state (append-only, ephemeral). Never derive workflow state from conversation replay.

### 2. Persist only on shutdown
Crashes happen during execution. Persist after every significant event -- step completion, tool execution, permission grant, commit. The load/reconstruct/restore pattern must work from any checkpoint, not just the final one.

### 3. Unrestricted agent writes to long-term memory
Without a write policy, agents pollute durable memory with unvalidated, low-confidence, or hallucinated information. This creates a compounding reliability problem: future retrievals return polluted data, which produces worse outputs, which get persisted again. Memory pollution is distinct from context rot -- it affects future sessions, not just the current one.

### 4. Tool-based memory as the only recall mechanism
Requiring the agent to decide when to search memory fails at exactly the moment it matters most: when the agent does not know what it does not know. Auto-recall removes this meta-cognitive requirement. The token cost is real but bounded and worth it.

### 5. Multi-feature sessions
Sessions that tackle multiple features exhaust context, leave unclean state, and make handoffs fragile. One feature, clean state, update progress. The constraint feels slow but yields higher throughput across a sequence of sessions.

### 6. Self-assessed progress
"I think this is correct" is not verification. Environmental feedback (test results, tool output, API responses) is the only reliable verification signal. Agents that self-assess pursue dead-end strategies without detection.

### 7. Promotion without governance
The highest-risk operation in any memory system is cross-layer promotion -- especially episodic to semantic. Uncontrolled promotion pollutes the knowledge layer that every future session relies on. Define explicit ownership, approval levels, and rollback paths for every tier boundary.

### 8. Raw transcript storage as memory
Storing entire conversation transcripts is expensive, noisy, and makes recall brittle (keyword search) or costly (full embedding). Extract discrete typed facts instead. Facts are compact, individually embeddable, and survive compaction.

---

## Related Guides

- **Memory tiers map to agent infrastructure:** The four-tier model in Step 1.1 is the memory dimension of the infrastructure tiers described in *Agent Architecture Decisions* (G3), Step 6.
- **Session resets defend against context rot:** The clean-state session boundaries in Step 3.1 are context rot mitigations described in *Managing Agent Context* (G2), Step 4.
- **Effort scaling requires baseline measurement:** The effort scaling rules in Step 3.2 presuppose the single-agent baseline measurement in *Agent Architecture Decisions* (G3), Step 1.
- **Structured facts are context engineering:** The fact extraction in Step 2.3 connects to the context curation patterns in *Managing Agent Context* (G2).
- **Write policies connect to governance:** The memory write policy in Step 1.2 is the memory-specific instantiation of the governance patterns in *Agent Governance and Trust* (G9).

---

## Contract

### Preconditions
- You have an agent system that persists beyond a single prompt-response cycle.
- You can write to a filesystem or database for state persistence.
- You understand the difference between conversation state (what was said) and workflow state (what was done).

### Invariants
- Memory is organized into explicit tiers with defined read/write policies per tier.
- Workflow state is tracked separately from conversation state and is the authoritative record of progress.
- Sessions leave the system in a clean, resumable state verified by automated checks.
- Memory writes are policy-governed -- agents do not freely append to long-term stores without provenance, classification, and authorization.
- Environmental feedback, not self-assessment, drives agent decisions at every state-modifying step.
- Promotion across tier boundaries is the highest-risk operation and is explicitly governed.

### Governance
- Memory tier boundaries, promotion policies, and retention rules are documented per system.
- Session boundary conventions (one-feature, clean-state, progress-update) are enforced by handoff prompts.
- Write policies specify which agent roles can write to which tiers.
- This guide is owned by Meta-System knowledge layer.

### Recovery
- If an agent crashes mid-task: load the last persisted workflow checkpoint, identify completed side effects, resume from the next incomplete step. Do not replay the conversation.
- If session handoff loses context: read PROGRESS.md and the handoff prompt from the prior session.
- If memory is corrupted at a tier: fall back to the last known-good state at that tier and reconstruct. Governance tier (git history) is the ultimate fallback.
- If parallel agents conflict: check the lock directory for abandoned locks; resolve via git merge or human review.
- If promotion pollutes the semantic tier: quarantine the affected entries, review the promotion filter, reconstruct from episodic tier if needed.
