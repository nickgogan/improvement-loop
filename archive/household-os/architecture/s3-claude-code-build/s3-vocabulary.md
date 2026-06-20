---
notion_id: 32b1e08b-9b34-8125-a16b-e6023e4f23ba
title: "S3 Vocabulary"
parent: "S3: Claude Code Build Architecture"
extracted: "2026-04-04"
---

# S3 Vocabulary

> **For agents:** This page defines terms specific to the Claude Code Build system (S3). For cross-system terms, see Governance Vocabulary.

---

| Term | Definition |
|---|---|
| **Vault** | The file-based configuration system for Claude Code. Organized in three tiers. |
| **Tier 1 (Global)** | ~/.claude/ directory. Skills and configuration shared across all projects. |
| **Tier 2 (Project-shared)** | Git-tracked project files. Shared between all project contributors. |
| **Tier 3 (Personal)** | Gitignored personal configuration. User-specific overrides and preferences. |
| **Build Spec** | A specification document that S3 uses to execute schema changes against S1. Includes review gates. |
| **Review Gate** | A checkpoint in the S3 build process where Nick reviews and approves changes before they are applied. |
| **CLAUDE.md** | The primary configuration file for Claude Code sessions. Contains project context, rules, and skill references. |
| **Parameterized Bootstrap** | The `/bootstrap` skill's ability to accept a parameter (`household` or `generic`) to determine which project context to load (DD-34). |
| **Memory System** | The /resume + /compress + /preserve pattern providing session continuity across Claude Code sessions (DD-34). |
| **Tier Precedence** | The override rule for vault tiers: lower tiers override higher tiers (Tier 3 > Tier 2 > Tier 1) (DD-33). |
| **Skill File** | A SKILL.md file defining a Claude Code skill's name, command, parameters, execution instructions, context requirements, and output specification (DD-34). |

*For cross-system terms (DD, IB, Human Gate, etc.), see Governance Vocabulary.*
