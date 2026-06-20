---
notion_id: "32b1e08b-9b34-813a-8096-fafec33b8e61"
title: "S3: Claude Code Build Architecture"
parent: "Architecture"
extracted: "2026-04-04"
---

> **For agents:** S3 is the builder system. It produces the schema that S2 consumes. S3 does not operate S2 -- Nick bridges feedback from S2 to S3. Key concepts: three-tier vault architecture (Tier 1 global, Tier 2 project-shared, Tier 3 personal), skill-based Claude Code architecture.

The builder system -- vault architecture, skill definitions, and schema modification workflows. S3 produces the schema that S2 consumes.

## Infrastructure

[Vault Architecture](32b1e08b-9b34-81a8-87b8-ecbb6eb86018)

[S3 Skill Catalog](32b1e08b-9b34-8143-8bc8-dcaa55518f91)

[S3 Vocabulary](32b1e08b-9b34-8125-a16b-e6023e4f23ba)

## Design Decision Specs

Per DD-43, S3 DD spec pages (DD-33, DD-34) now live in the DD database page bodies -- query the [Design Decisions](https://www.notion.so/cffef89836724e29822ec894594752bc) database with `Target System = "S3: Claude Code Build"` to find them.

## Child Pages Not Extracted

The following child pages under S3: Claude Code Build Architecture were not included in this extraction:

- **Vault Architecture** (32b1e08b-9b34-81a8-87b8-ecbb6eb86018)
- **S3 Skill Catalog** (32b1e08b-9b34-8143-8bc8-dcaa55518f91)
- **S3 Vocabulary** (32b1e08b-9b34-8125-a16b-e6023e4f23ba)
