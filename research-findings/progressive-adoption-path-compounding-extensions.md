---
name: "Progressive Adoption Path with Compounding Extensions"
summary: "A curated sequence of domain extensions that build on each other, creating cross-domain agent capabilities through progressive adoption. OB1's 6-extension learning path moves users from single-domain (household knowledge) to cross-domain integration (CRM knows captured thoughts, meal planner checks who's home, job contacts become professional network contacts)."
implementation_notes: "MetaSystem has no progressive adoption path. Systems are designed as standalone units. The extension compounding pattern could inform how Household OS capabilities are sequenced and how cross-domain integration is designed."
category: "Agentic OS"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
proposer_priority: P2 (Design Required)
applicability:
  - "S3 (Claude Code Build)"
  - "General"
adopted_in: []
sources: []
related_findings:
  - file: "five-pillar-agentic-os-framework.md"
    rel: "extends"
  - file: "context-infrastructure-seven-level-maturity-model.md"
    rel: "same-problem"
date_discovered: "2026-04-20"
last_updated: "2026-04-20"
pipeline_status: raw
consumed_by: []
---

## What It Is
A curated learning path of 6 domain extensions, ordered by difficulty and designed to compound:

1. **Household Knowledge Base** (Beginner) — Home facts the agent can recall
2. **Home Maintenance Tracker** (Beginner) — Scheduling and history for home upkeep
3. **Family Calendar** (Intermediate) — Multi-person schedule coordination
4. **Meal Planning** (Intermediate) — Recipes, meal plans, shared grocery lists
5. **Professional CRM** (Intermediate) — Contact tracking wired into thoughts
6. **Job Hunt Pipeline** (Advanced) — Application tracking and interview pipeline

The key design principle: extensions compound. The CRM knows about thoughts captured earlier. The meal planner checks who's home this week (via the calendar extension). Job hunt contacts automatically become professional network contacts (via the CRM extension). This creates a progressive adoption path where each extension is independently useful but becomes more powerful as the user builds more.

## Why It Matters
Most personal OS systems present capabilities as a flat menu — install what you want. The progressive path solves three problems: (1) decision paralysis for new users, (2) skill building (each extension teaches new concepts — RLS, shared MCP, cross-extension queries), (3) cross-domain integration that would never be designed if extensions were built independently.

## Why People Are Using It
Observed in [OB1 (Open Brain)](https://github.com/NateBJones-Projects/OB1) — see [[ob1-analysis]] for structural details. The learning path is the primary onboarding mechanism. Each extension's README includes a "Learning Path" table showing position, a "What You'll Learn" section listing new concepts, and a "Cross-Extension Integration" section documenting connections.

## Potential Alternatives
- **Flat capability menu** (most agent frameworks): User picks what they want. More flexible but no compound effects.
- **Monolithic system** (deploy everything at once): No adoption path, steep learning curve, no progressive skill building.
- **Capability discovery** (AI suggests next extension based on usage patterns): Adaptive but requires runtime intelligence.

## Potential Improvements
- Branching paths (not just linear) — some users might want CRM before meals
- Usage-based recommendations — "You've been capturing a lot of recipe thoughts, consider Meal Planning next"
- Extension dependency graph — formalize which extensions enhance which (currently documented in READMEs only)

## Potential Failure Modes
- Linear ordering may not match all users' priorities (a job seeker wants Extension 6 first)
- Cross-extension dependencies make individual extensions harder to maintain independently
- Compounding creates coupling — removing one extension may break features in later ones
