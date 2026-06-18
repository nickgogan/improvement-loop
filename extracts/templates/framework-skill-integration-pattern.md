---
title: "Framework Skill Integration Pattern (Scan-Catalog-Inject-Load)"
type: "extracted-artifact"
assigned_form: "template"
source_finding: "skills-portability-across-sdk-and-framework-boundaries"
extraction_date: "2026-05-25"
last_change_session: 102
last_change_sl: "session-102-codifier-identify-and-extract-artifacts"
identification_report: null
deployed: false
deployed_to: null
context:
  applies_to:
    - "any agent framework or SDK that loads skills from a directory and exposes them to the agent at runtime"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "build"
  reversibility: "low — replacing a native-tool approach with skill-based loading is a non-trivial refactor; individual skills remain portable"
  auditability: "high — the catalog injected into the system prompt is inspectable; load-skill tool calls are logged; no hidden state"
  evidence_strength: "Medium (practitioner-documented)"
  adoption:
    status: "Partially Adopted"
    notes: "Cole Medin demonstrated the pattern for both Claude Agent SDK and Pydantic AI in the same project; skills carried across without modification."
contract:
  preconditions: "A skills directory exists with SKILL.md files. Each SKILL.md has a name and description in its front matter or first lines. The agent framework allows dynamic system prompt construction. A file-read tool or equivalent is available for the agent to load skill content on demand."
  invariants: "Skill files are not modified at load time. The catalog injected into the system prompt lists every skill available in the directory at startup — no selective omission. The load-skill tool returns the full SKILL.md content without truncation."
  governance: "Skills directory path and the load-skill tool name must be declared in the agent's CLAUDE.md or equivalent config. Adding a skill is a file-drop operation; the agent picks it up on next startup without code changes. Removing a skill is a file-delete; catalog is regenerated on next startup."
  recovery: "If a skill file is malformed (missing name/description) → log the error, skip that skill in the catalog, continue startup. If the load-skill tool fails → surface the error in the agent's response; do not silently fall back to implicit model knowledge. If the catalog is stale (skills added after startup) → restart the agent session to pick up new skills."
tags:
  - "extracted-artifact"
  - "template"
  - "skills"
  - "agent-framework"
  - "context-engineering"
---

# Framework Skill Integration Pattern (Scan-Catalog-Inject-Load)

**Source:** [[skills-portability-across-sdk-and-framework-boundaries]]
**Form:** template
**Extraction date:** 2026-05-25

## Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `{{SKILLS_DIR}}` | Relative path from the agent's working directory to the skills directory | `skills/` or `.claude/skills/` |
| `{{LOAD_SKILL_TOOL_NAME}}` | Name of the tool the agent calls to read a full SKILL.md | `load_skill` |
| `{{SKILL_CATALOG_INJECTION_POINT}}` | Location in the system prompt where the catalog is injected | After core identity, before task instructions |
| `{{AGENT_FRAMEWORK}}` | SDK or framework in use | `Claude Agent SDK`, `Pydantic AI`, `LangGraph` |

---

## Body

### Step 1 — Scan (startup)

At agent initialization, scan `{{SKILLS_DIR}}` for `SKILL.md` files. For each file, extract:
- **Name** — first H1 heading or `title` frontmatter field
- **Description** — first paragraph below the heading or `description` frontmatter field

Build an in-memory skill catalog: `[{name, description, path}, ...]`.

```python
# {{AGENT_FRAMEWORK}} startup hook — pseudocode
skill_catalog = []
for path in glob("{{SKILLS_DIR}}/**/SKILL.md"):
    name, description = parse_skill_header(path)
    skill_catalog.append({"name": name, "description": description, "path": path})
```

### Step 2 — Inject (system prompt)

Inject the skill catalog into the system prompt at `{{SKILL_CATALOG_INJECTION_POINT}}`. Format:

```
## Available Skills

{{#each skill_catalog}}
- **{{name}}**: {{description}}
{{/each}}

To use a skill, call the `{{LOAD_SKILL_TOOL_NAME}}` tool with the skill name. Then follow the skill's instructions exactly.
```

### Step 3 — Provide Load Tool

Register a tool named `{{LOAD_SKILL_TOOL_NAME}}` that accepts a skill name, looks it up in the catalog, and returns the full SKILL.md content.

```python
def {{LOAD_SKILL_TOOL_NAME}}(skill_name: str) -> str:
    """Load the full instructions for a named skill."""
    entry = next((s for s in skill_catalog if s["name"] == skill_name), None)
    if entry is None:
        return f"Error: skill '{skill_name}' not found. Available: {[s['name'] for s in skill_catalog]}"
    return read_file(entry["path"])
```

### Step 4 — Agent Follows Skill Instructions

The agent calls `{{LOAD_SKILL_TOOL_NAME}}("{{SKILL_NAME}}")`, receives the SKILL.md content, and executes the procedure it describes — including any tool calls, sub-steps, or output formats the skill specifies.

The agent does not interpret, abridge, or rewrite the skill content. It follows the skill as written.

---

## Usage

1. Copy this template into your agent initialization code.
2. Fill in all `{{VARIABLES}}`.
3. Register the load-skill tool in your framework's tool registry.
4. Drop SKILL.md files into `{{SKILLS_DIR}}` — the agent picks them up on next startup.
5. Validate: invoke one skill end-to-end; confirm the agent reads the full SKILL.md before executing.

---

## Variation Axis

| Axis | Option A | Option B |
|------|----------|----------|
| **Catalog format** | Bulleted list in system prompt | Structured XML/JSON block (better for parsing) |
| **Load trigger** | Agent decides when to load | Caller specifies skill name in initial message |
| **Skill discovery** | Flat directory scan | Recursive scan with subdirectory namespacing |
| **Hot-reload** | Restart required | File-watcher re-scans on change (dev environments) |
| **Contextual scoping** | All skills always in catalog | Routing table filters catalog by workspace/task type (see [[skills-inside-workspace-contextual-skill]]) |

---

## Contract

### Preconditions
A skills directory exists with SKILL.md files. Each SKILL.md has a name and description in its front matter or first lines. The agent framework allows dynamic system prompt construction. A file-read tool or equivalent is available for the agent to load skill content on demand.

### Invariants
Skill files are not modified at load time. The catalog injected into the system prompt lists every skill available in the directory at startup — no selective omission. The load-skill tool returns the full SKILL.md content without truncation.

### Governance
Skills directory path and the load-skill tool name must be declared in the agent's CLAUDE.md or equivalent config. Adding a skill is a file-drop operation; the agent picks it up on next startup without code changes. Removing a skill is a file-delete; catalog is regenerated on next startup.

### Recovery
If a skill file is malformed (missing name/description) → log the error, skip that skill in the catalog, continue startup. If the load-skill tool fails → surface the error in the agent's response; do not silently fall back to implicit model knowledge. If the catalog is stale (skills added after startup) → restart the agent session to pick up new skills.
