---
title: "Claude Code Channels: Messaging Apps as Agent Interface"
type: "extracted-artifact"
assigned_form: "skill"
source_finding: "claude-code-channels-telegramdiscord-as-agent-inte"
extraction_date: "2026-05-25"
last_change_session: 94
last_change_sl: "session-94-codifier-extract-non-pattern-artifacts"
identification_report: "2026-05-24-identification-report-2.md"
deployed: false
deployed_to: null
context:
  applies_to:
    - "Developers or operators who run long-duration agentic tasks and need to dispatch them from a mobile device without being at a desktop"
    - "Teams building async workflows where tasks are triggered on demand and results are consumed in a chat interface rather than a terminal"
    - "Projects that want to expose a Claude Code agent as the backend for a lightweight custom UI, with the UI sending user interactions as task messages"
    - "Anyone needing a quick integration between an existing messaging workflow and an AI coding agent using officially supported plugin infrastructure"
  platform_coupling: "specific:claude-code"
  autonomy: "all"
  stage: "operate"
  reversibility: "low — channel configuration is a one-time setup; reverting requires revoking the bot token and removing the plugin configuration"
  auditability: "Medium — message history in the messaging app provides a log of dispatched tasks and results; sender allowlist is externally verifiable"
  evidence_strength: "Strong"
  adoption:
    status: "Not Yet Started"
    notes: null
contract:
  preconditions: "A bot token is obtained from the messaging platform. Sender allowlist is configured before the channel is opened. Claude Code is installed and can be started with --channels. The host machine will remain awake for the expected task duration."
  invariants: "Sender allowlist is non-empty at all times. Every inbound message is processed or explicitly rejected, never silently dropped. Bot tokens are stored outside source control."
  governance: "Owner: whoever operates the Claude Code session. Sender allowlist is the security perimeter and is owner-authorized. Custom plugin deviations from the channel plugin interface are owner risk."
  recovery: "Machine sleeps mid-task: restart with channel plugin and replay task. Git conflict detected: halt commits, resolve manually. Unauthorized sender received: log, reject, rotate token if compromise suspected."
tags:
  - "extracted-artifact"
  - "skill"
---

# Claude Code Channels: Messaging Apps as Agent Interface

**Source:** [[claude-code-channels-telegramdiscord-as-agent-inte]]
**Form:** skill
**Extraction date:** 2026-05-25

An officially supported Claude Code plugin system that creates a bidirectional channel between a messaging app (Telegram, Discord, or a custom plugin) and a running Claude Code session. Incoming messages dispatch tasks to the agent; outgoing messages deliver results and files back to the user. Enables asynchronous, mobile-triggered agentic workflows without requiring desktop presence.

## Inputs

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| `channel_type` | enum | Yes | `telegram`, `discord`, or `custom`. Determines which plugin is loaded. |
| `bot_token` | string | Yes (telegram/discord) | API token for the bot. For Telegram: obtained from BotFather. |
| `sender_allowlist` | array[string] | Yes | Authorized sender IDs or usernames. Messages from unlisted senders are rejected. |
| `task_message` | string | Yes | The message the user sends to dispatch a task. |
| `claude_code_session` | running process | Yes | A Claude Code session started with `--channels plugin:<channel>@<plugin-source>`. |

## Outputs

| Output | Type | Description |
|--------|------|-------------|
| `task_result` | string/file | The agent's response delivered as a message or attached file in the messaging app. |
| `delivery_receipt` | implicit | Messaging app delivery confirmation (inherent to Telegram/Discord transport). |

## Steps

### Step 1: Bot Setup (one-time)
- **Telegram:** Open BotFather, run `/newbot`, copy the API token.
- **Discord:** Create an application in the Discord Developer Portal, create a bot user, copy the token.
- **Custom plugin:** Implement the Claude Code channel plugin interface. Host the artifact on a local port.

### Step 2: Configure the Channel in Claude Code
- Run the configuration command in the Claude Code session:
  - Telegram: `/telegram:configure <token>`
  - Discord: `/discord:configure <token>`
- Set the `sender_allowlist` to restrict which senders can dispatch tasks.

### Step 3: Launch Claude Code with the Channel Plugin
- Start Claude Code with the channels flag:
  `claude --channels plugin:telegram@claude-plugins-official`
  (Substitute the plugin identifier for discord or custom plugins.)
- Confirm the bot is live and listening in the messaging app.

### Step 4: Dispatch Tasks Asynchronously
- Send a message from an allowlisted sender in the messaging app.
- Claude Code receives the message as a new task input and executes the task.

### Step 5: Receive Results
- Claude Code sends the result back as a message or file attachment in the same channel.
- For custom plugins: the result can trigger downstream actions (e.g., update an artifact, hot-reload a UI).

### Step 6: Custom Frontend Pattern (Advanced)
- Build a local HTML artifact on a local port as the custom channel.
- Users interact in the artifact UI (e.g., pinning a comment).
- Each pinned comment is sent to Claude Code as a task message.
- Claude Code queries MCP servers, modifies the artifact file, and the browser hot-reloads.
- Result: the artifact becomes a custom frontend; Claude Code is the backend.

## Failure Modes

| Failure | Detection | Recovery |
|---------|-----------|----------|
| Machine sleep/lock stops the agent | Task messages received but not processed; no response delivered | Keep machine awake; use a server or CI runner for long-running tasks |
| Git conflicts (two machines committing) | Merge conflict in version-controlled output files | Enforce single-machine per session; or use branch-per-task strategy |
| Unauthorized sender exploits open channel | Messages from non-allowlisted senders trigger execution | Always configure sender allowlist before going live; missing allowlist is a blocking misconfiguration |
| Bot token exposure | Token leaked via logs, messages, or source control | Store tokens in env vars or secrets manager; rotate on suspected exposure |

## Contract

### Preconditions
A bot token is obtained from the relevant messaging platform. A sender allowlist is configured before the channel is opened to any messages. Claude Code is installed and a session can be started with the `--channels` flag. The machine running Claude Code will remain awake for the expected task duration.

### Invariants
Sender allowlist is non-empty; no open-access channels. Every inbound message is either processed by Claude Code or explicitly rejected — not silently dropped. Bot tokens are stored outside source control and not echoed in task results.

### Governance
Owner: whoever operates the Claude Code session. Sender allowlist is the security perimeter; its contents are owner-authorized. Custom plugin implementations must conform to the channel plugin interface contract.

### Recovery
If the machine sleeps mid-task: restart Claude Code with the channel plugin; replay the task message. If a git conflict is detected: halt further commits from this session, resolve manually, then resume. If an unauthorized sender message is received: log the attempt, do not process, rotate the bot token if compromise is suspected.
