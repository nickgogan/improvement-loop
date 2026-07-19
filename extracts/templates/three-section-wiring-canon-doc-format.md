---
title: "Three-Section Wiring-Canon Doc Format"
type: "extracted-artifact"
assigned_form: "template"
source_finding: "wiring-canon-abstract-then-adapt-doc-structure"
extraction_date: "2026-07-19"
last_change_session: 152
last_change_report: "building-agentic-systems.harvest-queue"
identification_report: "building-agentic-systems.harvest-queue.md::wiring-canon-abstract-then-adapt-doc-structure::template::three-section-wiring-canon-doc-format"
deployed: false
deployed_to: null
context:
  applies_to:
    - "teams documenting the harness-integration layer of a multi-file agentic system that may need to run on more than one host"
    - "authors deciding how to phrase an install requirement so it stays true when the underlying platform mechanism changes"
    - "maintainers designing a change-review process that keeps platform-specific detail from silently hardening into a hidden requirement"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "specify"
  reversibility: "low — reverting from the canon/adapter/example structure back to single platform-shaped docs means manually re-merging content that is now split across sections; nothing is lost, but the split must be undone by hand"
  auditability: "high — a doc that mixes harness-specific content into its Canon or Adapter-delegated sections, or a folder missing its router-guard header, is a checkable structural violation rather than a judgment call"
  evidence_strength: "Medium"
  adoption:
    status: "Not Yet Started"
    notes: "Documented as the wiring-canon documentation architecture in one production agentic system's install layer; not yet adopted elsewhere."
contract:
  preconditions: "A harness-integration concern (or a small numbered set of them) has been identified for a system that installs, or may in the future install, onto more than one platform or host. Someone can state, per concern, what must hold on any platform (the requirement) versus what varies by platform (the mechanism)."
  invariants: "Each wiring-canon doc has exactly three sections, in order: Canon (the platform-agnostic requirement), Adapter-delegated (per-platform mechanism decisions, including the named fallback when a platform lacks the mechanism), and Harness-specific examples (illustrations from the current install, explicitly labeled with which harness they came from, never treated as requirements). The folder containing the canon docs opens with a router-guard document telling any agent operating in the live workspace that this folder is not its entry point, and enumerating the legitimate reasons to read it anyway (generalizing, adapting, receiving, auditing). Canon-side content changes only through a gated regeneration path triggered when the system itself changes; adapter-side content changes through a dated survey-then-diff-then-gated-plan path triggered when a platform changes. An adapter-side finding implying the canon itself is wrong is flagged and routed to the canon-side change path — never patched locally inside the adapter section."
  governance: "Owner: whoever maintains the system's harness-wiring documentation; governance-tier classification is recommended given edits change what a receiving platform is required to provide. Canon-side edits require the gated regeneration flow of the owning process; adapter-side edits require the survey-diff-plan flow. Neither side hand-edits past its own boundary — an adapter never rewrites canon text, and canon regeneration never silently absorbs one adapter's local wording as if it were universal."
  recovery: "If harness-specific content is found under the Canon or Adapter-delegated heading (an example smuggled in as a requirement): move it to Harness-specific examples and re-verify the requirement still holds without it. If an adapter-side survey finds the canon no longer matches reality: do not patch the adapter section to compensate — flag it and route to the canon-side gated regeneration instead. If the router-guard header is missing or stale: add or update it before treating the folder as install-ready documentation; its absence risks install-time docs leaking into live runtime context. If the canon and any artifacts derived from it (e.g. a system-contract wiring row, a file-hash manifest) disagree: treat the divergence as a signal that a regeneration was skipped, and reconcile before trusting either artifact."
tags:
  - "extracted-artifact"
  - "template"
  - "system-contract"
  - "doc-architecture"
  - "portability"
---

# Three-Section Wiring-Canon Doc Format

**Source:** [[wiring-canon-abstract-then-adapt-doc-structure]]
**Form:** template
**Extraction date:** 2026-07-19

A fixed three-section scaffold for documenting a single harness-integration concern platform-agnostically, plus a folder-level router guard that keeps the whole canon set out of live runtime context. One doc per concern (entry point, rule injection, memory scope, registry, and similar); the essential/incidental split is made explicit at authoring time by which section a sentence lands in, rather than discovered later when a second platform forces a rewrite.

## Variables

| Variable | Type | Description |
|----------|------|-------------|
| `{{DOC_NUMBER}}` | integer | Stable ordinal for this canon doc within the numbered wiring set. |
| `{{CONCERN_NAME}}` | identifier | Short stable name for the harness-integration concern this doc covers. |
| `{{CANON_STATEMENT}}` | string | The requirement, phrased so it holds on any platform — a guarantee, not a mechanism. |
| `{{ADAPTER_DECISION_N}}` | string | One per-platform mechanism decision (which mechanism, which paths, whether native enforcement can replace prose). |
| `{{ADAPTER_FALLBACK}}` | string | The named fallback a platform uses when it lacks the native mechanism for this concern. |
| `{{EXAMPLE_N}}` | string | One illustration from the current install, explicitly tagged with its source harness. |
| `{{EXAMPLE_N_HARNESS}}` | identifier | Which harness `{{EXAMPLE_N}}` was drawn from (e.g. `vscode-copilot`, `claude-code`). |
| `{{ROUTER_GUARD_TEXT}}` | string | The folder-level statement that this canon set is not a live-session entry point, plus the enumerated legitimate reasons to read it. |

## Body

```markdown
<!-- Folder-level file, e.g. AGENTS.md or README.md at the canon folder root -->
# Wiring Canon — Router Guard

{{ROUTER_GUARD_TEXT}}

This folder is install-time documentation, not a live cold-start entry point.
Legitimate reasons to read it: generalizing to a new platform, adapting an
existing install, receiving/installing this system, auditing wiring drift.
If you are a live-session agent looking for your own instructions, this is
not it — return to the live cold-start chain.

---

<!-- One doc per wiring concern -->
# {{DOC_NUMBER}}. {{CONCERN_NAME}}

## Canon
{{CANON_STATEMENT}}

## Adapter-delegated
- {{ADAPTER_DECISION_1}}
- {{ADAPTER_DECISION_2}}
<!-- one line per platform decision; always include the fallback -->
- **Fallback when unsupported:** {{ADAPTER_FALLBACK}}

## Harness-specific examples
<!-- harness-specific: {{EXAMPLE_1_HARNESS}} — illustration, never a requirement -->
{{EXAMPLE_1}}

<!-- Repeat one full doc block per numbered wiring concern. -->
```

## Usage

Write the Canon section first, and write it as if no specific platform existed yet — if a sentence names a file path, a config key, or a product name, it belongs in Adapter-delegated or Harness-specific examples instead. Fill Adapter-delegated with the current platform's actual decisions plus its fallback, even when only one platform exists today — this is what makes the doc reusable the day a second platform shows up. Tag every entry in Harness-specific examples with its source harness explicitly; an unlabeled example is indistinguishable from a requirement to a future reader and will eventually be copied as one. Place the router-guard document at the folder's entry point before treating the canon set as complete — a canon folder without it risks its install-time content leaking into a live agent's runtime context.

When the system itself changes, regenerate canon docs through the owning gated process rather than hand-editing; when a platform changes, run a dated survey, diff it against the current Adapter-delegated section, and route the resulting plan through the same gate. If a platform survey turns up something that contradicts the Canon section itself, do not resolve it inside the adapter doc — flag it and route it back to the canon-change path.

## Variation Axis

- **Number of live adapters.** With exactly one platform, Adapter-delegated has one entry and the abstraction earns less of its keep; the format still pays off the moment a second platform is real. For a genuinely single-harness system with no near-term second platform, this format is a layer without a second consumer — weigh it against the abstractions-earn-their-keep test before adopting.
- **Gating strictness.** A tightly gated regeneration process (diff → propose → human-approve) keeps canon trustworthy but adds latency to every change; a looser process risks the canon quietly drifting from live wiring, which is exactly what a companion hash-manifest or drift check exists to catch.
- **Derivation depth.** Some deployments treat the canon doc as the sole artifact; others derive a machine-readable wiring row (or an entire system contract) from each canon doc. The deeper the derivation chain, the more artifacts must be kept in agreement, and the more valuable an automated drift check between them becomes.

## Contract

### Preconditions
A harness-integration concern (or a small numbered set of them) has been identified for a system that installs, or may in the future install, onto more than one platform or host. Someone can state, per concern, what must hold on any platform (the requirement) versus what varies by platform (the mechanism).

### Invariants
Each wiring-canon doc has exactly three sections, in order: Canon (the platform-agnostic requirement), Adapter-delegated (per-platform mechanism decisions, including the named fallback when a platform lacks the mechanism), and Harness-specific examples (illustrations from the current install, explicitly labeled with which harness they came from, never treated as requirements). The folder containing the canon docs opens with a router-guard document telling any agent operating in the live workspace that this folder is not its entry point, and enumerating the legitimate reasons to read it anyway (generalizing, adapting, receiving, auditing). Canon-side content changes only through a gated regeneration path triggered when the system itself changes; adapter-side content changes through a dated survey-then-diff-then-gated-plan path triggered when a platform changes. An adapter-side finding implying the canon itself is wrong is flagged and routed to the canon-side change path — never patched locally inside the adapter section.

### Governance
Owner: whoever maintains the system's harness-wiring documentation; governance-tier classification is recommended given edits change what a receiving platform is required to provide. Canon-side edits require the gated regeneration flow of the owning process; adapter-side edits require the survey-diff-plan flow. Neither side hand-edits past its own boundary — an adapter never rewrites canon text, and canon regeneration never silently absorbs one adapter's local wording as if it were universal.

### Recovery
If harness-specific content is found under the Canon or Adapter-delegated heading (an example smuggled in as a requirement): move it to Harness-specific examples and re-verify the requirement still holds without it. If an adapter-side survey finds the canon no longer matches reality: do not patch the adapter section to compensate — flag it and route to the canon-side gated regeneration instead. If the router-guard header is missing or stale: add or update it before treating the folder as install-ready documentation; its absence risks install-time docs leaking into live runtime context. If the canon and any artifacts derived from it (e.g. a system-contract wiring row, a file-hash manifest) disagree: treat the divergence as a signal that a regeneration was skipped, and reconcile before trusting either artifact.
