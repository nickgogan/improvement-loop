---
title: "Composition-Unit Bundle Scaffold"
type: "extracted-artifact"
assigned_form: "template"
source_finding: "capability-as-agent-composition-primitive"
extraction_date: "2026-07-13"
last_change_session: 146
last_change_report: "agent-design-patterns.harvest-queue"
identification_report: null
deployed: false
deployed_to: null
context:
  applies_to:
    - "agent designers packaging one responsibility — its instructions, tools, hooks, guardrails, and model settings — as a single reusable unit"
    - "teams sharing the same capability across multiple agents who need one place to define and evolve it"
    - "framework or harness builders deciding what a composable agent extension must carry beyond a bare tool list"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "specify"
  reversibility: "trivial — the scaffold produces a specification document; discarding or revising it has no migration cost. Refactoring an existing agent onto bundle-based composition is a separate, heavier act."
  auditability: "high — every slot is a named field in one document; a reviewer can check bundle completeness (all five slots addressed), reuse claims (which agents mount it), and disclosure decisions without reading agent code"
  evidence_strength: "Medium (practitioner-documented)"
  adoption:
    status: "Not Yet Started"
    notes: "Shipped as a first-class primitive in a top-tier production agent framework (Pydantic AI 2.0 capabilities); the scaffold generalizes that primitive into a framework-neutral specification document."
contract:
  preconditions: "A responsibility has been identified that is coherent enough to bundle: its tools share instructions, or its behavior needs dedicated hooks/guardrails/settings. The designer knows which agent(s) will mount the bundle and can enumerate the tools it needs. A host framework or harness exists that can attach instructions, tools, hooks, guardrails, and model settings to an agent (natively as one primitive, or by convention across separate mechanisms)."
  invariants: "One bundle covers exactly one responsibility — seams follow responsibilities, not tool vendors or file layout. All five slots (instructions, tools/toolsets, lifecycle hooks, guardrails, model settings) are explicitly addressed; an intentionally empty slot is declared empty, never silently omitted. The bundle is self-contained: it does not assume unstated global agent state (shared memory, mounting order, another bundle's tools) — any such dependency is declared. The disclosure decision (always-loaded vs load-on-demand) is recorded per bundle, not defaulted."
  governance: "Owner: the team or maintainer of the shared bundle, not the agents that mount it. A bundle mounted by more than one agent is a shared dependency — changes are versioned and every mounting agent's owner is notified on change. New bundles are reviewed for responsibility overlap with existing bundles before being added to a catalog; catalog growth is bounded by review, not append-only."
  recovery: "If a bundle quietly depends on global state or another bundle → declare the dependency explicitly or split the bundle; composability claims are void until then. If two bundles' responsibilities are found to overlap → merge them or redraw the seam; do not let both drift. If the catalog grows past what the mounting agent can select between reliably → tighten descriptions, demote rarely-used bundles to on-demand, or split the agent. If a shared bundle change breaks one mounting agent → pin that agent to the prior version and re-review the change."
tags:
  - "extracted-artifact"
  - "template"
  - "agent-design"
  - "composition"
  - "skills"
  - "progressive-disclosure"
---

# Composition-Unit Bundle Scaffold

**Source:** [[capability-as-agent-composition-primitive]]
**Form:** template
**Extraction date:** 2026-07-13

A fillable scaffold for specifying one agent composition unit — a "capability"-style bundle that packages everything one responsibility needs. The unit of reuse is the responsibility, not the tool: an agent definition collapses to *model + list of bundles*, and a bundle moves between agents intact. Complete one scaffold per responsibility before wiring anything into an agent.

## Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `{{BUNDLE_NAME}}` | Canonical name for the composition unit (lowercase-hyphenated) | Yes |
| `{{RESPONSIBILITY}}` | The single responsibility this bundle owns, in one sentence | Yes |
| `{{CATALOG_DESCRIPTION}}` | Brief always-visible description used when the bundle is listed in a catalog for on-demand loading | Yes |
| `{{INSTRUCTIONS}}` | The system-prompt fragment governing this responsibility (inline text or a path reference) | Yes |
| `{{TOOL_N_NAME}}` | Name of tool N carried by the bundle | Yes (≥0, declared) |
| `{{TOOL_N_SOURCE}}` | Where tool N comes from: `native-function`, `tool-server`, `external-api`, `shell`, `other` | Per tool |
| `{{HOOK_N_POINT}}` | Lifecycle point for hook N (e.g., `pre-tool-use`, `post-tool-use`, `on-load`, `on-error`) | Yes (≥0, declared) |
| `{{HOOK_N_BEHAVIOR}}` | What hook N deterministically enforces or injects at that point | Per hook |
| `{{GUARDRAIL_N}}` | Input/output constraint N (validation, refusal condition, schema bound) | Yes (≥0, declared) |
| `{{MODEL_SETTINGS}}` | Model settings this bundle requires or overrides (temperature, max tokens, model tier), or `inherit` | Yes |
| `{{DISCLOSURE}}` | `eager` (instructions always loaded) or `on-demand` (catalog description visible; full instructions loaded when selected) — a decision, not a default | Yes |
| `{{STATE_ASSUMPTIONS}}` | Global agent state, ordering constraints, or other bundles this bundle assumes; `none` if fully self-contained | Yes |
| `{{MOUNTED_BY}}` | Agents currently mounting this bundle | Yes |
| `{{VERSION}}` | Bundle version; bump on any slot change once mounted by more than one agent | Yes |

## Body

```markdown
# Bundle: {{BUNDLE_NAME}} (v{{VERSION}})

**Responsibility:** {{RESPONSIBILITY}}
**Catalog description:** {{CATALOG_DESCRIPTION}}
**Disclosure:** {{DISCLOSURE}}
**Mounted by:** {{MOUNTED_BY}}

## 1. Instructions
{{INSTRUCTIONS}}

## 2. Tools / Toolsets
| Tool | Source | Notes |
|------|--------|-------|
| {{TOOL_1_NAME}} | {{TOOL_1_SOURCE}} | |
<!-- one row per tool; write "none — instructions-only bundle" if empty -->

## 3. Lifecycle Hooks
| Hook point | Behavior |
|-----------|----------|
| {{HOOK_1_POINT}} | {{HOOK_1_BEHAVIOR}} |
<!-- one row per hook; write "none" if empty -->

## 4. Guardrails
- {{GUARDRAIL_1}}
<!-- one line per constraint; write "none" if empty -->

## 5. Model Settings
{{MODEL_SETTINGS}}

## Self-Containment Declaration
State/ordering assumptions: {{STATE_ASSUMPTIONS}}
```

## Usage

1. **One scaffold per responsibility.** If you cannot state `{{RESPONSIBILITY}}` in one sentence, the seam is wrong — split before specifying.
2. **Address all five slots.** Instructions, tools, hooks, guardrails, model settings. Empty is a valid answer; unaddressed is not — silent omissions are where composability breaks later.
3. **Decide disclosure per bundle.** Write `{{CATALOG_DESCRIPTION}}` even for eager bundles; it is what lets the bundle move to on-demand later without redesign, and what keeps large catalogs mountable.
4. **Declare state assumptions honestly.** A bundle that assumes shared memory or mounting order is not portable; declaring the assumption is what makes reuse safe.
5. **Treat shared bundles as dependencies.** Once `{{MOUNTED_BY}}` lists two or more agents, every change is a versioned change: improving the bundle upgrades all of them simultaneously — and so does breaking it.

## Variation Axis

What drives different renderings of this scaffold:

- **Host mechanism.** A typed framework primitive (bundle maps 1:1 to a native capability object) vs a convention-based harness (instructions land in a prompt fragment, tools in a registry, hooks in a hook config — the scaffold is the one document tying them together).
- **Disclosure posture.** Eager bundles (identity-adjacent, always needed) render with full instructions inline; on-demand bundles lean on the catalog description and defer the body.
- **Bundle weight.** Instructions-only bundles (pure doctrine), tool-heavy bundles (thin instructions over a toolset), and hook/guardrail bundles (deterministic enforcement with minimal prompt surface) fill the same slots very differently.
- **Sharing scope.** Single-agent bundles can tolerate looser state assumptions; catalog-published bundles must be fully self-contained and versioned.

## Contract

### Preconditions
A responsibility has been identified that is coherent enough to bundle: its tools share instructions, or its behavior needs dedicated hooks/guardrails/settings. The designer knows which agent(s) will mount the bundle and can enumerate the tools it needs. A host framework or harness exists that can attach instructions, tools, hooks, guardrails, and model settings to an agent (natively as one primitive, or by convention across separate mechanisms).

### Invariants
One bundle covers exactly one responsibility — seams follow responsibilities, not tool vendors or file layout. All five slots (instructions, tools/toolsets, lifecycle hooks, guardrails, model settings) are explicitly addressed; an intentionally empty slot is declared empty, never silently omitted. The bundle is self-contained: it does not assume unstated global agent state (shared memory, mounting order, another bundle's tools) — any such dependency is declared. The disclosure decision (always-loaded vs load-on-demand) is recorded per bundle, not defaulted.

### Governance
Owner: the team or maintainer of the shared bundle, not the agents that mount it. A bundle mounted by more than one agent is a shared dependency — changes are versioned and every mounting agent's owner is notified on change. New bundles are reviewed for responsibility overlap with existing bundles before being added to a catalog; catalog growth is bounded by review, not append-only.

### Recovery
If a bundle quietly depends on global state or another bundle → declare the dependency explicitly or split the bundle; composability claims are void until then. If two bundles' responsibilities are found to overlap → merge them or redraw the seam; do not let both drift. If the catalog grows past what the mounting agent can select between reliably → tighten descriptions, demote rarely-used bundles to on-demand, or split the agent. If a shared bundle change breaks one mounting agent → pin that agent to the prior version and re-review the change.
