---
notion_id: 32b1e08b-9b34-810c-a70d-feceedcb4b6e
name: 'Skills Migration: Claude Code to Co-work for Dispatch Compatibility'
summary: Claude Code skills (markdown SOP files stored in the .claude/skills folder) can be copied to a Claude Co-work skills folder, making them available for execution via Dispatch from a mobile device.
  This enables mobile-triggered execution of workflows originally built in the Claude Code IDE environment.
implementation_notes: null
category: Tool Integration
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
priority: P3
applicability:
- S3 (Claude Code Build)
adopted_in: null
sources:
- claude-codes-leak-changes-everything.md
proposals: null
date_discovered: '2026-03-22'
last_updated: '2026-04-19'
related_findings:
- file: multi-ide-portability-via-installer-templates.md
  rel: same-problem
pipeline_status: raw
consumed_by: []
---
# Skills Migration: Claude Code to Co-work for Dispatch Compatibility

## What It Is
Skills developed in Claude Code live in a hidden .claude/skills directory. The user can duplicate these files to a cloud/skills folder (or equivalent Co-work skills directory) and then instruct Co-work to import them. Once imported, these skills appear as selectable tasks in the Co-work interface and become triggerable via Dispatch from the mobile app. The author demonstrates this for lead scrapers, inbox cleaners, and thumbnail generation workflows.

## Why It Matters
Developers who build and test sophisticated skills in Claude Code's IDE environment can now operationalize them as mobile-accessible automation without rebuilding the skills in a different format. This preserves investment in Claude Code skill development while unlocking the mobility and accessibility of Dispatch.

## Why People Are Using It
Power users who develop skills in Claude Code (with full IDE capabilities) but want to run them asynchronously or on-the-go without being tethered to their IDE. Bridges the gap between the developer-focused Claude Code environment and the more accessible Co-work interface.

## Potential Alternatives
Rebuilding skills natively in Co-work from scratch; using Claude's API directly with a mobile client; OpenClaw's skill/SOP system.

## Potential Improvements
Automated sync between Claude Code skills and Co-work skills folders would eliminate the manual copy step. Version control for skills shared across Co-work and Code would prevent divergence.

## Potential Failure Modes
Skills built with Claude Code-specific features (file system navigation, IDE-specific context) may not execute identically in Co-work. Relative path references in skills may break when moved between environments.
