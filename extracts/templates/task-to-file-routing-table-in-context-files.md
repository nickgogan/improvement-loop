---
title: Task-to-File Routing Table in Context Files
type: extracted-artifact
assigned_form: template
source_finding: task-to-file-routing-table-in-context-files
extraction_date: '2026-04-26'
identification_report: 2026-04-26-identification-report.md
deployed: false
deployed_to: null
context:
  applies_to:
  - agents operating over multi-file workspaces where different task types require different subsets of context files
  - operators managing context window budgets in long agentic sessions where loading all files is not feasible
  - teams that want human-readable, auditable control over what information an agent uses for each task type
  platform_coupling: agnostic
  autonomy: all
  stage: specify
  reversibility: trivial — the routing table is a markdown table in a text file; adding, editing, or removing rows has no downstream migration cost
  auditability: high — the routing table is a human-readable artifact; any observer can verify which files the agent should load for a given task by reading the table; compliance is checkable by comparing
    agent file-load behavior against the table
  evidence_strength: Strong
  adoption:
    status: Not Yet Started
    notes: null
contract:
  preconditions: The workspace has a stable set of recurring task types that can be named and described in plain English. The files relevant to each task type are known at the time the table is authored.
    The agent has a context file it reads at session or task start (e.g., CLAUDE.md or equivalent). The operator can maintain the table as the workspace evolves.
  invariants: 'The routing table is the authoritative source for file loading decisions within the workspace — the agent does not load files outside the table''s Read lists without explicit operator instruction.
    Every task type in active use has a row in the table. Skip lists are honored: the agent does not load skipped files even if they appear relevant to the task. The table is human-readable and editable
    without tooling.'
  governance: 'Owner: the workspace operator (human or team). The routing table is a workspace artifact — it is versioned with the workspace and updated whenever file dependencies change. Any agent authorized
    to propose additions to the routing table must surface them to the operator for approval before they are written. The table must not be modified by the agent autonomously during task execution.'
  recovery: 'If a referenced file no longer exists (renamed, moved, deleted): the agent halts and reports the missing file rather than proceeding with incomplete context; the operator updates the routing
    table. If a task does not match any row: the agent halts and prompts the operator to add a new row before continuing — it does not self-direct file loading. If the table becomes stale and produces incorrect
    context loads: audit all rows against the current workspace file structure; update or remove stale entries; add a last-verified date to each row.'
tags:
- extracted-artifact
- template
---

# Task-to-File Routing Table in Context Files

**Source:** [[task-to-file-routing-table-in-context-files]]
**Form:** template
**Extraction date:** 2026-04-26

## Variables

- **`{{WORKSPACE_NAME}}`** (string): The name of the workspace or project this routing table governs. Used as a header to identify scope.
- **`{{TASK_TYPE}}`** (string, repeating): A plain-English label for a category of tasks the agent performs in this workspace (e.g., "Write blog post", "Update schema", "Run research query"). Each row in the table has one task type.
- **`{{READ_FILES}}`** (list of strings, repeating): File paths or glob patterns the agent must read before executing this task type. Relative to the workspace root. Example: `voice-context.md, blog-template.md`.
- **`{{SKIP_FILES}}`** (list of strings or glob patterns, repeating): File paths or directories the agent must not load for this task type, even if they exist in the workspace. Example: `production-outputs/`. Use `—` if no files should be skipped.
- **`{{SKILLS_NEEDED}}`** (list of strings, repeating): Named skills or capabilities the agent must have available to execute this task type. Example: `humanizer, fact-checker`. Use `—` if no special skills are required.

## Body

```markdown
# Task Routing — {{WORKSPACE_NAME}}

The agent reads this table at the start of any task in this workspace.
Load ONLY the files listed under "Read" for the matching task type.
Do NOT load files listed under "Skip" even if they exist in the workspace.

| Task | Read These Files | Skip These Files | Skills Needed |
|------|-----------------|-----------------|---------------|
| {{TASK_TYPE}} | {{READ_FILES}} | {{SKIP_FILES}} | {{SKILLS_NEEDED}} |
| {{TASK_TYPE}} | {{READ_FILES}} | {{SKIP_FILES}} | {{SKILLS_NEEDED}} |
| {{TASK_TYPE}} | {{READ_FILES}} | {{SKIP_FILES}} | {{SKILLS_NEEDED}} |

## Routing Protocol

1. Match the incoming task description to the closest task type in the table above.
2. Load all files listed in "Read These Files" for the matched row before beginning the task.
3. Do not load any files listed in "Skip These Files" for this task, regardless of their presence in the workspace.
4. Confirm the required skills are available before proceeding.
5. If the task does not match any row: halt; prompt the operator to add a new row before continuing.
```

## Usage

Place the rendered routing table inside the workspace's context file (e.g., a workspace-level `CLAUDE.md`, a project-specific context document, or a workspace configuration file that the agent reads at session start).

The agent must be instructed — in the same context file or in its base prompt — to read this table before loading any other workspace files. The routing table is only effective if the agent reads it first and acts on its constraints.

Update the table whenever:
- A new task type is added to the workspace
- A file is renamed, moved, or removed
- A new skill becomes available or is deprecated
- The operator observes the agent loading files not relevant to the current task

## Variation Axis

What drives different renderings of this template:

- **Workspace complexity:** Simple workspaces (2–3 task types, few files) render minimal tables. Complex workspaces (10+ task types, deep file hierarchies) may benefit from splitting the routing table by task domain (e.g., one table for content tasks, one for operational tasks).
- **Agent capability:** If the agent cannot follow "skip" instructions reliably, omit the Skip column and rely on the Read column's specificity to constrain loading.
- **Staleness risk:** Workspaces where files are frequently renamed or reorganized need a "last verified" date on each row and a periodic review process. Add a `{{LAST_VERIFIED}}` column if staleness is a concern.
- **Dynamic discovery:** If the workspace has task types that cannot be anticipated in advance, add a catch-all row: `Unknown task | — | — | Halt and prompt operator to add a routing row` to make the protocol explicit for unmatched cases.

## Contract

### Preconditions
The workspace has a stable set of recurring task types that can be named and described in plain English. The files relevant to each task type are known at the time the table is authored. The agent has a context file it reads at session or task start (e.g., CLAUDE.md or equivalent). The operator can maintain the table as the workspace evolves.

### Invariants
The routing table is the authoritative source for file loading decisions within the workspace — the agent does not load files outside the table's Read lists without explicit operator instruction. Every task type in active use has a row in the table. Skip lists are honored: the agent does not load skipped files even if they appear relevant to the task. The table is human-readable and editable without tooling.

### Governance
Owner: the workspace operator (human or team). The routing table is a workspace artifact — it is versioned with the workspace and updated whenever file dependencies change. Any agent authorized to propose additions to the routing table must surface them to the operator for approval before they are written. The table must not be modified by the agent autonomously during task execution.

### Recovery
If a referenced file no longer exists (renamed, moved, deleted): the agent halts and reports the missing file rather than proceeding with incomplete context; the operator updates the routing table. If a task does not match any row: the agent halts and prompts the operator to add a new row before continuing — it does not self-direct file loading. If the table becomes stale and produces incorrect context loads: audit all rows against the current workspace file structure; update or remove stale entries; add a last-verified date to each row.
