---
name: "AIO Sandbox"
type: "watched-library"
repo_url: "https://github.com/agent-infra/sandbox"
description: "All-in-one Docker sandbox for AI agent execution — unified browser, shell, file ops, VSCode, Jupyter, and MCP servers in a single container with shared filesystem"
spectrum_position: "evaluating"
what_we_use: "Sandboxing architecture patterns, MCP server integration in containers, multi-SDK approach (Python/TypeScript/Go), unified execution environment design"
local_derivations: []
last_evaluated_version: "v1.0.0.150"
last_evaluated_date: "2026-04-19"
maintainer: "agent-infra"
status: "active"
tags:
  - "sandboxing"
  - "docker"
  - "mcp"
  - "execution-environment"
related_findings: []
related_sources: []
date_added: "2026-04-19"
---

## What It Does

An all-in-one Docker container combining browser (VNC + CDP), shell (WebSocket terminal), file operations, VSCode Server, Jupyter notebooks, and pre-configured MCP servers (browser, file, shell, markitdown) for AI agent execution. Single container with shared filesystem enables seamless workflows across all interfaces. Multi-language SDKs: Python (agent-sandbox on PyPI), TypeScript (@agent-infra/sandbox on npm), Go (sandbox-sdk-go). Designed for single-agent execution environments with safety guarantees via Docker isolation.

Key capabilities:
- **Unified container**: Browser + shell + files + IDE + notebooks in one image
- **MCP integration**: Pre-configured MCP servers for browser, file, shell, markitdown
- **Multi-SDK**: Python, TypeScript, Go SDKs for programmatic sandbox management
- **Browser automation**: Chrome DevTools Protocol + high-level MCP tools
- **Resource limits**: Configurable memory/CPU via Docker or Kubernetes

## What We Use From It

Evaluating patterns:
1. **All-in-one sandbox architecture** — single container with shared filesystem across multiple interfaces
2. **MCP server pre-configuration** — bundling MCP servers inside execution containers
3. **Multi-SDK sandbox management** — unified API across Python/TS/Go for sandbox lifecycle
4. **CDP + MCP browser tooling** — combining low-level browser protocol with high-level MCP abstraction

## Spectrum Rationale

**Evaluating** — MetaSystem doesn't currently use containerized execution, but as agent autonomy increases, sandboxing becomes critical. This repo represents the state of the art in unified agent execution environments. Worth monitoring for patterns that could inform future sandboxing decisions.

## Change Signals

Watch for:
- New MCP server additions
- Multi-agent support
- Security model changes
- Kubernetes deployment patterns
