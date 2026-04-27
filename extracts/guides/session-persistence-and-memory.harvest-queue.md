# Co-occurrence Harvest Queue — Session Persistence and Memory

Embedded artifact candidates surfaced during `/synthesize-guide` runs. Per DD-101.
Nothing here is auto-extracted; rows feed `/extract-artifacts` only after Nick rules.

| Date queued | Status | Target form | Source finding | Suggested headline | Recommendation |
|---|---|---|---|---|---|
| 2026-04-26 | queued | rule | [[memorymd-cross-session-preference-persistence]] | agent-must-read-and-update-memory-md-on-startup | extract via /extract-artifacts |
| 2026-04-26 | queued | rule | [[ground-truth-environmental-feedback-loops]] | verify-with-environmental-feedback-not-self-assessment | extract via /extract-artifacts |
| 2026-04-26 | queued | skill | [[file-based-task-locking-parallel-agents]] | filesystem-lock-parallel-agent-coordination | extract via /extract-artifacts |
| 2026-04-26 | queued | skill | [[structured-fact-extraction-from-conversations]] | structured-fact-extraction-from-agent-turn | extract via /extract-artifacts |
| 2026-04-26 | queued | rule | [[effort-scaling-rules-embedded-in-orchestrator]] | tier-based-orchestrator-effort-scaling-rules | extract via /extract-artifacts |
| 2026-04-26 | queued | rule | [[incremental-one-feature-per-session-pattern]] | one-feature-per-session-clean-state-exit | dismiss as inline |
| 2026-04-26 | queued | template | [[memory-bank-isolation-per-agent-per-project]] | memory-bank-isolation-config-template | dismiss as inline |
| 2026-04-26 | queued | skill | [[ace-agentic-context-engineering-rag-based]] | ace-generator-reflector-curator-loop | dismiss as inline |

## Per-row details

### memorymd-cross-session-preference-persistence::rule::agent-must-read-and-update-memory-md-on-startup

- **Date queued:** 2026-04-26
- **Status:** queued
- **Target form:** rule
- **Source finding:** [[memorymd-cross-session-preference-persistence]]
- **Source excerpt:**
  > "Read memory.md on startup. When you learn something new or are corrected, update the relevant section in memory.md immediately. Keep memory.md current."
- **Codifier's reading:** Clean rule-shape — imperative voice, machine-enforceable directive intended for system-prompt injection. Fits the rule artifact form per the form-classification rubric: scope-bounded (memory.md), declarative obligation (read/update), single concern. Independently deployable as a project-level rule on any agent harness that supports CLAUDE.md-style context files.
- **Suggested headline:** agent-must-read-and-update-memory-md-on-startup
- **Recommendation:** extract via /extract-artifacts
- **Resolution:** _(awaiting Nick's ruling)_

### ground-truth-environmental-feedback-loops::rule::verify-with-environmental-feedback-not-self-assessment

- **Date queued:** 2026-04-26
- **Status:** queued
- **Target form:** rule
- **Source finding:** [[ground-truth-environmental-feedback-loops]]
- **Source excerpt:**
  > "The agent obtains concrete environmental feedback (test results, tool outputs, API responses) at each decision point. Self-assessment is unreliable because the same model that made the mistake evaluates whether a mistake was made."
- **Codifier's reading:** Rule-shape — a hard prohibition against self-assessment paired with a positive obligation to obtain environmental signal at each decision point. Machine-enforceable in agent harnesses by detecting decision points without preceding tool calls. Broadly applicable across IL skills (research-loop, identify-artifacts, extract-artifacts, synthesize-guide) and S2/S3 agent work generally.
- **Suggested headline:** verify-with-environmental-feedback-not-self-assessment
- **Recommendation:** extract via /extract-artifacts
- **Resolution:** _(awaiting Nick's ruling)_

### file-based-task-locking-parallel-agents::skill::filesystem-lock-parallel-agent-coordination

- **Date queued:** 2026-04-26
- **Status:** queued
- **Target form:** skill
- **Source finding:** [[file-based-task-locking-parallel-agents]]
- **Source excerpt:**
  > "Per-agent workflow: 1. Acquire lock: atomic file creation in locks/ named after the task. 2. Pull and merge from upstream. 3. Work on the claimed task. 4. Push changes to upstream. 5. Remove the lock file."
- **Codifier's reading:** Skill-shape — a five-step procedure with a clear invocation contract (input: task name; output: completed task + released lock). The lock-acquisition primitive (atomic file creation) and the cleanup step are well-bounded. Fits skill artifact form: procedure with input/output, step-by-step structure, deployable as a callable workflow.
- **Suggested headline:** filesystem-lock-parallel-agent-coordination
- **Recommendation:** extract via /extract-artifacts
- **Resolution:** _(awaiting Nick's ruling)_

### structured-fact-extraction-from-conversations::skill::structured-fact-extraction-from-agent-turn

- **Date queued:** 2026-04-26
- **Status:** queued
- **Target form:** skill
- **Source finding:** [[structured-fact-extraction-from-conversations]]
- **Source excerpt:**
  > "Extract discrete structured facts in the background after each agent turn... Facts should include: type, text content, timestamp, entities involved, and confidence score."
- **Codifier's reading:** Skill-shape — a post-turn extraction procedure with explicit input (conversation turn), structured output (typed facts with provenance), and invocation contract (background, after each turn). The output schema (type / content / timestamp / entities / confidence) is well-defined enough to be a skill contract. Could be deployed as a Claude Code hook or as a periodic background skill.
- **Suggested headline:** structured-fact-extraction-from-agent-turn
- **Recommendation:** extract via /extract-artifacts
- **Resolution:** _(awaiting Nick's ruling)_

### effort-scaling-rules-embedded-in-orchestrator::rule::tier-based-orchestrator-effort-scaling-rules

- **Date queued:** 2026-04-26
- **Status:** queued
- **Target form:** rule
- **Source finding:** [[effort-scaling-rules-embedded-in-orchestrator]]
- **Source excerpt:**
  > "Tier 1 (Simple factual): 1 subagent, 3-10 tool calls. Tier 2 (Comparison/synthesis): 2-4 subagents, 10-15 tool calls. Tier 3 (Complex multi-source research): 10+ subagents, divided roles."
- **Codifier's reading:** Rule-shape — explicit resource-allocation directive that an orchestrator agent should consult before spawning subagents. The finding's title literally names them as "rules"; the tier-based table provides the enforceable thresholds. Fits rule artifact form: imperative, scope-bounded (orchestrator prompts), machine-enforceable via spawn-time check.
- **Suggested headline:** tier-based-orchestrator-effort-scaling-rules
- **Recommendation:** extract via /extract-artifacts
- **Resolution:** _(awaiting Nick's ruling)_

### incremental-one-feature-per-session-pattern::rule::one-feature-per-session-clean-state-exit

- **Date queued:** 2026-04-26
- **Status:** queued
- **Target form:** rule
- **Source finding:** [[incremental-one-feature-per-session-pattern]]
- **Source excerpt:**
  > "Each session implements exactly one focused objective and leaves the system in a production-mergeable state."
- **Codifier's reading:** Rule-shape — imperative directive about session scope and exit-state. Machine-enforceable via session-handoff hooks (verify single objective declared at session start; verify clean state at session close). However, this principle is already deeply embedded in MetaSystem session-handoff conventions and IL governance; codifying as a separate rule artifact would duplicate enforcement that already lives in the handoff prompts and session-handoff skill.
- **Suggested headline:** one-feature-per-session-clean-state-exit
- **Recommendation:** dismiss as inline
- **Resolution:** _(awaiting Nick's ruling)_

### memory-bank-isolation-per-agent-per-project::template::memory-bank-isolation-config-template

- **Date queued:** 2026-04-26
- **Status:** queued
- **Target form:** template
- **Source finding:** [[memory-bank-isolation-per-agent-per-project]]
- **Source excerpt:**
  > "bankId (default: 'claude_code'): Names the memory bank. bankMission: Tells the memory engine who this agent is. retainMission: Guides what the memory engine should remember. HINDSIGHT_CHANNEL_ID: Isolates memories per messaging channel. HINDSIGHT_USER_ID: Isolates memories per user."
- **Codifier's reading:** Template-shape — a structural scaffold of named configuration keys with per-key descriptions. Concrete (Hindsight-specific) but generalizable to any memory-isolation framework. The shape (key + role + isolation-axis) is template form per the form-classification rubric. However, this scaffold has already been absorbed into the guide's `Memory Architecture Specification` template (see the `bank_isolation` block, Step 1.4); a separate template artifact would duplicate that surface.
- **Suggested headline:** memory-bank-isolation-config-template
- **Recommendation:** dismiss as inline
- **Resolution:** _(awaiting Nick's ruling)_

### ace-agentic-context-engineering-rag-based::skill::ace-generator-reflector-curator-loop

- **Date queued:** 2026-04-26
- **Status:** queued
- **Target form:** skill
- **Source finding:** [[ace-agentic-context-engineering-rag-based]]
- **Source excerpt:**
  > "(1) a Generator that semantically retrieves the top-k most relevant behavioral bullets from a vector DB and executes the task with those bullets in context; (2) a Reflector that analyzes the execution trace and extracts new if/then lesson candidates; (3) a Curator that embeds new bullets, deduplicates against existing ones, updates helpful/harmful vote counts per bullet."
- **Codifier's reading:** Skill-shape — three-stage pipeline with named components, each having clear input/output/invocation contracts. ACE is treated in source literature as a deployable system. However, ACE is more architectural-pattern than single-skill: it requires a vector DB, a reflector loop, a curator loop, and a binary success signal. Extracting as a single IL skill would mis-scope it. Better deployed (when MetaSystem reaches RAG scale) as a system upgrade documented in the guide, not as a self-contained skill artifact.
- **Suggested headline:** ace-generator-reflector-curator-loop
- **Recommendation:** dismiss as inline
- **Resolution:** _(awaiting Nick's ruling)_
