# Delta Report — 2026-04-07

## Scan Summary

| Field | Value |
|-------|-------|
| **Trigger** | Ad hoc — user-provided URLs |
| **Dimensions covered** | Memory Architecture, Context Engineering, Orchestration, Tool Integration, Prompt Craft, Intent Engineering |
| **Sources reviewed** | 3 |
| **New findings added** | 18 |
| **Existing findings updated** | 0 (first run — no prior KB) |
| **Previous report** | First run |
| **Date** | 2026-04-07 |

---

## Sources Processed

| ID | Title | Channel | Date | Relevance | Tags |
|----|-------|---------|------|-----------|------|
| source-001 | [I Built Self-Evolving Claude Code Memory w/ Karpathy's LLM Knowledge Bases](https://www.youtube.com/watch?v=7huCP6RkcY4) | Cole Medin | 2026-04-06 | High | `memory`, `context-engineering`, `claude-code`, `vault-architecture`, `session-management` |
| source-002 | [I Broke Down Anthropic's $2.5 Billion Leak. Your Agent Is Missing 12 Critical Pieces.](https://www.youtube.com/watch?v=FtCdYhspm7w) | Nate B Jones | 2026-04-03 | High | `orchestration`, `tools`, `context-engineering`, `memory`, `claude-code`, `prompt-engineering`, `evaluation` |
| source-003 | [The Official BMad-Method Masterclass (The Complete IDE Workflow)](https://www.youtube.com/watch?v=LorEJPrALcg) | BMad Code | 2025-08-02 | High | `orchestration`, `context-engineering`, `prompt-engineering`, `multi-agent`, `skills`, `claude-code` |

---

## New Findings

| ID | Finding Name | Category | Evidence Strength | Proposer Priority | Applicability |
|----|-------------|----------|------------------|------------------|--------------|
| F-001 | LLM Knowledge Base Compiler Pattern (Karpathy) | Memory Architecture | Medium | P2 | Perplexity Skills, General |
| F-002 | Claude Code Hooks for Automatic Session Memory | Memory Architecture | Medium | **P1** | Perplexity Skills, S3 |
| F-003 | Index-File Navigation as RAG Replacement | Context Engineering | Medium | P2 | General, Perplexity Skills |
| F-004 | Compounding Knowledge Loop (Internal Data) | Memory Architecture | Medium | **P1** | S3, Perplexity Skills, General |
| F-005 | Tool Registry with Metadata-First Design | Tool Integration | **Strong** | **P1** | S2, S3, Perplexity Skills, General |
| F-006 | Tiered Permission System with Destructive-Command Safety | Tool Integration | **Strong** | **P1** | S3, Perplexity Skills, General |
| F-007 | Session Persistence as Recoverable State | Orchestration | **Strong** | **P1** | S2, S3, Perplexity Skills |
| F-008 | Workflow State vs. Conversation State Separation | Orchestration | **Strong** | **P1** | S2, S3, Perplexity Skills |
| F-009 | Token Budget Tracking with Pre-Turn Projection Checks | Orchestration | **Strong** | P2 | S2, S3, Perplexity Skills |
| F-010 | Structured Streaming Events for System Observability | Orchestration | **Strong** | P2 | S3, Perplexity Skills |
| F-011 | System Event Logging (Actions, Not Just Words) | Evaluation | **Strong** | **P1** | S2, S3, Perplexity Skills, General |
| F-012 | Agent Type System (Six Built-In Roles) | Orchestration | **Strong** | P2 | S2, S3, Perplexity Skills |
| F-013 | Dynamic Tool Pool Assembly + Transcript Compaction | Context Engineering | **Strong** | P2 | S3, Perplexity Skills |
| F-014 | Structured Multi-Agent Role Separation (BMad) | Orchestration | Medium | P2 | S3, Perplexity Skills, General |
| F-015 | Document Sharding for Context Efficiency | Context Engineering | Medium | **P1** | S3, Perplexity Skills, General |
| F-016 | Advanced Elicitation Techniques (18-Technique Library) | Prompt Craft | Medium | P2 | Perplexity Skills, S2, S3, General |
| F-017 | New-Chat-Per-Agent-Step as Context Hygiene Discipline | Context Engineering | Medium | P2 | S2, S3, Perplexity Skills |
| F-018 | Business Analyst as Upstream Quality Gate | Intent Engineering | Medium | P3 | S3, General |

---

## Updated Findings

None — first run.

---

## Already Captured

None — first run. Patterns that may overlap with existing practices:
- F-015 (Document Sharding) — partially adopted behavior in existing skills; needs formal implementation
- F-012 (Agent Type System) — partially reflected in existing Perplexity Skills role separation; not formalized

---

## P1 Findings Summary (Implement Now)

These 7 findings have actionable implementation paths and strong or medium evidence:

| ID | Finding | Why P1 | Quick Start |
|----|---------|--------|-------------|
| F-002 | Claude Code Hooks for Session Memory | Low effort, high leverage, live demo available | Clone https://github.com/coleam00/claude-memory-compiler, prompt Claude Code with gist |
| F-004 | Compounding Knowledge Loop | Follows from F-002; zero maintenance once running | Implement hooks first; flush runs automatically |
| F-005 | Tool Registry with Metadata-First Design | Production-proven at scale; enables F-013 as prerequisite | Audit current tool definitions; expose as data structure |
| F-006 | Tiered Permission System | Shell-access agents need this now; 18-module safety model | Start with pre-classification (read-only/mutating/destructive) |
| F-007 | Session Persistence as Recoverable State | Prevents long-running task loss on crash | Implement JSON session persistence; add `load/reconstruct/restore` |
| F-008 | Workflow State vs. Conversation State | Foundational for retry-safe long-running tasks | Define explicit workflow states; persist checkpoints |
| F-011 | System Event Logging | Easy to add now; expensive to retrofit | Add action-level logging alongside conversation logs |
| F-015 | Document Sharding | Directly applicable to over-large skill files | Audit Perplexity Skills for monolithic files; split into role-specific shards |

---

## Recommendations

### Priority 1 — High Impact, Low Effort

1. **Implement Claude Code Hooks for Session Memory (F-002 + F-004):** The repo is public, the setup is a one-shot prompt, and the payoff is immediate. Every S3 session that currently loses context becomes captured knowledge. Do this for the active Claude Code codebase first.

2. **Add System Event Logging (F-011):** Log what agents *do* at the action level (tool calls, routing decisions, permission grants) alongside conversation transcripts. This is foundational for debugging and auditing any agent system. Low engineering overhead; high diagnostic value.

3. **Audit and Shard Over-Large Skill Files (F-015):** Any Perplexity Skill that exceeds ~2,000 tokens in its system prompt is a candidate for sharding into role-specific sub-documents. Use the BMad shard pattern as a template.

### Priority 2 — High Impact, Higher Effort

4. **Workflow State Separation (F-008):** For any S2 or S3 agent that performs multi-step operations with external side effects (Notion writes, file edits, API calls), implement explicit workflow state tracking. This is a prerequisite for crash-resilient agents and safe retries.

5. **Tool Registry Refactor (F-005):** Move tool definitions to a metadata-first registry. This is a prerequisite for dynamic tool pool assembly (F-013) and enables runtime filtering by permission tier (F-006).

6. **Tiered Permission System (F-006):** Pre-classify all tools as read-only / mutating / destructive. Apply approval gates to destructive operations. Build the pre-approved patterns allowlist. Implement permission audit logging.

7. **Token Budget Pre-Turn Checks (F-009):** Add `max_tokens`, `max_turns`, and `compaction_threshold` configuration to agent runtimes. Implement pre-turn projection to stop before, not after, limit exceedance.

### Priority 3 — Monitor

8. **Advanced Elicitation Library (F-016):** The 18-technique YAML library from BMad is interesting for prompt-enhancer and prompt-evaluator integrations. Monitor for community adoption evidence before investing in a full implementation.

9. **BMad Full Workflow (F-014):** Consider adopting the Analyst → PM → Architect → Dev → QA pipeline for new S3 greenfield projects. Defer until a greenfield project justifies the setup cost.

10. **Business Analyst Agent (F-018):** Most relevant for new project starts. Monitor and apply selectively.

---

## Evaluation Handoff

**Prompts to evaluate next (for prompt-evaluator):**
- S3 Claude Code system prompt — evaluate against F-005 (tool registry), F-006 (permission tiers), F-008 (workflow state), F-011 (action logging)
- S2 Notion Operations agent prompt — evaluate against F-007 (session persistence), F-008 (workflow state), F-011 (action logging)
- Perplexity Skills (research-loop, research-proposer) — evaluate against F-015 (sharding), F-016 (elicitation techniques)

**Focus rubric areas:** Tool Integration, Orchestration, Context Engineering

---

## Authorities Added This Run

| ID | Name | Type | Credibility | Specialty |
|----|------|------|-------------|-----------|
| A-001 | Cole Medin | Individual | Tier 2 | memory, claude-code, vault-architecture |
| A-002 | Andrej Karpathy | Individual | Tier 1 | memory, context-engineering |
| A-003 | Nate B Jones | Individual | Tier 2 | orchestration, tools, claude-code |
| A-004 | Brian (BMad Code) | Individual | Tier 2 | orchestration, multi-agent, context-engineering |
| A-005 | Anthropic | Company | Tier 1 | claude-code, orchestration, tools |

---

## Next Scan Notes

**Patterns to watch:**
- Claude Code's full leaked source continues to circulate — additional practitioners will publish breakdowns. Watch for deeper analysis of the 18-module bash security architecture specifically.
- Karpathy's LLM KB pattern is spawning many derivative implementations. Watch for production-scale evidence of index-file navigation vs. RAG tradeoffs at larger corpus sizes.
- BMad-Method v4+ is actively evolving (npm package). Watch for updates to the agent type system and advanced elicitation YAML templates.
- Nate B Jones' agentic harness skill (Claude Code skill package + codec metadata) — download and evaluate against current S2/S3 prompts.

**Specific items to investigate next cycle:**
1. Retrieve and read Nate B Jones' agentic harness skill (linked in source-002 video description)
2. Review Claude Code's leaked source directly for additional primitives beyond the 12 covered in this analysis
3. Search for practitioner evidence on token budget pre-turn projection implementations — current evidence is architectural (leaked config) but no implementation guides were found
4. Search for production evidence of dynamic tool pool assembly at scale (currently inferred from Claude Code config; no practitioner walkthroughs found)
