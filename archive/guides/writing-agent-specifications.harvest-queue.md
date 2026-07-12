# Harvest Queue — Writing Agent Specifications

Candidates for extraction into standalone artifacts (rule/skill/template forms only).

| Finding | Candidate Form | Artifact Concept | Rationale |
|---------|---------------|------------------|-----------|
| `intent-based-meta-routing-skill` | template | Intent Routing Table Template — standalone markdown template for systems with 5+ skills, mapping intent keywords to skill files with fallback rules | Guide Step 6 mentions routing but does not provide a standalone routing table template; systems building skill catalogs need a reusable scaffold |
| `stop-rules-as-execution-boundaries` | rule | Three-Type Stop Rule Requirement — every agent spec and SKILL.md must include at least one halt condition, one escalation trigger, and one completion criterion | Most commonly omitted component; a standalone rule enables enforcement at review/audit time without requiring the full guide |
| `project-specific-custom-skills-for-repeated-task` | rule | Skill Extraction Trigger Rule — when a multi-step task with stable domain context is performed 3+ times, it must be packaged as a reusable skill specification | Prevents perpetual re-specification; the "3 times" threshold gives a concrete, auditable trigger |
