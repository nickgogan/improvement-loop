# Changelog — Writing Agent Specifications

## 2026-07-13 — Session 145 — staleness-threshold

- Findings: 21 (+12, -0 since last synthesis: 5 newly absorbed, 7 restorations of stems consumed at sessions 44/98 whose `consumed_by` back-annotations existed but had dropped out of `source_findings` — frontmatter repair, no body change from them)
- Added: [[plans-that-carry-their-own-contract]], [[war-game-plan-format-for-executor-handoff]], [[unknowns-reduction-phase-anchored-technique-set]], [[human-ai-seam-identification-three-question-rubric]], [[role-registry-prompt-hook-routing-backstop]] (new); restored: [[acceptance-criteria-as-verifiable-eval-anchor]], [[autonomy-gradient-not-binary-delegation]], [[context-enrichment-for-task-clarity]], [[health-metrics-vs-hard-constraints-distinction]], [[intent-engineering-framework-seven-part-agent-inten]], [[spec-first-agent-briefs-prompt-craft-context-inten]], [[task-contract-pattern-schema-first-agent]]
- Structural: added Step 0 (human/AI seam map before spec), Step 1a (author unknowns-reduction techniques), Step 7 (carried-contract executor handoffs: verbatim Global Constraints, per-task Interfaces, war-game failure branches, blocked-variables ledger, deviations protocol, abort conditions); Step 6 extended with deterministic prompt-hook routing backstop; new Plan Handoff Contract template + KB-backfill worked example; Key Concepts +2 (seam-before-spec, carried contracts); Pitfalls +4 (#12–#15)
- Preserved: none (no Nick's Annotations or PRESERVE markers found)
- SL: session-145 (SL retired as producer per session-138 ruling; git is the session record)

## 2026-05-25 — Session 98 — staleness-threshold

- Findings: 7 → 11 (+4: context-gap-task-vs-job, intent-based-meta-routing-skill, project-specific-custom-skills-for-repeated-task, stop-rules-as-execution-boundaries)
- Structural: Added Step 1 (Context Gap Assessment) before intent definition; expanded Step 4c (Stop Rules) into three explicit subtypes (halt/escalate/complete); added Step 6 (Skill Packaging) for repeated-task encoding; added Context Gap Assessment Worksheet template; added Skill Specification Addendum template; expanded Stop Rules in main template from flat list to three-type structure
- Key Concepts: expanded from 5 to 9; added #2 (task vs job context gap), #5 (stop rules as boundaries not suggestions), #8 (repeated tasks earn skills), #9 (intent routing scales systems)
- Pitfalls: expanded from 8 to 11; added #2 (stop rules only in prompt layer), #3 (ignoring context gap), #11 (re-specifying same task repeatedly)
- Worked Example: enriched with Context Supply Plan section and three-type Stop Rules structure
- Related Guides: added cross-refs to G2 (context gap) and G5 (skill packaging)
- Contract: updated invariants to require stop rules with all three types and context supply plan; updated recovery to cover confabulation from missing context
- Preserved: none (no Nick's Annotations or PRESERVE markers found)
- SL: session-98

## 2026-04-19 — Session 44 — initial-synthesis

- Findings: 7
- Structural: initial synthesis; no prior version
- Preserved: none
- SL: [[session-44-codifier-extraction-run]]
