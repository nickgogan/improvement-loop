# Co-occurrence Harvest Queue — Managing Agent Context

Embedded artifact candidates surfaced during `/synthesize-guide` runs. Per DD-101.
Nothing here is auto-extracted; rows feed `/extract-artifacts` only after Nick rules.

| Date queued | Status | Target form | Source finding | Suggested headline | Recommendation |
|---|---|---|---|---|---|
| 2026-04-26 | extracted | rule | [[catastrophic-context-collapse-risk-during-claudemd]] | "Never ask Claude to compact CLAUDE.md" | extracted to [[never-ask-claude-to-compact-claudemd]] |
| 2026-04-26 | nick-approved | rule | [[claudemd-context-rot-from-indiscriminate-rule-accu]] | "CLAUDE.md global rule cap" | extract via /extract-artifacts |
| 2026-04-26 | extracted | skill | [[trajectory-engineering-non-linear-session-forking]] | "/re Fork-and-Trim Trajectory Procedure" | extracted to [[re-fork-and-trim-trajectory-procedure]] |
| 2026-04-26 | extracted | template | [[progress-md-session-bridge]] | "PROGRESS.md Session Bridge Template" | extracted to [[progressmd-session-bridge-template]] |
| 2026-04-26 | extracted | template | [[response-format-enum-for-adaptive-verbosity]] | "Tool Response-Format Enum (detailed / concise)" | extracted to [[tool-response-format-enum]] |
| 2026-04-26 | extracted | rule | [[skills-as-pointers-to-second-brain-files]] | "Skills reference shared context by path, not by copy" | extracted to [[skills-reference-shared-context-by-path]] |
| 2026-04-26 | nick-approved | rule | [[ace-delta-updates-over-monolithic-rewrites]] | "Evolving context docs use delta updates, never monolithic LLM rewrites" | extract via /extract-artifacts |
| 2026-04-26 | extracted | rule | [[ide-context-streaming-silent-token-tax]] | "Close irrelevant IDE files during agent sessions" | extracted to [[close-irrelevant-ide-files-during-agent-sessions]] |
| 2026-04-26 | extracted | rule | [[model-specific-context-file-sensitivity]] | "Test context strategies against your actual model" | extracted to [[test-context-strategies-against-actual-model]] |
| 2026-04-26 | nick-dismissed | template | [[five-context-management-techniques-in-claude-code]] | "Context-Management Technique Selector" | dismiss as inline |
| 2026-04-26 | nick-dismissed | template | [[cross-platform-context-file-strategy]] | "Multi-Tool Context Mirror Map" | dismiss as inline |
| 2026-04-26 | nick-dismissed | template | [[self-describing-codebase-structural-semantic-context]] | "Module Manifest Template" | dismiss as inline |
| 2026-04-26 | nick-dismissed | template | [[monorepo-context-distribution-three-strategies]] | "Monorepo Context Distribution Decision Matrix" | dismiss as inline |
| 2026-04-26 | nick-dismissed | template | [[three-layer-folder-as-workspace-architecture]] | "Three-Layer Folder-as-Workspace Scaffold" | dismiss as inline |
| 2026-04-26 | nick-dismissed | template | [[three-tier-vault-architecture-global-shared-local]] | "Three-Tier Vault Architecture (Global/Shared/Local)" | dismiss as inline |
| 2026-04-26 | nick-dismissed | rule | [[session-atomicity-single-issue-scope-quadratic-cost-reduction]] | "Bound each agent session to a single atomic issue" | dismiss as inline |

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
- **Status:** nick-approved
- **Target form:** rule
- **Source finding:** [[claudemd-context-rot-from-indiscriminate-rule-accu]]
- **Source excerpt:** "As users add rules to CLAUDE.md each time something goes wrong, the file grows and loads in full at the start of every session. The accumulation of context noise gradually reduces instruction-following quality and increases hallucination rates... Keep CLAUDE.md to 3-5 globally true, universally relevant lines."
- **Codifier's reading:** Imperative cap on CLAUDE.md global section; machine-enforceable via line-count check on the global Tier-0 section. Fits rule form. Note: a stricter version restricts to *global rules only*; project-specific rules go to per-project / per-skill files. The 60-80 line benchmark from Step 1 is a softer band; this rule names the harder Tier-0 cap.
- **Suggested headline:** claudemd-global-rule-cap
- **Recommendation:** extract via /extract-artifacts
- **Resolution:**

Pending merge 2026-04-27 — Session 82 — [[session-82-codifier-extract-artifacts-harvest-promotion-batch]] — DD-97 extension proposal emitted at [[operations/extension-proposals/2026-04-27-claudemd-global-rule-cap-extension-proposal]]; primary match [[claudemd-minimum-viable-rule-only-add-globally-true-lines]]. Status remains `nick-approved` per DD-101 Branch C until Nick rules merge / separate / dismiss; on merge ruling, manually amend the existing rule then re-invoke this row to flip Status → `extracted`, Resolution → `merged into [[claudemd-minimum-viable-rule-only-add-globally-true-lines]]`.

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
- **Status:** nick-approved
- **Target form:** rule
- **Source finding:** [[ace-delta-updates-over-monolithic-rewrites]]
- **Source excerpt:** "When context documents change over time (playbooks, progress files, accumulated notes), update incrementally — append structured entries, then periodically consolidate. Never rewrite the full document with an LLM, as brevity bias silently drops domain-specific details."
- **Codifier's reading:** Imperative directive ("never rewrite full document with an LLM"); machine-enforceable via a hook that detects whole-document rewrites of designated long-lived files (CLAUDE.md, PROGRESS.md, playbooks) and warns. Fits rule form. The Delta Update Entry template (already in this guide) is the companion structural artifact.
- **Suggested headline:** evolving-docs-use-delta-updates
- **Recommendation:** extract via /extract-artifacts
- **Resolution:**

Pending merge 2026-04-27 — Session 83 — [[session-83-codifier-ib164-resume-extract-artifacts]] — DD-97 extension proposal emitted at [[operations/extension-proposals/2026-04-27-evolving-docs-use-delta-updates-extension-proposal]]; primary match [[never-ask-claude-to-compact-claudemd]]. Manual apply per DD-97 v1 (Step 1.7 auto-merge prohibition); after apply, row Status flips to `extracted` and Resolution to `merged into [[never-ask-claude-to-compact-claudemd]]` via manual queue edit (or future skill mode).

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
