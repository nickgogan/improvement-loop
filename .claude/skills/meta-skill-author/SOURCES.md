# Sources

This file maps each `[finding-filename]` citation used throughout the meta-skill-author skill
back to:

1. Where the finding lives in the corpus (`/research-findings/<filename>.md`)
2. The underlying upstream source the finding cites (paper, blog post, repo, etc.)

All findings live at:
`/home/user/workspace/research/improvement-loop/research-findings/<finding-filename>.md`

When citing a claim in conversation: cite the finding name in `[square-brackets]`.
When verifying against the upstream source: look up the URL column below.
When updating: this file is regenerated whenever the master inventory is rebuilt.

---

## Multiply-Cited Sources (from inventory §4)

Sources appearing in two or more distinct findings across all 9 buckets. This is the de-facto
canonical reference list for the corpus.

| Source (internal filename) | Findings citing it | Direction / Theme |
|----------------------------|-------------------|-------------------|
| `anthropic-claude-code-skills-docs.md` | `claude-code-skill-frontmatter-extensions`, `skill-content-lifecycle-context-budget`, `skill-cross-surface-portability-with-constraints`, `skill-description-budget-context-overflow`, `skill-dynamic-context-injection-shell-prerender`, `skill-forked-subagent-execution`, `skill-hierarchy-enterprise-personal-project-plugin`, `skill-invocation-control-side-effect-guard`, `skill-live-change-detection-hot-reload`, `skill-plugin-marketplace-distribution`, `skill-security-audit-obligation`, `slash-commands-merged-into-skills`, `code-as-deterministic-tool-inside-skills` | Claude Code skill platform specification |
| `anthropic-equipping-agents-with-agent-skills.md` | `meta-skill-for-skill-authorship`, `skill-as-directory-progressive-disclosure-three-levels`, `skill-authoring-four-guidelines`, `skill-md-frontmatter-as-discovery-trigger-primitive`, `skill-security-audit-obligation`, `skills-as-open-portable-standard`, `skills-mcp-recipes-kitchen-complementarity`, `iterate-on-single-task-then-extract-skill`, `code-as-deterministic-tool-inside-skills` | Anthropic equipping-agents blog post (Oct 2025) |
| `anthropic-complete-guide-building-skills-pdf.md` | `skill-as-directory-progressive-disclosure-three-levels`, `skill-authoring-four-guidelines`, `skill-description-structure-what-when-capabilities`, `skill-testing-three-tier-trigger-functional-perf`, `skills-as-open-portable-standard`, `skills-mcp-recipes-kitchen-complementarity`, `iterate-on-single-task-then-extract-skill`, `code-as-deterministic-tool-inside-skills` | Anthropic Complete Guide to Building Skills PDF |
| `anthropic-skills-repo.md` | `meta-skill-for-skill-authorship`, `skill-as-directory-progressive-disclosure-three-levels`, `skill-authoring-explain-the-why-not-musts`, `skill-description-optimization-loop-held-out-test`, `skill-security-audit-obligation`, `skill-testing-three-tier-trigger-functional-perf`, `generator-assessor-separation-in-skill-iteration` | Anthropic official skills GitHub repo (skill-creator) |
| `agentskills-open-standard.md` | `skill-as-directory-progressive-disclosure-three-levels`, `skill-frontmatter-validation-rules`, `skill-md-frontmatter-as-discovery-trigger-primitive`, `skills-as-open-portable-standard` | agentskills.io open standard (Apache 2.0 / CC-BY-4.0, Dec 2025) |
| `anthropic-agent-skills-overview-docs.md` | `skill-as-directory-progressive-disclosure-three-levels`, `skill-cross-surface-portability-with-constraints`, `skill-frontmatter-validation-rules`, `skill-md-frontmatter-as-discovery-trigger-primitive`, `skill-security-audit-obligation`, `code-as-deterministic-tool-inside-skills` | Anthropic agent skills overview documentation |
| `eth-zurich-context-files-paper-march-2026.md` (arXiv 2602.11988) | `context-file-taxonomy-claudemd-soulmd-agentsmd`, `context-file-instruction-bloat-eth-zurich`, `model-specific-context-file-sensitivity`, `pointers-over-copies-in-context-files`, `reasoning-token-overhead-from-context-files` | ETH Zurich empirical study: 438 tasks, 4 agents, March 2026 |
| `claude-codes-leak-changes-everything.md` | `skills-cli-tools-as-mobile-triggerable-modules`, `skills-migration-claude-code-to-co-work-for-dis`, `claude-dispatch-native-mobile-to-local-agent-orch`, `llm-as-judge-pattern-for-verification-agents`, `verification-agent-seven-prompt-patterns`, `explicit-permission-allow-listing-for-agent-resou` | Claude Code internal architecture leak analysis |
| `anthropics-2-5-billion-leak-12-critical-pieces.md` | `agentic-harness-self-assessment-skill`, `two-level-verification-agent-run-plus-harness-inte`, `tiered-permission-system-bash-safety` | Nate B. Jones analysis of Claude Code codebase |
| `nate-b-jones-videos-feb-mar-2026.md` | `four-discipline-prompt-evaluator`, `the-four-discipline-prompting-stack-nate-b-jones`, `eval-driven-development-autonomous-quality`, `two-level-verification-agent-run-plus-harness-inte` | Nate B. Jones video series (Feb–Mar 2026) |
| `intent-engineering-framework-for-ai-agents-product.md` | `intent-engineering-framework-seven-part-agent-inten`, `spec-first-agent-briefs-prompt-craft-context-inten`, `autonomy-gradient-not-binary-delegation` | productcompass.pm intent engineering article |
| `lilly-incident-agent-security-permissions.md` | `agent-action-reversibility-as-design-requirement`, `cross-system-permission-composition-audit-gap`, `permission-compounding-across-agent-delegation-chains`, `screen-as-permissions-model-agent-bypass-failure` | Eli Lilly agent security incident case study |
| `anthropic-trustworthy-agents-in-practice.md` | `autonomy-gradient-not-binary-delegation`, `claude-code-auto-mode-ai-driven-permission-classif`, `trust-calibration-progressive-autonomy-ramp`, `human-on-the-loop-hotl-autonomy-tiering-framework` | Anthropic Trustworthy Agents documentation |
| `anthropic-claude-code-auto-mode.md` | `claude-code-auto-mode-ai-driven-permission-classif`, `explicit-permission-allow-listing-for-agent-resou`, `tiered-permission-system-bash-safety` | Claude Code auto-mode documentation |
| `prompting-after-feb-2026-prompt-craft-context-inten.md` | `acceptance-criteria-as-verifiable-eval-anchor`, `spec-first-agent-briefs-prompt-craft-context-inten`, `context-curation-over-context-stuffing` | maniak.io post-Feb-2026 prompting guide |
| `every-ai-prompting-technique-that-works-on-reasoni.md` | `model-agnostic-prompting-three-properties`, `reasoning-model-anti-pattern-prescribed-reasoning`, `design-evaluate-dual-phase-prompting-framework` | Cross-model prompting techniques study (GPT-5.4, Claude 4.6, Gemini 3.1) |
| `markdown-vs-html-claude-code-derrick-anthropic.md` | `html-output-as-human-in-the-loop-restorer`, `format-constrained-improvisation-tax`, `output-format-token-cost-reframed-by-context-window-size`, `html-artifact-as-skill-output-design-variations` | Derrick (Anthropic) on HTML vs. Markdown output |
| `archon-open-source-harness-builder.md` | `cross-project-workflow-portability-register-and-run`, `description-based-workflow-routing-lazy-dispatch`, `intent-based-meta-routing-skill`, `archon-yaml-defined-harness-workflows`, `meta-workflow-builder-self-extending-harness`, `pr-acceptance-rate-harness-multiplier-evidence` | Archon open-source harness (https://github.com/coleam00/archon) |
| `five-agentic-patterns-claude-code.md` | `agent-description-auto-dispatch-routing`, `model-tier-routing-expensive-orchestrator-cheap-s`, `progressive-skill-loading`, `five-pattern-complexity-escalation-ladder` | Five agentic patterns for Claude Code post |
| `bmad-v610-v622-changelog.md` | `skills-as-markdown-sop-files-encode-processes`, `bmad-deterministic-skill-validator`, `distillator-with-round-trip-validation`, `bmad-outcome-based-skill-rewrite-pattern` | BMAD-METHOD changelog (v6.1.0 → v6.2.2) |
| https://github.com/bmad-code-org/BMAD-METHOD | `multi-ide-portability-via-installer-templates`, `everything-as-skill-architecture`, `distillator-with-round-trip-validation`, `named-agent-personas-with-session-lock` | BMAD-METHOD GitHub repo (direct upstream) |
| https://github.com/MemPalace/mempalace | `shared-instructions-multi-harness-plugin-wrappers`, `universal-harness-context-via-symlink` | MemPalace GitHub repo (direct upstream) |
| `hyperagents-arxiv-260319461.md` | `sandbox-first-modification-validation`, `emergent-tool-strategy-optimization`, `metacognitive-self-modification-hyperagents` | HyperAgents arXiv paper 26.03.19461 |
| `anthropic-demystifying-evals-for-ai-agents.md` | `eval-driven-development-autonomous-quality`, `capability-vs-regression-eval-lifecycle` | Anthropic demystifying evals documentation |
| `most-people-build-claude-skills-wrong-heres-what-w.md` | `skill-as-new-employee-mental-model`, `context-aware-routing-skill-classifier-sub-skill`, `domain-specific-intelligence-from-historical-busi` | "Most people build Claude skills wrong" practitioner post |
| `agentic-os-five-pillars-claude-code.md` | `skills-as-pointers-to-second-brain-files`, `scheduled-skill-chaining-with-file-based-activation`, `shared-context-folder-as-cross-skill-update-multiplier`, `framework-abstraction-tax-for-agents`, `platform-native-harness-over-agent-frameworks` | Agentic OS five pillars (Claude Code) post |
| `google-io-mcp-a2a-agui-protocol-stack.md` | `mcp-tool-description-prompt-injection-attack`, `operating-surface-underspecification-anti-pattern`, `tool-access-as-security-boundary-not-feature-toggle`, `coordination-cost-vs-flexibility-tradeoff-agent-delegation` | Google I/O 2025 protocol stack analysis (MCP, A2A, AgUI) |
| https://github.com/NateBJones-Projects/OB1 | `skill-self-improvement-three-approaches`, `self-improving-skill-lessons-log`, `spec-as-generator-agent-spec-pattern` | Nate B. Jones OB1 project (direct upstream) |
| https://github.com/langchain-ai/langgraph | `cross-platform-context-file-strategy`, `monorepo-context-distribution-three-strategies`, `specification-as-governance-fourth-enforcement-philosophy`, `interrupt-command-primitives-human-in-the-loop` | LangGraph v1.1.6 (direct upstream) |
| `agent-produces-100x-org-reviews-3x.md` | `skill-vs-process-distinction-deterministic-rails`, `trust-calibration-progressive-autonomy-ramp`, `compound-review-debt-from-deferred-inspection`, `reviewer-skill-elevation-for-agentic-output` | Agent productivity study: 100× individual output, 3× org reviews |
| `agent-cold-start-tacit-knowledge-elicitation.md` | `tacit-knowledge-as-agent-delegation-barrier`, `open-brain-personal-knowledge-store-pattern` | Agent cold-start tacit knowledge elicitation post |
| `bmad-method-masterclass.md` | `advanced-elicitation-techniques-library`, `yaml-templates-with-embedded-elicitation-instructions` | BMAD method masterclass content |
| `anthropic-building-effective-agents.md` | `framework-abstraction-tax-for-agents` (and harness simplification findings) | Anthropic Building Effective Agents documentation |
| `gstack-gsd-superpowers-orchestrator-headless.md` | `build-loop-skill-autonomous-phase-driver`, `gstack-specialist-role-architecture` | gstack / GSD / Superpowers orchestrator documentation |

---

## Finding-to-Source Mapping

For each finding referenced in the meta-skill, the table below shows: the finding name, a one-line
claim, the upstream source document(s), and the URL where available.

Entries marked "see /research-findings/[filename].md" have no public URL in the finding file; the
full citation chain is in the finding document itself.

| Finding | One-line claim | Upstream source(s) | URL |
|---------|---------------|-------------------|-----|
| `skill-md-frontmatter-as-discovery-trigger-primitive` | The YAML frontmatter is the only content Claude sees before deciding to load a skill, making description the single most consequential authoring variable. | Anthropic equipping-agents post, Claude Code skills docs, agentskills.io open standard, Anthropic Complete Guide PDF | https://docs.anthropic.com/en/docs/claude-code/skills — see finding for full chain |
| `meta-skill-for-skill-authorship` | Two convergent production implementations prove skill authorship is itself a packageable meta-skill with generator-assessor separation as the load-bearing governance rule. | Anthropic equipping-agents post, Anthropic skills repo (skill-creator) | https://github.com/anthropics/anthropic-agent-skills |
| `the-four-discipline-prompting-stack-nate-b-jones` | Four ascending disciplines (Prompt Craft → Context Engineering → Intent Engineering → Specification Engineering) form the diagnostic spine for all prompting work. | Nate B. Jones video series Feb–Mar 2026 | see /research-findings/the-four-discipline-prompting-stack-nate-b-jones.md |
| `generator-assessor-separation-in-skill-iteration` | Anthropic's skill-creator operationalizes five distinct subagent roles to prevent the author from grading their own artifact. | Anthropic skills repo (skill-creator) | https://github.com/anthropics/anthropic-agent-skills |
| `iterate-on-single-task-then-extract-skill` | Anthropic's primary endorsed methodology: work through ONE challenging task until success, then distill into SKILL.md. | Anthropic equipping-agents post, Anthropic skills repo, Anthropic Complete Guide PDF | https://docs.anthropic.com/en/docs/claude-code/skills |
| `skill-as-directory-progressive-disclosure-three-levels` | A skill is a filesystem directory loading content in three levels — ~100-token frontmatter always, <5K-token body on activation, bundled files on demand. | Anthropic equipping-agents post, Anthropic skills repo, agentskills.io, Anthropic Complete Guide PDF | https://agentskills.io |
| `four-discipline-prompt-evaluator` | A rubric scoring prompts across the four disciplines in dependency order produces actionable scorecards with per-dimension ratings and an enhancement handoff block. | Nate B. Jones videos, Anthropic prompt evaluation framework | see /research-findings/four-discipline-prompt-evaluator.md |
| `intent-engineering-framework-seven-part-agent-inten` | A formal seven-part structure encodes agent intent for when instructions run out, with Stop Rules as the most commonly omitted component. | productcompass.pm intent engineering article | https://www.productcompass.pm/p/intent-engineering-framework-for-ai-agents |
| `skill-description-optimization-loop-held-out-test` | Anthropic's skill-creator ships a description optimization loop treating triggering as a classification problem: 20 eval queries, 60/40 train/test, ≤5 iterations. | Anthropic skills repo (skill-creator) | https://github.com/anthropics/anthropic-agent-skills |
| `reasoning-model-anti-pattern-prescribed-reasoning` | On reasoning models, five classic techniques (CoT, few-shot, self-consistency, least-to-most, skeleton-of-thought) degrade performance. | Cross-model prompting techniques study | https://karozieminski.substack.com/p/ai-prompting-techniques-reasoning-models-2026 |
| `tacit-knowledge-as-agent-delegation-barrier` | Expertise compresses into automatic judgment even experts cannot articulate; a 5-layer elicitation workflow (~45 min) is the concrete mechanism to externalize it. | agent-cold-start-tacit-knowledge-elicitation post | see /research-findings/tacit-knowledge-as-agent-delegation-barrier.md |
| `negative-constraints-as-probabilistic-output-collapse` | Negative constraints collapse probability distribution; positive guidance only weakly biases output direction. | see finding | see /research-findings/negative-constraints-as-probabilistic-output-collapse.md |
| `declarative-goal-driven-agent-prompting` | LLMs are architecturally built to loop until they meet goals; declarative/outcome-based instructions outperform procedural step-by-step for reasoning models. | BMAD outcome-based rewrite pattern (cross-referenced) | see /research-findings/declarative-goal-driven-agent-prompting.md |
| `bmad-outcome-based-skill-rewrite-pattern` | BMAD's conversion from procedural to outcome-based instructions produced ~50% token reduction while maintaining or improving quality. | BMAD-METHOD changelog v6.1.0→v6.2.2 | https://github.com/bmad-code-org/BMAD-METHOD |
| `skill-authoring-four-guidelines` | Anthropic's four canonical orientations: Start with evaluation, Structure for scale, Think from Claude's perspective, Iterate with Claude. | Anthropic equipping-agents post, Anthropic Complete Guide PDF | https://docs.anthropic.com/en/docs/claude-code/skills |
| `multi-ide-portability-via-installer-templates` | BMAD packages identical skill definitions for 7+ IDE platforms via thin installer templates, demonstrating SKILL.md architecture is platform-agnostic. | BMAD-METHOD GitHub repo (direct) | https://github.com/bmad-code-org/BMAD-METHOD |
| `shared-instructions-multi-harness-plugin-wrappers` | MemPalace uses three-layer architecture: harness-agnostic instruction source + wrapper files + runtime delegation, eliminating drift and format coupling. | MemPalace GitHub repo (direct) | https://github.com/MemPalace/mempalace |
| `autonomy-gradient-not-binary-delegation` | Agent autonomy should be assigned per decision type on a four-level gradient using a 2×2 blast-radius × reversibility matrix. | productcompass.pm intent engineering, hitl-agentic-ai-strataio-2026-guide, Anthropic trustworthy agents | https://www.productcompass.pm/p/intent-engineering-framework-for-ai-agents |
| `capability-vs-regression-eval-lifecycle` | Eval suites must be split into capability evals (low starting pass rates) and regression evals (near-100%), with graduation thresholds. | Anthropic demystifying evals documentation | see /research-findings/capability-vs-regression-eval-lifecycle.md |
| `context-file-instruction-bloat-eth-zurich` | ETH Zurich found LLM-generated context files reduce success rates ~3% and increase inference cost 20%; even human-written files add 14–22% reasoning overhead. | ETH Zurich paper arXiv 2602.11988 (March 2026) | https://arxiv.org/abs/2602.11988 |
| `skill-security-audit-obligation` | Three distinct attack surfaces (static instructions, bundled scripts, dynamic external content) place the trust boundary at install time. | Anthropic equipping-agents post, Claude Code skills docs, Anthropic agent skills overview | see /research-findings/skill-security-audit-obligation.md |
| `spec-first-agent-briefs-prompt-craft-context-inten` | Eight spec primitives define the minimum for long-running agentic work; context and intent are first-class sections, not implicit prompt text. | maniak.io post-Feb-2026 guide, intent engineering framework | https://maniak.io/articles/2026-02-27-prompting-post-feb-2026/ |
| `bmad-deterministic-skill-validator` | BMAD replaced LLM-based code review with a 19-rule, 6-category deterministic validator in CI that catches structural violations before merge. | BMAD-METHOD changelog | https://github.com/bmad-code-org/BMAD-METHOD |
| `sandbox-first-modification-validation` | HyperAgents enforces a strict 5-step validation pipeline before committing any meta-level modification (78–92% commit rate, <1% undetected regressions). | HyperAgents arXiv paper 26.03.19461 | see /research-findings/sandbox-first-modification-validation.md |
| `skills-as-open-portable-standard` | Anthropic published Agent Skills as open standard at agentskills.io (Dec 2025, Apache 2.0 / CC-BY-4.0); adopters include Google Labs, Vercel, Stripe. | agentskills.io, Anthropic equipping-agents post, Anthropic Complete Guide PDF | https://agentskills.io |
| `yaml-templates-with-embedded-elicitation-instructions` | BMAD YAML agent templates contain two interleaved layers (output structure + per-section LLM instructions) that prevent one-shot document dumps. | BMAD method masterclass | https://github.com/bmad-code-org/BMAD-METHOD |
| `progressive-tiered-context-loading-convergence` | Four independent repos (BMAD, OpenViking, DeerFlow, Beads) converged on L0 abstract → L1 overview → L2 full body loading. | Cross-repo analysis (BMAD, OpenViking, DeerFlow, Beads) | https://github.com/bmad-code-org/BMAD-METHOD (primary) |
| `verification-agent-seven-prompt-patterns` | Seven prompt engineering patterns from Claude Code's verification sub-agent: adversarial framing, read-only permissions, binary pass/fail, anti-skip prompting, etc. | Claude Code internal architecture leak analysis | see /research-findings/verification-agent-seven-prompt-patterns.md |
| `two-level-verification-agent-run-plus-harness-inte` | Verification must operate at two levels: Level 1 (did agent produce correct output?) and Level 2 (when harness changes, do guardrails still hold?). | Anthropic Claude Code codebase (Nate B. Jones analysis) | see /research-findings/two-level-verification-agent-run-plus-harness-inte.md |
| `acceptance-criteria-as-verifiable-eval-anchor` | The most reliable way to prevent agent drift is verifiable pass/fail acceptance criteria plus 3–5 known-good eval cases as anchor for iterative improvement. | maniak.io post-Feb-2026 guide (cross-referenced) | see /research-findings/acceptance-criteria-as-verifiable-eval-anchor.md |
| `critic-verifier-loop-with-termination` | A generate–critique–patch cycle with explicit termination conditions and a fail-closed critic prevents unbounded token loops. | multi-agent-orchestration-production-playbook | see /research-findings/critic-verifier-loop-with-termination.md |
| `design-evaluate-dual-phase-prompting-framework` | Every prompting technique has two required phases: Design phase (before) and Evaluate phase (after), both requiring human judgment. | every-ai-prompting-technique-that-works-on-reasoni, prompting-best-practices-collection | see /research-findings/design-evaluate-dual-phase-prompting-framework.md |
| `core-specialized-skill-inheritance-pattern` | Skills declare `specializes: <core-skill>` linking to a shared repo; specialized skills customize only declared slots without forking. | Cross-repo analysis; production-tested at Warp (15 skills) | see /research-findings/core-specialized-skill-inheritance-pattern.md |
| `skill-frontmatter-validation-rules` | Mechanical validation rules for SKILL.md frontmatter: name ≤64 chars, lowercase a-z/0-9/hyphens, no reserved words, description no XML. | agentskills.io open standard, Anthropic agent skills overview | https://agentskills.io |
| `skill-description-structure-what-when-capabilities` | Canonical three-part description structure: [What it does] + [When to use it] + [Key capabilities]. | Anthropic Complete Guide PDF | see /research-findings/skill-description-structure-what-when-capabilities.md |
| `agent-action-reversibility-as-design-requirement` | Every agent action must be classified on the reversibility spectrum; gate intensity is proportional to irreversibility. | Lilly incident security case study | see /research-findings/agent-action-reversibility-as-design-requirement.md |
| `permission-compounding-across-agent-delegation-chains` | Each delegation step can only reduce permissions; Agent B's scope must be strict subset of Agent A's (monotonic narrowing). | Lilly incident security case study | see /research-findings/permission-compounding-across-agent-delegation-chains.md |
| `human-on-the-loop-hotl-autonomy-tiering-framework` | Veto Protocol with three-question Decision Summary + EU AI Act Article 14 compliance as the governance framework for HITL gates. | hitl-agentic-ai-strataio-2026-guide, Anthropic trustworthy agents | see /research-findings/human-on-the-loop-hotl-autonomy-tiering-framework.md |
| `advisory-only-for-persistent-mutations` | Mutations of persistent/broad-blast state (schema changes, governance docs) blocked until human manually applies — advisory artifact only. | Internal MetaSystem architecture (cross-referenced) | see /research-findings/advisory-only-for-persistent-mutations.md |
| `five-layer-agent-prompt-architecture` | Five-layer completeness template: Role & Scope / Instructions & Constraints / Context & Retrieved Data / Examples & Edge Cases / Output Format & Tool-Calling. | see finding | see /research-findings/five-layer-agent-prompt-architecture.md |
| `hands-off-routine-prompt-precision-pattern` | Unattended/scheduled routines require numbered SOP instructions with explicit completion signals; outcome-based instructions are insufficient for autonomous execution. | see finding | see /research-findings/hands-off-routine-prompt-precision-pattern.md |
| `prompt-as-policy-version-control-and-cicd-for-agen` | Treating agent prompts as versioned policy artifacts with ROLE/AUTHORITY/CONSTRAINT/FAILURE SIGNAL properties and CI/CD hooks formalizes skill versioning. | ai-agent-prompt-engineering-best-practices-inflect | https://www.reddit.com/r/PromptEngineering/comments/1q8elob/prompting_apo_and_agentic_systems_in_2026/ |
| `specification-as-governance-fourth-enforcement-philosophy` | Specification-based governance (LangGraph conformance tests, n8n spec-driven dev) makes compliance verified, not just instructed. | LangGraph v1.1.6, n8n v2.16.0 | https://github.com/langchain-ai/langgraph — https://github.com/n8n-io/n8n |
| `skill-testing-three-tier-trigger-functional-perf` | Three-tier skill testing: Tier 1 (triggering), Tier 2 (functional), Tier 3 (performance baseline comparison). Target: 90% trigger rate on relevant queries. | Anthropic skills repo, Anthropic Complete Guide PDF | https://github.com/anthropics/anthropic-agent-skills |
| `eval-driven-development-autonomous-quality` | Eval-driven development — building evaluation suites agents run against — is identified as one of three essential 2026 builder skills. | Nate B. Jones videos, Anthropic demystifying evals | see /research-findings/eval-driven-development-autonomous-quality.md |
| `self-improving-skill-lessons-log` | After every invocation, append lessons to SKILL.md Lessons Log section based on three questions: lost work? reasonable tokens? user correction? | Nate B. Jones OB1 repo | https://github.com/NateBJones-Projects/OB1 |
| `bidirectional-prompting-for-spec-creation` | Before implementation, alternating Q&A between user and Claude until both share identical mental model prevents implicit training-data assumptions from becoming bugs. | TACHES claude-code-resources-skills | see /research-findings/bidirectional-prompting-for-spec-creation.md |

---

## How To Use This File

**Citing in conversation:** Use `[finding-filename]` notation. Example: "Outcome-based instructions
outperform procedural step-by-step on frontier reasoning models
`[declarative-goal-driven-agent-prompting]`."

**Verifying upstream:** Look up the finding in the URL column above. If marked "see
/research-findings/[filename].md", open that file to find the upstream citation chain.

**Updating this file:** When new findings are added to the improvement-loop corpus, add rows to the
Finding-to-Source Mapping table and check whether the upstream source already appears in the
Multiply-Cited Sources table.

**When a URL is stale:** Flag in the finding file itself; the finding file is the source of truth
for upstream citations.
