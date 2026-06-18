---
notion_id: null
log_entry: "IL Stream 0 step A: §Construction substrate landed for skill/agent concept docs, design.md rewritten in author mode, rule 12 (audit/design symmetry) codified, consumer-abstractions-map filed"
actor: "Nick + Agent: Claude (Owner disposition)"
area: null
change_type: "Governance / Substrate Update"
milestone: "Cross-system roadmap step A"
rationale: "Completed cross-system roadmap step A from session 106 plan. Substep A.2 (Librarian audit) had landed previously; this session completed the remaining five substeps (A.4a, A.4b, A.3, A.5, A.6) that operationalize the Librarian's audit/design symmetry at the concept-doc level. Skill and agent concept docs now carry §Construction substrate (Decision sequence, Template skeleton, Scoping heuristics, Authoring-time anti-patterns); design.md was rewritten from advisor mode (legacy 2026-04-22) to author mode to align with /design-skill and /design-agent build targets; rule 12 codifies the structural invariant that audit and design read the same substrate; consumer-abstractions-map gates which abstractions earn substrate per rule 11."
source_dd: "DD-82, DD-86"
target_system: "Improvement Loop"
timestamp: "2026-06-11T00:00:00.000Z"
---

## What Changed

- **A.4a — `skill.md` Construction section.** Replaced standalone `## Safety-critical classification` with `## Construction` containing four sub-sections; classification promoted into Decision sequence step 4 (no content duplication). Updated Librarian read rule to reference Construction step 4 instead of "see classification above".
- **A.4b — `agent.md` Construction section.** Replaced standalone `## Variant selection` with variant-aware `## Construction`; variant selection promoted into Decision sequence step 1. Template skeleton encodes common-core + variant overlays (B, C). Updated Librarian read rule so the `design → ### Step N` forward pointer now references the just-landed §Construction substrate.
- **A.3 — `design.md` rewritten in author mode.** Existing design.md (2026-04-22, advisor mode — produced step guidance for consumer to follow) was replaced by an author-mode spec — produces a draft artifact directly, composing from §Construction substrate. Six phases mirror audit.md structure; Phase 5 delegates audit to `/assess-*` in fresh context per rule 10. Predecessor noted in the new spec's Short definition; advisor-mode operation can be reintroduced as `advise.md` if recurrence evidence emerges (rule 11).
- **A.5 — Rule 12 (Audit-design symmetry) codified.** Appended to `governance/agent-rules.md`. Captures the structural invariant that audit and design compose against the same concept doc — §Composition for audit, §Construction for design, bilingual readings of one substrate. Source attribution names rule 10 (structural prerequisite) and rule 11 (substrate abstraction earning its keep) as parents. Existing §Construction debt (harness, second-brain, memory, context-rot, agentic-systems, prompt) acknowledged as non-blocking IB work.
- **A.6 — `consumer-abstractions-map.md` filed.** New reference in `operations/references/`. Inventories Skill / Agent (strong, committed), Prompt (moderate, audit-only), Governance / Security (weak, Nick-named aspirational), Memory / Hook / Workflow / Tool / Eval-suite / Subagent / Context-structure (weak, future candidates not committed). Encodes promotion rules per rule 11.

## Affected Items

- `systems/improvement-loop/operations/references/librarian/skill.md` — Construction added; Safety-critical classification promoted in.
- `systems/improvement-loop/operations/references/librarian/agent.md` — Construction added (variant-aware); Variant selection promoted in.
- `systems/improvement-loop/operations/references/librarian/design.md` — full rewrite from advisor mode to author mode.
- `systems/improvement-loop/governance/agent-rules.md` — rule 12 appended; updated date 2026-06-11.
- `systems/improvement-loop/governance/_index.md` — agent-rules.md summary row updated to include "audit-design symmetry".
- `systems/improvement-loop/operations/references/consumer-abstractions-map.md` — new file.
- Workspace `PROGRESS.md` — step A → Done; step B → In progress.
- `systems/improvement-loop/PROGRESS.md` — Current Focus updated.

## Decision Trail

- **Librarian review (rule 10).** Drafts for A.3 and A.5 were reviewed by Librarian subagent in fresh context before writing. Verdict: Approve with edits. Six prescribed edits applied: A.3 (Output shape filled in, Phase 3 anti-pattern boundary clarified, ~500-line size gate added, Phase 1 §Composition forward-reference clarified); A.5 (source attribution revised to remove weak rule 5 link, §Construction debt acknowledged).
- **design.md replacement (vs. augment).** Nick gated. Existing advisor-mode design.md predated §Construction substrate and rule 12. Author mode is what cross-system roadmap step D (`/design-skill`, `/design-agent`) requires and what audit/design symmetry implies. Replacement preserves the option to reintroduce advisor mode as a separate operation when recurrence evidence justifies it (rule 11).
