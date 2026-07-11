# Pancake Taxonomy Data Dictionary

Version: 0.2

## Overview

The Pancake Taxonomy dataset is an exploratory cultural and technological classification system for pancakes and pancake-adjacent foods.

The goal of the project is not to establish a strict definition of what is or is not a pancake. Instead, it provides a multidimensional framework for discussing culinary ancestry, technological development, cultural significance, and perceived pancake-ness.

Many foods occupy ambiguous positions within the taxonomy. These ambiguities are considered a feature rather than a flaw. The dataset is designed to support discussion, visualization, and exploration of relationships between foods that share common preparation techniques, ingredients, or historical origins.

Scores are assigned on a normalized 0–10 scale unless otherwise specified.

---

# Dataset Structure

Each row represents a single food item.

Each column represents either:

* Identification metadata
* Descriptive metadata
* Taxonomic metrics

---

# Identification Fields

## id

Unique machine-readable identifier.

Type:

```text
string
```

Examples:

```text
dosa
crepe
injera
waffle
```

Identifiers should remain stable across dataset revisions.

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
```

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
```

This field reflects common cultural association rather than origin claims.

---

## family

Curated lineage grouping.

Type:

```text
string
```

Examples:

```text
rice_lentil_fermented
corn_cake
foam_pancake
```

Families are intended as heuristic groupings rather than formal scientific categories.

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
```

Ingredients are representative rather than exhaustive.

---

# Documentation Fields

## summary

Short descriptive summary.

Type:

```text
string
```

Purpose:

Human-readable explanation suitable for catalogs, websites, and visualizations.

---

## alt_text

Accessibility description for illustrations or photographs.

Type:

```text
string
```

Purpose:

Provides meaningful descriptions suitable for screen readers and future image generation workflows.

---

# Metric Fields

## fermentation

Measures dependence on intentional fermentation.

Scale:

```text
0 = no fermentation

10 = fermentation is essential
```

Examples:

| Food               | Score |
| ------------------ | ----: |
| Crêpe              |     0 |
| Buttermilk Pancake |     1 |
| Dosa               |     9 |
| Injera             |    10 |

Interpretation:

This metric measures process dependency rather than flavor.

---

## fermentation_visibility

Measures how obvious fermentation is to the eater.

Scale:

```text
0 = fermentation not perceptible

10 = fermentation dominates flavor and texture
```

Examples:

| Food    | Score |
| ------- | ----: |
| Crêpe   |     0 |
| Baghrir |     5 |
| Dosa    |     9 |
| Injera  |    10 |

Interpretation:

A food may score high in fermentation but lower in fermentation visibility.

---

## planarity

Measures how sheet-like or planar the finished food is.

Scale:

```text
0 = spherical, puffed, or vertically developed

10 = thin planar sheet
```

Examples:

| Food            | Score |
| --------------- | ----: |
| Soufflé Pancake |     0 |
| Dutch Baby      |     0 |
| Crêpe           |    10 |
| Jianbing        |     9 |

Interpretation:

This metric replaced the earlier "thinness" metric.

The focus is geometry rather than thickness alone.

---

## batter_identity

Measures the degree to which a food is fundamentally batter-derived.

Scale:

```text
0 = dough-derived

5 = mixed or ambiguous

10 = batter-derived
```

Examples:

| Food             | Score |
| ---------------- | ----: |
| Roti Canai       |     1 |
| Scallion Pancake |     2 |
| Dosa             |    10 |
| Crêpe            |    10 |

Interpretation:

This is one of the most important metrics in the dataset.

It distinguishes batter pancakes from dough pancakes, laminated pancakes, and pancake-adjacent foods.

---

## griddle_dependence

Measures dependence on a flat heated cooking surface.

Scale:

```text
0 = griddle not required

10 = griddle is fundamental
```

Examples:

| Food              | Score |
| ----------------- | ----: |
| Yorkshire Pudding |     0 |
| Dutch Baby        |     2 |
| Dosa              |    10 |
| Crêpe             |    10 |

Interpretation:

This metric captures a major technological lineage within pancake evolution.

---

## fillability

Measures the ability of a food to function as a wrapper, carrier, enclosure, or delivery mechanism.

Scale:

```text
0 = cannot realistically contain fillings

10 = commonly wraps, folds, encloses, or carries fillings
```

Examples:

| Food     | Score |
| -------- | ----: |
| Latke    |     1 |
| Dosa     |     8 |
| Crêpe    |    10 |
| Jianbing |    10 |
| Arepa    |    10 |

Interpretation:

This metric captures an important evolutionary branch of pancake development.

Many successful pancakes function as both food and food-delivery systems.

---

## savory_orientation

Measures typical placement on the sweet–savory spectrum.

Scale:

```text
0 = strongly sweet

5 = neutral or mixed

10 = strongly savory
```

Examples:

| Food       | Score |
| ---------- | ----: |
| Poffertjes |     0 |
| Crêpe      |     4 |
| Dosa       |     9 |
| Jeon       |    10 |

Interpretation:

Scores reflect typical usage rather than all possible preparations.

---

## staple_role

Measures the extent to which a food functions as a dietary staple.

Scale:

```text
0 = novelty, dessert, or occasional treat

10 = major daily staple
```

Examples:

| Food            | Score |
| --------------- | ----: |
| Soufflé Pancake |     1 |
| Dosa            |     8 |
| Injera          |    10 |
| Tortilla        |    10 |

Interpretation:

This metric distinguishes foundational foods from specialty foods.

---

## ritual_social_weight

Measures cultural, ceremonial, communal, or identity significance.

Scale:

```text
0 = little cultural significance

10 = major ritual, communal, or identity-associated food
```

Examples:

| Food               | Score |
| ------------------ | ----: |
| Pancake on a Stick |     1 |
| Blini              |    10 |
| Latke              |     9 |
| Injera             |     9 |

Interpretation:

This metric captures social meaning rather than nutritional importance.

---

## technology_complexity

Measures accumulated technological and culinary infrastructure.

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
* Cultural knowledge requirements

Examples:

| Food               | Score |
| ------------------ | ----: |
| Ancient Grain Cake |     3 |
| Dosa               |     9 |
| Hopper             |     9 |
| Soufflé Pancake    |     9 |

Interpretation:

Complexity reflects process sophistication, not food quality.

---

## lineage_confidence

Measures confidence in historical continuity and documentation.

Scale:

```text
0 = speculative reconstruction

10 = well-documented living tradition
```

Examples:

| Food               | Score |
| ------------------ | ----: |
| Ancient Grain Cake |     2 |
| Crêpe              |    10 |
| Dosa               |    10 |
| Injera             |    10 |

Interpretation:

This metric reflects historical certainty rather than culinary significance.

---

## pancake_claim

Measures the likelihood that an average observer would classify the food as a pancake.

Scale:

```text
0 = almost nobody would call it a pancake

10 = universally recognized as a pancake
```

Examples:

| Food               | Score |
| ------------------ | ----: |
| Naan               |     1 |
| Yorkshire Pudding  |     2 |
| Arepa              |     4 |
| Dosa               |     9 |
| Crêpe              |    10 |
| Buttermilk Pancake |    10 |

Interpretation:

Unlike most metrics in this dataset, pancake_claim measures cultural perception rather than structural characteristics.

It intentionally captures disagreement.

---

# Design Philosophy

The Pancake Taxonomy treats pancakes as a technological lineage rather than a strict food category.

Under this framework, foods may be related through:

* Shared cooking methods
* Shared ingredient transformations
* Shared fermentation techniques
* Shared cultural functions
* Shared technological ancestry

A food may score highly on pancake_claim while being structurally unusual.

Likewise, a food may share strong technological ancestry with pancakes while rarely being described as one.

These tensions are intentional.

The purpose of the dataset is not to settle classification debates.

The purpose is to make those debates visible.

---

# License

This dataset is intended as a cultural, educational, and exploratory taxonomy.

Values are subjective, approximate, and expected to evolve through discussion and future revisions.

Contributions, corrections, disagreements, and entirely unreasonable pancake theories are welcome.
