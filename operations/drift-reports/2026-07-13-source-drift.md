---
type: "drift-report"
target_system:
  - "improvement-loop"
generated_by: "/detect-drift"
date: "2026-07-13"
invocation_context: "codifier-run pre-step (Nick-authorized 2026-07-13)"
total_scanned: 125
drift_hits: 42
schematic_drift_hits: 4
clean_count: 79
enumeration_gaps: 0
unresolvable_sources: 0
forms_scanned:
  - "rules"
  - "skills"
  - "templates"
  - "agents"
  - "schematics"
---

# Source Drift Report — 2026-07-13

**Invocation context:** codifier-run pre-step (Nick-authorized 2026-07-13)

**Scan summary:** 125 artifacts scanned across forms (rules, skills, templates, agents, schematics); 42 extract drift hit(s); 4 schematic drift hit(s); 79 drift-clean; 0 enumeration gap(s); 0 unresolvable source(s).

**Judgment method note:** Most hits date from the 2026-07-12/13 crosslink sweep and priority reassessment. To separate material from cosmetic drift, each source finding's state at the artifact's baseline date was git-diffed against HEAD, distinguishing body changes from frontmatter-only changes (typed links, reverse links, `consumed_by`, YAML requoting from `kb_parser` writes, priority metadata). Body unchanged + metadata-only → cosmetic; new dated evidence sections or evidence-strength shifts → material.

**Recommendation tallies:** extracts — 11 `re-run /extract-artifacts on this finding`, 31 `dismiss as cosmetic`, 0 `reclassify`. Schematics — 3 `re-evaluate this schematic against its moved grounding`, 1 `dismiss as cosmetic`.

## Drift Hits

### agent-must-read-and-update-memory-md-on-startup
- Source: [[memorymd-cross-session-preference-persistence]]
- Source updated: 2026-07-12 (post-extraction)
- Artifact extracted: 2026-04-27
- Recommendation: dismiss as cosmetic

Body unchanged; only `consumed_by`, `related_findings` crosslinks, and YAML requoting moved.

### agent-self-reporting-unreliability-independent-eval
- Source: [[agent-self-reporting-unreliability-independent-eval]]
- Source updated: 2026-07-13 (post-extraction)
- Artifact extracted: 2026-04-19
- Recommendation: dismiss as cosmetic

Body unchanged since extraction; changes are crosslinks plus a priority assignment (P1). Priority is pipeline metadata — the rule's content remains faithful to the finding.

### agentic-harness-self-assessment
- Source: [[agentic-harness-self-assessment-skill]]
- Source updated: 2026-07-13 (post-extraction)
- Artifact extracted: 2026-04-19
- Recommendation: dismiss as cosmetic

Body unchanged; crosslinks + priority assignment (P2) only.

### ai-and-human-vaults-must-be-separate
- Source: [[ai-managed-vault-separate-from-human-vault]]
- Source updated: 2026-07-12 (post-extraction)
- Artifact extracted: 2026-04-27
- Recommendation: dismiss as cosmetic

Body unchanged; `consumed_by` + crosslinks only.

### apply-hard-ceilings-to-agent-memory-files
- Source: [[bounded-tiered-memory-inference-driven-curation]]
- Source updated: 2026-07-13 (post-extraction)
- Artifact extracted: 2026-05-25
- Recommendation: re-run /extract-artifacts on this finding

New "Practitioner Rebuild in Claude Code (2026-07)" body section: concrete cap evidence (2,500-char memory.md), post-turn-hook curation, user-editable promotion rules, and failure evidence for unbounded curation — materially strengthens and specifies the rule's claim.

### claudemd-symlink-to-agentsmd-at-every-governance-boundary
- Source: [[distributed-boundary-guides]]
- Source updated: 2026-07-13 (post-extraction)
- Artifact extracted: 2026-04-27
- Recommendation: dismiss as cosmetic

Body unchanged; crosslinks only.

### compounding-loops-must-encode-outcomes
- Source: [[compounding-knowledge-loop-internal-data]]
- Source updated: 2026-07-12 (post-extraction)
- Artifact extracted: 2026-04-27
- Recommendation: dismiss as cosmetic

Body unchanged; `consumed_by` + crosslinks only.

### context-degradation-40-percent-threshold
- Source: [[context-degradation-40-50-percent-threshold]]
- Source updated: 2026-05-25 (post-extraction)
- Artifact extracted: 2026-05-24
- Recommendation: dismiss as cosmetic

One-day drift window predates git history, but the body carries no post-extraction dated content and no evidence-strength change — consistent with the 05-25 linkage-session metadata touch.

### core-specialized-skill-pair-spec
- Source: [[core-specialized-skill-inheritance-pattern]]
- Source updated: 2026-07-13 (post-extraction)
- Artifact extracted: 2026-05-25
- Recommendation: dismiss as cosmetic

Body unchanged since first git snapshot; crosslinks only.

### default-to-file-search-before-rag
- Source: [[file-search-outperforms-rag-for-small-corpora]]
- Source updated: 2026-07-12 (post-extraction)
- Artifact extracted: 2026-05-25
- Recommendation: dismiss as cosmetic

Body unchanged; frontmatter changes are YAML requoting + crosslinks.

### eval-driven-tool-iteration-loop
- Source: [[eval-driven-tool-iteration-loop]]
- Source updated: 2026-07-12 (post-extraction)
- Artifact extracted: 2026-04-19
- Recommendation: dismiss as cosmetic

Body unchanged; crosslinks + priority assignment (P2) only.

### explicit-permission-allow-listing-for-agent-resource-access
- Source: [[explicit-permission-allow-listing-for-agent-resou]]
- Source updated: 2026-07-12 (post-extraction)
- Artifact extracted: 2026-04-26
- Recommendation: dismiss as cosmetic

Body unchanged; crosslinks only.

### filesystem-lock-parallel-agent-coordination
- Source: [[file-based-task-locking-parallel-agents]]
- Source updated: 2026-07-12 (post-extraction)
- Artifact extracted: 2026-04-27
- Recommendation: dismiss as cosmetic

Body unchanged; crosslinks only.

### framework-skill-integration-pattern
- Source: [[skills-portability-across-sdk-and-framework-boundaries]]
- Source updated: 2026-07-13 (post-extraction)
- Artifact extracted: 2026-05-25
- Recommendation: dismiss as cosmetic

Body unchanged since first git snapshot; crosslinks only.

### headless-multi-pass-iterative-review
- Source: [[headless-multi-pass-iterative-review]]
- Source updated: 2026-07-13 (post-extraction)
- Artifact extracted: 2026-05-25
- Recommendation: dismiss as cosmetic

Body unchanged; frontmatter diff is YAML line-reflow of `summary`/`implementation_notes` (same text) plus two `same-problem` crosslinks.

### holdout-validation-pattern-blind-regression
- Source: [[holdout-validation-pattern-blind-regression]]
- Source updated: 2026-07-12 (post-extraction)
- Artifact extracted: 2026-05-25
- Recommendation: dismiss as cosmetic

Body unchanged; `consumed_by` + crosslinks only.

### html-pr-explainer-with-margin-annotations
- Source: [[html-pr-explainer-with-margin-annotations]]
- Source updated: 2026-07-13 (post-extraction)
- Artifact extracted: 2026-05-25
- Recommendation: dismiss as cosmetic

Body unchanged since first git snapshot; crosslinks only.

### iterative-refinement-loop-with-quality-gate
- Source: [[iterative-refinement-loop-with-quality-gate]]
- Source updated: 2026-07-13 (post-extraction)
- Artifact extracted: 2026-04-26
- Recommendation: re-run /extract-artifacts on this finding

New 2026-07-13 Archon v0.5.0 corroboration is material: a shipped adversarial Generator/Evaluator workflow with explicit numeric criteria (7/10 gate, bounded retries) that structurally answers the finding's flagged self-evaluation-bias failure mode — content the skill artifact should incorporate.

### maximum-unreviewed-depth-policy
- Source: [[compound-review-debt-from-deferred-inspection]]
- Source updated: 2026-07-13 (post-extraction)
- Artifact extracted: 2026-04-27
- Recommendation: dismiss as cosmetic

Body unchanged; crosslinks only.

### mcp-tool-description-prompt-injection-attack-surface
- Source: [[mcp-tool-description-prompt-injection-attack]]
- Source updated: 2026-05-25 (post-extraction)
- Artifact extracted: 2026-05-24
- Recommendation: dismiss as cosmetic

One-day drift window predates git history, but the body carries no post-extraction dated content and no evidence-strength change — consistent with the 05-25 linkage-session metadata touch.

### never-ask-claude-to-compact-claudemd
- Source: [[catastrophic-context-collapse-risk-during-claudemd]]
- Source updated: 2026-05-24 (post-extraction)
- Artifact extracted: 2026-04-27
- Recommendation: dismiss as cosmetic

Body unchanged over the full window; `consumed_by` + crosslinks only.

### never-inline-ephemeral-into-cached-layers
- Source: [[layered-prompt-assembly-stable-segment-caching]]
- Source updated: 2026-07-13 (post-extraction)
- Artifact extracted: 2026-05-25
- Recommendation: re-run /extract-artifacts on this finding

New opencode cross-harness section adds cache-write/read economics (~1.25x write, ~0.1x read, breakeven at ~1.4 reads) that strengthens the rule's rationale. Note: the update is corroborative — the re-extract likely touches the rule's evidence/rationale, not its normative statement.

### no-agent-action-without-identity-record
- Source: [[agent-identity-governance-enforcement-layer]]
- Source updated: 2026-07-12 (post-extraction)
- Artifact extracted: 2026-04-27
- Recommendation: dismiss as cosmetic

Body unchanged; crosslinks + `sources` link additions only.

### prefer-cli-over-mcp-when-both-exist-for-the-same-tool
- Source: [[cli-first-tool-integration-less-overhead-than-mcp]]
- Source updated: 2026-07-12 (post-extraction)
- Artifact extracted: 2026-05-25
- Recommendation: dismiss as cosmetic

Body unchanged; `consumed_by` + crosslinks + YAML requoting only.

### production-database-wipeout-agent-context
- Source: [[production-database-wipeout-agent-context]]
- Source updated: 2026-07-13 (post-extraction)
- Artifact extracted: 2026-05-25
- Recommendation: dismiss as cosmetic

Body unchanged; crosslinks only.

### progressmd-session-bridge-template
- Source: [[progress-md-session-bridge]]
- Source updated: 2026-07-13 (post-extraction)
- Artifact extracted: 2026-04-27
- Recommendation: dismiss as cosmetic

Body unchanged; `consumed_by`, `sources`, and crosslinks only.

### ralph-wiggum-execution-pattern
- Source: [[ralph-wiggum-execution-pattern]]
- Source updated: 2026-07-13 (post-extraction)
- Artifact extracted: 2026-05-25
- Recommendation: re-run /extract-artifacts on this finding

Confirmed material (the pre-flagged suspect): (1) priority upgraded P2 → P1 (Nick-accepted, criteria C1/C4/C5, 5 independent orgs); (2) Archon v0.5.0 promotes the loop to a schema-enforced `loop:` engine primitive (`until`/`until_bash`, required `max_iterations`, `fresh_context` with `$LOOP_PREV_OUTPUT` bridging, per-iteration gates); (3) Nick gate note establishes Ralph/PIV as sibling loop variants with distinct loop topologies. The staged skill predates all three.

### reach-l6-before-l7
- Source: [[context-infrastructure-seven-level-maturity-model]]
- Source updated: 2026-07-12 (post-extraction)
- Artifact extracted: 2026-04-27
- Recommendation: dismiss as cosmetic

Body unchanged; `consumed_by` + crosslinks only.

### scheduled-workflows-require-human-checkpoint
- Source: [[five-pillar-agentic-os-framework]]
- Source updated: 2026-05-25 (post-extraction)
- Artifact extracted: 2026-04-27
- Recommendation: dismiss as cosmetic

Body unchanged over the full window; crosslinks only.

### screen-as-permissions-model-agent-bypass
- Source: [[screen-as-permissions-model-agent-bypass-failure]]
- Source updated: 2026-05-25 (post-extraction)
- Artifact extracted: 2026-05-24
- Recommendation: re-run /extract-artifacts on this finding

The finding gained a dated "Evidence Strengthening — 2026-05-25" section one day after extraction: evidence upgraded Medium → Strong, and the incident is reframed as an industry-wide systemic pattern (six-vendor convergence) rather than a single-org failure — material to the rule's claim strength and scope.

### seven-layer-prompt-assembly-with-cache-control
- Source: [[layered-prompt-assembly-stable-segment-caching]]
- Source updated: 2026-07-13 (post-extraction)
- Artifact extracted: 2026-05-25
- Recommendation: re-run /extract-artifacts on this finding

The opencode addition supplies the concrete breakpoint-placement heuristic (last tool definition, last system part, latest user message) that the finding's original source left open — directly material to a prompt-assembly template with cache-control markers.

### skill-self-improvement-lessons-log-template
- Source: [[self-improving-skill-lessons-log]]
- Source updated: 2026-07-12 (post-extraction)
- Artifact extracted: 2026-05-25
- Recommendation: re-run /extract-artifacts on this finding

Second independent implementation added (AI LABS "learning loop", separate `learning.md` journal) — a structural variant (external journal vs in-skill appended log) that expands the template's applicability options. Modest but not cosmetic.

### skills-reference-shared-context-by-path
- Source: [[skills-as-pointers-to-second-brain-files]]
- Source updated: 2026-07-12 (post-extraction)
- Artifact extracted: 2026-04-27
- Recommendation: re-run /extract-artifacts on this finding

New "Additional Evidence — 2026-07-12" body section: two independent corroborating channels and an expanded applicability span (root-router, skill-context, and loop-state applications; read-your-own-history payoff) — expanded applicability per the enum's material test.

### stupid-button-token-audit-diagnostic
- Source: [[stupid-button-six-question-token-audit-diagnostic]]
- Source updated: 2026-07-12 (post-extraction)
- Artifact extracted: 2026-04-19
- Recommendation: dismiss as cosmetic

Body unchanged; crosslinks + priority assignment (P2) only.

### surgical-change-agent-scope
- Source: [[surgical-change-constraint-agent-scope]]
- Source updated: 2026-07-12 (post-extraction)
- Artifact extracted: 2026-04-20
- Recommendation: dismiss as cosmetic

Body unchanged; the wide frontmatter field list is YAML requoting (values identical) plus crosslink/`sources` additions.

### tacit-knowledge-elicitation-template
- Source: [[tacit-knowledge-as-agent-delegation-barrier]]
- Source updated: 2026-07-13 (post-extraction)
- Artifact extracted: 2026-05-25
- Recommendation: dismiss as cosmetic

Body unchanged; YAML requoting + `consumed_by` + crosslinks only.

### task-to-file-routing-table-in-context-files
- Source: [[task-to-file-routing-table-in-context-files]]
- Source updated: 2026-07-12 (post-extraction)
- Artifact extracted: 2026-04-26
- Recommendation: dismiss as cosmetic

Body unchanged; crosslinks only.

### test-context-strategies-against-actual-model
- Source: [[model-specific-context-file-sensitivity]]
- Source updated: 2026-07-12 (post-extraction)
- Artifact extracted: 2026-04-27
- Recommendation: re-run /extract-artifacts on this finding

New "Corroboration Note — 2026-07-12": production-scale Lindy migration evidence extends the claim from context-file sensitivity to whole-harness scope (memory architecture, prompts, tool-call handling) — a material broadening of the rule's applicability.

### tier-based-orchestrator-effort-scaling-rules
- Source: [[effort-scaling-rules-embedded-in-orchestrator]]
- Source updated: 2026-07-13 (post-extraction)
- Artifact extracted: 2026-04-27
- Recommendation: dismiss as cosmetic

Body unchanged; crosslinks only.

### tiered-memory-file-architecture
- Source: [[bounded-tiered-memory-inference-driven-curation]]
- Source updated: 2026-07-13 (post-extraction)
- Artifact extracted: 2026-05-25
- Recommendation: re-run /extract-artifacts on this finding

Same material source movement as `apply-hard-ceilings-to-agent-memory-files`: the Claude Code practitioner rebuild adds portable-markdown architecture details (post-turn hook writes, dedup-then-replace overflow policy, user-editable promotion rules) directly relevant to this template's structure.

### trust-promotion-and-demotion-thresholds
- Source: [[trust-calibration-progressive-autonomy-ramp]]
- Source updated: 2026-07-12 (post-extraction)
- Artifact extracted: 2026-04-27
- Recommendation: re-run /extract-artifacts on this finding

Evidence strength upgraded Medium → Strong, third independent corroboration (Cole Medin), and a new subtractive framing — promotion means removing an existing human touchpoint from an already-trusted workflow — that refines how the rule's thresholds should be expressed.

### verify-sub-agent-wiring-after-each-wave
- Source: [[orchestrated-execution-one-task-per-sub-agent-wit]]
- Source updated: 2026-07-12 (post-extraction)
- Artifact extracted: 2026-05-25
- Recommendation: dismiss as cosmetic

Body unchanged; `consumed_by` + crosslinks + YAML requoting only.

## Schematic Drift Hits

### codebase-audit-workcell
- Schematic last curated: 2026-06-18 (`updated`)
- Moved grounding(s):
  - [[agent-self-reporting-unreliability-independent-eval]] — last_updated 2026-07-13 (post-curation)
  - [[llm-as-judge-pattern-for-verification-agents]] — last_updated 2026-07-12 (post-curation)
  - [[subagent-isolation-contract]] — last_updated 2026-07-13 (post-curation)
- Recommendation: dismiss as cosmetic

All three groundings moved by crosslink additions only; no body content changed since curation. The evidence the schematic rests on is undisturbed.

### project-coding-workcell
- Schematic last curated: 2026-06-18 (`updated`)
- Moved grounding(s):
  - [[autonomy-gradient-not-binary-delegation]] — last_updated 2026-07-12 (post-curation)
  - [[builder-validator-chain-pattern]] — last_updated 2026-07-13 (post-curation)
  - [[compound-review-debt-from-deferred-inspection]] — last_updated 2026-07-13 (post-curation)
- Recommendation: re-evaluate this schematic against its moved grounding

`autonomy-gradient-not-binary-delegation` gained a material body section (Cole Medin / Dan Shapiro five-level ladder): the gradient is traversed over time as maturity grows, per workflow — a second axis complementary to the blast-radius 2x2 that may change the schematic's autonomy-configuration mapping. The other two groundings moved by crosslinks only.

### research-scanning-agent
- Schematic last curated: 2026-06-18 (`updated`)
- Moved grounding(s):
  - [[agent-self-reporting-unreliability-independent-eval]] — last_updated 2026-07-13 (post-curation)
  - [[bounded-tiered-memory-inference-driven-curation]] — last_updated 2026-07-13 (post-curation)
  - [[context-curation-over-context-stuffing]] — last_updated 2026-07-12 (post-curation)
  - [[karpathy-autoresearch-self-improvement-loop]] — last_updated 2026-07-12 (post-curation)
- Recommendation: re-evaluate this schematic against its moved grounding

`bounded-tiered-memory-inference-driven-curation` gained the material Claude Code practitioner-rebuild section (size caps, post-turn-hook curation, unbounded-curation failure evidence) — memory architecture is load-bearing for this schematic. The other three groundings moved by crosslinks only.

### scheduled-operations-assistant
- Schematic last curated: 2026-06-18 (`updated`)
- Moved grounding(s):
  - [[advisory-only-for-persistent-mutations]] — last_updated 2026-07-13 (post-curation)
  - [[ai-managed-vault-separate-from-human-vault]] — last_updated 2026-07-12 (post-curation)
  - [[autonomy-gradient-not-binary-delegation]] — last_updated 2026-07-12 (post-curation)
- Recommendation: re-evaluate this schematic against its moved grounding

Same material `autonomy-gradient-not-binary-delegation` movement as `project-coding-workcell` (maturity-gated autonomy progression) — directly relevant to a scheduled assistant's autonomy configuration. The other two groundings moved by crosslinks only.
