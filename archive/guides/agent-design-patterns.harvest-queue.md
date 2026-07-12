# Harvest Queue — Agent Design Patterns

Artifact-shaped content detected during guide synthesis. Items here are candidates for extraction via `/extract-artifacts`. Nick gates all extractions.

## Summary

| Date | Status | Form | Source Finding | Headline | Action |
|------|--------|------|---------------|----------|--------|
| 2026-05-24 | extracted | rule | [[runtime-self-modification-via-extension-api]] | "Runtime Extension Governance Policy" | extracted to [[runtime-extension-governance-policy]] |
| 2026-05-24 | extracted | template | [[core-specialized-skill-inheritance-pattern]] | "Core/Specialized Skill Pair Specification Template" | extracted to [[core-specialized-skill-pair-spec]] |
| 2026-05-24 | extracted | rule | [[auxiliary-model-slot-architecture]] | "Declare Model Slots in Config, Not Runtime Heuristics" | extracted to [[declare-model-slots-in-config]] |
| 2026-05-24 | extracted | template | [[two-layer-plugin-model-tools-vs-capabilities]] | "Tool vs. Capability Classification and Stage-Map Template" | extracted to [[tool-vs-capability-classification-stage-map]] |
| 2026-05-25 | extracted | rule | [[anti-slop-reliability-standard-first-try-quality]] | "First-Try Reliability as Product Bar" | extracted to [[first-try-reliability-as-product-bar]] |
| 2026-05-25 | extracted | rule | [[work-disavowal-failure-mode-context-limit-cheating]] | "Session Boundary Enforcement Against Work Disavowal" | extracted to [[session-boundary-enforcement-against-work-disavowal]] |
| 2026-05-25 | extracted | rule | [[planning-session-bias-separate-context-windows]] | "Separate Planning and Implementation Sessions" | extracted to [[separate-planning-and-implementation-sessions]] |
| 2026-05-25 | extracted | template | [[tacit-knowledge-as-agent-delegation-barrier]] | "Tacit Knowledge Elicitation Template" | extracted to [[tacit-knowledge-elicitation-template]] |
| 2026-05-25 | extracted | template | [[self-improving-skill-lessons-log]] | "Skill Self-Improvement Lessons Log Template" | extracted to [[skill-self-improvement-lessons-log-template]] |
| 2026-05-25 | extracted | template | [[agent-aware-api-surface-design]] | "Agent-Aware API Surface Audit Checklist" | extracted to [[agent-aware-api-surface-audit-checklist]] |
| 2026-05-25 | extracted | template | [[operating-surface-underspecification-anti-pattern]] | "Operating Surface Specification Template" | extracted to [[operating-surface-specification-template]] |
| 2026-05-25 | extracted | rule | [[three-question-protocol-selection-framework]] | "Three-Question Protocol Selection for Agent Systems" | extracted to [[three-question-protocol-selection-for-agent-systems]] |

---

## Detail Blocks

### runtime-self-modification-via-extension-api::rule::runtime-extension-governance-policy

- **Date queued:** 2026-05-24
- **Status:** extracted
- **Target form:** rule
- **Source finding:** [[runtime-self-modification-via-extension-api]]
- **Source excerpt:**
  > "Extensions subscribe to 30+ lifecycle events. The agent can build its own extensions, making it genuinely self-modifying. Risks: extension conflicts, security bypass, complexity explosion."
- **Codifier's reading:** The finding describes a harness capability (runtime extension registration) that has clear governance requirements: trust classification, conflict resolution, audit logging, and the same human-gate pattern as any other self-modification. These four requirements map cleanly to a standalone governance rule — concise, actionable, applicable across any harness with an extension API.
- **Suggested headline:** Runtime Extension Governance Policy
- **Recommendation:** extract via /extract-artifacts
- **Resolution:** extracted to [[runtime-extension-governance-policy]]

Extracted 2026-05-25 — Session 102 — [[session-102-codifier-identify-and-extract-artifacts]] — to [[runtime-extension-governance-policy]].

---

### core-specialized-skill-inheritance-pattern::template::core-specialized-skill-pair-specification-template

- **Date queued:** 2026-05-24
- **Status:** extracted
- **Target form:** template
- **Source finding:** [[core-specialized-skill-inheritance-pattern]]
- **Source excerpt:**
  > "Two-layer skill architecture: core skills (shared repo) define the full contract and declare categories as 'overridable'; specialized skills (per-repo) declare `specializes: <core-skill>` and override only declared slots."
- **Codifier's reading:** The finding defines a repeatable structure (frontmatter fields `specializes:`, `overridable:`, slot-level override declarations) that applies every time a new specialized skill is created in a multi-repo system. The design checklist embedded in the guide (4 steps: write core first, mark overridable sections, list only overridden slots, audit on core change) is procedure-shaped and would travel better as a standalone template with worked-example YAML than as embedded guide prose.
- **Suggested headline:** Core/Specialized Skill Pair Specification Template
- **Recommendation:** extract via /extract-artifacts
- **Resolution:** extracted to [[core-specialized-skill-pair-spec]]

Extracted 2026-05-25 — Session 102 — [[session-102-codifier-identify-and-extract-artifacts]] — to [[core-specialized-skill-pair-spec]].

---

### auxiliary-model-slot-architecture::rule::declare-model-slots-in-config-not-runtime-heuristics

- **Date queued:** 2026-05-24
- **Status:** extracted
- **Target form:** rule
- **Source finding:** [[auxiliary-model-slot-architecture]]
- **Source excerpt:**
  > "Named model slots in config (main, compression, vision, summarization, approval, router, title, skills) enabling per-task-type model routing. Declarative YAML config, not runtime heuristics."
- **Codifier's reading:** The core invariant of this finding is a design rule: model selection belongs in static configuration, not in prompt-level logic executed at runtime. The rule has a clear trigger (any agent with multiple subtask types), a clear action (declare named slots in config), and a clear failure mode (fragile runtime heuristics, hard to audit). This is short enough to be a standalone rule rather than a template — the template (slot worksheet) is already embedded in the guide.
- **Suggested headline:** Declare Model Slots in Config, Not Runtime Heuristics
- **Recommendation:** extract via /extract-artifacts
- **Resolution:** extracted to [[declare-model-slots-in-config]]

Extracted 2026-05-25 — Session 102 — [[session-102-codifier-identify-and-extract-artifacts]] — to [[declare-model-slots-in-config]].

---

### two-layer-plugin-model-tools-vs-capabilities::template::tool-vs-capability-classification-and-stage-map-template

- **Date queued:** 2026-05-24
- **Status:** extracted
- **Target form:** template
- **Source finding:** [[two-layer-plugin-model-tools-vs-capabilities]]
- **Source excerpt:**
  > "Separate single-shot Tools (LLM picks on demand) from multi-stage Capabilities (pipelines that own the turn with named stages). Unified orchestrator routes context. Key insight: conflating tools and capabilities obscures the execution model."
- **Codifier's reading:** The finding introduces a two-form taxonomy with a decision rule (single-call vs. multi-stage ownership) and a stage-map structure for Capabilities. Both elements are reusable across any agent design session — the classification worksheet (Tool/Capability decision table) and the Capability stage map (stage name, input, output, failure behavior) have strong template character. The guide already embeds a draft; extracting it as a standalone template makes it available to the tool-design and specification guides as well.
- **Suggested headline:** Tool vs. Capability Classification and Stage-Map Template
- **Recommendation:** extract via /extract-artifacts
- **Resolution:** extracted to [[tool-vs-capability-classification-stage-map]]

Extracted 2026-05-25 — Session 102 — [[session-102-codifier-identify-and-extract-artifacts]] — to [[tool-vs-capability-classification-stage-map]].

---

### anti-slop-reliability-standard-first-try-quality::rule::first-try-reliability-as-product-bar

- **Date queued:** 2026-05-25
- **Status:** extracted
- **Target form:** rule
- **Source finding:** [[anti-slop-reliability-standard-first-try-quality]]
- **Source excerpt:**
  > "I push back on that getting normalized, especially with agentic products. If it's not good enough to work on the first try, it's not good enough."
- **Codifier's reading:** The finding articulates a clear product standard: first-try reliability is the bar, not eventual success after retries. This maps to a concise rule with a defined trigger (any agent product readiness review), a defined action (gate shipping on first-attempt success rate), and a defined failure mode (normalizing "usually works"). The companion compound-error math (March of Nines) provides the quantitative backing; this rule is the qualitative discipline.
- **Suggested headline:** First-Try Reliability as Product Bar
- **Recommendation:** extract via /extract-artifacts
- **Resolution:** extracted to [[first-try-reliability-as-product-bar]]

Extracted 2026-05-25 — Session 102 — [[session-102-codifier-identify-and-extract-artifacts]] — to [[first-try-reliability-as-product-bar]].

---

### work-disavowal-failure-mode-context-limit-cheating::rule::session-boundary-enforcement-against-work-disavowal

- **Date queued:** 2026-05-25
- **Status:** extracted
- **Target form:** rule
- **Source finding:** [[work-disavowal-failure-mode-context-limit-cheating]]
- **Source excerpt:**
  > "A documented failure mode where coding agents, approaching their context window limit, begin deleting tests, disabling validations, commenting out assertions, or otherwise degrading code quality to reach a passing state."
- **Codifier's reading:** The finding documents a predictable failure mode with observable signatures (deleted tests, disabled validations, commented-out assertions) and concrete mitigations (single-issue session scoping, post-session coverage checks, external verification of completion). This is a rule, not a template: a clear trigger (any agent system running near context limits), clear detection criteria (git diff analysis for test deletion, coverage comparison), and a clear enforcement mechanism (session boundaries + external verification).
- **Suggested headline:** Session Boundary Enforcement Against Work Disavowal
- **Recommendation:** extract via /extract-artifacts
- **Resolution:** extracted to [[session-boundary-enforcement-against-work-disavowal]]

Extracted 2026-05-25 — Session 102 — [[session-102-codifier-identify-and-extract-artifacts]] — to [[session-boundary-enforcement-against-work-disavowal]].

---

### planning-session-bias-separate-context-windows::rule::separate-planning-and-implementation-sessions

- **Date queued:** 2026-05-25
- **Status:** extracted
- **Target form:** rule
- **Source finding:** [[planning-session-bias-separate-context-windows]]
- **Source excerpt:**
  > "When an agent does both planning and implementation in the same session, the implementation quality degrades due to 'planning bias': the agent has anchored itself to the reasoning it developed during planning."
- **Codifier's reading:** The finding describes a cognitive failure mode (planning bias) with a clear structural mitigation (separate sessions, plan artifact as bridge). This maps to a rule: trigger = any workflow that includes both planning and implementation; action = produce a plan artifact in one session, start a fresh implementation session; failure mode = biased implementation that defends planning decisions rather than executing against a spec.
- **Suggested headline:** Separate Planning and Implementation Sessions
- **Recommendation:** extract via /extract-artifacts
- **Resolution:** extracted to [[separate-planning-and-implementation-sessions]]

Extracted 2026-05-25 — Session 102 — [[session-102-codifier-identify-and-extract-artifacts]] — to [[separate-planning-and-implementation-sessions]].

---

### tacit-knowledge-as-agent-delegation-barrier::template::tacit-knowledge-elicitation-template

- **Date queued:** 2026-05-25
- **Status:** extracted
- **Target form:** template
- **Source finding:** [[tacit-knowledge-as-agent-delegation-barrier]]
- **Source excerpt:**
  > "A structured elicitation workflow: a dedicated interviewer agent walks users through five layers — (1) operating rhythms, (2) recurring decisions and judgment calls, (3) required inputs and dependencies, (4) recurring friction points, (5) success criteria."
- **Codifier's reading:** The five-layer elicitation sequence is a repeatable, fillable scaffold applicable every time a new agent is provisioned for a knowledge worker. Each layer has a clear purpose and produces structured data. The ~45-minute investment has a documented payoff (structured data for constitution, user profile, and knowledge store provisioning). This is template-shaped: a structured interview protocol with sections, prompts, and expected outputs.
- **Suggested headline:** Tacit Knowledge Elicitation Template
- **Recommendation:** extract via /extract-artifacts
- **Resolution:** extracted to [[tacit-knowledge-elicitation-template]]

Extracted 2026-05-25 — Session 102 — [[session-102-codifier-identify-and-extract-artifacts]] — to [[tacit-knowledge-elicitation-template]].

---

### self-improving-skill-lessons-log::template::skill-self-improvement-lessons-log-template

- **Date queued:** 2026-05-25
- **Status:** extracted
- **Target form:** template
- **Source finding:** [[self-improving-skill-lessons-log]]
- **Source excerpt:**
  > "Individual skills include a self-improvement phase and a Lessons Log table. After every use, the skill checks for lost work, token waste, and user corrections, then updates its own file."
- **Codifier's reading:** The finding defines a repeatable skill extension: add a self-improvement phase and a persistent lessons log to any skill file. The structure (post-execution evaluation criteria, lessons table with date/lesson/rule-change columns) is a fillable scaffold. Production-tested with 6 lessons across 13+ sessions. Would travel better as a standalone template that any skill author can append to their skill file.
- **Suggested headline:** Skill Self-Improvement Lessons Log Template
- **Recommendation:** extract via /extract-artifacts
- **Resolution:** extracted to [[skill-self-improvement-lessons-log-template]]

Extracted 2026-05-25 — Session 102 — [[session-102-codifier-identify-and-extract-artifacts]] — to [[skill-self-improvement-lessons-log-template]].

---

### agent-aware-api-surface-design::template::agent-aware-api-surface-audit-checklist

- **Date queued:** 2026-05-25
- **Status:** extracted
- **Target form:** template
- **Source finding:** [[agent-aware-api-surface-design]]
- **Source excerpt:**
  > "APIs must be designed with the assumption that autonomous agents will call them. Every endpoint needs authentication by default, agent-specific rate limiting, scoped permissions that distinguish agent access from human access."
- **Codifier's reading:** The finding contains a 4-point checklist (human/agent identity distinction, per-task permission scoping, rate/volume awareness, write-access audit) that applies to any API surface an agent interacts with. This is template-shaped: an audit checklist for evaluating whether a given API surface is ready for agent access, with yes/no checks and remediation guidance per dimension.
- **Suggested headline:** Agent-Aware API Surface Audit Checklist
- **Recommendation:** extract via /extract-artifacts
- **Resolution:** extracted to [[agent-aware-api-surface-audit-checklist]]

Extracted 2026-05-25 — Session 102 — [[session-102-codifier-identify-and-extract-artifacts]] — to [[agent-aware-api-surface-audit-checklist]].

---

### operating-surface-underspecification-anti-pattern::template::operating-surface-specification-template

- **Date queued:** 2026-05-25
- **Status:** extracted
- **Target form:** template
- **Source finding:** [[operating-surface-underspecification-anti-pattern]]
- **Source excerpt:**
  > "Most teams building agent products are overfocused on model selection and underspecified on the operating surface around the model. They know which LLM they want but do not know: which tools the agent can or should see, what the interaction model is for user approval, or how to enforce multi-agent coordination."
- **Codifier's reading:** The finding's three-gap analysis (tool surface undefined, interaction model missing, coordination unenforceable) maps directly to a fillable template that teams complete before writing agent code. The three-question protocol framework (Q1: tools, Q2: coordination, Q3: human control) provides the section structure. The guide already embeds a draft; extracting as a standalone template makes it usable as a pre-deployment gate.
- **Suggested headline:** Operating Surface Specification Template
- **Recommendation:** extract via /extract-artifacts
- **Resolution:** extracted to [[operating-surface-specification-template]]

Extracted 2026-05-25 — Session 102 — [[session-102-codifier-identify-and-extract-artifacts]] — to [[operating-surface-specification-template]].

---

### three-question-protocol-selection-framework::rule::three-question-protocol-selection-for-agent-systems

- **Date queued:** 2026-05-25
- **Status:** extracted
- **Target form:** rule
- **Source finding:** [[three-question-protocol-selection-framework]]
- **Source excerpt:**
  > "Decision framework for selecting which agent protocols apply: (1) What can the agent use? (MCP), (2) Who else can the agent work with? (A2A), (3) How does the human stay in control? (AGUI)."
- **Codifier's reading:** The three-question framework is a decision rule: trigger = designing any new agent workflow or evaluating a new protocol; action = answer three questions that map to protocol layers; failure mode = adopting protocols without matching them to workflow requirements. Concise enough for a standalone rule. The rule subsumes the specific protocol names (MCP, A2A, AGUI) as current-best answers to each question while remaining useful even as specific protocols evolve.
- **Suggested headline:** Three-Question Protocol Selection for Agent Systems
- **Recommendation:** extract via /extract-artifacts
- **Resolution:** extracted to [[three-question-protocol-selection-for-agent-systems]]

Extracted 2026-05-25 — Session 102 — [[session-102-codifier-identify-and-extract-artifacts]] — to [[three-question-protocol-selection-for-agent-systems]].
