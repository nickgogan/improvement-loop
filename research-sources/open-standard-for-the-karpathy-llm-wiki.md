---
name: "Finally, an Open Standard for the Karpathy LLM Wiki is HERE"
source_type: "Video"
status: "Done"
key_takeaways: |-
  Cole Medin positions OKF as the missing standard for the Karpathy LLM wiki: everyone
  is building bespoke wikis that other people's agents can't consume — different
  metadata fields, folder layouts, and linking conventions compound into
  non-interoperability. OKF standardizes exactly two things (how information is
  organized, and the metadata fields), and that minimalism is the point. Framing: "what
  MCP did for agent-to-tool communication, OKF does for agent-to-knowledge-base
  communication" — a standard for both consuming and producing knowledge bases.
  Adoption mechanics demonstrated: paste spec.md into a coding agent to one-shot a
  conformant KB or refactor an existing one (subagent-parallelized for large KBs);
  multi-bundle management via a top-level document plus per-bundle indexes (two-tier
  indexing) and a thin CLI (list bundles, view index, read by bundle + concept ID);
  shareable bundles as a distribution format (he ships his videos as an OKF bundle
  anyone can drop into their second brain). Honest caveats: the "too simple" critique,
  and his own bet that OKF itself may not win but something shaped like it will.
relevance: "High"
added_by: "Nick"
tags:
  - "context-engineering"
  - "vault-architecture"
  - "memory"
url: "https://www.youtube.com/watch?v=T33iI6izAKw"
authority:
  - "cole-medin.md"
findings:
  - "okf-open-knowledge-format-curated-bundle-spec.md"
  - "knowledge-substrate-standardization-cross-agent-interop.md"
  - "karpathy-llm-knowledge-base-obsidian-rag.md"
date_added: "2026-07-12"
date_processed: "2026-07-12"
date_published: "2026-07-02"
---

# Finally, an Open Standard for the Karpathy LLM Wiki is HERE (Cole Medin)

Pass 2 deep extraction completed 2026-07-12 from cached transcript
(`app/transcript-fetcher/transcripts/T33iI6izAKw.md`). Densest video in the OKF
cluster and the one that raises the engine-facing architecture question (KB
conformance/exportability) captured in the substrate-standardization finding.
