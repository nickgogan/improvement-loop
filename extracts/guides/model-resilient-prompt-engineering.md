---
title: "Model-Resilient Prompt Engineering"
type: "guideline"
category: "Prompt Craft"
target_system:
  - "improvement-loop"
stage: "draft"
created: "2026-04-19"
updated: "2026-07-16"
author: "claude"
source_findings:
  - "model-agnostic-prompting-three-properties"
  - "reasoning-model-anti-pattern-prescribed-reasoning"
  - "extract-deep-plan-prompt-as-custom-skill"
  - "advisor-executor-api-pattern"
  - "task-specific-model-routing-table-march-2026-bench"
  - "brevity-constraints-reverse-llm-performance"
  - "advanced-elicitation-techniques-library"
  - "oneshot-infrastructure-setup-prompt-pattern"
  - "cot-fails-without-inductive-generalization"
  - "negative-constraints-as-probabilistic-output-collapse"
  - "yaml-template-dual-structure"
  - "design-evaluate-dual-phase-prompting-framework"
  - "prompt-as-policy-version-control-and-cicd-for-agen"
  - "bmad-outcome-based-skill-rewrite-pattern"
  - "frontier-release-compression-march-2026"
  - "layered-prompt-assembly-stable-segment-caching"
  - "bidirectional-prompting-for-spec-creation"
  - "metaprompting-karpathy-autoresearch-for-build"
  - "programmatic-snippet-extraction-via-shell-anti-hallucination"
  - "star-commands-for-explicit-output-format-override"
  - "declarative-goal-driven-agent-prompting"
  - "hands-off-routine-prompt-precision-pattern"
  - "leading-words-lexical-steering-reasoning-trace-verification"
  - "progressive-search-wide-then-narrow"
  - "seven-rung-minimal-code-decision-ladder"
  - "skill-authoring-explain-the-why-not-musts"
  - "skill-description-structure-what-when-capabilities"
  - "strictness-escalation-skill-architecture"
  - "surgical-change-constraint-agent-scope"
  - "thinking-models-mental-framework-commands-for-codi"
  - "gstack-office-hours-socratic-discovery-pipeline"
  - "dev-cost-estimation-bias-correction"
  - "mandatory-explicit-model-per-dispatch"
  - "effort-level-tuning-as-first-order-cost-lever"
  - "no-mid-session-model-switching-subagent-handoff"
  - "prototype-at-frontier-then-downshift"
  - "center-vs-edge-of-distribution-task-classification"
source_dd:
  - "DD-81"
tags:
  - "guide"
  - "prompt-engineering"
  - "model-resilience"
  - "model-selection"
contract:
  preconditions: "You are writing or auditing prompts for agent systems that may run on different models or survive model upgrades. You understand the distinction between reasoning models (extended thinking, internalized CoT) and standard models. You have access to test the prompts against acceptance criteria."
  invariants: "Prompts tell the model what to produce, not how to think. No prescribed reasoning paths in prompts for reasoning models. Constraints are expressed as boundaries (negative) rather than aspirations (positive) for high-priority rules, and consequential constraints carry their reasoning. Instructions for skills and agents explain the why; ALL-CAPS imperatives are a yellow flag. Skill descriptions carry what + when + key capabilities. Model selection is task-based, not provider-based; task classification (center vs edge of distribution) precedes routing; model choice is named explicitly at every dispatch and pinned per session; effort level is tuned per task. Prompts are versioned artifacts with testable acceptance criteria. Output format control is explicit and user-overridable, not left to model inference. Code snippets in agent-produced outputs are extracted from source files programmatically, not reconstructed from model memory."
  governance: "Prompts are versioned and tested against acceptance criteria after model upgrades. Model routing and effort tables are reviewed when new benchmark data is available or any constituent model has a major release; downshift events are recorded as routing datapoints. Anti-pattern audits are conducted after major model releases. Metaprompt loops include acceptance criteria that resist proxy-metric gaming. This guide is owned by the Improvement Loop knowledge layer."
  recovery: "If a prompt breaks after a model upgrade: audit against the three durability properties and remove prescribed reasoning patterns. If model costs are too high: tune effort level first, then apply the Advisor-Executor pattern or reroute to cheaper models for bulk work. If a subagent fan-out costs blow up: check for silent model inheritance and make the model explicit per dispatch. If a mid-session model switch is tempting: hand off to a subagent on the cheaper model instead. If prompt performance varies across models: check for violated durability properties first, then check constraint specificity. If brevity constraints degrade complex reasoning: switch to dynamic brevity (verbose for planning, terse for execution). If a skill fails to trigger: audit its description against the what/when/capabilities structure. If a skill triggers but does not comply: strengthen and unify its leading words and verify echo in reasoning traces before adding rules. If cache misses occur on every turn despite stable content: ensure ephemeral state is injected as a separate layer-7 block and not inlined into the cached segment. If agent-produced outputs contain incorrect code snippets: add a programmatic-extraction rule to the prompt. If output format is wrong despite constraints: add explicit user-overridable format commands (star commands). If spec-implementation misalignment causes cascading bugs: insert a bidirectional prompting phase before implementation begins."
---

# Model-Resilient Prompt Engineering

How to write prompts that survive model upgrades, route tasks to the right model at the right effort, and manage prompts as versioned policy. This guide synthesizes five concerns that are usually treated separately -- prompt durability, instruction craft, model selection, prompt lifecycle, and output grounding -- because they interact: a prompt that encodes model-specific reasoning patterns breaks on upgrade, costs too much on the wrong model or effort setting, hallucinates code snippets when quoting from source, and cannot be versioned meaningfully if it drifts with every release.

## When to Use This Guide

- You are writing prompts for skills, agents, or recurring tasks that must survive model upgrades
- You are auditing existing prompts after a model update broke behavior
- You are authoring skill instructions or descriptions and want them to trigger and steer reliably
- You need to choose which model -- and which effort level -- to assign to which agent role or task
- Agent costs are too high and you want to optimize model routing, effort tuning, or dispatch discipline
- You are writing prompts for unattended execution (scheduled routines, cloud automations)
- You are designing prompt templates for reuse across teams or systems
- You want to version-control prompts with testable acceptance criteria
- An agent is producing outputs with incorrect code snippets or stale references
- You need deterministic control over output format during interactive sessions
- You are building a spec before implementation and want to align assumptions with the model

---

## Key Concepts

### Prompt Durability

**Three properties make prompts model-agnostic.** Prompts that survive across model generations share three testable properties: (1) they tell the model *what* to produce, not *how* to think; (2) they surface human judgment *before* the model generates; (3) they keep evaluation responsibility on the human side. These properties emerged from testing 19 techniques across GPT-5.4, Claude 4.6, and Gemini 3.1 -- the common thread across every technique that survived reasoning models.

**Five classic techniques degrade reasoning models.** Chain-of-thought ("think step by step"), few-shot examples, self-consistency runs, least-to-most decomposition, and skeleton-of-thought all conflict with reasoning models' internalized reasoning. They prescribe a thinking process the model already performs better on its own.

**CoT has a hard ceiling.** Chain-of-thought amplifies existing reasoning capabilities but cannot create new ones. When a model lacks the right inductive generalization for a task, no amount of additional reasoning tokens helps. This means reasoning models are not universal amplifiers -- they improve tasks within training distribution but add nothing for genuinely novel abstraction.

**Declarative beats imperative: define done, not steps.** The strongest form of goal-oriented prompting states success criteria and lets the model explore. LLMs are exceptionally good at looping until they meet a specific goal; step-by-step prescriptions constrain that strength, prematurely commit to an approach before the model has analyzed the situation, and leave the agent stuck when the prescribed path fails. The declarative form -- "the user must be able to accomplish Y; figure out how" -- keeps the human in control of outcomes rather than implementation details. For tasks with hard requirements, use the hybrid: declarative goal plus an explicit constraint list.

**Outcome-based instructions outperform procedural ones.** Rewriting skill instructions from step-by-step procedures ("do step 1, then step 2") to outcome specifications ("ensure X is true, ensure Y is complete") cuts token consumption approximately 50% while making prompts more resilient to model changes. The model selects its own execution path rather than following scaffolding that encodes assumptions about its reasoning strategy.

**The declarative default inverts for unattended execution.** Interactive prompts can be goal-shaped because a human can redirect mid-session. Scheduled routines and cloud automations cannot be steered once triggered -- the prompt is the complete specification. For unattended runs, write numbered SOP steps, name data sources explicitly, define the completion signal, narrow scope to limit blast radius, and encode edge-case handling inline ("if no unreads exist, send a Slack message saying 'No unread emails'"). Attendance, not taste, decides which philosophy applies.

### Constraint Engineering

**Negative constraints collapse the output space.** Explicit negative instructions ("never begin with an apology," "do not use technical jargon in summaries") create hard probabilistic walls that remove undesirable output regions, producing more reliable behavior changes than positive guidance ("try to be confident," "aim for clarity"). Use negative constraints for the highest-priority behavioral rules where consistency matters most.

**Constraints need their reasoning attached.** Prescriptive rules without the why produce brittle compliance: the model follows the rule mechanically where it fits, fails to extend it to unanticipated edge cases, and cannot recognize legitimate exceptions. Anthropic's own skill-authoring guidance treats ALL-CAPS MUST/NEVER and rigid structures as yellow flags -- when you find yourself writing them, reframe and explain why the behavior matters. "ALWAYS validate input -- because the downstream consumer assumes well-formed data" outperforms either half alone. Hard constraints (security boundaries, format requirements) keep their teeth; the reasoning rides along.

**Brevity constraints improve accuracy.** Research across 31 models and 1,500 problems shows that forcing brief responses improves accuracy by up to 26 percentage points. Larger models suffer from "spontaneous scale-dependent verbosity" -- RLHF training rewards thoroughness, which introduces error accumulation through over-elaboration. A conciseness constraint is a quality intervention, not just a token-saving measure.

**The biggest token savings come from not writing code at all.** For code-generating prompts, a fixed reuse-before-write decision ladder attacks volume at the source that brevity constraints miss: (1) is this needed at all (YAGNI), (2) does it exist in the codebase, (3) standard library, (4) native platform feature, (5) installable dependency, (6) one-line fix, (7) only then write minimal new code. Every rung climbed saves 100% of that code's tokens -- at write time and at every future read. Independent replication measured ~22% cost reduction; composable with brevity and effort tuning.

**Scope constraints prevent productivity theater.** Agents "improve" code they were not asked to touch -- rewriting comments, reorganizing structure, reformatting -- producing diffs that look helpful while introducing unreviewed drift. The surgical-change constraint bounds the blast radius: touch only what the task requires; leave comments, formatting, and structure outside the task scope untouched. It is the complement of the reuse ladder: the ladder governs how much new code is written; surgical governs how much existing code is touched.

**Correct the model's cost-estimation bias.** Models price design options at human development timelines (weeks for what they build in minutes), which silently biases them toward cheap, low-quality architectures. A one-line standing rule corrects it: *when making technical decisions, don't give too much weight to development cost.* Scope it to design decisions -- the rule corrects mis-estimation, it does not license gold-plating, and human-facing project estimates still need human timelines.

**Output format should be explicitly overridable, not inferred.** Models default to verbose explanatory prose, and even well-crafted system prompts cannot anticipate every format need across a session. User-defined format commands (e.g., `*brief` for bullet points only, `*dev` for code over explanation, `*plan` for structured step-by-step output) provide deterministic override regardless of context. The principle: domains set autopilot defaults; explicit commands give the user manual override.

**Design before prompting, evaluate after.** Every prompt interaction has two phases requiring human judgment: a *Design* phase (choosing the lens, prioritizing constraints, curating evidence) and an *Evaluate* phase (judging whether the output matches intent). Skipping the Design phase produces prompts without intentionality. Skipping the Evaluate phase means the human cannot detect when the model's reasoning diverges from their goals.

### Instruction Craft for Skills and Agents

**Explain the why, don't bludgeon with MUSTs.** Modern models have good theory of mind. Given the reasoning behind an instruction, they extend it to unanticipated cases, recognize exceptions, coordinate it with other rules, and can explain their own behavior. Given only the imperative, they comply brittly. This is the instruction-level expression of durability property 1 -- reasoned context survives model change better than rigid scaffolding.

**Steer with leading words, verify in reasoning traces.** When a skill is not obeyed, the fix is usually not more rules -- it is choosing one high-prior-density phrase ("vertical slice," "facts vs decisions") and repeating it consistently through the instruction. A well-chosen phrase invokes an entire behavior from the model's priors at near-zero token cost. The verification loop is the novel half: watch the reasoning traces. If the agent echoes the phrase in its own thinking, the steering landed; if the phrase never appears, make it more consistent or more powerful before adding rules. Trace echo is a binary, observable acceptance test for whether a phrase is doing work -- necessary evidence, though not sufficient (models can parrot while deviating).

**Descriptions decide whether skills trigger.** The most consequential field of a skill is its description, and it has a proven structure: [What it does] + [When to use it] + [Key capabilities]. Good descriptions are specific, include trigger phrases users would naturally say, and carry a clear value proposition ("Analyzes Figma design files and generates developer handoff documentation. Use when user uploads .fig files, asks for 'design specs'..."). The three named failure modes: too vague ("Helps with projects"), missing triggers, too technical with no user-facing phrasing. To combat documented undertriggering, add a slight push: "Make sure to use this skill whenever the user mentions X, Y, Z, even if they don't explicitly ask."

**Strictness must be operationalized, not adverbialized.** "Be strict" regresses to polite hedging. A review or audit skill that must hold a high bar needs strictness engineered at every layer where it can leak: numbered non-negotiable standards, per-change review questions, an aggressive-flag list of concrete escalation triggers, preferred remedies biased toward deletion, tone calibration via literal example phrases the reviewer should emit, prioritized output ordering with an anti-flooding rule, and an explicit approval bar separating presumptive blockers from waivable concerns. The literal-phrase layer is the most transferable piece -- it pins register far more precisely than adjectives.

### Prompt Architecture

**Templates should encode interaction protocols, not just output schemas.** YAML templates that embed coaching instructions alongside the document schema ("which questions to ask per section, what level of detail to push for, when to move on") produce consistently higher-quality outputs than templates that only define structure. The dual structure makes the agent both a producer and a facilitator.

**Oneshot prompts beat interactive setup.** For infrastructure and configuration tasks, a single comprehensive prompt containing all decisions, known fixes, and overrides is more reliable than an interactive back-and-forth. Each conversation turn introduces noise. A oneshot prompt also serves as living documentation -- reproducible, reviewable, and shareable.

**Elicitation techniques are a library, not a default.** Eighteen advanced techniques (tree of thought, red team/blue team, critique-and-refine, stakeholder roundtable, etc.) exist for pushing past first-pass quality, and mental-model commands (Pareto, inversion, first principles, 5 whys, via negativa, and others packaged as on-demand slash commands) make specific reasoning lenses invocable without permanent prompt weight. The key is selective application based on task type, not applying all techniques everywhere. Overuse wastes tokens and produces analysis paralysis.

**Search prompts should widen before they narrow.** LLMs default to long, over-specific search queries that return nothing. Prompt search-using agents to start with short, broad queries to map the information topology, evaluate what exists, then progressively narrow -- the expert-researcher strategy. In Anthropic's production research system this heuristic (with parallel tool calls) cut complex query resolution time by up to 90%.

**Prompt assembly should be layered, and caching boundaries should be decoupled from structural boundaries.** A well-structured system prompt is built from seven ordered layers: (1) core role/persona, (2) values and soul (SOUL.md), (3) persistent memory and user profile (MEMORY.md/USER.md), (4) skills metadata, (5) project context, (6) provider-specific instructions, (7) ephemeral state. Stable layers (1-6) are assembled by a dedicated module and marked with cache-control markers; ephemeral content (layer 7) is injected as a separate content block so it never invalidates the cached stable portion. The key insight: where you draw the cache boundary is independent of where you draw the logical structure boundary. Benefits apply only in rapid multi-turn sessions (Anthropic's cache TTL is 5 minutes), so this pattern is relevant for interactive agent loops, not one-shot API calls.

### Output Grounding

**Agent-produced code snippets must be extracted programmatically, not reconstructed from memory.** When an agent produces output that quotes code from a codebase (walkthrough documents, PR descriptions, annotated explanations), the prompt should instruct it to extract snippets via shell tools (`sed`, `grep`, `cat`, or equivalent read-only access) rather than typing or reconstructing code from its understanding. Shell-extracted snippets are byte-accurate; hand-typed snippets are reconstructed from the model's working understanding of the file, which diverges from the actual bytes in two ways: direct hallucination (writing code that does not exist in the file) and stale mental model (quoting code as it was before an edit, not as it is now). Both produce plausible-looking output that is subtly wrong -- the class of error that standard review catches least reliably. The mitigation is one sentence of prompt instruction that shifts extraction from inference to filesystem.

**Bidirectional prompting aligns assumptions before implementation.** Instead of dumping a spec and starting implementation, alternate questions between you and the model until both share an identical mental model. The model's questions surface implicit assumptions it would otherwise silently fill from training data; your counter-questions validate that it correctly understands edge cases and architecture constraints. Only when both parties have no more questions does implementation begin. The resulting plan is signed off line by line. This is a Design-phase discipline (see "Design before prompting, evaluate after" above) specifically adapted for spec creation, where undetected assumption misalignment causes cascading bugs during long agentic runs with no opportunity to course-correct.

**Socratic discovery scales the same discipline to scoping.** Where bidirectional prompting aligns an agreed spec, a structured Socratic interrogation challenges whether the spec should exist in that shape at all: force the smallest deployable slice ("what is the smallest version a paying customer will use this week?"), demand behavioral evidence over stated wants, surface the working premises explicitly and require agree/disagree on each, and bring in a fresh-context second opinion that cannot have been biased by the conversation. The premise-challenge step is the highest-leverage part -- assumptions get caught before they calcify into design decisions. The cost is real (~170k tokens in the source implementation), so reserve it for scope-setting moments, not every task.

### Model Selection

**Classify the task before consulting any routing table.** The scarce input in model routing is not benchmark data -- it is knowing whether the task sits at the *center* or the *edge* of the training distribution. Center-of-distribution tasks (familiar shapes, millions of prior examples, output a human can inspect quickly: brochure sites, standard decks, routine feature work) are where models have converged -- cheap and open models tie or beat frontier models there, and paying 9x for frontier buys no quality premium. Edge-of-distribution tasks (novel in shape, hard to inspect, beyond prior example density) are where models still separate and frontier spend pays. Cheap-ties-frontier benchmark results are facts about the task, not the models -- do not over-generalize parity at the center into "frontier is a rip-off," and do not let familiar-looking tasks with hidden edge complexity fail silently on cheap models.

**Route by task, not by provider.** Different models excel at different task types, and the gaps are now wide enough that routing matters. March 2026 benchmarks show clear specialization: Claude Sonnet for coding, GPT-5.4 for browser automation, Gemini 3.1 Pro for abstract reasoning, Gemini Flash for batch extraction at cost floor. Using one model for everything is a documented cost mistake.

**The effort dial moves cost more than the model picker.** Within one frontier model, effort-level tuning is a first-order cost lever: on a long-horizon agentic benchmark, the same model at low effort scored 60% for $3.76/task -- beating the previous tier at max effort (59%, $13/task) at ~29% of the cost -- while its own max-effort configuration cost $22/task for ~70%. The curve flattens at the top (extra-high to max buys almost nothing for 2-4x the cost), so the default (high) overpays on most tasks. Match effort to task complexity and treat effort as a routing input alongside model tier.

**Model choice binds at the dispatch and at the session -- never mid-flight.** Two disciplines follow: (1) *Every subagent dispatch names its model explicitly.* An omitted model silently inherits the session's model -- usually the most expensive; one observed fan-out put all 26 reviewers on the top tier. Explicitness converts a cost architecture from an intention into a checkable property of every dispatch. (2) *Never switch models mid-session.* Prompt caches are model-specific; switching a running session to a cheaper model re-processes the entire accumulated context at full input price -- frequently costing more than finishing on the expensive model. The sanctioned pattern is subagent hand-off: compose a hand-off message and let a fresh session on the cheaper model build its own small cache. Cost savings come from topology, not dynamic switching.

**Turn count beats token price.** The cheapest models take 2-3x the turns on multi-step work and cost more end-to-end than a mid-tier model that finishes in fewer turns. Naive down-tiering on per-token price backfires; the tier heuristics need this correction or the rule produces cheap models failing expensively.

**Prototype at the frontier, then downshift.** Frontier spend is a one-time cost per task class, not a recurring cost per task: prove a new capability end-to-end on the frontier model first, then decompose the proven flow and migrate sub-tasks with familiar shapes to cheaper models, keeping frontier only where it uniquely earns its cost. Each downshift emits a validated task-to-cheap-model mapping -- this is the process that *generates* routing-table entries rather than consuming them. Precondition: verification infrastructure (tests, review capacity) must exist before the downshift, or the harvested volume cannot be approved.

**The Advisor-Executor pattern beats single-model defaults.** Pairing Opus as a reasoning-only advisor with Sonnet as the tool-calling executor achieves higher quality at lower cost than either model alone -- SWE-Bench 74.8 vs 72.1 at roughly half the cost. The relationship is dynamic (not one-shot planning) -- the executor consults the advisor when it hits hard decisions.

**Frontier releases compress faster than routing tables update.** Five major model releases in 23 days (March 2026) means routing guidance has a shorter shelf life. The routing *structure* (task-based, not provider-based) remains stable even when specific model recommendations change. Set review cadence by release events, not calendar quarters.

### Prompt Lifecycle

**Prompts are policy artifacts.** Production prompts should carry explicit ROLE, AUTHORITY, CONSTRAINT, and FAILURE SIGNAL properties. They should be versioned with commit messages, diffed like code, and tested with automated validation before deployment. Treating prompts as informal text that lives in chat history is the prompt equivalent of unversioned infrastructure.

**Planning prompts can be extracted and customized.** Proven multi-agent planning pipelines (e.g., Claude Code's 4-agent deep plan: planner, critic, refiner, finalizer) can be reverse-engineered and run as deterministic custom skills, bypassing vendor A/B randomization and enabling domain-specific critic criteria.

**Metaprompting closes the prompt-improvement loop.** Using an LLM to generate, test, and iteratively improve the prompts that other LLMs execute transforms prompt optimization from one-time authoring to continuous engineering. The Karpathy autoresearch pattern extends this by closing the loop autonomously: a meta-prompt generates a candidate prompt, that prompt is executed and tested against acceptance criteria, results are fed back to the meta-prompt, and the cycle repeats until criteria are met. The critical safeguard: acceptance criteria must resist proxy-metric gaming, or the loop converges on metric-satisfying outputs rather than genuinely useful ones. A prompt-evaluator chained ahead of a prompt-enhancer in an automated loop -- with explicit, machine-checkable acceptance criteria -- is the minimum viable implementation.

---

## Procedure

### Step 1: Audit Prompts Against the Three Durability Properties

For every prompt in your system, apply three binary tests:

| Property | Test Question | If Failing |
|----------|--------------|------------|
| **Goal-oriented** | Does it say *what* to produce, or does it prescribe *how* to think? | Remove reasoning scaffolding. State the deliverable, constraints, and context only. |
| **Human judgment first** | Does it require human decisions (priorities, trade-offs, curated evidence) *before* generation? | Front-load constraints and choices into the prompt. Do not hope the model infers intent. |
| **Human-side evaluation** | Does it keep evaluation on the human side, or delegate self-assessment to the model? | Replace "verify your answer" with external acceptance criteria or a separate evaluator. |

**Techniques that satisfy all three:** structured output formats, constraint specification, role/persona assignment, context curation, negative behavioral constraints, declarative goal statements with acceptance criteria.

**Techniques that violate at least one (avoid on reasoning models):** chain-of-thought, few-shot reasoning examples, self-consistency, least-to-most decomposition, skeleton-of-thought, "check your work."

### Step 2: Remove Reasoning Anti-Patterns and Rewrite as Declarative Goal + Constraints + Context

| Anti-Pattern | Replacement |
|-------------|-------------|
| "Think step by step" | Remove entirely -- reasoning models do this internally |
| Few-shot reasoning examples | Provide output format examples only, not reasoning chains |
| "First analyze X, then consider Y, then decide Z" | "Produce a decision on Z considering X and Y" |
| "Break this into sub-problems" | State the goal; let the model decompose |
| "Check your work and verify" | Use external verification (tests, assertions, independent evaluator) |
| Step-by-step procedural skill instructions | Rewrite as outcome specifications: "ensure X is true" not "do step 1, step 2" |
| "Add a button in the top-right that opens a modal with 5 icons" | "The user must be able to select an icon for each agent" -- define done, let the agent explore |

**Prefer the declarative form.** State what done looks like, not the path: the model loops until it meets the goal, adapts when a prescribed approach would have failed, and often finds a better implementation than the one you would have prescribed. Strengthen it with verifiable acceptance criteria ("Done when: user can click any agent card and change its icon; change persists across reload") so the loop has an exit condition. Where you have hard requirements (accessibility, budget, UX conventions), use the hybrid: declarative goal plus explicit constraint list.

**Decision: does a human attend the run?**

```
Is a human present who can redirect mid-run?
├── YES (interactive session, supervised agent)
│   └── Declarative prompt: goal + constraints + context.
│       Let the model choose the path; steer live if needed.
└── NO (scheduled routine, cloud automation, unattended pipeline)
    └── SOP prompt: numbered steps, named data sources
        ("use the provided Gmail connector", not "check my email"),
        explicit completion signal, narrow scope, inline edge-case
        handling ("if no unreads exist, send 'No unread emails'").
        Verbosity is safe; under-specification is not.
```

The unattended branch is the one legitimate exception to "define done, not steps": with no human in the loop, ambiguity becomes an uncorrectable error, and the prompt is the complete specification. Tasks requiring judgment mid-flow should stay interactive rather than being force-fit into an SOP.

When removing reasoning scaffolding, compensate with explicit constraints. Under-specifying the goal while also removing process instructions produces worse results than either approach alone.

### Step 3: Engineer Constraints for Reliability

Apply these constraint principles in priority order:

1. **Express high-priority rules as negative constraints.** "Never skip the validation step" is more reliably followed than "always remember to validate." Negative constraints collapse the output space; positive guidance merely nudges within it.

2. **Attach the why to every consequential constraint.** ALL-CAPS MUST/NEVER and rigid structures are yellow flags: reframe with the reasoning ("Never skip the validation step -- the downstream consumer assumes well-formed data") so the model can extend the rule to unanticipated cases and recognize legitimate exceptions. Explain the why of consequential decisions; accept that some details are self-evident (explaining everything is bloat). Do not fabricate a why you don't know -- "we found this works; not sure exactly why" is also useful context.

3. **Add brevity constraints for accuracy.** Include conciseness directives ("be concise, no filler," or explicit length limits) in system prompts. This improves output quality on problems where verbosity causes error accumulation -- not just token savings.

4. **Pair negatives with positive examples.** Each "never do X" should be accompanied by an example of what to do instead, so the model has a viable output path after the constraint removes the undesirable one.

5. **Scope constraints to avoid collateral damage.** "Never use technical jargon" will prevent accurate technical descriptions. Scope: "Never use technical jargon in user-facing summaries."

6. **Constrain the diff, not just the prose.** For code-editing prompts, add the surgical-change constraint: touch only what the task requires; do not refactor unrelated code, remove comments, or reorganize structure outside the task scope. Unrequested changes are a token tax, an unreviewed-diff risk, and compound across sessions into architecture drift.

7. **Add the reuse-before-write ladder to code-generating prompts.** Before writing new code the agent must check, in order: needed at all → exists in codebase → standard library → native platform feature → installable dependency → one-line fix → only then minimal new code. Watch for YAGNI over-application silently dropping needed scope -- the "is it needed" judgment is delegated to the model.

8. **Correct the cost-estimation bias in design prompts.** One standing line wherever agents make design or scoping decisions: "when making technical decisions, don't give too much weight to development cost." Scope it to technical decisions -- it corrects mis-pricing of the better option, not the existence of cost (tokens, review burden, and maintenance are real), and must not leak into human project planning.

9. **Add task-shape heuristics for search.** For agents that use search tools: start with short, broad queries to assess what exists, then progressively narrow. This counters the default LLM behavior of over-specific queries that return nothing.

10. **Add programmatic-extraction rules for code-quoting tasks.** For any prompt that produces output containing code snippets from a codebase (walkthroughs, PR descriptions, documentation), add a grounding constraint: "Use `sed`, `grep`, `cat`, or similar to extract code snippets from source files; do not type code from memory or reconstruct it from understanding."

11. **Watch for diminishing returns.** Beyond a threshold, additional constraints add cognitive load without improving compliance. If a prompt has more than 8-10 hard constraints, prioritize and cut.

### Step 4: Craft Skill Descriptions and Instructions That Trigger and Steer

For prompts packaged as skills or agent instructions, four sub-disciplines:

1. **Structure the description as [What it does] + [When to use it] + [Key capabilities].** The description decides whether the skill fires at all. Include trigger phrases users would naturally say and file types where relevant; add a push against undertriggering ("Make sure to use this skill whenever the user mentions X, Y, Z, even if they don't explicitly ask"). Avoid the three named failure modes: too vague, missing triggers, too technical. Respect validation constraints (kebab-case name matching the folder, no reserved words, description ≤1024 chars, no XML angle brackets).

2. **Write the body as reasoned outcomes, not rigid procedure.** Combine the outcome-based rewrite (Step 2) with why-explanations (Step 3.2). The body should read as a briefing to a smart colleague, not a compliance script.

3. **Choose leading words before writing procedure prose.** Identify the skill's key behavioral demand and express it as one consistent, high-prior-density phrase ("vertical slice," "facts vs decisions"), repeated verbatim throughout. Avoid weak-prior phrases that mean something only to you, and avoid referring to the same behavior with three different phrasings -- lexical discipline is the mechanism.

4. **Verify steering in reasoning traces, then escalate strictness structurally if needed.** Acceptance test: the leading word appears in the agent's own thinking traces. If compliance still fails, do not pile on rules -- strengthen the leading words first. For audit/review skills that must hold an unusually high bar, apply the strictness-escalation stack: numbered non-negotiable standards, per-change review questions, aggressive-flag escalation triggers, preferred remedies, literal example phrases pinning tone, prioritized output ordering with anti-flooding, and an approval bar separating presumptive blockers from waivable concerns.

### Step 5: Structure Prompts with Design/Evaluate Phases and Bidirectional Alignment

Before writing the prompt (Design phase):
- Choose the interpretive lens (role, persona, expertise domain)
- Prioritize trade-offs explicitly (format vs. depth, speed vs. thoroughness)
- Curate what counts as evidence (specific sources, not "use your knowledge")
- Define what a "good enough" output looks like

**For spec creation and complex implementation tasks,** extend the Design phase with bidirectional prompting: dump your initial thoughts, then alternate questions with the model until both parties have no more questions. The model's questions surface implicit assumptions; your counter-questions validate edge-case understanding. The resulting spec and implementation plan (with checkbox bullet points per task) is signed off line by line before implementation begins. This is especially critical for agentic runs where the human is not in the loop during execution.

**For scope-setting moments (new feature, new project), escalate to Socratic discovery.** Before any spec exists, have the agent interrogate the request rather than accept it: force the smallest deployable slice; ask for behavioral evidence ("have you watched users without helping them? what surprised you?"); project the feature forward ("if models get cheaper and competitors copy this, does it become more or less central?"); then surface 5-6 explicit premises derived from the session and demand agree/disagree on each before proceeding. Optionally add a fresh-context second opinion: a sub-agent with no conversation history reviews the problem statement, answers, and premises to produce an independent verdict. Budget for it deliberately -- structured discovery is token-expensive and teams shortcut it under time pressure, which is exactly when its premise-catch value is highest.

After receiving the output (Evaluate phase):
- Does the model's strategic frame match yours?
- Did it stay grounded in the evidence you provided?
- Is the synthesis genuine or a false compromise?
- Would a different lens have produced a better result?

This is not a one-time checklist -- it is the cognitive discipline that makes prompting work across model boundaries.

### Step 6: Assemble System Prompts in Ordered Layers with Cache-Aware Segmentation

For multi-turn agent applications, structure the system prompt as seven ordered layers and manage the cache boundary explicitly:

| Layer | Content | Stability | Cache? |
|-------|---------|-----------|--------|
| 1 | Core role / persona | Immutable | Yes |
| 2 | Values / SOUL.md | Immutable | Yes |
| 3 | Persistent memory / user profile | Changes infrequently | Yes |
| 4 | Skills metadata | Changes infrequently | Yes |
| 5 | Project context | Changes per project | Yes |
| 6 | Provider-specific instructions | Rarely changes | Yes |
| 7 | Ephemeral state (current task, session vars) | Changes every turn | No -- inject as separate block |

**Assembly rule:** Build layers 1-6 in a dedicated assembly module that attaches `cache_control` markers at each stable boundary. Inject layer 7 as a separate content block -- never inline it into the cached portion. This prevents ephemeral content from invalidating the cache for the stable layers above it.

**Caching pitfalls:**
- *Over-caching:* Including fast-changing context in the cached portion causes stale context to persist across turns. If the model is acting on outdated information, check whether project context or session state has migrated up into a cached layer.
- *Under-caching:* Not marking stable layers means you pay full token cost on every turn. Apply cache markers to every layer that does not change between turns.
- *TTL mismatch:* Anthropic's cache TTL is 5 minutes. If turns are more than 5 minutes apart (e.g., overnight sessions, batch pipelines), the cache expires between turns and the benefit disappears. This pattern is most valuable for interactive agent loops with rapid turn cycles.

**When NOT to use:** One-shot API calls, batch pipelines with long inter-call gaps, or prompts short enough that caching overhead exceeds savings.

### Step 7: Define Explicit Output Format Controls

For interactive agent sessions, define named format commands that users can invoke to override the model's default output style:

| Command | Behavior | Use Case |
|---------|----------|----------|
| `*brief` | Bullet points only, no prose | Quick status checks, summaries |
| `*dev` | Code over explanation -- show the fix, do not describe it | Mid-session debugging |
| `*plan` | Explicit step-by-step structured output | Architecture planning, task decomposition |
| `*verbose` | Full explanation with rationale | Learning, onboarding, review |

**Design principle:** Domains (loaded context, project type) set autopilot defaults for format; star commands give the user manual override. This separates the concern of "what format should be default" from "what format does the user need right now."

**Implementation:** Define the commands in the system prompt or manifest with their mappings. The model applies the format for the duration of the response. If no command is given, the domain default applies.

**When NOT to use:** Non-interactive contexts (batch pipelines, one-shot API calls) where there is no user in the loop to invoke overrides.

### Step 8: Classify the Task, Route the Model, Tune the Effort

**8a. Classify center vs edge of distribution first.** Before consulting any routing table, ask: has this task shape been tried millions of times before, and can a human inspect the output quickly? If yes (center), route to the cheap tier by default -- frontier buys no quality premium there (quantified anchor: on ordinary feature work, a <$1 open model, a ~$1.50 mid model, and a $9 frontier model produced equally acceptable output). If the task is novel in shape, hard to inspect, or beyond prior example density (edge), frontier spend pays -- on a genuinely hard systems-code task, only the frontier model could touch it. Beware misclassification: familiar-looking tasks with hidden edge complexity fail silently on cheap models, and the line moves every model generation.

**8b. Route by task type.**

| Task Type | Recommended Model | Evidence | Relative Cost |
|-----------|------------------|----------|---------------|
| Repository-level coding, knowledge work | Claude Sonnet 4.6 | GDPval Elo 1633, SWE-bench ~79.6% | 1x |
| Complex reasoning, architectural decisions | Claude Opus 4.6 (via Advisor pattern) | SWE-Bench 74.8 with advisor vs 72.1 alone | ~0.5x (advisor) |
| Computer use, browser automation | GPT-5.4 | WebArena-Verified 67.3% | ~1.2x |
| Abstract reasoning, long-horizon math | Gemini 3.1 Pro | ARC-AGI-2 77.1% | ~1.5x |
| Extraction, batch processing | Gemini Flash | 97.1% quality, $0.003/task | ~0.1x |

**Anti-default:** Opus 4.6 costs 3.5x Sonnet with no accuracy premium on most benchmarks. Do not default to it.

**8c. Tune effort before switching tiers.** Within a frontier model, the effort dial is a first-order cost lever: low effort on the frontier tier can match or beat the previous tier at max effort for a fraction of the price (60% pass at $3.76/task vs 59% at $13/task in the quantified case), and the top of the curve is flat (extra-high → max: ~nothing gained for 2-4x cost). Default effort (high) is wrong for most tasks. Match effort to task complexity; use low/medium for center-of-distribution work; reserve high/max for long-horizon-complex tasks where the ~10-point pass-rate spread is exactly the margin that matters. Effort settings and prices go stale quickly -- keep the numbers in a registry, not in prose.

**Hard ceiling reminder:** All frontier models score 0% on ARC-AGI-3 (novel abstraction). For tasks requiring genuinely novel inductive generalization, route to human judgment, not a more powerful model.

**Review cadence:** Re-evaluate when any constituent model has a major release. The routing structure (task-based) is durable; the specific model assignments are snapshots.

### Step 9: Bind Model Choice at Dispatch and Session Boundaries

Model routing plans fail silently at the two places the decision actually binds. Enforce both:

1. **Name a model on every subagent dispatch.** An unspecified model inherits the session's model -- usually the most expensive -- and nothing surfaces the cost until the bill (observed incident: all 26 reviewers in one fan-out on the top tier). Make the model parameter mandatory in every dispatch template, with tier heuristics to fill it:
   - Task complexity maps to tier: boilerplate implementation down-tier; judgment-heavy review up-tier.
   - **Turn count beats token price:** cheap models take 2-3x the turns on multi-step work and cost more end-to-end. Down-tier on total cost, not per-token price.
   - Review models scale with diff size and risk; pin exactly one dispatch -- the final whole-scope review -- to the most capable model.
   - Audit tier *distribution*, not field presence: always naming the default model is compliance theater.

2. **Pin the model per session; delegate to switch.** Prompt caches are model-specific -- switching mid-session re-processes the entire accumulated context at the new model's full input price, frequently costing more than staying put. For a cheap stretch of work, spawn a subagent on the cheaper model with an explicit hand-off message instead of downshifting the parent. The hand-off message is load-bearing: a thin hand-off produces wrong work at any price. Exceptions: very short sessions with little accumulated context, where a direct switch may genuinely be cheaper than orchestration overhead.

3. **Run the frontier-prototype-then-downshift lifecycle for new task classes.** First instance of a new task class runs on the frontier tier at whatever effort it needs -- the frontier model's job is doing the whole thing at once and proving the flow. Then decompose: sub-tasks with familiar shapes migrate to cheaper models, validated against the frontier-built reference output. Record each clean downshift as a routing datapoint (this is where routing-table entries come from). Do not downshift before verification infrastructure exists, and do not downshift a task class whose edge cases the frontier model was silently absorbing.

### Step 10: Implement the Advisor-Executor Pattern (API Applications)

For API-based applications where quality matters but Opus for everything is too expensive:

```
[Executor: Sonnet]        [Advisor: Opus]
  handles all tools    <->  reasoning guidance only
  most decisions            consulted at decision points
  $0.96/task average        full shared context
                            never makes tool calls
```

**Configuration:** Set `type: "advisor"` and `max_uses` in API calls. The executor consults the advisor when it hits a decision it cannot resolve.

**Tuning max_uses:**
- Start with 3-5 for general tasks
- Too low: executor makes avoidable mistakes at decision points
- Too high: unnecessary advisor calls increase cost without quality gain
- Monitor consultation logs to find the right level per task type

**When NOT to use:** Claude Code sessions (not API-based), tasks that are entirely routine (Sonnet alone is sufficient), tasks requiring primarily tool calls with no reasoning decisions.

### Step 11: Version and Test Prompts as Policy

Treat production prompts as versioned artifacts:

1. **Structure prompts with explicit properties:** ROLE (who the agent is), AUTHORITY (what it can do), CONSTRAINT (what it must not do), FAILURE SIGNAL (how to detect and report failure).

2. **Version with diffs:** Store prompts in version control. Write commit messages that explain *why* the prompt changed, not just *what* changed.

3. **Test before deployment:** Define acceptance criteria for each prompt. After a model upgrade, run the prompt against the acceptance criteria before deploying to production. For skills, include the steering check: do the leading words still echo in reasoning traces on the new model? (Leading-word strength is model-family-dependent.)

4. **Extract and customize proven pipelines:** When a vendor feature (like a planning mode) produces good results, extract the underlying prompt as a custom skill so you get deterministic access to the best variant and can add domain-specific criteria.

### Step 12: Apply Metaprompting for Continuous Prompt Improvement

When a prompt is critical enough to justify optimization beyond hand-tuning:

1. **Define machine-checkable acceptance criteria.** Before entering the metaprompt loop, write criteria that test the prompt's actual output quality -- not proxy metrics the loop can game. Examples: "output parses as valid YAML," "all referenced files exist," "no hallucinated function signatures."

2. **Generate candidate prompts with a meta-prompt.** Use an LLM to produce or refine the target prompt. The meta-prompt receives the acceptance criteria and any failure cases from previous iterations.

3. **Execute and evaluate.** Run the candidate prompt against test inputs. Score against the acceptance criteria.

4. **Iterate or accept.** Feed failures back to the meta-prompt for another round. Stop when criteria are met or improvement plateaus.

**Minimum viable implementation:** Chain a prompt-evaluator ahead of a prompt-enhancer, with the evaluator's output feeding the enhancer's next iteration. This is the manual version; full automation closes the loop without human intervention per cycle.

**When NOT to use:** Prompts that are used infrequently (the optimization cost exceeds the benefit), or prompts where acceptance criteria cannot be made machine-checkable (the loop cannot converge).

---

## Templates

### Template 1: Model-Resilient Prompt Structure

```markdown
## {{PROMPT_NAME}}

### Role
You are {{ROLE_DESCRIPTION}}.

### Authority
You may {{PERMITTED_ACTIONS}}.
You must not {{PROHIBITED_ACTIONS}}.

### Goal
Produce {{DELIVERABLE_DESCRIPTION}} that satisfies:
- {{CONSTRAINT_1}}
- {{CONSTRAINT_2}}
- {{CONSTRAINT_3}}

### Context
{{CURATED_CONTEXT — specific sources, files, or evidence the model should use}}

### Output Format
{{FORMAT_SPECIFICATION — structure, length, sections}}

### Grounding Rules
- Use `sed`, `grep`, `cat`, or equivalent to extract code snippets from source files. Do not type code from memory or reconstruct from understanding.
- {{ADDITIONAL_GROUNDING_RULES — e.g., "cite file:line for every claim about code behavior"}}

### Failure Signal
If {{FAILURE_CONDITION}}, then {{FAILURE_ACTION — stop, escalate, report}}.
```

#### Worked Example: Research Extraction Prompt

```markdown
## Extract Research Findings

### Role
You are a research analyst extracting actionable patterns from technical sources.

### Authority
You may create new finding entries in the research-findings directory.
You must not modify existing findings, source files, or governance documents.

### Goal
Produce a structured finding entry for each distinct pattern in the source that satisfies:
- Each finding describes a single, testable pattern (not a vague observation)
- Evidence strength is assessed as Strong/Medium/Weak with justification
- Implementation notes are specific enough for a developer to act on without re-reading the source
- No duplicate of an existing KB finding (check first)

### Context
Source transcript: {{SOURCE_PATH}}
Existing findings directory: systems/improvement-loop/research-findings/ (filter with ripgrep on frontmatter `category:` / `dimension:`)

### Output Format
YAML frontmatter per _schema.yaml, followed by markdown body with sections:
What It Is, Why It Matters, Why People Are Using It, Potential Failure Modes.

### Grounding Rules
- Use `sed`, `grep`, `cat`, or equivalent to extract code snippets from source files.
  Do not type code from memory or reconstruct from understanding.

### Failure Signal
If the source contains fewer than 2 extractable patterns, report "low-density source"
and stop. Do not generate filler findings.
```

### Template 2: Prompt Audit Worksheet

```markdown
## Prompt Audit — {{SYSTEM_NAME}}
Date: {{AUDIT_DATE}}
Auditor: {{AUDITOR}}
Trigger: {{MODEL_UPGRADE / SCHEDULED_REVIEW / QUALITY_INCIDENT}}

### Durability Property Check
| Prompt Location | Goal-oriented (P1) | Human Judgment First (P2) | Human-side Eval (P3) | Action |
|----------------|---------------------|---------------------------|----------------------|--------|
| {{PROMPT_PATH}} | {{PASS/FAIL: detail}} | {{PASS/FAIL: detail}} | {{PASS/FAIL: detail}} | {{REMOVE/REWRITE/OK}} |

### Anti-Pattern Scan
| Location | Anti-Pattern | Current Text | Replacement |
|----------|-------------|-------------|-------------|
| {{PATH:LINE}} | {{CoT/few-shot/self-verify/decomposition/skeleton}} | "{{CURRENT_TEXT}}" | "{{REPLACEMENT_TEXT}}" |

### Constraint Quality Check
| Constraint | Type (neg/pos) | Why attached? | Scoped? | Collateral risk? | Action |
|-----------|----------------|---------------|---------|-------------------|--------|
| {{CONSTRAINT_TEXT}} | {{negative/positive}} | {{yes/no — reasoning present}} | {{yes/no — scope described}} | {{risk if any}} | {{CONVERT_TO_NEGATIVE / ADD_WHY / ADD_SCOPE / OK}} |

### Instruction Craft Check (skills/agents)
| Skill | Description = what+when+capabilities? | ALL-CAPS/rigid-structure yellow flags? | Leading words consistent? | Trace echo verified? | Action |
|-------|---------------------------------------|----------------------------------------|---------------------------|----------------------|--------|
| {{SKILL_PATH}} | {{yes/no}} | {{count/none}} | {{yes/no/n-a}} | {{yes/no/n-a}} | {{FIX_DESCRIPTION / ADD_WHY / UNIFY_LEADING_WORDS / OK}} |

### Grounding Check
| Prompt | Produces code snippets? | Programmatic extraction rule present? | Action |
|--------|------------------------|---------------------------------------|--------|
| {{PROMPT_PATH}} | {{yes/no}} | {{yes/no}} | {{ADD_RULE / OK / N/A}} |

### Output Format Control
| Prompt | Format overrides defined? | Override mechanism | Action |
|--------|--------------------------|-------------------|--------|
| {{PROMPT_PATH}} | {{yes/no}} | {{star commands / inline / none}} | {{ADD_OVERRIDES / OK / N/A}} |

### Model Routing
| Agent Role | Task Class (center/edge) | Current Model + Effort | Recommended Model + Effort | Rationale |
|-----------|--------------------------|------------------------|----------------------------|-----------|
| {{ROLE}} | {{center/edge}} | {{CURRENT}} | {{RECOMMENDED}} | {{BENCHMARK_EVIDENCE / downshift record}} |

### Dispatch Discipline
| Dispatch Site | Model named explicitly? | Tier justified (turn-count aware)? | Action |
|---------------|-------------------------|-------------------------------------|--------|
| {{DISPATCH_PATH}} | {{yes/no}} | {{yes/no}} | {{ADD_MODEL / RETIER / OK}} |

### Prompt Policy Properties
| Prompt | ROLE defined? | AUTHORITY defined? | CONSTRAINTS defined? | FAILURE SIGNAL defined? |
|--------|--------------|-------------------|---------------------|------------------------|
| {{PROMPT_PATH}} | {{yes/no}} | {{yes/no}} | {{yes/no}} | {{yes/no}} |
```

#### Worked Example: MetaSystem Prompt Audit

```
Prompt Audit — MetaSystem Skills
Date: 2026-04-19
Auditor: Claude (session 26)
Trigger: P2 finding integration

DURABILITY PROPERTY CHECK:
/synthesize-guide:
  P1 (goal-oriented): PASS — "Synthesize findings into guide" (goal, not process)
  P2 (human judgment first): PASS — findings pre-curated by human
  P3 (human-side eval): PASS — human reviews draft before deployment

/identify-artifacts (subagent prompt):
  P1: PASS — "Classify this finding into a form" (goal-oriented after session 24 fix)
  P2: PASS — rubric front-loaded as context
  P3: PASS — human reviews identification report

ANTI-PATTERN SCAN: None found after session 24 prompt improvement.

CONSTRAINT QUALITY CHECK:
  "Be concise" in CLAUDE.md: positive, unscoped — CONVERT to
    "Do not include filler phrases, hedging language, or restated instructions in output"
  "Never skip the Review Gate": negative, scoped, no why — ADD WHY
    ("— deployment without review violates DD-29's human-gate invariant")

INSTRUCTION CRAFT CHECK:
  /identify-artifacts: description has what+when, missing key capabilities — FIX DESCRIPTION
  /extract-artifacts: two ALL-CAPS NEVERs without reasoning — ADD WHY
  /synthesize-guide: core demand phrased 3 ways ("synthesize"/"unify"/"merge") —
    UNIFY LEADING WORDS on "synthesize, never compile"; verify echo in traces

GROUNDING CHECK:
  /synthesize-guide: Does not produce code snippets — N/A
  Walkthrough-generating skills: Produces code snippets, no extraction rule — ADD RULE

MODEL ROUTING:
  Orchestrator: Opus — justified (edge-class architectural decisions, low volume)
  Subagents: Sonnet — justified (center-class batch classification, parallel)
  Effort: default high on batch classification — RETIER to medium

DISPATCH DISCIPLINE:
  /identify-artifacts fan-out: model not named per dispatch — ADD_MODEL
    (silent inheritance risk: subagents would inherit the session's Opus)

PROMPT POLICY PROPERTIES:
  /synthesize-guide: ROLE yes, AUTHORITY partial (no explicit prohibitions),
    CONSTRAINTS yes, FAILURE SIGNAL no — ADD failure signal for low-finding-count edge case
```

### Template 3: Outcome-Based Skill Rewrite

```markdown
## {{SKILL_NAME}} — Outcome Specification

### Outcomes (what must be true when the skill completes)
1. {{OUTCOME_1 — a verifiable end-state, not a step}}
2. {{OUTCOME_2}}
3. {{OUTCOME_3}}

### Constraints (boundaries, not process — each with its why)
- {{CONSTRAINT_1 — "never," "must not," or "must" + "— because {{REASONING}}"}}
- {{CONSTRAINT_2}}

### Context (what the skill needs to work with)
- {{CONTEXT_ITEM_1 — file, schema, or reference}}
- {{CONTEXT_ITEM_2}}

### Acceptance Criteria
- [ ] {{CRITERION_1 — binary testable}}
- [ ] {{CRITERION_2}}

### Failure Signal
If {{CONDITION}}, then {{ACTION}}.
```

#### Worked Example: Rewriting a Procedural Skill

**Before (procedural, 180 tokens):**
```
Step 1: Read the source transcript.
Step 2: Identify each distinct pattern.
Step 3: For each pattern, check the existing KB for duplicates.
Step 4: For each non-duplicate pattern, write a finding entry.
Step 5: Use the _schema.yaml for frontmatter format.
Step 6: Include all required sections.
Step 7: Save to research-findings/ directory.
Step 8: Report what was extracted.
```

**After (outcome-based, 90 tokens):**
```
Outcomes:
1. Every distinct, non-duplicate pattern in the source has a finding entry
   in research-findings/.
2. Each entry conforms to _schema.yaml frontmatter and includes all
   required sections.
3. Extraction report summarizes what was created and any duplicates skipped.

Constraints:
- Never create a finding that duplicates an existing KB entry — duplicate
  entries fork the citation graph and double maintenance.
- Never modify existing findings or source files.

Failure Signal:
If fewer than 2 patterns found, report "low-density source" and stop.
```

### Template 4: YAML Template with Dual Structure (Schema + Coaching)

```yaml
# {{TEMPLATE_NAME}}
# This template defines both the output structure and the interaction protocol.

sections:
  - name: "{{SECTION_1_NAME}}"
    schema:
      required_fields:
        - "{{FIELD_1}}"
        - "{{FIELD_2}}"
    coaching: |
      {{INSTRUCTION_FOR_LLM — what questions to ask the user for this section,
       what level of detail to push for, when this section is "done enough"}}

  - name: "{{SECTION_2_NAME}}"
    schema:
      required_fields:
        - "{{FIELD_3}}"
    coaching: |
      {{INSTRUCTION_FOR_LLM — elicitation guidance for this section}}

quality_gate: |
  {{CRITERIA_FOR_WHEN_THE_TEMPLATE_IS_COMPLETE — e.g., "all required fields
   populated, no placeholder text remaining, user has confirmed priorities"}}
```

#### Worked Example: PRD Template with Coaching

```yaml
# Product Requirements Document
# Defines PRD structure + tells the agent how to elicit each section.

sections:
  - name: "Problem Statement"
    schema:
      required_fields:
        - "user_pain_point"
        - "current_workaround"
        - "impact_if_unsolved"
    coaching: |
      Ask: "What specific problem does the user face today?"
      Push for: A concrete scenario, not an abstract description.
      Move on when: The user has described the pain in terms of
      observable behavior, not feelings.

  - name: "Success Criteria"
    schema:
      required_fields:
        - "metric"
        - "target_value"
        - "measurement_method"
    coaching: |
      Ask: "How will you know this is working?"
      Push for: A number, not a qualitative statement.
      Move on when: At least one metric has a target value
      and a measurement method.

quality_gate: |
  All required fields populated. Problem statement describes
  observable behavior. At least one success metric has a numeric target.
```

### Template 5: Bidirectional Prompting Protocol

```markdown
## {{TASK_NAME}} — Spec Alignment

### Phase 0 (optional, scope-setting): Socratic Discovery
- Smallest deployable slice: {{WEDGE — the single feature a real user will
  use this week; reject multi-feature scope}}
- Behavioral evidence: {{OBSERVED_USAGE — what users actually did, not what
  they said they want}}
- Premise challenge: {{5-6 EXPLICIT PREMISES — each marked agree/disagree
  by the human before proceeding}}
- Fresh-context second opinion: {{INDEPENDENT_VERDICT — sub-agent with no
  conversation history reviews problem, answers, premises}}

### Phase 1: Initial Dump
{{USER_INTENT — unstructured description of what you want built, including
known constraints, architecture preferences, and non-obvious requirements}}

### Phase 2: Model Questions
The model asks targeted questions to surface implicit assumptions.
Do not proceed until you have answered all questions.

### Phase 3: Human Counter-Questions
Ask the model to confirm its understanding of:
- {{EDGE_CASE_1 — boundary condition the model might mishandle}}
- {{EDGE_CASE_2}}
- {{ARCHITECTURE_CONSTRAINT — e.g., "this must work without network access"}}

### Phase 4: Alignment Check
Both parties confirm: no more questions.

### Phase 5: Implementation Plan
Structured checklist with checkbox bullet points per task.
Human signs off line by line before implementation begins.

### Failure Signal
If the implementation plan exceeds {{MAX_CONTEXT_TOKENS}} tokens,
decompose into sub-plans before proceeding.
```

### Template 6: Metaprompt Loop

```markdown
## {{TARGET_PROMPT_NAME}} — Metaprompt Optimization

### Acceptance Criteria (machine-checkable)
- [ ] {{CRITERION_1 — e.g., "output parses as valid YAML"}}
- [ ] {{CRITERION_2 — e.g., "no hallucinated function signatures"}}
- [ ] {{CRITERION_3 — e.g., "all referenced files exist in the repo"}}

### Test Inputs
- {{TEST_INPUT_1 — representative input for the target prompt}}
- {{TEST_INPUT_2 — edge case input}}

### Meta-Prompt
Generate a prompt for {{TARGET_TASK}} that, when executed against the test
inputs above, satisfies all acceptance criteria. If previous iterations
failed, the failure cases are:
{{FAILURE_CASES — empty on first iteration, populated on subsequent}}

### Iteration Log
| Round | Criteria Met | Criteria Failed | Change Made |
|-------|-------------|-----------------|-------------|
| {{N}} | {{PASSING}} | {{FAILING}} | {{DELTA}} |

### Stop Condition
Accept when all criteria pass, or stop after {{MAX_ROUNDS}} rounds
if improvement has plateaued (last 2 rounds produced no new passes).
```

### Template 7: Skill Description (What + When + Capabilities)

| Variable | Type | Description | Required |
|----------|------|-------------|----------|
| `WHAT_IT_DOES` | string | One sentence, concrete verb + object — what the skill produces or performs | yes |
| `WHEN_TO_USE` | string | Trigger conditions phrased as the user would say them; file types if relevant | yes |
| `KEY_CAPABILITIES` | string | 2-4 specific capabilities — extra keywords for varied user phrasing | yes |
| `PUSH_CLAUSE` | string | Anti-undertriggering nudge ("Make sure to use this skill whenever...") | optional |

```markdown
description: >-
  {{WHAT_IT_DOES}}. Use when {{WHEN_TO_USE}}. {{KEY_CAPABILITIES}}.
  {{PUSH_CLAUSE — "Make sure to use this skill whenever the user mentions
  X, Y, or Z, even if they don't explicitly ask."}}
```

Validation constraints: name kebab-case matching the folder; no reserved words (`claude`, `anthropic`); description ≤1024 chars; no XML angle brackets; must include both what and when.

#### Worked Example: Transcript Fetcher Skill

```markdown
description: >-
  Fetches YouTube video transcripts as full-text markdown files for research
  extraction. Use when the user provides YouTube URLs and wants transcripts,
  or when a research pass needs full transcript text for a video source.
  Handles caption-blocked videos via fallback API, batch URL lists, and
  cache-aware refetching. Make sure to use this skill whenever the user
  mentions "transcript", "captions", or pastes a youtube.com/watch URL,
  even if they don't explicitly ask to fetch it.
```

Anti-examples (the three named failure modes): "Helps with videos" (too vague); "Creates sophisticated multi-source transcript archives" (missing triggers); "Implements the caption-retrieval fallback chain with IP-block detection" (too technical, no user phrasing).

### Template 8: Model Dispatch and Effort Policy

| Variable | Type | Description | Required |
|----------|------|-------------|----------|
| `TASK_CLASS` | string | The task family this row governs | yes |
| `DISTRIBUTION` | enum | `center` / `edge` — classification per Step 8a | yes |
| `MODEL` | string | Explicit model for this dispatch — never blank | yes |
| `EFFORT` | enum | `low` / `medium` / `high` / `max` | yes |
| `RATIONALE` | string | Benchmark row, downshift record, or turn-count justification | yes |

```markdown
## Model Dispatch Policy — {{SYSTEM_NAME}}

Session model (pinned; never switched mid-session — delegate instead): {{SESSION_MODEL}}

| Dispatch Site | Task Class | Distribution | Model | Effort | Rationale |
|---------------|-----------|--------------|-------|--------|-----------|
| {{DISPATCH_1}} | {{TASK_CLASS}} | {{center/edge}} | {{MODEL}} | {{EFFORT}} | {{RATIONALE}} |
| {{DISPATCH_2}} | {{TASK_CLASS}} | {{center/edge}} | {{MODEL}} | {{EFFORT}} | {{RATIONALE}} |
| final whole-scope review | review | edge | {{MOST_CAPABLE_MODEL}} | high | breadth concentrated by design |

Rules:
- No dispatch without an explicit model ({{ENFORCEMENT — template lint / harness rejection}}).
- Down-tier on end-to-end cost: turn count beats token price on multi-step work.
- New task classes prototype on {{FRONTIER_MODEL}} first; downshifts are recorded below.

### Downshift Log (routing datapoints)
| Date | Sub-task | From → To | Validated against | Result |
|------|----------|-----------|-------------------|--------|
| {{DATE}} | {{SUBTASK}} | {{FRONTIER}} → {{CHEAP}} | {{REFERENCE_OUTPUT}} | {{clean/reverted}} |
```

#### Worked Example: Research Pipeline Fan-Out

```markdown
## Model Dispatch Policy — IL Research Pipeline

Session model (pinned): Opus (orchestrator; architectural judgment)

| Dispatch Site | Task Class | Distribution | Model | Effort | Rationale |
|---------------|-----------|--------------|-------|--------|-----------|
| finding classification fan-out | batch classification | center | Sonnet | medium | center-class; 67% accuracy validated session 24; high effort added nothing |
| transcript summarization | extraction | center | Haiku | low | single-turn per item; turn-count risk absent |
| identification-report review | judgment review | edge | Opus | high | final whole-scope review; pinned to most capable |

Rules:
- No dispatch without an explicit model (dispatch template lint).
- Batch items are single-turn: token price dominates, Haiku safe.
  Multi-step extraction stays on Sonnet — Haiku took 2-3x turns in trial.
- New task classes prototype on Opus first; downshifts recorded below.

### Downshift Log
| Date | Sub-task | From → To | Validated against | Result |
|------|----------|-----------|-------------------|--------|
| 2026-05-02 | transcript summarization | Opus → Haiku | session-24 reference set | clean |
| 2026-05-02 | crosslink detection | Opus → Sonnet | 50-pair golden set | clean |
```

---

## Pitfalls

### 1. Removing reasoning scaffolding without adding constraints
Stripping "think step by step" and few-shot examples is correct for reasoning models, but if you also remove the implicit structure those techniques provided, the model has less guidance than before. Compensate: specify the goal precisely, add explicit constraints, and define the output format. The replacement pattern is Goal + Constraints + Context, not just Goal.

### 2. Over-constraining with negatives
Negative constraints are powerful, but too many create contradictions. If the model cannot satisfy all constraints simultaneously, behavior becomes unpredictable as it attempts partial compliance. Keep hard negative constraints to the highest-priority rules (5-8 maximum) and use positive guidance for preferences.

### 3. Defaulting to the most expensive model
Opus 4.6 costs 3.5x Sonnet with no accuracy premium on most benchmarks. The Advisor-Executor pattern achieves higher quality at lower cost than Opus alone. Route bulk work to Sonnet or cheaper models. "Use Opus for everything" is a cost mistake, not a quality strategy.

### 4. Provider-based model selection
"We're a Claude shop" is not a routing strategy. Different models excel at different tasks. The March 2026 release compression (5 launches in 23 days) means the competitive landscape shifts monthly. Route by task characteristics, re-evaluate at each major release.

### 5. Treating CoT as a universal amplifier
Chain-of-thought amplifies reasoning within the model's training distribution but adds nothing for tasks requiring genuinely novel abstraction (ARC-AGI-3: all models 0%). For novel-abstraction tasks, route to human judgment rather than throwing more thinking tokens at the problem.

### 6. Applying brevity constraints to planning tasks
Brevity improves accuracy on many problem types, but complex multi-step planning genuinely benefits from elaboration. Use dynamic brevity: verbose for planning and analysis, terse for execution and output. Do not apply a blanket conciseness constraint to every prompt.

### 7. Elicitation technique overload
Eighteen advanced elicitation techniques and twelve mental-model commands exist, but applying multiple techniques to every prompt wastes tokens and produces analysis paralysis. Select 1-2 based on task type. Critique-and-refine for design work. Red team/blue team for security reviews. Inversion or via-negativa for de-risking decisions. Not all of them, not all the time.

### 8. Unversioned prompt changes
Changing a production prompt without versioning, testing, or rollback capability is the prompt equivalent of pushing untested code to production. Treat prompt changes like policy changes: diff, test against acceptance criteria, deploy with rollback.

### 9. Conflating prompt structure boundaries with cache boundaries
The logical layers of a prompt (persona, memory, skills, context) and the cache boundaries (which portions share a cache key) are independent concerns. Inlining ephemeral turn state into a stable cached layer forces a cache miss on every turn, erasing the caching benefit. Conversely, placing slowly-changing context outside the cache means paying full token cost every turn. Keep the assembly module responsible for drawing cache boundaries; keep prompt structure logic separate.

### 10. Letting the model reconstruct code snippets from memory
When an agent produces walkthroughs, PR descriptions, or documentation that quotes code, it will by default reconstruct snippets from its working understanding of the file rather than reading the actual bytes. This introduces two failure modes: direct hallucination (quoting code that does not exist) and stale mental model (quoting code as it was before a recent edit). Add a programmatic-extraction rule to the prompt. Over-application to trivial references (e.g., a built-in function name) wastes tool calls, so scope the rule to project-specific code, not language primitives.

### 11. Skipping the bidirectional prompting phase for complex specs
Dumping a spec and immediately starting implementation is faster, but implicit assumptions filled from training data are the root cause of most cascading bugs in long agentic runs. The cost of bidirectional prompting (several minutes of Q&A) is small compared to the cost of unwinding a 30-step implementation built on a misunderstood requirement. The adoption friction is real -- most developers skip after a few exchanges -- but the payoff scales with project complexity.

### 12. Metaprompt loops that optimize for proxy metrics
When using an LLM to improve prompts for other LLMs, the acceptance criteria determine whether the loop converges on genuinely useful outputs or on metric-satisfying artifacts. Criteria like "output is longer than 500 words" or "uses at least 3 headers" are gameable. Criteria like "output parses as valid YAML" or "all referenced files exist" are not. Design acceptance criteria that test the actual quality you care about, not surface features the loop can learn to produce.

### 13. Bludgeoning with ALL-CAPS MUSTs instead of explaining why
Prescriptive rules without reasoning produce brittle compliance: the model follows the letter where the rule fits and fails to extend the spirit where it doesn't. ALL-CAPS ALWAYS/NEVER and rigid structures are yellow flags -- reframe with the why. Two caveats: explaining every micro-decision is bloat (explain consequential constraints), and a wrong why is worse than none (the model now extends an incorrect framework).

### 14. Diffuse steering instead of consistent leading words
Referring to the same behavioral demand with three different phrasings dilutes the prior-invocation effect; a phrase with meaning only to the author ("do it the Acme way") has no prior density and steers nothing. Pick one high-prior-density phrase, repeat it verbatim, and verify echo in reasoning traces. Remember trace echo is necessary, not sufficient -- an agent can parrot the phrase while deviating in action, so keep an output-level check too.

### 15. One prompting philosophy for both attended and unattended runs
Declarative define-done prompts are correct for interactive sessions and wrong for scheduled routines, where nobody can redirect mid-run and ambiguity becomes silent failure (the wrong email sent, discovered hours later). Conversely, SOP-style over-specification makes interactive prompts brittle and wastes the model's exploration strength. Decide by attendance first; also beware SOPs that assume a specific input format -- the long tail of unexpected inputs still needs inline edge-case handling.

### 16. Switching models mid-session
Prompt caches are model-specific. Dropping a running session from an expensive model to a cheap one for "the easy part" re-processes the entire accumulated context at the new model's full input price -- frequently more expensive than staying put. Pin the model per session; spawn a subagent on the cheaper model with an explicit hand-off message instead. Watch the inverse failure too: over-delegation of trivial subtasks, where orchestration overhead exceeds the model-cost savings.

### 17. Silent model inheritance in fan-outs
A subagent dispatch that does not name a model inherits the session's -- usually the most expensive -- and nothing surfaces the cost until the bill (26 reviewers on the top tier, in the documented incident). Make the model parameter mandatory per dispatch. And avoid cargo-cult down-tiering: without the turn-count heuristic, cheap models thrash through multi-step work at higher total cost. Audit tier distribution, not field presence.

### 18. Leaving effort at the default
Default effort (high) overpays on most tasks: the top of the effort curve is flat (extra-high → max buys ~nothing for 2-4x cost), and low-effort frontier can beat max-effort previous-tier at a fraction of the price. But watch for silent quality erosion on tasks where the ~10-point pass-rate spread between low and high effort is exactly the margin that matters. Effort numbers go stale fast -- keep them in a registry with a refresh owner, not hardcoded in prompts or prose.

### 19. Reading cheap-ties-frontier parity as a fact about models
When a cheap model ties the frontier on your benchmark, that is usually a fact about the *task* (center-of-distribution) rather than the models. Over-generalizing it into "frontier is a rip-off" starves the edge tasks where only frontier delivers; the mirror error routes familiar-looking tasks with hidden edge complexity to cheap models that fail silently. Classify first; and re-classify each model generation, because the center/edge line moves.

---

## Related Guides

- **G1 -- Writing Agent Specifications:** The three durability properties (Step 1) depend on clear intent specification. G1 Step 1 covers how to define agent goals and constraints that feed into model-resilient prompts.
- **G2 -- Managing Agent Context:** The Design/Evaluate framework (Step 5) is the prompt-level application of context curation. G2 covers the broader context engineering discipline that determines what the model sees.
- **G3 -- Agent Architecture Decisions:** The Advisor-Executor pattern (Step 10) is one of three orchestration patterns in G3. The model routing table (Step 8) and dispatch/session binding discipline (Step 9) connect to G3's multi-agent architecture guidance -- G3 owns the routing *topology* (which agent runs on which model); this guide owns the selection and binding discipline.
- **G10 -- Agent Design Patterns:** The five-layer prompt architecture in G10 provides the structural framework for applying the durability properties from this guide at each layer. The agent constitution pattern (G10, Step 1) is where model-resilient identity prompts live.

---

## Contract

### Preconditions
- You are writing or auditing prompts for agent systems.
- You understand the distinction between reasoning models and standard models.
- You can test prompts against acceptance criteria after model upgrades.
- You have access to benchmark data or a routing table for model selection.

### Invariants
- Prompts tell the model what to produce, not how to think; the declarative define-done form is the default for attended runs, SOP precision for unattended runs.
- No prescribed reasoning paths (CoT, few-shot, decomposition, skeleton-of-thought) in prompts for reasoning models.
- High-priority behavioral rules are expressed as negative constraints, not positive aspirations, and consequential constraints carry their reasoning -- ALL-CAPS imperatives are a yellow flag.
- Skill descriptions carry [What it does] + [When to use it] + [Key capabilities]; skill steering uses consistent leading words verified by trace echo.
- Model selection is task-based, not provider-based, and center/edge task classification precedes any routing-table lookup.
- Every subagent dispatch names its model explicitly; the session model is pinned -- cheap subtasks are delegated to subagents, never switched mid-session.
- Effort level is tuned per task; default-high is not assumed correct.
- The Advisor-Executor pattern is considered before defaulting to the most expensive model.
- New task classes are prototyped at the frontier tier; downshifts are validated against the frontier reference and recorded as routing datapoints.
- Prompts carry explicit ROLE, AUTHORITY, CONSTRAINT, and FAILURE SIGNAL properties.
- Prompt changes are versioned and tested before deployment.
- For multi-turn agent applications, stable prompt layers are cached separately from ephemeral turn state.
- Code snippets in agent-produced outputs are extracted programmatically from source files, not reconstructed from model memory.
- Output format control is explicit and user-overridable where the agent is interactive.
- Spec creation for complex tasks includes a bidirectional prompting phase before implementation; scope-setting moments add Socratic discovery with an explicit premise challenge.
- Metaprompt optimization loops use machine-checkable acceptance criteria that resist proxy-metric gaming.

### Governance
- Prompts are versioned and tested against acceptance criteria after model upgrades.
- Model routing and effort tables are reviewed when any constituent model has a major release; downshift events are recorded as routing datapoints; effort/cost numbers live in a maintained registry, not prose.
- Anti-pattern audits are conducted after major model releases.
- Prompt policy properties (ROLE, AUTHORITY, CONSTRAINT, FAILURE SIGNAL) are checked during skill review, alongside the instruction-craft checks (description structure, why-explanations, leading-word consistency).
- Dispatch templates require an explicit model; audits check tier distribution, not field presence.
- Elicitation technique selection is justified per task type, not applied by default.
- Metaprompt loops include acceptance criteria that resist proxy-metric gaming; criteria are reviewed when the loop is first established and when failure modes are detected.
- This guide is owned by the Improvement Loop knowledge layer.

### Recovery
- **Prompt breaks after model upgrade:** Audit against the three durability properties. Remove prescribed reasoning patterns first (most common cause). If the prompt passes all three properties, escalate to context engineering or constraint specificity.
- **Model costs too high:** Tune effort level first (the bigger, cheaper lever), then apply the Advisor-Executor pattern for API applications or reroute bulk work to cost-floor models. Check for Opus-as-default and silent-inheritance anti-patterns.
- **Subagent fan-out cost blowup:** Check dispatches for missing model parameters (silent inheritance of the session's expensive model). Make the model explicit per dispatch; re-tier using the turn-count heuristic, not per-token price.
- **Tempted to switch models mid-session:** Don't -- the cache break usually costs more. Compose a hand-off message and spawn a subagent on the cheaper model. Exception: very short sessions with little accumulated context.
- **Cheap model fails on a "familiar" task:** Re-classify -- the task likely carries hidden edge-of-distribution complexity. Route back to frontier, or run the prototype-then-downshift lifecycle to isolate which sub-tasks genuinely need frontier.
- **Skill never triggers:** Audit the description against [What] + [When] + [Capabilities]; add natural trigger phrases and a push clause. Check the validation constraints (name, reserved words, length).
- **Skill triggers but does not comply:** Strengthen and unify the leading words before adding rules; verify echo in reasoning traces. If a review skill is too soft, apply the strictness-escalation stack (standards, flags, literal phrases, approval bar) rather than adding "be strict."
- **Prompt performance varies across models:** Check for violated durability properties (especially property 1 -- prescribed reasoning). If properties pass, the issue is likely in context quality or constraint underspecification. Leading-word strength also varies by model family -- re-verify trace echo.
- **Brevity constraints degrade output:** Switch to dynamic brevity -- verbose for planning and analysis phases, terse for execution and final output. Do not apply blanket brevity to all prompt types.
- **Agent gold-plates after cost-bias correction:** Re-scope the rule -- development cost is lower, not zero. Price options by tokens and review burden; minimum viable abstraction still applies.
- **Agent rewrites code it was not asked to touch:** Add the surgical-change constraint; for recurring violations, require a pre-task scope declaration (files and line ranges) the human approves before execution.
- **Elicitation produces diminishing returns:** Reduce to 1-2 techniques per prompt. The problem is technique overload, not technique failure.
- **Routing table is stale:** Update specific model assignments; the task-based routing structure remains valid. Set a review trigger on major model releases, not calendar dates. Harvest downshift-log entries as new routing rows.
- **Cache misses on every turn despite stable content:** Verify that ephemeral turn state is injected as a separate content block and is not inlined into the cached layer 1-6 segment. Check that `cache_control` markers are attached at the correct layer boundaries in the assembly module.
- **Stale context persisting across turns:** The cached layer includes content that changes between turns (e.g., session variables, current task). Move that content to the ephemeral layer 7 block so it is refreshed each turn.
- **Agent outputs contain incorrect code snippets:** Add a programmatic-extraction rule ("use `sed`/`grep`/`cat` to extract code; do not type from memory"). If the agent ignores the rule, escalate to a hook or post-hoc verification that diffs quoted snippets against source files.
- **Output format wrong despite system prompt constraints:** Add explicit user-overridable format commands (star commands). If format conflicts arise between domain defaults and user overrides, the user override takes precedence.
- **Spec-implementation misalignment causes cascading bugs:** Insert a bidirectional prompting phase before implementation. If misalignment traces to a wrong premise rather than a missed detail, escalate to Socratic discovery with an explicit premise challenge. If the resulting plan exceeds context limits, decompose into sub-plans before proceeding.
- **Unattended routine fails silently:** Rewrite the routine prompt as a numbered SOP with named data sources, an explicit completion signal, and inline edge-case handling. If the task needs mid-flow judgment, it is not routine-suitable -- keep it interactive.
- **Metaprompt loop converges on poor outputs:** Review acceptance criteria for proxy-metric gaming. Replace gameable criteria (word count, header count) with structural validity checks (parseable output, existing file references, correct schema).
