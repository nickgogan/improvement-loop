---
title: "Eager-Prompt Whitelist"
type: "extracted-artifact"
assigned_form: "rule"
source_finding: "disclosure-granularity-decision-rubric"
extraction_date: "2026-07-13"
last_change_session: 146
last_change_report: "agent-design-patterns.harvest-queue"
identification_report: null
deployed: false
deployed_to: null
context:
  applies_to:
    - "agent builders composing the always-loaded portion of a system prompt when on-demand loading is available for the rest"
    - "teams with a growing catalog of skills, tools, or capabilities deciding what earns permanent prompt residency"
    - "reviewers auditing an agent's eager context for bloat before or after deployment"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "specify"
  reversibility: "trivial — demoting content from eager to on-demand is a configuration or prompt edit with no data migration; the content remains reachable"
  auditability: "high — the eager prompt is a single inspectable surface; each block either names one of the four whitelist categories or it does not; lintable as a per-block category check"
  evidence_strength: "Medium (practitioner-documented)"
  adoption:
    status: "Not Yet Started"
    notes: "Shipped as documented doctrine inside a top-tier production agent framework's packaged agent-construction skill; the framework's own first-party capabilities follow it."
contract:
  preconditions: "The agent's context is split into an always-loaded (eager) portion and an on-demand portion, and an on-demand loading mechanism exists (deferred capabilities, skill catalogs, tool search, file references). The builder controls what goes into the eager portion."
  invariants: "Every piece of always-loaded prompt content belongs to one of four categories: identity (who the agent is), task boundaries (what it does and does not do), global safety (constraints that must hold before any loading decision), or routing (what exists and how to reach it). Content outside these categories loads on demand. Eager status is an explicit per-unit decision, never a default."
  governance: "Owner: whoever owns the agent's prompt assembly. Every addition to the eager prompt names its whitelist category at review time; unclassifiable additions are rejected to on-demand. The 'routing' category is policed hardest — it covers pointers to content, not the content itself. Periodic audit re-checks existing eager content, since whitelist creep is gradual."
  recovery: "If eager content fails the category test → demote it to on-demand (a capability body, a skill file, a referenced document) and leave only a routing pointer if one is needed. If safety or routing content was wrongly deferred and the agent acts before loading it → promote it back to eager; the whitelist exists precisely so safety and routing never pay a load round-trip. If the eager prompt has regrown → audit block-by-block against the four categories in one pass rather than trimming opportunistically."
tags:
  - "extracted-artifact"
  - "rule"
  - "context-engineering"
  - "progressive-disclosure"
  - "prompt-engineering"
---

# Eager-Prompt Whitelist

**Source:** [[disclosure-granularity-decision-rubric]]
**Form:** rule
**Extraction date:** 2026-07-13

## Condition

An agent builder is deciding what belongs in the always-loaded (eager) portion of an agent's prompt, and an on-demand loading mechanism is available for everything else — deferred capabilities, a skill catalog, tool search, or file references loaded when needed.

The rule fires on every candidate addition to the eager prompt, and on every audit of existing eager content. It presupposes that eager-vs-deferred is treated as a design question asked per unit of content — never a default.

## Action

**Required:** Admit content to the always-loaded prompt only if it belongs to one of four categories:

1. **Identity** — who the agent is and how it conducts itself.
2. **Task boundaries** — what the agent does and explicitly does not do.
3. **Global safety** — constraints that must hold before any loading decision is made.
4. **Routing** — what exists and how to reach it: catalog descriptions, tool indexes, pointers to on-demand content.

**Forbidden:** Eager-loading anything outside the four categories — procedure bodies, domain reference material, per-capability instructions, examples, or workflow detail. These load on demand. Also forbidden: smuggling content in through the elastic "routing" category — routing admits pointers to content, never the content itself.

## Boundary

Enforced at prompt-assembly design time: wherever the eager prompt is composed (system-prompt authoring, context-file curation, capability `defer_loading` decisions, harness configuration). Every addition to the always-loaded surface passes the category test before it lands; periodic audits re-apply the test to accumulated content.

## Enforcement

- **Mechanism:** Each block of the eager prompt is annotated (or annotatable on review) with exactly one whitelist category. A block that cannot name its category does not qualify.
- **Check (deterministic):** For each eager block: `category(block) ∈ {identity, task-boundaries, global-safety, routing}`. Any block whose honest classification falls outside the enum is a violation. Secondary check on routing blocks: `is_pointer(block) == true` — a routing block that carries the target content inline rather than pointing to it is a violation.
- **Violation response:** Demote the block to the on-demand layer; if it must remain discoverable, replace it with a routing pointer. On repeated whitelist creep, audit the entire eager surface in one pass rather than per-addition.
- **Lint integration:** The category check is mechanically lintable — flag eager content that declares no category or declares "routing" while exceeding pointer size.

## Rationale

Always-loaded content taxes every turn of every session, and eager prompts regrow by default: each addition looks locally justified, and "routing" stretches to cover whatever the author wants resident. A closed positive-space whitelist inverts the burden — content must qualify for eager status rather than being trimmed after the fact — which converts a recurring per-author judgment call into a checkable standard. The four categories are exactly the things that cannot pay a load round-trip: the agent must know who it is, what it does, what is never allowed, and what else exists *before* it can make any on-demand loading decision. Everything downstream of that decision can afford to load on demand.

## Failure Modes

- **Whitelist creep via "routing."** Routing is the elastic category; catalog descriptions balloon into inlined instructions. Mitigation: routing admits pointers, not content — enforce the pointer-size check.
- **Over-deferral of safety.** Applying the whitelist too zealously and deferring a genuinely global constraint means the agent can act before loading it. Mitigation: the whitelist is a floor for eagerness as much as a ceiling — safety and routing are always eager.
- **Category laundering.** Procedure detail rebranded as "task boundaries." Mitigation: boundaries state *what*, never *how*; any block containing steps fails the test.
- **Rubric fossilization.** As models improve at on-demand retrieval, what deserves eager status shrinks; a whitelist without a revision owner drifts stale. Mitigation: assign an owner and re-audit on model or harness upgrades.

## Contract

### Preconditions
The agent's context is split into an always-loaded (eager) portion and an on-demand portion, and an on-demand loading mechanism exists (deferred capabilities, skill catalogs, tool search, file references). The builder controls what goes into the eager portion.

### Invariants
Every piece of always-loaded prompt content belongs to one of four categories: identity (who the agent is), task boundaries (what it does and does not do), global safety (constraints that must hold before any loading decision), or routing (what exists and how to reach it). Content outside these categories loads on demand. Eager status is an explicit per-unit decision, never a default.

### Governance
Owner: whoever owns the agent's prompt assembly. Every addition to the eager prompt names its whitelist category at review time; unclassifiable additions are rejected to on-demand. The "routing" category is policed hardest — it covers pointers to content, not the content itself. Periodic audit re-checks existing eager content, since whitelist creep is gradual.

### Recovery
If eager content fails the category test → demote it to on-demand (a capability body, a skill file, a referenced document) and leave only a routing pointer if one is needed. If safety or routing content was wrongly deferred and the agent acts before loading it → promote it back to eager; the whitelist exists precisely so safety and routing never pay a load round-trip. If the eager prompt has regrown → audit block-by-block against the four categories in one pass rather than trimming opportunistically.
