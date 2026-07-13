---
title: "Defending Against Context Degradation"
type: "guideline"
category: "Context Engineering"
target_system:
  - "improvement-loop"
stage: "draft"
created: "2026-05-25"
updated: "2026-07-13"
author: "claude"
source_findings:
  - "ace-delta-updates-over-monolithic-rewrites"
  - "context-rot-attention-budget-depletion"
  - "context-rot-silent-killer-and-mitigations"
  - "prompt-caching-for-stable-agent-context"
  - "dynamic-tool-pool-assembly-transcript-compaction"
  - "response-format-enum-for-adaptive-verbosity"
  - "reasoning-token-overhead-from-context-files"
  - "ide-context-streaming-silent-token-tax"
  - "new-chat-per-agent-step-context-hygiene"
  - "gsd-global-learnings-store-cross-session-persistence"
  - "five-context-management-techniques-in-claude-code"
  - "catastrophic-context-collapse-risk-during-claudemd"
  - "claudemd-context-rot-from-indiscriminate-rule-accu"
  - "cross-platform-context-file-strategy"
  - "global-vs-project-level-skill-and-context"
  - "model-native-context-window-awareness"
  - "monorepo-context-distribution-three-strategies"
  - "session-atomicity-single-issue-scope-quadratic-cost-reduction"
  - "three-layer-folder-as-workspace-architecture"
  - "three-tier-vault-architecture-global-shared-local"
  - "progress-md-session-bridge"
  - "trajectory-engineering-non-linear-session-forking"
  - "session-tree-as-first-class-abstraction"
  - "orchestrator-headless-dispatch-context-isolation"
  - "bounded-tiered-memory-inference-driven-curation"
  - "proactive-compaction-before-intelligence-degradation"
  - "token-economics-as-architecture-driver"
  - "html-output-as-human-in-the-loop-restorer"
  - "format-constrained-improvisation-tax"
  - "output-format-token-cost-reframed-by-context-window-size"
  - "file-mediated-subagent-handoff-workspace"
  - "attention-closure-goal-accessibility-collapse"
  - "cache-safe-compaction-forked-prefix-buffer"
  - "append-only-context-updates-system-reminder-injection"
  - "derive-dont-edit-artifacts-as-log-renders"
  - "memory-file-to-skill-migration"
  - "skill-pruning-failure-modes-noop-deletion-test"
source_dd:
  - "DD-81"
  - "DD-98"
tags:
  - "guide"
  - "context-engineering"
  - "context-degradation"
contract:
  preconditions: "Agent system is operational or in active development; context management strategy exists (see companion guide: Structuring and Loading Agent Context)"
  invariants: "Context quality degrades over time unless actively defended; token costs compound with session length; degradation is silent by default"
  governance: "Owner agent maintains; re-synthesize when source findings change by 3+"
  recovery: "If context degradation is suspected mid-session, consult the session discipline decision tree and compaction timing guide"
---

# Defending Against Context Degradation

Your agent was sharp at the start of the session and dull by the end. Or it forgot a constraint you told it five turns ago. Or your token costs grew 3x without any visible cause. These are symptoms of context degradation -- the progressive, silent erosion of agent quality that occurs in every long-running session and multi-step workflow unless you actively defend against it.

This guide covers the defense: how to detect degradation, when and how to compact, how to structure sessions so degradation never compounds, and how to control the token costs that degradation imposes.

## When to Use This Guide

- Agent output quality is declining over the course of a session or across phases
- Token costs are growing faster than task complexity warrants
- You suspect context rot -- the agent forgets constraints, re-derives conclusions, or contradicts earlier decisions
- You are deciding when and how to compact, clear, or fork a session
- You are designing a multi-phase workflow and need context isolation between phases
- You are choosing an output format and want to prevent review fatigue from degrading oversight
- Evolving documents (PROGRESS.md, context files, memory files) are growing without bound
- You are setting up cross-session persistence and need memory files that degrade gracefully
- You orchestrate subagents and the orchestrator's own context is filling with pasted briefs, reports, and diffs
- Your always-loaded context files (CLAUDE.md, memory files, skills) have accumulated content and need auditing down

**Companion guide:** For structuring and loading context -- what goes into the window and how to organize it -- see G2a: *Structuring and Loading Agent Context*. This guide assumes you have a working context architecture and focuses on keeping it healthy over time.

## Key Concepts

**1. Context is a depletable resource, not a bucket.** As tokens accumulate, the transformer's attention mechanism must distribute budget across O(n^2) pairwise relationships. Every unnecessary token actively degrades recall of every other token. Context management is not "stay under the limit" -- it is "minimize waste at all times." A 1M token window does not make this less urgent; it only defers the degradation, which makes the eventual compaction worse because there is more to summarize. Mechanistically, the failure is not uniform blurring: attention to early goal-defining tokens decays monotonically as the conversation lengthens, and when it falls below a per-model threshold the "attention channel" to those tokens closes. The instructions are still physically in the window -- they are just no longer reachable. *In-context is not the same as usable.*

**2. Degradation is invisible by default.** Context rot produces plausible-looking output that silently deviates from requirements. Standard monitoring (error rates, latency, completion status) will not catch it. Only explicit state tracking, contract validation, and proactive compaction detect drift before it compounds into visible failures. Users who blame model providers for "nerfing" models are often experiencing their own context files rotting under them.

**3. The cost of context is multiplicative, not additive.** Context files do not just add input tokens -- they amplify reasoning token usage by 14-22%. Agents reason about context instructions even when irrelevant, consuming compute on instruction-processing rather than task-solving. This compounds across turns: a 20% reasoning overhead on a 10-turn task means 200% additional reasoning tokens over the session. Additionally, the same data structured differently can cost 15x more to query, making structure a cost multiplier. The same multiplicative logic governs orchestration: everything you paste into a subagent dispatch prompt stays resident in the orchestrator's context for the rest of the session -- pasted content is a permanent tax, not a one-time cost.

**4. Session boundaries are your strongest defense.** Bounding each session to a single issue reduces context consumption quadratically relative to multi-task sessions. Each task in a multi-task session adds to the context that subsequent tasks must parse, plan against, and avoid contradicting -- coordination cost dominates task cost. Fresh context per task is cheaper and produces better decisions. This defense has no cheap in-place substitute: periodically re-injecting the goal as a reminder message was empirically tested and did *not* restore goal-conditioned behavior once attention to the original instructions had closed. Repeating text is not the same as preserving usable goal information -- prefer a fresh-session handoff at the task boundary over an ever-longer conversation patched with reminders.

**5. Compact early, while the model is still sharp.** The model is at its least intelligent point when autocompaction fires. Proactive compaction at stable checkpoints (task boundaries, post-test-pass) produces better summaries than reactive compaction under pressure. A 1M context window is not a license to defer compaction -- it is time to compact well.

---

## Detecting Context Degradation

Context rot is silent. You need active detection rather than waiting for visible failures.

### Behavioral Signals

Observe your agent for these degradation indicators:

| Signal | What You See | Root Cause |
|--------|-------------|------------|
| **Constraint amnesia** | Agent violates a rule stated earlier in the session | Attention budget depleted; early instructions lost in noise |
| **Conclusion re-derivation** | Agent re-solves a problem it already solved, possibly with a contradictory result | Prior reasoning displaced by newer context |
| **Increasing verbosity** | Agent responses grow longer without providing more substance | Reasoning token amplification from context bloat |
| **Plausible drift** | Output looks correct but subtly deviates from requirements | Contract not being validated; accumulated drift |
| **Disavowal** | Agent claims it cannot do something it did earlier | Context limit approaching; self-preservation behavior |
| **Goal drift despite reminders** | Agent keeps deviating even after you restate the objective | Attention channel to goal tokens has closed; repetition does not reopen it |

### Structural Detection

Beyond observing behavior, build detection into your workflow:

1. **Track state as data, not prose.** Maintain an explicit state object (YAML/JSON) of active constraints, goals, and decisions. When the agent needs to check a constraint, it reads the state object, not the conversation. Prose summaries lose precision; structured state forces explicit representation of each active constraint.

2. **Validate against contracts at step boundaries.** Define what inputs are expected, what outputs are required, and what invariants must hold for each phase. A contract violation is a hard stop, not a warning.

3. **Ground reasoning in citations.** When the agent makes a claim, it should cite the source (state object field, document section, prior validated result). Uncitable claims are ungrounded and signal drift.

4. **Monitor token utilization.** Watch for the 40-50% utilization threshold. Some models track their own remaining headroom internally and can self-report -- but do not rely on this alone. Instrument your harness to project utilization per turn.

5. **Treat degradation as threshold-shaped, not gradual.** Attention to early instructions declines monotonically and then fails abruptly when it crosses a per-model threshold -- and post-failure behavior varies sharply by architecture. Drift tolerance observed on one model does not transfer to another. Calibrate session-length budgets per model, and re-validate them on every model switch rather than assuming the old budget holds.

---

## Session Discipline

Session design is the highest-leverage defense against degradation. The way you scope, bound, and transition between sessions determines whether degradation accumulates or resets.

### The Session Discipline Decision Tree

```
Is this task achievable in a single focused session?
  |
  +-- YES --> Single-issue session
  |           One task, full context budget, clean exit
  |
  +-- NO, it requires multiple phases
        |
        +-- Can phases run independently?
        |     |
        |     +-- YES --> Headless dispatch
        |     |           Thin orchestrator + fresh process per phase
        |     |           Orchestrator holds only coordination state
        |     |
        |     +-- NO, phases depend on prior results
        |           |
        |           +-- Can results transfer via files?
        |                 |
        |                 +-- YES --> New-chat-per-phase
        |                 |           Kill session at each boundary
        |                 |           Next phase reads output files only
        |                 |
        |                 +-- NO --> Long session with checkpoints
        |                            Compact proactively at phase boundaries
        |                            Use /rewind to trim dead branches
```

### Single-Issue Sessions

Bound each session to exactly one fine-grained task. The mechanism: smaller scope means less prior context loaded, fewer intermediate states tracked, and cleaner handoffs. Context consumption scales super-linearly with task scope -- a session handling N tasks requires O(N^2) context because each task's intermediate state pollutes every subsequent task's context. N single-task sessions require only O(N) total context.

This requires a persistent work queue so agents can pick up single issues without loading a full plan. Session start = load one issue + its direct dependencies. Session end = update issue status + file any discovered issues.

### New-Chat-Per-Phase

At each phase boundary, kill the current session and start fresh. Information transfers via document artifacts only -- the next agent reads the output files, not the conversation history. This eliminates the accumulation of noise, outdated instructions, and conflicting context that degrade long-running sessions. The mechanism argument is now empirical: once attention to the original goal tokens has closed, re-stating the goal inside the same conversation does not restore goal-conditioned behavior -- a fresh session with a clean handoff is the intervention that actually works.

The discipline: every file kept in the project is potential context. Rather than leaving reference material in the active conversation, add it to a project references file that can be loaded selectively.

### Headless Dispatch for Context Isolation

For multi-phase autonomous workflows, a thin orchestrator dispatches each phase as a separate headless subprocess. Each subprocess gets a fresh context window, executes one phase, reports a summary, and exits. The orchestrator never accumulates work context -- only coordination state -- staying under 10% context utilization even after dispatching 100+ phases.

The trade-off: phase prompts must be self-contained because the subprocess has no access to the orchestrator's conversation history. Complex inter-phase dependencies require explicit state passing through files.

### File-Mediated Subagent Handoffs

The headless-dispatch discipline generalizes to every orchestrator/subagent handoff, headless or not: **never paste task text, reports, or diffs into a dispatch prompt -- write them to files and dispatch paths.** Everything pasted into a dispatch stays resident in the orchestrator's context for the rest of the session; the orchestrator's context should hold routing state, not artifact bodies. (Documented anti-pattern: a 42,000-character dispatch prompt that was 99% pasted history.)

The working protocol, converged on independently by multiple production frameworks:

1. **A runtime scratch workspace** holds the handoff files -- task briefs, worker reports, review packages, a progress ledger. Keep it in the working tree but self-ignoring (its own `.gitignore`), and deliberately *outside* `.git/`, which harnesses write-protect. Note the recovery constraint: `git clean -fdx` erases the workspace, so anything that must survive belongs in git history, not the scratch area.
2. **Deterministic tools write the files, dispatches carry paths.** A script extracts task N from the plan into `task-N-brief.md` -- no subagent ever reads the whole plan -- and packages review diffs into a single readable file. Scripted assembly, not orchestrator prose, is what makes brief extraction and diff packaging reliable and cheap. The dispatch prompt is a thin frame: one line of scene-setting, the brief path ("read this first -- it is your requirements"), interfaces from earlier tasks, and the report-file path plus its contract.
3. **Thin returns.** Worker return messages are capped (~15 lines); detail lives in the report file. The orchestrator reads the verdict and the path, and opens the report only when it must.

Two failure modes need explicit defense: a subagent that skips reading its brief file executes on vibes -- the dispatch must make the read mandatory and verifiable; and file-name/section conventions between separately-versioned components drift -- pin the handoff-file contract somewhere both sides read.

### Trajectory Engineering

When working in a single session, treat the conversation as a tree rather than a linear transcript. After resolving a bug or exploring an approach, rewind to before the exploration began, provide a brief summary of what happened and how it was resolved, and continue from the clean state. This eliminates dead-weight context (debugging attempts, failed approaches, exploratory tangents) while preserving learnings in compact form.

The tree model also enables forking: from a common starting point, explore multiple approaches on separate branches, compare results, and continue from the best branch. Keep the trunk lean -- it is the stable, reusable context. Branches are explorations that should be trimmed once evaluated.

The branching and pruning model can be made explicit through session tree data structures that support forking from any entry point, compacting summaries of pruned branches, navigating to any node with automatic summarization of skipped branches, and user-defined bookmarks on specific entries.

---

## Compaction Timing and Strategy

Compaction is the most commonly misused context management tool. Used reactively at the wrong moment, it causes irreversible information loss. Used proactively at stable checkpoints, it is one of the strongest defenses against degradation.

### The Compaction Timing Decision Tree

```
Are you at a natural task boundary (post-test-pass, phase complete, plan confirmed)?
  |
  +-- YES --> Is context utilization above 40%?
  |             |
  |             +-- YES --> Compact now with a steering hint
  |             |           "Compact, preserving: {{CURRENT_FOCUS}}"
  |             |
  |             +-- NO --> No compaction needed yet
  |                        Continue working
  |
  +-- NO --> Is the agent showing degradation signals?
              |
              +-- YES --> Can you reach a task boundary within 2-3 turns?
              |             |
              |             +-- YES --> Finish the current micro-task, then compact
              |             |
              |             +-- NO --> Compact now (accept lower summary quality)
              |                        or /clear + handoff document
              |
              +-- NO --> Continue working
                         Check again at next boundary
```

### Five Context Management Techniques, Ranked

When degradation is detected or anticipated, choose the right tool:

| Technique | Mechanism | Quality | Speed | When to Use |
|-----------|-----------|---------|-------|-------------|
| **Sub-agent spawn** | Fresh context window for isolated subtask | Best | Fast | Isolated subtasks that don't need session history |
| **/handoff + /clear** | Write structured summary, then clear everything | High | Slow | Clean phase transitions; you can write a better summary than the model |
| **Trajectory trim (/rewind)** | Return to prior point, trim dead branches | High | Fast | After bug fixes, failed explorations, tangents |
| **/clear at break point** | Full context reset at a natural boundary | Medium | Fast | Quick reset when CLAUDE.md can re-orient the model |
| **Compaction** | Lossy compression of conversation history | Low | Auto | Only as a fallback; never mid-implementation |

Avoid compaction as the default. It is the most common technique but the least effective -- every compaction step has a small but fixed probability (~3%, increasing by ~0.25% per additional compaction) of producing a catastrophic rewrite where the entire context collapses to an unhelpful summary. The probability is low per attempt but cumulative, and a poisoned context persists permanently.

### Cache-Safe Compaction Mechanics

When you do compact -- or build compaction into a harness -- the mechanics determine whether compaction is a routine background operation or a cost spike at the worst possible moment. Compaction fires precisely when the conversation is at its longest, i.e., when a cache miss is at its most expensive.

The naive design -- a separate summarization call with its own system prompt and no tools -- gets zero cache hits: its prefix differs from the parent conversation at token one, so the provider re-processes the entire transcript at full input price. The cache-safe design instead **forks the conversation**: identical system prompt, session context, and tool definitions, all parent messages prepended byte-for-byte, and the compaction instruction appended as one new user message. Everything except the compaction prompt is served from cache, so marginal cost scales with the compaction prompt, not conversation length.

Two supporting disciplines:

- **Reserve a compaction buffer.** Keep fixed headroom free below the context ceiling so the summary always has room to be generated. Without it, the harness can reach a state where it needs to compact but no longer can. Size it deliberately: too small truncates summaries; too large wastes usable context every turn.
- **Prefer native compaction when available.** Providers now offer server-side compaction built on these mechanics; use it instead of hand-rolling. And remember that cache-safety fixes the *cost* of compaction, not its *lossiness* -- critical constraints can still fall out of the summary, which is why the steering-hint discipline above still applies.

### Defending Evolving Documents

Documents that evolve across sessions (PROGRESS.md, memory files, context files) are vulnerable to a specific failure mode: asking an LLM to rewrite the full document introduces brevity bias that silently drops domain-specific details. Each cycle of rewriting erodes the document further. Mitigation:

1. **Never ask the LLM to rewrite the full document.** Instead, produce compact delta entries (what changed, what was learned, what follows) and merge them with deterministic (non-LLM) logic.
2. **Set a size budget.** When the budget is approached, trigger human-reviewed consolidation -- not LLM summarization.
3. **Consolidation is a human task.** Periodically review accumulated deltas and consolidate redundant or stale entries under human judgment.

The strongest form of this defense inverts where truth lives: **derive, don't edit.** Make an append-only decision log the canonical record and treat the polished artifact (spec, architecture doc, status document) as a *derived view* that is re-rendered from the log -- never hand-patched. Pair it with a single-writer rule: exactly one process or skill renders each artifact; everyone else contributes by appending to the log. The payoff is structural: contributions append in any order without merge drift, resumes are cheap (re-render, don't reconcile), and every artifact can be explained by the log that produced it. The costs are equally structural: hand-edits to a derived artifact are overwritten on the next render (contributors must know the log is the only writable surface), an LLM-performed render can vary between runs, and decisions that were never logged vanish from every future render.

---

## Context Isolation Architecture

Degradation compounds when context from unrelated concerns bleeds across boundaries. Architectural isolation prevents this at the structural level.

### Tier and Scope Isolation

Separate context into tiers with distinct sharing and persistence rules:

| Tier | Location | Persistence | Loads When |
|------|----------|-------------|------------|
| **Global** | `~/.claude/` | Permanent, follows the user | Every session |
| **Project** | Repo root, `.claude/rules/` | Git-shared | Sessions in this repo |
| **Workspace** | Subdirectory context files | Git-shared | Working in that directory |
| **Ephemeral** | Gitignored runtime state | Session-local | Current session only |

Scope each context element to the narrowest tier where it applies. A skill relevant only to one project does not belong at the global tier. A rule relevant only to one workspace does not belong at the project tier. Incorrect scoping causes irrelevant context to load in every session, recreating the same bloat problem that a flat, monolithic context file creates.

For monorepos, three strategies exist in production:

1. **Per-package chain-loaders** (highest precision, highest maintenance): Each package gets its own context file pair with domain-specific conventions. The agent loads only the active package's context.
2. **Path-scoped rules** (balanced): Rule files auto-load based on which directory the agent is editing. No per-package context files needed.
3. **Single global file** (simplest, lowest precision): One context file serves all packages. Works for small projects with uniform conventions.

### Cross-Platform Context Distribution

When multiple AI tools share a codebase (Claude Code, Copilot, Cursor), each tool auto-loads different files. Three production strategies:

- **Chain-loader indirection:** Root CLAUDE.md is a pointer (`@AGENTS.md`); other tools read AGENTS.md directly. Minimal duplication.
- **Platform-specific mirroring:** Parallel agent definitions adapted per platform. Maximum fidelity, but copies drift.
- **Content duplication:** Identical files with different names. Simplest, but drift risk increases with size.

Prefer chain-loading when possible. It solves the naming constraint with zero content duplication.

---

## Memory File Discipline

Cross-session persistence files (MEMORY.md, PROGRESS.md, learnings stores) are context degradation vectors if they grow without bound or drift from reality.

### Bounded Memory with Hard Ceilings

Enforce hard character ceilings on always-loaded memory files. When the ceiling is exceeded, a curator step consolidates and evicts entries, resolving conflicts in favor of most-recent high-confidence facts.

The architecture:

| Tier | Injection | Ceiling | Example |
|------|-----------|---------|---------|
| **Hot** (always loaded) | Verbatim into system prompt | Hard character limit | MEMORY.md, USER.md, identity files |
| **Warm** (retrieved) | Surfaced by search, LLM-summarized before injection | Soft limit (search budget) | Full-text search over prior sessions |
| **Cold** (archival) | Not injected; available for explicit retrieval | None | Raw session transcripts |

The key innovations are: (1) hard ceilings prevent unbounded growth of always-loaded files; (2) inference-driven writes -- the agent decides what to persist based on conversation patterns, not just explicit "remember this" commands; (3) a curator step that consolidates under human-defined priorities when ceilings are exceeded.

### The Always-Loaded Test and Skill Migration

Ceilings bound growth; migration reduces what needs bounding. The test for each section of an always-loaded file is: **is this needed by every session, or only conditionally?** Anything conditionally useful in a memory file is a standing token tax -- it loads whether or not the session needs it.

The lifecycle discipline:

1. **Global memory stays minimal** -- a few dozen lines of genuinely universal preferences and bias corrections. Everything in it enters every session across all projects.
2. **Project memory accumulates by correction.** Each time the agent errs, store the fix as a learning. The file bloats by design -- capture is cheap.
3. **Conditional content migrates to skills.** Periodically, sections needed only for some session types (testing procedures, deployment steps) are extracted into skills, whose progressive disclosure loads a one-line description at startup and the full content only on invocation. The migration can be delegated to the agent itself ("extract the E2E testing instructions from the memory file into a project-level skill") -- but review the diff; agent-performed migration can drop nuance.

Push-loaded memory and pull-loaded skills are not an architectural either/or -- they are lifecycle stages of the same content. Knowledge enters through the memory file (cheap to capture) and graduates to a skill once its conditionality is clear (cheap to carry). Guard the inverse failure: over-migrating content the agent needs every session hides it behind a skill description it may fail to invoke, and the missed-context tax is worse than the token tax.

### Pruning Context Files: Duplication, Sediment, No-Ops

A bloated context file or skill is a symptom, not the disease. When auditing an always-loaded file down (the fix for indiscriminate accumulation -- see Pitfalls), diagnose against three named failure modes, each with its own test:

| Failure mode | What it looks like | Test / remedy |
|--------------|--------------------|---------------|
| **Duplication** | The same template, rule, or explainer stated in several places, including across reference files | Single source of truth for every part -- steps *and* reference material |
| **Sediment** | Accreted multi-contributor content nobody feels brave enough to delete; stale or irrelevant to every current branch | Structural re-sort: move each addition to the branch it serves, or kill it dead if it serves none |
| **No-ops** | Passages that appear to do something but don't change agent behavior ("write a clear, detailed commit message") | The **deletion test**: delete the paragraph (mentally or actually) -- if the agent would behave the same from priors, it was a no-op; remove it |

No-ops are especially common in agent-written files, so agent-authored context artifacts deserve a harder deletion-test pass. Two cautions: the deletion test samples behavior under today's model -- content that survives deletion now may regress under a different model or in edge branches; and hard constraints (security boundaries, gates) can look like no-ops precisely because they rarely bind. Never prune safety text on deletion-test evidence alone.

### Session Bridge Files

A structured session bridge file (PROGRESS.md or equivalent) persists working state across session boundaries. At session start, the agent reads it to orient itself; at session end, it writes an updated summary covering what was completed, what is in progress, what is blocked, and what comes next.

The bridge file must be verified against actual file state -- stale entries that diverge from reality actively mislead future sessions. A dual-file pattern (plan file for intent + changelog file for history) provides richer context than a single bridge file by separating what the agent should do from what has happened.

### Cross-Session Learnings Store

For repeated workflows, a structured learnings store (outside ephemeral session directories) converts repeated failures into durable knowledge. The store should expose CRUD operations, auto-copy learnings at phase completion, and inject relevant learnings into planning context at the right moment.

As the store grows, it needs relevance filtering -- injecting all learnings into every plan becomes its own context budget problem. Learnings should carry confidence scores that decay as the codebase evolves.

---

## Token Cost Defense

Degradation and cost are coupled: degradation increases token waste, and token waste accelerates degradation. Defending against cost blowout is part of defending against quality erosion.

### Caching Stable Context

Separate agent context into stable and dynamic elements, then cache the stable portion. Cache hits on Claude Opus cost $0.50/M tokens vs $5/M standard input -- a 90% cost reduction. If 80% of input tokens are stable context and you cache them, your effective input cost drops by approximately 72%.

The stability classification:

| Stable (cacheable) | Dynamic (not cacheable) |
|---------------------|------------------------|
| System prompt | Conversation history |
| Tool definitions | User input per turn |
| Persona instructions | Intermediate results |
| Reference documentation | Task-specific state |
| Rules and schemas | Retrieved context |

**Ordering constraint:** Cached content must appear in the same position in the message array with identical bytes across requests. Even a single character change forces a full-price re-read of the entire block. Batch prompt edits rather than making incremental changes.

### The Append-Only Prefix Discipline

The parent rule behind every cache mechanic: **the prompt prefix is append-only.** When information in the prefix goes stale mid-session (current time, file contents changed on disk, a mode toggled), do not rewrite the prefix -- inject the update as a marked reminder block inside a later user message or tool result. The cached prefix stays byte-identical; the model receives the correction through the conversation channel. State flows forward through messages; the prefix is immutable. Multiple production harnesses have converged on this independently, treating the immutable baseline context as architecture rather than an optimization -- with compaction rolling a *new* baseline rather than mutating the old one.

The enabling structure is **static-first prompt layering**, ordered by cache scope -- each layer changes less often than everything below it, so the maximal shared prefix survives across turns and across sessions:

1. Static system prompt and tool definitions -- cached globally, across sessions
2. Project context file -- cached per project
3. Session context -- cached per session
4. Conversation messages -- grows turn by turn

Cache breakage is silent, so lint for prefix-mutation patterns: dynamic timestamps embedded in static prompts, non-deterministic tool ordering, mid-session tool-parameter changes, and mid-session model switches all quietly revert you to full price. Pair the discipline with cache hit-rate observation to verify it is actually holding. Two costs to manage: appended reminders accumulate (repeated corrections spend the tokens the cache saved), and genuinely wrong prefix content can only be countermanded, never removed, until the next compaction or fresh session.

### Adaptive Tool and Response Verbosity

Two complementary techniques reduce context consumption from tool interactions:

1. **Dynamic tool pool assembly:** Instead of loading all tools, assemble a session-specific subset based on mode flags, permissions, and deny lists. Token reduction of up to 98.7% (150K to 2K tokens) when tools are discovered on-demand via filesystem navigation rather than loaded upfront.

2. **Response format enums:** Add a verbosity parameter (detailed vs. concise) to tool return values. Concise format returns only high-signal information (~72 tokens vs. ~206 detailed). The agent selects format based on current task needs -- scanning vs. chaining.

### Output Format as Governance and Cost Decision

Output format affects both token cost and human oversight quality. The decision framework depends on context window size:

| Factor | Favor Markdown | Favor HTML |
|--------|---------------|------------|
| Token budget | Tight (< 128K window) | Abundant (1M window) |
| Output complexity | Pure prose, status updates | Quantitative data, spatial layouts, decision specs |
| Human engagement | Reviewer reads reliably | Reviewer is skimming or rubber-stamping |
| Rendering environment | Terminal-only, Obsidian | Browser-accessible |

When the format cannot express what the model knows (charts, spatial layouts, color), the model improvises with lossy workarounds -- ASCII bar charts that break on font change, Unicode color swatches, pipe-and-dash diagrams. These improvisations consume tokens for a degraded result. Matching output expressiveness to information type eliminates this tax.

With 1M token windows, the 2-4x token overhead of HTML "barely registers against the budget." The constraint shifts from token budget to human absorption -- the question becomes "what format maximizes the chance the human will actually engage?"

### Model-Native Budget Awareness

Some models (Claude Sonnet 4.5+) track their own remaining context headroom internally and can reason about it during response generation. This provides a third escape hatch beyond harness-side projection and user intervention: the model itself saying "I have 10% left, let me wrap up."

This complements, rather than replaces, harness-side pre-turn budget projection. They operate at different layers (model vs. orchestrator) and catch different failure modes. Layered defense is stronger than either alone.

---

## Templates

### Context Degradation Audit Template

Use at session start or when degradation is suspected.

| Variable | Type | Description | Required |
|----------|------|-------------|----------|
| `{{SESSION_ID}}` | string | Current session identifier | Yes |
| `{{CONTEXT_UTILIZATION}}` | percentage | Current context window usage | Yes |
| `{{ACTIVE_CONSTRAINTS}}` | list | Constraints the agent should be tracking | Yes |
| `{{LAST_COMPACT_POINT}}` | timestamp | When context was last compacted or cleared | Yes |
| `{{DEGRADATION_SIGNALS}}` | list | Any observed behavioral signals | No |
| `{{PHASE_BOUNDARY_NEXT}}` | string | When the next natural compaction point occurs | No |

```markdown
## Context Degradation Audit — {{SESSION_ID}}

### Current State
- **Context utilization:** {{CONTEXT_UTILIZATION}}
- **Last compaction/clear:** {{LAST_COMPACT_POINT}}
- **Next phase boundary:** {{PHASE_BOUNDARY_NEXT}}

### Constraint Verification
Active constraints (verify agent still tracks each):
{{ACTIVE_CONSTRAINTS}}

### Degradation Signals Observed
{{DEGRADATION_SIGNALS}}

### Action
- [ ] If utilization > 40% and at boundary: compact with steering hint
- [ ] If constraints forgotten: re-inject state object
- [ ] If signals present but no boundary near: /clear + handoff document
- [ ] If no signals: continue, check again at next boundary
```

### Compaction Steering Hint Template

Use when invoking proactive compaction to guide what the model preserves.

| Variable | Type | Description | Required |
|----------|------|-------------|----------|
| `{{CURRENT_FOCUS}}` | string | The specific task or file currently being worked | Yes |
| `{{PRESERVE_LIST}}` | list | Decisions, constraints, or state that must survive compaction | Yes |
| `{{DISCARD_CANDIDATES}}` | list | Completed tasks or dead-end explorations safe to drop | No |

```
/compact Preserve the following across compaction:
- Current focus: {{CURRENT_FOCUS}}
- Active decisions: {{PRESERVE_LIST}}
- Safe to drop: {{DISCARD_CANDIDATES}}
Retain all open questions and unresolved constraints.
```

### Session Bridge File Template

Use at session end to persist state for the next session.

| Variable | Type | Description | Required |
|----------|------|-------------|----------|
| `{{DATE}}` | date | Session date | Yes |
| `{{SESSION_NUM}}` | integer | Session number | Yes |
| `{{COMPLETED}}` | list | Tasks completed this session | Yes |
| `{{IN_PROGRESS}}` | list | Tasks started but not finished | No |
| `{{BLOCKED}}` | list | Tasks blocked with reason | No |
| `{{NEXT}}` | list | Prioritized next actions | Yes |
| `{{DECISIONS}}` | list | Decisions made this session with rationale | No |
| `{{LEARNINGS}}` | list | Reusable insights discovered | No |

```markdown
## Session {{SESSION_NUM}} — {{DATE}}

### Completed
{{COMPLETED}}

### In Progress
{{IN_PROGRESS}}

### Blocked
{{BLOCKED}}

### Decisions Made
{{DECISIONS}}

### Learnings
{{LEARNINGS}}

### Next Session
{{NEXT}}
```

### Memory File Ceiling Enforcement Template

Use when designing always-loaded memory files.

| Variable | Type | Description | Required |
|----------|------|-------------|----------|
| `{{FILE_NAME}}` | string | Memory file name (e.g., MEMORY.md) | Yes |
| `{{CHAR_CEILING}}` | integer | Hard character ceiling | Yes |
| `{{PRIORITY_RULE}}` | string | How to resolve conflicts when ceiling exceeded | Yes |
| `{{WRITE_TRIGGER}}` | string | What triggers a write (inference/explicit/both) | Yes |

```yaml
memory_file:
  name: "{{FILE_NAME}}"
  ceiling_chars: {{CHAR_CEILING}}
  injection: "always"  # loaded into system prompt every session
  write_trigger: "{{WRITE_TRIGGER}}"
  overflow_policy:
    action: "curate"
    priority: "{{PRIORITY_RULE}}"
    method: "consolidate-and-evict"
    eviction_order: "oldest-lowest-confidence-first"
  format: "timestamped entries, one fact per line"
```

### File-Mediated Dispatch Prompt Template

Use when dispatching a subagent so the orchestrator's context holds paths, not payloads.

| Variable | Type | Description | Required |
|----------|------|-------------|----------|
| `{{SCENE}}` | string | One line of scene-setting (project, phase) | Yes |
| `{{BRIEF_PATH}}` | path | Task brief file the subagent must read first | Yes |
| `{{INTERFACE_NOTES}}` | list | Interfaces/contracts from earlier tasks it must honor | No |
| `{{REPORT_PATH}}` | path | Where the subagent writes its full report | Yes |
| `{{REPORT_CONTRACT}}` | string | Required report structure (sections, verdict field) | Yes |
| `{{RETURN_CAP}}` | integer | Max lines for the return message (default 15) | Yes |

```markdown
{{SCENE}}

Read {{BRIEF_PATH}} first — it is your requirements. Do not proceed until you have read it.

Interfaces from earlier tasks you must honor:
{{INTERFACE_NOTES}}

Write your full report to {{REPORT_PATH}} with this structure:
{{REPORT_CONTRACT}}

Your return message must be at most {{RETURN_CAP}} lines: verdict, top findings, and the report path. All detail goes in the report file, not the return.
```

---

## Worked Examples

### Example 1: Compaction Steering Hint -- Mid-Session Bug Fix

A developer has been working on a feature implementation for 40 minutes. After fixing an unexpected bug at turn 15, context utilization is at 52%. The bug-fixing exploration added significant noise. Rather than continuing with degraded context, they compact:

```
/compact Preserve the following across compaction:
- Current focus: Implementing the webhook retry logic in src/webhooks/retry.ts
- Active decisions:
  - Using exponential backoff with jitter (decided turn 3)
  - Max retries = 5 with 30s ceiling (decided turn 7)
  - Dead letter queue for exhausted retries (decided turn 12)
- Safe to drop:
  - The TypeScript type error in turn 8-11 (resolved: was a missing generic parameter)
  - The test runner configuration detour in turn 13-14 (resolved: needed --experimental-vm-modules flag)
Retain all open questions and unresolved constraints.
```

The compact preserves the architectural decisions and current focus while shedding the debugging context that would otherwise pollute subsequent reasoning.

### Example 2: Memory File with Ceiling -- User Preferences

A personal assistant agent maintains a USER.md file that is injected into every session:

```yaml
memory_file:
  name: "USER.md"
  ceiling_chars: 1375
  injection: "always"
  write_trigger: "inference"
  overflow_policy:
    action: "curate"
    priority: "most-recent high-confidence facts win"
    method: "consolidate-and-evict"
    eviction_order: "oldest-lowest-confidence-first"
  format: "timestamped entries, one fact per line"
```

Current file content (at 1,340 of 1,375 chars):

```markdown
## User Preferences
- [2026-05-20] Prefers concise output; dislikes filler paragraphs
- [2026-05-18] Uses macOS with zsh; primary editor is Cursor
- [2026-05-15] Working timezone: US Pacific
- [2026-05-10] Writes TypeScript (strict mode) and Python 3.12+
- [2026-04-28] Prefers plan mode before any multi-step task
- [2026-04-15] Never run destructive commands without explicit approval
- [2026-03-20] Interested in agentic coding patterns and context engineering
```

When a new observation pushes past the 1,375-char ceiling, the curator consolidates: the March entry about interests is lower-confidence (inferred from conversation, not explicitly stated) and oldest, making it the eviction candidate. The curator removes it and adds the new entry, keeping the file within budget.

### Example 3: Headless Dispatch -- Autonomous Multi-Phase Project

An orchestrator manages a 6-phase migration project. Each phase runs as a separate headless subprocess:

```
Phase 1: Schema migration      --> claude -p "Migrate schema..."  --> DONE
Phase 2: Data migration         --> claude -p "Migrate data..."    --> DONE
Phase 3: API endpoint updates   --> claude -p "Update endpoints.." --> IN_PROGRESS
Phase 4: Test suite updates     --> [waiting]
Phase 5: Documentation          --> [waiting]
Phase 6: Deployment config      --> [waiting]
```

The orchestrator's state file:

```json
{
  "project": "v2-migration",
  "phases": [
    {"id": 1, "status": "done", "summary": "Schema migrated: 12 tables, 3 new indexes"},
    {"id": 2, "status": "done", "summary": "Data migrated: 1.2M rows, 0 failures"},
    {"id": 3, "status": "running", "started": "2026-05-25T14:30:00Z"},
    {"id": 4, "status": "pending", "depends_on": [3]},
    {"id": 5, "status": "pending", "depends_on": [3, 4]},
    {"id": 6, "status": "pending", "depends_on": [5]}
  ]
}
```

After phase 3 completes, the orchestrator reads the summary, writes it to the state file, checks dependencies, and dispatches phase 4 in a fresh subprocess. The orchestrator never accumulates work context from any phase -- it holds only the coordination state shown above. Even after all 6 phases, its own context utilization remains under 10%.

### Example 4: File-Mediated Dispatch -- Implementing Task 3 of a Plan

An orchestrator is executing a 6-task implementation plan. A script has already extracted task 3 into a brief file inside the runtime scratch workspace (`.workspace/task-3-brief.md`). The dispatch prompt:

```markdown
You are implementing task 3 of the payments-retry milestone.

Read .workspace/task-3-brief.md first — it is your requirements. Do not proceed until you have read it.

Interfaces from earlier tasks you must honor:
- RetryPolicy interface defined in src/webhooks/policy.ts (task 1)
- Dead-letter queue writer exported from src/webhooks/dlq.ts (task 2)

Write your full report to .workspace/task-3-report.md with this structure:
## Verdict (done | blocked)
## What was built
## Deviations from the brief
## Test results

Your return message must be at most 15 lines: verdict, top findings, and the report path. All detail goes in the report file, not the return.
```

The subagent reads the brief (never the whole plan), implements, writes the report, and returns five lines. The orchestrator's context gains a verdict and two paths -- not the plan, not the diff, not the report body.

---

## Pitfalls

**1. Compacting at the wrong moment.** Compaction mid-implementation (rather than at a clean task boundary) produces irreversible information loss. The model is at its worst when forced to summarize under context pressure -- the summary is low quality precisely because the model has the least headroom to reason about what to preserve. Always compact at a stable checkpoint where direction is clear.

**2. Treating compaction as maintenance.** Asking an LLM to periodically "summarize" or "compact" an evolving document (CLAUDE.md, PROGRESS.md) introduces a fixed probability (~3%) of catastrophic rewrite per attempt. The probability increases with each additional compaction. After collapse, accuracy drops to ~57% of previous performance -- often below the baseline of having no context file at all. A sparse, inaccurate summary is worse than no context because it actively misleads the model.

**3. Indiscriminate rule accumulation.** Adding a rule to CLAUDE.md every time something goes wrong causes silent performance degradation. Every rule loads into every conversation regardless of relevance. Over 60-80 lines, aggregate noise dilutes attention on relevant tokens. The fix is not to compact the file (see pitfall 2) but to audit it down to universally true, globally relevant lines.

**4. Invisible context injection.** IDE context streaming silently injects open files and highlighted selections into the context window. Users have no visual indicator and may not realize it is happening. This inflates token consumption and fills the window with potentially irrelevant content. Ask the model "what do you see?" to discover what is being injected, and close irrelevant files during agent sessions.

**5. Reasoning token amplification.** Context files do not just cost their own token count -- they induce 14-22% additional reasoning tokens as the agent processes instructions even when irrelevant. Instructions that do not reduce task ambiguity are doubly expensive: input tokens + amplified reasoning. Audit each section of your context files not just for relevance but for whether it actually reduces the agent's reasoning burden.

**6. Over-atomization of sessions.** While single-issue sessions reduce context overhead, issues that are too fine-grained require more coordination overhead than they save. The break-even point depends on orchestrator communication cost and the fixed cost of loading codebase context per session. If each issue requires loading the same large codebase context, the per-session fixed cost dominates and the savings do not materialize.

**7. Stale cross-session state.** Session bridge files, learnings stores, and memory files that are not verified against actual file state become sources of outdated constraints. Without expiry or validation mechanisms, persistent state degrades into noise -- or worse, actively misleads the planner into re-applying constraints that no longer hold.

**8. Novelty-driven format switching.** Switching to HTML output restores human engagement now because it is new. If every agent output is HTML, the same review fatigue may return. The underlying problem -- output volume exceeding human review capacity -- is not solved by format alone. The format should match the information complexity and the decision type, not be applied uniformly.

**9. Patching drift with reminders.** Re-stating the goal inside a degraded conversation feels like a fix but empirically is not one: once attention to the original instructions has closed, re-injected reminder text did not restore goal-conditioned behavior in testing. Reminders spend tokens to produce the appearance of re-anchoring. The working intervention is structural -- a fresh session with a handoff document, or rewinding to a pre-drift point.

**10. Pasting artifacts into dispatch prompts.** Everything pasted into a subagent dispatch stays resident in the orchestrator's context for the rest of the session. A dispatch that inlines the plan, the history, and the diff turns the orchestrator into the very long-context session it was supposed to prevent (observed in the wild: a 42k-character dispatch that was 99% pasted history). Write files, dispatch paths, cap returns.

**11. Silent cache breakage.** A single embedded timestamp, a reordered tool list, or a mid-session model switch silently reverts every subsequent request to full-price re-processing -- nothing fails visibly; the bill just grows. The same applies to a compaction call whose prefix differs from the parent conversation. Treat the prefix as append-only and verify with cache hit-rate observation, not intent.

**12. Hand-editing derived artifacts.** In a derive-don't-edit setup, the artifact is a render of the log -- a hand-edit is not merged, it is overwritten on the next render. Contributors who don't know the log is the only writable surface lose work silently. Label derived artifacts as generated, and route all contributions through the log.

**13. Pruning on the deletion test alone.** The deletion test identifies no-op instructions cheaply, but it samples today's model's behavior -- and hard constraints look like no-ops precisely because they rarely bind. Over-migration has the same shape: moving content the agent needs every session into a skill hides it behind a description the agent may not invoke. In both cases the missed-context failure is worse than the token tax that motivated the cut.

---

## Contract

### Preconditions

- An agent system is operational or in active development.
- A context management strategy exists -- context files are structured and loaded (see companion guide G2a: *Structuring and Loading Agent Context*).
- Token usage is measurable (token counts available per turn or per session).
- Context management primitives (compaction, clearing, session creation) are available in the runtime.
- Evolving documents have version control (git or equivalent) enabling rollback.

### Invariants

- Context quality degrades over time unless actively defended. This is not a defect -- it is a property of transformer attention mechanics.
- In-context is not the same as usable. Attention to early instructions decays below a per-model threshold; presence in the window does not guarantee reachability, and in-place repetition does not restore it.
- Token costs compound with session length and task count. The relationship is super-linear, not linear.
- Degradation is silent by default. Explicit detection mechanisms (state tracking, contract validation, utilization monitoring) are required.
- Compaction at stable checkpoints produces better summaries than compaction under pressure.
- Session boundaries reset degradation. The strongest defense is to not let degradation accumulate in the first place.
- The prompt prefix is append-only. State changes flow forward through messages; mutating the prefix silently forfeits the cache.
- The orchestrator's context holds routing state, not artifact bodies. Handoffs are file-mediated; returns are thin.
- Hard ceilings on always-loaded memory files prevent unbounded context growth.
- Full-document LLM rewrites of evolving documents are prohibited; delta updates with deterministic merge are the safe alternative.

### Governance

- Owner agent maintains this guide.
- Re-synthesize when source findings change by 3+.
- Compaction timing thresholds (currently 40% utilization) are calibrated per model family and reviewed when switching models or context window sizes.
- Memory file ceilings are set per file and reviewed when the agent's responsibilities change.

### Recovery

- If context degradation is suspected mid-session: consult the session discipline decision tree and compaction timing guide above.
- If catastrophic context collapse has occurred (context file reduced to thin summary): revert to last known-good version via git. Do not attempt to "fix" the collapsed file in place.
- If a delta merge produces a malformed document: revert via git and re-apply the delta with corrected merge logic.
- If drift is detected via contract validation failure: reset to the last validated state checkpoint and re-derive from that point. Do not attempt to patch the drifted state.
- If memory file curation evicts an entry that turns out to be important: retrieve from cold storage (raw session transcripts) and re-add with updated confidence.
- If token costs spike without a workload change: audit for silent cache breakage -- prefix mutations (timestamps, tool reordering, model switches) and non-forked compaction calls are the usual suspects.
- If a scratch handoff workspace is destroyed (e.g., `git clean -fdx`): recover report content from git history where committed; treat uncommitted briefs/reports as lost and re-derive from the plan.
