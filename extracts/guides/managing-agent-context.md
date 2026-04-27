---
title: "Managing Agent Context"
type: "guideline"
category: "Context Engineering"
target_system:
  - "cross-system"
stage: "draft"
created: "2026-04-19"
updated: "2026-04-26"
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
  - "five-context-management-techniques-in-claude-code"
  - "progressive-tiered-context-loading-convergence"
  - "catastrophic-context-collapse-risk-during-claudemd"
  - "claudemd-context-rot-from-indiscriminate-rule-accu"
  - "context-file-taxonomy-claudemd-soulmd-agentsmd"
  - "cross-platform-context-file-strategy"
  - "global-vs-project-level-skill-and-context"
  - "model-native-context-window-awareness"
  - "monorepo-context-distribution-three-strategies"
  - "progressive-skill-loading"
  - "self-describing-codebase-structural-semantic-context"
  - "session-atomicity-single-issue-scope-quadratic-cost-reduction"
  - "three-layer-folder-as-workspace-architecture"
  - "three-tier-progressive-context-loading"
  - "three-tier-vault-architecture-global-shared-local"
  - "progress-md-session-bridge"
  - "skills-as-pointers-to-second-brain-files"
  - "trajectory-engineering-non-linear-session-forking"
source_dd:
  - "DD-81"
tags:
  - "guide"
  - "context-engineering"
  - "context-architecture"
contract:
  preconditions: "Agent system exists with context files or context injection mechanism"
  invariants: "Context budget stays within model limits; context freshness maintained; architecture decisions are explicit at the file, tier, tool, and session layers"
  governance: "IL-owned draft; Nick deploys to meta-system/knowledge/guides/"
  recovery: "If context rot detected, run context audit procedure from this guide"
---

# Managing Agent Context

Your agent is losing context, burning tokens, or drifting from its goals. This guide covers why that happens and what to do about it — from auditing what is in the window, to structuring context for selective loading, defending against silent degradation, choosing the right management technique mid-session, and architecting context across the tools, tiers, and sessions where your agents actually run.

## When to Use This Guide

- Agent output quality degrades over long sessions or multi-step workflows
- Token costs are higher than expected or growing without clear cause
- You are designing context files (CLAUDE.md, system prompts, skill definitions) for a new agent
- You suspect context rot — the agent forgets constraints, re-derives conclusions, or drifts from requirements
- You are scaling from a single agent to multi-agent pipelines and need context isolation
- You are bootstrapping a new system and need to decide what goes into the initial context package
- You operate across multiple AI tools (Claude Code + Copilot + Cursor + Codex) and need a single set of project conventions all of them can read
- You are growing into a monorepo and "one CLAUDE.md for everything" is starting to drown package-specific context
- You manage multiple roles (developer, marketer, EA) with overlapping but distinct skill sets and need scope discipline

**Do not use for:** defining what the agent should do (see G1: *Writing Agent Specifications*), designing the agent's tool set (see G5: *Designing Agent Tools*), or evaluation suite design (see G4: *Building Agent Evaluation Suites*).

## Key Concepts

**1. Context is a finite, depletable resource — not a bucket.** As tokens accumulate, transformer attention budget depletes across n-squared pairwise relationships. Every unnecessary token actively degrades the model's recall of tokens that matter. Context management is not "stay under the limit" — it is "minimize waste at all times."

**2. More context often makes output worse — and the cost is hidden.** ETH Zurich (2026) proved that LLM-generated context files reduce agent success by 3% and increase cost by 20%. But the cost goes deeper: context files increase reasoning token usage by 14-22%, meaning agents spend compute processing irrelevant instructions rather than solving the task. The true cost is input bloat + reasoning amplification + additional steps (2.45-3.92 extra steps per task).

**3. Context rot is the #1 silent killer.** Agents forget constraints, drift from goals, and re-derive nonsensical conclusions over long sessions. The output looks plausible but increasingly deviates from requirements. Standard monitoring (error rates, latency) will not catch it — only explicit state tracking and contract validation detect drift before it compounds.

**4. Structure beats volume.** The difference between effective and wasteful context is not how much you provide but how you organize it: small high-signal files loaded upfront, everything else retrieved just-in-time, evolving documents updated incrementally, and each agent scoped to the minimum it needs.

**5. Context sensitivity is model-specific.** Claude Code (Sonnet-4.5) was the only agent in the ETH Zurich study where even human-written context files failed to improve performance. Different models respond dramatically differently to the same context files. One-size-fits-all context strategies are empirically wrong — optimize for the model you are actually using.

**6. Context architecture spans tools, tiers, and sessions — not just files.** A complete context architecture has decisions at four layers: per-file (what goes inside), per-tier (global vs project vs ephemeral), per-tool (Claude Code vs Copilot vs Cursor vs Codex), and per-session (how state crosses session boundaries). Treating only the first layer leaves the others to accumulate by accident, which is where most "my agent is bad" problems actually live.

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

### Skills as Pointers to a Second Brain

The pointer principle scales to skill definitions. Once a centralized knowledge base exists (Obsidian vault, internal wiki, second-brain folder), each skill's `SKILL.md` should contain only:

1. The workflow the agent follows
2. Path references to where it should read shared context

Instead of `skills/linkedin-writer/references/icp.md` embedding the ideal-customer-profile, the SKILL.md says "read ICP context from `/second-brain/business/icp.md`." Updates to the ICP propagate automatically to every skill that references it. Teams running 30+ skills with embedded shared context experience version drift; the pointer pattern collapses shared context into a single source of truth and eliminates the per-skill maintenance surface.

Migration heuristic: identify reference files duplicated across multiple skills → move the canonical copy to the second brain → replace the in-skill reference with a path. Low-churn, skill-specific content can remain embedded.

### Self-Describing Codebases as a Context Layer

Context engineering does not stop at the prompt window — the codebase itself is a context source. Two structural layers make a codebase legible to agents (and to humans) without requiring tribal knowledge:

- **Structural context (answers "where").** Every module gets a manifest covering: what the module does, what it depends on (dependencies in), what depends on it (dependencies out). This makes navigation and impact analysis legible by reading the manifest rather than reverse-engineering import graphs.
- **Semantic context (answers "what").** Every interface — not just public APIs — carries a behavioral contract: performance expectations, failure modes, retry semantics, behavioral guarantees. This goes beyond data shape; the intent is to give any reader (agent or human) the rules of engagement for using the interface.

This is high-leverage for agentic development: when an agent reads a module manifest, it has explicit dependency context that would otherwise require inference. When it reads a behavioral contract, it has explicit failure-mode guidance that would otherwise require reverse-engineering. The Module Manifest Template (Templates section) provides a starter format.

Watch for two failure modes: manifests drift from implementation (becoming misleading), and teams write structural manifests but skip the harder semantic-contract layer (the more valuable one).

---

## Step 3: Structure for Selective Loading

### 3a: Tier Your Context (File-Granularity)

Instead of loading one monolithic file into every interaction, categorize instructions by when they are needed:

| Tier | What Goes Here | When Loaded | Token Budget |
|------|---------------|-------------|--------------|
| **Tier 0 (Always-On)** | Identity, safety constraints, hard rules | Every interaction | < 20 lines |
| **Tier 1 (Task-Scoped)** | Coding conventions when coding, test patterns when testing, review criteria when reviewing | When task type is detected | Varies by task |
| **Tier 2 (On-Demand)** | Architecture overviews, dependency docs, reference material | When agent signals need | Retrieved JIT |

ETH Zurich data shows task-relevant instruction subsets reduce context by 60-80% while maintaining or improving accuracy compared to monolithic file loading. The cost savings alone (20%+ reduction in inference cost) justify the structural investment.

### 3b: Tier Your Content (L0/L1/L2 — Content-Granularity)

Tiering at the file granularity (3a) decides *which files* to load. Tiering at the content granularity decides *how much of each file* to load. The pattern is converging across the ecosystem with at least six independent implementations: BMAD's L1/L2/L3, OpenViking's L0/L1/L2, DeerFlow's skill descriptions → SKILL.md, Beads' SKILL.md → 14 resource files, plus Claude Code's deferred tool loading and MCP's progressive tool discovery. This convergence is among the strongest signals in the registry — independent teams arriving at the same design principle.

| Tier | Size | What it is | When read |
|------|------|------------|-----------|
| **L0 — Abstract** | ~100 tokens | Semantic summary generated at ingest | Initial scoring; "is this relevant at all?" |
| **L1 — Overview** | ~1-2k tokens | Structural summary; outline; section headings | Reranking; "is this section worth opening?" |
| **L2 — Full** | unbounded | Original content | Final read; "I'm using this content now" |

The retrieval pipeline scores at L0, reranks at L1, reads at L2 only for top-ranked results. Token budget is enforced at each tier boundary. This addresses the fundamental tension: loading full content for all candidates is wasteful; loading nothing until selected means the selection has no content signal.

MetaSystem's `_index.md` files function as a partial L0/L1 implementation — formalizing tier labels and automating L0 generation would close the gap.

### 3c: Shard Large Documents

Break monolithic documents into focused, role-specific shards. Each agent loads only the shards relevant to its current task.

| Instead of | Shard into |
|------------|-----------|
| Full PRD (5000 lines) | `coding-standards.md`, `tech-stack.md`, `data-model.md`, `api-contracts.md` |
| Monolithic CLAUDE.md | Global CLAUDE.md (60 lines) + per-system CLAUDE.md files |
| Single architecture doc | One file per subsystem boundary |
| Full tool registry | Session-specific tool subsets via mode flags and deny lists |

**Sharding rule:** Each shard should be loadable independently without losing critical context. If shard A requires shard B to make sense, they should be one file or the dependency should be explicit.

### 3d: Use the Hybrid Context Architecture

Combine upfront and just-in-time modes:

| Mode | What Goes Here | Why |
|------|---------------|-----|
| **Upfront (always loaded)** | Small, high-signal files: CLAUDE.md, system prompt, persona, tool defs | Immediate availability, no retrieval latency, cacheable |
| **Just-in-time (retrieved on demand)** | Everything else: docs, code, reference material | Context efficiency — load only when needed |

The upfront layer should be small enough that it does not crowd out task-specific context. The JIT layer uses filesystem primitives (glob, grep, read) rather than embedding-based retrieval. Single-vector embeddings achieve under 20% Recall@100 on combinatorial queries while BM25 achieves 85.7%. For small-to-medium knowledge bases (under 1000 documents), index-file navigation — reading an `_index.md` and following links — outperforms RAG pipelines with zero infrastructure overhead.

### 3e: Use CLAUDE.md as a Traversal Guide

For knowledge-base-heavy projects, the CLAUDE.md file serves double duty: project rules plus a navigation protocol that teaches the agent how to find information efficiently.

Effective traversal instructions:
- Where to find the master index
- How to read per-section indexes and follow links
- File structure conventions for new files (so the agent maintains navigability)
- What to read first vs. what to retrieve on demand

Without traversal instructions, agents use expensive tool calls (glob, grep) to discover structure on every query. With a navigation protocol, the agent follows a deterministic 2-3 file read path: master index, section index, target file.

### 3f: Curate Context for Downstream Agents

When dispatching work to sub-agents, do not pass your full context window. Produce a self-contained context package with exactly what the sub-agent needs:

- Relevant architecture sections (not the full doc)
- Task-specific constraints (not all system constraints)
- Carry-forward notes from prior steps when dependencies exist
- Acceptance criteria for the sub-agent's output
- Purpose, audience, and workflow position (context enrichment)

The sub-agent should never need to search for information to start working. If it does, the context curation was incomplete. This is the "scrum master" pattern: a curator agent reads multiple sources and produces a context-complete handoff file so the executing agent starts with a focused, complete window.

### 3g: Progressive Skill Loading

Tiered loading also applies at the skill level. Bulk-loading 16+ skills at boot consumes 8-32k tokens of context before the first user message. The progressive pattern: at boot, scan all enabled skills and inject only their `name` + `description` (~50 tokens each) as `<skill>` XML elements. The full SKILL.md (~500-2000 tokens) is loaded on-demand via `read_file` when a task matches.

DeerFlow implements this against `skills/public/*/SKILL.md`; Claude Code's tool-search pattern is the same shape applied to tools rather than skills; MetaSystem's skill-description tables in CLAUDE.md are a partial implementation. Skills are higher-level than tools (they contain multi-step workflows, references, templates) and therefore even more expensive to load — making progressive loading more valuable, not less.

Tradeoff: agents may not recognize when a skill is relevant if the description is too terse, and `read_file` adds a tool-call round trip. Mitigations: write descriptions for discoverability not just identity; pre-warm skill caches at startup if cold reads are too slow.

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

### 4e: Pick Your Context-Management Technique (Preference Order)

Mid-session, you have at least five distinct techniques with sharply different cost/quality tradeoffs. Choosing wrong is one of the most common sources of quality degradation. Use the preference order:

| Rank | Technique | Mechanism | Time Cost | Quality | When to Use |
|------|-----------|-----------|-----------|---------|-------------|
| **1** | **Sub-agent spawn** | Fresh window for an isolated task | Low | Best (no information loss) | Bounded sub-task with a clear scope and deliverable |
| **2** | **/handoff + /clear** | User-requested structured handoff doc, then full clear | High (writing the doc) | High (precisely controlled summary) | Major phase transitions; ending a session you'll resume |
| **3** | **/re (context trimming)** | Selective removal of completed/irrelevant context | Medium | Good (manual selection required) | Mid-session bug fix where the bug-finding context is now noise |
| **4** | **/clear (destructive reset)** | Complete context wipe | Low | Risky alone — best paired with re-orientation | At a clean break; combine with CLAUDE.md re-read |
| **5** | **Compaction** | Automatic LLM compression | Lowest | Lowest (significant information loss; black-swan collapse risk) | Last resort when nothing else is appropriate |

The default (compaction) is the worst option. Sub-agents and `/handoff + /clear` are dramatically better. Compaction at the wrong moment (mid-implementation) causes irreversible information loss; `/clear` without a handoff loses all implementation context; sub-agents without a clear scope produce fragmented, unwired code.

### 4f: Trajectory Engineering — Fork and Trim

Treat the session as a tree, not a linear chat. Use Claude Code's `/re` (or Esc+Esc) to time-travel to any prior point:

1. **Trim after fix.** When you finish debugging, rewind to before the bug was spotted, paste a 2-3 line summary of what happened and the fix, and continue from that clean state. The bug-finding context is now dead weight.
2. **Fork to compare.** When exploring two architectural options, fork from a common starting point, run each branch down its trajectory, compare results, and keep the best.
3. **Trim back to trunk.** After each exploration, return to the lean trunk (stable repo info, current plan) — branches (debugging attempts, dead ends) get pruned.

Anthropic's April 2026 framing promotes rewind from "advanced technique" to first-class default: "Rewind is often the better approach to correction" — over forward-patching with "that didn't work, try X." The shortcut is officially Esc+Esc.

This requires mental tagging of trunk vs. branch content; trimming load-bearing context by accident is the failure mode. Time-travel is also session-scoped — it cannot restore context from a previous session.

### 4g: Layer Harness and Model-Side Awareness

Window-headroom awareness lives at two layers; combine both for layered defense:

- **Harness layer (pre-turn projection).** The harness measures input tokens *before* calling the model and gates the call (compact, summarize, abort). Catches the failure mode where the model is about to overrun without realizing it.
- **Model-native layer.** Sonnet 4.5, Sonnet 4.6, and Haiku 4.5 track their own remaining headroom internally and can reason about it inline ("I have N tokens left, let me wrap up"). The ACL 2025 "Token-Budget-Aware Reasoning" paper shows that surfacing the budget to the model explicitly compresses the reasoning trace to fit. Anthropic ships this by default on 4.5+ models; no opt-in required.

Native awareness does not replace pre-turn projection — it catches a different failure mode (the harness's projection was wrong and the user was inattentive). Mixed-model loops lose the model-native guarantee unless every link in the chain has it. Verify behavior on your specific model; Opus 4.7's behavior, for example, is not documented in the same terms as 4.5.

---

## Step 5: Defend Against Context Rot

Context rot is silent — the agent's output looks plausible but increasingly deviates from requirements. Seven production-tested defenses:

**1. Maintain an explicit state object.** Track active constraints, goals, and accumulated decisions as structured data (YAML/JSON), not conversation history. Prose summarization loses precision. The state object is the source of truth for what the agent should be attending to.

**2. Validate against contracts at each step.** If the agent produces structured output, validate it against its task contract before passing it downstream. Contract violations are early rot indicators.

**3. Use delta updates for evolving documents.** When context documents change over time (playbooks, progress files, accumulated notes), update incrementally — append structured entries, then periodically consolidate. Never rewrite the full document with an LLM, as brevity bias silently drops domain-specific details. The ACE framework (Stanford/SambaNova) demonstrates that structured playbook accumulation with deduplication outperforms compaction by +10.6% on agentic benchmarks.

**4. Persist learnings across sessions.** Hard-won context disappears at every session boundary. A structured global learnings store — with CRUD operations, auto-injection into planner context, and relevance filtering — converts repeated failures into durable institutional knowledge. Without expiry or validation mechanisms, the store degrades into noise, so prune and update.

**5. Reset context at natural boundaries.** New sessions, new workflow phases, and completed milestones are natural reset points. Re-inject the upfront context layer and start with a fresh conversation rather than accumulating stale turns.

**6. Bound sessions to single atomic issues.** Yegge's claim from the Beads coding-agent system: each agent session bounded to exactly one fine-grained issue produces *quadratic* cost reduction relative to multi-task sessions. Mechanism: a session handling N tasks needs O(N²) context (each task's intermediate state pollutes every subsequent task's context); N sessions each handling one task needs O(N) total. The session boundary is also a natural kill point — agents approaching context limits can be terminated at issue completion without losing work, since state lives in the issue store, not agent memory. Requires a persistent work queue (Beads JSONL, GitHub issues, etc.) so agents pick up single issues without parsing a full plan.

Watch for over-atomization: issues too fine-grained generate more coordination overhead than they save in context overhead. The break-even depends on orchestrator communication cost.

**7. Don't let Claude compact your own CLAUDE.md.** Asking Claude to summarize or compact CLAUDE.md introduces a fixed per-attempt probability (~3%, increasing ~0.25% per additional compaction) of *catastrophic context collapse* — the entire playbook reduces to ~100-200 tokens, accuracy drops to ~57% of previous, often *below* the no-CLAUDE.md baseline. A sparse, inaccurate summary is worse than no summary at all. Users who compact repeatedly are eventually guaranteed to trigger collapse, then continue with a poisoned context, blaming the model.

Safer alternatives: ACE-style voting curation (multi-shot consensus, not single rewrite), `/clear` + handoff documents at natural break points, and git-snapshot the CLAUDE.md before any compaction so rollback is one command.

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

### Cost Compounds at the Session Layer

Per-call optimization is necessary but not sufficient. The session-scoping pattern (Step 5 defense #6) compounds cost reduction quadratically — an N-task session does not just cost N times a single-task session, it costs O(N²) because each task's context bloats every subsequent task. Splitting long sessions into many short ones is often the largest single cost win available, separate from any per-call optimization.

---

## Step 7: Offload to External Knowledge Bases

When your reference material exceeds what fits efficiently in the context window, offload to external query layers:

- **NotebookLM** for project-specific research, YouTube transcripts, and accumulated reference material. Claude Code queries it on demand, keeping the context window lean while maintaining access to extensive documentation. The "grounded" aspect is critical — NotebookLM only uses sources you provide, eliminating hallucination from the knowledge layer.
- **Obsidian wiki with index navigation** for internal codebase memory and institutional knowledge. The LLM maintains an `_index.md` and navigates via wiki-links, achieving effective retrieval for under 1000 documents with zero infrastructure overhead. This second-brain pattern compounds when paired with the skills-as-pointers approach (Step 2): one canonical knowledge layer, many skills that read from it.
- **Context7** (or equivalent) for library documentation, API references, and framework-specific content.

The principle: keep task context in the window, keep reference context queryable externally.

---

## Step 8: Architect Context Across Tools, Tiers, and Sessions

Steps 1-7 operate within a single context window or single project. Real-world context architecture also has decisions at the workspace, tool, and session layers. Get these wrong and the per-file optimizations will not save you.

### 8a: Three-Tier Vault Architecture (Global / Shared / Local)

Organize the file system into three tiers with distinct sharing and persistence rules:

| Tier | Location | Holds | Sharing | Persistence |
|------|----------|-------|---------|-------------|
| **Tier 1 — Global** | `~/.claude/` | Agent identity; universal skills (`/bootstrap`, `/resume`, `/compress`); cross-project behaviors | Travels with the developer | Permanent |
| **Tier 2 — Shared** | git repo | Project reference files; patterns; playbooks | Cloneable by collaborators | Versioned |
| **Tier 3 — Local** | gitignored | PROGRESS.md (when not committed); agent logs; auth tokens; ephemeral state | Private | Mutable runtime state |

Without tiering, agents either over-share sensitive state or under-share reusable knowledge. A collaborator can clone Tier 2 and immediately have the same reference library — no manual onboarding. Tier 2 is vulnerable to bloat if reference files are added but never pruned; assign an owner and a review cadence.

### 8b: Three-Layer Folder-as-Workspace Architecture

For projects that span multiple workspaces (writing, production, community, research), a three-layer folder structure lets one Claude Code instance adapt to many domains without pre-programmed agents:

- **Layer 1 (Map): Root CLAUDE.md.** Global folder structure, naming conventions, what's in each workspace, routing rules. "The floor plan on the wall."
- **Layer 2 (Rooms): Per-workspace context file.** Each workspace subdirectory (e.g., `writing_room/`, `production/`, `community/`) contains its own context markdown specifying purpose, what files to load for which tasks, what to skip, which skills/MCPs to invoke.
- **Layer 3 (Workspace): The actual files.** Drafts, scripts, outputs — organized by the conventions defined in Layer 1.

The agent reads Layer 1 always, descends into the relevant Layer 2 file when working in a workspace, and reads Layer 3 files only as needed. Eliminates the proliferation of separate domain-specific agents — Claude Code becomes the universal agent, behavior adapts via context files. Failure modes: CLAUDE.md proliferation, stale workspace context files, ambiguous routing in Layer 1.

### 8c: Global vs Project-Level Skill Scoping

Every skill, MCP, and CLAUDE.md should be scoped deliberately:

| Scope | Use For | Example |
|-------|---------|---------|
| **Global** (`~/.claude/`) | Universally useful skills | `/bootstrap`, `/truncate`, `/session-handoff` |
| **Project** (per-folder) | Role- or domain-specific skills | "Sebastian-refer" skill (relevant only in the EA context); database-migration skill (relevant only in the platform repo) |

Without strategic scoping, every skill loads into every session — recreating the flat-CLAUDE.md bloat problem at the skill layer. Scoping ensures each agent role only loads the capabilities it actually needs.

Failure modes: skills mistakenly added to global scope bloat every session; skills needed across multiple projects but scoped per-project create maintenance burden when the process changes and all copies must be updated. Audit which skills are loaded in a session — if you cannot list them quickly, you have lost scope discipline.

### 8d: Cross-Platform Context File Strategy

If you operate across multiple AI coding tools (Claude Code reads `CLAUDE.md`; GitHub Copilot reads `AGENTS.md`; Cursor reads `.cursorrules`), pick a portability strategy explicitly:

| Strategy | Mechanism | Pro | Con |
|----------|-----------|-----|-----|
| **Chain-loader indirection** | `CLAUDE.md` is a single line: `@AGENTS.md` (Claude Code follows the pointer; other tools read AGENTS.md directly) | Minimal duplication; one source of truth | `@` syntax is Claude Code-specific |
| **Platform-specific mirroring** | Maintain parallel `.claude/agents/`, `.github/agents/`, `.github/prompts/` — same specialists adapted per platform | Maximum fidelity per tool | Three copies drift over time |
| **Content duplication** | `CLAUDE.md` and `AGENTS.md` at root contain identical content | Simplest; works everywhere | Drift when one is updated and the other is not |

The chain-loader approach is the most elegant when Claude Code is one of your tools — n8n uses it across ~44 packages. Mirroring fits when each tool needs platform-specific adaptations. Duplication is pragmatic for very small files where drift cost is low.

Whatever you pick, add drift detection (a CI check that compares mirrored files) before the next "the agent is using outdated conventions" incident.

### 8e: Monorepo Context Distribution

In monorepos, "one CLAUDE.md for everything" stops scaling. Three observed strategies:

| Strategy | Pattern | Best For |
|----------|---------|----------|
| **Per-package chain-loaders** | Each package gets its own `CLAUDE.md` → `@AGENTS.md` pair (n8n: ~44 packages, frontend has CSS conventions, nodes-base has INodeType patterns, database has migration DSL rules) | Large monorepos with genuinely distinct package conventions |
| **Path-scoped rules** | `.claude/rules/*.md` files auto-load by directory (Archon: 11 rules covering orchestrator, workflows, isolation, adapters, database) | Mid-sized monorepos; auto-loading reduces per-package authoring burden |
| **Single global file** | One brief CLAUDE.md (~58 lines) at the monorepo root for all packages (LangGraph: 8 libraries) | Small monorepos where conventions are uniform across libraries |

Tradeoff: precision vs. authoring effort vs. simplicity. n8n maximizes precision at the cost of maintaining 44+ file pairs; Archon balances via auto-loading; LangGraph prioritizes simplicity by accepting that all packages share the same minimal context. Hybrid: a brief global CLAUDE.md with path-scoped overrides that inject additional rules for specific packages. Watch for stale rules that reference deleted/renamed packages.

### 8f: PROGRESS.md as a Session Bridge

Claude Code has limited native memory across sessions; a structured bridge file collapses cold-start time. PROGRESS.md is the canonical pattern (identified in 12 of 14 practitioner videos surveyed):

- **At session start:** the agent reads PROGRESS.md to orient.
- **At session end:** the agent writes an updated summary covering completed work, in-progress work, blocked items, and next steps.

Drift is the failure mode — agents write optimistic summaries that diverge from actual file state. Mitigate by either (a) verifying summaries against actual file state at session start, or (b) treating PROGRESS.md as a structured, append-only delta log rather than a rewritten summary (Step 5 defense #3 applies here too).

Two evolutions worth knowing:
- Anthropic's long-running scientific-computing workflow uses CHANGELOG.md as "lab notes" — failed approaches included ("tried Tsit5 for perturbation ODE; too stiff, switched to Kvaerno5"), accuracy tables at checkpoints, known limitations. This prevents re-attempting dead ends. Pairs well with PROGRESS.md (intent vs. narrative).
- Cloud-scheduled tasks running while the local machine is off cannot read a local PROGRESS.md. If you use cloud-scheduled agents, host the bridge file in the git repo or another cloud-accessible location.

For the deep treatment of memory architecture and persistence patterns (banks, write policy, retrieval pipelines), see G7: *Session Persistence and Memory*.

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
- [ ] Module manifests present for major code modules (where applicable)
- [ ] Behavioral contracts present on key interfaces (where applicable)

### Tiering Check
- [ ] Tier 0 contains only identity, safety, and hard rules (< 20 lines)
- [ ] Task-scoped instructions are in Tier 1, not Tier 0
- [ ] Reference material is in Tier 2 (on-demand), not loaded upfront
- [ ] Tool pool is dynamically assembled, not all-tools-always
- [ ] Skill pool uses progressive loading (descriptions at boot, full SKILL.md on-demand)

### Curation Check
- [ ] Each context element has a justifiable reason for being there
- [ ] Volatile content is not in cached/upfront files
- [ ] Sub-agents receive scoped context, not the full parent window
- [ ] Context enrichment present: purpose, audience, workflow position, criteria
- [ ] Retrieved content uses hybrid retrieval (not embeddings alone)
- [ ] Skills reference shared context via path, not embedded copies

### Architecture Check
- [ ] Vault tiered (global / shared / local) with deliberate scoping
- [ ] Skills and MCPs scoped global vs project deliberately
- [ ] Multi-tool projects have a portability strategy (chain-loader / mirror / duplicate)
- [ ] Monorepos have a context distribution strategy (per-package / path-scoped / global)
- [ ] Session bridge file (PROGRESS.md or equivalent) exists and is read at session start

### Rot Defense Check
- [ ] Explicit state object exists for long-running sessions
- [ ] Evolving documents use delta updates, not monolithic rewrites
- [ ] Context resets happen at natural workflow boundaries
- [ ] Output is validated against contracts at each step
- [ ] Cross-session learnings are persisted and injected
- [ ] Sessions bounded to single atomic issues where workload permits
- [ ] CLAUDE.md is never sent to Claude for self-compaction

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

### Module Manifest Template

For self-describing codebases (Step 2 — Self-Describing Codebases). Drop one of these into each significant module directory.

```markdown
# Module Manifest -- {{MODULE_PATH}}

## Purpose
{{ONE_SENTENCE_DESCRIPTION_OF_WHAT_THE_MODULE_DOES}}

## Dependencies In (this module needs)
- {{DEPENDENCY_1}}: {{WHY_NEEDED}}
- {{DEPENDENCY_2}}: {{WHY_NEEDED}}

## Dependencies Out (these depend on this module)
- {{CONSUMER_1}}: {{WHAT_THEY_CONSUME}}
- {{CONSUMER_2}}: {{WHAT_THEY_CONSUME}}

## Public Interfaces

### {{INTERFACE_NAME_1}}
- **Behavior:** {{HOW_IT_BEHAVES_NOT_JUST_DATA_SHAPE}}
- **Performance:** {{LATENCY_OR_THROUGHPUT_EXPECTATION}}
- **Failure modes:** {{WHAT_BREAKS_AND_HOW_IT_SURFACES}}
- **Retry semantics:** {{IDEMPOTENT_OR_NOT_AND_RETRY_GUIDANCE}}

### {{INTERFACE_NAME_2}}
- **Behavior:** ...
- **Performance:** ...
- **Failure modes:** ...
- **Retry semantics:** ...

## Constraints
- {{CONSTRAINT_THAT_CALLERS_MUST_RESPECT_1}}
- {{CONSTRAINT_THAT_CALLERS_MUST_RESPECT_2}}

## Owner
- {{OWNER_NAME_OR_TEAM}} -- responsible for keeping this manifest in sync with the code
```

### Worked Example: Module Manifest for the Improvement Loop's Researcher Agent

```markdown
# Module Manifest -- systems/improvement-loop/agents/researcher/

## Purpose
Stage 1 of the IL pipeline -- intake research sources (URLs, transcripts, repos), extract findings, and write them to research-findings/, research-sources/, research-authorities/.

## Dependencies In
- research-dimensions.md: filters what counts as in-scope research
- _schema.yaml: frontmatter contract for finding/source/authority files
- watched-libraries/, watched-blogs/: source registries for monitoring loops

## Dependencies Out
- agents/codifier/: consumes pipeline_status: classified findings as Stage 2 input
- agents/librarian/: reads the KB to answer queries (no write coupling)

## Public Interfaces

### /research-loop
- **Behavior:** Periodic research scan; produces a delta report and writes new finding/source/authority files. Idempotent on the same source set.
- **Performance:** ~1-2 minutes per source for Pass 1; Pass 2 (deep extraction) is per-source on demand.
- **Failure modes:** Network failures on Perplexity/WebFetch surface as partial reports; partial writes are detectable via missing pipeline_status frontmatter.
- **Retry semantics:** Re-running on the same source set is safe (duplicate detection by source URL).

### /perplexity-research
- **Behavior:** Discover or compare modes; produces a standalone report. Does not write to the KB by default.
- **Performance:** 30s+ per query; --discover mode invokes 3-5 Perplexity calls.
- **Failure modes:** Perplexity rate limits surface as report-level errors.
- **Retry semantics:** Idempotent; same prompt → similar but not byte-identical reports.

## Constraints
- WRITE access only to research-findings/, research-sources/, research-authorities/, watched-libraries/, watched-blogs/.
- READ-ONLY everywhere else (cannot write to extracts/, governance/, agents/).
- Must respect pipeline_status state machine: raw → classified is a Codifier transition, not a Researcher one.

## Owner
- IL Owner agent -- maintains this manifest under DD-86.
```

---

### Multi-Tool Context Mirror Map

For projects that span multiple AI coding tools. Pick a strategy (chain-loader / mirror / duplicate); the map records what lives where and how drift is detected.

```markdown
# Multi-Tool Context Map -- {{PROJECT_NAME}}

## Strategy
- [ ] Chain-loader indirection (CLAUDE.md → @AGENTS.md)
- [ ] Platform-specific mirroring (parallel files per tool)
- [ ] Content duplication (identical files at root)
- [ ] Hybrid: {{DESCRIBE_HYBRID}}

## File Map

| Tool | File | Source of Truth | Sync Mechanism |
|------|------|-----------------|----------------|
| Claude Code | {{PATH}} | {{IS_SOT_OR_DERIVED_FROM}} | {{HOW_KEPT_IN_SYNC}} |
| GitHub Copilot | {{PATH}} | {{IS_SOT_OR_DERIVED_FROM}} | {{HOW_KEPT_IN_SYNC}} |
| Cursor | {{PATH}} | {{IS_SOT_OR_DERIVED_FROM}} | {{HOW_KEPT_IN_SYNC}} |
| Codex | {{PATH}} | {{IS_SOT_OR_DERIVED_FROM}} | {{HOW_KEPT_IN_SYNC}} |

## Drift Detection
- [ ] CI check that compares mirrored files: {{COMMAND_OR_SCRIPT}}
- [ ] Last drift audit: {{DATE}}
- [ ] Drift incidents in last quarter: {{COUNT}}

## Tool-Specific Adaptations
| Tool | What Differs From SoT | Why |
|------|----------------------|-----|
| {{TOOL}} | {{DIFFERENCE}} | {{REASON}} |
```

### Worked Example: n8n-Style Chain-Loader

```markdown
# Multi-Tool Context Map -- n8n

## Strategy
- [x] Chain-loader indirection (CLAUDE.md → @AGENTS.md)

## File Map

| Tool | File | Source of Truth | Sync Mechanism |
|------|------|-----------------|----------------|
| Claude Code | CLAUDE.md (root + per-package) | Pointer to AGENTS.md | One-line file: `@AGENTS.md` |
| Claude Code (packages) | packages/*/CLAUDE.md | Pointer to packages/*/AGENTS.md | One-line per-package file |
| GitHub Copilot | AGENTS.md (root + per-package) | Yes (canonical) | N/A |
| Cursor | AGENTS.md (root + per-package) | Yes (same as Copilot) | N/A |

## Drift Detection
- [x] CI check that compares mirrored files: N/A — chain-loader has no mirroring
- [x] Last drift audit: 2026-04-09 (zero drift; chain-loader by construction)
- [x] Drift incidents in last quarter: 0

## Tool-Specific Adaptations
None. AGENTS.md is the single source of truth; CLAUDE.md is a one-line pointer.
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

### 12. Asking Claude to compact your own CLAUDE.md
Each LLM-driven compaction of a long-lived context file carries a small but cumulative probability of *catastrophic context collapse* — the playbook reduces to a sparse, inaccurate ~100-200 token summary, accuracy drops to ~57% of previous, often *below* having no CLAUDE.md at all. The failure mode is silent and persistent across sessions. Use ACE-style voting curation or `/clear` + handoff at natural break points; git-snapshot the CLAUDE.md before any compaction so rollback is one command.

### 13. Single global CLAUDE.md in a monorepo
"One file for the whole repo" stops scaling once packages have genuinely distinct conventions. The frontend agent loads database migration rules; the database agent loads CSS conventions. Pick a distribution strategy (per-package chain-loaders, path-scoped rules, or accept the global file's limitations and keep it minimal). Don't let it drift into a kitchen-sink doc.

### 14. Embedded copies of shared context across skills
Running 30+ skills that each embed their own copy of a shared ICP, brand voice, or audience persona means version drift the moment shared truth changes. Skills operate on different versions of the same underlying fact. Migrate to the pointer pattern: shared context lives in a second-brain folder, skills reference it by path. The migration is mechanical (identify duplication, move to vault, replace with path).

### 15. Multi-tool context file drift without enforcement
Maintaining `CLAUDE.md`, `AGENTS.md`, and `.cursorrules` as parallel files works until one is updated and the others aren't. By the time you notice, three tools are operating on three subtly different versions of project conventions. Either pick a chain-loader (one source of truth, others are pointers) or add a CI check that compares mirrored files. Don't rely on discipline.

---

## Related Guides

- **Tool definition tokens and deferred loading:** If tool definitions are a major context consumer, see *Designing Agent Tools* (G5) for dynamic tool pool assembly and deferred loading patterns.
- **Memory architecture and session persistence:** Cross-session persistence stores, memory tiers, retrieval pipelines, and the state object pattern are detailed in *Session Persistence and Memory* (G7). G2 covers the *window* — G7 covers what crosses session boundaries.
- **Context curation for measurement:** To measure whether removing a context element actually improves output, see *Building Agent Evaluation Suites* (G4) for eval-driven context optimization.
- **Multi-agent composition and scope:** Step 3f (curating context for downstream agents) and Step 5 defense #6 (atomic session scoping) intersect with single-vs-multi-agent decisions; see *Agent Architecture Decisions* (G3) for composition patterns.
- **Model-specific context sensitivity:** The model-specific findings (Step 4g, Pitfall #9) tie into prompt-engineering portability across model upgrades; see *Model-Resilient Prompt Engineering* (G8) for the prompt side of model-resilience.
- **Distributed boundary files for governance:** The AGENTS.md/CLAUDE.md placement at subsystem boundaries (Step 8 cross-platform portability + monorepo distribution) doubles as the governance-distribution layer — same files, two readers. See *Agent Governance and Trust* (G9), Section 4 Layer 4 (Distributed Governance Scope), for the rule-distribution discipline at the same locations: universal rules in the root file, subsystem-specific rules at the boundary, explicit inheritance semantics.

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
- Context architecture is explicit at all four layers: per-file, per-tier (vault), per-tool (cross-platform portability), and per-session (bridge file + scoping).
- CLAUDE.md (and other long-lived context files) are never compacted by Claude itself without git-snapshot rollback.
- Skills reference shared context via path, not embedded copies (when a second brain exists).

### Governance
- Context file owners audit their files against the signal-to-noise criteria in this guide at least once per milestone.
- The context budget worksheet is reviewed when agent performance degrades or costs spike unexpectedly.
- Context architecture changes (new upfront files, changed sharding boundaries, tier reassignments, scope changes for skills/MCPs, cross-platform mirror-strategy changes) are documented.
- Multi-tool projects run drift detection against mirrored files at the cadence of their CI pipeline, not "when someone notices."
- Model-specific context strategies are re-validated when the underlying model changes.
- Module manifests are owned by module owners and updated as part of any breaking-change PR for that module's interfaces.
- This guide is owned by the Improvement Loop and deployed to the Meta-System knowledge layer after review.

### Recovery
- If agent output quality degrades: run the context audit checklist first. Context bloat and rot are the most common root causes.
- If token costs spike: check for cache invalidation (any character change forces full-price re-read), context duplication, reasoning token amplification from unnecessary instructions, hidden IDE context injection, or upfront loading of content that should be JIT.
- If context rot is suspected: compare current agent state against the explicit state object or contract to detect drift. If no state object exists, the absence of one is the root cause.
- If a new model performs differently: re-run the context audit with model-specific sensitivity in mind. What worked for Codex may not work for Claude Code, and vice versa.
- If the agent is using outdated conventions in a multi-tool project: check whether mirrored context files have drifted; restore from the source of truth and add drift detection if it is missing.
- If CLAUDE.md was compacted and quality dropped: roll back to the pre-compaction git snapshot. If no snapshot exists, restore from the last good version in git history; the compacted file is a write-off.
- If a monorepo agent loads irrelevant package context: the global file has likely become a kitchen sink — split into per-package or path-scoped rules per Step 8e.
