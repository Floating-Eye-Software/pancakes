# Outline: `docs/pancakes-reference-services.md`

## Purpose

Define the architecture and philosophy of Pancakes Reference Services.

Reference services provide public, shared knowledge that can be used by Pancakes nodes without centralizing personal data.

They answer questions about the world rather than questions about people.

This document establishes a common pattern for future reference services.

---

# 1. Introduction

## Motivation

Many applications require common knowledge.

Examples:

* maps
* barcodes
* species
* recipes
* infrastructure
* administrative boundaries

Today this information is often:

* proprietary
* fragmented
* duplicated
* surveillance-supported

Pancakes proposes open, community-governed reference infrastructure.

---

## Design Goals

Reference services should be:

* open
* privacy-respecting
* reusable
* versioned
* community-maintained
* application-independent
* globally extensible

---

# 2. What Is A Reference Service?

Define the abstraction.

A reference service provides stable public facts.

Examples:

"This coordinate is inside this watershed."

"This barcode identifies this product."

"This species is native to this region."

Reference services do **not** store private user activity.

---

## Public Knowledge vs Private Knowledge

Public

* geography
* species
* products
* civic infrastructure

Private

* walks
* inventories
* journals
* habits
* health
* household activity

Nodes combine private events with public knowledge locally.

---

# 3. Architectural Pattern

Introduce the fundamental pattern.

```text
Private Node Event

+

Public Reference Service

↓

Local Meaning
```

Examples.

Scan barcode

↓

Product lookup

↓

Local pantry update

Walk in park

↓

GIS lookup

↓

Place relationship

Boil water advisory

↓

Infrastructure lookup

↓

Relevant household notification

---

# 4. Categories Of Reference Services

Introduce the concept of service families.

---

## Geographic Reference

Examples:

* boundaries
* watersheds
* aquifers
* parks
* trails
* ecological regions

---

## Goods Reference

Examples:

* barcodes
* commodities
* ingredients
* packaging
* repairability
* recycling

---

## Civic Infrastructure

Examples:

* drinking water
* wastewater
* electricity
* waste collection
* transit
* libraries
* schools
* hospitals

---

## Ecological Reference

Examples:

* species
* habitats
* migration routes
* invasive species
* pollinators

---

## Knowledge Reference

Examples:

* recipes
* standards
* educational materials
* public datasets

---

## Future Reference Services

Architecture intentionally supports additional categories.

Examples:

* astronomy
* geology
* weather
* heritage
* accessibility

---

# 5. Relationship To Nodes

Reference services are passive.

Nodes remain active.

Nodes decide:

* what to query
* what to store
* what to ignore

Reference services do not monitor nodes.

---

# 6. Relationship To Capabilities

Capabilities consume reference services.

Example:

GIS Capability

↓

queries

↓

Open GIS

Barcode Capability

↓

queries

↓

Open Barcode Database

Future capabilities integrate additional services naturally.

---

# 7. Reference Services And Place

Reference services enrich place.

Examples:

GIS

↓

Watershed

↓

Aquifer

↓

Conservation authority

↓

Stewardship opportunities

Explain relationship to the Place Model.

---

# 8. Reference Services And Symbolic Systems

Relationship to Pitchfork.

Reference services provide context.

Nodes interpret context.

Pitchfork derives symbolic frequencies.

Example:

Walk

↓

GIS

↓

Wetland

↓

Pitchfork

↓

Wetland frequency

Reference services do not perform symbolic interpretation.

---

# 9. Privacy Principles

One of the most important sections.

Reference services should:

* avoid surveillance
* avoid user profiling
* avoid advertising
* avoid behavior tracking

Queries should reveal as little personal information as practical.

Nodes should cache stable reference information whenever appropriate.

---

# 10. Governance

How reference services evolve.

Community governance.

Open standards.

Versioning.

Corrections.

Regional extensions.

Multiple implementations.

Avoid central monopolies.

---

# 11. Canonical Examples

Worked examples.

---

## Open GIS

Provides:

* watersheds
* aquifers
* parks
* ecological regions
* municipalities

---

## Open Barcode Database

Provides:

* product identity
* ingredients
* packaging
* categories
* repairability

---

## Civic Infrastructure Registry

Provides:

* water systems
* wastewater
* electricity
* waste
* transit

Supports local notifications rather than surveillance.

---

## Species Database

Provides:

* native plants
* birds
* insects
* invasive species

Supports stewardship capabilities.

---

## Recipe Registry

Provides:

* community recipes
* service recipes
* educational recipes

Nodes remain responsible for local execution.

---

# 12. Design Principles

Summarize.

Examples:

* Reference services describe the world, not people.
* Nodes remain the source of private knowledge.
* Public knowledge should remain openly accessible.
* Services should be reusable across applications.
* Services should remain modular.
* Services should support local-first computing.
* New reference services should require new data rather than new architecture.

---

# 13. Relationship To Other Documents

Boundaries.

This document defines:

* reference services
* public knowledge
* service categories
* architectural relationships

Other documents define:

* place model
* node capabilities
* symbolic frequencies
* symbolic crafting
* node infrastructure
* service exchange

Reference services become a foundational architectural layer shared across Pancakes, Pitchfork, Lone Honk, Wellness Notebook, Red Witch, and future clients. They provide a common understanding of the world while allowing each node to preserve its own autonomy, privacy, and interpretation.
