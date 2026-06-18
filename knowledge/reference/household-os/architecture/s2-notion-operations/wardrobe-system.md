---
notion_id: 30f1e08b-9b34-8162-95dc-c784a3f667ab
title: "Wardrobe System"
parent: "S2: Notion Operations Architecture"
extracted: "2026-04-04"
---

# Wardrobe System

> **For agents:** This page defines the three-database wardrobe system. When answering "what should I wear today?", query the Outfits database filtered by Owner, current weather/season, calendar occasion, and requested mood. Return the full outfit including fragrance pairing. If no exact match, compose from Wardrobe Items using the style segment rules below.

---

## Core Decision

**DD-16:** Three interconnected databases form the wardrobe system: Wardrobe Items (every piece), Outfits (curated combinations), and Fragrance Library (scent layer). Outfits reference Items and Fragrances via relations. Per-person ownership with coordinated pairing support for joint occasions.

---

## System Architecture

```
+-------------------+     +-------------------+     +-------------------+
|  Wardrobe Items   |---->|     Outfits       |<----|  Fragrance Library|
|  (the pieces)     |     |  (combinations)   |     |   (the scents)   |
+-------------------+     +--------+----------+     +-------------------+
                                   |
                          +--------+----------+
                          |  Pair With (self) |
                          |  Nick <-> JR      |
                          +-------------------+
```

---

## Database 1: Wardrobe Items

Every garment, shoe, and accessory each person owns.

### Schema

| Property | Type | Options / Notes |
|----------|------|----------------|
| **Name** | Title | e.g., "Billy Reid Pocket Tee (Green)" |
| **Owner** | Select | Nick, JR |
| **Category** | Select | Top, Bottom, Outerwear, Footwear, Accessory, Underwear |
| **Subcategory** | Select | T-Shirt, Polo, Henley, Oxford, Dress Shirt, Sweater, Cardigan, Hoodie, Tank, Turtleneck, Rugby, Chinos, Jeans, Dress Pants, Joggers, Shorts, Blazer, Bomber, Trench, Pea Coat, Parka, Denim Jacket, Leather Jacket, Sneakers, Loafers, Oxfords, Boots, Chelsea Boots, Belt, Watch, Ring, Sunglasses, Hat, Scarf |
| **Brand** | Select | Populated as items are added |
| **Color** | Multi-select | Navy, Black, White, Gray, Charcoal, Olive, Brown, Tan, Burgundy, Green, Blue, Cream, Amber |
| **Material** | Select | Cotton, Linen, Wool, Denim, Leather, Suede, Synthetic, Chambray, Twill, Corduroy, French Terry, Gingham, Satin, Blend |
| **Style Segment** | Multi-select | **Nick:** Ruggedly Refined, Activewear, Loungewear, Professional. **JR:** Traditional, Workwear, Sporty, Experimental. **Shared:** Formal |
| **Season** | Multi-select | Spring, Summer, Fall, Winter |
| **Formality** | Select | Casual, Smart Casual, Business Casual, Business, Formal, Cocktail |
| **Condition** | Select | New, Good, Fair, Worn |
| **Status** | Select | Active, Retired, Wishlist, Alterations Needed, Seasonal Storage |
| **Size** | Rich text | Free-form for different sizing systems |
| **Price** | Number ($) | Purchase price |
| **Link** | URL | Purchase/brand link |

### Style Segments Explained

> **For agents:** When composing outfits from individual items, respect these style segment rules. Items from the same segment pair naturally. Cross-segment pairing requires intentional contrast (e.g., RR top + Activewear bottom works for casual weekends but not for date night).

**Nick's segments:**

- **Ruggedly Refined (RR):** Workwear-inspired but high-quality. Unconventional stitching, interesting hardware. Deceivingly simple — layered details reward close inspection. NYC/London influenced.
- **Activewear:** Lifting, running, hiking. More synthetic content for drape and smoothness. Provides contrast to RR.
- **Loungewear:** Military-inspired and contemporary. Nice enough for office if properly paired.
- **Professional:** Classic + Military influences. Structured pieces, clean lines.

**JR's segments:**

- **Traditional/Formalish:** Knits, blazers, button-ups. Polished and put-together.
- **Workwear:** Practical, durable, structured. Overlaps with Nick's RR in spirit.
- **Sporty:** Quarter-zips, vests, tanks. Active but styled.
- **Experimental:** Rule-breaking pieces. Unusual silhouettes, bold choices.

---

## Database 2: Outfits

Curated, proven combinations. The primary query surface for "what should I wear today?"

### Schema

| Property | Type | Options / Notes |
|----------|------|----------------|
| **Name** | Title | e.g., "Fall Date Night — Navy & Brown" |
| **Owner** | Select | Nick, JR |
| **Top** | Relation → Wardrobe Items | Can be multiple (e.g., shirt + sweater layer) |
| **Bottom** | Relation → Wardrobe Items | Single item |
| **Outerwear** | Relation → Wardrobe Items | Optional. Jacket, coat, etc. |
| **Footwear** | Relation → Wardrobe Items | Single item |
| **Accessories** | Relation → Wardrobe Items | Belt, watch, ring, sunglasses, etc. |
| **Fragrance** | Relation → Fragrance Library | The scent that completes the look |
| **Season** | Multi-select | Spring, Summer, Fall, Winter |
| **Weather** | Multi-select | Hot, Warm, Cool, Cold, Rainy, Humid |
| **Temp Range** | Rich text | e.g., "45-65F" — for precise weather API matching |
| **Occasion** | Multi-select | Date Night, Casual, Work, Formal, Brunch, Travel, Gym, Cocktail, Errands |
| **Location** | Multi-select | Home, Office, Restaurant, Bar, Outdoor, Travel, Gym, Gallery/Museum |
| **Mood** | Multi-select | Confident, Relaxed, Playful, Romantic, Energized, Cozy, Focused, Sensual |
| **Formality** | Select | Casual, Smart Casual, Business Casual, Business, Formal, Cocktail |
| **Style Segment** | Select | Same options as Wardrobe Items |
| **Pair With** | Self-relation → Outfits | Link Nick's outfit to JR's complementary look for coordinated occasions |
| **Rating** | Select | Love, Like, Neutral, Dislike |
| **Status** | Select | Active, Seasonal, Retired, Draft |

### Agent Query Logic

> **For agents:** When asked "what should I wear today?", execute this sequence:
>
> 1. **Identify context:** Check calendar for today's events (occasion, location). Get current weather forecast (temperature, conditions). Ask for mood if not stated.
> 2. **Query Outfits database:** Filter by Owner + Season + Weather + Occasion. If mood specified, filter further.
> 3. **Rank results:** Prefer outfits with Rating = Love. Deprioritize recently worn (check System Log if available).
> 4. **Return recommendation:** Full outfit breakdown including each item name, the fragrance pairing, and why it fits the context.
> 5. **Coordinated looks:** If both partners are going out together, query for Pair With links or recommend complementary outfits that don't clash.
>
> **Fallback:** If no curated outfit matches, compose from Wardrobe Items: pick pieces from the same Style Segment, matching Season/Formality, and pair with an appropriate fragrance from the Fragrance Library.

---

## Database 3: Fragrance Library

Already documented in the Fragrance Library page under Personal Care → Wardrobe → Reference & Education. Schema designed with all the same query properties (Season, Weather, Occasion, Mood, Style Pairing).

When the Fragrance Library is converted to a proper Notion database, the Outfits database will link to it via relation. Until then, use text references.

---

## How It All Connects

| Question | Primary Query | Supporting Data |
|----------|--------------|-----------------|
| "What should I wear today?" | Outfits → filter by weather + occasion + mood | Items for piece details, Fragrance for scent |
| "What should we both wear tonight?" | Outfits → filter by occasion + Pair With relation | Both owners' outfits, coordinated fragrances |
| "What fragrance for a rainy fall evening?" | Fragrance Library → filter by season + weather + mood | Can also check which outfits pair with that fragrance |
| "Do I need to buy anything for summer?" | Wardrobe Items → filter by Season = Summer + Status = Active | Compare against Outfits rated Love for gaps |
| "What's in my closet that I never wear?" | Wardrobe Items NOT referenced by any Active Outfit | Candidates for retirement or creative reuse |
| "Build me a capsule for a weekend trip" | Outfits → filter by Location = Travel, maximize item overlap | Minimize total items packed while covering occasions |

---

## Relationship to Existing Content

The current wardrobe pages contain style philosophy, color palettes, measurements, brand preferences, and shopping notes. These remain as **reference pages** — they inform how outfits are curated but aren't replaced by the databases.

| Existing Page | Role After DB Creation |
|--------------|----------------------|
| Wardrobe - Nick | Style philosophy, color preferences, measurements. **Reference** for outfit curation. |
| Wardrobe - JR | Style philosophy, color palette, measurements. **Reference** for outfit curation. |
| Nick/JR - Shopping/Brands | Brand preferences, wishlist notes. Feed Wardrobe Items (Status = Wishlist). |
| Wardrobe - Accessories | Reference for accessory types. Items get entries in Wardrobe Items database. |
| Fragrance Library | Becomes Database 3 via IB-14 (tooling now working). Already has full schema. |
| Shared Knowledge (fabrics, styles, vocabulary) | Agent reference for understanding garment terms and making informed suggestions. |

---

## Implementation Notes

> **Tooling update (2026-02-28):** The Notion `create-database` tool is now working (verified via IB-29 audit). Database creation for these schemas can proceed programmatically via IB-12 (Wardrobe Items), IB-13 (Outfits), and IB-14 (Fragrance Library).

**Recommended implementation order:**

1. Create Wardrobe Items database (no dependencies)
2. Create Outfits database with relations to Wardrobe Items
3. Convert Fragrance Library page to database
4. Add Fragrance relation to Outfits
5. Populate Wardrobe Items by cataloging actual closets
6. Curate initial Outfits from known combinations
7. Build views: My Outfits (filtered by Owner), Seasonal Rotation, Date Night Sets

---

## Cross-References

- **DD-16:** Three-database wardrobe system architecture
- **DD-14:** UB3 Integration Map (these databases extend UB3 alongside existing ones)
- **DD-13:** Lives in the Household Teamspace's Operational Databases section
- **DD-12:** Owner property for personal scoping within shared workspace
- **Fragrance Library:** Schema and initial entries already documented
