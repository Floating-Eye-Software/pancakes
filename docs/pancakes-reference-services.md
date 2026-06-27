# Pancakes Reference Services

## Purpose

Reference services provide shared public knowledge that Pancakes nodes can use without centralizing private household or personal information.

Reference services answer questions about the world.

They do not answer questions about people.

This document defines:

* reference services
* public knowledge
* reference service families
* the relationship between reference services, nodes, capabilities, place, and symbolic systems

It does **not** define symbolic meaning, GIS implementation, application behaviour, or private household storage.

---

# Canonical Definition

A reference service is an open or community-governed source of stable public knowledge.

Examples include:

* this coordinate belongs to this watershed
* this barcode identifies this product
* this trail is maintained by this authority
* this species is native here
* this public water system has an advisory
* this school belongs to this district

Reference services describe the shared world.

They do not describe individual lives.

---

# Public Knowledge And Private Knowledge

Pancakes deliberately separates public knowledge from private interpretation.

Public knowledge includes:

* geography
* products
* species
* infrastructure
* public alerts
* standards
* educational material
* repair information
* public recipes

Private knowledge includes:

* household inventories
* journals
* health information
* walks
* routines
* stewardship history
* preferences
* local governance
* symbolic history

Nodes combine both locally.

```text id="9a0xyv"
Private transformation

+

Public reference knowledge

↓

Local meaning
```

Meaning belongs to the node.

Not the reference service.

---

# Reference Service Families

Reference services organize public knowledge into reusable domains.

---

## Geographic

Examples include:

* watersheds
* aquifers
* municipalities
* parks
* trails
* conservation areas
* ecological regions

---

## Goods

Examples include:

* barcodes
* ingredients
* packaging
* repairability
* recycling
* commodity identity
* standards

---

## Civic Infrastructure

Examples include:

* water systems
* wastewater
* transit
* libraries
* schools
* public health
* waste collection
* emergency alerts

---

## Ecological

Examples include:

* species
* habitats
* pollinators
* migration routes
* native plants
* invasive species
* restoration guidance

---

## Knowledge

Examples include:

* educational resources
* standards
* public datasets
* repair manuals
* community-maintained recipes
* safety guidance

---

Future domains might include:

* weather
* astronomy
* geology
* accessibility
* heritage
* agriculture
* energy
* public transportation

The architecture should remain open to future domains.

---

# Relationship To Nodes

Reference services are passive.

Nodes are active.

Reference services answer questions.

Nodes decide:

* what to ask
* what to remember
* what to ignore
* what to combine
* what to share

Nodes should prefer:

* local caches
* downloaded datasets
* regional mirrors
* offline operation

when those approaches improve privacy and resilience.

---

# Relationship To Capabilities

Capabilities consume reference services.

Examples include:

* GIS
* barcode
* pollinator stewardship
* civic infrastructure
* inventory
* weather

Capabilities translate public knowledge into domain-specific behaviour.

Reference services remain application-independent.

---

# Relationship To Place

Reference services describe places.

Nodes relate to places.

GIS may identify:

* watersheds
* parks
* trails
* municipalities
* conservation authorities

The node determines whether those relationships matter.

Place remains a local relationship rather than a centralized profile.

---

# Relationship To Symbolic Systems

Reference services do not produce symbolic meaning.

They expose public structure.

For example:

```text id="2d2n8y"
Reference service

"This location is inside a wetland."

↓

Node

"A stewardship walk occurred here."

↓

Pitchfork

movement
wetland
stewardship

↓

Projection

Ember Moss
```

The wetland is public knowledge.

The walk is private.

The symbolic spectrum emerges locally.

The RPG projection occurs later.

These responsibilities should remain separate.

---

# Relationship To Quality Of Life

Reference services support quality-of-life understanding.

Examples include:

* food access
* transit
* parks
* libraries
* air quality
* flood risk
* repair resources
* public services

Reference services expose conditions.

Nodes determine personal relevance.

Quality-of-life interpretation remains local.

---

# Privacy Principles

Reference services should minimize personal information exposure.

Prefer:

* anonymous queries
* local caches
* downloadable datasets
* regional mirrors
* coarse queries
* versioned snapshots

Avoid:

* behavioural tracking
* household registries
* advertising identifiers
* persistent user profiling
* unnecessary query logging

Reference services should not become surveillance infrastructure.

---

# Governance

Reference services should support:

* open formats
* versioning
* provenance
* correction processes
* plural governance
* regional extensions
* multiple implementations
* public documentation

Communities should be free to operate trusted mirrors or alternative implementations.

No single organization should own public knowledge.

---

# Design Principles

Public knowledge should remain reusable.

Meaning should emerge locally.

Reference services should expose facts rather than interpretations.

Private household history should remain private.

Reference services should compose naturally with capabilities.

Plural implementations should be encouraged.

---

# Non-Goals

Reference services are not:

* social networks
* advertising platforms
* identity providers
* payment processors
* household databases
* symbolic interpreters
* AI assistants
* centralized node registries

Reference services also do not replace community authority.

Some ecological, Indigenous, historical, or cultural knowledge requires governance beyond what a generic public reference service should publish.

---

# Examples

An open GIS service identifies watersheds, parks, municipalities, trails, and ecological regions.

A barcode database identifies products, ingredients, repairability, packaging, and recycling guidance.

A civic infrastructure registry identifies water systems, transit agencies, public health regions, and emergency alerts.

A species database identifies native plants, pollinators, habitats, and invasive species.

A repair knowledge service publishes repair manuals, maintenance guidance, and replacement part information.

A public recipe registry publishes recipes for food preparation, repair, education, stewardship, and community practices.

Nodes combine these public facts with local transformations to produce meaningful local interpretations.

---

# What Later Documents Should Reference

Later documents should reference this article whenever they require canonical language for:

* reference services
* public knowledge
* private interpretation
* reference service families
* privacy-preserving public lookup
* public infrastructure
* open reference data
* the boundary between reference services and symbolic systems

Application documents should describe concrete datasets, APIs, and client behaviour.

They should not redefine the reference service architecture.
