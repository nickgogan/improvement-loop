# FOUNDATIONS — the engine's spine

> **GENERATED — do not edit by hand.** This file is a derived view, rebuilt from DD
> frontmatter by `operations/kb-maintenance-scripts/generate_foundations.py`. To change
> what appears here, set `foundational: true` (or remove it) on the DD itself, then
> regenerate. A pre-commit check fails if this file drifts from the DD flags.
>
> **The DD files are canonical.** If this map and a DD ever disagree, the DD wins.

The load-bearing decisions that define what this system *is* and how it works — read
these first to orient, out of the full DD corpus. Each row links to the canonical DD.
To see the complete set, filter DD frontmatter (`rg -l 'foundational: true'`).

## What earns a `foundational: true` flag (DD-115)

**Litmus test:** if someone had *not* read this DD, would they get the system's
identity, architecture, governance, or core operating model wrong — or just make a
*local, procedural* mistake? Foundational = the former. Orientation, not importance.

**Include** if it fills one role (and shows ≥2 corroborating signals — cited in
CHARTER/CLAUDE/rules, high inbound DD-reference count, scope ∈ Principle/Structure/
Infrastructure/Governance):
- **C1 Identity & architecture** — what the system is / its top-level shape.
- **C2 Non-negotiable governance constraint** — a rule binding every session.
- **C3 Primary actors & interaction model** — who/what does the work.
- **C4 Core value flow** — the pipeline the system exists to run.
- **C5 Load-bearing substrate / ownership boundary** — infra everything sits on; who owns what.

**Exclude** even if Binding + important:
- **X1** procedural "how one part works" (needed only when touching that part)
- **X2** data-integrity / format rule (hit when *writing data*, not *understanding the system*)
- **X3** narrow component/feature addition (one dimension/skill/field/pathway)
- **X4** tuning / threshold change
- **X5** superseded (auto-dropped by the `status == Binding` filter)

**Meta-guard:** the spine's value is being small. Cap ~15–20. A new flag must clear the
bar cleanly **or displace the weakest current member** — it is not additive-by-default.
Past ~20, the test has gone loose; re-tighten rather than expand.


| DD | Title | Category | Canonical file |
|----|-------|----------|----------------|
| DD-29 | Human gate at every stage boundary | Principle | `systems/improvement-loop/project-management/design-decisions/DD-29.md` |
| DD-36 | Periodic research drives system evolution | Principle | `systems/improvement-loop/project-management/design-decisions/DD-36.md` |
| DD-37 | Five foundational design philosophy principles | Principle | `systems/improvement-loop/project-management/design-decisions/DD-37.md` |
| DD-41 | Research KB is IL-owned operational data | Structure | `systems/improvement-loop/project-management/design-decisions/DD-41.md` |
| DD-44 | DD lifecycle: Binding, Proposed, Superseded | Principle | `systems/improvement-loop/project-management/design-decisions/DD-44.md` |
| DD-47 | Three-peer workspace directory organization | Structure | `systems/improvement-loop/project-management/design-decisions/DD-47.md` |
| DD-52 | Seven-folder fractal unit structure | Structure | `systems/improvement-loop/project-management/design-decisions/DD-52.md` |
| DD-53 | Agents as primary work interface | Principle | `systems/improvement-loop/project-management/design-decisions/DD-53.md` |
| DD-54 | Single Obsidian vault with YAML frontmatter | Structure | `systems/improvement-loop/project-management/design-decisions/DD-54.md` |
| DD-55 | DDs distributed to system-scoped folders | Structure | `systems/improvement-loop/project-management/design-decisions/DD-55.md` |
| DD-56 | IB items distributed to system-scoped folders | Structure | `systems/improvement-loop/project-management/design-decisions/DD-56.md` |
| DD-59 | System log distributed to system-scoped folders | Structure | `systems/improvement-loop/project-management/design-decisions/DD-59.md` |
| DD-80 | Direct extraction replaces proposer stage | Flow | `systems/improvement-loop/project-management/design-decisions/DD-80.md` |
| DD-82 | Four-agent system with file-mediated handoffs | Component | `systems/improvement-loop/project-management/design-decisions/DD-82.md` |
| DD-84 | Private monorepo with subtree publishing | Infrastructure | `systems/improvement-loop/project-management/design-decisions/DD-84.md` |
| DD-86 | Owner agent as system steward default | Component | `systems/improvement-loop/project-management/design-decisions/DD-86.md` |
| DD-103 | Architecture reset: collapse the federation into one self-evolving engine | Structure | `systems/improvement-loop/project-management/design-decisions/DD-103.md` |
| DD-104 | Single-engine, three-altitude architecture | Structure | `systems/improvement-loop/project-management/design-decisions/DD-104.md` |
| DD-105 | The charter: a root-level vision doc with explicit trajectory signals | Principle | `systems/improvement-loop/project-management/design-decisions/DD-105.md` |
| DD-108 | Owner autonomy: files DDs as mechanics; Nick gates decision content | Governance | `systems/improvement-loop/project-management/design-decisions/DD-108.md` |

_Spine: 20 foundational DDs._
