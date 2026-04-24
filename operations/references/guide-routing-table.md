---
name: Guide Routing Table
description: >-
  Maps research dimensions to guide clusters and tracks unrouted findings.
  Read by /synthesize-guide at Step 0 and updated by /identify-artifacts
  when findings don't fit existing guide clusters. Living artifact — grows
  from evidence as new finding themes emerge.
type: "reference"
target_system:
  - "improvement-loop"
created: "2026-04-19"
updated: "2026-04-24"
source_dd:
  - "DD-81"
---

# Guide Routing Table

Maps research dimensions (intake) to guide clusters (output). Read by `/synthesize-guide` to resolve finding sets and by `/identify-artifacts` to flag findings that don't fit existing clusters.

**This table is a living artifact.** It grows as new findings reveal themes not covered by existing guides. Do not pre-create guides speculatively — let the unrouted bucket accumulate evidence first.

---

## Synthesis Status

Tracks when `/synthesize-guide` was last run against each cluster, how many findings were synthesized, and the output path. Read by `/synthesize-guide` (Step 0) and `/identify-artifacts` (Step 6) to assess coverage and staleness.

| ID | Guide Title | Last Synthesized | Findings at Synthesis | Output Path | Status |
|----|------------|-----------------|----------------------|-------------|--------|
| G1 | Writing Agent Specifications | 2026-04-19 | 7 | `extracts/guides/writing-agent-specifications.md` | draft |
| G2 | Managing Agent Context | 2026-04-19 | 26 | `extracts/guides/managing-agent-context.md` | draft |
| G3 | Agent Architecture Decisions | 2026-04-19 | 21 | `extracts/guides/agent-architecture-decisions.md` | draft |
| G3b | Agent Workflow and Execution | 2026-04-19 | 20 | `extracts/guides/agent-workflow-and-execution.md` | draft |
| G4 | Building Agent Evaluation Suites | 2026-04-19 | 30 | `extracts/guides/building-agent-evaluation-suites.md` | draft |
| G5 | Designing Agent Tools | 2026-04-19 | 14 | `extracts/guides/designing-agent-tools.md` | draft |
| G6 | Agent Safety and Permissions | 2026-04-19 | 5 | `extracts/guides/agent-safety-and-permissions.md` | draft |
| G7 | Session Persistence and Memory | 2026-04-19 | 14 | `extracts/guides/session-persistence-and-memory.md` | draft |
| G8 | Model-Resilient Prompt Engineering | 2026-04-19 | 15 | `extracts/guides/model-resilient-prompt-engineering.md` | draft |
| G9 | Agent Governance and Trust | 2026-04-19 | 10 | `extracts/guides/agent-governance-and-trust.md` | draft |
| G10 | Agent Design Patterns | 2026-04-19 | 11 | `extracts/guides/agent-design-patterns.md` | draft |

**Staleness indicator:** If a cluster's finding count (in the Guide Clusters table below) exceeds "Findings at Synthesis" by 3+, the guide should be re-synthesized to incorporate new material.

---

## Dimension → Guide Mapping

| Research Dimension | Primary Guide | Secondary Guide(s) | Notes |
|-------------------|--------------|-------------------|-------|
| Context Engineering | Managing Agent Context | Session Persistence and Memory | Largest dimension; may split further |
| Model | Model-Resilient Prompt Engineering | Agent Architecture Decisions | Model routing → Architecture; model prompting → Prompt Engineering |
| Prompt | Model-Resilient Prompt Engineering | — | Shares guide with Model; split when mass justifies it |
| Tools | Designing Agent Tools | — | Clean 1:1 mapping |
| Intent | Writing Agent Specifications | — | Clean 1:1 mapping |
| Orchestration | Agent Architecture Decisions | Agent Workflow and Execution, Session Persistence and Memory | Architecture gets topology/composition; Workflow gets execution/operations; Session gets state management |
| Evaluation | Building Agent Evaluation Suites | Agent Safety and Permissions | Safety inherits independent-eval findings |
| Sandboxing | Agent Safety and Permissions | — | Clean 1:1 mapping |
| Governance | Agent Governance and Trust | — | Graduated from unrouted; 10 findings (2 P1 + 8 P2) |
| Agent Design | Agent Design Patterns | Writing Agent Specs, Session Persistence | Graduated from scattered; 11 P2 findings |

---

## Guide Clusters

Each cluster defines a guide by the practitioner question it answers. The `stage` field maps to the practitioner lifecycle: Specify → Build → Verify → Secure → Operate.

### Active Clusters

Current per-cluster finding counts are not enumerated here — they drift per session and are better sourced by ripgrep on `category:` in `research-findings/*.md` at read time.

| ID | Guide Title | Question | Stage | Dimensions |
|----|------------|----------|-------|------------|
| G1 | Writing Agent Specifications | "How do I specify what my agent should do?" | specify | Intent, Context, Orchestration |
| G2 | Managing Agent Context | "My agent is losing context or burning tokens" | build | Context Engineering |
| G3 | Agent Architecture Decisions | "Should I use one agent or many? How do I compose?" | build | Orchestration, Model |
| G3b | Agent Workflow and Execution | "How do I run agents in production?" | operate | Orchestration |
| G4 | Building Agent Evaluation Suites | "How do I verify my agent actually works?" | verify | Evaluation |
| G5 | Designing Agent Tools | "How do I design tools for agents?" | build | Tools |
| G6 | Agent Safety and Permissions | "How do I make my agent system safe?" | secure | Sandboxing, Evaluation |
| G7 | Session Persistence and Memory | "How do I handle memory and session continuity?" | operate | Context, Orchestration, Memory Architecture |
| G8 | Model-Resilient Prompt Engineering | "How do I write prompts that survive model upgrades?" | build | Prompt, Model |
| G9 | Agent Governance and Trust | "How do I govern agent autonomy and maintain human oversight?" | secure | Governance |
| G10 | Agent Design Patterns | "How do I design an individual agent's identity and behavior?" | specify | Agent Design |

### Unrouted Bucket

Findings that don't map cleanly to any active guide cluster. Reviewed after each identification run.

| Finding | Category | Same-Problem Links | Notes |
|---------|----------|--------------------|-------|
| [[claude-code-daily-brief-multi-source-inbox-obsidian]] | Agentic Systems | → ai-managed-vault, → multi-agent-proportional-summarization | Agentic Systems — personal aggregation layer. Added 2026-04-20. |
| [[ai-managed-vault-separate-from-human-vault]] | Agentic Systems | → claude-code-daily-brief, → multi-agent-proportional-summarization, → open-brain (G7) | Agentic Systems — personal storage layer. Added 2026-04-20. |

**Graduation trigger:** When 5+ unrouted findings share `same-problem` relationships, they form a candidate cluster. Surface to Nick for guide creation approval.

**Emerging theme (below threshold):** "Agentic Systems" category — 2 pattern findings + 1 skill (multi-agent-proportional-summarization) form a 3-finding cluster describing components of a personal agentic system. Not yet at 5-finding threshold. Monitor next 2 research-loop runs for additional Agentic Systems findings before proposing G11.

**History:**
- 2 P1 Governance findings (review-bandwidth, review-obsolescence) graduated to G9 on 2026-04-19.
- 2 P2 Agentic Systems findings added 2026-04-20 (session 43 identification run) — first entries in this category (category previously named "Agentic OS"; renamed 2026-04-21 to reflect team/business scope).

---

## Routing Rules

### For `/identify-artifacts`

After classifying findings into forms, check each pattern-classified finding against this table:

1. Match the finding's `category` field to a research dimension.
2. Look up the dimension's primary guide in the mapping table above.
3. If a primary guide exists → the finding is **routed**. No action needed.
4. If the dimension maps to `*unrouted*` or `*scattered*` → add the finding to the Unrouted Bucket section of this table.
5. After each identification run, check: does the unrouted bucket contain 5+ findings with `same-problem` links? If yes, flag a candidate cluster in the identification report.

### For `/synthesize-guide`

When resolving a finding set:

1. Read this table to determine which findings belong to the requested guide cluster.
2. Use the Guide Clusters table to get the guide's dimensions, then query findings by those dimensions.
3. Check the Unrouted Bucket — any unrouted findings that share `same-problem` links with the current guide's findings should be offered as candidates for inclusion.

### For taxonomy evolution

- **New guide:** Requires 5+ related unrouted findings + Nick approval. Add to Active Clusters, remove from Unrouted Bucket, update the Dimension → Guide mapping.
- **Guide split:** When an active guide exceeds 20 findings or covers clearly separable practitioner tasks. Propose the split; Nick approves.
- **Guide merge:** When two guides have <3 findings each and address adjacent practitioner tasks. Propose the merge; Nick approves.
- **Dimension update:** If findings consistently categorize into a theme not covered by the 10 dimensions (e.g., "Memory/Persistence"), propose a new dimension or sub-dimension via `/research-loop` refinement.

---

## Lifecycle Stages

Secondary navigation axis. Agents can query by stage to get all relevant guides for their current phase of work.

| Stage | Guides | Practitioner Phase |
|-------|--------|-------------------|
| **specify** | G1 (Agent Specs), G10 (Agent Design) | Defining what the agent should do and how it behaves |
| **build** | G2 (Context), G3 (Architecture), G5 (Tools), G8 (Prompts) | Implementing the agent system |
| **verify** | G4 (Evaluation) | Checking correctness and reliability |
| **secure** | G6 (Safety), G9 (Governance) | Hardening permissions, boundaries, and oversight |
| **operate** | G3b (Workflow/Execution), G7 (Session/Memory) | Running in production, maintaining state |

---

## Trigger Keywords

For agent-driven guide discovery. An agent encountering these terms in a task description should consult the corresponding guide.

| Keywords | Guide |
|----------|-------|
| intent, objective, disposition, autonomy, stop rules, health metrics, agent spec | G1 |
| context window, token budget, context rot, CLAUDE.md, sharding, compaction | G2 |
| multi-agent, single agent, orchestration, delegation, subagent, planner-executor | G3 |
| eval, verification, assertion, grading, benchmark, pass rate, test suite | G4 |
| tool design, tool definition, MCP, tool registry, poka-yoke | G5 |
| permissions, sandbox, injection, safety, isolation, blast radius | G6 |
| session, memory, persistence, crash recovery, handoff, state management, memory tiers, write policy | G7 |
| prompt engineering, model-agnostic, model routing, reasoning model, constraints, elicitation, prompt versioning | G8 |
| governance, trust, autonomy, oversight, review process, audit trail, human-on-the-loop, trust calibration | G9 |
| agent identity, constitution, soul, prompt layers, agent lifecycle, behavioral patterns, clarification, self-improvement | G10 |
| workflow, execution, cost, degradation, stall detection, observability, tracing, sprint contract, durable workflow | G3b |
