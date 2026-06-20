---
notion_id: 3101e08b-9b34-81e8-abb9-e234ea6a0dc0
title: "Reference Libraries"
parent: "S2: Notion Operations Architecture"
extracted: "2026-04-04"
---

# Reference Libraries

> **For agents:** Reference Libraries are the PARA Resources layer — structured catalogs of things the household owns, consumes, or stores. When answering questions like "do we have a stand mixer?", "what's on the SSD about taxes?", or "what business ideas have we explored?", query the appropriate library below. Recipes and Books are existing UB3 databases; Archive, Clarkson Storage, Clarkson Active, and Business Ideas are new catalogs.

---

## Purpose

Reference Libraries answer **"what do we have?"** across six domains. They are not action-oriented (no tasks or deadlines) — they are the stable knowledge layer that other system components query.

| PARA Element | Reference Libraries Role |
|-------------|------------------------|
| Projects | Projects may query libraries (e.g., a renovation project checks Clarkson Active for existing furniture) |
| Areas | Areas own libraries (e.g., Household Area owns Clarkson Active; Health & Wellness may query Recipes) |
| Resources | **This is the Resources layer.** Libraries ARE the structured resources. |
| Archives | The Archive (SSD) library catalogs what's been archived. Clarkson Storage catalogs physical items in long-term storage. |

---

## The Six Libraries

### 1. Recipes (Existing UB3 Database)

**Status:** Live — no changes needed
**Database:** UB3 Recipes
**Key properties:** Name, Chef Name, Meal Time, Prep/Cook Time, Favorite, Tags, URL
**Answers:** "What should we make for dinner?" "Any quick breakfast recipes?" "What are our favorite meals?"

---

### 2. Books (Existing UB3 Database)

**Status:** Live — no changes needed
**Database:** UB3 Books
**Key properties:** Title, Author, Status, Rating, Genres, Owned Formats, Shelf, Reading Log
**Answers:** "What should I read next?" "Have we read anything by this author?" "What are our favorite books?"

---

### 3. Archive (SSD) — NEW

**Status:** Design complete — not yet built
**Purpose:** Catalog of digital files stored on the external SSD. Enables finding files without plugging in and browsing.

**Schema (Basic):**

| Property | Type | Options / Notes |
|----------|------|----------------|
| Name | Title | Descriptive name of file or file group |
| File Type | Select | Document, Photo, Video, Audio, Backup, Project Archive, Software |
| Category | Select | Finances, Legal, Career, Health, Household, Personal, Creative |
| Owner | Select | Nick, JR, Household |
| Path | Text | Folder path on SSD (e.g., /Backups/2024/Taxes) |
| Date Archived | Date | When the file was moved to the SSD |
| Size | Text | Approximate file size (e.g., "2.3 GB", "45 MB") |
| Notes | Text | Description, context, or retrieval instructions |

**Future expansion:** Original Source, Date Created, Retention Policy, Last Accessed

**Answers:** "Where are our 2024 tax documents?" "What videos do we have on the SSD?" "How much space is used by backups?"

---

### 4. Clarkson Storage — NEW

**Status:** Design complete — not yet built
**Purpose:** Inventory of physical items in the storage unit at 77 Clarkson Ave. Enables answering "do we already have one?" without visiting the unit.

**Schema (Basic):**

| Property | Type | Options / Notes |
|----------|------|----------------|
| Name | Title | Item name |
| Category | Select | Furniture, Electronics, Kitchenware, Decor, Clothing/Textiles, Sports/Outdoor, Seasonal, Documents/Paper, Miscellaneous |
| Owner | Select | Nick, JR, Household |
| Location in Unit | Text | Where in the storage unit (e.g., "Back wall, top shelf") |
| Condition | Select | Excellent, Good, Fair, Poor |
| Photo | File | Image of the item |
| Date Stored | Date | When the item was placed in storage |
| Notes | Text | Description, assembly notes, or context |

**Future expansion:** Purchase Date, Estimated Value, Dimensions, Weight, Insurance Claimed, Disposition (Keep / Sell / Donate / Discard)

**Answers:** "Do we have extra dining chairs?" "What furniture is in storage?" "Is the holiday decor there?"

---

### 5. Clarkson Active — NEW

**Status:** Design complete — not yet built
**Purpose:** Inventory of significant items currently in use at 77 Clarkson Ave — furniture, appliances, electronics, fixtures. Not every fork and napkin, but anything you'd want to track, insure, or replace.

**Schema (Basic):**

| Property | Type | Options / Notes |
|----------|------|----------------|
| Name | Title | Item name |
| Category | Select | Furniture, Major Appliance, Small Appliance, Electronics, Kitchenware, Decor, Fixture, Textile/Linen |
| Room | Select | Living Room, Kitchen, Primary Bedroom, Guest Bedroom, Bathroom, Hallway, Closet, Office, Balcony |
| Owner | Select | Nick, JR, Household |
| Brand | Text | Manufacturer or brand name |
| Condition | Select | Excellent, Good, Fair, Poor |
| Photo | File | Image of the item |
| Notes | Text | Model number, serial number, special care instructions |

**Future expansion:** Purchase Date, Purchase Price, Estimated Value, Warranty Expiry, Dimensions, Link (product page), Receipt (file)

**Answers:** "What brand is our dishwasher?" "What's in the living room?" "What do we need for renter's insurance?"

---

## How Libraries Connect to the System

| System Component | How It Uses Reference Libraries |
|-----------------|-------------------------------|
| Front Desk | Routes "do we have X?" queries to the appropriate library |
| Wardrobe System | The Fragrance Library is a specialized Reference Library (DD-16). Wardrobe Items database follows the same catalog pattern. |
| Capturing Beast | New purchases or acquisitions get cataloged in the appropriate library after the 3-lens filter |
| OKRs / Projects | Renovation or organization projects query Clarkson Active/Storage to assess current state |
| Archive page | Items moved to the Notion Archive section may correspond to entries in Clarkson Storage or Archive (SSD) |

---

## Clarkson Storage <-> Clarkson Active Movement

Items move between Storage and Active when they're retrieved from or placed into storage. The workflow:

1. **Storage → Active:** Find item in Clarkson Storage, update its status/notes, create a new entry in Clarkson Active with the Room it's going to
2. **Active → Storage:** Find item in Clarkson Active, archive or delete the entry, create/update entry in Clarkson Storage with Location in Unit

In a future workstream, these could be linked via a relation property so movement is tracked automatically.

---

### 6. Business Ideas — NEW

**Status:** Design complete — not yet built
**Purpose:** A running catalog of business ideas Nick and JR have had over the years. Preserves early-stage thinking without cluttering the active project space. The place to return to when exploring new ventures or revisiting past concepts.

**Schema (Basic):**

| Property | Type | Options / Notes |
|----------|------|----------------|
| Name | Title | Name or working title of the idea |
| Status | Select | Idea, Exploring, On Hold, Abandoned |
| Owner | Select | Nick, JR, Both |
| Domain | Select | Tech, Food & Beverage, Creative, Real Estate, Consulting, Health & Wellness, Retail, Other |
| Enthusiasm | Select | Low, Medium, High — current gut-level interest |
| Summary | Text | One or two sentence description of the idea |
| Date Added | Date | When the idea was first captured |
| Notes | Text | Research, links, prior conversations, reasons it was shelved |

**Future expansion:** Market Size, Estimated Startup Cost, Related Ideas (self-relation), Linked Projects (for ideas that graduate to active exploration)

**Answers:** "What business ideas have we had?" "Any ideas in the food space?" "What did we think about that consulting idea?"

---

## Implementation Notes

> **Tooling update (2026-02-28):** The Notion `create-database` tool is now working (verified via IB-29 audit). These four new databases can be created programmatically via their dedicated IB items when prioritized.

**Recommended build order:**

1. Business Ideas (easiest to start — no physical inventory needed, just recall and capture)
2. Clarkson Active (most immediately useful — you live there)
3. Clarkson Storage (useful next time you visit the unit)
4. Archive SSD (useful next time you plug in the drive)

---

**Cross-references:** DD-14 (UB3 integration), DD-16 (Wardrobe System follows same catalog pattern), DD-17 (this design decision)
