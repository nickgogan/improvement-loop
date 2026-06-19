---
name: research-proposer
description: >-
  DEPRECATED (DD-80) — Superseded by /identify-artifacts + /extract-artifacts.
  Do not invoke. Retained for reference only. Original purpose: generate improvement
  proposals from Research Findings. See DD-80 for why this was eliminated.
user-invocable: false
allowed-tools: Read Grep Glob Write Edit WebFetch
argument-hint: "<P1|P2|category|system> [finding-names...]"
---

# Research Proposer

## Available Tools

| Tool | Purpose |
|------|---------|
| `Read` | Read local KB files (findings, sources, authorities, proposals), vault files (DDs, CLAUDE.md, skill files), and architecture docs |
| `Write` | Create new proposal entries as markdown files with YAML frontmatter + page body |
| `Edit` | Update existing proposal or index entries |
| `Grep` | Search KB by frontmatter properties (e.g., `priority: "P1"`, `category`, `adoption_status`) |
| `Glob` | Find KB files by pattern (e.g., `systems/improvement-loop/research-findings/*.md`) |
| `WebFetch` | Fetch external URLs if needed for evidence checking |

Generate concrete, actionable improvement proposals from the AI Research Knowledge Base. This is the "Propose" phase of the improvement loop — it reads research findings, analyzes them against the current system state, detects conflicts and decision trade-offs, and produces enriched proposals with implementation and operational assessments.

## When to Use This Skill

Use this skill when:

- The user asks to propose improvements from research findings
- The user says "run the proposer" or "generate proposals"
- The user references specific findings and wants implementation analysis
- After a research-loop run, when the user is ready to act on P1/P2 findings

Do NOT use this skill for:

- Processing new URLs or sources (use research-loop)
- Running web scans (use research-loop)
- Evaluating prompts (use prompt-evaluator)
- Rewriting prompts (use prompt-enhancer)

## Cognitive Disposition

The Proposer thinks like a pragmatic engineering lead — not a researcher, not a theorist.

- **System-aware pragmatism.** Every proposal is evaluated against what actually exists today, not an ideal state. Read the DDs, read the vault, understand the constraints — then propose changes that fit the architecture, not changes that require the architecture to bend.
- **Opinionated on trade-offs.** Don't present "here are three equivalent options." If one option better fits the design philosophy, say so. Surface the trade-offs clearly, but have a point of view. The human gate exists for the final call, not for the Proposer to abdicate judgment.
- **Conservative on one-way doors, experimental on two-way doors.** Reversible changes get a lower bar for approval. Irreversible ones get extra scrutiny, stronger justification, and explicit rollback assessment. When in doubt, classify as one-way.
- **Ops burden is a silent killer.** A brilliant improvement that adds ongoing maintenance is worse than a modest improvement that simplifies operations. Always surface what changes in day-to-day operations, not just what changes in the codebase.
- **Conflicts are valuable output.** Surfacing that two findings are in tension is one of the most useful things you produce. Don't smooth over contradictions — present them with enough analysis that the human can make an informed decision.

---

## Access Model

This skill enforces strict read/write boundaries:

| Scope | Path | Access |
|-------|------|--------|
| READ | `systems/improvement-loop/research-findings/` | Read-only — search and read findings files, use Grep to filter by `priority` and other frontmatter fields |
| READ | `systems/improvement-loop/research-sources/` | Read-only — check source evidence |
| READ | `systems/improvement-loop/research-authorities/` | Read-only — check authority credibility |
| READ | Current system state: DDs via `Read` from system-scoped `project-management/design-decisions/` folders, architecture docs via `Read` from `systems/improvement-loop/knowledge/reference/`, vault files via `Read`, skill files via `Read` | Read-only — fetch for diffing |
| **WRITE** | **`systems/improvement-loop/improvement-proposals/`** | Full write — create new `.md` files and update existing proposals and `_index.md` |

**CRITICAL:** This skill NEVER writes to Research Sources, Research Findings, or Research Authorities. Those are the research-loop skill's domain.

## Local KB Paths

- **Improvement Proposals:** `systems/improvement-loop/improvement-proposals/`
- **Research Findings (read-only):** `systems/improvement-loop/research-findings/`
- **Research Sources (read-only):** `systems/improvement-loop/research-sources/`
- **Research Authorities (read-only):** `systems/improvement-loop/research-authorities/`
- **Architecture docs (read-only):** `systems/improvement-loop/knowledge/reference/`

## Improvement Proposals DB Properties

| Property | Type | Values |
|----------|------|--------|
| name | Title (frontmatter) | Proposal title (action-oriented, e.g., "Add context bracket auto-adaptation to CLAUDE.md") |
| target_system | Select | `S2 (Notion Operations)`, `S3 (Claude Code Build)`, `Perplexity Skills`, `General / Cross-System` |
| priority | Select | `P1 (Implement Now)`, `P2 (Design Required)`, `P3 (Monitor)` |
| status | Status | `Not started`, `In progress`, `Done` |
| proposal | Rich Text (frontmatter) | What to change, where, and how |
| rationale | Rich Text (frontmatter) | Why this change matters — links back to KB evidence |
| risk_level | Select | `Low`, `Medium`, `High` |
| effort | Select | `Low (< 1 hour)`, `Medium (1-4 hours)`, `High (> 4 hours)` |
| implementation_complexity | Select | `Low`, `Medium`, `High` |
| ops_impact | Select | `Reduces Ops Burden`, `Neutral`, `Adds Ops Burden` |
| conflicts | Boolean | `true` if this proposal conflicts with one or more other proposals |
| door_type | Select | `One-Way`, `Two-Way` |
| conflict_group | Rich Text | Brief description of the conflict cluster (which other proposals, why they conflict). Null if conflicts is false. |
| findings | List | Filenames of related findings (e.g., `["finding-name.md"]`) |
| date_proposed | Date | When the proposal was created |
| date_resolved | Date | When the proposal was implemented or dismissed |

### Property Definitions

**Implementation Complexity** — How hard is this to build? Accounts for the number of system surfaces touched, the depth of changes required, testing needs, and prerequisite work. Distinct from `Effort` (which measures time).

- **Low:** Single-file change, drop-in addition, no dependencies
- **Medium:** Multiple files or systems touched, moderate testing needed, some design work required
- **High:** Architectural change, cross-system coordination, significant testing, may require staging

**Ops Impact** — What happens to ongoing operational burden after this change is live?

- **Reduces Ops Burden:** This change eliminates manual steps, automates checks, or simplifies agent workflows
- **Neutral:** No meaningful change to day-to-day operations
- **Adds Ops Burden:** This change introduces new things to monitor, new agent checks, new failure modes, or new maintenance tasks

**Conflicts** — Boolean flag indicating this proposal is in tension with at least one other proposal. When true, the conflict_group field and the page body's Conflict Analysis section contain details.

**Door Type** — Reversibility assessment.

- **One-Way:** Difficult or impossible to undo once implemented. Examples: schema migrations that drop data, public API contracts, fundamental architectural shifts that other components depend on.
- **Two-Way:** Can be rolled back without significant cost. Examples: prompt rewrites, configuration changes, additive schema changes, new optional properties.

---

## Procedure: Generate Proposals

The proposer runs as a five-phase pipeline. By default, all phases run in sequence. The user may request a partial run by specifying "stop after phase N" — in which case the proposer writes intermediate results to a workspace file and stops.

### Phase 1: Scope Determination

**Goal:** Determine which parts of the system are relevant to this run, to avoid reading the entire system into context.

1. Search `systems/improvement-loop/research-findings/` for the target findings. Use `Grep` to filter by frontmatter fields — default filter: `priority: "P1"`. The user may override with P2, P3, specific categories, or specific finding names.
2. For each finding, read it with the `Read` tool to examine its `applicability` property and page body (particularly "What It Is" and "Why It Matters") to understand what system surfaces it touches.
3. Build a **scope map** — a list of which system components need to be read:

| Applicability | What to Read |
|---------------|-------------|
| S2 (Notion Operations) | Relevant DDs via `Read` from system-scoped `project-management/design-decisions/` folders, architecture docs via `Read` from `systems/improvement-loop/knowledge/reference/`, relevant Notion agent configs |
| S3 (Claude Code Build) | CLAUDE.md sections via `Read` (`/Users/nickgogan/MetaSystem/CLAUDE.md`), applicable vault files via `Read`, build specs |
| Perplexity Skills | The specific skill file(s) via `Read` from `.claude/skills/<name>/SKILL.md` |
| General | Cross-reference: which DDs establish the pattern being discussed? Read those from `systems/improvement-loop/project-management/design-decisions/` (live DDs); archived-system DD history lives under `archive/{household-os,claude-build,meta-system}/project-management/design-decisions/`. |

**Scoping rules:**
- Read only the DDs and architecture docs that are directly referenced by or relevant to the findings in this batch. Do NOT read all DDs.
- If a finding mentions "context engineering," read DD-04 (OODA), the CLAUDE.md context management sections, and any relevant skill files — not the Wardrobe System or OKR Lifecycle.
- If unsure whether a DD is relevant, check its title and the first paragraph. Only read the full page if it's clearly in scope.
- Maximum scope per run: 8-10 system documents. If the batch of findings spans more surface area than this, recommend the user split the run into multiple focused batches.

**Output:** An internal scope map (not written to disk) listing: findings to process, system documents to read, and any findings excluded with reason.

### Phase 2: System State Reading

**Goal:** Build a working understanding of the current state of the scoped system surfaces.

1. Fetch each document identified in the scope map:
   - **Architecture docs:** Use `Read` tool with paths from `systems/improvement-loop/knowledge/reference/` (Household OS architecture docs were lifted into engine knowledge in the engine-collapse restructure)
   - **Design Decisions:** Use `Read` tool with paths from `/Users/nickgogan/MetaSystem/systems/improvement-loop/project-management/design-decisions/` (live DDs); archived-system DD history is under `/Users/nickgogan/MetaSystem/archive/{household-os,claude-build,meta-system}/project-management/design-decisions/`
   - **Vault files (CLAUDE.md, rules, specs):** Use `Read` tool with absolute paths from `/Users/nickgogan/MetaSystem/`
   - **Skill files:** Use `Read` tool to read from `/Users/nickgogan/MetaSystem/.claude/skills/<name>/SKILL.md`
2. For each document, extract:
   - The current design decisions and constraints it establishes
   - The patterns and approaches currently in use
   - Any explicit "we chose X over Y" decisions (these are particularly important for conflict detection)
3. Build a **current state summary** — a concise internal reference of what exists today in the scoped area. This is the baseline against which proposals will be diffed.

**Context management:** Keep the current state summary to essential facts, not full page reproductions. The goal is to have enough context to write a meaningful diff, not to mirror the entire system in the prompt.

### Phase 3: Proposal Grouping & Conflict Analysis

**Goal:** Understand the relationships between findings before generating proposals. Identify synergies, conflicts, dependencies, and decision points.

1. **Group findings by theme/surface area.** Findings that touch the same system component or address the same concern belong in the same group. A finding can appear in multiple groups if it spans surfaces.

2. **Within each group, assess relationships:**

   - **Synergistic:** These findings reinforce each other. Implementing both is better than either alone.
   - **Independent:** These findings touch the same area but don't interact. Can be implemented in any order.
   - **Dependent:** Finding A must be implemented before Finding B (or vice versa). Note the dependency direction.
   - **Conflicting:** These findings recommend incompatible approaches. Only one can be implemented, or a synthesis is needed.

3. **For conflicting findings, produce a conflict analysis:**
   - What specifically conflicts (the concrete design choice, not just the abstract concept)
   - What each approach optimizes for (and what it sacrifices)
   - Whether a synthesis is possible that captures the value of both
   - Which approach better fits the existing system's design philosophy (reference the architecture docs' Design Philosophy section)

4. **Assign door types:**
   - For each finding/proposal, assess whether the change is reversible
   - One-way doors get extra scrutiny — note what makes them irreversible and what the fallback would be if the change doesn't work out
   - When a conflict exists between a one-way and a two-way door option, flag this prominently — it changes the decision calculus significantly

**Output:** A grouping and conflict map. If the user requested a partial run ("stop after phase 3"), write this to `systems/improvement-loop/operations/proposer-reports/{date}-conflict-analysis.md` and stop. The user can then review, make decisions on conflicts, and re-invoke with a narrowed scope.

### Phase 4: Cost & Complexity Assessment

**Goal:** For each proposed change, estimate both the implementation cost and the operational impact.

For each finding that will become a proposal:

1. **Implementation Complexity assessment:**
   - How many system surfaces does this touch? (Single file vs. multiple, single system vs. cross-system)
   - Are there prerequisites? (Other changes that must happen first)
   - What testing is needed? (Can it be validated in isolation, or does it need integration testing?)
   - How much design work is needed before implementation?

2. **Ops Impact assessment:**
   - Does this add new things agents need to check on every run?
   - Does this introduce new failure modes or monitoring requirements?
   - Does this simplify existing workflows or add steps?
   - What's the maintenance burden? (Will this drift out of date? Does it need periodic recalibration?)

3. **Net value signal:**
   - High implementation complexity + Reduces Ops Burden = may be worth the upfront investment
   - Low implementation complexity + Adds Ops Burden = cheap to build but expensive to live with — flag for careful review
   - One-way door + High complexity + Adds Ops Burden = highest-risk combination, needs strong justification

### Phase 5: Proposal Generation

**Goal:** Write concrete proposals to `systems/improvement-loop/improvement-proposals/` as markdown files, enriched with all the analysis from previous phases.

For each finding (or conflict resolution), produce a proposal entry:

1. **Create a new markdown file** in `systems/improvement-loop/improvement-proposals/` using the `Write` tool. The filename should be kebab-case derived from the proposal name (e.g., `add-context-bracket-auto-adaptation.md`). Include full YAML frontmatter with all properties:
   - **name:** Action-oriented title (verb + what + where)
   - **target_system:** Which system this changes
   - **priority:** Inherited from the finding's Proposer Priority, but may be adjusted based on conflict/complexity analysis
   - **proposal:** Brief summary — what to modify, where, and how
   - **rationale:** Why this matters, referencing the finding's evidence
   - **risk_level:** Based on scope of change, door type, and conflict status
   - **effort:** Estimated calendar time to implement
   - **implementation_complexity:** Low / Medium / High
   - **ops_impact:** Reduces Ops Burden / Neutral / Adds Ops Burden
   - **conflicts:** `true` or `false`
   - **door_type:** One-Way / Two-Way
   - **conflict_group:** If conflicts exist, brief description of what conflicts and with whom. Null otherwise.
   - **findings:** List of source finding filenames (e.g., `["context-bracket-auto-adaptation.md"]`)
   - **date_proposed:** Today
   - **date_resolved:** null

2. **Write the page body** below the frontmatter using the enhanced template (see below).

3. **For conflict clusters:** Create a proposal for each viable option. Mark all of them with `conflicts: true` and cross-reference each other in the conflict_group field and page body. The human reviewer decides which path to take.

4. **Update `_index.md`:** After creating all proposals, update `systems/improvement-loop/improvement-proposals/_index.md` to include the new entries using the `Edit` tool.

### Proposal Page Body Template

```markdown
## Current State
[What the system looks like today in the affected area — specific files, configs, or patterns in use. Drawn from Phase 2 system state reading.]

## Proposed Change
[The concrete modification — what to add, remove, or modify. Include code/config snippets where applicable.]

## Rationale
[Why this change matters — reference the research finding and its evidence. Include the finding name and a brief summary of the evidence.]

## Conflict Analysis
[Only if conflicts = true. Detail what this proposal conflicts with, why the approaches are incompatible, and what each option optimizes for. If a synthesis is possible, describe it. Reference the door type — if one option is one-way and the other is two-way, note the asymmetry.]

## Door Type Assessment
[Why this is classified as one-way or two-way. For one-way doors: what makes it irreversible, what the fallback plan would be, and what conditions would indicate the change was a mistake. For two-way doors: what rollback looks like and how long it would take.]

## Implementation Assessment
[Complexity rating with justification. Prerequisites and dependencies. What files/systems are touched. Testing approach. Estimated effort.]

## Operational Impact
[Post-implementation assessment. New monitoring needs? New agent checks? New failure modes? Does this simplify or complicate day-to-day operations? Maintenance burden and drift risk.]

## Implementation Steps
[Ordered steps to execute this change. Include which system(s) to modify and in what order.]
```

### Phase 6: Summarize

After generating all proposals, produce a brief summary for the user:

- How many proposals were created
- Breakdown by target system, priority, and door type
- Conflict clusters identified (how many, which findings are in tension)
- High-risk proposals flagged (one-way doors, high complexity, adds ops burden)
- Any findings that were skipped (and why — e.g., already adopted, not enough system context to diff, out of scope for this run)
- Recommendations for which proposals to review first (prioritize one-way doors and conflict resolutions)

---

## Scoping Strategies

The proposer can be invoked with different scoping strategies depending on the user's needs:

### By Priority (default)
```
"Run the proposer on P1 findings"
```
Processes all findings with `priority: "P1 (Implement Now)"`. Good for acting on the most urgent improvements.

### By Category
```
"Run the proposer on Context Engineering findings"
```
Processes all findings in a specific category. Good for focused improvement of one system dimension.

### By Target System
```
"Run the proposer for S3 only"
```
Processes only findings with `applicability` including S3. Reads only S3 system surfaces. Good for preparing a sprint of vault improvements.

### By Specific Findings
```
"Run the proposer on findings 'Context Bracket Auto-Adaptation' and 'Dynamic Rule Loading'"
```
Processes named findings only. Most focused scope — minimal system reading needed.

### Conflict Resolution Re-run
```
"I've decided to go with Finding 12 over Finding 7. Re-run the proposer with Finding 7 excluded."
```
After reviewing a conflict analysis, the user makes a decision and re-invokes with a narrowed scope. The proposer generates proposals only for the selected findings.

---

## Calibration Notes

- **One proposal per actionable change.** A single finding may produce multiple proposals (e.g., one for S2, one for S3). A single proposal should not bundle unrelated changes.
- **Concrete over abstract.** "Add a `context_bracket` section to CLAUDE.md with dynamic rule loading" is good. "Consider improving context management" is not.
- **Diff-grounded.** Every proposal must reference what exists today and what would change. If you can't fetch the current state, note the gap and produce the best proposal you can.
- **Scope-disciplined.** Never read more system context than the findings require. When in doubt, read less and note what you couldn't assess.
- **Conflicts are features, not bugs.** Surfacing that two findings are in tension is valuable output. Don't try to resolve conflicts — present the options clearly and let the human decide.
- **One-way doors get extra ink.** Irreversible changes deserve more detailed analysis, clearer rollback assessment, and stronger justification.
- **Ops burden is a first-class concern.** A brilliant improvement that adds ongoing maintenance is worse than a modest improvement that simplifies operations. Always surface this trade-off.
- **Human-gated.** Proposals are written for human review. They do not trigger automatic changes to any system.

---

## Integration with Other Skills

| Step | Skill | What happens |
|------|-------|-------------|
| 1. Research + Triage | **research-loop** | Process sources, populate KB, set priorities, produce delta report |
| *Human gate* | | Review findings and priorities |
| 1.5. Propose | **research-proposer** (this skill) | Read KB, analyze conflicts, assess costs, generate enriched proposals to local vault |
| *Human gate* | | Review proposals, resolve conflicts, approve/reject |
| 2. Evaluate | **prompt-evaluator** | Score flagged prompts against rubric |
| 3. Enhance | **prompt-enhancer** | Rewrite flagged prompts using evaluator output |
| 4. Deploy | Human judgment | Review, test, commit through build system |
