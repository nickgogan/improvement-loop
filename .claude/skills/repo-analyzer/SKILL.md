---
name: repo-analyzer
description: >-
  Structural analysis of GitHub repos tracked in the watched-libraries registry.
  Clones repos to a temp cache, extracts patterns across 5 dimensions (structural
  inventory, context file map, workflow topology, governance model, cross-agent
  protocol), and writes standardized analysis docs. Use when evaluating a new
  watched library, re-analyzing after an upstream version bump, or producing a
  cross-repo comparison report.
user-invocable: true
allowed-tools: Read Grep Glob Write Edit Bash WebFetch
argument-hint: "<library-name|all> [--dimensions dim1,dim2,...] [--compare] [--force]"
---

# Repo Analyzer

Repeatable structural analysis of GitHub repos in the watched-libraries registry. Clones repos to an ephemeral cache, extracts patterns across 5 dimensions, and writes standardized analysis docs to `systems/improvement-loop/watched-libraries/analysis/`.

## When to Use This Skill

- After adding a new watched library entry to the registry
- After a version bump in a watched library (detected by comparing versions)
- When the user asks to analyze a specific repo's architecture or patterns
- When producing a cross-repo comparison of all analyzed libraries
- Periodically as a refresh pass

Do NOT use this skill for:
- Running or testing code from external repos
- Writing research findings (use `/research-loop` for that)
- Evaluating whether to adopt a library (use the watched-library entry's spectrum rationale)

## Cognitive Disposition

The Repo Analyst thinks like a structural cartographer, not a code reviewer.

- **Structure over semantics.** Map how a repo is organized, not whether its code is good. Record what exists and how it connects.
- **Patterns over details.** Extract recurring structural patterns (naming conventions, file hierarchies, handoff mechanisms). Skip one-off implementation specifics.
- **Descriptive, not prescriptive.** Document observations. Do not recommend changes to the analyzed repo. Recommendations about MetaSystem adoption belong in research findings, not here.
- **Consistent lens across repos.** Every repo gets the same 5-dimension treatment. This is what makes cross-repo comparison possible.
- **Context files are the highest-value target.** These define how agents behave — CLAUDE.md, SOUL.md, .cursorrules, agents.md, etc. Map every one of them.

## Available Tools

| Tool | Purpose |
|------|---------|
| `Bash` | Clone repos (`git clone --depth 1`), run `find`/`wc`/`tree` for structural stats |
| `Read` | Read context files, config files, workflow definitions |
| `Grep` | Search for patterns (agent handoff markers, phase transitions, constraint expressions) |
| `Glob` | Find files by pattern (all `.md`, all `CLAUDE.md`, all `agents/`) |
| `Write` | Create analysis output docs |
| `Edit` | Update existing analysis docs on re-run |
| `WebFetch` | Fetch README or docs if repo clone fails |

## Paths

| Path | Purpose |
|------|---------|
| `systems/improvement-loop/watched-libraries/` | Watched library metadata entries (input) |
| `systems/improvement-loop/watched-libraries/analysis/` | Analysis output docs |
| `systems/improvement-loop/watched-libraries/analysis/_index.md` | Index of all analysis docs |
| `systems/improvement-loop/watched-libraries/analysis/cross-repo-comparison.md` | Cross-repo comparison report |
| `/tmp/metasystem-repo-cache/` | Ephemeral shallow clones (outside vault) |

---

## Arguments

| Argument | Effect |
|----------|--------|
| `<library-name>` | Analyze a single watched library by name (kebab-case slug, e.g. `gsd`, `bmad-method`) |
| `all` | Analyze all watched libraries sequentially |
| `--compare` | Produce cross-repo comparison from existing analysis docs. Can combine with `all` to analyze then compare. |
| `--dimensions dim1,dim2` | Only run specified dimensions. Values: `structural-inventory`, `context-file-map`, `workflow-topology`, `governance-model`, `cross-agent-protocol` |
| `--force` | Re-analyze even if version hasn't changed since last analysis |

---

## Analysis Output Frontmatter Schema

```yaml
---
title: "{Library Name} -- Structural Analysis"
id: "{library-name}-analysis"
type: "analysis"
category: "upstream-tracking"
target_system:
  - "cross-system"
stage: "active"
created: "{date}"
updated: "{date}"
author: "improvement-loop"
source_dd:
  - "DD-45"
  - "DD-46"
tags:
  - "repo-analysis"
  - "watched-library"
  - "{library-name}"
analyzed_version: "{version from watched-library entry}"
analyzed_date: "{today}"
repo_url: "{url from watched-library entry}"
dimensions_analyzed:
  - "structural-inventory"
  - "context-file-map"
  - "workflow-topology"
  - "governance-model"
  - "cross-agent-protocol"
---
```

## Analysis Output Body Structure

```markdown
# {Library Name} -- Structural Analysis

## Metadata
- **Repo:** {url}
- **Version analyzed:** {version}
- **Date:** {date}
- **Spectrum position:** {from watched-library entry}

---

## 1. Structural Inventory

### File Tree Statistics
| Metric | Value |
|--------|-------|
| Total files | |
| Total directories | |
| Markdown files | |
| Code files (by language) | |
| Config/YAML/JSON files | |
| MD-to-code ratio | |
| Max directory depth | |

### Markdown Composition
| Purpose | Count | Directory |
|---------|-------|-----------|
| Agent definitions | | |
| Commands/skills | | |
| Workflows/orchestration | | |
| Reference docs (shared knowledge) | | |
| Templates (artifact schemas) | | |
| Human documentation | | |
| Other | | |

[Classify each MD file by its functional role, not just its extension. The composition reveals whether markdown is "the codebase" (agent personas, workflows) or supplementary (docs, README).]

### Directory Naming Conventions
[Observed patterns: kebab-case, camelCase, etc. Role-based naming? Type-based naming?]

### Top-Level Structure
[Tree-like representation of the first 2 levels of the directory hierarchy]

### Notable Structural Patterns
[Anything unusual or distinctive about the file organization]

---

## 2. Context File Map

| File Path | Audience | Scope | Mechanism | Content Type | Summary |
|-----------|----------|-------|-----------|--------------|---------|

### Classification Key
- **Audience**: `LLM` (parsed by model), `Human` (developer docs), `Both`
- **Scope**: `Global` (all agents), `Project` (project-specific), `Task` (per-task), `Tool` (tool-specific)
- **Mechanism**: `Auto-loaded` (harness reads automatically, self-contained), `Chain-loader` (auto-loaded AND @-references other files — entry point that assembles context from downstream files), `Hook-injected` (injected into session context by a hook script, not by file path or agent spawn), `Referenced` (pulled in via @ mentions or includes from another file), `Injected` (loaded by harness when a skill/workflow spawns an agent)
- **Content Type**: `Identity/Persona`, `Constraints/Rules`, `Workflow/Process`, `Tool Usage`, `Memory/State`

### Sampling Notes
[If the sampling strategy was used, note which files were read in full vs. classified by extrapolation. E.g., "Read in full: 3 agent exemplars. Classified by pattern: 21 remaining agents."]

### Context Loading Strategy
[How does this repo assemble agent context? Single file? Layered? Dynamic?]

---

## 3. Workflow Topology

### Phases/Stages
| Phase | Entry Trigger | Exit Condition | Human Gate? |
|-------|--------------|----------------|-------------|

### Flow Diagram (ASCII)
[ASCII representation of workflow stages and transitions]

### Transition Mechanisms
[How does the system move between phases? File markers? Function calls? User commands?]

### Parallelism
[Are any stages designed to run in parallel? How is coordination handled?]

---

## 4. Governance Model

### Constraint Expression
| Mechanism | Location | Enforcement | Example |
|-----------|----------|-------------|---------|
| Constitution file | path | Hard/Soft | ... |
| Rules files | path | ... | ... |
| Inline constraints | path | ... | ... |

### Guardrail Patterns
[How does this repo prevent agents from going off-rails? Allowlists? Denylists? Budget limits?]

### Permission Model
[Who/what can do what? Are there explicit permission boundaries?]

---

## 5. Cross-Agent Protocol

### Agent Roster
| Agent/Role | Defined In | Capabilities | Communicates With |
|------------|-----------|--------------|-------------------|

### Handoff Mechanisms
[How do agents pass work to each other? File-based? Message-based? Tool invocation?]

### Shared State
[What state is shared across agents? Files? Databases? Memory objects?]

### Coordination Patterns
[Sequential pipeline? Hub-and-spoke? Peer-to-peer? Event-driven?]

---

## 6. Research Dimension Mapping

| Dimension | Relevance | Key Patterns Observed |
|-----------|-----------|----------------------|
| Context Engineering | | |
| Model | | |
| Prompt | | |
| Tools | | |
| Intent | | |
| Orchestration | | |
| Evaluation | | |
| Sandboxing | | |
| Governance | | |
| Agent Design | | |

[Rate relevance as `High`, `Medium`, `Low`, or `None`. For High/Medium, note the specific patterns observed that map to this dimension. This bridges structural analysis to the research pipeline — `/research-proposer` can read this to understand what implementation details back a pattern.]

### Findings Candidates

[Patterns worth promoting to Research Findings KB entries. Include the dimension they map to and why they're notable. These are suggestions only — promotion requires a separate `/research-loop` invocation.]

---

## Version Log

| Date | Version | Dimensions | Notes |
|------|---------|------------|-------|
```

---

## Procedure

### Step 0: Parse Arguments and Load Context

1. Parse the argument to determine scope:
   - `repo-analyzer gsd` -- analyze one library
   - `repo-analyzer all` -- analyze all libraries
   - `repo-analyzer all --compare` -- analyze all, then produce comparison
   - `repo-analyzer --compare` -- produce comparison from existing analyses only (no cloning)
   - `--dimensions structural-inventory,context-file-map` -- only run specified dimensions
   - `--force` -- re-analyze even if version unchanged
2. Use `Read` to load `systems/improvement-loop/watched-libraries/_index.md` and the target watched-library entry(ies).
3. For each target library, extract `repo_url`, `last_evaluated_version`, `name`, and `spectrum_position` from the entry.
4. If not `--force`, check if `systems/improvement-loop/watched-libraries/analysis/{library-name}-analysis.md` exists. If it does, read its `analyzed_version` frontmatter. Skip if it matches `last_evaluated_version`. Report "up to date" to the user.

### Step 1: Ensure Analysis Directory

1. Use `Bash` to verify `systems/improvement-loop/watched-libraries/analysis/` exists.
2. If `systems/improvement-loop/watched-libraries/analysis/_index.md` does not exist, create it with the standard index frontmatter.

### Step 2: Clone or Reuse Cached Repository

1. Use `Bash` to check if `/tmp/metasystem-repo-cache/{library-name}/` exists and contains a `.git` directory.
2. If it exists, reuse it. Optionally run `git -C /tmp/metasystem-repo-cache/{library-name}/ pull` if freshness matters.
3. If it does not exist, run:
   ```bash
   git clone --depth 1 {repo_url} /tmp/metasystem-repo-cache/{library-name}/
   ```
4. If clone fails (private repo, rate limit, network), fall back to `WebFetch` on the README URL and note the limitation. Mark affected dimensions as "partial" in the output.

### Step 3: Structural Inventory (Dimension 1)

1. Count total files: `find /tmp/metasystem-repo-cache/{name}/ -type f -not -path '*/.git/*' | wc -l`
2. Count directories: `find ... -type d -not -path '*/.git/*' | wc -l`
3. Count by file extension (top 20):
   ```bash
   find ... -type f -not -path '*/.git/*' | sed 's/.*\.//' | sort | uniq -c | sort -rn | head -20
   ```
4. Count markdown files: `find ... -name "*.md" -not -path '*/.git/*' | wc -l`
5. Produce 2-level directory tree:
   ```bash
   find ... -maxdepth 2 -type d -not -path '*/.git/*' | sort
   ```
6. Compute max directory depth:
   ```bash
   find ... -type d -not -path '*/.git/*' | awk -F/ '{print NF}' | sort -rn | head -1
   ```
7. Calculate MD-to-code ratio from the extension counts.
8. **Markdown composition breakdown**: Classify each `.md` file by functional purpose (agent definition, command/skill, workflow, reference doc, template, human documentation, other). Use directory location as the primary signal — e.g., files in `agents/` are agent definitions, files in `docs/` are human documentation. Populate the Markdown Composition table.
9. Note directory naming conventions (kebab-case, camelCase, etc.).

### Step 4: Context File Map (Dimension 2)

1. Search for known context file patterns in the cloned repo using `Glob` or `Bash`:
   - `**/CLAUDE.md`, `**/SOUL.md`, `**/.cursorrules`, `**/.clinerules`
   - `**/agents.md`, `**/AGENTS.md`, `**/TOOLS.md`, `**/MEMORY.md`, `**/USER.md`, `**/HEARTBEAT.md`
   - `**/.claude/rules/*.md`, `**/.claude/skills/*/SKILL.md`, `**/.claude/agents/*.md`
   - `**/rules/*.md`, `**/prompts/*.md`, `**/personas/*.md`
   - `**/*.prompt`, `**/*.system`, files with "system-prompt" in name
   - Root and first-level `README.md` files
2. Also scan for any `.md` file containing LLM-addressing language: `"You are"`, `"When the user"`, `"Your role"`, `"## Instructions"`, `"## Rules"`.
3. **Sampling strategy for large sets**: If a directory contains more than 5 files with the same structural pattern (same frontmatter schema, same XML/section structure), read 2-3 exemplars in full, then classify the rest by extrapolation. Note in the output which files were read vs. inferred. This prevents token waste on repos with 20+ uniform agent definitions.
4. For each found file (or exemplar), use `Read` (first 100 lines) to classify:
   - **Audience**: Addresses the model directly ("You are...", "When asked...") = `LLM`. Explains to developers = `Human`. Both = `Both`.
   - **Scope**: Repo root = `Global`. Project/feature subdirectory = `Project`. Task/workflow directory = `Task`. Attached to a tool = `Tool`.
   - **Mechanism**: In a harness auto-load location AND self-contained (no `@` references to other files) = `Auto-loaded`. In a harness auto-load location AND `@`-references other files (entry point that assembles context) = `Chain-loader`. Injected into session context by a hook script (e.g., SessionStart) = `Hook-injected`. Pulled in via `@` references or includes from another file = `Referenced`. Loaded by harness when a skill/workflow spawns an agent = `Injected`.
   - **Content Type**: Identity/persona definitions = `Identity/Persona`. Constraints/rules = `Constraints/Rules`. Workflow/process docs = `Workflow/Process`. Tool usage = `Tool Usage`. Memory/state tracking = `Memory/State`.
5. Populate the Context File Map table.
6. Write a "Context Loading Strategy" summary describing the overall pattern, paying special attention to chain-loading relationships (which files pull in which other files, and in what order).

### Step 5: Workflow Topology (Dimension 3)

1. Search for phase/stage indicators using `Grep`:
   - Patterns: `phase`, `stage`, `step`, `workflow`, `pipeline`, `-->`, `transition`
   - Look in: `workflows/`, `phases/`, `steps/`, `process/` directories
2. Read the main README and any workflow definition files.
3. Search for transition triggers: `trigger`, `when`, `after`, `before`, `gate`, `approval`
4. Search for human gate markers: `human`, `manual`, `approval`, `review`, `confirm`
5. Map the workflow as phases with entry triggers, exit conditions, and human gates.
6. Produce an ASCII flow diagram.
7. Note if the repo has no discernible workflow (libraries like mem0 may not).

### Step 6: Governance Model (Dimension 4)

1. Search for governance files using `Grep`:
   - Patterns: `constitution`, `rules`, `constraints`, `guardrails`, `permissions`, `forbidden`, `must not`, `never`
   - Look in: `governance/`, `rules/`, `constraints/` directories
2. For each governance file, classify:
   - **Mechanism**: Constitution file, rules file, inline constraint, config restriction
   - **Enforcement**: `Hard` (system refuses) vs `Soft` (system warns)
3. Map the permission model: allowlists, denylists, role-based access, tool restrictions.
4. Note if governance is implicit (no explicit files) vs explicit.

### Step 7: Cross-Agent Protocol (Dimension 5)

1. Search for multi-agent indicators using `Grep`:
   - Patterns: `agent`, `subagent`, `handoff`, `delegate`, `orchestrat`, `coordinator`, `worker`, `specialist`
   - Look in: `agents/`, `roles/` directories
2. Read agent definition files. Map:
   - Agent roster (who exists, where defined)
   - Communication channels (files, tool calls, shared state)
   - Handoff protocols (how work moves between agents)
   - Shared state mechanisms
3. Classify coordination pattern: `Sequential Pipeline`, `Hub-and-Spoke`, `Peer-to-Peer`, `Event-Driven`, `None` (single-agent).

### Step 7b: Research Dimension Mapping (Dimension 6)

1. Read the active research dimensions registry at `systems/improvement-loop/operations/knowledge/research-dimensions.md`.
2. For each of the 10 dimensions, assess how relevant this repo's patterns are:
   - **High**: The repo has explicit, well-developed patterns that directly exemplify this dimension (e.g., a multi-agent orchestration framework is High for Orchestration).
   - **Medium**: The repo touches this dimension but it's not a primary focus (e.g., a tool framework that has some context management but isn't centered on it).
   - **Low**: Incidental relevance only.
   - **None**: No observable patterns for this dimension.
3. For High and Medium dimensions, note the specific patterns observed — reference the relevant sections from dimensions 1-5.
4. Identify **Findings Candidates**: patterns that are novel, well-implemented, or would fill a gap in the current Research KB. Note which dimension they map to and why they're worth promoting. These are suggestions only — actual promotion goes through `/research-loop`.

### Step 8: Write Analysis Document

1. **New analysis**: Use `Write` to create `systems/improvement-loop/watched-libraries/analysis/{library-name}-analysis.md` with the full frontmatter and all dimension sections.
2. **Re-run (existing doc)**: Use `Edit` to update each dimension section and frontmatter fields (`updated`, `analyzed_version`, `analyzed_date`, `dimensions_analyzed`). Append a new row to the Version Log table.
3. Update `systems/improvement-loop/watched-libraries/analysis/_index.md` with the new or updated entry row.

### Step 9: Repeat for Additional Libraries

If `all` was specified, repeat Steps 2-8 for each watched library in the registry. Process sequentially. Write each analysis doc before moving to the next to preserve partial progress.

### Step 10: Cross-Repo Comparison (if `--compare`)

1. Use `Glob` to find all `*-analysis.md` files in `systems/improvement-loop/watched-libraries/analysis/`.
2. Use `Read` to load each analysis doc.
3. Produce `systems/improvement-loop/watched-libraries/analysis/cross-repo-comparison.md` with:

**Comparison frontmatter:**
```yaml
---
title: "Cross-Repo Structural Comparison"
id: "cross-repo-comparison"
type: "analysis"
category: "upstream-tracking"
target_system:
  - "cross-system"
stage: "active"
created: "{date}"
updated: "{date}"
author: "improvement-loop"
source_dd:
  - "DD-45"
  - "DD-46"
tags:
  - "repo-analysis"
  - "cross-repo"
  - "comparison"
repos_compared: [list of analyzed library names]
---
```

**Comparison body sections:**

- **Comparison Matrix** — Tables comparing all repos across each dimension:
  - Structural Scale (files, MD:code ratio, depth)
  - Context File Patterns (count, mechanism, layering)
  - Workflow Comparison (phases, gates, parallelism)
  - Governance Comparison (constitution?, enforcement, permissions)
  - Cross-Agent Comparison (agent count, coordination, handoff)
- **Pattern Clusters**:
  - Shared Patterns (3+ repos) — emerging conventions
  - Unique Patterns (1 repo only) — potential innovation or niche
  - Contradictory Approaches — opposite design choices for the same problem
- **Findings Candidates** — Patterns worth promoting to Research Findings KB (suggestions only, promotion requires a separate `/research-loop` invocation)

---

## Rules

1. **Never persist cloned repos inside the vault.** Always use `/tmp/metasystem-repo-cache/`. Clones in the vault cause git-in-git pain, search pollution, and graph noise.
2. **Shallow clones only.** `--depth 1` is sufficient for structural analysis. Git history is not needed.
3. **Do not execute any code from cloned repos.** No `npm install`, `pip install`, `make`, or running scripts. This is a read-only structural pass.
4. **Do not write to Research Findings.** Analysis docs stay in `watched-libraries/analysis/`. Pattern promotion to the KB is a separate human-gated decision.
5. **Every analysis doc gets the full frontmatter schema.** No exceptions, even for partial analyses (note which dimensions are incomplete).
6. **Update `_index.md` after every write.**
7. **Respect the `--dimensions` flag.** If the user only requests `context-file-map`, do not run the other 4 dimensions. Update only the specified sections in an existing doc.
8. **Stale detection is automatic.** On every invocation (unless `--force`), compare `analyzed_version` to `last_evaluated_version`. Report "up to date" and skip if unchanged.
9. **Handle missing workflows gracefully.** Not every repo has a workflow topology (libraries vs frameworks). Record "No discernible workflow" rather than forcing a topology.
10. **Cap structural listings.** For very large repos, truncate file listings at 500 entries and note the truncation.
