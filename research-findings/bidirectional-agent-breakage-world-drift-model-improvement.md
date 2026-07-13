---
name: "Bidirectional Agent Breakage: World Drift and Model Improvement"
summary: |-
  Plain English: agents break in two directions, and most maintenance thinking only
  covers one. They break when the world drifts around them (stale wikis, changed
  processes, redefined dashboard metrics — which agents ingest as truth and turn into
  convincing wrong work), and they break when the model inside them *improves* — a tool
  that helped a weaker model confuses a stronger one; a rule that protected against an
  unreliable model traps a better one; broad access that was harmless for a clumsy
  model lets a strong one take 20 plausible actions in minutes that a human must
  unwind. Software breaking on improvement is a genuinely new maintenance problem;
  harness fitness must be reviewed against both moving parts, on a schedule.
implementation_notes: |-
  P2: the harness-fitness-review half of the pending Nate B Jones gap-check. The
  engine's model-capability-registry periodic refresh half-embodies the
  model-improvement trigger; nothing currently pairs it with a review of whether engine
  rules/skills/tool restrictions written for older models now over- or under-constrain.
  Gap-check next session should ask: on a model upgrade, what re-examines the harness?
category: "Agent Design"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Partially Adopted"
priority: "P2 (Design Required)"
applicability:
  - "IL (registry refresh, rule/skill fitness reviews)"
  - "General"
adopted_in:
  - "Improvement Loop"
sources:
  - "dont-build-more-ai-agents-until-you-watch-this.md"
related_findings:
  - file: "harness-simplification-as-models-improve.md"
    rel: "extends"
  - file: "tool-pruning-as-harness-maintenance.md"
    rel: "same-problem"
  - file: "five-point-agent-health-checklist.md"
    rel: "extended-by"
  - file: "harness-depth-as-maintenance-ownership.md"
    rel: "enables"
proposals: null
date_discovered: "2026-07-13"
last_updated: "2026-07-13"
pipeline_status: "raw"
consumed_by: []
---

# Bidirectional Agent Breakage: World Drift and Model Improvement

## What It Is

A failure-mode model for deployed agents, framed via Stewart Brand's *Maintenance of
Everything*: agents are sailboats, not apps — they live in motion, with the model
changing inside them and the world changing around them.

**Direction 1 — world drift.** Every organization already has drift (stale wikis, CRM
fields whose meaning shifted, dashboards still saying "activation" after the definition
changed, SOPs describing last quarter's process). With normal software this is
annoying; with agents it is dangerous, because agents *produce work* from the mess —
they summarize, recommend, draft, route, and act on stale truth, and the output looks
convincing. "The agent did its job." It doesn't fail loudly; it keeps working and
starts to haunt the business.

**Direction 2 — model improvement.** Concrete cases from the source (dated Nov-Mar of
the covered period): a careful harness built for an unreliable model — strict tools,
narrow prompt, "only summarize, don't infer" — becomes wrong when the model can
suddenly compare sources, distinguish weak signals from real patterns, and draft useful
next steps: the agent is now underused. Or the mirror image: broad access granted
because a clumsy model's mistakes were human-caught becomes hazardous when a strong
model takes twenty organized, plausible actions in minutes. "We are used to software
breaking when it gets worse. Agents can also break when the model gets better."

Maintenance is defined as keeping the harness fit *between* the two moving things.

## Why It Matters

It extends the KB's harness-simplification finding (remove scaffolding as models
improve) into a full two-sided review obligation: simplification handles the
over-restriction side, but world drift requires the opposite discipline (refreshing
sources and definitions), and both need a trigger — a scheduled fitness review, not
incident response. For any system that pins behavior to model-era assumptions (rules,
tool allowlists, subagent budgets), a model upgrade is a maintenance event, not a free
upgrade.

## Why People Are Using It

Jones grounds it in the Vercel SDR-agent case (production) and frames it as "the real
agent story of 2026": not whether you can build an agent, but whether you can keep the
setup around it healthy as the work and the model change.

## Potential Improvements

- Formalize the two triggers: model-release-triggered harness review and
  cadence-triggered source-currency review, as distinct checklists.
- Pair every restriction/permission with the model assumption that justified it, so
  reviews can test assumptions rather than re-derive them.

## Potential Failure Modes

- Review theater: fitness reviews that re-approve the status quo without testing either
  drift direction.
- Over-rotation on model improvement — removing guardrails on release-day faith rather
  than evidence (the premature-simplification risk already flagged in the KB).
- The silent version is the killer: an agent that keeps producing plausible output
  gives no failure signal to trigger any review at all.
