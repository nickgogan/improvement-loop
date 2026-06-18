---
notion_id: 3101e08b-9b34-810f-9b56-cbd331030cec
title: "External Content Index"
parent: "S2: Notion Operations Architecture"
extracted: "2026-04-04"
---

# External Content Index

> **For agents:** This page defines how Notion maintains its role as index-of-record when content lives outside Notion. When creating or referencing items stored in Google Drive, Heptabase, or the Archive SSD, always create the corresponding Notion index entry. Notion must know *about* everything even when it doesn't *contain* everything.

---

## Core Decision

**DD-22:** Notion is the Single Source of Truth (SSOT) for the Household Operating System. When content must live outside Notion — in Google Drive, Heptabase, or the Archive SSD — Notion maintains an index entry with metadata and a pointer to the external location. Three mechanisms serve this purpose: Drive Index database, Archive Index database, and Heptabase Reference Note stubs.

---

## The Principle

**Notion knows about everything, even when it doesn't contain everything.**

Some content legitimately belongs outside Notion:

- **Google Drive** — Shared documents, spreadsheets, PDFs, photos, receipts (collaborative editing, file storage)
- **Heptabase** — Deep synthesis, evergreen notes, complex thinking (spatial canvas, linked atomic notes)
- **Archive SSD** — Cold storage files no longer actively needed (old projects, tax records, media backups)

For each external destination, Notion holds a lightweight index entry: enough metadata to discover, classify, and retrieve the content without opening the external tool.

---

## Three Index Mechanisms

| Mechanism | External Destination | Notion Artifact | Scope |
|-----------|---------------------|-----------------|-------|
| **Drive Index** | Google Drive | Dedicated database | Area-scoped: files in Area folders |
| **Archive Index** | Archive SSD | Dedicated database | All archived files |
| **Heptabase Stubs** | Heptabase | Notes database entries | Per-card or per-whiteboard |

---

## 1. Drive Index Database (NEW)

A dedicated Notion database cataloging files stored in Google Drive, scoped to Area folders.

### Design Rationale

Google Drive is the household's shared file storage. Each PARA Area has a corresponding folder in Drive (e.g., `Finances/`, `Health/`, `Legal/`). Files within these Area folders are significant enough to track — they're part of the household's managed knowledge. Files outside Area folders (random downloads, one-off shares) don't need indexing.

### Schema

| Property | Type | Description |
|----------|------|-------------|
| **Name** | Title | File name or descriptive title |
| **Drive URL** | URL | Direct link to the file in Google Drive |
| **File Type** | Select | Document, Spreadsheet, PDF, Photo, Receipt, Presentation, Other |
| **Area** | Relation → Tags | Links to the PARA Area this file belongs to |
| **Status** | Select | Active, To Archive, Archived |
| **Owner** | Select | Nick, John, Household |
| **Date Added** | Date | When the file was indexed |
| **Notes** | Text | Brief description or context |
| **Related Project** | Relation → Projects | Optional link to the Project this file serves |

### Lifecycle

```
File created in Drive Area folder
    |
    +-- Create Drive Index entry (Status = Active)
    |
    +-- File is actively used ---------> Status stays Active
    |
    +-- File no longer needed ---------> Mark Status = To Archive
    |                                    (flagged for next archive batch)
    |
    +-- File moved to Archive SSD -----> Update Status = Archived
                                         Create Archive Index entry
                                         Update Drive Index with archive path
```

### Granularity Rule

**Index files in Area folders. Skip everything else.** The Drive Index tracks files that are part of the household's managed knowledge — budget spreadsheets, lease agreements, medical records, project deliverables. Random photos, temporary downloads, and one-off shares don't get indexed unless they're moved into an Area folder.

### Review Integration

During The Compass review cadences (DD-18):

- **Monthly Audit:** Spot-check Drive Index against actual Drive contents for one Area
- **Quarterly Deep Review:** Full reconciliation of Drive Index vs Drive for all Areas. Flag stale entries, missing files, and items marked "To Archive"

---

## 2. Archive Index Database (Enhanced from DD-17)

DD-17 (Reference Libraries) already specified the Archive (SSD) database as one of six Reference Libraries. DD-22 enhances this by connecting it to the broader External Content Index principle and defining the lifecycle integration with Drive Index.

### Schema (from DD-17, unchanged)

| Property | Type | Description |
|----------|------|-------------|
| **Name** | Title | File or folder name |
| **File Type** | Select | Document, Spreadsheet, Photo, Video, Audio, Archive, Other |
| **Category** | Select | Tax Records, Project Archive, Media, Personal, Legal, etc. |
| **Owner** | Select | Nick, John, Household |
| **Path** | Text | File path on the SSD |
| **Date Archived** | Date | When the file was moved to the SSD |
| **Size** | Text | File size (approximate) |
| **Source Area** | Relation → Tags | The Area this file originally belonged to |
| **Original Drive URL** | URL | If migrated from Drive, the original location |

### Integration with Drive Index

When a file moves from Google Drive to the Archive SSD:

1. Update the Drive Index entry: Status → Archived
2. Create an Archive Index entry with the SSD path
3. Optionally link the two entries via the Original Drive URL property

This creates a traceable chain: the system knows where the file *was* (Drive) and where it *is now* (SSD).

---

## 3. Heptabase Reference Note Stubs

Unlike Drive and Archive content (which get dedicated databases), Heptabase content is indexed via **Reference Notes** in the existing Notes database. This is because Heptabase content is *knowledge* — it belongs in the same semantic space as other Notes.

### Pattern

When an item is routed to Heptabase during inbox processing (DD-21):

1. Create or keep the Note in the Notes database
2. Set **Type = Reference**
3. Add **Tag = Heptabase** (or a dedicated "Heptabase" label)
4. Add a **URL property** pointing to the Heptabase card or whiteboard
5. Write a brief summary in the Note body — enough context to understand what the Heptabase content is about without opening Heptabase

### What This Enables

- **Discoverability:** Searching Notion for a topic surfaces the Reference Note, which points to the deeper Heptabase content
- **Relational links:** The Note can relate to Projects, Areas, and other Notes within Notion's relational graph
- **The Compass visibility:** Heptabase content appears in review cadences through its Notion stub
- **Agent awareness:** AI agents can see that deep synthesis exists on a topic without needing Heptabase access

### Granularity Rule

Not every Heptabase card needs a Notion stub. Create stubs for:

- **Whiteboards** that represent significant thinking sessions
- **Evergreen notes** that have matured into reusable knowledge
- **Cards** that relate to active Projects or Areas

Fleeting notes and work-in-progress thinking in Heptabase don't need Notion stubs until they've been distilled into something worth indexing.

---

## Unified Discovery

The External Content Index ensures that when reviewing an Area, all related content is visible regardless of where it lives:

| Content Location | How It Surfaces in Area View |
|-----------------|----------------------------|
| Notion (Tasks, Notes, Projects) | Direct relation to Area Tag |
| Google Drive | Drive Index entries related to Area Tag |
| Archive SSD | Archive Index entries related to Source Area |
| Heptabase | Reference Note stubs related to Area Tag |

This means asking "show me everything about Finances" returns Tasks, Notes, Projects, Drive files, archived files, and deep thinking — all from Notion.

---

## Relationship to Existing Decisions

| DD | Relationship |
|----|-------------|
| **DD-02 (PARA)** | Areas provide the organizational scope for Drive Index and Archive Index |
| **DD-14 (UB3 Integration)** | Notes database hosts Heptabase Reference Note stubs |
| **DD-17 (Reference Libraries)** | Archive (SSD) database is enhanced with lifecycle integration |
| **DD-21 (Capture-to-Action)** | Processing phase routes items to external destinations; this DD defines the backlink pattern |
| **DD-18 (The Compass)** | Review cadences include Drive Index reconciliation checks |
| **DD-11 (System Log)** | Archive migrations and index creation are logged |

---

## WS2 vs Later Scope

| WS2 (Now) | WS3+ (Later) |
|-----------|-------------|
| Drive Index database schema defined | Automated Drive → Notion sync |
| Manual index entry creation | Agent creates entries on file upload |
| Archive Index enhanced with Source Area | Batch archive workflow with Drive Index integration |
| Heptabase Reference Note pattern documented | Heptabase API integration for auto-stub creation |
| Area-scoped granularity rule | Full-text search across external content via stubs |

---

*See also: Capture-to-Action Pipeline · Reference Libraries · The Compass · Vocabulary*
