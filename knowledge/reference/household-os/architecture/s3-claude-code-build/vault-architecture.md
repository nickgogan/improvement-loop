---
notion_id: 32b1e08b-9b34-81a8-87b8-ecbb6eb86018
title: "Vault Architecture"
parent: "S3: Claude Code Build Architecture"
extracted: "2026-04-04"
---

# Vault Architecture

> **For agents:** This page defines the three-tier vault architecture for the Claude Code Build system (S3). For the governing system boundaries, see Constitution. For S3's skill definitions, see S3 Skill Catalog.

---

This page is a placeholder. It will be populated when the vault architecture decisions are formalized as Design Decisions. Expected content:

- Three-tier vault model:
  - **Tier 1 (Global):** ~/.claude/ — shared across all projects. Contains bootstrap, resume, compress, preserve skills.
  - **Tier 2 (Project-shared):** Git-tracked project files. Shared between Nick and JR.
  - **Tier 3 (Personal):** Gitignored personal configuration. User-specific overrides.
- File organization within each tier
- What lives where and why
- Interaction rules between tiers
