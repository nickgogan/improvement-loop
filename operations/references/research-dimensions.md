---
name: Research Dimensions
description: Active query registry for the eleven research dimensions. Read by research-loop at scan start. Updated at scan end with query refinements.
last_updated: "2026-04-19"
---

# Research Dimensions

This file is the **active query source** for the research-loop skill. The skill reads it at Step 0 and proposes refinements at Step 6. Edit queries here to steer future scans — no need to touch the skill definition.

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

---

## Dimension 2: Model

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

## Dimension 3: Prompt

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

## Dimension 4: Tools

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

## Dimension 5: Intent (Meta-Dimension)

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

## Dimension 11: Agentic OS

**What to search for:**
- Personal knowledge management with AI agents (second brain, vault-as-OS)
- Obsidian + AI agent integration patterns (CLI, terminal plugins, graph views)
- Scheduled agent tasks for life/business operations (morning briefs, meeting transcript ingestion, analytics rollups)
- File-based personal OS architecture (folder structure, index files, CLAUDE.md as routing layer)
- Context infrastructure maturity models (chat → projects → skills → file access → second brain → business OS)
- Team context sharing and permission patterns (sync, relay plugins, access control)
- Experiment/ritual tracking with agent assistance
- Daily routine automation and habit-tracking workflows

**Web queries:**
- `AI agent personal OS second brain [current year]`
- `obsidian claude code knowledge management workflow [current year]`
- `agentic business OS scheduled tasks automation [current year]`
- `personal productivity AI agent operations [current year]`

**arXiv queries:**
- `personal knowledge management AI agent`
- `AI assistant daily workflow automation`
- `human AI collaborative knowledge system`
