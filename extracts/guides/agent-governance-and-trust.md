---
title: "Agent Governance and Trust"
type: "guideline"
category: "Governance"
target_system:
  - "cross-system"
stage: "draft"
created: "2026-04-19"
updated: "2026-04-26"
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
source_dd:
  - "DD-81"
tags:
  - "guide"
  - "governance"
  - "trust"
  - "autonomy"
  - "enforcement-architecture"
contract:
  preconditions: "Agent system with human oversight requirements; governance model needed; an enforcement architecture is chosen (rules, hooks, middleware, or specification) before policies are written"
  invariants: "Human retains override authority; audit trail maintained; enforcement-architecture choice is explicit and matches system complexity; rule scope is locality-aware (universal rules central, local rules at the boundary)"
  governance: "IL-owned draft; Nick deploys to meta-system/knowledge/guides/"
  recovery: "If trust violations detected, demote agent to lower autonomy tier; if enforcement bypass detected, audit the architecture choice before adjusting policy"
---

# Agent Governance and Trust

How to govern agent autonomy and maintain human oversight as agent output scales beyond human review capacity. This guide addresses the central tension of agentic systems: agents produce at 100x speed, humans review at 3x speed, and the gap between those numbers is where governance either holds or collapses.

The guide covers four concerns: defining autonomy tiers so agents act within calibrated boundaries, evolving review processes so oversight scales with output and the comprehension that justifies it, building governance infrastructure so policies are enforced rather than aspirational, and managing agent identity so oversight is traceable and portable.

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

## Key Concepts

**1. Autonomy is a gradient, not a switch.** Binary models (approve everything vs. approve nothing) fail. Approve-everything creates risk; approve-nothing creates a bottleneck indistinguishable from not having an agent. The correct model is a four-level gradient -- full autonomy, guarded, proposal-first, human-required -- assigned per decision type based on blast radius and reversibility, and refinable per decision point within a workflow.

**2. Review is the binding constraint, not production.** The investment that determines agentic ROI is review infrastructure, not agent tooling. An agent that produces 100 artifacts per day into a queue that drains at 10 per day accumulates liability, not value. Design the pipeline to match review bandwidth, not production capacity.

**3. Every review comment is a system design signal.** The purpose of catching an issue in review is not to fix that instance but to eliminate the entire class of issue from future review. Each review comment that recurs is evidence that the system allows a preventable error. The reviewer's goal is to make their own review obsolete for mechanical categories.

**4. Governance policies without enforcement infrastructure are aspirational.** HITL checkpoints, autonomy tiers, and trust ramps only work if backed by identity-aware orchestration, tool gateways, and append-only audit logs. Without enforcement, agents can act before approval is obtained.

**5. Trust is earned per task type, not granted globally.** An agent trusted to write documentation is not automatically trusted to modify infrastructure. Trust calibration tracks success rates per task type and promotes autonomy incrementally. Regression (model updates, scope changes) can invalidate previously earned trust.

**6. Comprehension is upstream of review.** Review exists because someone has to understand what was produced before it ships. When agents generate code that no human reads, the review step does not become unnecessary -- it becomes structurally impossible. Review obsolescence achieved by automation eliminates mechanical review categories; review obsolescence achieved by skipping comprehension creates "dark code" that passes tests but is owned by no one. Restoring comprehension is the upstream fix; throughput improvements are downstream.

**7. Enforcement is architectured, not just policy.** Two systems can declare identical autonomy tiers, identical trust ramps, and identical audit requirements, yet deliver opposite levels of safety -- because one enforces via static rules at invocation time, the other intercepts every tool call through ordered middleware. The enforcement architecture (rules / hooks / middleware / specification) is itself a design decision with its own tradeoffs in coverage, ordering, latency, and debuggability. Policy without architecture is aspirational; architecture without policy is mechanism without intent.

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
- The workflow is short (≤2 steps) or every step has similar trust profile.
- Tool restrictions become so finely sliced that a single legitimate action requires whitelisting across many nodes.

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

### Batch Configuration
- Batch size: {{N}} artifacts per review cycle
- Review cadence: {{SCHEDULE}}
- Backlog threshold (pause production): {{N}} unreviewed items

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

### Batch Configuration
- Batch size: 15 findings per review cycle
- Review cadence: End of each research session
- Backlog threshold: 30 unreviewed findings triggers pipeline pause

### Quality Metrics
- Downstream failure rate: Not yet tracked
- Approval rate: ~85% (within target)
```

---

## Section 4: Build Governance Infrastructure

Autonomy tiers and review processes are policy. Without enforcement infrastructure, they are aspirational. This section starts with the meta-decision -- which enforcement architecture to use -- then walks the four infrastructure layers that an architecture-of-choice instantiates.

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
- Spec-driven development where specs are living artifacts kept bidirectionally in sync with code -- read spec → implement → verify alignment → update spec or code.
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

**Inheritance semantics must be explicit.** Without explicit override rules, it is unclear whether a subsystem rule supplements or replaces a root rule. Default heuristic: subsystem rules add to root rules; conflicts fail the load with a structured error. Override-by-default semantics are dangerous unless the system has well-tested cascade rules.

**When to reach for distributed scope:**
- The system has 3+ subsystems with materially different governance needs.
- The root governance file exceeds ~300 lines or accumulates rules irrelevant to most agent loops.
- Multiple AI tools read governance from differently-named files.

**When not to:**
- Single-subsystem project; rules fit comfortably in one file.
- Rule granularity is finer than subsystem boundaries (use a tagged-rule system instead).
- File system layout does not cleanly map to governance boundaries (use dynamic context assembly instead).

### Governance Infrastructure Template

```markdown
## Governance Infrastructure — {{SYSTEM_NAME}}

### Enforcement Architecture
- Primary architecture: {{RULES / HOOKS / MIDDLEWARE / MIXED}}
- Specification-based layer: {{NONE / CONFORMANCE_TESTS / SPEC_DRIVEN_DEV}}
- Hook events instrumented: {{LIST OR N/A}}
- Middleware layers (in order): {{LIST OR N/A}}
- Spec location (if specification-based): {{PATH OR N/A}}

### Audit Layer
- Log format: {{FORMAT}}
- Fields: episode_id, retrieval_set_id, policy_version, model_version, {{ADDITIONAL_FIELDS}}
- Retention policy: {{DURATION}}
- Storage location: {{PATH_OR_SERVICE}}
- Query interface: {{TOOL}}

### Tool Gateway
- Enforcement point: {{GATEWAY_LOCATION}}
- Allowlisted tools: {{LIST}}
- Credential handling: {{PROXY / DIRECT / NONE}}
- Rate limits: {{LIMITS}}
- Per-step restrictions: {{YES / NO}} (per-node tool allowlists/denylists active in workflow YAML)

### Identity
- Provisioning: {{JIT / STATIC / N_A}}
- Decision lanes:
  | Risk Level | Approval Window | Timeout Action |
  |-----------|----------------|---------------|
  | {{LEVEL}} | {{DURATION}} | {{DENY / ESCALATE}} |
- Approval format: {{SIMPLE / CHECKLIST / STRUCTURED_BRIEFING}}

### Distributed Scope
- Root governance file: {{PATH}}
- Subsystem boundaries with local files: {{LIST OR N/A}}
- Multi-tool compatibility: {{SYMLINK / DUPLICATE / NONE}}
- Inheritance semantics: {{ADD-ONLY / OVERRIDE-ALLOWED / N_A}}

### Current Gaps
| Component | Status | Gap |
|-----------|--------|-----|
| {{COMPONENT}} | {{IMPLEMENTED / PARTIAL / MISSING}} | {{DESCRIPTION}} |
```

### Worked Example: MetaSystem Governance Infrastructure

```markdown
## Governance Infrastructure — MetaSystem

### Enforcement Architecture
- Primary architecture: HOOKS (Claude Code event hooks)
- Specification-based layer: NONE (DD set is reference, not conformance-tested)
- Hook events instrumented: SessionStart, PreCompact, PostToolUse, PreToolUse (read-guard removed 2026-04-23)
- Middleware layers: N/A (no request-pipeline middleware)
- Spec location: N/A
- GAP: No conformance-test layer for cross-system invariants

### Audit Layer
- Log format: Markdown files (system-log/)
- Fields: date, category, description, system, related DDs
- Retention policy: Indefinite (git-tracked)
- Storage location: {system}/operations/system-log/
- Query interface: Dataview queries, Glob/Grep
- GAP: No episode-level capture of tool calls or context window state

### Tool Gateway
- Enforcement point: Claude Code built-in permission system
- Allowlisted tools: Bash, Read, Write, Edit, Glob, Grep, MCP tools
- Credential handling: Direct (no proxy)
- Rate limits: None
- Per-step restrictions: NO (no workflow-DAG layer; single-loop architecture)
- GAP: No centralized gateway; permissions distributed across tool prompts

### Identity
- Provisioning: N/A (single-agent, single-operator)
- Decision lanes: None (conversational approval)
- Approval format: Simple ("agent asks, Nick approves in chat")
- GAP: No time-boxed lanes, no structured briefings, no JIT identity

### Distributed Scope
- Root governance file: CLAUDE.md (workspace root)
- Subsystem boundaries with local files: systems/improvement-loop/CLAUDE.md, systems/meta-system/CLAUDE.md, .claude/rules/governance.md
- Multi-tool compatibility: NONE (Claude Code only; no AGENTS.md symlinks yet)
- Inheritance semantics: ADD-ONLY (system files extend root; no override path)

### Current Gaps
| Component | Status | Gap |
|-----------|--------|-----|
| Governance memory | PARTIAL | System-log exists but lacks tool-call-level granularity |
| Tool gateway | PARTIAL | Built-in permissions, but no centralized audit |
| Identity governance | MISSING | Conversational only, not policy-driven |
| Decision lanes | MISSING | No time-boxed approval windows |
| Specification layer | MISSING | DDs are reference, not conformance-verified |
| Per-step restrictions | N/A | No workflow-DAG architecture; single-loop agent |
```

---

## Section 5: Manage Agent Identity and Portability

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
Specification-based enforcement only works when specs are kept in sync with the code they specify. A spec that drifts -- ignored when the code is updated, kept around for compliance optics -- becomes a decoration that passes its own conformance tests while failing to reflect actual behavior. Bidirectional sync (read spec → implement → verify alignment → update spec or code) is the discipline; without it, specification-based governance degrades into wishful thinking.

### 11. Per-step over-restriction breaking workflows
Per-node tool restrictions are valuable for least-privilege at workflow granularity, but they introduce a new failure mode: a node legitimately needs a tool that was denied, and the workflow stalls or fails. Default to inheriting the workflow's broader tool set; narrow only when a specific node's blast radius warrants it; configure clear escalation paths when a node hits a tool-restriction error rather than retrying blindly.

---

## Related Guides

- **G1 -- Writing Agent Specifications:** Hard constraints from specifications feed directly into autonomy tier boundaries and guardrail definitions. Spec-driven development (Section 3's Comprehension Problem, Layer 1) is the upstream discipline that makes governance specs possible.
- **G2 -- Managing Agent Context:** Distributed governance scope (Section 4 Layer 4) and distributed context architecture share the same boundary mechanic -- root + subsystem files at the same locations -- but G2 governs context distribution and this guide governs rule distribution. Use both at the same boundary points; the AGENTS.md/CLAUDE.md files often serve both functions.
- **G6 -- Agent Safety and Permissions:** The permission tiers and sandboxing in G6 are the enforcement layer beneath the governance policies in this guide. G6 covers how to enforce; this guide covers what to enforce, when, and through which architecture.
- **G3 -- Agent Architecture Decisions:** Architecture choices (single-agent vs. multi-agent, planner-executor patterns) determine the governance topology -- how many agents need tiers, who reviews whom, and how identity chains propagate. Per-step tool restrictions (Section 1) presume a workflow-DAG architecture; if no DAG exists, per-step granularity does not apply.
- **G4 -- Building Agent Evaluation Suites:** Evaluation results provide the evidence for trust calibration -- the data that determines whether an agent has earned promotion to a higher autonomy tier. The "spec becomes the eval" insight (Section 3) is the bridge from specification to evaluation.
- **G7 -- Session Persistence and Memory:** Memory write policies, novelty gates, and contradiction detection in G7 (Part 5) are the memory-specific instantiation of the governance patterns in this guide. Memory governance and agent governance share the same human-gate / audit-trail / rollback-path structure.
- **G11 -- [[building-agentic-systems|Building Agentic Systems]]:** Human-gate placement and review workflows from this guide apply to G11's proactive-loop checkpoint discipline (Section 6) — where scheduled autonomous agents need governance rails.

---

## Contract

### Preconditions
- An agent system exists that makes decisions with varying blast radius and reversibility.
- Human oversight is required (regulatory, organizational, or risk-based).
- A decision taxonomy exists or can be constructed for the domain.
- The system supports per-decision-type configuration of oversight level.
- An enforcement architecture is chosen (rules, hooks, middleware, specification, or a deliberate mix) before policies are written -- policy without architecture is aspirational.

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

### Governance
- Autonomy tier assignments are governed artifacts -- agents cannot modify their own tier.
- Per-step tool restrictions in workflow YAML are governed artifacts -- the orchestration engine enforces them; the agent cannot widen its own access.
- Changes to review delegation (what gets auto-screened vs. human-reviewed) require explicit authorization.
- Trust ledger assessments are revisited when model versions change, system scope changes, or failures occur.
- Review quality metrics (downstream failure rate) are tracked alongside throughput metrics.
- Comprehension coverage is tracked alongside test coverage; surfaces lacking self-describing structure or comprehension-gate review are flagged for remediation.
- Enforcement-architecture choice is reviewed when system complexity grows (subsystem count, tool count, lifecycle event count) -- the chosen architecture may need promotion.
- Distributed governance file inheritance semantics are documented at the root file and validated on load.
- This guide is IL-owned draft; Nick deploys to `meta-system/knowledge/guides/`.

### Recovery
- **Trust violation:** If an agent acts beyond its assigned autonomy level, immediately demote to human-required for that task type. Investigate the enforcement mechanism, not just the agent's behavior. Remediate any damage. Reclassify only after the enforcement gap is closed.
- **Review quality degradation:** If downstream failure rate of approved artifacts increases, reduce production throughput and tighten review criteria until quality stabilizes. Do not increase review volume to compensate for a quality problem.
- **Audit gap detected:** If the governance memory layer fails to capture a decision (missing log entries), treat as a governance incident. Reconstruct the decision trail from available evidence, then fix the logging mechanism before resuming autonomous operations.
- **Model regression:** If a model update invalidates previously earned trust (detected via increased failure rates), reset affected task types to proposal-first and re-earn trust from that level.
- **Enforcement bypass detected:** If an agent acts before approval was obtained, audit the architecture choice before adjusting policy. Static rules cannot intercept ongoing execution -- a bypass under rules-only enforcement may be evidence the architecture needs promotion to hooks or middleware, not just stricter policy.
- **Comprehension audit reveals dark code:** If a surface ships without any human reading the diff, freeze further automated production on that surface, restore comprehension via spec write-up + review walkthrough, and add the surface to the comprehension-gate roster before resuming.
- **Specification drift:** If specs and code disagree, halt the affected workflow and reconcile spec → code or code → spec by judgment. Do not let either side run authoritatively while the other is stale; that is the failure mode "specs as governance theater" surfaces.
