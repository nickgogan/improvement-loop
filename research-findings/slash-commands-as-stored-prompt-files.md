---
name: Slash Commands as Stored Prompt Files for Repeated Vault Tasks
summary: Creating a /commands/ folder in the vault where each file is a saved prompt for a frequently repeated task. Claude reads the file when the slash command is invoked, executing the full prompt without the user retyping it. This is the Obsidian-native equivalent of Claude Code custom skills, but simpler — a plain text file with a prompt.
implementation_notes: This pattern is a lighter-weight alternative to full skill files (.md with frontmatter + full instructions). For simple repeated prompts in an Obsidian vault, a commands/ folder is sufficient. For complex multi-step workflows with branching logic, a full skill is still appropriate.
category: Tool Integration
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
proposer_priority: P3 (Monitor)
applicability:
- General
- S3 (Claude Code Build)
adopted_in: []
sources:
- obsidian-claude-code-setup-terminal-integration.md
related_findings:
- file: project-specific-custom-skills-for-repeated-task.md
  rel: same-problem
- file: obsidian-terminal-plugin-embedded-claude-code-sidebar.md
  rel: extends
proposals: null
date_discovered: '2026-04-19'
last_updated: '2026-04-19'
pipeline_status: raw
consumed_by: []
---
# Slash Commands as Stored Prompt Files for Repeated Vault Tasks

## What It Is
A `commands/` folder in the vault root. Each file in the folder is a plain text (or markdown) file containing a full prompt for a frequently repeated task. Example: `commands/journal-image-entry.md` contains the full prompt for creating a journal entry from a screenshot — specifying where to save it, what metadata to include, how to cross-link people mentioned, where to store attached images.

Workflow:
1. Type `/journal-image-entry` in the terminal (or a keyboard shortcut if configured)
2. Claude reads `commands/journal-image-entry.md`
3. Executes the prompt with any attached context (e.g., a pasted screenshot)

The key advantage over retyping: the prompt file is versioned in git, editable as a markdown file, and can accumulate refinements over time. When a new convention is established, update the prompt file — all future invocations use the improved prompt without the user remembering to change their query.

The B35SWx_4BNM creator demonstrates: asks Claude to "create a slash command for me that I can use to trigger this in the future" — Claude creates the commands/ folder and a file with an expanded, more detailed version of the prompt than the user originally provided.

## Why It Matters
Custom skills (SKILL.md with full frontmatter and multi-step instructions) have overhead: they require the full skill file format, they're loaded into context via the skills system, and they need to be installed. For simple repeated prompts, this overhead is unnecessary. The commands/ folder pattern is the minimal viable version: a folder of text files that Claude reads when invoked.

This also separates concerns: CLAUDE.md holds vault-wide conventions and environment context; commands/ holds task-specific prompts. CLAUDE.md gets loaded every session; commands/ files are loaded on demand.

## Why People Are Using It
The creator demonstrates the journal entry workflow — takes a screenshot, types `/journal image entry`, pastes the image, and Claude executes the full structured ingestion (save image to attachments/, create/update daily journal entry, cross-link people, update people base). All of this from a single command, driven by the prompt file's instructions.

## Potential Alternatives
Full Claude Code custom skills (more powerful, more overhead). Repeating the prompt manually each time (error-prone, inconsistent). Keyboard text expanders (system-level, not context-aware). CLAUDE.md "task patterns" section (always loaded, wastes context on tasks not performed in the session).

## Potential Improvements
Add a command index file (`commands/_index.md`) listing all available commands with one-line descriptions. Support parameterized commands (e.g., `/project-status [project-name]`) by using template placeholders that Claude fills from context. Auto-complete command names in the terminal via shell tab-completion (would require a wrapper script).

## Potential Failure Modes
Commands/ folder discovery requires Claude to know the folder exists — if not mentioned in CLAUDE.md, Claude won't find it on first invocation. Command files can become stale if vault conventions change but commands aren't updated. Command names that clash with Claude built-in slash commands may cause unexpected behavior.
