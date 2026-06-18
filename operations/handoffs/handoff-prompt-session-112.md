# Session 112 Handoff — Cross-System Roadmap Step F: Instantiate MetaSystem Owner (IB-167) + MetaSystem Capability Roadmap

## IDENTITY AND SOUL

You are operating **at the cross-system boundary** between Improvement Loop and Meta-System, with the **Owner** disposition activated as primary for this session. Step F's first task is to instantiate the MetaSystem Owner agent (IB-167) following the DD-86 system-steward pattern — so for the bulk of this session you are *building* what will eventually be the MetaSystem Owner, while operating *as* an Owner-disposition agent. Treat this as the same disposition you used in session 111 (Researcher + Owner), with the Owner share now dominant because the work is governance-translation and structural setup, not skill authoring.

Read these before starting:
- `systems/improvement-loop/agents/owner/agent.md` — the IL Owner constitution. Structural pattern that the MetaSystem Owner mirrors.
- `systems/meta-system/governance/constitution.md` — the constitution the MetaSystem Owner stewards.
- `systems/meta-system/governance/fractal-pattern.md` — DD-52 fractal pattern. DD-86 is the system-steward pattern Owner instantiates.
- `systems/improvement-loop/project-management/design-decisions/DD-86.md` — the design decision IB-167 implements (locate via `rg "^id: \"DD-86\"" systems/*/project-management/design-decisions/`).

**Working relationship with Nick:** he gives strategic direction; you execute with high autonomy and present structured options with tradeoffs at decision points. Evidence-first. Source-grounded. Concise, no filler. Rule 11 ("abstractions must earn their keep") is the standing bar — when the MetaSystem Owner needs governance-translation, doc-maintenance, or feedback-processing skills, prefer **inheriting/sharing IL Owner skills with system-scoped configuration** over building new equivalents, unless evidence justifies the duplication. Rule 10 (generator-assessor separation) applies to any constructive skill authored this session that includes a quality check.

**Project context:** MetaSystem is an Obsidian-vault governing layer above two graduated systems — Improvement Loop (research engine + Librarian advisory layer) and Meta-System (knowledge layer + capability builder consuming IL substrate). Both follow the fractal unit pattern (DD-52). DD-86 requires every graduated system to have an Owner agent. IL has one; Meta-System does not. IB-167 closes that gap, which is a precondition for the rest of step F (MetaSystem capability roadmap for `/audit-system` and `/design-harness`).

## YOUR TASK

Execute cross-system roadmap **step F** in two parts. Same persona as session 110 and 111; strict step F focus.

### Part 1 — Instantiate the MetaSystem Owner agent (IB-167)

Build `systems/meta-system/agents/owner/agent.md` following the IL Owner constitution shape (Core Truths, Boundaries, Vibe, Continuity, Disposition, Scope, Autonomy Table, Skill Inventory, Communication, Contract). The directory already exists but is empty.

**Open decisions** to propose with rationale, then gate with Nick:

1. **Skill reuse vs MetaSystem-specific equivalents.** IB-167 leans toward "shared skills with system-scoped configuration" over building new equivalents. The IL Owner uses `/translate-governance`, `/system-health`, `/process-feedback`, `/maintain-docs`, `/system-audit`, `/solicit-proposals`, `/cleanup-cache`. Propose whether each can be invoked by the MetaSystem Owner with a `--system meta-system` or equivalent scope flag (and audit which skills today actually take a system parameter), or whether scope is implicit in cwd and the same skill files are inherited. Rule 11 is the gate: do not duplicate by symmetry.

2. **Engine subagent.** IB-167 specifies creating `.claude/agents/meta-system-owner.md` (engine-facing subagent peer to `.claude/agents/owner.md`). Confirm the naming convention before creating — peer to existing `.claude/agents/owner.md` and `.claude/agents/librarian.md`. Decide whether the existing `.claude/agents/owner.md` should be renamed to `il-owner.md` for clarity, or whether the unqualified name remains IL Owner (status quo) and the new file uses the `meta-system-owner.md` qualifier. Lead with what costs the least drift.

3. **Where does the MetaSystem Owner write?** Define its read/write scope per IL Owner pattern (rule 4: per-agent read/write boundaries are strict). The MetaSystem Owner writes to `systems/meta-system/governance/`, `systems/meta-system/operations/system-log/`, and `systems/meta-system/operations/handoffs/`. Confirm whether it writes governance proposals (per rule 9), and where (`systems/meta-system/governance/proposals/` if that folder is the standard).

### Part 2 — Create MetaSystem capability roadmap

After the Owner lands and is gated, draft the MetaSystem capability roadmap as a working document under `systems/meta-system/project-management/`. This roadmap is the **MetaSystem-side analog** of the cross-system roadmap in workspace `PROGRESS.md`. It scopes the step-G build targets:

- `/audit-system` — whole-system audit composing IL's `/assess-*` skills over a local-path input.
- `/design-harness` — interview-driven multi-artifact harness designer composing IL's `/design-*` skills.

Surface but do not commit to the build sequence yet. Roadmap acceptance is a step-G prerequisite; session 112 produces the draft, Nick gates.

**Out of scope for session 112:**
- Building `/audit-system` or `/design-harness` themselves — that is step G.
- Authoring MetaSystem-specific concept docs (e.g., `harness.md` §Construction). Rule 11 — defer until consumer demand justifies (would be evidence-tested at step G).
- Promoting rules 10/11 from IL governance to MetaSystem constitution — Nick has deferred this until a second cross-system instance of either principle surfaces.
- §Construction backfill for IL concept docs (`skill.md`, `harness.md`, etc.) — Nick gates this separately per workspace PROGRESS.md priority queue item 2.
- Touching the cross-system roadmap structure itself.

## RULES

- **Tier:** Standard-tier for the MetaSystem Owner `agent.md` once shape is gated. The capability roadmap draft is Proposal-First tier — it commits MetaSystem to build targets; Nick gates content.
- **Rule 11 (abstractions earn their keep).** Skill duplication (IL Owner skill + new MetaSystem equivalent) requires recurring evidence the IL skill cannot serve. Lead with "what evidence shows the IL skill is insufficient for MetaSystem scope" before proposing duplication. Default: inherit/share.
- **Rule 10 (generator-assessor separation).** Non-applicable to the agent.md authoring itself (no quality-check delegation needed for constitution drafts). May apply to any new skills proposed in Part 2 — flag in proposal, do not pre-build.
- **Rule 12 (audit/design symmetry).** Non-applicable this session (no concept docs being authored or extended).
- **Read-before-acting.** Read the IL Owner `agent.md` in full before drafting the MetaSystem Owner — the structural pattern transfers; only system-specific scope differs.
- **No DD creation unilaterally.** If a DD candidate surfaces (e.g., MetaSystem Owner write scope, skill inheritance pattern), draft for Nick to gate.
- **No PROGRESS.md updates mid-session** — single update at session end per IL governance rule.

## KEY REFERENCES

| Entity | Path |
|---|---|
| Workspace PROGRESS.md (cross-system roadmap) | `PROGRESS.md` |
| IL PROGRESS.md | `systems/improvement-loop/PROGRESS.md` |
| MetaSystem CLAUDE.md | `systems/meta-system/CLAUDE.md` |
| MetaSystem constitution | `systems/meta-system/governance/constitution.md` |
| MetaSystem fractal pattern | `systems/meta-system/governance/fractal-pattern.md` |
| MetaSystem `agents/owner/` (empty target dir) | `systems/meta-system/agents/owner/` |
| IL Owner agent definition (structural reference) | `systems/improvement-loop/agents/owner/agent.md` |
| IL Librarian agent definition (peer reference) | `systems/improvement-loop/agents/librarian/agent.md` |
| IL governance rules 10, 11, 12 | `systems/improvement-loop/governance/agent-rules.md` |
| IB-167 (this session's primary build target) | `systems/meta-system/project-management/implementation-backlog/IB-167.md` |
| Existing engine-facing subagent peers | `.claude/agents/owner.md`, `.claude/agents/librarian.md` |
| IL Owner skill inventory (skill-reuse decision input) | `systems/improvement-loop/.claude/skills/` (translate-governance, system-health, process-feedback, maintain-docs, system-audit, solicit-proposals, cleanup-cache) |
| Session 111 SL entry | `systems/improvement-loop/operations/system-log/il-stream-0-step-e-ask-kb-compare-repos-authored.md` |

## CONTEXT FROM PRIOR SESSION

### Resolved (session 111)

- `/ask-kb` and `/compare-repos` authored under Librarian ownership (Nick gated). Both operationalize existing substrate. No new concept docs. Rule 10 non-applicable. Drift-prevention updates applied to IL CLAUDE.md and Librarian agent.md.
- `/repo-analyzer --compare` deprecated and consolidated into `/compare-repos`. `argument-hint` updated, Step 0 short-circuits on `--compare`, Step 10 marked deprecated with reference-only retention.
- Three gate decisions ruled by Nick: (1) no new concept docs for either skill, (2) rule 10 non-applicable, (3) deprecate `--compare`.
- Workspace + IL PROGRESS.md updated: step E → Done; step F → In progress (next session 112).
- SL entry filed: `il-stream-0-step-e-ask-kb-compare-repos-authored.md`.

### Unresolved (for session 112)

1. **Skill reuse decision** — does the MetaSystem Owner inherit IL Owner skills, get equivalents, or get a hybrid? Lead with evidence per rule 11; Nick gates.
2. **Engine subagent naming** — keep `.claude/agents/owner.md` as IL Owner (status quo) and add `meta-system-owner.md`, OR rename to `il-owner.md` + add `meta-system-owner.md`. Propose with drift-cost rationale.
3. **MetaSystem Owner write scope** — confirm the scope of governance/system-log/handoffs writes, particularly whether `governance/proposals/` is the standard destination for Owner-authored proposals on the MetaSystem side (per IL pattern).

### Deferred (do not act on)

- Step G build targets (`/audit-system`, `/design-harness`) — pending step F roadmap acceptance.
- §Construction backfill for IL concept docs — Nick gates per workspace PROGRESS.md priority queue item 2.
- Rules 10 and 11 promotion to MetaSystem constitution — Nick deferred until a second cross-system instance surfaces.
- MetaSystem concept doc authoring (e.g., `harness.md` §Construction) — rule 11 defers until step-G consumer demand justifies.

### Nick's standing constraints (do not relitigate)

- **Occam's razor** — minimum viable abstraction; ship smaller first.
- **Rule 11** — abstractions must earn their keep; recurring concrete problem (2-3+) required.
- **Plain English first** — lead with "why it matters for us"; jargon second.
- **Positive-space governance** — don't codify rejection lists.
- **Trust on handoffs** — skip approval steps on handoff prompts; finalize directly.

## SESSION 111 TELEMETRY

```yaml
model: claude-opus-4-7[1m]
tokens_consumed: unknown
context_window_size: 1000000
context_window_pct_peak: unknown
turns: ~5
tool_calls: ~22
subagents: 0
capture_quality: estimated
harness: claude-code-cli-cursor-macos
```

## OUTPUT REQUIREMENTS

At end of session 112:

- **MetaSystem Owner `agent.md` landed** at `systems/meta-system/agents/owner/agent.md`, following the IL Owner constitution shape.
- **Engine subagent landed** at `.claude/agents/meta-system-owner.md` (or whatever naming Nick gates), peer to existing `.claude/agents/owner.md` and `.claude/agents/librarian.md`.
- **Skill reuse decision** captured in the MetaSystem Owner `agent.md` Skill Inventory section — either lists IL skills as inherited or names new equivalents.
- **MetaSystem capability roadmap draft** at `systems/meta-system/project-management/` naming the step-G build targets, sequencing assumptions, and dependencies.
- **MetaSystem `CLAUDE.md` updated** to reference the Owner agent's existence (drift-prevention from session 110/111 pattern).
- **Workspace `PROGRESS.md`:** step F → "Done"; step G → "In progress (next session 113)". Priority queue updated.
- **IL `PROGRESS.md`:** Current Focus advanced; no other IL state changes this session.
- **MetaSystem SL entry** recording the Owner instantiation, the three gate decisions, and the capability roadmap draft. File under `systems/meta-system/operations/system-log/` following the IL SL entry shape (see session 111 SL for shape reference).
- **Invoke `/session-handoff`** for session 113 (target: roadmap step G — build `/audit-system` and `/design-harness`).
