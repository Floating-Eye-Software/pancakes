# Outline: `docs/pancakes-place-model.md`

## Purpose

Define "place" as a first-class concept within the Pancakes ecosystem.

Nodes, households, recipes, services, and stewardship all occur somewhere. The place model provides a shared vocabulary for understanding the ecological, civic, historical, and social context of those activities.

This document defines what places are and how they relate to nodes.

It does **not** define GIS implementation details or symbolic crafting rules.

---

# 1. Introduction

## Motivation

People do not flourish in abstract space.

They flourish in homes, neighbourhoods, watersheds, ecosystems, and communities.

Pancakes therefore models places as meaningful relationships rather than merely coordinates.

---

## Design Goals

* encourage stewardship
* strengthen local identity
* support ecological awareness
* preserve privacy
* support local-first computing
* avoid surveillance
* remain globally applicable

---

# 2. What Is A Place?

Define place.

A place is more than a point on a map.

It consists of overlapping relationships.

Examples:

* ecological
* historical
* civic
* cultural
* economic
* social

Places have identities independent of any individual user.

---

# 3. Nodes Have Homelands

Introduce the major new idea.

Nodes may optionally define a homeland.

This is **not** continuous location tracking.

It is a statement that:

> This node belongs here.

Discuss:

* households
* organizations
* schools
* neighbourhood groups
* cooperatives

---

## Homeland Is Optional

Support:

* mobile households
* travelling users
* privacy-sensitive deployments

Nodes remain functional without place information.

---

# 4. Place Relationships

A node may relate to many places.

Examples:

Home

Favourite park

Walking trail

Library

Community garden

School

Creek

Transit station

Market

Volunteer organization

Relationships are meaningful.

Not merely bookmarks.

---

# 5. Layers Of Place

Introduce the layered model.

---

## Ecological

Examples:

* watershed
* aquifer
* biome
* forest
* wetland
* coastline

---

## Geological

Examples:

* escarpment
* bedrock
* soil
* floodplain

---

## Civic

Examples:

* municipality
* ward
* conservation authority
* transit agency
* school board
* library system

---

## Historical

Examples:

* neighbourhood history
* industrial history
* settlement history
* archaeological context

---

## Cultural

Examples:

* festivals
* public art
* local traditions
* languages

---

## Indigenous Context

Traditional territories.

Treaties.

Indigenous place names.

Important guidance:

These are contextual relationships.

They are **not** game resources.

Do not gamify Indigenous identity or territory.

---

# 6. Place And Stewardship

Introduce stewardship.

Nodes may choose places they actively care for.

Examples:

* neighbourhood cleanup
* invasive species removal
* community gardens
* bird monitoring
* creek restoration

Stewardship is relational.

Not ownership.

---

# 7. Place And Quality Of Life

Place contributes to node understanding.

Examples:

Nearby parks

Libraries

Transit

Water quality

Flood risk

Food access

Air quality

Walkability

QoL indicators should support households rather than centralized surveillance.

---

# 8. Place And Symbolic Ecology

Relationship to Pitchfork.

Places contribute symbolic context.

Examples:

Wetlands

↓

Wetland frequencies

Forest

↓

Forest frequencies

Place enriches symbolic interpretation without replacing activities.

Refer readers to symbolic frequencies.

---

# 9. Place And Community

Communities emerge in places.

Examples:

Neighbourhood associations

Conservation groups

Volunteer organizations

Mutual aid

Markets

Libraries

Parks

Explain why locality matters.

---

# 10. Place And Infrastructure

Introduce infrastructure relationships.

Examples:

Water source

Wastewater treatment

Electric utility

Garbage

Transit

Food distribution

Healthcare

These relationships help nodes understand how households are connected to civic systems.

Do not imply continuous monitoring.

---

# 11. Place And Reference Services

Reference the future reference-service architecture.

Examples:

GIS

Species database

Civic infrastructure

Open barcodes

Reference services provide knowledge.

Nodes retain agency.

---

# 12. Privacy

One of the most important sections.

Explain:

Nodes should understand place.

They should not continuously report movement.

Relationship-based.

Not surveillance-based.

Homeland

≠

tracking.

---

# 13. Examples

Worked examples.

---

## Household Node

Home

↓

Watershed

↓

Aquifer

↓

Conservation authority

↓

Community garden

---

## Stewardship

Node adopts:

Mason Road Park

Receives:

community cleanup opportunities

local restoration events

bird surveys

---

## Lone Honk

Player explores:

Duffins Creek

Node learns:

place relationship

Pitchfork interprets:

wetland frequencies

---

## Boil Water Advisory

Reference service reports:

boil water advisory

↓

Relevant nodes understand:

their household is affected

without exposing private information.

---

# 14. Design Principles

Summarize.

Examples:

* Places are relationships, not coordinates.
* Stewardship is more important than ownership.
* Local knowledge should remain local.
* Place enriches meaning rather than restricting participation.
* Nodes should understand where they belong.
* Indigenous history should be acknowledged respectfully without becoming gameplay.
* Public reference data should remain separate from private household information.

---

# 15. Relationship To Other Documents

Explain boundaries.

This document defines:

* place
* homeland
* stewardship
* locality
* infrastructure relationships

Other documents define:

* GIS implementation
* reference services
* node capabilities
* symbolic frequencies
* symbolic crafting

The place model becomes the canonical conceptual definition of locality throughout the Pancakes ecosystem. It provides the vocabulary that allows nodes, reference services, community quests, and the Pitchfork symbolic economy to share a consistent understanding of place without coupling them to any specific application or technology.
