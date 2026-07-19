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
updated: "2026-07-19"
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
| G1 | Writing Agent Specifications | 2026-07-13 | 21 | `extracts/guides/writing-agent-specifications.md` | draft |
| G2 | Managing Agent Context | 2026-05-25 | 64 | `archive/guides/managing-agent-context.md` | deprecated (archived) |
| G2a | Structuring and Loading Agent Context | 2026-07-16 | 61 | `extracts/guides/structuring-agent-context.md` | draft |
| G2b | Defending Against Context Degradation | 2026-07-13 | 37 | `extracts/guides/defending-agent-context.md` | draft |
| G3 | Agent Architecture Decisions | 2026-07-19 | 72 | `extracts/guides/agent-architecture-decisions.md` | draft |
| G3b | Agent Workflow and Execution | 2026-07-19 | 42 | `archive/guides/agent-workflow-and-execution.md` | deprecated (archived) |
| G3c | Production Agent Execution | 2026-07-19 | 27 | `extracts/guides/production-agent-execution.md` | draft |
| G3d | Autonomous and Scheduled Agent Operation | 2026-07-19 | 20 | `extracts/guides/autonomous-scheduled-agent-operation.md` | draft |
| G4 | Building Agent Evaluation Suites | 2026-07-19 | 77 | `archive/guides/building-agent-evaluation-suites.md` | deprecated (archived) |
| G4a | Verifying Agent Output | 2026-07-19 | 63 | `extracts/guides/verifying-agent-output.md` | draft |
| G4b | Eval-Driven Improvement Loops | 2026-07-19 | 17 | `extracts/guides/eval-driven-improvement-loops.md` | draft |
| G5 | Designing Agent Tools | 2026-07-16 | 37 | `extracts/guides/designing-agent-tools.md` | draft |
| G6 | Agent Safety and Permissions | 2026-07-16 | 16 | `extracts/guides/agent-safety-and-permissions.md` | draft |
| G7 | Session Persistence and Memory | 2026-07-19 | 40 | `extracts/guides/session-persistence-and-memory.md` | draft |
| G8 | Model-Resilient Prompt Engineering | 2026-07-16 | 37 | `extracts/guides/model-resilient-prompt-engineering.md` | draft |
| G9 | Agent Governance and Trust | 2026-07-16 | 58 | `extracts/guides/agent-governance-and-trust.md` | draft |
| G10 | Agent Design Patterns | 2026-07-19 | 47 | `extracts/guides/agent-design-patterns.md` | draft |
| G11 | Building Agentic Systems | 2026-07-19 | 39 | `extracts/guides/building-agentic-systems.md` | draft |

**Staleness indicator:** If a cluster's finding count (in the Guide Clusters table below) exceeds "Findings at Synthesis" by 3+, the guide should be re-synthesized to incorporate new material.

---

## Dimension → Guide Mapping

| Research Dimension | Primary Guide | Secondary Guide(s) | Notes |
|-------------------|--------------|-------------------|-------|
| Context Engineering | Structuring and Loading Agent Context (G2a), Defending Against Context Degradation (G2b) | Session Persistence and Memory | Split from G2 in session 104; G2a covers structuring/loading/retrieval, G2b covers rot prevention/cost control/session discipline |
| Model | Model-Resilient Prompt Engineering | Agent Architecture Decisions | Model routing → Architecture; model prompting → Prompt Engineering |
| Prompt | Model-Resilient Prompt Engineering | — | Shares guide with Model; split when mass justifies it |
| Tools | Designing Agent Tools | — | Clean 1:1 mapping |
| Intent | Writing Agent Specifications | — | Clean 1:1 mapping |
| Orchestration | Agent Architecture Decisions | Production Agent Execution (G3c), Autonomous and Scheduled Agent Operation (G3d), Session Persistence and Memory | Architecture gets topology/composition; G3c gets supervised execution/operations; G3d gets unattended/scheduled/autonomous operation; Session gets state management. G3b (Agent Workflow and Execution) split into G3c+G3d, session 152, DD-122 |
| Evaluation | Verifying Agent Output (G4a), Eval-Driven Improvement Loops (G4b) | Agent Safety and Permissions | Split from G4 in session 152 (DD-123); G4a covers verification architecture (prove output works), G4b covers eval-driven improvement (make agent/skills better). Safety inherits independent-eval findings — secondary stays pointed at G4a. G4b is a future secondary for Tools (eval-driven tool iteration) — note only; no Tools-row change until demand shows. |
| Sandboxing | Agent Safety and Permissions | — | Clean 1:1 mapping |
| Governance | Agent Governance and Trust | — | Graduated from unrouted; 10 findings (2 P1 + 8 P2) |
| Agent Design | Agent Design Patterns | Writing Agent Specs, Session Persistence | Graduated from scattered; 11 P2 findings |
| Agentic Systems | Building Agentic Systems | Session Persistence and Memory, Orchestration | Graduated 2026-04-27 from emerging-theme; 29 findings post-IB-153 rebalance |

---

## Guide Clusters

Each cluster defines a guide by the practitioner question it answers. The `stage` field maps to the practitioner lifecycle: Specify → Build → Verify → Secure → Operate.

### Active Clusters

Current per-cluster finding counts are not enumerated here — they drift per session and are better sourced by ripgrep on `category:` in `research-findings/*.md` at read time.

| ID | Guide Title | Question | Stage | Dimensions |
|----|------------|----------|-------|------------|
| G1 | Writing Agent Specifications | "How do I specify what my agent should do?" | specify | Intent Engineering, Context Engineering, Orchestration |
| G2 | ~~Managing Agent Context~~ | ~~"My agent is losing context or burning tokens"~~ | ~~build~~ | ~~Context Engineering~~ | *(deprecated — split into G2a + G2b, session 104)* |
| G2a | Structuring and Loading Agent Context | "How do I structure and load context efficiently — what to include, how to tier it, and how to retrieve it?" | build | Context Engineering |
| G2b | Defending Against Context Degradation | "How do I prevent context degradation, rot, and cost blowout?" | build | Context Engineering |
| G3 | Agent Architecture Decisions | "Should I use one agent or many? How do I compose?" | build | Orchestration, Model Selection |
| G3b | ~~Agent Workflow and Execution~~ | ~~"How do I run agents in production?"~~ | ~~operate~~ | ~~Orchestration~~ | *(deprecated — split into G3c + G3d, session 152, DD-122)* |
| G3c | Production Agent Execution | "How do I make production agent workflows reliable, observable, and reviewable?" | operate | Orchestration |
| G3d | Autonomous and Scheduled Agent Operation | "How do I run agents unattended — scheduled, headless, and autonomous?" | operate | Orchestration |
| G4 | ~~Building Agent Evaluation Suites~~ | ~~"How do I verify my agent actually works?"~~ | ~~verify~~ | ~~Evaluation~~ | *(deprecated — split into G4a + G4b, session 152, DD-123)* |
| G4a | Verifying Agent Output | "How do I verify my agent's output actually works?" | verify | Evaluation |
| G4b | Eval-Driven Improvement Loops | "How do I use evals to drive autonomous improvement of my agent and its skills?" | verify/operate | Evaluation |
| G5 | Designing Agent Tools | "How do I design tools for agents?" | build | Tool Integration |
| G6 | Agent Safety and Permissions | "How do I make my agent system safe?" | secure | Sandboxing, Evaluation |
| G7 | Session Persistence and Memory | "How do I handle memory and session continuity?" | operate | Context Engineering, Orchestration |
| G8 | Model-Resilient Prompt Engineering | "How do I write prompts that survive model upgrades?" | build | Prompt Craft, Model Selection |
| G9 | Agent Governance and Trust | "How do I govern agent autonomy and maintain human oversight?" | secure | Governance |
| G10 | Agent Design Patterns | "How do I design an individual agent's identity and behavior?" | specify | Agent Design |
| G11 | Building Agentic Systems | "How do I build a personal/team/business agentic system on top of a knowledge store?" | specify | Agentic Systems |

### Unrouted Bucket

Findings that don't map cleanly to any active guide cluster. Reviewed after each identification run.

| Finding | Category | Same-Problem Links | Notes |
|---------|----------|--------------------|-------|
| _(empty)_ | | | |

**Graduation trigger:** When 5+ unrouted findings share `same-problem` relationships, they form a candidate cluster. Surface to Nick for guide creation approval.

**History:**
- 2 P1 Governance findings (review-bandwidth, review-obsolescence) graduated to G9 on 2026-04-19.
- 2 P2 Agentic Systems findings added 2026-04-20 (session 43 identification run) — first entries in this category (category previously named "Agentic OS"; renamed 2026-04-21 to reflect team/business scope).
- Agentic Systems theme graduated to G11 (Building Agentic Systems) on 2026-04-27 (session 82) — 29 findings post-IB-153 dimension rebalance, 5.8× over the 5-finding threshold.

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
| **specify** | G1 (Agent Specs), G10 (Agent Design), G11 (Agentic Systems) | Defining what the agent or system should do and how it behaves |
| **build** | G2a (Context Structuring), G2b (Context Defense), G3 (Architecture), G5 (Tools), G8 (Prompts) | Implementing the agent system |
| **verify** | G4a (Verifying Agent Output), G4b (Eval-Driven Improvement Loops) | Checking correctness and reliability; driving eval-based improvement |
| **secure** | G6 (Safety), G9 (Governance) | Hardening permissions, boundaries, and oversight |
| **operate** | G3c (Production Agent Execution), G3d (Autonomous and Scheduled Agent Operation), G4b (Eval-Driven Improvement Loops), G7 (Session/Memory) | Running in production, maintaining state |

---

## Trigger Keywords

For agent-driven guide discovery. An agent encountering these terms in a task description should consult the corresponding guide.

| Keywords | Guide |
|----------|-------|
| intent, objective, disposition, autonomy, stop rules, health metrics, agent spec | G1 |
| context window, token budget, CLAUDE.md, sharding, tiered loading, retrieval, pointers, progressive loading | G2a |
| context rot, compaction, degradation, session discipline, cost control, token tax, session atomicity | G2b |
| multi-agent, single agent, orchestration, delegation, subagent, planner-executor | G3 |
| eval, verification, assertion, grading, benchmark, pass rate, test suite, deploy gate | G4a |
| eval-driven improvement, keep/revert, convergence, skill lifecycle, with/without baseline, skill smells, description optimization | G4b |
| tool design, tool definition, MCP, tool registry, poka-yoke | G5 |
| permissions, sandbox, injection, safety, isolation, blast radius | G6 |
| session, memory, persistence, crash recovery, handoff, state management, memory tiers, write policy | G7 |
| prompt engineering, model-agnostic, model routing, reasoning model, constraints, elicitation, prompt versioning | G8 |
| governance, trust, autonomy, oversight, review process, audit trail, human-on-the-loop, trust calibration | G9 |
| agent identity, constitution, soul, prompt layers, agent lifecycle, behavioral patterns, clarification, self-improvement | G10 |
| workflow, execution, cost, degradation, stall detection, observability, tracing, sprint contract, quality-at-source, durable workflow | G3c |
| scheduled, headless, cron, trigger shape, routine, loop contract, autonomous, unattended, reconciliation queue, durable workflow | G3d |
| vault-as-OS, second brain, personal knowledge management, daily brief, scheduled agent, file-over-app, agentic OS, knowledge store, Obsidian, vault, PKM, context infrastructure | G11 |

---

## Disambiguation Notes

Operational risks where the routing structure is functional but weakened.

**G2a/G2b vs G7 (post-split).** G2a (Structuring and Loading Agent Context), G2b (Defending Against Context Degradation), and G7 (Session Persistence and Memory) all carry `Context Engineering` in their Dimensions field. The G2→G2a/G2b split (session 104) sharpens the discriminator: G2a = what to include and how to load it (build-time structuring); G2b = how to prevent degradation over a session (runtime defense); G7 = how to persist state across sessions (operational persistence). The `bounded-tiered-memory-inference-driven-curation` finding is shared between G2a and G2b, with G7 cross-reference for its eviction/persistence aspect. If a future `/identify-artifacts` run mis-routes between G2a/G2b/G7, consult the trigger-keyword table above and the practitioner question text as discriminators.

**G3c vs G3d (post-split, session 152, DD-122).** G3b (Agent Workflow and Execution) split into G3c (Production Agent Execution) and G3d (Autonomous and Scheduled Agent Operation); both carry `Orchestration`, stage `operate`. Discriminator: G3c = harden a *supervised* production workflow (plan/execute separation, workflow state, per-run observability, cost, degradation, review bandwidth, routing); G3d = remove the human from the loop (scheduling surfaces, trigger shapes, headless composition, loop contracts, portfolio observability, autonomy levels). Five findings are deliberately shared across both `source_findings[]` — `durable-workflow-engine-for-agent-systems`, `durable-checkpointed-sessions-as-framework-default`, `archon-yaml-defined-harness-workflows`, `agent-cost-blowup-mitigation-strategies`, `graceful-degradation-modes-for-agent-failure` (the execution/failure substrate common to both regimes; `durable workflow` keyword routes to both). New Orchestration operate-stage findings route to G3c/G3d, never the deprecated G3b.

**`lint-test-failures-as-remediation-prompts` cross-dimension provenance.** This finding carries `category: Context Engineering`, not Orchestration. It was Nick-routed into the G3b cluster (session 152) as a quality-at-source authoring standard, and on the split it stays with **G3c** (supervised execution's Step 8 review-bandwidth material). If a future `/identify-artifacts` or `/dimension-rebalance` run reconsiders it against Context Engineering (G2a/G2b), the Nick-ruled routing to G3c takes precedence unless Nick re-rules.

**G4a vs G4b (post-split, session 152, DD-123).** G4 (Building Agent Evaluation Suites) split into G4a (Verifying Agent Output) and G4b (Eval-Driven Improvement Loops); both carry `Evaluation`. G4a is stage `verify`; G4b spans `verify` and `operate`. Discriminator: G4a = prove the agent's output works (assertions, reliability metrics, verification architectures — builder-validator/dual-blind/holdout/goal-backward/cross-model/fleet review, benchmark and config discipline, production evaluation, quality gates incl. evals-as-deploy-gate); G4b = use those evals to improve the agent and its skills over time (keep/revert loops, convergence contracts, skill lifecycle evaluation, description optimization, with/without baselines, eval-driven tool iteration, review-feedback→durable-checks). Three findings are deliberately shared across both `source_findings[]` — `capability-vs-regression-eval-lifecycle`, `generator-assessor-separation-in-skill-iteration`, `eval-rubric-carve-outs-subjective-and-script-core-skills` (the lifecycle/separation/carve-out invariants both questions stand on). New Evaluation findings route to G4a/G4b, never the deprecated G4.
