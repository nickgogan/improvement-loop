---
title: "Agent Governance and Trust"
type: "guideline"
category: "Governance"
target_system:
  - "cross-system"
stage: "draft"
created: "2026-04-19"
updated: "2026-05-25"
author: "claude"
source_findings:
  - "review-bandwidth-as-organizational-bottleneck"
  - "review-obsolescence-as-design-goal"
  - "behavioral-context-portability-intelligence-lock-in"
  - "governance-memory-append-only-audit-layer"
  - "compound-review-debt-from-deferred-inspection"
  - "reviewer-skill-elevation-for-agentic-output"
  - "tool-gateway-security-boundary"
  - "human-on-the-loop-hotl-autonomy-tiering-framework"
  - "trust-calibration-progressive-autonomy-ramp"
  - "agent-identity-governance-enforcement-layer"
  - "dark-code-organizational-capability-problem"
  - "distributed-boundary-guides"
  - "middleware-as-enforcement-architecture"
  - "per-node-tool-restrictions-workflow-governance"
  - "specification-as-governance-fourth-enforcement-philosophy"
  - "three-enforcement-pipeline-architectures"
  - "actor-passport-schema-bound-identity"
  - "agent-action-reversibility-as-design-requirement"
  - "capability-restricted-agent-spawning-via-allowlist"
  - "context-warrant-justified-data-package"
  - "cross-system-permission-composition-audit-gap"
  - "dri-rotation-pattern-time-bounded-sensemaking-ownership"
  - "foreground-vs-background-subagent-permission-models"
  - "governance-ontology-semantic-foundation"
  - "governed-dependency-chain-build-order"
  - "interpretive-boundary-layer-fact-vs-judgment"
  - "management-unbundling-routing-sensemaking-accountability"
  - "passport-object-decision-governance-binding"
  - "pattern-scale-signals-systemic-not-individual-failure"
  - "permission-compounding-across-agent-delegation-chains"
  - "policy-as-data-machine-readable-constraints"
  - "policy-as-data-runtime-governance-pattern"
  - "runtime-governance-gap-buildtime-to-production"
  - "runtime-threshold-management-truth-conditions"
  - "subagent-scope-priority-ladder"
  - "supervision-debt-anti-pattern"
  - "tool-access-as-security-boundary-not-feature-toggle"
  - "tool-model-io-contracts-with-preconditions"
source_dd:
  - "DD-81"
tags:
  - "guide"
  - "governance"
  - "trust"
  - "autonomy"
  - "enforcement-architecture"
  - "permissions"
  - "auditability"
  - "runtime-governance"
contract:
  preconditions: "Agent system with human oversight requirements; governance model needed; an enforcement architecture is chosen (rules, hooks, middleware, or specification) before policies are written; permission model defined for multi-agent delegation if applicable"
  invariants: "Human retains override authority; audit trail maintained; enforcement-architecture choice is explicit and matches system complexity; rule scope is locality-aware (universal rules central, local rules at the boundary); permissions narrow monotonically across delegation chains; every agent action is traceable to an identity and a governing policy version"
  governance: "IL-owned draft; Nick deploys to meta-system/knowledge/guides/"
  recovery: "If trust violations detected, demote agent to lower autonomy tier; if enforcement bypass detected, audit the architecture choice before adjusting policy; if permission compound detected, audit the delegation chain and apply monotonic narrowing; if audit gap found, freeze autonomous operations until the trail is restored"
---

# Agent Governance and Trust

How to govern agent autonomy and maintain human oversight as agent output scales beyond human review capacity. This guide addresses the central tension of agentic systems: agents produce at 100x speed, humans review at 3x speed, and the gap between those numbers is where governance either holds or collapses.

The guide covers seven concerns: defining autonomy tiers so agents act within calibrated boundaries, evolving review processes so oversight scales with output, building governance infrastructure so policies are enforced rather than aspirational, managing agent identity so oversight is traceable and portable, making governance machine-readable and enforceable at runtime, managing permissions across agent delegation chains, and tracing agent decisions for auditability.

## When to Use This Guide

- You are deploying agents that make decisions with varying blast radius and reversibility
- Your review queue grows faster than you can drain it
- You need to decide which agent actions require approval vs. monitoring vs. full autonomy
- You want to reduce review burden without abandoning human oversight
- You need an audit trail that answers "why did the agent do that?"
- You are concerned about behavioral context lock-in with a specific AI provider
- You are choosing between rule-based, hook-based, middleware-based, or specification-based enforcement
- AI-generated code is shipping faster than humans can read and understand it
- Your governance rules have outgrown a single root file and need to scope to subsystems
- You are building multi-agent systems where agents delegate to other agents and permissions compound
- You need governance rules that are enforced at runtime, not just documented at build time
- You want every agent decision to carry its own proof of authorization
- Your agents cross multiple backend systems and you need composed audit trails
- You are shipping agents to production without a control layer and accumulating supervision debt

## Key Concepts

**1. Autonomy is a gradient, not a switch.** Binary models (approve everything vs. approve nothing) fail. Approve-everything creates risk; approve-nothing creates a bottleneck indistinguishable from not having an agent. The correct model is a four-level gradient -- full autonomy, guarded, proposal-first, human-required -- assigned per decision type based on blast radius and reversibility, and refinable per decision point within a workflow.

**2. Review is the binding constraint, not production.** The investment that determines agentic ROI is review infrastructure, not agent tooling. An agent that produces 100 artifacts per day into a queue that drains at 10 per day accumulates liability, not value. Design the pipeline to match review bandwidth, not production capacity.

**3. Every review comment is a system design signal.** The purpose of catching an issue in review is not to fix that instance but to eliminate the entire class of issue from future review. Each review comment that recurs is evidence that the system allows a preventable error. The reviewer's goal is to make their own review obsolete for mechanical categories.

**4. Governance policies without enforcement infrastructure are aspirational.** HITL checkpoints, autonomy tiers, and trust ramps only work if backed by identity-aware orchestration, tool gateways, and append-only audit logs. Without enforcement, agents can act before approval is obtained.

**5. Trust is earned per task type, not granted globally.** An agent trusted to write documentation is not automatically trusted to modify infrastructure. Trust calibration tracks success rates per task type and promotes autonomy incrementally. Regression (model updates, scope changes) can invalidate previously earned trust.

**6. Comprehension is upstream of review.** Review exists because someone has to understand what was produced before it ships. When agents generate code that no human reads, the review step does not become unnecessary -- it becomes structurally impossible. Review obsolescence achieved by automation eliminates mechanical review categories; review obsolescence achieved by skipping comprehension creates "dark code" that passes tests but is owned by no one. Restoring comprehension is the upstream fix; throughput improvements are downstream.

**7. Enforcement is architectured, not just policy.** Two systems can declare identical autonomy tiers, identical trust ramps, and identical audit requirements, yet deliver opposite levels of safety -- because one enforces via static rules at invocation time, the other intercepts every tool call through ordered middleware. The enforcement architecture (rules / hooks / middleware / specification) is itself a design decision with its own tradeoffs in coverage, ordering, latency, and debuggability. Policy without architecture is aspirational; architecture without policy is mechanism without intent.

**8. Governance must be machine-readable and runtime-enforceable.** Prose policies ("agents should not access PII without authorization") are aspirational. Machine-readable policies are enforced -- the runtime checks them and blocks non-compliant events. The gap between build-time governance and production execution is where most agentic systems fail: rules designed at build time are validated at deployment, then left behind as agents execute continuously.

**9. Permissions compound unpredictably across delegation chains.** When Agent A delegates to Agent B, the effective permissions are the compound of A's delegation scope, B's own capabilities, and the target system's access model. This compound is rarely designed explicitly -- it emerges at runtime from the intersection of independently-designed permission systems. Each delegation step must narrow permissions, never expand them.

**10. Every agent decision must carry its own proof of authorization.** Standard telemetry records what happened but not what rule governed the decision. The rule existed in a repository; it did not travel with the event. For governance to be provable rather than aspirational, the governing policy version, permits, evidence, and authority must be fused with the action at execution time.

**11. Reversibility determines governance intensity.** Every agent action sits on a reversibility spectrum. Fully reversible actions (read-only, draft generation) need minimal gating. Practically irreversible actions (sent communications, triggered payments) require human approval. The reversibility classification must account for actual infrastructure, not theoretical possibility of reversal.

**12. Pattern-scale failure signals systemic, not individual problems.** When governance failures appear at scale (11% of endpoints, not 1 of 200), the root cause is organizational and structural. The correct diagnostic is "what process keeps producing this pattern?" and the correct mitigation is architectural defaults, not training.

---

## Section 1: Define Autonomy Tiers

### Decision: What oversight model fits your system?

Use the HOTL (Human-on-the-Loop) framework to classify every agent-driven process by two dimensions: complexity and stakes.

**HITL vs. HOTL distinction:**
- **HITL (Human-in-the-Loop):** Human approves before every action. The agent cannot proceed without a command at each stage. This is the bottleneck model.
- **HOTL (Human-on-the-Loop):** Agent operates autonomously within guardrails. Human monitors and can intervene. Intelligence shifts from interface prompting to infrastructure-embedded decision-making.

Most production systems need both models applied to different decision types -- HITL for high-stakes irreversible actions, HOTL for routine operations within defined boundaries.

### Decision Tree: Assigning Autonomy Levels

For each decision type the agent handles, classify by blast radius and reversibility:

```
                    Is the decision easily reversible?
                         /                \
                       YES                 NO
                      /                     \
            Low blast radius?          Low blast radius?
              /        \                 /        \
            YES         NO             YES         NO
             |           |              |           |
        FULL AUTONOMY  GUARDED    PROPOSAL-FIRST  HUMAN-REQUIRED
        Agent acts.    Agent acts,  Agent proposes, Agent cannot act.
        No report.     then reports. waits for      Must escalate.
                                     approval.
```

**Autonomy level definitions:**

| Level | Agent Behavior | Human Behavior | When to Use |
|-------|---------------|----------------|-------------|
| Full Autonomy | Acts without notification | None unless auditing | Log entries, formatting, index updates |
| Guarded | Acts, then reports what it did | Reviews reports, intervenes if needed | Refactoring within a module, config changes with rollback |
| Proposal-First | Proposes action, waits for approval | Reviews proposal, approves/rejects | Cross-system changes, new Design Decisions, API changes |
| Human-Required | Cannot act, must escalate | Makes the decision directly | Schema migrations, production deploys, data deletion |

### Reversibility-Aware Classification

The autonomy decision tree classifies by blast radius and reversibility in the abstract. In practice, reversibility depends on actual infrastructure:

| Reversibility Category | Examples | Required Gate | Infrastructure Dependency |
|------------------------|----------|---------------|---------------------------|
| Fully reversible | Read-only queries, draft generation, local file edits with VCS | Minimal (Full Autonomy) | Version control, local state |
| Reversible with effort | Database writes with backup, config changes with audit trail | Pre-action confirmation or post-action review window | Backup system, tested restore procedure |
| Practically irreversible | Sent communications, triggered payments, published content | Human approval required | No reliable undo mechanism |
| Irreversible | Legal commitments, regulatory filings, physical-world actions | Must not be delegatable to agents | N/A |

A database write is reversible if there is a backup and a tested restore procedure. The same write is irreversible if there is no backup. Classify against actual infrastructure, not theoretical possibility.

### Algorithmic Guardrails

For HOTL-tier decisions (full autonomy and guarded), define boundaries with explicit thresholds rather than procedures:

- "The agent may create new research findings autonomously, provided the finding file does not exceed 200 lines and does not modify existing findings."
- "The agent may commit to a feature branch autonomously. Commits to main require approval."
- "The agent may allocate budget between marketing channels, provided the shift does not exceed $5,000 per day."

Each guardrail answers three questions at the veto point: What action am I taking? Why is this the optimal path? What is the projected impact?

### Per-Decision-Point Granularity

Tier-by-decision-type is the right model when the agent operates as a single contiguous loop. Multi-step workflows complicate the picture: a research node and a code-modification node within the same workflow have fundamentally different trust profiles, even if both run under one autonomy level globally.

**Refine tiers down to the decision point.** Within a workflow, each node can carry its own tool allowlist or denylist. A planning node gets read-only access. A classification node gets `tools: []` to prevent tool use during routing decisions. An implementation node gets full access. The orchestration engine enforces the per-step restriction; the agent cannot widen its own access.

Per-step restrictions express least-privilege as workflow configuration rather than agent disposition. The unit of trust narrows from "the agent" to "this step of this workflow."

```yaml
# Per-step tool restriction (workflow YAML)
nodes:
  - name: classify_issue
    model: small-fast
    tools: []                     # routing decision; no tools allowed
  - name: research_solution
    tools: [Read, Grep, WebFetch] # read-only
    denied_tools: [Write, Edit, Bash]
  - name: implement_fix
    tools: [Read, Edit, Write, Bash] # full access; gated behind earlier nodes
  - name: verify
    tools: [Read, Bash]           # tests + reads only
```

**When to reach for per-step granularity:**
- The workflow has steps with materially different blast radii (planning vs. execution).
- A compromised or misbehaving node would otherwise have access to every tool any node in the workflow uses.
- Tool restrictions need to be edited by workflow authors without modifying the execution engine.

**When not to:**
- The workflow is short (<=2 steps) or every step has similar trust profile.
- Tool restrictions become so finely sliced that a single legitimate action requires whitelisting across many nodes.

### Supervision Debt: Identify Control Points Before Deployment

Teams that wire models to tools without identifying control points accumulate supervision debt: they ship agents, discover what agents are actually doing in production, then retroactively bolt on approval buttons, audit logs, and cancel mechanisms as symptomatic fixes.

The root issue is not the missing UI elements but the failure to identify control points upfront. A control point is a moment where a human needs to observe, approve, edit, deny, or cancel agent work. Map every agent workflow to explicit control points before deployment:

1. **Observation points:** Where must the human see agent state and progress?
2. **Approval points:** Which actions require pre-execution human sign-off?
3. **Steering points:** Where can the human correct course mid-task?
4. **Cancel points:** Where can the human interrupt and roll back?

Uniform gating (gate everything equally) is safer than no gating but is its own form of debt -- excessive approval friction that masks which operations genuinely need human oversight. The correct investment is classifying operations by actual risk tier: auto-approve (read-only), human-approve (mutations), human-initiate (irreversible).

---

## Section 2: Calibrate Trust Progressively

Static autonomy assignments waste human attention on proven-safe tasks and may under-gate novel risks. A progressive trust ramp adjusts autonomy levels based on demonstrated track record.

### The Trust Ramp

Trust calibration follows three rules:

1. **Start restrictive.** Every new task type begins at proposal-first or human-required. No task type starts at full autonomy.
2. **Promote per task type.** An agent that demonstrates reliability on documentation tasks earns autonomy for documentation only -- not for infrastructure changes.
3. **Track and threshold.** Define a concrete promotion criterion (e.g., 20 consecutive successful executions) and a demotion trigger (e.g., any failure that reaches production).

### Decision: When to Promote

```
Has the agent completed {{THRESHOLD}} consecutive successful 
executions of this task type without human correction?
    /          \
  YES           NO
   |             |
   v             v
Promote one     Keep current
level up.       level.
   |
   v
Has the system scope changed or the model been updated 
since the last trust assessment?
    /          \
  YES           NO
   |             |
   v             v
Reset to       Maintain
proposal-first. promoted level.
```

### Trust Ledger Template

Use this to track per-task-type trust state:

```markdown
## Trust Ledger — {{SYSTEM_NAME}}

### Task Type: {{TASK_TYPE}}
- Current autonomy level: {{FULL_AUTONOMY / GUARDED / PROPOSAL_FIRST / HUMAN_REQUIRED}}
- Consecutive successes: {{COUNT}}
- Last failure: {{DATE or NEVER}}
- Failure description: {{DESCRIPTION or N/A}}
- Promotion threshold: {{N}} consecutive successes
- Demotion trigger: {{CONDITION}}
- Last trust assessment: {{DATE}}
- Model version at assessment: {{MODEL_VERSION}}

### Task Type: {{TASK_TYPE_2}}
...
```

### Worked Example: MetaSystem Research Pipeline Trust Ledger

```markdown
## Trust Ledger — MetaSystem Improvement Loop

### Task Type: Research Finding Extraction
- Current autonomy level: GUARDED
- Consecutive successes: 34
- Last failure: 2026-03-15
- Failure description: Duplicate finding created for existing KB entry
- Promotion threshold: 20 consecutive successes
- Demotion trigger: Any finding that requires deletion after review
- Last trust assessment: 2026-04-12
- Model version at assessment: Claude Opus 4 (200K)

### Task Type: Design Decision Creation
- Current autonomy level: HUMAN_REQUIRED
- Consecutive successes: N/A (always human-required)
- Promotion threshold: N/A — permanently human-required per DD-29
- Demotion trigger: N/A
- Last trust assessment: 2026-04-12
- Model version at assessment: Claude Opus 4 (200K)

### Task Type: Source Triage
- Current autonomy level: FULL_AUTONOMY
- Consecutive successes: 47
- Last failure: NEVER
- Promotion threshold: 20 (met)
- Demotion trigger: Any source mis-triaged as skip that later proves high-value
- Last trust assessment: 2026-04-19
- Model version at assessment: Claude Opus 4.6 (1M)
```

---

## Section 3: Scale Review Without Sacrificing Quality

### The Review Bottleneck

Agents produce at ~100x human speed. Human reviewers can scale to ~3x their normal rate. This 100x/3x asymmetry means unreviewed output accumulates as liability. Three strategies address this:

**Strategy 1: Triage before review.** Sort agent output into review tiers:

| Tier | Criteria | Review Approach |
|------|----------|----------------|
| Auto-approvable | Tests pass, schema validates, linting clean | Spot-check only |
| Standard review | Well-scoped single artifact, requires judgment | Full human review |
| Deep review | Architectural, cross-system, governance | Priority human attention |

**Strategy 2: Batch to review rhythm.** Do not let agents produce continuously while the review queue grows. Run agents in batches sized to reviewer capacity. Produce a batch, review it, produce the next. This prevents backlog accumulation and compound review debt.

**Strategy 3: Eliminate review categories.** For every recurring review comment, ask: "How do I make this comment impossible in the future?" Build the check (linter, schema constraint, CI rule) and eliminate the category permanently. This is the constructive response to the bottleneck -- shrink the volume of reviewable material.

### Compound Review Debt

Skipping review on agent-produced work creates compound debt. Each unreviewed change embeds assumptions that subsequent changes build upon. Reviewing a chain of 10 unreviewed commits costs far more than reviewing each individually, because the reviewer must untangle cascading dependencies.

**Policy: Set a maximum unreviewed depth.** No more than {{MAX_UNREVIEWED_DEPTH}} changes should accumulate before a review gate triggers, regardless of phase boundaries.

### Reviewer Skill Elevation

Reviewing AI-generated output requires different skills than producing it:
- Pattern recognition across large diffs (not line-by-line correctness)
- Architecture-level reasoning about generated patterns
- Detecting subtle errors in superficially correct output

Senior engineers are more valuable as reviewers than as producers in agentic workflows. Invest in review scaffolding: structured diffs, summary-first presentation, comparison views against prior approved artifacts, and per-task-type review checklists.

### The Comprehension Problem

Review exists because someone has to understand what was produced before it ships. The strategies above shrink the volume of reviewable material and elevate the skill applied to what remains -- but they assume the prerequisite, comprehension, is intact. When agents generate code at velocity and humans never read it, that prerequisite quietly fails.

**Dark code** is AI-generated code that passed automated checks and shipped, but was never understood by any human at any point. It is not buggy code, spaghetti code, or technical debt. It is code where the comprehension step simply did not happen -- because the development process no longer required it. Observability tells you what dark code is breaking in production. Better pipelines add more layers to troubleshoot when dark code fails. Neither restores comprehension.

The root cause is structural: AI generating code creates a structural barrier to understanding (you did not write it), and AI-enabled velocity creates pressure not to pause and understand. When those combine without countermeasures, comprehension decouples from authorship.

The three-layer response:

**Layer 1 -- Spec-driven development.** Force understanding before the code exists. Write the spec out -- not a 16-artifact waterfall process, just enough to articulate what you want to build in a degree of detail you can write down. The spec then doubles as the eval: a clearly written spec is the test against which the agent can iterate autonomously. (See [G1 -- Writing Agent Specifications].)

**Layer 2 -- Self-describing systems.** Make comprehension embedded in the codebase rather than locked in individuals' heads. Structural context (module manifests: what does this do, what does it depend on, what depends on it). Semantic context (behavioral contracts on interfaces: performance expectations, failure modes, retry semantics -- not just the shape of the data).

**Layer 3 -- Comprehension gates at review.** An AI-assisted filter at PR review that asks senior-engineer-style questions as code is reviewed: why was this dependency called here? How is caching structured in relation to other services? What are the separation-of-concerns implications? The gate makes architectural questions immediately legible rather than requiring the reviewer to surface them from scratch. Output from comprehension gate checks feeds back into evals -- creating a flywheel that improves code quality and review quality simultaneously.

The relationship between comprehension and review obsolescence: review obsolescence achieved by *automating mechanical categories* is the goal of the previous sub-section. Review obsolescence achieved by *skipping comprehension* is dark code. Both reduce review volume; only the first reduces review necessity.

### The Interpretive Boundary Layer

Agent outputs that reach human decision-makers must be explicitly classified into two categories:

- **"Act on this"** -- factual, verified, low-risk. Status rollups, dependency flags, metrics that crossed thresholds with clear historical precedent. The system is operating within its competence.
- **"Interpret this first"** -- judgment calls the system is not equipped to make reliably. Trends that might be noise. Correlations that might not be causal. Prioritizations that might reflect model bias.

Presenting both at the same confidence level is an architectural failure that silently degrades decision quality. Once a team begins treating system output the way they treat a director's analysis, the damage is slow: a degradation of decision quality that looks like bad luck rather than "the system was making editorial choices it was never equipped to make."

This is distinct from a confidence score. It is a binary classification of output type: factual versus inferential. The boundary is never perfect, but it must be explicitly drawn.

### Scaling Oversight as an Organizational Function

The human oversight function bundles three distinct sub-functions:

1. **Routing** (AI-automatable): aggregating signal up from agents and distributing directives down. Synthesizing status, cascading policy changes, monitoring agent output. This is a solved problem for AI.
2. **Sensemaking** (partially automatable, human-dominant): distinguishing signal from noise. Translating strategy into agent direction. Surfacing meaningful patterns from ground-level data upward. Requires domain context AI cannot replicate reliably.
3. **Accountability** (human-essential): ownership of outcomes over time. The multi-year attachment a product manager develops toward a domain. Feedback delivery that is timed, contextual, developmentally appropriate.

Flattening oversight (removing human review layers) without explicitly reassigning all three functions produces drift. The DRI rotation pattern addresses this: name a responsible individual per agent domain for a bounded term (e.g., 90 days) with explicit authority to interpret signals, set priority, and make direction calls. Time-bounding prevents territory accumulation; rotation builds cross-domain fluency.

### Systemic Failure Diagnosis

When governance failures appear at pattern-scale (affecting a significant percentage of a system's surface), the correct diagnostic is not "who forgot to follow the checklist?" but "what process keeps producing this pattern?"

**Diagnostic process:**
1. Count the instances. A single violation is plausibly individual error. Multiple violations (3+) are a pattern.
2. Identify the process that produces the pattern. "Why wasn't there a default that would have captured this?"
3. Trace the organizational root cause. Technical defaults are set by organizational priorities.
4. Target the mitigation at the process. Training fixes individual errors. Architectural defaults fix systematic patterns.

If the failure is at pattern-scale, training is the wrong mitigation. Architectural defaults that apply automatically to every action are the correct response.

### Review Process Template

```markdown
## Review Process — {{SYSTEM_NAME}}

### Review Tiers
| Output Type | Review Tier | Max Unreviewed Depth | Reviewer |
|-------------|-------------|---------------------|----------|
| {{OUTPUT_TYPE}} | {{AUTO / STANDARD / DEEP}} | {{N}} | {{ROLE}} |

### Review Obsolescence Tracking
| Review Comment Category | Frequency | Automatable? | Prevention Mechanism | Status |
|------------------------|-----------|-------------|---------------------|--------|
| {{CATEGORY}} | {{HIGH/MED/LOW}} | {{YES/NO/PARTIAL}} | {{MECHANISM}} | {{ACTIVE/PLANNED/N_A}} |

### Comprehension Coverage
| Component / Surface | Self-Describing? | Spec on File? | Comprehension Gate Active? |
|---------------------|------------------|---------------|---------------------------|
| {{COMPONENT}} | {{YES/NO/PARTIAL}} | {{YES/NO}} | {{YES/NO}} |

### Interpretive Boundary
| Output Type | Classification | Confidence Basis |
|-------------|---------------|------------------|
| {{OUTPUT}} | {{ACT_ON_THIS / INTERPRET_FIRST}} | {{BASIS}} |

### Batch Configuration
- Batch size: {{N}} artifacts per review cycle
- Review cadence: {{SCHEDULE}}
- Backlog threshold (pause production): {{N}} unreviewed items

### Oversight Function Assignment
| Function | Owner | Term | Authority |
|----------|-------|------|-----------|
| Routing | {{AGENT_OR_ROLE}} | Ongoing | N/A (automated) |
| Sensemaking | {{DRI_NAME}} | {{TERM_LENGTH}} | {{AUTHORITY_SCOPE}} |
| Accountability | {{ROLE}} | Ongoing | {{AUTHORITY_SCOPE}} |

### Quality Metrics
- Downstream failure rate of approved artifacts: {{RATE}}
- Review depth indicator: {{METRIC}}
- Approval rate (target < 90%): {{RATE}}
```

### Worked Example: MetaSystem Research Pipeline Review Process

```markdown
## Review Process — Improvement Loop Pipeline

### Review Tiers
| Output Type | Review Tier | Max Unreviewed Depth | Reviewer |
|-------------|-------------|---------------------|----------|
| Research findings | STANDARD | 10 | Nick |
| Source triage verdicts | AUTO | 25 | Nick (spot-check) |
| Identification reports | STANDARD | 1 | Nick |
| Extracted artifacts | DEEP | 3 | Nick |
| Guide drafts | DEEP | 1 | Nick |
| Design Decisions | DEEP | 1 | Nick |

### Review Obsolescence Tracking
| Review Comment Category | Frequency | Automatable? | Prevention Mechanism | Status |
|------------------------|-----------|-------------|---------------------|--------|
| Missing frontmatter fields | HIGH | YES | YAML schema validator | PLANNED |
| Duplicate findings | MED | YES | Dedup check in research-loop | ACTIVE |
| Broken cross-links | MED | YES | linkage-repair skill | ACTIVE |
| Architectural judgment | LOW | NO | N/A | N/A |

### Comprehension Coverage
| Component / Surface | Self-Describing? | Spec on File? | Comprehension Gate Active? |
|---------------------|------------------|---------------|---------------------------|
| /synthesize-guide skill | YES (SKILL.md procedure) | YES (DD-93/94/98/101) | NO |
| Codifier agent | YES (agent.md) | PARTIAL | NO |
| Research findings KB | PARTIAL (frontmatter) | NO | NO |

### Interpretive Boundary
| Output Type | Classification | Confidence Basis |
|-------------|---------------|------------------|
| Finding extraction | ACT_ON_THIS | Schema-validated, source-linked |
| Priority assessment | INTERPRET_FIRST | LLM judgment, requires Nick gate |
| Split proposal recommendation | INTERPRET_FIRST | Codifier judgment, heuristic |

### Batch Configuration
- Batch size: 15 findings per review cycle
- Review cadence: End of each research session
- Backlog threshold: 30 unreviewed findings triggers pipeline pause

### Oversight Function Assignment
| Function | Owner | Term | Authority |
|----------|-------|------|-----------|
| Routing | Researcher agent | Ongoing | Automated pipeline |
| Sensemaking | Nick | Ongoing | All architectural decisions |
| Accountability | Nick | Ongoing | System-wide |

### Quality Metrics
- Downstream failure rate: Not yet tracked
- Approval rate: ~85% (within target)
```

---

## Section 4: Build Governance Infrastructure

Autonomy tiers and review processes are policy. Without enforcement infrastructure, they are aspirational. This section starts with the meta-decision -- which enforcement architecture to use -- then walks the infrastructure layers that an architecture-of-choice instantiates.

### Choose an Enforcement Architecture

Two systems can declare identical policies and deliver opposite levels of safety. The difference is the enforcement architecture: where in the request/response flow checks fire, what they can intercept, and how composable they are.

**Three runtime architectures form a sophistication spectrum:**

| Architecture | Where it fires | Power | Complexity | When it fits |
|--------------|---------------|-------|------------|--------------|
| **Rule-based allowlists** | At invocation time | Static (cannot intercept ongoing execution) | Simplest | Static constraints, small agents, the system is fully controllable, ordering does not matter |
| **Event-driven hooks** | On specific lifecycle events (PostToolUse, PreCompact, SessionStart) | Per-event (validate, modify, block) | Moderate. No guaranteed ordering between hooks. | Agent harnesses with discrete lifecycle events; behavioral validation per event |
| **Request-pipeline middleware** | On every tool call and model response, in declared order | Per-interaction (intercept all I/O) | Highest. 12-layer pipelines are real. | Complex agent harnesses with cross-cutting concerns (sandbox lifecycle, summarization, subagent limiting, loop detection) |

**Specification-based enforcement is a fourth, complementary philosophy.** The first three are runtime architectures (where checks execute). Specification-based enforcement encodes governance as executable contracts that compliance is *verified against* rather than instructed to follow:

- A conformance test suite that any implementation must pass (the interface owns the tests, not the implementation -- inverts the typical relationship).
- Spec-driven development where specs are living artifacts kept bidirectionally in sync with code -- read spec -> implement -> verify alignment -> update spec or code.
- Compliance is *verified*, not *instructed*. A conformance test either passes or fails -- there is no "rationalize past the test suite."

This pairs with the runtime architectures: specification-based for *what* compliance means, rules/hooks/middleware for *what runs* when an action is attempted.

**Decision: which architecture(s) to adopt?**

```
Is the agent a single contiguous loop with a small action set?
    /          \
  YES           NO
   |             |
   v             v
Rules suffice.  Does the agent have discrete lifecycle events
                that need interception (compaction, session start,
                tool call boundaries)?
                /          \
              YES            NO
               |              |
               v              v
        Add hooks for     Are there cross-cutting concerns
        those events.     (sandbox, summarization, subagent caps,
                           loop detection) that span tool calls?
                          /          \
                        YES            NO
                         |              |
                         v              v
                  Promote to       Hooks alone suffice.
                  request-pipeline
                  middleware (12-layer
                  pipelines are real).
```

**Pair runtime architecture with specification-based enforcement** when interface contracts matter (multiple implementations of one interface; cross-system invariants; spec-as-eval pattern). Pair without specification when policies are local to one implementation and unlikely to need verification by an external party.

**Cost of architecture choice (read this before reaching for middleware):**
- Rules: zero per-request overhead; zero ordering complexity; cannot intercept ongoing behavior.
- Hooks: per-event overhead; ordering is loose (interaction effects between hooks are hard to predict).
- Middleware: per-request latency on *every* tool call and model response; ordering is strict and powerful but creates subtle bugs when layers interact; debugging through 12 layers requires good observability up-front.
- Specification: maintenance burden -- specs that drift from reality become governance theater.

The architecture choice is not "more is better." Reach for the simplest layer that meets the policy enforcement need; promote when the simpler layer cannot intercept what you need to enforce.

### Layer 1: Append-Only Governance Memory

An immutable audit log that answers "why did the agent do that?" -- distinct from debug logs, with different retention, access controls, and purpose.

**What to capture:**
- Prompts and system instructions (versioned)
- Retrieved items (what was injected into context, and from where)
- Actions taken (tool calls, writes, approvals)
- Outputs produced
- Memory/policy versions used

**Design properties:**
- Not in the hot path (no impact on agent response latency)
- Append-only retention (immutable logs with versioning)
- Separate from debug/operational logs
- Queryable for post-incident analysis and drift detection

### Layer 2: Tool Gateway

A centralized gateway through which all agent tool calls are routed. Provides allowlist validation, scoped credentials, parameter validation, rate limiting, audit logging, and sandboxing.

Without a gateway, each tool manages its own security -- creating an inconsistent, unauditable attack surface. The gateway transforms agents from security liabilities into systems that can be governed, monitored, and audited.

**Tool access is a security boundary, not a feature toggle.** MCP tool enablement in most UIs looks like a feature toggle (enable/disable server), but it is actually a security boundary crossing. MCP was designed for high-trust environments and does not enforce access control at the protocol level. Enabling a tool grants the agent arbitrary code execution and arbitrary data access within that tool's scope. Required mitigations when crossing the boundary:
1. **Scopes:** Which tools can the agent see in which context?
2. **Approval flows:** Which operations require human confirmation?
3. **Audit trails:** What tools were called, with what parameters, producing what results?
4. **Context-sensitive visibility:** Do not expose tools irrelevant to the current task.

**Credential isolation pattern:** Sensitive credentials (git credentials, signing keys, API tokens) stay outside the agent's sandbox entirely. A credential proxy handles authentication; the agent never sees real tokens.

### Layer 3: Identity-Aware Orchestration

The technical enforcement mechanism for HITL checkpoints. Without identity infrastructure, HITL policies cannot be enforced -- agents can act before approval is obtained.

**Key components:**
- **JIT identity provisioning:** Purpose-bound, time-limited identities for ephemeral agents. No pre-provisioned static accounts. Every action is traceable to an identity record tied to a specific task and human delegator.
- **Time-boxed decision lanes:** Match approval SLA to risk level -- 15s for low-risk, 2m for PII, 15m for financial. If approval times out, fail-safe to denied.
- **Challenge-and-response approvals:** Replace "Approve?" with a structured checklist: intent, data lineage, permissions chain, expected blast radius, rollback plan.
- **Two-factor judgment:** On critical actions, require independent human review or counter-model sanity check before execution.

### Layer 4: Distributed Governance Scope

A monolithic governance file (one large rules document at the project root) scales poorly. As a system grows, the root file accumulates rules for every subsystem, and agents working in any part of the system must process all of them. This wastes context budget and increases the chance of rule conflicts -- two subsystems may have contradictory local rules that the global file does not reconcile.

**Distribute governance scope to match the boundaries it constrains.** Place a governance file at each major subsystem boundary. The root file carries only universal rules. Subsystem files add local constraints: import restrictions, public contract definitions, testing requirements, and boundary rules specific to that area.

This creates progressive disclosure: an agent working in `src/plugins/` loads root rules plus plugins-specific rules, without being burdened by gateway-specific constraints irrelevant to its current scope.

**Multi-tool compatibility via the symlink pattern.** When more than one AI tool reads governance from differently-named files (e.g., one expects `CLAUDE.md`, another expects `AGENTS.md`), the canonical file is one of them and the others are symlinks to it. Single source of truth, multiple access paths. The symlink approach avoids file duplication and the drift it would create.

```
project/
├── AGENTS.md                # ~300 lines; universal rules
├── CLAUDE.md → AGENTS.md    # symlink for Claude Code
├── extensions/
│   ├── AGENTS.md            # extensions-specific rules
│   └── CLAUDE.md → AGENTS.md
├── src/
│   ├── channels/
│   │   ├── AGENTS.md        # channels-specific rules
│   │   └── CLAUDE.md → AGENTS.md
│   ├── plugins/
│   │   ├── AGENTS.md        # plugins-specific rules
│   │   └── CLAUDE.md → AGENTS.md
│   └── gateway/
│       ├── AGENTS.md        # gateway-specific rules
│       └── CLAUDE.md → AGENTS.md
```

**Scope priority ladder.** When definitions or rules share the same name across multiple scopes, resolution follows a deterministic priority order: organization-managed (highest) > CLI-session > project > user > plugin (lowest). Higher priority wins with no merging. This ensures organization admins can enforce defaults that developers cannot override, while plugins remain guest-citizens whose contributions are overridable by any higher scope.

**Inheritance semantics must be explicit.** Without explicit override rules, it is unclear whether a subsystem rule supplements or replaces a root rule. Default heuristic: subsystem rules add to root rules; conflicts fail the load with a structured error. Override-by-default semantics are dangerous unless the system has well-tested cascade rules.

**When to reach for distributed scope:**
- The system has 3+ subsystems with materially different governance needs.
- The root governance file exceeds ~300 lines or accumulates rules irrelevant to most agent loops.
- Multiple AI tools read governance from differently-named files.

**When not to:**
- Single-subsystem project; rules fit comfortably in one file.
- Rule granularity is finer than subsystem boundaries (use a tagged-rule system instead).
- File system layout does not cleanly map to governance boundaries (use dynamic context assembly instead).

---

## Section 5: Make Governance Machine-Readable

Prose governance ("agents should not access PII without authorization") is aspirational. Machine-readable governance is enforceable. This section covers how to transform policy from documentation into runtime-enforced constraints.

### The Runtime Governance Gap

Traditional compliance tools (policy-as-code, infrastructure-as-code, CI/CD gates) were engineered for a world where systems are built, deployed, and then remain still until the next patch. The deployment gate is the enforcement point. Everything downstream is assumed to be static.

Agents contradict this assumption. When an agentic workload is deployed, it wakes up. Decision nodes fire continuously. The agent allocates resources, routes work, triggers APIs, and spends money between deployments -- it is never still. Oversight that only covers the deployment gate covers only a single moment in a system that never stops acting.

As agents execute, they move progressively further from the original deployment gate. The farther they travel, the larger the gap between "what the agent was authorized to do at deployment" and "what rules are actually governing current decisions." In a multi-agent system, this gap translates to thousands of autonomous actions per hour under potentially outdated, misaligned, or unchecked parameters.

**Diagnostic test:** For any single active decision happening right now, can you name the rule that governs it? The version? The evidence evaluated? The approving authority? If answering those questions requires a log search, a Slack thread, or a developer -- runtime governance does not exist.

### Policy as Data Architecture

Instead of prose documentation, represent governance rules as machine-readable data structures that the runtime evaluates against every event.

**Three categories of policy rules:**
1. **Boundary rules** -- what the system is and is not permitted to do (scope constraints)
2. **Authority rules** -- who is permitted to trigger which events (access constraints)
3. **Data handling rules** -- how data may be accessed, retained, and shared (compliance constraints)

**Runtime binding pattern:** Governance rules are decoupled from application code and stored as independent, version-controlled policy bundles. Each bundle specifies permits granted, denials enforced, obligations that must fire, and specific evidence required before execution is allowed. At runtime, agents query a policy service and bind to a specific bundle version before executing an action.

**Instant update path:** Policy changes are made by promoting a new bundle version. Every agent in scope binds to the new logic instantly, with no pipeline redeployment required. This closes the update-lag failure mode: emergency policy changes take effect at agent speed rather than deployment-pipeline speed.

### The Governed Build Order

Machine-readable governance requires a dependency-ordered construction sequence. Each layer depends on the artifacts of the layer below it:

| Step | Layer | What It Defines |
|------|-------|----------------|
| 1 | Ontology + Semantic Model | Core domain nouns; disambiguation rules |
| 2 | Event Schema | Noun-verb mappings; mandatory fields; state implications |
| 3 | Policy as Data | Boundary, authority, data-handling rules (machine-readable) |
| 4 | Actor Model + Passport Schema | Actor classes; role bindings; authority ceilings; trust markers |
| 5 | Context Warrant | Justified minimum-necessary data assembly; freshness enforcement |
| 6 | Protocol + State Machines | Allowed action sequences; transition rules; timeouts |
| 7 | Tool and Model IO Contracts | External effect boundaries; preconditions; rate limits; idempotency |
| 8 | Provenance + Audit/Replay | Action lineage; policy traces; decision logic; replay capability |
| 9 | Threshold Management | Live signal monitoring; escalation and containment triggers |
| 10 | Truth Conditions Framework | Three-level verification: semantic, procedural, historical |
| 11 | Capability Contracts | Runtime engines with no independent logic; derive authority from chain |

**The dependency chain narrative:** Meaning dictates events. Events are filtered by policy. Policy governs actors. Actors wield context. Context navigates state. State triggers effects. Effects generate proof. Proof is verified by runtime controls. Runtime is operationalized by capability contracts.

**The atomic rule:** One artifact serves exactly one concern. Mixing semantic definitions with runtime thresholds -- or any other cross-layer contamination -- breaks system integrity. This prevents category drift: the failure mode where control, history, trust, and state collapse into an unmanageable blob.

Not every system needs all 11 layers. The correct question is: what is the minimum required depth for your risk profile? A simple single-agent tool with low blast radius may need only layers 1-4. A regulated multi-agent system processing financial transactions needs all 11.

### Runtime Threshold Management

Beyond static preconditions, runtime thresholds respond to live conditions as a "pressure valve" that escalates or contains behaviors:

- **Volume signals:** Is the system processing more events than expected?
- **Error rate signals:** Are failures accumulating?
- **Authority signals:** Is an actor approaching its authority ceiling?
- **Temporal signals:** Has the system been in a state longer than permitted?

When a threshold is crossed, the system either escalates (notifies a human or higher-level orchestrator) or contains (pauses, limits, or terminates the behavior).

**Truth conditions verification** checks whether an action is valid across three independent dimensions:
1. **Semantically correct** -- does the action conform to the ontology and event schema?
2. **Procedurally sound** -- is the action permitted given the current state machine position, actor passport, and policy layer?
3. **Historically accurate** -- is the action consistent with the provenance trail? Does it reference events and states that actually occurred?

Validating all three simultaneously prevents actions that satisfy observable governance checks while relying on fabricated historical context.

### Machine-Readable Governance Template

```markdown
## Machine-Readable Governance — {{SYSTEM_NAME}}

### Ontology
- Core nouns: {{LIST_OF_CANONICAL_DOMAIN_TYPES}}
- Disambiguation rules: {{SEMANTIC_MODEL_LOCATION}}
- Versioning: {{ONTOLOGY_VERSION_SCHEME}}

### Policy Bundle Configuration
- Bundle format: {{JSON_SCHEMA / YAML / OPA_REGO / CEDAR / CUSTOM}}
- Bundle location: {{PATH_OR_SERVICE}}
- Bundle versioning: {{SEMVER / SEQUENTIAL / HASH}}
- Update path: {{PROMOTION_LIFECYCLE: draft → review → active → deprecated}}
- Binding mechanism: {{QUERY_AT_RUNTIME / EMBED_AT_DEPLOY / HYBRID}}

### Policy Categories
| Category | Rule Count | Enforcement Point | Update Frequency |
|----------|-----------|-------------------|-----------------|
| Boundary rules | {{N}} | {{WHERE}} | {{CADENCE}} |
| Authority rules | {{N}} | {{WHERE}} | {{CADENCE}} |
| Data handling rules | {{N}} | {{WHERE}} | {{CADENCE}} |

### Runtime Thresholds
| Signal | Threshold | Escalation Action | Containment Action |
|--------|-----------|-------------------|-------------------|
| {{SIGNAL_TYPE}} | {{VALUE}} | {{ESCALATE_TO}} | {{CONTAIN_HOW}} |

### Truth Conditions
- Semantic validation: {{ENABLED / DISABLED}} — checks against layers 1-2
- Procedural validation: {{ENABLED / DISABLED}} — checks against layers 3-6
- Historical validation: {{ENABLED / DISABLED}} — checks against layer 8

### Build Order Compliance
| Layer | Status | Artifact Location |
|-------|--------|------------------|
| Ontology | {{COMPLETE / PARTIAL / MISSING}} | {{PATH}} |
| Event Schema | {{COMPLETE / PARTIAL / MISSING}} | {{PATH}} |
| Policy as Data | {{COMPLETE / PARTIAL / MISSING}} | {{PATH}} |
| Actor Model | {{COMPLETE / PARTIAL / MISSING}} | {{PATH}} |
| Context Warrant | {{COMPLETE / PARTIAL / MISSING}} | {{PATH}} |
| State Machines | {{COMPLETE / PARTIAL / MISSING}} | {{PATH}} |
| IO Contracts | {{COMPLETE / PARTIAL / MISSING}} | {{PATH}} |
| Provenance | {{COMPLETE / PARTIAL / MISSING}} | {{PATH}} |
| Thresholds | {{COMPLETE / PARTIAL / MISSING}} | {{PATH}} |
| Truth Conditions | {{COMPLETE / PARTIAL / MISSING}} | {{PATH}} |
| Capability Contracts | {{COMPLETE / PARTIAL / MISSING}} | {{PATH}} |
```

---

## Section 6: Manage Permissions Across Delegation Chains

When agents delegate to other agents, permissions compound in ways that no single agent's access scope predicts. This section covers how to govern the permission surface that emerges when agents compose.

### Permission Compounding Problem

When Agent A delegates to Agent B, B's effective permissions are the compound of A's delegation scope, B's own capabilities, and the target system's access model. Three compounding patterns:

1. **Inheritance:** Agent B inherits Agent A's credentials and access scope. If A has broad access, B may inherit that entire scope even though B's task requires only a fraction.
2. **Escalation:** Agent B's own tool capabilities combine with Agent A's delegated access to produce a higher effective privilege than either holds alone.
3. **Intersection gap:** Each system along the delegation chain has its own permission model. No system checks the composite access -- whether the sequence of legitimate accesses across systems produces an illegitimate composite.

Human delegation naturally bounds permission compounding through screen-mediated access. Agent delegation has no such implicit bound. The compound permission surface grows combinatorially with each delegation step.

### Cross-System Composition Audit

When an agent operates across multiple backends in a single workflow (CRM, support, contracts, wiki), three composition problems emerge:

1. **Permission composition:** System A grants access, System B grants access, System C grants access. But the composite -- reading A's data, correlating with B's data, writing to C -- may violate a policy that no individual system knows about.
2. **Audit trail composition:** Each system answers for its own portion, but composing audit trails across systems into a coherent narrative does not exist by default.
3. **Staleness composition:** Agents mix data with different freshness without distinguishing -- stale wiki pages correlated with fresh CRM data produce synthesis that blends stale and fresh information without marking the difference.

**Mitigation:** Cross-system correlation IDs ensure every agent run generates a unique trace ID passed to every system touched. Freshness metadata tags all retrieved data with timestamps and staleness thresholds. A "permission manifest" declares all systems a workflow will touch, reviewed before deployment.

### Spawning Restrictions

For multi-agent orchestration systems, restrict which subagent types a coordinator can spawn:

| Syntax | Effect |
|--------|--------|
| `tools: Agent(worker, researcher)` | Allowlist -- can spawn only `worker` and `researcher` |
| `tools: Agent` | Unrestricted -- can spawn any subagent |
| `tools: Read, Bash` (no `Agent`) | Denied -- cannot spawn any subagents |

Key properties:
- **Allowlist, not denylist.** Listing types permits only those; everything else is blocked.
- **Silent block with visible types.** Attempted spawn of a non-allowed type fails; the agent sees only allowed types.
- **Scope: main-thread only.** Subagents cannot spawn other subagents regardless -- bounds recursive depth at one level.

### Foreground vs. Background Permission Models

Two distinct permission semantics for two execution modes:

**Foreground** (blocking):
- Permission prompts pass through to the user in real-time.
- Clarifying questions are answerable interactively.
- Risk is bounded by attention span.

**Background** (concurrent):
- All tool permissions are prompted upfront before launch.
- Once running, the agent auto-denies anything not pre-approved.
- Risk is bounded by the correctness of the initial permission inventory.

**Design principle:** Skills that touch destructive operations default to foreground (interactive approval per action). Skills that are strictly read-only default to background (pre-approved limited scope).

### Permission Governance Template

```markdown
## Permission Governance — {{SYSTEM_NAME}}

### Delegation Chain Policy
- Monotonic narrowing: {{ENFORCED / NOT_ENFORCED}}
- Maximum delegation depth: {{N_LEVELS}}
- Authority ceiling inheritance: {{STRICT_SUBSET / CONFIGURABLE / UNRESTRICTED}}

### Spawning Restrictions
| Coordinator Agent | Allowed Subagents | Denied Subagents |
|-------------------|-------------------|------------------|
| {{AGENT_NAME}} | {{ALLOWLIST}} | {{ALL_OTHERS / SPECIFIC}} |

### Cross-System Permission Manifest
| Workflow | Systems Touched | Composite Access Review | Correlation ID |
|----------|----------------|------------------------|----------------|
| {{WORKFLOW}} | {{SYSTEMS}} | {{REVIEWED_DATE / PENDING}} | {{ID_SCHEME}} |

### Permission Mode Defaults
| Skill / Agent | Default Mode | Rationale |
|---------------|-------------|-----------|
| {{SKILL}} | {{FOREGROUND / BACKGROUND}} | {{RATIONALE}} |

### Scope Priority Ladder
| Priority | Location | Scope |
|----------|----------|-------|
| 1 (highest) | Managed settings | Organization-wide |
| 2 | CLI flag | Current session |
| 3 | Project `.claude/agents/` | Current project |
| 4 | User `~/.claude/agents/` | All user projects |
| 5 (lowest) | Plugin `agents/` | Where plugin enabled |

### Compound Permission Audit
| Delegation Chain | Effective Permissions | Designed? | Last Audit |
|------------------|-----------------------|-----------|------------|
| {{A → B → C}} | {{COMPOSITE_PERMISSIONS}} | {{YES / EMERGENT}} | {{DATE}} |
```

---

## Section 7: Trace and Audit Agent Decisions

Every agent action should be self-documenting: the governing policy version, permits, evidence, and authority fused with the action at execution time. This section covers how to build decision traceability into agent architectures.

### The Actor Passport Schema

Every actor in a governed system is wrapped in a passport schema -- a structured identity artifact that the policy layer consults at runtime:

1. **Role bindings** -- which roles the actor holds. Roles determine which events the actor may trigger.
2. **Authority ceilings** -- the maximum scope of action the actor is permitted, regardless of role. Prevents privilege escalation even if a role temporarily gains broader permissions.
3. **Trust markers** -- verifiable signals of trustworthiness (authentication source, delegation chain, JIT provisioning timestamp).

The passport transforms anonymous prompts into governed identities. From the actor model forward, every event has a bound identity and a strictly defined authority limit. Before the actor model, agency is implicit (any prompt can claim any role). After it, agency is explicit and verifiable.

**Runtime validation flow:** When an actor triggers an event, the policy layer validates the passport against the event's authority requirements. If the passport does not carry the required role bindings or exceeds its authority ceiling, the event is blocked.

### The Passport Object (Per-Decision Artifact)

A passport object is generated at the moment an agent executes an action. It permanently fuses:

- The action data (what, when, inputs/outputs)
- The exact policy bundle version bound at execution time
- The specific permits granted by that bundle
- The denials enforced
- The obligations required to fire
- The evidence required before execution was allowed

The passport is cryptographically bound to the bundle version, creating an immutable, self-contained record. An auditor can answer every regulatory question from the passport alone, without log search or developer query.

This differs from standard telemetry: telemetry records *what happened*; passport objects record *what rule governed the decision*. The rule traveled with the event rather than remaining in a repository.

**Tiered passport variants:** Full passport for high-consequence actions. Summary passport for routine operations. Tiered by action risk level to manage storage growth.

### The Context Warrant

Before any agent decision, the system assembles a context warrant: a formally justified, minimum-necessary data package.

**Key properties:**
1. **Justified** -- every piece of context has an explicit reason for inclusion. Context without justification is rejected.
2. **Minimum-necessary** -- pulls exactly what's needed; rejects extraneous assembly.
3. **Freshness-enforced** -- stale data (outdated policy versions, expired actor states) is rejected, not just flagged.
4. **Dimension-scoped** -- context organized by dimension (history, policy, actor state, tool state); the warrant specifies which dimensions are required for this specific decision.

Over-context is a governance failure as dangerous as under-context. An agent with excessive context can make decisions that appear plausible but are based on irrelevant signals. The context warrant makes context assembly an auditable, governed step.

### Tool and Model IO Contracts

Every external side effect is governed by a formal IO contract:

1. **Strict preconditions** -- conditions that must be true before execution. Failure to meet preconditions blocks the effect entirely.
2. **Rate limits** -- bounds on frequency. Violations block execution, not just warn.
3. **Idempotency rules** -- what happens if the effect is triggered twice. Idempotent effects are safe on retry; non-idempotent effects need explicit deduplication guards.

The precondition-block pattern (rather than precondition-warn) is the critical design choice. Many systems log when preconditions fail but still execute. This produces systems where governance failures are observable in hindsight but not preventable in the moment.

### Decision Traceability Template

```markdown
## Decision Traceability — {{SYSTEM_NAME}}

### Actor Passport Schema
```yaml
actor_passport:
  actor_id: "{{UNIQUE_ID}}"
  role_bindings:
    - role: "{{ROLE}}"
      scope: "{{SCOPE}}"
      granted_by: "{{AUTHORITY}}"
  authority_ceiling:
    max_blast_radius: "{{LEVEL}}"
    max_cost_per_action: "{{AMOUNT}}"
    forbidden_operations: [{{LIST}}]
  trust_markers:
    authentication: "{{METHOD}}"
    delegation_chain: [{{CHAIN}}]
    provisioned_at: "{{TIMESTAMP}}"
    expires_at: "{{TIMESTAMP}}"
```

### Passport Object Schema
```yaml
passport_object:
  action_id: "{{UNIQUE_ID}}"
  timestamp: "{{ISO_TIMESTAMP}}"
  actor_passport_ref: "{{ACTOR_ID}}"
  policy_bundle_version: "{{VERSION}}"
  permits_granted: [{{LIST}}]
  denials_enforced: [{{LIST}}]
  obligations_fired: [{{LIST}}]
  evidence_evaluated:
    - type: "{{EVIDENCE_TYPE}}"
      value: "{{EVIDENCE_VALUE}}"
      freshness: "{{TIMESTAMP}}"
  action_data:
    operation: "{{WHAT}}"
    inputs: {{INPUTS}}
    outputs: {{OUTPUTS}}
  cryptographic_binding: "{{HASH}}"
```

### Context Warrant Schema
```yaml
context_warrant:
  decision_type: "{{TYPE}}"
  required_dimensions:
    - dimension: "{{HISTORY / POLICY / ACTOR_STATE / TOOL_STATE}}"
      justification: "{{WHY_NEEDED}}"
      freshness_requirement: "{{MAX_AGE}}"
      source: "{{WHERE_FROM}}"
  excluded_dimensions:
    - "{{DIMENSION_NOT_NEEDED}}"
  assembled_at: "{{TIMESTAMP}}"
  warrant_valid_until: "{{EXPIRY}}"
```

### IO Contract Registry
| Tool / Effect | Preconditions | Rate Limit | Idempotent? | Failure Mode |
|---------------|---------------|------------|-------------|--------------|
| {{TOOL}} | {{CONDITIONS}} | {{LIMIT}} | {{YES/NO}} | {{BLOCK / WARN / RETRY}} |
```

---

## Section 8: Manage Agent Identity and Portability

### The Behavioral Lock-In Problem

After months of interaction, an AI agent accumulates a behavioral model -- not just your data, but patterns of how you work: which emails you respond to immediately, how you schedule, which threads matter, how you prepare for meetings. This behavioral context is the product of your data + the provider's compute + months of inference.

Unlike data lock-in (which has export tools, legal frameworks, and migration consultants), behavioral context does not export. There is no CSV of "how this person thinks." Switching providers means losing the compounding that made the agent useful -- returning to a "brilliant stranger."

### Mitigation Strategies

1. **Build a portable behavioral audit.** Periodically export a structured description of your work patterns, preferences, and decision criteria in a provider-agnostic format. This is a lossy approximation but better than nothing.
2. **Separate data from behavioral inference.** Keep your data (documents, communications, decisions) in systems you control. The behavioral model built on top is harder to port, but the underlying data should be portable.
3. **Define learning boundaries.** Explicitly scope what the agent should and should not learn about your behavior. Some behavioral context is valuable; some is a privacy risk.
4. **Treat portability as a governance requirement.** Before adopting a persistent agent platform, assess: Can I export behavioral context? Who owns the behavioral model -- user, employer, or provider? What is the switching cost after 6 months?

---

## Pitfalls

### 1. Binary autonomy (all-or-nothing)
Approve-everything creates risk exposure. Approve-nothing creates a bottleneck indistinguishable from not having an agent. Use the four-level gradient, assigned per decision type.

### 2. Deferred review creating compound debt
Batching reviews at milestones instead of reviewing incrementally creates exponential review cost. Ten individually-reviewed changes might take 10 minutes each; the same ten changes reviewed as a batch might take 3 hours due to cascading assumptions. Set a maximum unreviewed depth.

### 3. Governance policies without enforcement
HITL policies without identity-aware orchestration are unenforceable aspirations. Only 28% of organizations can trace agent actions back to a human sponsor. Invest in enforcement infrastructure, not just policy documents.

### 4. Static trust that never adjusts
A fixed permission model wastes human attention on proven-safe tasks and may under-gate novel risks. Trust should ramp up with demonstrated reliability and reset when the model changes or scope expands.

### 5. Single-reviewer bottleneck
Over-reliance on a single reviewer (common in solo-operator systems) creates a single point of failure. Reviewer fatigue from high-volume review degrades quality over time. Use automated pre-screening and review obsolescence to reduce the volume requiring human attention.

### 6. Speeding up review at the expense of depth
Attempts to process the review queue faster risk approving subtly flawed work. Track downstream failure rates of approved artifacts. If failures increase, reduce throughput and tighten review criteria -- do not increase volume to compensate for a quality problem.

### 7. Over-automating review
Not all review can be automated away. Architectural judgment, design tradeoffs, and naming decisions require human evaluation. The goal is to eliminate mechanical review categories, not eliminate all review.

### 8. Ignoring behavioral lock-in until it is established
The conversation about portability tends to happen after lock-in is already established. Assess portability before adopting persistent agent platforms, not after.

### 9. Adopting middleware before the system needs it
Twelve-layer middleware pipelines are powerful but expensive: per-request latency on every tool call, ordering bugs that surface only under interaction, and debugging that demands good observability up-front. Most agent harnesses are not at the complexity that justifies middleware. Start with rules; promote to hooks when discrete lifecycle events need interception; only promote to middleware when cross-cutting concerns span tool calls and the simpler architectures cannot intercept what needs enforcing.

### 10. Specs as governance theater
Specification-based enforcement only works when specs are kept in sync with the code they specify. A spec that drifts -- ignored when the code is updated, kept around for compliance optics -- becomes a decoration that passes its own conformance tests while failing to reflect actual behavior. Bidirectional sync (read spec -> implement -> verify alignment -> update spec or code) is the discipline; without it, specification-based governance degrades into wishful thinking.

### 11. Per-step over-restriction breaking workflows
Per-node tool restrictions are valuable for least-privilege at workflow granularity, but they introduce a new failure mode: a node legitimately needs a tool that was denied, and the workflow stalls or fails. Default to inheriting the workflow's broader tool set; narrow only when a specific node's blast radius warrants it; configure clear escalation paths when a node hits a tool-restriction error rather than retrying blindly.

### 12. Shipping agents without a control layer (supervision debt)
Teams that wire models to tools without identifying control points upfront accumulate supervision debt. Each production surprise triggers another bolt-on control -- approval buttons, logs, cancel mechanisms -- that was not designed into the architecture. Map control points before deployment: observation, approval, steering, and cancel points for every workflow.

### 13. Treating tool enablement as feature configuration
MCP server enablement looks like a feature toggle but is actually a security boundary crossing. Enabling a server grants arbitrary code execution within that tool's scope. Assess what the agent can do with each enabled tool, not just whether the tool is useful.

### 14. Assuming deployment-gate governance covers production
Policy-as-code exits the room the moment the agent goes live. Agents execute continuously between deployments. The deployment gate covers a single moment in a system that never stops acting. Runtime-enforceable policy bundles close this gap.

### 15. Permission compounds invisible until breach
Each system in a delegation chain evaluates access independently. The composite access across all systems is nobody's problem until it produces a breach. Require compound permission audits for multi-agent workflows. Enumerate all systems touched and verify the composite access is intentional.

### 16. Building runtime engines before governance layers
Most multi-agent systems are built in reverse order: agent personas and prompt protocols first, governance retrofitted after. Post-hoc governance fails because governance requirements should constrain architectural decisions, not be retrofitted around them. Build in dependency order: ontology first, capability contracts last.

### 17. Over-engineering the build order for simple systems
A 3-agent workflow does not need all 11 governance layers. Applying the full build order to low-complexity systems introduces unnecessary overhead. Match governance depth to risk profile.

---

## Related Guides

- **G1 -- Writing Agent Specifications:** Hard constraints from specifications feed directly into autonomy tier boundaries and guardrail definitions. Spec-driven development (Section 3's Comprehension Problem, Layer 1) is the upstream discipline that makes governance specs possible.
- **G2 -- Managing Agent Context:** Distributed governance scope (Section 4 Layer 4) and distributed context architecture share the same boundary mechanic -- root + subsystem files at the same locations -- but G2 governs context distribution and this guide governs rule distribution. Use both at the same boundary points; the AGENTS.md/CLAUDE.md files often serve both functions. Context warrants (Section 7) formalize the context assembly that G2 describes informally.
- **G6 -- Agent Safety and Permissions:** The permission tiers and sandboxing in G6 are the enforcement layer beneath the governance policies in this guide. G6 covers how to enforce; this guide covers what to enforce, when, and through which architecture. Permission compounding (Section 6) extends G6's single-agent model to multi-agent delegation chains.
- **G3 -- Agent Architecture Decisions:** Architecture choices (single-agent vs. multi-agent, planner-executor patterns) determine the governance topology -- how many agents need tiers, who reviews whom, and how identity chains propagate. Per-step tool restrictions (Section 1) presume a workflow-DAG architecture; if no DAG exists, per-step granularity does not apply. Spawning restrictions (Section 6) are the governance surface of G3's orchestration patterns.
- **G4 -- Building Agent Evaluation Suites:** Evaluation results provide the evidence for trust calibration -- the data that determines whether an agent has earned promotion to a higher autonomy tier. The "spec becomes the eval" insight (Section 3) is the bridge from specification to evaluation.
- **G7 -- Session Persistence and Memory:** Memory write policies, novelty gates, and contradiction detection in G7 (Part 5) are the memory-specific instantiation of the governance patterns in this guide. Memory governance and agent governance share the same human-gate / audit-trail / rollback-path structure.
- **G11 -- [[building-agentic-systems|Building Agentic Systems]]:** Human-gate placement and review workflows from this guide apply to G11's proactive-loop checkpoint discipline (Section 6) -- where scheduled autonomous agents need governance rails.

---

## Contract

### Preconditions
- An agent system exists that makes decisions with varying blast radius and reversibility.
- Human oversight is required (regulatory, organizational, or risk-based).
- A decision taxonomy exists or can be constructed for the domain.
- The system supports per-decision-type configuration of oversight level.
- An enforcement architecture is chosen (rules, hooks, middleware, specification, or a deliberate mix) before policies are written -- policy without architecture is aspirational.
- For multi-agent systems: a permission model is defined that addresses delegation chains and compound access.
- Reversibility classification exists for each action type the agent can take.

### Invariants
- Human retains override authority at all autonomy levels. No tier removes the ability to intervene.
- Audit trail is maintained for all agent actions -- append-only, immutable, queryable.
- Autonomy level is assigned per decision type, not per agent globally; per-decision-point granularity refines this further when a workflow-DAG architecture is in use.
- Trust promotion requires demonstrated track record; trust demotion is immediate on failure.
- No decision type defaults to full autonomy without explicit classification.
- Destructive or irreversible actions always require human approval regardless of trust level.
- Comprehension is maintained for shipped work; agent-generated artifacts that no human has read are governance debt, not throughput gains.
- Enforcement architecture matches system complexity: rules for static constraints, hooks for lifecycle events, middleware for cross-cutting concerns, specification for verified compliance. Promotion to a heavier architecture is justified by what the lighter architecture cannot intercept, not by aesthetic preference.
- Governance scope is locality-aware: universal rules live in the root file; subsystem-specific rules live at the boundary they constrain; inheritance semantics are explicit.
- Permissions narrow monotonically across delegation chains. Each delegation step can only reduce permissions, never expand them.
- Every agent action is traceable to a governing policy version. The rule travels with the decision, not just with the deployment.
- Agent outputs that reach human decision-makers carry explicit fact-vs-judgment classification.
- Tool access is treated as a security boundary, not a feature toggle. Connection-level assessment precedes per-call approval.
- Pattern-scale governance failures trigger process-level architectural fixes, not individual training.

### Governance
- Autonomy tier assignments are governed artifacts -- agents cannot modify their own tier.
- Per-step tool restrictions in workflow YAML are governed artifacts -- the orchestration engine enforces them; the agent cannot widen its own access.
- Changes to review delegation (what gets auto-screened vs. human-reviewed) require explicit authorization.
- Trust ledger assessments are revisited when model versions change, system scope changes, or failures occur.
- Review quality metrics (downstream failure rate) are tracked alongside throughput metrics.
- Comprehension coverage is tracked alongside test coverage; surfaces lacking self-describing structure or comprehension-gate review are flagged for remediation.
- Enforcement-architecture choice is reviewed when system complexity grows (subsystem count, tool count, lifecycle event count) -- the chosen architecture may need promotion.
- Distributed governance file inheritance semantics are documented at the root file and validated on load.
- Policy bundle versions are immutable once active; changes require new version promotion, not in-place mutation.
- Permission manifests for cross-system agent workflows are reviewed before deployment and re-audited on workflow change.
- Spawning allowlists are governed artifacts; changes require governance review.
- This guide is IL-owned draft; Nick deploys to `meta-system/knowledge/guides/`.

### Recovery
- **Trust violation:** If an agent acts beyond its assigned autonomy level, immediately demote to human-required for that task type. Investigate the enforcement mechanism, not just the agent's behavior. Remediate any damage. Reclassify only after the enforcement gap is closed.
- **Review quality degradation:** If downstream failure rate of approved artifacts increases, reduce production throughput and tighten review criteria until quality stabilizes. Do not increase review volume to compensate for a quality problem.
- **Audit gap detected:** If the governance memory layer fails to capture a decision (missing log entries), treat as a governance incident. Reconstruct the decision trail from available evidence, then fix the logging mechanism before resuming autonomous operations.
- **Model regression:** If a model update invalidates previously earned trust (detected via increased failure rates), reset affected task types to proposal-first and re-earn trust from that level.
- **Enforcement bypass detected:** If an agent acts before approval was obtained, audit the architecture choice before adjusting policy. Static rules cannot intercept ongoing execution -- a bypass under rules-only enforcement may be evidence the architecture needs promotion to hooks or middleware, not just stricter policy.
- **Comprehension audit reveals dark code:** If a surface ships without any human reading the diff, freeze further automated production on that surface, restore comprehension via spec write-up + review walkthrough, and add the surface to the comprehension-gate roster before resuming.
- **Specification drift:** If specs and code disagree, halt the affected workflow and reconcile spec -> code or code -> spec by judgment. Do not let either side run authoritatively while the other is stale; that is the failure mode "specs as governance theater" surfaces.
- **Permission compound detected:** If a delegation chain produces composite permissions that were not designed, freeze the delegation chain. Apply monotonic narrowing: each delegation step must produce a strict subset of the delegator's permissions. Audit the compound and redesign the delegation scopes before re-enabling.
- **Runtime governance gap detected:** If agents are executing under outdated policy (bundle version drift), immediately promote the current bundle version to all bound agents. If instant promotion is not supported, halt agent execution until the deployment pipeline catches up. Implement runtime binding for future gap prevention.
- **Cross-system audit failure:** If a regulator or audit requires the full trail of a cross-system agent action and the composed trail cannot be produced, freeze the workflow. Implement correlation IDs and freshness metadata before re-enabling cross-system agent operations.
