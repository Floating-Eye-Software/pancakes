# Pancake Taxonomy Data Dictionary

Version: 0.3

## Overview

The Pancake Taxonomy dataset is an exploratory cultural and technological classification system for pancakes and pancake-adjacent foods.

The goal of the project is not to establish a strict definition of what is or is not a pancake. Instead, it provides a multidimensional framework for discussing culinary ancestry, technological development, cultural significance, preparation technology, and perceived pancake-ness.

Many foods occupy ambiguous positions within the taxonomy. These ambiguities are considered a feature rather than a flaw. The dataset is designed to support discussion, visualization, and exploration of relationships between foods that share common preparation techniques, ingredients, cultural functions, or historical lineages.

Scores are assigned on a normalized 0–10 scale unless otherwise specified. These scores are interpretive taxonomy values, not laboratory measurements.

---

# Dataset Structure

Each row represents a single food item or food category.

Each column belongs to one of five groups:

* Identification metadata
* Descriptive metadata
* Source and fact-check metadata
* Taxonomic metrics
* Maintenance and review metadata

Current canonical column order:

```text
id,
name,
region,
family,
base,
summary,
alt_text,
fermentation,
fermentation_visibility,
planarity,
batter_identity,
griddle_dependence,
fillability,
savory_orientation,
staple_role,
ritual_social_weight,
technology_complexity,
lineage_confidence,
pancake_claim,
source_url,
fact_check_status,
fact_check_note
```

---

# Field Conventions

## Text fields

Text fields should use plain UTF-8 strings.

Use title case only where appropriate for display names. Machine-readable identifiers and families should use lowercase snake case.

## List fields

The `base` field uses a semicolon-separated string list rather than a JSON array to keep the CSV simple and spreadsheet-friendly.

Example:

```text
rice; urad dal
wheat; buckwheat
rice flour; turmeric; coconut milk
```

## Numeric metric fields

Metric fields use integer values from 0 to 10 unless otherwise specified.

Use the full scale. Avoid clustering all canonical pancakes at 8–10 unless the metric genuinely calls for it.

Suggested interpretation bands:

| Range | Meaning |
| ---: | --- |
| 0 | Absent or nearly absent |
| 1–2 | Marginal / incidental |
| 3–4 | Present but secondary |
| 5 | Mixed, ambiguous, or balanced |
| 6–7 | Strong but not defining |
| 8–9 | Defining or near-essential |
| 10 | Essential, extreme, or paradigmatic |

## Missing values

Prefer explicit values over blanks.

If a score cannot be assigned, use a review workflow rather than leaving it blank:

* `fact_check_status = Needs review`
* `fact_check_note = Explain what is uncertain`

## URLs

`source_url` should contain a single URL that best explains or substantiates the row. It does not need to be a definitive academic citation; recipes, culinary explainers, museum pages, reputable food publications, cultural essays, and high-quality blogs are acceptable.

When a food is speculative, reconstructed, or borderline, the URL should support the specific claim being made rather than overstate certainty.

---

# Identification Fields

## id

Unique machine-readable identifier.

Type:

```text
string
```

Format:

```text
lowercase snake_case
```

Examples:

```text
dosa
crepe
injera
waffle
ancient_grain_cake
```

Rules:

* Must be unique.
* Should remain stable across dataset revisions.
* Should not include accents, punctuation, spaces, or display formatting.
* Should not be renamed merely because the display name changes.

---

## name

Human-readable display name.

Type:

```text
string
```

Examples:

```text
Dosa
Crêpe
Injera
Buttermilk pancake
```

Rules:

* Preserve common diacritics where useful for display.
* Use the most recognizable English-language culinary name unless the original-language name is the standard display form.
* Do not force every item into the word “pancake.” The taxonomy can include pancake-adjacent foods without renaming them.

---

## region

Primary geographic or cultural association.

Type:

```text
string
```

Examples:

```text
South India
France
Ethiopia / Eritrea
Morocco / North Africa
```

Interpretation:

This field reflects common cultural association rather than a strict origin claim.

Rules:

* Use broad regions when the food is shared across many communities.
* Avoid unsupported origin claims.
* Use slash-separated regions where a food is strongly associated with multiple places.
* Prefer “cultural association” over “invented in.”

---

## family

Curated lineage grouping.

Type:

```text
string
```

Format:

```text
lowercase snake_case
```

Examples:

```text
rice_lentil_fermented
corn_cake
foam_pancake
layered_flatbread_pancake
oven_puffed_batter
```

Interpretation:

Families are heuristic groupings rather than formal scientific categories.

Rules:

* A family should describe technological or structural kinship.
* Families may combine ingredient, process, and morphology.
* Do not create a new family for every row unless the item is genuinely structurally distinct.

---

## base

Primary ingredient list.

Type:

```text
semicolon-separated string list
```

Examples:

```text
rice; urad dal
wheat
potato; egg
semolina; wheat
```

Interpretation:

Ingredients are representative rather than exhaustive.

Rules:

* Include primary structural ingredients, not every seasoning or garnish.
* Use common ingredient names.
* Use `wheat` rather than `flour` when the grain identity matters.
* Include fermentation cultures only when they are a defining base component.

---

# Documentation Fields

## summary

Short descriptive summary.

Type:

```text
string
```

Purpose:

Human-readable explanation suitable for catalogs, websites, visualizations, or hovercards.

Rules:

* One sentence is preferred.
* Mention defining preparation, structure, or cultural function.
* Avoid unsupported historical claims.
* Borderline cases should be described as relatives, cousins, or contested cases rather than forced into canonical pancake status.

Example:

```text
A fermented rice-and-lentil pancake, often thin and crisp, usually served with chutney and sambar.
```

---

## alt_text

Accessibility description for illustrations or photographs.

Type:

```text
string
```

Purpose:

Provides meaningful descriptions suitable for screen readers and future image generation workflows.

Rules:

* Describe the visible food plainly.
* Avoid saying “image of” unless necessary.
* Include important shape, texture, serving context, and fillings.
* Do not include factual claims that would not be visible in the image.

Example:

```text
Golden dosa folded beside small bowls of chutney and sambar.
```

---

# Source and Fact-Check Fields

## source_url

A URL that supports, explains, or contextualizes the row.

Type:

```text
URL string
```

Examples:

```text
https://www.seriouseats.com/dosa-indian-rice-and-lentil-crepes
https://www.ucl.ac.uk/news/2018/jul/bread-predates-agriculture-4000-years
```

Purpose:

Provides a lightweight citation trail for readers and future dataset maintainers.

Acceptable source types:

* Recipe pages with clear culinary explanation
* Culinary reference articles
* Museum, university, or cultural heritage pages
* Reputable food publications
* Specialist blogs with useful preparation detail
* Encyclopedic sources when better sources are unavailable
* Video or reel pages if they clearly document the food type

Interpretation:

`source_url` does not mean the entire row is proven by that source. It means the source is useful evidence for the food category and its description.

Rules:

* Use one URL per row.
* Prefer sources that explain ingredients, preparation, cultural context, or morphology.
* For speculative rows, use sources that support the underlying archaeological or historical claim, not a modern recipe that implies false continuity.
* For borderline rows, use sources that support the item’s actual category, even if the row’s `pancake_claim` is low.
* Avoid low-information recipe scrapers when better explanations exist.

---

## fact_check_status

Summary status of the row after review.

Type:

```text
controlled string
```

Allowed values:

```text
Verified
Needs nuance
Needs review
Disputed
Borderline
Speculative
```

Recommended meanings:

| Value | Meaning |
| --- | --- |
| `Verified` | The row’s basic identity, ingredients, preparation, and cultural association are well supported. |
| `Needs nuance` | The row is broadly supportable but the wording, region, lineage, or category should be interpreted carefully. |
| `Needs review` | The row has not been sufficiently checked or needs better sourcing. |
| `Disputed` | There are conflicting claims or meaningful disagreement about identity, origin, category, or lineage. |
| `Borderline` | The food is intentionally pancake-adjacent rather than a canonical pancake. |
| `Speculative` | The row represents reconstruction, hypothesis, or analogy rather than a documented named tradition. |

Rules:

* Use `Verified` only for the basic descriptive row, not for every interpretive numeric score.
* Use `Borderline` for items such as naan, pita, tortilla, waffle, takoyaki, Yorkshire pudding, and other deliberately adjacent cases.
* Use `Speculative` for archaeological reconstructions or inferred early food forms.
* Use `Needs nuance` where the item is real and correctly described but the pancake framing requires explanation.

---

## fact_check_note

Short explanation of the fact-check status.

Type:

```text
string
```

Purpose:

Gives maintainers a compact explanation of what was checked, what remains uncertain, or how the row should be interpreted.

Rules:

* Keep notes concise but specific.
* Mention whether the source supports the food identity, ingredients, process, cultural context, or pancake-borderline status.
* For speculative or borderline rows, explain the boundary clearly.
* Do not use this field for long research essays.

Examples:

```text
Fermented rice-and-urad/black-gram batter and South Indian context supported.
```

```text
Layered wheat flatbread rather than batter pancake; included as a pancake-flatbread border case.
```

```text
Hypothetical reconstruction. Source supports prehistoric flatbread from ground cereals, not a named pancake type.
```

---

# Metric Fields

## fermentation

Measures dependence on intentional fermentation.

Type:

```text
integer, 0–10
```

Scale:

```text
0 = no fermentation
10 = fermentation is essential
```

Examples:

| Food | Score |
| --- | ---: |
| Crêpe | 0 |
| Buttermilk pancake | 1 |
| Dosa | 9 |
| Injera | 10 |

Interpretation:

This metric measures process dependency rather than flavor. Chemical leavening, egg foams, and baking powder are not fermentation.

---

## fermentation_visibility

Measures how obvious fermentation is to the eater.

Type:

```text
integer, 0–10
```

Scale:

```text
0 = fermentation not perceptible
10 = fermentation dominates flavor and texture
```

Examples:

| Food | Score |
| --- | ---: |
| Crêpe | 0 |
| Baghrir | 5 |
| Dosa | 9 |
| Injera | 10 |

Interpretation:

A food may score high in `fermentation` but lower in `fermentation_visibility` if fermentation is technically important but not strongly perceptible in flavor or texture.

---

## planarity

Measures how sheet-like or planar the finished food is.

Type:

```text
integer, 0–10
```

Scale:

```text
0 = spherical, puffed, or vertically developed
10 = thin planar sheet
```

Examples:

| Food | Score |
| --- | ---: |
| Soufflé pancake | 0 |
| Dutch baby | 0 |
| Crêpe | 10 |
| Jianbing | 9 |

Interpretation:

This metric replaced the earlier `thinness` metric. The focus is geometry rather than thickness alone.

A thin sheet, wrapper, or crepe-like form scores high. A puffed, ball-shaped, heavily risen, or thick vertical form scores low.

---

## batter_identity

Measures the degree to which a food is fundamentally batter-derived.

Type:

```text
integer, 0–10
```

Scale:

```text
0 = dough-derived
5 = mixed or ambiguous
10 = batter-derived
```

Examples:

| Food | Score |
| --- | ---: |
| Roti canai | 1 |
| Scallion pancake | 2 |
| Dosa | 10 |
| Crêpe | 10 |

Interpretation:

This is one of the most important metrics in the dataset. It distinguishes batter pancakes from dough pancakes, laminated pancakes, flatbreads, and pancake-adjacent foods.

---

## griddle_dependence

Measures dependence on a flat heated cooking surface.

Type:

```text
integer, 0–10
```

Scale:

```text
0 = griddle not required
10 = griddle is fundamental
```

Examples:

| Food | Score |
| --- | ---: |
| Yorkshire pudding | 0 |
| Dutch baby | 2 |
| Dosa | 10 |
| Crêpe | 10 |

Interpretation:

This metric captures a major technological lineage within pancake evolution.

A special pan may still count as griddle-like if the key process is contact with a hot cooking surface. Oven-puffed, deep-fried, tandoor-baked, waffle-ironed, and spherical-mold foods score lower because they diverge from the flat griddle lineage.

---

## fillability

Measures the ability of a food to function as a wrapper, carrier, enclosure, or delivery mechanism.

Type:

```text
integer, 0–10
```

Scale:

```text
0 = cannot realistically contain fillings
10 = commonly wraps, folds, encloses, splits, pockets, or carries fillings
```

Examples:

| Food | Score |
| --- | ---: |
| Latke | 1 |
| Dosa | 8 |
| Crêpe | 10 |
| Jianbing | 10 |
| Arepa | 10 |

Interpretation:

This metric captures an important evolutionary branch of pancake development. Many successful pancake-like foods function as both food and food-delivery systems.

Fillability includes wrapping, folding, topping, splitting, stuffing, pocketing, or forming a bowl.

---

## savory_orientation

Measures typical placement on the sweet–savory spectrum.

Type:

```text
integer, 0–10
```

Scale:

```text
0 = strongly sweet
5 = neutral or mixed
10 = strongly savory
```

Examples:

| Food | Score |
| --- | ---: |
| Poffertjes | 0 |
| Crêpe | 4 |
| Dosa | 9 |
| Jeon | 10 |

Interpretation:

Scores reflect typical usage rather than all possible preparations.

A food with common sweet and savory variants should score near the middle unless one mode dominates public perception.

---

## staple_role

Measures the extent to which a food functions as a dietary staple.

Type:

```text
integer, 0–10
```

Scale:

```text
0 = novelty, dessert, or occasional treat
10 = major daily staple
```

Examples:

| Food | Score |
| --- | ---: |
| Soufflé pancake | 1 |
| Dosa | 8 |
| Injera | 10 |
| Tortilla | 10 |

Interpretation:

This metric distinguishes foundational foods from specialty foods.

A high `staple_role` does not imply a high `pancake_claim`. Tortilla and naan may be staples while still having low pancake perception in English-language contexts.

---

## ritual_social_weight

Measures cultural, ceremonial, communal, festive, or identity significance.

Type:

```text
integer, 0–10
```

Scale:

```text
0 = little cultural significance
10 = major ritual, communal, festive, or identity-associated food
```

Examples:

| Food | Score |
| --- | ---: |
| Pancake on a stick | 1 |
| Blini | 10 |
| Latke | 9 |
| Injera | 9 |

Interpretation:

This metric captures social meaning rather than nutritional importance.

Factors may include holiday association, communal serving, national or regional identity, ceremonial use, household tradition, and symbolic meaning.

---

## technology_complexity

Measures accumulated technological and culinary infrastructure.

Type:

```text
integer, 0–10
```

Scale:

```text
0 = minimal technology
10 = highly specialized process or equipment
```

Factors may include:

* Fermentation
* Specialized cookware
* Ingredient preparation
* Process sensitivity
* Timing requirements
* Heat-control requirements
* Laminating, stretching, aerating, or shaping technique
* Cultural knowledge requirements

Examples:

| Food | Score |
| --- | ---: |
| Ancient grain cake | 3 |
| Dosa | 9 |
| Hopper | 9 |
| Soufflé pancake | 9 |

Interpretation:

Complexity reflects process sophistication, not food quality.

A simple staple can be culturally important while scoring low on technology complexity.

---

## lineage_confidence

Measures confidence in historical continuity and documentation.

Type:

```text
integer, 0–10
```

Scale:

```text
0 = speculative reconstruction
10 = well-documented living tradition
```

Examples:

| Food | Score |
| --- | ---: |
| Ancient grain cake | 2 |
| Crêpe | 10 |
| Dosa | 10 |
| Injera | 10 |

Interpretation:

This metric reflects historical certainty rather than culinary significance.

A row can have low lineage confidence while still being useful as a conceptual ancestor or reconstruction.

---

## pancake_claim

Measures the likelihood that an average observer would classify the food as a pancake.

Type:

```text
integer, 0–10
```

Scale:

```text
0 = almost nobody would call it a pancake
10 = universally recognized as a pancake
```

Examples:

| Food | Score |
| --- | ---: |
| Naan | 1 |
| Yorkshire pudding | 2 |
| Arepa | 4 |
| Dosa | 9 |
| Crêpe | 10 |
| Buttermilk pancake | 10 |

Interpretation:

Unlike most metrics in this dataset, `pancake_claim` measures cultural perception rather than structural characteristics.

It intentionally captures disagreement. A food can be structurally pancake-like but culturally understood as a flatbread, bread, fritter, dumpling, cake, or snack.

---

# Fact-Checking Guidance

The fact-check layer should verify ordinary descriptive claims while preserving the dataset’s interpretive freedom.

## What fact-checking should verify

Fact-checking should support claims about:

* Food identity
* Common ingredients
* Preparation method
* Cooking technology
* Region or cultural association
* Typical serving mode
* Whether the item is canonical, contested, or adjacent

## What fact-checking should not overclaim

Fact-checking should not pretend that these are objective facts:

* Exact metric scores
* Whether something “really is” a pancake
* A single origin story when multiple histories exist
* A universal regional identity for foods with broad diasporic spread
* A precise ancestral relationship where only analogy is supported

## Recommended review workflow

For each row:

1. Confirm the food exists as a recognized type or category.
2. Confirm the summary does not overstate origin, lineage, or universality.
3. Confirm the `base` ingredients are representative.
4. Confirm the source URL explains the food or supports the relevant historical reconstruction.
5. Assign `fact_check_status`.
6. Add a compact `fact_check_note`.
7. Only revise metric scores when the source materially contradicts the existing interpretation.

---

# Borderline and Adjacent Foods

The dataset intentionally includes pancake-adjacent foods.

Borderline rows should remain in the dataset when they illuminate the pancake boundary.

Common borderline categories:

| Category | Examples | Reason for inclusion |
| --- | --- | --- |
| Layered flatbread | Scallion pancake, roti canai, msemen | Griddled, flat, often called pancake in English translation, but dough-derived. |
| Staple flatbread | Tortilla, pita, naan, bannock | Shares grain + heat + flatness lineage, but culturally framed as bread. |
| Fried batter relative | Funnel cake, frybread | Batter/dough plus hot fat rather than griddle lineage. |
| Specialized cookware relative | Waffle, takoyaki, poffertjes | Batter lineage transformed by strong cookware specialization. |
| Oven-puffed batter | Dutch baby, Yorkshire pudding | Batter-derived but not griddle-dependent. |
| Corn or root cakes | Arepa, latke, hoe cake, cachapa | Pancake-like griddled/fried cakes outside wheat-batter norms. |

Borderline status is not a defect. It is part of the taxonomy’s purpose.

---

# Recommended Future Fields

These fields are not required in version 0.3, but they are recommended if the dataset continues to grow.

## source_type

Controlled category for the source URL.

Suggested values:

```text
recipe
culinary_explainer
cultural_reference
academic_or_museum
encyclopedia
video
blog
review
```

Purpose:

Allows filtering sources by evidentiary type.

---

## source_quality

Lightweight confidence rating for the source itself.

Suggested values:

```text
high
medium
low
```

Purpose:

Separates row confidence from source quality. A row may be correct even if the currently attached URL is merely adequate.

---

## canonical_status

Clarifies the row’s relation to the pancake category.

Suggested values:

```text
canonical_pancake
regional_pancake
translated_as_pancake
pancake_adjacent
borderline_flatbread
borderline_fritter
speculative_ancestor
control_case
```

Purpose:

Makes the taxonomy easier to query without relying only on `pancake_claim`.

---

## primary_cooking_method

Controlled preparation technology.

Suggested values:

```text
griddle
pan_fried
deep_fried
oven_baked
tandoor_baked
waffle_iron
molded_pan
steamed_or_other
```

Purpose:

Supports cleaner analysis of griddle lineage versus other cooking technologies.

---

## dough_batter_state

Controlled descriptor for pre-cook material state.

Suggested values:

```text
thin_batter
thick_batter
fermented_batter
dough
laminated_dough
shredded_or_grated_matrix
hybrid
```

Purpose:

Makes the distinction behind `batter_identity` easier to audit.

---

## review_date

Date when the row was last reviewed.

Type:

```text
YYYY-MM-DD
```

Purpose:

Supports maintenance and periodic source checking.

---

# Design Philosophy

The Pancake Taxonomy treats pancakes as a technological lineage rather than a strict food category.

Under this framework, foods may be related through:

* Shared cooking methods
* Shared ingredient transformations
* Shared fermentation techniques
* Shared cultural functions
* Shared wrapper/carrier functions
* Shared griddle technologies
* Shared technological ancestry
* Shared translation or perception as “pancake”

A food may score highly on `pancake_claim` while being structurally unusual.

Likewise, a food may share strong technological ancestry with pancakes while rarely being described as one.

These tensions are intentional.

The purpose of the dataset is not to settle classification debates.

The purpose is to make those debates visible.

---

# Version History

## Version 0.1

Early schema centered on simpler structural dimensions, including `thinness`.

## Version 0.2

Replaced `thinness` with `planarity` and added more abstract relational dimensions including:

* `fermentation_visibility`
* `fillability`
* `pancake_claim`

## Version 0.3

Added source and review metadata:

* `source_url`
* `fact_check_status`
* `fact_check_note`

Also clarified:

* Column order
* Metric interpretation bands
* Borderline food handling
* Source-selection rules
* Fact-check workflow
* Recommended future fields

---

# License and Use

This dataset is intended as a cultural, educational, and exploratory taxonomy.

Values are subjective, approximate, and expected to evolve through discussion and future revisions.

Sources should be treated as supporting references rather than final authorities.

Contributions, corrections, disagreements, and entirely unreasonable pancake theories are welcome.
