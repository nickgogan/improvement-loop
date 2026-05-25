# Co-occurrence Harvest Queue — Managing Agent Context

Embedded artifact candidates surfaced during `/synthesize-guide` runs. Per DD-101.
Nothing here is auto-extracted; rows feed `/extract-artifacts` only after Nick rules.

| Date queued | Status | Target form | Source finding | Suggested headline | Recommendation |
|---|---|---|---|---|---|
| 2026-04-26 | extracted | rule | [[catastrophic-context-collapse-risk-during-claudemd]] | "Never ask Claude to compact CLAUDE.md" | extracted to [[never-ask-claude-to-compact-claudemd]] |
| 2026-04-26 | extracted | rule | [[claudemd-context-rot-from-indiscriminate-rule-accu]] | "CLAUDE.md global rule cap" | merged into [[claudemd-minimum-viable-rule-only-add-globally-true-lines]] |
| 2026-04-26 | extracted | skill | [[trajectory-engineering-non-linear-session-forking]] | "/re Fork-and-Trim Trajectory Procedure" | extracted to [[re-fork-and-trim-trajectory-procedure]] |
| 2026-04-26 | extracted | template | [[progress-md-session-bridge]] | "PROGRESS.md Session Bridge Template" | extracted to [[progressmd-session-bridge-template]] |
| 2026-04-26 | extracted | template | [[response-format-enum-for-adaptive-verbosity]] | "Tool Response-Format Enum (detailed / concise)" | extracted to [[tool-response-format-enum]] |
| 2026-04-26 | extracted | rule | [[skills-as-pointers-to-second-brain-files]] | "Skills reference shared context by path, not by copy" | extracted to [[skills-reference-shared-context-by-path]] |
| 2026-04-26 | extracted | rule | [[ace-delta-updates-over-monolithic-rewrites]] | "Evolving context docs use delta updates, never monolithic LLM rewrites" | merged into [[never-ask-claude-to-compact-claudemd]] |
| 2026-04-26 | extracted | rule | [[ide-context-streaming-silent-token-tax]] | "Close irrelevant IDE files during agent sessions" | extracted to [[close-irrelevant-ide-files-during-agent-sessions]] |
| 2026-04-26 | extracted | rule | [[model-specific-context-file-sensitivity]] | "Test context strategies against your actual model" | extracted to [[test-context-strategies-against-actual-model]] |
| 2026-04-26 | nick-dismissed | template | [[five-context-management-techniques-in-claude-code]] | "Context-Management Technique Selector" | dismiss as inline |
| 2026-04-26 | nick-dismissed | template | [[cross-platform-context-file-strategy]] | "Multi-Tool Context Mirror Map" | dismiss as inline |
| 2026-04-26 | nick-dismissed | template | [[self-describing-codebase-structural-semantic-context]] | "Module Manifest Template" | dismiss as inline |
| 2026-04-26 | nick-dismissed | template | [[monorepo-context-distribution-three-strategies]] | "Monorepo Context Distribution Decision Matrix" | dismiss as inline |
| 2026-04-26 | nick-dismissed | template | [[three-layer-folder-as-workspace-architecture]] | "Three-Layer Folder-as-Workspace Scaffold" | dismiss as inline |
| 2026-04-26 | nick-dismissed | template | [[three-tier-vault-architecture-global-shared-local]] | "Three-Tier Vault Architecture (Global/Shared/Local)" | dismiss as inline |
| 2026-04-26 | nick-dismissed | rule | [[session-atomicity-single-issue-scope-quadratic-cost-reduction]] | "Bound each agent session to a single atomic issue" | dismiss as inline |
| 2026-05-24 | extracted | rule | [[bounded-tiered-memory-inference-driven-curation]] | "Apply hard character ceilings to agent memory files" | extracted to [[apply-hard-ceilings-to-agent-memory-files]] |
| 2026-05-24 | extracted | template | [[bounded-tiered-memory-inference-driven-curation]] | "Tiered Memory File Architecture (hot/warm/cold)" | extracted to [[tiered-memory-file-architecture]] |
| 2026-05-24 | extracted | rule | [[write-time-vs-query-time-synthesis-kb-poisoning]] | "Synthesize KB content at query time; never re-index LLM-authored output" | merged into [[never-ask-claude-to-compact-claudemd]] |
| 2026-05-24 | extracted | skill | [[orchestrator-headless-dispatch-context-isolation]] | "Headless Subprocess Dispatch Procedure" | merged into [[build-loop-skill-autonomous-phase-driver]] |
| 2026-05-25 | extracted | rule | [[claude-code-context-management-decision-matrix-five-tools]] | "Use /rewind for corrections; forward-patching accumulates failed context" | extracted to [[use-rewind-for-corrections-not-forward-patching]] |
| 2026-05-25 | extracted | rule | [[proactive-compaction-before-intelligence-degradation]] | "Compact proactively at stable checkpoints; model is least intelligent at capacity" | merged into [[context-degradation-40-percent-threshold]] |
| 2026-05-25 | extracted | template | [[inline-scoped-mcp-servers-per-subagent]] | "Subagent-scoped MCP server inline frontmatter definition" | extracted to [[subagent-scoped-mcp-server-inline-frontmatter]] |
| 2026-05-25 | extracted | rule | [[file-search-outperforms-rag-for-small-corpora]] | "Default to file search; add semantic search only at corpus scale threshold" | extracted to [[default-to-file-search-before-rag]] |
| 2026-05-25 | extracted | rule | [[summary-gate-agent-traversal-pattern]] | "Every knowledge node carries mandatory one-sentence summary for agent triage" | extracted to [[knowledge-node-mandatory-summary-field]] |

## Per-row details

### catastrophic-context-collapse-risk-during-claudemd::rule::never-ask-claude-to-compact-claudemd

- **Date queued:** 2026-04-26
- **Status:** extracted
- **Target form:** rule
- **Source finding:** [[catastrophic-context-collapse-risk-during-claudemd]]
- **Source excerpt:** "Each compaction step has a small but fixed probability (e.g., 3%, increasing by 0.25% per additional compaction) of producing a catastrophic rewrite — a context collapse where the entire file is reduced to a thin, unhelpful summary. After collapse, accuracy can drop to around 57% of previous performance, often below the baseline of having no CLAUDE.md at all."
- **Codifier's reading:** Imperative directive ("never ask Claude to summarize/compact your own CLAUDE.md"); machine-enforceable as a pre-commit hook against `claude /compact CLAUDE.md`-style invocations or a session-start check that detects suspiciously short CLAUDE.md vs git history. Fits rule artifact form per the form-classification rubric — directive + structural enforcement path. Companion artifacts: ACE-style voting curation procedure (separate skill candidate).
- **Suggested headline:** never-ask-claude-to-compact-claudemd
- **Recommendation:** extract via /extract-artifacts
- **Resolution:** extracted to [[never-ask-claude-to-compact-claudemd]]

Extracted 2026-04-27 — Session 82 — [[session-82-codifier-extract-artifacts-harvest-promotion-batch]] — to [[never-ask-claude-to-compact-claudemd]].

### claudemd-context-rot-from-indiscriminate-rule-accu::rule::claudemd-global-rule-cap

- **Date queued:** 2026-04-26
- **Status:** extracted
- **Target form:** rule
- **Source finding:** [[claudemd-context-rot-from-indiscriminate-rule-accu]]
- **Source excerpt:** "As users add rules to CLAUDE.md each time something goes wrong, the file grows and loads in full at the start of every session. The accumulation of context noise gradually reduces instruction-following quality and increases hallucination rates... Keep CLAUDE.md to 3-5 globally true, universally relevant lines."
- **Codifier's reading:** Imperative cap on CLAUDE.md global section; machine-enforceable via line-count check on the global Tier-0 section. Fits rule form. Note: a stricter version restricts to *global rules only*; project-specific rules go to per-project / per-skill files. The 60-80 line benchmark from Step 1 is a softer band; this rule names the harder Tier-0 cap.
- **Suggested headline:** claudemd-global-rule-cap
- **Recommendation:** extract via /extract-artifacts
- **Resolution:** merged into [[claudemd-minimum-viable-rule-only-add-globally-true-lines]]

Pending merge 2026-04-27 — Session 82 — [[session-82-codifier-extract-artifacts-harvest-promotion-batch]] — DD-97 extension proposal emitted at [[operations/extension-proposals/2026-04-27-claudemd-global-rule-cap-extension-proposal]]; primary match [[claudemd-minimum-viable-rule-only-add-globally-true-lines]]. Status remains `nick-approved` per DD-101 Branch C until Nick rules merge / separate / dismiss; on merge ruling, manually amend the existing rule then re-invoke this row to flip Status → `extracted`, Resolution → `merged into [[claudemd-minimum-viable-rule-only-add-globally-true-lines]]`.

Merged 2026-04-27 — Session 84 — [[session-84-codifier-reconcile-and-dd97-sweep]] — Option A applied per [[operations/extension-proposals/2026-04-27-claudemd-global-rule-cap-extension-proposal]] — into [[claudemd-minimum-viable-rule-only-add-globally-true-lines]]. Volume cap (Tier-0: 3-5 lines; Tier-1: 60-80 line band) integrated as operate-stage backstop alongside existing per-line global-truth test.

### trajectory-engineering-non-linear-session-forking::skill::re-fork-and-trim-trajectory-procedure

- **Date queued:** 2026-04-26
- **Status:** extracted
- **Target form:** skill
- **Source finding:** [[trajectory-engineering-non-linear-session-forking]]
- **Source excerpt:** "Pressing double-ESC (or using /re) activates a time-travel feature that returns to any prior point in the current session. Trajectory engineers use this not just to retry failed attempts, but proactively: (1) after a bug fix, they trim out the bug-fixing context (now irrelevant) by rewinding to before the bug was spotted, providing a brief summary of what happened and how it was fixed, then continuing from that clean state; (2) when exploring architectural options, they fork from a common starting point, run each option down its trajectory, compare results, and keep the best; (3) they intentionally keep sessions lean by trimming branches back to the trunk after each exploration."
- **Codifier's reading:** Procedural pattern with three named modes (trim-after-fix, fork-to-compare, trim-back-to-trunk); has clear inputs (current session state), outputs (lean session at chosen rewind point), and step-by-step structure. Fits skill form. Anthropic's 2026 framing promotes this from advanced practice to first-class default with `Esc+Esc` shortcut. Skill candidate would wrap the three modes with decision criteria + companion handoff-summary template.
- **Suggested headline:** re-fork-and-trim-trajectory-procedure
- **Recommendation:** extract via /extract-artifacts
- **Resolution:** extracted to [[re-fork-and-trim-trajectory-procedure]]

Extracted 2026-04-27 — Session 83 — [[session-83-codifier-ib164-resume-extract-artifacts]] — to [[re-fork-and-trim-trajectory-procedure]].

### progress-md-session-bridge::template::progressmd-session-bridge-template

- **Date queued:** 2026-04-26
- **Status:** extracted
- **Target form:** template
- **Source finding:** [[progress-md-session-bridge]]
- **Source excerpt:** "PROGRESS.md is a structured markdown file that serves as persistent working memory between Claude Code sessions. At session start, the agent reads it to orient itself; at session end, it writes an updated summary covering what was completed, what is in progress, what is blocked, and what comes next."
- **Codifier's reading:** Structural scaffold meant for rendering — has identifiable sections (Completed / In Progress / Blocked / Next Steps + optional Decisions/Assumptions/Risks), placeholder fields per session entry, structural form. Fits template artifact form. Worth extracting as a starter PROGRESS.md template that consumers can copy-and-fill, distinct from any specific deployment of it. The Anthropic CHANGELOG.md "lab notes" variant could be a sibling template or merged.
- **Suggested headline:** progressmd-session-bridge-template
- **Recommendation:** extract via /extract-artifacts
- **Resolution:** extracted to [[progressmd-session-bridge-template]]

Extracted 2026-04-27 — Session 83 — [[session-83-codifier-ib164-resume-extract-artifacts]] — to [[progressmd-session-bridge-template]].

### response-format-enum-for-adaptive-verbosity::template::tool-response-format-enum

- **Date queued:** 2026-04-26
- **Status:** extracted
- **Target form:** template
- **Source finding:** [[response-format-enum-for-adaptive-verbosity]]
- **Source excerpt:** "Add a response format parameter to tools that return variable-length results: Detailed (~206 tokens): Full metadata, IDs, and content for operation chaining. Concise (~72 tokens): High-signal summary for scanning and triage. This yields ~65% token reduction when the agent only needs a summary."
- **Codifier's reading:** Structural scaffold for tool definitions — the closed enum (`detailed | concise`) plus the per-mode token-budget guideline plus the agent-side selection heuristic together form a reusable template that tool authors can drop into any new tool definition. Fits template form. Likely a small artifact (one-page tool-design recipe + JSON schema fragment).
- **Suggested headline:** tool-response-format-enum
- **Recommendation:** extract via /extract-artifacts
- **Resolution:** extracted to [[tool-response-format-enum]]

Extracted 2026-04-27 — Session 83 — [[session-83-codifier-ib164-resume-extract-artifacts]] — to [[tool-response-format-enum]].

### skills-as-pointers-to-second-brain-files::rule::skills-reference-shared-context-by-path

- **Date queued:** 2026-04-26
- **Status:** extracted
- **Target form:** rule
- **Source finding:** [[skills-as-pointers-to-second-brain-files]]
- **Source excerpt:** "When a centralized second brain (Obsidian vault or equivalent) exists, skills should not embed copies of shared context documents inside their own reference folders. Instead, each skill's SKILL.md contains only: 1. The workflow/SOP the agent should follow. 2. File path references to where it should read context from within the second brain."
- **Codifier's reading:** Imperative directive applicable to skill authoring; machine-enforceable as a skill-audit rule that flags skill `references/` folders containing duplicated shared context. Fits rule form. Companion: the migration playbook (identify duplication → move to vault → replace with path) could be its own skill artifact.
- **Suggested headline:** skills-reference-shared-context-by-path
- **Recommendation:** extract via /extract-artifacts
- **Resolution:** extracted to [[skills-reference-shared-context-by-path]]

Extracted 2026-04-27 — Session 82 — [[session-82-codifier-extract-artifacts-harvest-promotion-batch]] — to [[skills-reference-shared-context-by-path]].

### ace-delta-updates-over-monolithic-rewrites::rule::evolving-docs-use-delta-updates

- **Date queued:** 2026-04-26
- **Status:** extracted
- **Target form:** rule
- **Source finding:** [[ace-delta-updates-over-monolithic-rewrites]]
- **Source excerpt:** "When context documents change over time (playbooks, progress files, accumulated notes), update incrementally — append structured entries, then periodically consolidate. Never rewrite the full document with an LLM, as brevity bias silently drops domain-specific details."
- **Codifier's reading:** Imperative directive ("never rewrite full document with an LLM"); machine-enforceable via a hook that detects whole-document rewrites of designated long-lived files (CLAUDE.md, PROGRESS.md, playbooks) and warns. Fits rule form. The Delta Update Entry template (already in this guide) is the companion structural artifact.
- **Suggested headline:** evolving-docs-use-delta-updates
- **Recommendation:** extract via /extract-artifacts
- **Resolution:** merged into [[never-ask-claude-to-compact-claudemd]]

Pending merge 2026-04-27 — Session 83 — [[session-83-codifier-ib164-resume-extract-artifacts]] — DD-97 extension proposal emitted at [[operations/extension-proposals/2026-04-27-evolving-docs-use-delta-updates-extension-proposal]]; primary match [[never-ask-claude-to-compact-claudemd]]. Manual apply per DD-97 v1 (Step 1.7 auto-merge prohibition); after apply, row Status flips to `extracted` and Resolution to `merged into [[never-ask-claude-to-compact-claudemd]]` via manual queue edit (or future skill mode).

Merged 2026-04-27 — Session 84 — [[session-84-codifier-reconcile-and-dd97-sweep]] — Option A applied per [[operations/extension-proposals/2026-04-27-evolving-docs-use-delta-updates-extension-proposal]] — into [[never-ask-claude-to-compact-claudemd]]. Scope generalized from CLAUDE.md/AGENTS.md/system-prompt files to all load-bearing evolving documents (PROGRESS.md, playbooks, accumulated notes); ACE-style voting curators promoted to fully-specified delta-update sub-rule; title shifted to "Evolving Load-Bearing Documents: No In-Place LLM Rewrite + Delta-Update Discipline."

### ide-context-streaming-silent-token-tax::rule::close-irrelevant-ide-files-during-agent-sessions

- **Date queued:** 2026-04-26
- **Status:** extracted
- **Target form:** rule
- **Source finding:** [[ide-context-streaming-silent-token-tax]]
- **Source excerpt:** "IDE context streaming silently injects open files and highlighted selections into the window without visual indication... every open file and highlighted selection in VS Code or JetBrains gets silently injected as context tokens. Close irrelevant files during agent sessions."
- **Codifier's reading:** Imperative practitioner rule; partially machine-enforceable via an IDE extension or pre-session hook that prompts the user to close non-task tabs. Fits rule form. The hidden-cost mechanism (10-20% of total context usage from IDE injection) is the rationale.
- **Suggested headline:** close-irrelevant-ide-files-during-agent-sessions
- **Recommendation:** extract via /extract-artifacts
- **Resolution:** extracted to [[close-irrelevant-ide-files-during-agent-sessions]]

Extracted 2026-04-27 — Session 83 — [[session-83-codifier-ib164-resume-extract-artifacts]] — to [[close-irrelevant-ide-files-during-agent-sessions]].

### model-specific-context-file-sensitivity::rule::test-context-strategies-against-actual-model

- **Date queued:** 2026-04-26
- **Status:** extracted
- **Target form:** rule
- **Source finding:** [[model-specific-context-file-sensitivity]]
- **Source excerpt:** "Different models respond dramatically differently to the same context files. One-size-fits-all context strategies are empirically wrong — optimize for the model you are actually using... What worked for Codex may not work for Claude Code, and vice versa."
- **Codifier's reading:** Imperative directive; testable as a contract that every context-file change runs a small eval against the deployment model before merging. Fits rule form. Closely tied to G4 (eval-driven optimization) — the rule names the requirement; G4 covers the eval mechanics.
- **Suggested headline:** test-context-strategies-against-actual-model
- **Recommendation:** extract via /extract-artifacts
- **Resolution:** extracted to [[test-context-strategies-against-actual-model]]

Extracted 2026-04-27 — Session 83 — [[session-83-codifier-ib164-resume-extract-artifacts]] — to [[test-context-strategies-against-actual-model]].

### five-context-management-techniques-in-claude-code::template::context-management-technique-selector

- **Date queued:** 2026-04-26
- **Status:** nick-dismissed
- **Target form:** template
- **Source finding:** [[five-context-management-techniques-in-claude-code]]
- **Source excerpt:** "Five distinct techniques manage context in Claude Code, with different cost/quality tradeoffs: sub-agent (fresh window), /re context trimming (selective cut), compaction (lossy compression), /handoff + /clear (structured summary), and /clear (destructive reset at break points). Preference order (best to worst): sub-agent > /handoff+/clear > context trimming > /clear > compaction."
- **Codifier's reading:** Decision-matrix template (technique × mechanism × time cost × quality × when-to-use). The matrix is now embedded as Step 4e of this guide; standalone extraction would duplicate the inline content without adding rendering value. Recommendation: dismiss as inline.
- **Suggested headline:** context-management-technique-selector
- **Recommendation:** dismiss as inline
- **Resolution:** dismissed

### cross-platform-context-file-strategy::template::multi-tool-context-mirror-map

- **Date queued:** 2026-04-26
- **Status:** nick-dismissed
- **Target form:** template
- **Source finding:** [[cross-platform-context-file-strategy]]
- **Source excerpt:** "Three distinct strategies for maintaining AI coding context files that work across multiple tools (Claude Code, GitHub Copilot, Cursor, Codex): platform-specific mirroring (Archon), chain-loader indirection (n8n), and content duplication (LangGraph)."
- **Codifier's reading:** Template/scaffold for documenting which context files live where across tools, with a strategy choice and a drift-detection mechanism. Now extracted as Template #7 (Multi-Tool Context Mirror Map) in this guide. Recommendation: dismiss as inline.
- **Suggested headline:** multi-tool-context-mirror-map
- **Recommendation:** dismiss as inline
- **Resolution:** dismissed

### self-describing-codebase-structural-semantic-context::template::module-manifest-template

- **Date queued:** 2026-04-26
- **Status:** nick-dismissed
- **Target form:** template
- **Source finding:** [[self-describing-codebase-structural-semantic-context]]
- **Source excerpt:** "Two distinct layers: Structural context (answers 'where'): Every module should have a manifest that describes: What the module does, What it depends on (dependencies in), What depends on it (dependencies out)... Semantic context (answers 'what'): Every interface should carry behavioral contracts that specify: Performance expectations, Failure modes, Retry semantics, Behavioral contracts."
- **Codifier's reading:** Structural template for module-level documentation; now embedded as Template #6 (Module Manifest Template) in this guide with a worked example. Standalone extraction would duplicate without adding rendering value. Recommendation: dismiss as inline.
- **Suggested headline:** module-manifest-template
- **Recommendation:** dismiss as inline
- **Resolution:** dismissed

### monorepo-context-distribution-three-strategies::template::monorepo-context-distribution-decision-matrix

- **Date queued:** 2026-04-26
- **Status:** nick-dismissed
- **Target form:** template
- **Source finding:** [[monorepo-context-distribution-three-strategies]]
- **Source excerpt:** "Three monorepo repos solve package-level AI context differently: n8n distributes CLAUDE.md→AGENTS.md chain-loaders per package (~44 packages), Archon uses path-scoped .claude/rules/*.md files that auto-load by directory (11 rules), and LangGraph uses a single global CLAUDE.md for all 8 libraries."
- **Codifier's reading:** Decision-matrix template; now embedded as Step 8e of this guide. Recommendation: dismiss as inline.
- **Suggested headline:** monorepo-context-distribution-decision-matrix
- **Recommendation:** dismiss as inline
- **Resolution:** dismissed

### three-layer-folder-as-workspace-architecture::template::three-layer-folder-as-workspace-scaffold

- **Date queued:** 2026-04-26
- **Status:** nick-dismissed
- **Target form:** template
- **Source finding:** [[three-layer-folder-as-workspace-architecture]]
- **Source excerpt:** "Layer 1 (Map): A root CLAUDE.md file that the agent always reads first... Layer 2 (Rooms): Each workspace subdirectory contains its own context markdown file specifying what that workspace does... Layer 3 (Workspace): The actual working files."
- **Codifier's reading:** Architectural scaffold for multi-workspace projects; now embedded as Step 8b of this guide. Recommendation: dismiss as inline.
- **Suggested headline:** three-layer-folder-as-workspace-scaffold
- **Recommendation:** dismiss as inline
- **Resolution:** dismissed

### three-tier-vault-architecture-global-shared-local::template::three-tier-vault-architecture

- **Date queued:** 2026-04-26
- **Status:** nick-dismissed
- **Target form:** template
- **Source finding:** [[three-tier-vault-architecture-global-shared-local]]
- **Source excerpt:** "Tier 1 (Global, ~/.claude/) for identity and universal skills; Tier 2 (Shared, git repo) for project reference files and playbooks; Tier 3 (Local, gitignored) for ephemeral state like PROGRESS.md, agent logs, and auth tokens."
- **Codifier's reading:** Architectural scaffold; now embedded as Step 8a of this guide with a tier table. Recommendation: dismiss as inline.
- **Suggested headline:** three-tier-vault-architecture
- **Recommendation:** dismiss as inline
- **Resolution:** dismissed

### session-atomicity-single-issue-scope-quadratic-cost-reduction::rule::bound-each-agent-session-to-single-atomic-issue

- **Date queued:** 2026-04-26
- **Status:** nick-dismissed
- **Target form:** rule
- **Source finding:** [[session-atomicity-single-issue-scope-quadratic-cost-reduction]]
- **Source excerpt:** "Bounding each agent session to exactly one fine-grained issue reduces context consumption quadratically relative to multi-task sessions, while improving decision quality. The mechanism: smaller scope means less prior context loaded, fewer intermediate states tracked, and cleaner handoffs."
- **Codifier's reading:** Imperative practitioner rule. Could be extracted as a standalone rule artifact, but the rule's enforcement is tightly coupled to having a persistent work queue (Beads / GitHub issues / equivalent) — without that infrastructure, the rule is unenforceable. The principle is now embedded as Step 5 defense #6 of this guide; standalone rule extraction is premature until issue-store infrastructure exists. Recommendation: dismiss as inline; revisit after IL adopts an issue-store pattern.
- **Suggested headline:** bound-each-agent-session-to-single-atomic-issue
- **Recommendation:** dismiss as inline
- **Resolution:** dismissed

### bounded-tiered-memory-inference-driven-curation::rule::apply-hard-ceilings-to-agent-memory-files

- **Date queued:** 2026-05-24
- **Status:** extracted
- **Target form:** rule
- **Source finding:** [[bounded-tiered-memory-inference-driven-curation]]
- **Source excerpt:** "Memory files have hard character ceilings (MEMORY.md ≤2,200 chars, USER.md ≤1,375 chars). Writes triggered by conversation-pattern inference, not explicit commands. A Curator step consolidates/evicts on overflow."
- **Codifier's reading:** Imperative directive with a quantified enforcement threshold (character ceiling). Machine-enforceable as a pre-write hook that checks the target file length before appending. The specific numbers (2,200 / 1,375 chars) are implementation-specific but the principle (hard ceiling + Curator-on-overflow) is generalizable. Companion: the tiered architecture template (separate row below) is the structural artifact that makes this rule operable. Fits rule form per rubric — directive + structural enforcement path.
- **Suggested headline:** apply-hard-ceilings-to-agent-memory-files
- **Recommendation:** extract via /extract-artifacts
- **Resolution:** extracted to [[apply-hard-ceilings-to-agent-memory-files]]

Pending merge 2026-05-25 — Session 102 — [[session-102-codifier-identify-and-extract-artifacts]] — DD-97 extension proposal emitted at [[operations/extension-proposals/2026-05-25-extension-proposals]]; primary match [[token-budget-pre-turn-projection]]. Manual apply per DD-97 v1 (Step 1.7 auto-merge prohibition); after apply, row Status flips to extracted and Resolution to merged into [[token-budget-pre-turn-projection]] via manual queue edit (or future skill mode).

Extracted 2026-05-25 — Session 103 — [[session-103-codifier-complete-extract-artifacts-write-phase]] — to [[apply-hard-ceilings-to-agent-memory-files]]. Nick ruled "create new" per extension proposals report; false positive on corpus match.

### bounded-tiered-memory-inference-driven-curation::template::tiered-memory-file-architecture

- **Date queued:** 2026-05-24
- **Status:** extracted
- **Target form:** template
- **Source finding:** [[bounded-tiered-memory-inference-driven-curation]]
- **Source excerpt:** "Three tiers: hot (always-injected), warm (FTS5 retrieved), cold (archival JSONL). Key insight: fixed ceilings + inference-driven writes + LLM curation = self-maintaining user model."
- **Codifier's reading:** Structural scaffold for memory file architecture — three-tier layout with named tiers, ceiling values, retrieval mechanism per tier, and Curator step procedure. Has identifiable structural form (tier table + Curator invocation protocol + eviction policy). Fits template form. The template would give consumers a copy-and-fill scaffold for implementing tiered memory in their agent harness. Distinct from the rule row above — rule governs the ceiling, template scaffolds the architecture.
- **Suggested headline:** tiered-memory-file-architecture
- **Recommendation:** extract via /extract-artifacts
- **Resolution:** extracted to [[tiered-memory-file-architecture]]

Extracted 2026-05-25 — Session 102 — [[session-102-codifier-identify-and-extract-artifacts]] — to [[tiered-memory-file-architecture]].

### write-time-vs-query-time-synthesis-kb-poisoning::rule::synthesize-at-query-time-never-re-index-llm-output

- **Date queued:** 2026-05-24
- **Status:** extracted
- **Target form:** rule
- **Source finding:** [[write-time-vs-query-time-synthesis-kb-poisoning]]
- **Source excerpt:** "Write-time synthesis (Karpathy pattern) trades trustworthiness for speed. Query-time synthesis preserves chain of custody but costs more. Three principles: immutable originals, structure over prose, query-time synthesis."
- **Codifier's reading:** Imperative directive with three named sub-rules (immutable originals, structure over prose, query-time synthesis). Machine-enforceable: a write-guard hook can detect when LLM-authored content is being written to a namespace that holds original sources. The "immutable originals" sub-rule is the strongest enforcement point. Relates to the existing `never-ask-claude-to-compact-claudemd` rule but broader — applies to any KB where agents both read and write, not just CLAUDE.md. Recommend extract as a standalone rule with the three sub-rules as a checklist; include the cost/latency tradeoff table as inline rationale.
- **Suggested headline:** synthesize-at-query-time-never-re-index-llm-output
- **Recommendation:** extract via /extract-artifacts
- **Resolution:** merged into [[never-ask-claude-to-compact-claudemd]]

Pending merge 2026-05-25 — Session 102 — [[session-102-codifier-identify-and-extract-artifacts]] — DD-97 extension proposal emitted at [[operations/extension-proposals/2026-05-25-extension-proposals]]; primary match [[never-ask-claude-to-compact-claudemd]]. Manual apply per DD-97 v1 (Step 1.7 auto-merge prohibition); after apply, row Status flips to extracted and Resolution to merged into [[never-ask-claude-to-compact-claudemd]] via manual queue edit (or future skill mode).

Merged 2026-05-25 — Session 103 — [[session-103-codifier-complete-extract-artifacts-write-phase]] — into [[never-ask-claude-to-compact-claudemd]].

### orchestrator-headless-dispatch-context-isolation::skill::headless-subprocess-dispatch-procedure

- **Date queued:** 2026-05-24
- **Status:** extracted
- **Target form:** skill
- **Source finding:** [[orchestrator-headless-dispatch-context-isolation]]
- **Source excerpt:** "Thin orchestrator dispatches each phase as separate headless subprocess. Each gets fresh context window. Orchestrator never accumulates work context — stays under 10% utilization after 100+ sessions."
- **Codifier's reading:** Procedural pattern with named inputs (phase prompt, explicit state from prior phase), outputs (phase result artifact, explicit state for next phase), and an invariant (orchestrator window utilization ≤10%). Has a clear skill form: a SKILL.md that codifies the dispatch procedure, the state-passing contract format (what goes in, what comes out), and the orchestrator keep-lean invariant. Distinct from `re-fork-and-trim-trajectory-procedure` (that skill handles single-session trajectory management via rewind; this skill handles multi-session/multi-phase process isolation). Strong candidate for extraction given the quantified invariant and the growing body of evidence (phase-dispatch pattern appears in multiple orchestrator architectures). The skill would include a worked example of the state-passing contract and a checklist for phase-prompt self-containment.
- **Suggested headline:** headless-subprocess-dispatch-procedure
- **Recommendation:** extract via /extract-artifacts
- **Resolution:** merged into [[build-loop-skill-autonomous-phase-driver]]

Pending merge 2026-05-25 — Session 102 — [[session-102-codifier-identify-and-extract-artifacts]] — DD-97 extension proposal emitted at [[operations/extension-proposals/2026-05-25-extension-proposals]]; primary match [[build-loop-skill-autonomous-phase-driver]]. Manual apply per DD-97 v1 (Step 1.7 auto-merge prohibition); after apply, row Status flips to extracted and Resolution to merged into [[build-loop-skill-autonomous-phase-driver]] via manual queue edit (or future skill mode).

Merged 2026-05-25 — Session 103 — [[session-103-codifier-complete-extract-artifacts-write-phase]] — into [[build-loop-skill-autonomous-phase-driver]].

### claude-code-context-management-decision-matrix-five-tools::rule::rewind-for-corrections

- **Date queued:** 2026-05-25
- **Status:** extracted
- **Target form:** rule
- **Source finding:** [[claude-code-context-management-decision-matrix-five-tools]]
- **Source excerpt:**
  > "Rewind is the default correction, not forward-patching. 'That didn't work, try X' accumulates both the failed attempt and the correction in context. /rewind drops the failed attempt cleanly."
- **Codifier's reading:** Imperative directive embedded within the broader 5-tool decision matrix. The rule is independently enforceable: when correcting a failed approach, use /rewind (drops the failed attempt) rather than forward-patching (which accumulates dead context). Machine-detectable via session analysis: consecutive "that didn't work, try X" patterns without /rewind indicate rule violation. The directive is one cell in the matrix but functions as a standalone operational rule.
- **Suggested headline:** rewind-for-corrections
- **Recommendation:** extract via /extract-artifacts
- **Resolution:** extracted to [[use-rewind-for-corrections-not-forward-patching]]

Extracted 2026-05-25 — Session 102 — [[session-102-codifier-identify-and-extract-artifacts]] — to [[use-rewind-for-corrections-not-forward-patching]].

### proactive-compaction-before-intelligence-degradation::rule::compact-proactively-at-checkpoints

- **Date queued:** 2026-05-25
- **Status:** extracted
- **Target form:** rule
- **Source finding:** [[proactive-compaction-before-intelligence-degradation]]
- **Source excerpt:**
  > "The model is at its least intelligent point when compacting. Compact proactively. Pick a stable checkpoint (task boundary, post-test-pass, after a successful file read sequence), invoke /compact with a steering hint, and do it while the model is still sharp."
- **Codifier's reading:** Imperative directive: "compact at stable checkpoints proactively, never at capacity pressure." Machine-enforceable as a heuristic trigger: detect stable-state signals (successful test pass, task completion, plan approval) and suggest /compact. The rule inverts the default mental model (compact = fallback) to compact = regular cadence tool. Independent of the broader context management pattern — the rule applies to any long-running Claude Code session.
- **Suggested headline:** compact-proactively-at-checkpoints
- **Recommendation:** extract via /extract-artifacts
- **Resolution:** merged into [[context-degradation-40-percent-threshold]]

Pending merge 2026-05-25 — Session 102 — [[session-102-codifier-identify-and-extract-artifacts]] — DD-97 extension proposal emitted at [[operations/extension-proposals/2026-05-25-extension-proposals]]; primary match [[context-degradation-40-percent-threshold]]. Manual apply per DD-97 v1 (Step 1.7 auto-merge prohibition); after apply, row Status flips to extracted and Resolution to merged into [[context-degradation-40-percent-threshold]] via manual queue edit (or future skill mode).

Merged 2026-05-25 — Session 103 — [[session-103-codifier-complete-extract-artifacts-write-phase]] — into [[context-degradation-40-percent-threshold]].

### inline-scoped-mcp-servers-per-subagent::template::subagent-inline-mcp-frontmatter

- **Date queued:** 2026-05-25
- **Status:** extracted
- **Target form:** template
- **Source finding:** [[inline-scoped-mcp-servers-per-subagent]]
- **Source excerpt:**
  > "Each entry in mcpServers is either a string reference to a session-wide server (shares the parent's connection) or an inline server definition (scoped to this subagent). Lifecycle-scoped: connects on start, disconnects on finish. Token-cost-scoped: tool descriptions don't consume parent context."
- **Codifier's reading:** Structural scaffold for subagent frontmatter: the mcpServers block with both reference (string) and inline (object with command/args/env) entries. Fill-in template with {{SERVER_NAME}}, {{COMMAND}}, {{ARGS}}, {{ENV}} slots. Distinct from the pattern (which argues why scoping matters) — the template is the concrete YAML shape that subagent authors copy-and-fill.
- **Suggested headline:** subagent-inline-mcp-frontmatter
- **Recommendation:** extract via /extract-artifacts
- **Resolution:** extracted to [[subagent-scoped-mcp-server-inline-frontmatter]]

Extracted 2026-05-25 — Session 102 — [[session-102-codifier-identify-and-extract-artifacts]] — to [[subagent-scoped-mcp-server-inline-frontmatter]].

### file-search-outperforms-rag-for-small-corpora::rule::default-file-search-over-rag

- **Date queued:** 2026-05-25
- **Status:** extracted
- **Target form:** rule
- **Source finding:** [[file-search-outperforms-rag-for-small-corpora]]
- **Source excerpt:**
  > "For smaller document sets, the precision of exact text matching (grep) and the ability to navigate file structure (glob, directory traversal) eliminates the lossy compression inherent in embedding-based retrieval. Start with file search, add semantic search only when corpus scale demands it."
- **Codifier's reading:** Imperative directive for retrieval architecture decisions: "default to file search (grep/glob/Read); add RAG infrastructure only when corpus exceeds the file-search threshold." Machine-enforceable as a KB architecture audit: flag systems with vector databases serving <100 documents where file search would suffice. The rule is independent of the broader "file search vs RAG" analysis — it's a decision heuristic for architects.
- **Suggested headline:** default-file-search-over-rag
- **Recommendation:** extract via /extract-artifacts
- **Resolution:** extracted to [[default-to-file-search-before-rag]]

Extracted 2026-05-25 — Session 102 — [[session-102-codifier-identify-and-extract-artifacts]] — to [[default-to-file-search-before-rag]].

### summary-gate-agent-traversal-pattern::rule::mandatory-summary-for-agent-triage

- **Date queued:** 2026-05-25
- **Status:** extracted
- **Target form:** rule
- **Source finding:** [[summary-gate-agent-traversal-pattern]]
- **Source excerpt:**
  > "Every knowledge node in a graph or document store carries a mandatory one-sentence summary field. When an agent is exploring the knowledge base, it reads summaries first (cheap — ~50 tokens each) and uses them to decide which full documents to load (expensive — potentially hundreds or thousands of tokens each)."
- **Codifier's reading:** Imperative schema requirement: "every knowledge node must carry a one-sentence summary field." Machine-enforceable as a frontmatter validation rule: check that all markdown files in a KB namespace have a `summary:` field, and that the field is ≤1 sentence. The rule is independent of the broader traversal pattern — it's a schema constraint that enables summary-gate navigation regardless of the traversal algorithm used.
- **Suggested headline:** mandatory-summary-for-agent-triage
- **Recommendation:** extract via /extract-artifacts
- **Resolution:** extracted to [[knowledge-node-mandatory-summary-field]]

Extracted 2026-05-25 — Session 102 — [[session-102-codifier-identify-and-extract-artifacts]] — to [[knowledge-node-mandatory-summary-field]].
