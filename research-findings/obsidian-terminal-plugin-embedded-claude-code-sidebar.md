---
name: Obsidian Terminal Plugin for Embedded Claude Code Sidebar
summary: The "Terminal" community plugin (100k+ downloads) embeds a full terminal inside Obsidian, allowing Claude Code to run as a sidebar panel alongside notes. Claude launches directly inside the open vault — no drag-and-drop folder setup needed. Enables session naming, crash recovery via --resume, and side-by-side note editing with AI.
implementation_notes: This is the integration point for the "Claude Code inside Obsidian" workflow. Relevant if MetaSystem ever uses Obsidian as a primary interaction surface rather than a separate terminal.
category: Tool Integration
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
priority: P3 (Monitor)
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources:
- obsidian-claude-code-setup-terminal-integration.md
- claude-code-obsidian-second-brain-project-onboarding.md
related_findings:
- file: cursor-claude-code-ide-composition.md
  rel: same-problem
- file: obsidian-as-transparent-frontend-vs-rag-black-box.md
  rel: extends
- file: session-persistence-crash-resilient.md
  rel: extends
proposals: null
date_discovered: '2026-04-19'
last_updated: '2026-04-19'
pipeline_status: raw
consumed_by: []
---
# Obsidian Terminal Plugin for Embedded Claude Code Sidebar

## What It Is
The **Terminal** community plugin (Settings → Community Plugins → browse "Terminal") adds a terminal icon to Obsidian's sidebar. Clicking it opens an integrated terminal panel within the Obsidian window. Key behaviors:

- **Vault-aware launch**: When the terminal opens inside an active vault, launching `claude` automatically starts Claude Code inside that vault directory — no manual `cd` or folder drag-and-drop needed.
- **Sidebar positioning**: The terminal panel can be docked to the left or right sidebar, letting the user view and edit notes in the main pane while Claude Code runs in the terminal alongside.
- **Tab switching**: Multiple notes can be open in the main pane; the user can switch between them with Cmd+click while Claude continues working in the terminal.
- **Session naming**: `/rename` command renames the current session so sessions are identifiable after a crash.
- **Crash recovery**: If Claude crashes (which can happen when it triggers an Obsidian reload), `claude --resume` inside the terminal picks up the last session. The `--resume` flag restores context without requiring the user to re-explain the task.
- **Permission modes**: `claude --dangerously-skip-permissions` skips per-file confirmation prompts; Shift+Tab cycles between full-auto, auto-accept-edits, and plan-only modes within the session.

Setup requires Obsidian version 1.12.7+ (which installs the Obsidian CLI). The CLI provides Claude with structured commands for reading, writing, and manipulating vault files more efficiently than raw filesystem operations.

## Why It Matters
Running Claude Code in a separate terminal window requires constant context switching between the terminal and Obsidian to verify changes. Embedding the terminal inside Obsidian collapses this to a single window. The sidebar layout mirrors VS Code's pattern of running Claude Code in the integrated terminal while editing code — except here the "code" is your knowledge base.

The vault-aware launch is non-trivial: it eliminates the common mistake of launching Claude in the wrong directory (e.g., home directory instead of vault root), which causes Claude to create files in unexpected locations.

## Why People Are Using It
The B35SWx_4BNM video demonstrates the full workflow: install plugin, position terminal in sidebar, launch Claude, run `/init` to register the vault environment, then work interactively with notes. The creator explicitly says the goal is "the feeling that Claude is working with me inside" — the same reason developers prefer VS Code's integrated terminal over a separate terminal window.

## Potential Alternatives
External terminal with `cd` to vault root. VS Code with Claude Code extension (same terminal-in-editor pattern but not Obsidian-native). The Obsidian community "Cursor" plugin (if it exists). Running Claude Code via CLAUDE.app in Cursor (different mental model entirely).

## Potential Improvements
Add a keyboard shortcut to focus the terminal panel without the mouse. Support for split-terminal (multiple Claude sessions in parallel panels within Obsidian). Display the current session name and context usage in the Obsidian status bar.

## Potential Failure Modes
Claude triggering an Obsidian vault reload (via certain CLI commands) kills the terminal session. The `--resume` recovery path works but loses any unsaved state. Plugin updates may change terminal behavior. The dangerously-skip-permissions flag removes all safety checks — inappropriate for vaults with sensitive content.
