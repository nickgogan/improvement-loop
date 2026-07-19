---
name: "From fork() to Fleet: Designing an Agent Sandbox Cloud"
source_type: "Video"
status: "Done"
key_takeaways: |-
  Abhishek Bhardwaj (OpenAI, RL and agent infrastructure) walks a first-principles
  sandbox-cloud architecture in three pillars — runtime, persistence, orchestration —
  built for ChatGPT and Codex Web at scale. The runtime/isolation ladder (fork/exec →
  containers → gVisor → hardware microVMs) corroborates and deepens ground this KB
  already covers well; the novel yield is concentrated in persistence and fleet
  orchestration: incremental copy-on-write block-level snapshotting with lineage
  chains, an always-on POSIX-compliant tiered-cache filesystem over object storage, and
  snapshot-lineage-aware scheduling for fast, locality-optimized sandbox restores
  across a fleet.
relevance: "High"
added_by: "Nick"
tags:
  - "sandboxing"
  - "infrastructure"
  - "orchestration"
url: "https://www.youtube.com/watch?v=OqM67QG_Ikk"
authority:
  - "abhishek-bhardwaj.md"
  - "ai-engineer.md"
findings:
  - "incremental-snapshotting-copy-on-write-block-diffing.md"
  - "posix-tiered-cache-persistence-over-object-storage.md"
  - "snapshot-lineage-aware-fleet-scheduling.md"
  - "sandbox-architecture-by-threat-model-microvm-vs-container.md"
date_added: "2026-07-18"
date_processed: "2026-07-18"
date_published: "2026-07-13"
---

Session-151 Pass 2 deep extraction (link-intake triage 2026-07-18, KB-ONLY verdict,
Nick-accepted, batch-b2). Transcript:
`app/transcript-fetcher/transcripts/OqM67QG_Ikk.md`. AI Engineer conference talk,
44:33, ~9.8k transcript tokens.

Per the triage report's own estimate ("novel only in persistence... isolation third
already covered"), the isolation/runtime section was checked against six existing
findings (`sandbox-architecture-by-threat-model-microvm-vs-container`,
`three-sandbox-architectures-comparison`, `all-in-one-sandbox-architecture`,
`three-tier-sandbox-provisioner`, `os-level-agent-sandboxing-filesystem-network-
isolation`, `borrowed-strongest-isolation-boundary-tenancy`) before extraction. The
fork/exec→container→gVisor→microVM ladder and its trade-offs are already KB ground;
this talk's delta there (Rust-VMM lineage, device-level jailing, concrete spin-up
mechanics, a third production corroboration at OpenAI scale, and the "seven stages of
grief / start with microVMs" practitioner heuristic) is staged as a surgical UPDATE to
`sandbox-architecture-by-threat-model-microvm-vs-container.md`, not a new finding — no
isolation ground was re-created. Persistence and orchestration yielded three new
findings, matching the ~3 prior.
