---
name: "DeerFlow"
type: "watched-library"
repo_url: "https://github.com/bytedance/deer-flow"
description: "Super agent harness — LangGraph-based runtime with sub-agent orchestration, integrated sandbox execution (local/Docker/K8s), long-term memory, extensible skills, MCP support, multi-channel messaging (Telegram/Slack/Feishu/WeChat)"
spectrum_position: "cherry-pick"
what_we_use: "Sub-agent orchestration patterns, sandbox provisioner architecture (local→Docker→K8s), long-term memory integration, multi-channel messaging adapter pattern, LangGraph-based agent runtime"
local_derivations: []
last_evaluated_version: "v2.0"
last_evaluated_date: "2026-04-19"
maintainer: "bytedance"
status: "active"
tags:
  - "orchestration"
  - "agent-design"
  - "sandboxing"
  - "memory"
  - "langgraph"
  - "multi-channel"
related_findings: []
related_sources: []
date_added: "2026-04-19"
---

## What It Does

An open-source super agent harness from ByteDance that orchestrates sub-agents, memory, and sandboxes for complex task execution. Ground-up v2.0 rewrite. LangGraph-based agent runtime with optional Gateway mode. Integrated sandbox execution across local, Docker, and Kubernetes via a provisioner pattern. Long-term memory with configurable storage. Extensible skills and tools framework with MCP server support. Multi-channel messaging (Telegram, Slack, Feishu, WeChat, WeCom). Supports multiple LLM providers (OpenAI, Claude, DeepSeek, Qwen). Python backend + Node.js frontend.

Key capabilities:
- **Sub-agent orchestration**: Lead agents route to specialist sub-agents
- **Sandbox provisioner**: Graduated isolation — local → Docker → Kubernetes
- **Long-term memory**: Configurable persistent memory across sessions
- **MCP support**: Model Context Protocol server integration
- **Multi-channel**: Unified messaging across Telegram/Slack/Feishu/WeChat/WeCom
- **LangGraph runtime**: Graph-based agent execution with state management

## What We Use From It

Cherry-pick patterns:
1. **Sub-agent orchestration** — lead agent → specialist routing with LangGraph state management
2. **Sandbox provisioner** — graduated isolation levels (local, Docker, K8s) behind a unified interface
3. **Multi-channel adapter** — unified messaging interface across 5+ platforms
4. **Memory integration** — long-term memory as a first-class agent capability
5. **Skills framework** — extensible skill registry with tool binding

## Spectrum Rationale

**Cherry-pick** — DeerFlow is a full agent platform (frontend, backend, messaging, sandbox). MetaSystem doesn't need the platform but can learn from its orchestration patterns, sandbox provisioner architecture, and how it integrates LangGraph with sub-agents and memory. At 62.7k stars it's the most popular repo in this batch.

## Change Signals

Watch for:
- Sub-agent routing and orchestration changes
- Sandbox provisioner evolution
- Memory architecture updates
- New skill framework patterns
- MCP integration depth
