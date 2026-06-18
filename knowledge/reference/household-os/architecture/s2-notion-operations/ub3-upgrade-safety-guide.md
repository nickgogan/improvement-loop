---
notion_id: 3111e08b-9b34-81ec-806f-da9b6429f8fa
title: "UB3 Upgrade Safety Guide"
parent: "S2: Notion Operations Architecture"
extracted: "2026-04-04"
---

# UB3 Upgrade Safety Guide

> **For agents:** This page describes the process for safely evaluating and applying Thomas Frank's Ultimate Brain 3.0 template updates to our customized copy. Before applying any UB3 update, read this page and the UB3 Integration Map. For the list of specific pending updates, see the UB3 Template Updates page.

## Why This Guide Exists

Ultimate Brain is a Notion template. Once duplicated into a workspace, it becomes a fully independent copy with no connection to the source. Updates are not automatic — Thomas Frank publishes upgrade guides (for small changes) or transfer guides (for large changes) that users apply manually.

Our Household OS extends UB3 significantly: we add properties, deprecate others, create new views, and layer architectural concepts on top. This means any upstream UB3 update must be evaluated for compatibility before applying it. This guide provides the process.

---

## Risk Assessment Framework

Every UB3 update involves one or more of the following change types. Each carries a different risk level when applied to our customized copy.

### Low Risk — Safe to Apply Directly

- **New properties** (checkbox, select, relation): Adding a property that didn't exist before. This never conflicts with our additions because we haven't touched what doesn't exist yet.
- **New views**: Adding a filtered view to a database. Our custom views are unaffected.
- **New pages or templates**: Adding content pages. No conflict with existing structure.
- **Cosmetic changes**: Renaming a property, changing an icon, reordering properties in a view.

### Medium Risk — Evaluate Before Applying

- **Formula updates**: Thomas Frank's formulas may reference property names. If we've renamed a property (e.g., Tags → Labels, which UB3 itself did in Dec 2024), a new formula pasted verbatim could break. Always diff the formula against our current version before replacing.
- **Automation changes**: Automations may depend on specific property values or names. If we've added select options (e.g., a new Status value) or changed property semantics (e.g., Visibility → Owner), automations may not account for our additions.
- **Relation changes**: New relations between databases are usually safe, but if the relation name collides with one we've already created, it could cause confusion or duplicate properties.

### High Risk — Requires Careful Planning

- **Formula replacements that touch Smart List or core UB3 logic**: The Smart List formula is the backbone of GTD-Lite task routing. We do not modify it (Operating Rule #10), but a UB3 update that replaces it could invalidate views or filters that depend on its output values.
- **Property deprecation or deletion**: If Thomas Frank removes a property we've built views or formulas around, those break. Unlikely but possible in major version bumps.
- **Structural database changes**: Merging databases, splitting databases, or changing property types (e.g., select → multi-select). These are rare but happened in the 2.0 → 3.0 migration.

---

## The Upgrade Process (Step by Step)

### Step 1: Capture the Update

When Thomas Frank publishes a new UB3 update:

1. Download the upgrade guide (usually a PDF or video walkthrough)
2. Save the guide to the workspace folder as `UltimateBrainChangelog.pdf` (append or replace)
3. Add a new section to the **UB3 Template Updates** page documenting each individual change with: what changed, which databases are affected, implementation steps

### Step 2: Classify Each Change

For each individual change in the update, assign a risk level (Low / Medium / High) using the framework above. Document this on the Template Updates page.

### Step 3: Check the Modification Registry

Before applying any change, consult these pages to understand what we've customized:

- **UB3 Integration Map** → "Properties to add or modify" and "Properties to deprecate" tables for each database
- **UB3 Template Updates** → Audit Results section showing current property state
- **Implementation Backlog** → Any active IB items that touch the same database

Look for conflicts: Does the UB3 update touch a property we've modified? Does it assume a property name we've changed? Does it add a formula that references something we've deprecated?

### Step 4: Duplicate Before Touching

Before applying any Medium or High risk change:

1. Duplicate the affected database page as a backup (right-click → Duplicate in Notion)
2. Name the backup with a date suffix: e.g., "Tasks (backup 2026-02-24)"
3. Apply the change to the original
4. Test thoroughly (see Step 5)
5. Delete the backup only after confirming everything works

For Low risk changes, a backup is optional but still recommended if you're applying multiple changes at once.

### Step 5: Test After Each Change

After applying each individual change (not after applying the whole batch):

1. **Check views**: Open every standard view in the affected database. Do filters still work? Are the right items showing?
2. **Check formulas**: If you changed a formula, spot-check 3-5 items. Does the calculated value make sense?
3. **Check relations**: If you added a relation, verify both sides show the correct linked items.
4. **Check automations**: If you modified an automation, trigger it with a test item and verify the result.
5. **Check our custom properties**: Verify that Owner, Level, Type, and other Household OS properties still display correctly in views.

### Step 6: Update Documentation

After successfully applying changes:

1. Update the **UB3 Template Updates** page — mark items as applied, update the Audit Results section
2. Update the **UB3 Integration Map** if any property mappings changed
3. Update the **Implementation Backlog** if any IB items are affected
4. Update the **Agent Handoff Prompt** if the change affects how agents should work with the database

---

## What We Customize vs. What Thomas Frank Touches

This is the key insight that makes upgrades manageable: **our customizations and Thomas Frank's updates rarely overlap.**

### What We Add (Thomas Frank Doesn't Touch)

- **Owner** (select) on Tasks, Projects — our DD-09 addition
- **Level** (select) on Goals — our DD-09 addition
- **Type** (select: Task/Speedy) on Tasks — our DD-07 addition
- **Source** (select) on Tasks — our capture tracking addition
- **All Architecture pages** — System Documentation, DD specs, Topic Map, etc.
- **All custom views** filtered by Owner, Level, or Area
- **Command Center page** — our view layer, not a UB3 component

### What Thomas Frank Updates (We Don't Touch)

- **Smart List formula** — GTD-Lite routing logic. We use it but never modify it.
- **Recurring task formulas** (Next Due, Postpone, Enforce Schedule) — his domain
- **Time tracking formulas** — calculated from Work Sessions
- **Built-in automations** — recurring task processing, completion dates, sub-task sync
- **Core properties** — Status, Priority, Due, My Day, Energy, Location, P/I

### The Overlap Zone (Requires Care)

- **Visibility property** — We plan to deprecate it in favor of Owner. If Thomas Frank updates Visibility, we can safely ignore it since we're replacing it anyway. But if a new formula references Visibility by name, we may need to adapt it.
- **Tags database** — We use it as our PARA Area taxonomy (DD-23). If Thomas Frank changes Tags structure, we need to evaluate impact on our Area system.
- **Notes Type property** — We may add an "Inbox" option. If Thomas Frank adds new Type options, no conflict. If he restructures the Type property, we'd need to reconcile.

---

## Decision: When to Skip an Update

Not every UB3 update needs to be applied. Thomas Frank himself says updates are "safe to miss out on" since Notion's platform updates apply automatically. Skip an update if:

- The change is cosmetic and doesn't affect functionality you use
- The change adds a feature you don't need (e.g., a new view type you won't use)
- The change conflicts with a Household OS customization and the customization is more important
- The effort to apply exceeds the benefit

Document skipped updates on the Template Updates page with a reason, so future agents know it was intentional.

---

## Emergency Rollback

If an update breaks something:

1. **Undo via version history**: Notion's page history (... → Page history) can restore individual pages to previous states. This works well for formula and content changes.
2. **Restore from backup**: If you duplicated the database before the change (Step 4), you can delete the broken version and rename the backup.
3. **Reverse the change manually**: For property additions, simply delete the property. For formula changes, paste back the previous formula (which should be documented on the Template Updates page).
4. **Document the failure**: Add a note to the Template Updates page explaining what went wrong and why. This helps future agents avoid the same mistake.

---

## Update Cadence Expectations

Based on the UB3 changelog history:

- **Major updates** (new features, formula overhauls): ~2-3 per year
- **Minor updates** (bug fixes, cosmetic tweaks): ~1-2 per year
- **Breaking changes** (property type changes, database restructuring): Only in major version bumps (1.0→2.0 was incremental, 2.0→3.0 was a ground-up rewrite). The next major version is likely years away.

This means you'll realistically evaluate 3-4 updates per year, most of which will be Low risk property or formula additions.

---

*This guide is a living document. Update it as we learn more about the interaction between our customizations and Thomas Frank's updates. The UB3 Integration Map and UB3 Template Updates pages are the two companion references.*

---

## Build Spec

> *Status: Not started — fill in this spec when this IB item is picked up for implementation. See [Implementation Process](https://www.notion.so/3111e08b9b348187912ec41944e810eb) for the full schema reference.*

### 1. Header

| Field | Value |
|-------|-------|
| **IB Item** | *(see database properties)* |
| **Milestone** | |
| **Source DD** | *(see database properties)* |
| **Type** | *(see database properties)* |
| **Priority** | *(see database properties)* |
| **Prerequisites** | |
| **Status** | Draft |

### 2. Summary

*(What this item accomplishes and why it matters.)*

### 3. Human Steps

*(Steps requiring manual action in Notion UI. Mark N/A if none.)*

| Step | Database | Action | Property Name | Property Type | Values / Config | Notes |
|------|----------|--------|--------------|---------------|----------------|-------|
| H1 | | | | | | |

### 4. Agent Steps

*(Steps the agent executes after human steps are confirmed. Mark N/A if none.)*

| Step | Action | Target | Details |
|------|--------|--------|---------|
| A1 | | | |

### 5. Verification

*(One check per Human Step and Agent Step.)*

| Check | Method | Expected Result | Status | Notes |
|-------|--------|----------------|--------|-------|
| H1 | | | Pending | |
| A1 | | | Pending | |

### 6. Rollback

*(How to reverse each Human Step. Mark N/A if agent-only.)*

| Step | Reversal | Risk |
|------|----------|------|
| H1 | | |

### 7. Documentation Cascade

*(Pages to update when this item is marked Complete.)*

| Page | Update Needed? | Details |
|------|---------------|---------|
| Implementation Backlog | Yes | Mark item as Done |
| Vocabulary | | |
| Architecture hub | | |
