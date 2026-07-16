---
name: Credential Setup Outside the LLM Context Window
summary: Archon's setup wizard detects when API keys need to be entered and spawns a separate terminal process for credential entry. The coding agent guides the user through setup but never sees the actual
  credentials. This prevents API keys from entering the LLM's context window, where they could be logged, cached, or exposed via prompt injection.
implementation_notes: null
category: Governance
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources:
- archon-open-source-harness-builder.md
related_findings:
- file: credential-isolation-bundled-auth-vault-proxy.md
  rel: same-problem
- file: tiered-permission-system-bash-safety.md
  rel: same-problem
proposals: null
date_discovered: '2026-05-25'
last_updated: '2026-05-25'
pipeline_status: synthesized
consumed_by:
- extracts/rules/credential-setup-outside-llm-context-window.md
- agent-safety-and-permissions.md
tags:
- session-95-reextract
---

## What It Is

During Archon's guided setup, when the user needs to enter API keys for platforms (GitHub, Slack, Telegram, Anthropic), the system spawns a **separate terminal process** for credential entry. The Claude Code session orchestrates the setup flow (asking what platforms to configure, what database to use, etc.) but explicitly does not handle the credentials step. Cole Medin explains: "We need to do this in a different window, because we don't want to send our API keys directly into Claude Code."

The separate terminal runs `archon setup`, a locally-installed CLI command that walks through credential entry in a standard terminal — no LLM involved. After credentials are stored, the user returns to the Claude Code session and says "done," and the setup skill validates the connections without reading the actual credentials.

## Why It Matters

Any text entered into a coding agent session becomes part of the LLM context. API keys pasted into Claude Code are sent to Anthropic's API, logged in conversation history, and potentially exposed if the session is shared or if a prompt injection attack extracts context. The separate-terminal pattern creates a hard architectural boundary: credentials flow through a local CLI, never through the LLM.

This is a lighter-weight version of the "vault proxy" pattern documented in the credential-isolation finding. The vault proxy requires infrastructure (a proxy service, credential storage); the separate-terminal approach requires only that the credential entry happens outside the LLM session. Both achieve the same goal: keeping secrets out of the model's context.

## Why People Are Using It

Cole Medin demonstrates the full setup flow, showing the automatic terminal spawn for credential entry and the return to the Claude Code session for validation. The pattern is built into Archon's setup skill, not a user discipline — it's enforced by the tool architecture.

## Potential Improvements

- Encrypted credential storage with key rotation
- Credential health checks that run periodically without exposing the actual keys
- Credential scoping per workflow (some workflows may only need GitHub access, not Slack)

## Potential Failure Modes

- On some operating systems (VPS, headless environments), the automatic terminal spawn may fail, requiring manual terminal opening
- Users who bypass the setup wizard and manually paste credentials into the Claude Code session
- Credential storage location may not be protected from other processes on the machine
