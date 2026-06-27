# Pancakes Place Model

## Purpose

Place is a first-class concept in Pancakes.

Every household, service, recipe, transformation, stewardship activity, quality-of-life indicator, and symbolic projection exists in relationship to places.

The place model provides a shared language for ecological, civic, historical, cultural, and infrastructural relationships while preserving privacy and avoiding surveillance.

This document defines:

* place
* homeland
* place relationships
* stewardship
* place memory
* symbolic place identity

It does **not** define GIS implementation, live location tracking, mapping interfaces, or symbolic crafting behaviour.

---

# Canonical Definition

A place is a meaningful relationship rather than merely a coordinate.

Coordinates identify locations.

Places describe the web of relationships surrounding those locations.

Examples include:

* watersheds
* neighbourhoods
* libraries
* wetlands
* markets
* conservation areas
* schools
* clinics
* trails
* community gardens

A place has identity independent of any particular user.

Nodes relate to places.

They do not own them.

---

# Homelands

A node may optionally define a homeland.

A homeland is a durable relationship between a node and one or more places.

It expresses belonging, responsibility, familiarity, or ongoing participation.

A homeland does **not** imply continuous tracking.

A node can possess a homeland without revealing its address, publishing movement history, or participating in real-time location services.

Homelands may belong to:

* households
* schools
* cooperatives
* libraries
* clinics
* guilds
* neighbourhood organizations
* farms
* community groups

Homeland remains optional.

Travelling users, mobile deployments, privacy-sensitive households, and purely virtual services must remain fully supported.

---

# Place Relationships

Nodes may relate to many places.

Examples include:

* home
* workplace
* library
* creek
* workshop
* trail
* market
* favourite park
* community garden
* food bank
* transit station
* repair café

These relationships determine which public knowledge, stewardship opportunities, community practices, and quality-of-life indicators may become relevant.

Relationships should remain:

* explicit
* reviewable
* locally governed
* removable
* privacy preserving

The node decides which relationships matter.

---

# Layers Of Place

Places possess many overlapping identities.

## Ecological

Examples include:

* watershed
* aquifer
* wetland
* forest
* coastline
* habitat
* migration corridor
* conservation area

---

## Geological

Examples include:

* escarpment
* bedrock
* soil
* river valley
* floodplain
* erosion zone

---

## Civic

Examples include:

* municipality
* ward
* school board
* transit agency
* library system
* conservation authority
* public health region
* water utility

---

## Historical

Examples include:

* neighbourhood history
* industrial history
* archaeological sites
* heritage buildings
* former land use
* community memory

---

## Cultural

Examples include:

* festivals
* markets
* public art
* local traditions
* languages
* gathering places
* institutions

---

## Indigenous Context

Traditional territories, treaty relationships, Indigenous place names, stewardship knowledge, and governance relationships are important contextual knowledge.

The place model should support respectful recognition.

It must never convert Indigenous knowledge into game mechanics, ownership claims, or symbolic rewards.

---

# Stewardship

Stewardship is a relationship of care.

A node may choose to care for:

* parks
* streams
* libraries
* trails
* gardens
* streets
* neighbourhoods
* habitats
* public infrastructure

Stewardship includes activities such as:

* restoration
* cleanup
* maintenance
* education
* accessibility work
* mutual aid
* habitat monitoring
* community gardening

Stewardship does not imply ownership.

It represents ongoing responsibility and attention.

---

# Place Memory

Places accumulate history.

Every meaningful transformation contributes to the symbolic identity of a place.

Examples include:

* repeated stewardship
* festivals
* workshops
* teaching
* restoration
* storytelling
* repair
* celebration
* community meals

A workshop develops craftsmanship.

A woodland develops stewardship.

A library develops learning.

A commons develops hospitality and civic participation.

Place therefore possesses symbolic memory.

This memory arises through accumulated transformations rather than being assigned by designers.

---

# Place And Symbolic Meaning

Place contributes symbolic context.

Transformations also contribute symbolic history back to the place.

This relationship is reciprocal.

```text
Place

↓

Transformation

↓

Symbolic spectrum

↓

Place memory
```

A walk through a wetland gains ecological context.

Repeated stewardship also strengthens the symbolic identity of that wetland.

Neither relationship replaces the other.

---

# Place And Quality Of Life

Places influence flourishing.

Examples include:

* nearby parks
* food access
* libraries
* transit
* walkability
* flood risk
* air quality
* repair access
* community services
* public health alerts

Quality-of-life indicators should support local decision making.

They must not become centralized ranking or profiling systems.

---

# Place And Infrastructure

Nodes relate to civic and ecological infrastructure.

Examples include:

* drinking water
* wastewater
* electrical grid
* recycling
* waste collection
* transit
* conservation authority
* public health
* emergency alerts
* food systems

Understanding these relationships allows a node to interpret public events locally.

A boil-water advisory matters because the node understands its water relationship.

The advisory service does not need to know the household.

---

# Relationship To Reference Services

Reference services provide public knowledge.

Examples include:

* GIS
* civic registries
* ecological databases
* species references
* public datasets

Reference services answer questions about places.

Nodes combine those public facts with local relationships and private history.

Meaning emerges locally.

---

# Relationship To Symbolic Systems

Places contribute symbolic frequencies.

Transformations occurring within places contribute symbolic history.

Later projections may interpret that symbolic history in many different ways.

Examples include:

* RPG environments
* ambient worlds
* stewardship indicators
* community archives
* educational clients

No projection owns the meaning of a place.

---

# Design Principles

Places are relationships.

Relationships matter more than coordinates.

Stewardship matters more than ownership.

Place identity should emerge from accumulated transformations.

Privacy should be preserved.

Meaning should remain local whenever possible.

Public knowledge and private interpretation should remain separate.

---

# Non-Goals

This document does not define:

* live tracking
* surveillance
* geofencing
* advertising profiles
* centralized household registries
* game rewards
* symbolic crafting rules
* mapping UI
* routing algorithms

It also does not define Indigenous governance, treaty interpretation, or cultural authority.

Those remain matters for the appropriate communities and institutions.

---

# Examples

A household declares a homeland connected to a watershed, library system, conservation authority, and community garden.

A stewardship capability records participation in habitat restoration.

The activity contributes stewardship, ecological, and place relationships while preserving household privacy.

A workshop hosting regular repair events gradually develops a symbolic identity centred on craftsmanship, mentoring, and community resilience.

A Speakers' Corner accumulates memory through stories shared over many years.

A community commons develops hospitality, celebration, learning, and civic participation through repeated transformations rather than by design alone.

A boil-water advisory becomes relevant because the node understands its infrastructure relationships without revealing private household information.

---

# What Later Documents Should Reference

Later documents should reference this article whenever they require canonical language for:

* place
* homeland
* stewardship
* place relationships
* place memory
* layered place identity
* symbolic place meaning
* infrastructure relationships
* quality-of-life context
* privacy-preserving place systems

Application documents should describe how individual clients use place.

They should not redefine what place means within Pancakes.
