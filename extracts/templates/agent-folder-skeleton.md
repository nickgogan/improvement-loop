---
title: "Agent Folder Skeleton"
type: "extracted-artifact"
assigned_form: "template"
source_finding: "agent-as-folder-compiled-to-manifest"
extraction_date: "2026-07-19"
last_change_session: 152
last_change_report: "agent-design-patterns.harvest-queue"
identification_report: null
deployed: false
deployed_to: null
context:
  applies_to:
    - "builders scaffolding a new agent who want capability inclusion to be structural (a file exists in the right place) rather than wired by hand-written imports or a registry entry"
    - "teams standardizing how multiple agents are laid out so any contributor can find where a given capability lives without reading code"
    - "framework or harness builders deciding what folder convention a compile/discovery step should traverse"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "specify"
  reversibility: "trivial — the scaffold produces a directory-layout specification; adopting or abandoning it before implementation has no migration cost. Moving an already-implemented agent onto this layout is a separate, heavier refactor."
  auditability: "high — every primitive category is a named, checkable subfolder; a reviewer can confirm completeness (which categories are populated vs. intentionally empty) by listing the directory, and can confirm correctness by inspecting the compiled manifest against the folder contents"
  evidence_strength: "Medium"
  adoption:
    status: "Not Yet Started"
    notes: "Documented as the core convention of an open-source agent framework (thousands of GitHub stars, active); no adoption in this scaffold's consuming context yet."
contract:
  preconditions: "A build or deploy-time mechanism exists (native to a framework, or purpose-built) that can traverse a folder, discover files by their subfolder location, and resolve them into a single manifest without hand-written imports. The set of primitives the agent needs (instructions, skills, tools, etc.) is at least roughly known before folder creation starts."
  invariants: "Each subfolder maps to exactly one primitive category — nothing is wired in from outside the agent's own folder. The entry-point file never references subfolder contents directly; inclusion is structural (file presence), not declared (an import or registry line). An unused primitive category is either omitted entirely or left empty — never populated with stale or placeholder files that the compile step would pick up. The compiled manifest, not a re-read of the folder tree, is the authoritative record of what is actually wired."
  governance: "Owner: the agent's maintainer or the team responsible for the agent. Adding a new primitive category to the convention itself (not just a new file within an existing category) is a framework-level change, reviewed separately from routine additions within a category."
  recovery: "If an added file's capability doesn't take effect, inspect the compiled manifest before assuming the code is broken — misplacement (wrong subfolder, naming collision) has no compiler-error surface in the base convention and is a likely cause. If the folder and the compiled manifest are suspected to have drifted, run a folder-vs-manifest diff; if no such check exists yet, treat this as a known gap and diff manually on a regular cadence until tooling closes it. If the folder accumulates enough files across categories that navigation degrades, subdivide by sub-responsibility or add an index file summarizing what lives where — the same remedy other folder-as-structure conventions use at scale."
tags:
  - "extracted-artifact"
  - "template"
  - "agent-design"
  - "folder-convention"
  - "declarative-config"
---

# Agent Folder Skeleton

**Source:** [[agent-as-folder-compiled-to-manifest]]
**Form:** template
**Extraction date:** 2026-07-19

A fillable scaffold for laying out an entire agent as one parent folder of named, single-purpose subfolders that a build/deploy-time compile step discovers and resolves into one manifest — with nothing in the agent's entry-point file referencing the pieces it's made of. Complete one scaffold per agent before wiring anything by hand.

## Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `{{AGENT_NAME}}` | Name of the parent agent folder | Yes |
| `{{ENTRY_POINT}}` | Path to the entry-point file (e.g., `agent.ts`) and the model/config it specifies | Yes |
| `{{INSTRUCTIONS}}` | System-prompt / global-rules content or path, or `none` | Yes (declared) |
| `{{SKILLS}}` | List of skill files, each with its trigger description, or `none` | Yes (declared) |
| `{{TOOLS}}` | List of individual tool files/definitions, or `none` | Yes (declared) |
| `{{SANDBOX}}` | Isolated code-execution config, or `none` | Yes (declared) |
| `{{CHANNELS}}` | Integration channels (chat platforms, etc.), or `none` | Yes (declared) |
| `{{CONNECTIONS}}` | External service connections (e.g., protocol servers), or `none` | Yes (declared) |
| `{{SUB_AGENTS}}` | Sub-agent folders dispatched for scoped or token-heavy work, or `none` | Yes (declared) |
| `{{SCHEDULES}}` | Recurring/autonomous run definitions, or `none` | Yes (declared) |
| `{{COMPILE_MECHANISM}}` | How the build/deploy step traverses the folder and produces the manifest | Yes |
| `{{MANIFEST_INSPECT_METHOD}}` | How to view the compiled manifest to debug "why wasn't this picked up" | Yes |
| `{{DRIFT_CHECK_METHOD}}` | How folder-vs-manifest drift is detected, or `none — not yet implemented` | Yes |

## Body

```markdown
# Agent: {{AGENT_NAME}}

**Entry point:** {{ENTRY_POINT}}
**Compile mechanism:** {{COMPILE_MECHANISM}}

## Folder Layout

{{AGENT_NAME}}/
├── agent.ts              # entry point — never imports the folders below directly
├── instructions/         # {{INSTRUCTIONS}}
├── skills/                # {{SKILLS}}
├── tools/                 # {{TOOLS}}
├── sandbox/                # {{SANDBOX}}
├── channels/               # {{CHANNELS}}
├── connections/             # {{CONNECTIONS}}
├── sub-agents/               # {{SUB_AGENTS}}
└── schedules/                 # {{SCHEDULES}}

<!-- Minimum viable agent = entry point only, specifying a model. Every other folder is optional and additive. -->

## Debugging Safeguards

- **Manifest inspection:** {{MANIFEST_INSPECT_METHOD}}
- **Drift check (folder source vs. compiled manifest):** {{DRIFT_CHECK_METHOD}}
```

## Usage

1. **Start from the entry point only.** The minimum viable agent is `{{ENTRY_POINT}}` naming a model — every subfolder is optional and additive from there.
2. **One subfolder per primitive category.** Do not add ad hoc top-level files or mix primitive types inside one folder; the compile step relies on the folder location to know what it's discovering.
3. **Declare emptiness explicitly.** A category with no content is `none`, not silently absent from the record — this scaffold is also the completeness checklist.
4. **Fill in the debugging safeguards before relying on the layout at scale.** The base convention has no compiler-error surface for a misplaced or miscollided file; the manifest-inspect method is how "why wasn't my skill picked up" gets answered without guessing.
5. **Add the drift check once more than a couple of contributors touch the folder.** Without one, folder source and compiled manifest can silently diverge — write `none — not yet implemented` honestly rather than assuming re-reading the folder is equivalent to reading the manifest.

## Variation Axis

What drives different renderings of this scaffold:

- **Framework binding.** A native compiled primitive (the folder convention is the framework's own build step) vs. a convention-only harness bolted onto an existing setup (the compile mechanism must be purpose-built, and the debugging safeguards carry more weight because there is no vendor-provided manifest inspector).
- **Agent complexity.** A minimal single-purpose agent renders with most categories `none`; a production, multi-integration agent populates most or all categories and needs the drift check from day one rather than as an afterthought.
- **Team size.** A solo-maintained agent can tolerate re-reading the folder as a stand-in for the manifest; a multi-contributor agent needs the manifest-inspect and drift-check safeguards actually implemented, not just declared as a future step.

## Contract

### Preconditions
A build or deploy-time mechanism exists (native to a framework, or purpose-built) that can traverse a folder, discover files by their subfolder location, and resolve them into a single manifest without hand-written imports. The set of primitives the agent needs (instructions, skills, tools, etc.) is at least roughly known before folder creation starts.

### Invariants
Each subfolder maps to exactly one primitive category — nothing is wired in from outside the agent's own folder. The entry-point file never references subfolder contents directly; inclusion is structural (file presence), not declared (an import or registry line). An unused primitive category is either omitted entirely or left empty — never populated with stale or placeholder files that the compile step would pick up. The compiled manifest, not a re-read of the folder tree, is the authoritative record of what is actually wired.

### Governance
Owner: the agent's maintainer or the team responsible for the agent. Adding a new primitive category to the convention itself (not just a new file within an existing category) is a framework-level change, reviewed separately from routine additions within a category.

### Recovery
If an added file's capability doesn't take effect, inspect the compiled manifest before assuming the code is broken — misplacement (wrong subfolder, naming collision) has no compiler-error surface in the base convention and is a likely cause. If the folder and the compiled manifest are suspected to have drifted, run a folder-vs-manifest diff; if no such check exists yet, treat this as a known gap and diff manually on a regular cadence until tooling closes it. If the folder accumulates enough files across categories that navigation degrades, subdivide by sub-responsibility or add an index file summarizing what lives where — the same remedy other folder-as-structure conventions use at scale.
