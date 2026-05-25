# Co-occurrence Harvest Queue — Agent Governance and Trust

Embedded artifact candidates surfaced during `/synthesize-guide` runs. Per DD-101.
Nothing here is auto-extracted; rows feed `/extract-artifacts` only after Nick rules.

| Date queued | Status | Target form | Source finding | Suggested headline | Recommendation |
|---|---|---|---|---|---|
| 2026-04-26 | extracted | rule | [[dark-code-organizational-capability-problem]] | "Ship only what at least one human comprehended" | extracted to [[ship-only-what-at-least-one-human-comprehended]] |
| 2026-04-26 | extracted | skill | [[dark-code-organizational-capability-problem]] | "Comprehension Gate at PR Review" | extracted to [[comprehension-gate-at-pr-review]] |
| 2026-04-26 | extracted | rule | [[distributed-boundary-guides]] | "CLAUDE.md is a symlink to AGENTS.md at every governance boundary" | extracted to [[claudemd-symlink-to-agentsmd-at-every-governance-boundary]] |
| 2026-04-26 | extracted | skill | [[specification-as-governance-fourth-enforcement-philosophy]] | "Spec-Driven Development Loop" | extracted to [[spec-driven-development-loop]] |
| 2026-04-26 | extracted | rule | [[specification-as-governance-fourth-enforcement-philosophy]] | "Spec and code reconcile bidirectionally on every change" | extracted to [[spec-and-code-reconcile-bidirectionally]] |
| 2026-04-26 | extracted | rule | [[review-obsolescence-as-design-goal]] | "Every recurring review comment must triage to mechanism or judgment-only" | extracted to [[every-recurring-review-comment-triages-to-mechanism-or-judgment]] |
| 2026-04-26 | extracted | rule | [[compound-review-debt-from-deferred-inspection]] | "Maximum unreviewed depth policy" | extracted to [[maximum-unreviewed-depth-policy]] |
| 2026-04-26 | extracted | rule | [[trust-calibration-progressive-autonomy-ramp]] | "Trust promotion thresholds and immediate-demotion triggers" | extracted to [[trust-promotion-and-demotion-thresholds]] |
| 2026-04-26 | extracted | rule | [[agent-identity-governance-enforcement-layer]] | "No agent action proceeds without an identity record bound to the task" | extracted to [[no-agent-action-without-identity-record]] |
| 2026-04-26 | extracted | rule | [[governance-memory-append-only-audit-layer]] | "Audit log is append-only and never overwritten" | extracted to [[audit-log-append-only-never-overwritten]] |
| 2026-04-26 | nick-dismissed | template | [[distributed-boundary-guides]] | "Distributed Governance Folder Layout" | dismiss as inline |
| 2026-04-26 | nick-dismissed | template | [[per-node-tool-restrictions-workflow-governance]] | "Per-Node Tool Restriction YAML" | dismiss as inline |
| 2026-04-26 | nick-dismissed | template | [[trust-calibration-progressive-autonomy-ramp]] | "Trust Ledger Template" | dismiss as inline |
| 2026-04-26 | nick-dismissed | template | [[human-on-the-loop-hotl-autonomy-tiering-framework]] | "Four-Level Autonomy Tier Table" | dismiss as inline |
| 2026-05-25 | extracted | rule | [[permission-compounding-across-agent-delegation-chains]] | "Permissions narrow monotonically across delegation chains" | extracted to [[permission-compounding-across-agent-delegation-chains]] |
| 2026-05-25 | extracted | rule | [[supervision-debt-anti-pattern]] | "Map control points before agent deployment" | extracted to [[supervision-debt-anti-pattern]] |
| 2026-05-25 | extracted | rule | [[pattern-scale-signals-systemic-not-individual-failure]] | "Pattern-scale failure triggers process fix not training" | merged into [[every-recurring-review-comment-triages-to-mechanism-or-judgment]] |
| 2026-05-25 | extracted | rule | [[tool-access-as-security-boundary-not-feature-toggle]] | "Tool enablement is security boundary not feature toggle" | merged into [[explicit-permission-allow-listing-for-agent-resource-access]] |
| 2026-05-25 | extracted | rule | [[interpretive-boundary-layer-fact-vs-judgment]] | "Label agent outputs as act-on-this vs interpret-first" | extracted to [[interpretive-boundary-layer-fact-vs-judgment]] |
| 2026-05-25 | extracted | rule | [[policy-as-data-machine-readable-constraints]] | "Governance rules are machine-readable data not prose" | extracted to [[policy-as-data-machine-readable-constraints]] |

## Per-row details

### dark-code-organizational-capability-problem::rule::ship-only-what-at-least-one-human-comprehended

- **Date queued:** 2026-04-26
- **Status:** extracted
- **Target form:** rule
- **Source finding:** [[dark-code-organizational-capability-problem]]
- **Source excerpt:** "'Dark code' is AI-generated code that passed automated checks and shipped — but was never understood by any human at any point. It is not buggy code, spaghetti code, or technical debt. It is code where the comprehension step simply did not happen because the development process no longer requires it."
- **Codifier's reading:** Imperative directive applicable to any AI-assisted development process: an artifact does not ship if zero humans have read it with comprehension. Machine-checkable as a PR-merge gate that requires at least one human reviewer-with-comprehension signal (acknowledgment, comprehension-gate question answered, etc.) before merge. Fits rule artifact form per the form-classification rubric — directive + enforcement path. Companion artifacts: comprehension-gate review skill (separate row); comprehension-coverage metric (downstream).
- **Suggested headline:** ship-only-what-at-least-one-human-comprehended
- **Recommendation:** extract via /extract-artifacts
- **Resolution:** extracted to [[ship-only-what-at-least-one-human-comprehended]]

Extracted 2026-04-27 — Session 82 — [[session-82-codifier-extract-artifacts-harvest-promotion-batch]] — to [[ship-only-what-at-least-one-human-comprehended]].

### dark-code-organizational-capability-problem::skill::comprehension-gate-at-pr-review

- **Date queued:** 2026-04-26
- **Status:** extracted
- **Target form:** skill
- **Source finding:** [[dark-code-organizational-capability-problem]]
- **Source excerpt:** "An AI-assisted filter at PR review that asks senior-engineer-style questions as code is reviewed: why was this dependency called here? How is caching structured in relation to other services? What are the separation-of-concerns implications? The gate makes architectural questions immediately legible rather than requiring the reviewer to surface them from scratch. Output from comprehension gate checks feeds back into evals — creating a flywheel that improves code quality and review quality simultaneously."
- **Codifier's reading:** Procedural pattern with input (PR diff + prior context), per-question prompts (dependency rationale, caching topology, separation-of-concerns), and output (gate verdict + eval-feedback signal). Has clear step-by-step structure suitable for SKILL.md form. Fits skill artifact form. The skill would carry a starter prompt set drawn from senior-engineer review patterns plus a feedback loop to evals.
- **Suggested headline:** comprehension-gate-at-pr-review
- **Recommendation:** extract via /extract-artifacts
- **Resolution:** extracted to [[comprehension-gate-at-pr-review]]

Extracted 2026-04-27 — Session 83 — [[session-83-codifier-ib164-resume-extract-artifacts]] — to [[comprehension-gate-at-pr-review]].

### distributed-boundary-guides::rule::claudemd-symlink-to-agentsmd-at-every-governance-boundary

- **Date queued:** 2026-04-26
- **Status:** extracted
- **Target form:** rule
- **Source finding:** [[distributed-boundary-guides]]
- **Source excerpt:** "At each location, CLAUDE.md is a symlink pointing to AGENTS.md. This ensures that both Claude Code (which reads CLAUDE.md) and other AI tools (which may read AGENTS.md or other convention files) see identical governance context. The symlink is the compatibility mechanism — one source of truth, two access paths."
- **Codifier's reading:** Imperative directive; machine-enforceable as a filesystem-discipline check that scans every governance-file location and verifies CLAUDE.md is a symlink pointing at the colocated AGENTS.md (or the canonical name chosen by the project). Fits rule artifact form. Pre-commit hook or CI step is the natural enforcement surface. Note: rule applies only when the project actually maintains AGENTS.md as the canonical name — projects with a different canonical may want a parameterized version.
- **Suggested headline:** claudemd-symlink-to-agentsmd-at-every-governance-boundary
- **Recommendation:** extract via /extract-artifacts
- **Resolution:** extracted to [[claudemd-symlink-to-agentsmd-at-every-governance-boundary]]

Extracted 2026-04-27 — Session 82 — [[session-82-codifier-extract-artifacts-harvest-promotion-batch]] — to [[claudemd-symlink-to-agentsmd-at-every-governance-boundary]].
- **Resolution:**

### specification-as-governance-fourth-enforcement-philosophy::skill::spec-driven-development-loop

- **Date queued:** 2026-04-26
- **Status:** extracted
- **Target form:** skill
- **Source finding:** [[specification-as-governance-fourth-enforcement-philosophy]]
- **Source excerpt:** "n8n's spec-driven development skill: `.claude/specs/` files serve as living architectural decisions. The skill enforces bidirectional sync between specs and implementation code. Core loop: read spec → implement → verify alignment → update spec or code. TODO checkboxes track completion, with strikethrough+annotation for deliberately skipped items. Specs are the source of truth, not the code."
- **Codifier's reading:** Procedural pattern with explicit input/output and step-by-step structure (read → implement → verify → reconcile). Has clear invocation contract (specs in `.claude/specs/`, agent enters loop), step semantics (TODO checkboxes for completion tracking), and termination criteria (alignment verified). Fits skill artifact form per the form-classification rubric. Skill would package the loop with the TODO-checkbox convention and the spec-or-code reconciliation step.
- **Suggested headline:** spec-driven-development-loop
- **Recommendation:** extract via /extract-artifacts
- **Resolution:** extracted to [[spec-driven-development-loop]]

Extracted 2026-04-27 — Session 83 — [[session-83-codifier-ib164-resume-extract-artifacts]] — to [[spec-driven-development-loop]].

### specification-as-governance-fourth-enforcement-philosophy::rule::spec-and-code-reconcile-bidirectionally

- **Date queued:** 2026-04-26
- **Status:** extracted
- **Target form:** rule
- **Source finding:** [[specification-as-governance-fourth-enforcement-philosophy]]
- **Source excerpt:** "The skill enforces bidirectional sync between specs and implementation code. Core loop: read spec → implement → verify alignment → update spec or code... A spec that drifts from reality becomes governance theater — the spec passes but doesn't reflect actual behavior."
- **Codifier's reading:** Imperative directive applicable to any spec-as-governance system: when spec and code disagree, neither runs authoritatively until reconciliation. Machine-enforceable as a CI check that flags spec/code drift on every change to either side. Fits rule artifact form. Companion to the skill above (skill is the procedure; rule is the invariant).
- **Suggested headline:** spec-and-code-reconcile-bidirectionally
- **Recommendation:** extract via /extract-artifacts
- **Resolution:** extracted to [[spec-and-code-reconcile-bidirectionally]]

Extracted 2026-04-27 — Session 82 — [[session-82-codifier-extract-artifacts-harvest-promotion-batch]] — to [[spec-and-code-reconcile-bidirectionally]].

### review-obsolescence-as-design-goal::rule::every-recurring-review-comment-triages-to-mechanism-or-judgment

- **Date queued:** 2026-04-26
- **Status:** extracted
- **Target form:** rule
- **Source finding:** [[review-obsolescence-as-design-goal]]
- **Source excerpt:** "For every recurring review comment, ask: 'How do I make this comment impossible in the future?' Build the check (linter, schema constraint, CI rule) and eliminate the category permanently. This is the constructive response to the bottleneck — shrink the volume of reviewable material."
- **Codifier's reading:** Imperative directive applicable to all review-process operation: every recurring review comment is triaged into one of two terminal states — eliminated by mechanism (linter / schema / CI) or accepted as judgment-only with explicit reasoning. Machine-trackable as a Review Obsolescence Tracking table (already a template fragment in the guide); the rule version specifies the triage discipline that the table records. Fits rule artifact form.
- **Suggested headline:** every-recurring-review-comment-triages-to-mechanism-or-judgment
- **Recommendation:** extract via /extract-artifacts
- **Resolution:** extracted to [[every-recurring-review-comment-triages-to-mechanism-or-judgment]]

Extracted 2026-04-27 — Session 82 — [[session-82-codifier-extract-artifacts-harvest-promotion-batch]] — to [[every-recurring-review-comment-triages-to-mechanism-or-judgment]].
- **Resolution:**

### compound-review-debt-from-deferred-inspection::rule::maximum-unreviewed-depth-policy

- **Date queued:** 2026-04-26
- **Status:** extracted
- **Target form:** rule
- **Source finding:** [[compound-review-debt-from-deferred-inspection]]
- **Source excerpt:** "Skipping review on agent-produced work creates compound debt. Each unreviewed change embeds assumptions that subsequent changes build upon. Reviewing a chain of 10 unreviewed commits costs far more than reviewing each individually... Policy: Set a maximum unreviewed depth. No more than {{MAX_UNREVIEWED_DEPTH}} changes should accumulate before a review gate triggers, regardless of phase boundaries."
- **Codifier's reading:** Imperative directive with a parameterized threshold; machine-enforceable as a CI/branch-protection check that counts unreviewed commits since the last reviewed merge and blocks production-ward merges past the configured depth. Fits rule artifact form. The {{MAX_UNREVIEWED_DEPTH}} parameter is per-organization; the rule is the discipline (cap exists; cap is enforced regardless of phase boundaries).
- **Suggested headline:** maximum-unreviewed-depth-policy
- **Recommendation:** extract via /extract-artifacts
- **Resolution:** extracted to [[maximum-unreviewed-depth-policy]]

Extracted 2026-04-27 — Session 82 — [[session-82-codifier-extract-artifacts-harvest-promotion-batch]] — to [[maximum-unreviewed-depth-policy]].
- **Resolution:**

### trust-calibration-progressive-autonomy-ramp::rule::trust-promotion-and-demotion-thresholds

- **Date queued:** 2026-04-26
- **Status:** extracted
- **Target form:** rule
- **Source finding:** [[trust-calibration-progressive-autonomy-ramp]]
- **Source excerpt:** "Trust calibration follows three rules: 1. Start restrictive. Every new task type begins at proposal-first or human-required. No task type starts at full autonomy. 2. Promote per task type... 3. Track and threshold. Define a concrete promotion criterion (e.g., 20 consecutive successful executions) and a demotion trigger (e.g., any failure that reaches production)."
- **Codifier's reading:** Imperative discipline with parameterized thresholds; machine-trackable via the Trust Ledger template (separate row, dismiss-as-inline). The rule formulation: "trust is promoted only after explicit threshold met; trust is demoted immediately on failure; no task type defaults to full autonomy." Fits rule artifact form. Companion artifact: the Trust Ledger template that records compliance.
- **Suggested headline:** trust-promotion-and-demotion-thresholds
- **Recommendation:** extract via /extract-artifacts
- **Resolution:** extracted to [[trust-promotion-and-demotion-thresholds]]

Extracted 2026-04-27 — Session 82 — [[session-82-codifier-extract-artifacts-harvest-promotion-batch]] — to [[trust-promotion-and-demotion-thresholds]].

### agent-identity-governance-enforcement-layer::rule::no-agent-action-without-identity-record

- **Date queued:** 2026-04-26
- **Status:** extracted
- **Target form:** rule
- **Source finding:** [[agent-identity-governance-enforcement-layer]]
- **Source excerpt:** "Identity-Aware Orchestration is the technical enforcement mechanism for HITL checkpoints. Without identity infrastructure, HITL policies cannot be enforced — agents can act before approval is obtained... JIT identity provisioning: Purpose-bound, time-limited identities for ephemeral agents. No pre-provisioned static accounts. Every action is traceable to an identity record tied to a specific task and human delegator."
- **Codifier's reading:** Imperative directive: every agent action must be traceable to an identity record bound to a task and a human delegator before execution. Machine-enforceable at the orchestration layer (request gateway rejects actions lacking a valid identity record). Fits rule artifact form. The companion JIT-provisioning procedure could become a separate skill.
- **Suggested headline:** no-agent-action-without-identity-record
- **Recommendation:** extract via /extract-artifacts
- **Resolution:** extracted to [[no-agent-action-without-identity-record]]

Extracted 2026-04-27 — Session 82 — [[session-82-codifier-extract-artifacts-harvest-promotion-batch]] — to [[no-agent-action-without-identity-record]].

### governance-memory-append-only-audit-layer::rule::audit-log-append-only-never-overwritten

- **Date queued:** 2026-04-26
- **Status:** extracted
- **Target form:** rule
- **Source finding:** [[governance-memory-append-only-audit-layer]]
- **Source excerpt:** "Append-only retention (immutable logs with versioning); separate from debug/operational logs; queryable for post-incident analysis and drift detection... Not in the hot path (no impact on agent response latency)."
- **Codifier's reading:** Imperative directive: governance audit log entries are append-only and never modified after write. Machine-enforceable at the storage layer (write-only credentials; cryptographic immutability; database constraint). Fits rule artifact form. The contrast with debug logs (which may be retentioned/rotated) is part of the rule's scope: governance audit and operational debug have different retention disciplines.
- **Suggested headline:** audit-log-append-only-never-overwritten
- **Recommendation:** extract via /extract-artifacts
- **Resolution:** extracted to [[audit-log-append-only-never-overwritten]]

Extracted 2026-04-27 — Session 82 — [[session-82-codifier-extract-artifacts-harvest-promotion-batch]] — to [[audit-log-append-only-never-overwritten]].
- **Resolution:**

### distributed-boundary-guides::template::distributed-governance-folder-layout

- **Date queued:** 2026-04-26
- **Status:** nick-dismissed
- **Target form:** template
- **Source finding:** [[distributed-boundary-guides]]
- **Source excerpt:** Folder layout block at root with AGENTS.md/CLAUDE.md pairs at extensions/, src/channels/, src/plugins/, src/gateway/. Captured by the guide's Section 4 Layer 4 as an inline code block.
- **Codifier's reading:** Structural scaffold meant for rendering at a project's root, with placeholders for subsystem boundaries. Template-shape per the form-classification rubric. **Already absorbed inline** as a code block in Section 4 Layer 4 (Distributed Governance Scope) of this guide. Extracting as a standalone template would duplicate the absorption without adding new utility — the guide's inline version is parameterizable via the subsystem-boundary list. Recommend dismiss as inline.
- **Suggested headline:** distributed-governance-folder-layout
- **Recommendation:** dismiss as inline
- **Resolution:** dismissed

### per-node-tool-restrictions-workflow-governance::template::per-node-tool-restriction-yaml

- **Date queued:** 2026-04-26
- **Status:** nick-dismissed
- **Target form:** template
- **Source finding:** [[per-node-tool-restrictions-workflow-governance]]
- **Source excerpt:** "nodes: - name: classify_issue / model: small-fast / tools: [] (routing decision; no tools allowed) - name: research_solution / tools: [Read, Grep, WebFetch] / denied_tools: [Write, Edit, Bash] - name: implement_fix / tools: [Read, Edit, Write, Bash] / verify / tools: [Read, Bash]"
- **Codifier's reading:** Structural scaffold for workflow YAML with placeholder fields for node names, models, allowed_tools, and denied_tools. Template-shape. **Already absorbed inline** as a YAML code block in Section 1's Per-Decision-Point Granularity sub-step. The inline version covers the same structural pattern; standalone extraction would duplicate. Recommend dismiss as inline.
- **Suggested headline:** per-node-tool-restriction-yaml
- **Recommendation:** dismiss as inline
- **Resolution:** dismissed

### trust-calibration-progressive-autonomy-ramp::template::trust-ledger-template

- **Date queued:** 2026-04-26
- **Status:** nick-dismissed
- **Target form:** template
- **Source finding:** [[trust-calibration-progressive-autonomy-ramp]]
- **Source excerpt:** "Trust Ledger — {{SYSTEM_NAME}} / Task Type: {{TASK_TYPE}} / Current autonomy level / Consecutive successes / Last failure / Promotion threshold / Demotion trigger / Last trust assessment / Model version at assessment"
- **Codifier's reading:** Structural scaffold for tracking per-task-type trust state with explicit `{{VARIABLE}}` placeholders. Template-shape. **Already absorbed inline** as the Trust Ledger Template in Section 2 of this guide, with a paired worked example (MetaSystem Improvement Loop ledger). Standalone extraction would duplicate. Recommend dismiss as inline.
- **Suggested headline:** trust-ledger-template
- **Recommendation:** dismiss as inline
- **Resolution:** dismissed

### human-on-the-loop-hotl-autonomy-tiering-framework::template::four-level-autonomy-tier-table

- **Date queued:** 2026-04-26
- **Status:** nick-dismissed
- **Target form:** template
- **Source finding:** [[human-on-the-loop-hotl-autonomy-tiering-framework]]
- **Source excerpt:** "Full Autonomy / Acts without notification / None unless auditing / Log entries, formatting, index updates. Guarded / Acts, then reports what it did / Reviews reports, intervenes if needed / Refactoring within a module... Proposal-First... Human-Required..."
- **Codifier's reading:** Structural scaffold (4-row table) defining each autonomy level by agent behavior, human behavior, and use-case examples. Template-shape. **Already absorbed inline** as the Autonomy level definitions table in Section 1 of this guide. Standalone extraction would duplicate. Recommend dismiss as inline.
- **Suggested headline:** four-level-autonomy-tier-table
- **Recommendation:** dismiss as inline
- **Resolution:** dismissed

### permission-compounding-across-agent-delegation-chains::rule::permissions-narrow-monotonically

- **Date queued:** 2026-05-25
- **Status:** extracted
- **Target form:** rule
- **Source finding:** [[permission-compounding-across-agent-delegation-chains]]
- **Source excerpt:**
  > "Implement monotonic permission narrowing: each delegation step can only reduce permissions, never expand them. Agent B's permissions must be a strict subset of Agent A's delegated scope."
- **Codifier's reading:** Imperative directive applicable to any multi-agent delegation architecture: each step in a delegation chain produces a strict subset of the delegator's permissions; no escalation path exists. Machine-enforceable at the orchestration layer (delegation request rejected if target scope exceeds source scope). Fits rule artifact form per form-classification rubric — directive + enforcement path + machine-checkable invariant.
- **Suggested headline:** permissions-narrow-monotonically
- **Recommendation:** extract via /extract-artifacts
- **Resolution:** extracted to [[permission-compounding-across-agent-delegation-chains]]

Extracted 2026-05-25 — Session 102 — [[session-102-codifier-identify-and-extract-artifacts]] — to [[permission-compounding-across-agent-delegation-chains]].

### supervision-debt-anti-pattern::rule::map-control-points-before-deployment

- **Date queued:** 2026-05-25
- **Status:** extracted
- **Target form:** rule
- **Source finding:** [[supervision-debt-anti-pattern]]
- **Source excerpt:**
  > "Map every agent workflow to explicit control points before deployment, not after. Classify operations by risk tier: auto-approve (read-only), human-approve (mutations), and human-initiate (irreversible)."
- **Codifier's reading:** Imperative directive applicable to any agent deployment process: every workflow must have its control points (observation, approval, steering, cancel) mapped and classified before production deployment. Machine-checkable as a pre-deployment gate that verifies control-point documentation exists per workflow. Fits rule artifact form — directive + temporal constraint ("before deployment") + enforcement surface (deployment gate).
- **Suggested headline:** map-control-points-before-deployment
- **Recommendation:** extract via /extract-artifacts
- **Resolution:** extracted to [[supervision-debt-anti-pattern]]

Extracted 2026-05-25 — Session 102 — [[session-102-codifier-identify-and-extract-artifacts]] — to [[supervision-debt-anti-pattern]].

### pattern-scale-signals-systemic-not-individual-failure::rule::pattern-scale-triggers-process-fix

- **Date queued:** 2026-05-25
- **Status:** extracted
- **Target form:** rule
- **Source finding:** [[pattern-scale-signals-systemic-not-individual-failure]]
- **Source excerpt:**
  > "If the failure is at pattern-scale, training is the wrong mitigation. ... if the same error appears 3+ times, escalate from individual fix to process fix."
- **Codifier's reading:** Imperative directive with a quantified trigger threshold: governance failures appearing at pattern-scale (3+ instances) require process-level architectural fixes, not individual training or one-off repairs. Machine-trackable as a governance incident counter with automatic escalation when the threshold fires. Fits rule artifact form — imperative + threshold + mitigation target specification.
- **Suggested headline:** pattern-scale-triggers-process-fix
- **Recommendation:** extract via /extract-artifacts
- **Resolution:** merged into [[every-recurring-review-comment-triages-to-mechanism-or-judgment]]

Pending merge 2026-05-25 — Session 102 — [[session-102-codifier-identify-and-extract-artifacts]] — DD-97 extension proposal emitted at [[operations/extension-proposals/2026-05-25-extension-proposals]]; primary match [[every-recurring-review-comment-triages-to-mechanism-or-judgment]]. Manual apply per DD-97 v1 (Step 1.7 auto-merge prohibition); after apply, row Status flips to extracted and Resolution to merged into [[every-recurring-review-comment-triages-to-mechanism-or-judgment]] via manual queue edit (or future skill mode).

Merged 2026-05-25 — Session 103 — [[session-103-codifier-complete-extract-artifacts-write-phase]] — into [[every-recurring-review-comment-triages-to-mechanism-or-judgment]].

### tool-access-as-security-boundary-not-feature-toggle::rule::tool-enablement-is-security-boundary

- **Date queued:** 2026-05-25
- **Status:** extracted
- **Target form:** rule
- **Source finding:** [[tool-access-as-security-boundary-not-feature-toggle]]
- **Source excerpt:**
  > "MCP tool access is treated as a feature toggle in most UIs (enable/disable server), but it is actually a security boundary crossing. ... Enabling a tool grants the agent arbitrary code execution and arbitrary data access within that tool's scope."
- **Codifier's reading:** Imperative directive: tool/MCP server enablement must be assessed as a security boundary crossing, not a feature toggle. Each enablement should include capability assessment (what can the agent now do?) and scope limitation (which tools from this server are exposed?). Machine-enforceable as a pre-enablement checklist or a security-classification gate in server configuration. Fits rule artifact form — reframes a common implicit assumption into an explicit invariant.
- **Suggested headline:** tool-enablement-is-security-boundary
- **Recommendation:** extract via /extract-artifacts
- **Resolution:** merged into [[explicit-permission-allow-listing-for-agent-resource-access]]

Pending merge 2026-05-25 — Session 102 — [[session-102-codifier-identify-and-extract-artifacts]] — DD-97 extension proposal emitted at [[operations/extension-proposals/2026-05-25-extension-proposals]]; primary match [[explicit-permission-allow-listing-for-agent-resource-access]]. Manual apply per DD-97 v1 (Step 1.7 auto-merge prohibition); after apply, row Status flips to extracted and Resolution to merged into [[explicit-permission-allow-listing-for-agent-resource-access]] via manual queue edit (or future skill mode).

Merged 2026-05-25 — Session 103 — [[session-103-codifier-complete-extract-artifacts-write-phase]] — into [[explicit-permission-allow-listing-for-agent-resource-access]].

### interpretive-boundary-layer-fact-vs-judgment::rule::label-outputs-act-vs-interpret

- **Date queued:** 2026-05-25
- **Status:** extracted
- **Target form:** rule
- **Source finding:** [[interpretive-boundary-layer-fact-vs-judgment]]
- **Source excerpt:**
  > "Every AI-powered knowledge system that surfaces information to decision-makers must explicitly label outputs as either 'act on this' (factual, verified, low-risk) or 'interpret this first' (judgment call, causal inference, novel pattern) — because presenting both at the same confidence level is an architectural failure."
- **Codifier's reading:** Imperative directive: all agent outputs reaching human decision-makers must carry an explicit binary classification (factual vs. inferential). Machine-enforceable as a mandatory field on agent output schemas or as a post-processing classification step before human-facing rendering. Fits rule artifact form — imperative + binary classification requirement + explicit failure mode ("presenting both at the same confidence level is an architectural failure").
- **Suggested headline:** label-outputs-act-vs-interpret
- **Recommendation:** extract via /extract-artifacts
- **Resolution:** extracted to [[interpretive-boundary-layer-fact-vs-judgment]]

Extracted 2026-05-25 — Session 102 — [[session-102-codifier-identify-and-extract-artifacts]] — to [[interpretive-boundary-layer-fact-vs-judgment]].

### policy-as-data-machine-readable-constraints::rule::governance-rules-machine-readable

- **Date queued:** 2026-05-25
- **Status:** extracted
- **Target form:** rule
- **Source finding:** [[policy-as-data-machine-readable-constraints]]
- **Source excerpt:**
  > "Prose policies ('agents should not access PII without authorization') are aspirational. Machine-readable policies are enforced — the runtime checks them and blocks non-compliant events. This is the distinction between governance-as-documentation and governance-as-enforcement."
- **Codifier's reading:** Imperative directive: governance rules must be represented as machine-readable data structures that the runtime evaluates against every event, not as prose documentation that agents are instructed to follow. Machine-enforceable as a meta-rule: every policy statement must have a machine-readable encoding; prose-only policies are governance debt that must be converted. Fits rule artifact form — imperative + binary distinction (documentation vs. enforcement) + clear target state (runtime-evaluated data structures).
- **Suggested headline:** governance-rules-machine-readable
- **Recommendation:** extract via /extract-artifacts
- **Resolution:** extracted to [[policy-as-data-machine-readable-constraints]]

Extracted 2026-05-25 — Session 102 — [[session-102-codifier-identify-and-extract-artifacts]] — to [[policy-as-data-machine-readable-constraints]].
