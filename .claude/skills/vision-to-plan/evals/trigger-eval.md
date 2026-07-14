# Trigger eval — ops-vision-to-plan

Distilled install-acceptance set (meta-skill-author §2.1/§6). Self-administer after
install: pose each query in a fresh context, record whether this skill activates,
compare against the expected verdict. Triggering is non-deterministic — re-run any
mismatch 3×; a persistent mismatch is a triggering-conformance failure (fix by
adapting the port's description via its platform profile, never by editing queries
to match observed behavior).

Generic by construction: phrasings are specific-but-fictional; no real user or
workspace facts. Verdicts: **trigger** (this skill must activate) · **abstain**
(it must not). Routing notes name the skill that should serve the query when the
receiving host has it installed.

## Should trigger (10)

| # | Query | Expected | Note |
|---|-------|----------|------|
| 1 | "I have an idea for a meal-planning app — help me turn it into a real plan" | trigger | rough vision → plan, casual |
| 2 | "Create a PRD for the notifications overhaul" | trigger | canonical trigger phrase |
| 3 | "Let's capture the vision for this side project before we write any code" | trigger | vision-capture vocabulary |
| 4 | "Write the architecture doc for the sync service" | trigger | architecture-doc deliverable |
| 5 | "Turn this rough idea into a roadmap with milestones" | trigger | idea → roadmap |
| 6 | "I want to plan out the billing subsystem properly — goals, epics, the works" | trigger | subsystem planning, natural vocabulary |
| 7 | "We keep building without direction — let's define what this product actually is" | trigger | intent elicitation, no PM jargon |
| 8 | "Draft a product brief for the tutoring-marketplace idea" | trigger | brief stage |
| 9 | "Break this PRD into epics we can execute" | trigger | PRD → epics stage |
| 10 | "I need to pitch this internally — help me structure the intent and scope first" | trigger | deliverable-motivated, structure ask |

## Should not trigger (10)

| # | Query | Expected | Note |
|---|-------|----------|------|
| 11 | "Let's create a detailed execution plan for the current milestone" | abstain | milestone *execution* planning is not vision→plan — observed real miss shape; served by the harness's plan mode / no owning skill |
| 12 | "What's on the roadmap right now?" | abstain | status read |
| 13 | "Do a handoff — note the plan for next session" | abstain | routes to ops-session-handoff where installed |
| 14 | "Author a SKILL.md for the release process" | abstain | routes to meta-skill-author where installed |
| 15 | "Update the architecture doc's diagram to match the new folder layout" | abstain | mechanical doc edit, no elicitation |
| 16 | "Plan my week" | abstain | trivial, base model handles |
| 17 | "Estimate how long the migration will take" | abstain | estimation, not intent capture |
| 18 | "Write user stories for this sprint in the ticket tracker" | abstain | sprint tooling artifact, different layer |
| 19 | "Review this PRD someone else wrote and give feedback" | abstain | review, not Socratic authoring |
| 20 | "What framework should I use for the frontend?" | abstain | tech Q&A |
