---
name: "Give Your AI Agent a Second Brain (Gbrain + Hermes Agent)"
source_type: "Video"
status: "Done"
key_takeaways: |-
  Tonbi's AI Garage installs and tests Gbrain (Garry Tan's MIT-licensed, 25k-star
  world-knowledge base) with Hermes Agent. Cleanest boundary taxonomy in the batch:
  agent memory remembers conversations, LLM wikis know domains, a world-KB knows your
  world (things that never touched chat). Architecture: markdown-in-git as system of
  record, synced to a derived in-process PG lite database with hybrid search (vector +
  keyword + self-wiring knowledge graph — claimed +31 points precision over vector-only
  RAG), exposed as 30+ typed tools over a local MCP stdio subprocess. Concrete
  MCP-subprocess-vs-CLI-shell-out tradeoff for stateful tools, and a write-back
  discipline ("memory is not the brain" — durable decisions become brain pages, world
  facts go to the KB, everything cited).
relevance: "High"
added_by: "Nick"
tags:
  - "memory"
  - "vault-architecture"
  - "mcp"
  - "tools"
url: "https://www.youtube.com/watch?v=-fSjdYzrFvA"
authority:
  - "tonbis-ai-garage.md"
findings:
  - "memory-wiki-world-kb-trichotomy.md"
  - "markdown-git-system-of-record-derived-disposable-db.md"
  - "stateful-mcp-subprocess-vs-cli-shell-out.md"
  - "write-back-discipline-memory-is-not-the-brain.md"
date_added: "2026-07-12"
date_processed: "2026-07-12"
date_published: "2026-07-07"
---

# Give Your AI Agent a Second Brain (Gbrain + Hermes Agent)

First-use walkthrough of Gbrain with Hermes Agent: install via agent-pasted markdown
instructions (bun; separate embeddings API key required — agent OAuth does not carry
over), seed, query with cited sources, graph queries from zero-LLM-call typed-edge
extraction, then MCP server setup and a decision written back from chat into the brain.

Roster note: Gbrain is a watched-libraries CANDIDATE (Nick-gated; zero KB coverage
before this source).

Pass 2 deep extraction completed from full transcript (453 segments, 15:20).
