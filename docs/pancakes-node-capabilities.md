# Outline: `docs/pancakes-node-capabilities.md`

---
Authoring note (remove this note after writing the section)

This document should become the primary architectural reference for extending Pancakes nodes. It provides the mechanism by which future domains, technologies, civic practices, and forms of flourishing can be incorporated into the ecosystem while preserving a stable, privacy-respecting, and local-first node core.

One thing I'd strongly encourage adding to this document is a **"Why capabilities instead of plugins?"** subsection near the beginning.

A typical plugin system extends software. A Pancakes capability extends a **domain of life**. That's why a capability is allowed to contribute events, data models, recipes, QoL indicators, symbolic frequencies, governance hooks, and UI all at once. The unit of modularity isn't a code library—it's a coherent area of human activity or knowledge. I think that distinction will help keep the architecture focused as the ecosystem grows.
---

## Purpose

Define the capability model for Pancakes nodes.

Capabilities are the primary extension mechanism for the Pancakes ecosystem.

Rather than modifying the node core whenever new forms of flourishing, knowledge, or civic participation emerge, new capabilities can be added to extend node behavior.

This document operationalizes the Sneeds principle.

---

# 1. Introduction

## Motivation

Human flourishing evolves.

Communities discover:

* new needs
* new practices
* new technologies
* new risks
* new institutions

A healthy node architecture should adapt by adding capabilities rather than redesigning the core.

---

## Design Goals

Capabilities should:

* remain modular
* remain composable
* support local governance
* preserve privacy
* support future domains
* minimize changes to the node core

---

# 2. What Is A Capability?

Define the abstraction.

A capability extends the node's understanding of a particular domain.

Capabilities are not applications.

They provide:

* data models
* events
* APIs
* QoL indicators
* recipes
* reference-service integrations
* user interfaces
* reports
* symbolic interpretations

---

# 3. Node Core vs Capabilities

Define architectural boundaries.

## Node Core

Responsible for:

* identity
* storage
* synchronization
* governance
* permissions
* event bus
* capability management

The core should remain intentionally small.

---

## Capabilities

Responsible for domain knowledge.

Examples:

* GIS
* Barcode
* GPX
* Stewardship
* Inventory
* Pollinators
* Civic Infrastructure

---

# 4. Capability Lifecycle

Describe how capabilities behave.

Install

Configure

Enable

Disable

Upgrade

Remove

Migration

Capabilities should fail gracefully.

Nodes remain functional without optional capabilities.

---

# 5. Capability Interface

Every capability should define a common structure.

Examples:

Identity

Configuration

Permissions

Data schema

Events

Reference services

Recipes

QoL indicators

UI components

Reports

Synchronization

Version information

---

# 6. Events

Capabilities contribute event types.

Examples:

GPX

walk.completed

Barcode

product.scanned

GIS

place.relationship.discovered

Community

cleanup.completed

Pollinator

bee.observed

Capabilities extend the event vocabulary without modifying the node core.

---

# 7. Data Models

Capabilities define their own persistent data.

Examples:

Barcode inventory

Species observations

Stewardship records

Infrastructure relationships

Avoid coupling unrelated capabilities.

---

# 8. Quality Of Life Integration

Capabilities may contribute QoL indicators.

Examples:

Food security

Transit access

Park access

Pollinator habitat

Volunteer participation

Future indicators emerge through new capabilities.

---

# 9. Reference Service Integration

Capabilities consume public knowledge.

Examples:

GIS

↓

Open GIS

Barcode

↓

Open Barcode Database

Infrastructure

↓

Civic Registry

Capabilities interpret reference services for node use.

---

# 10. Recipes

Capabilities may define recipes.

Examples:

Community Cleanup

Household Garden

Pollinator Survey

Pantry Audit

Recipes become domain-specific without changing recipe architecture.

---

# 11. Symbolic Interpretation

Relationship to Pitchfork.

Capabilities may contribute symbolic frequencies.

Examples:

GIS

↓

Wetland

Forest

Watershed

Barcode

↓

Commodity

Packaging

Community

↓

Stewardship

Cooperation

Capabilities do not directly create magic.

They provide additional context.

---

# 12. Governance

Capabilities participate in governance.

Examples:

Permissions

Approval

Community adoption

Policy

Configuration

Nodes determine which capabilities are trusted.

---

# 13. Privacy

One of the most important sections.

Capabilities should:

* minimize data collection
* prefer local computation
* use reference services rather than centralized storage
* expose user controls
* degrade gracefully

Capabilities should not introduce surveillance.

---

# 14. Canonical Capabilities

Introduce example capabilities.

---

## Inventory

Household goods.

Consumables.

Tools.

---

## GPX

Walking.

Cycling.

Routes.

Activity history.

---

## GIS

Places.

Watersheds.

Aquifers.

Parks.

Stewardship geography.

---

## Barcode

Products.

Ingredients.

Packaging.

Repairability.

---

## Civic Infrastructure

Water.

Wastewater.

Electricity.

Transit.

Waste.

Public alerts.

---

## Community Quests

Volunteer opportunities.

Stewardship.

Community events.

Neighbourhood participation.

---

## Pollinator Stewardship

Species observations.

Habitat.

Native plants.

Community science.

---

## Future Capability Example

Introduce the Sneeds test.

Demonstrate that:

"Sneed Stewardship"

requires only a new capability.

No architectural redesign.

---

# 15. Capability Composition

Capabilities should cooperate.

Examples:

Walk

*

GIS

↓

Regional stewardship

Barcode

*

Recipes

↓

Household pantry

GIS

*

Infrastructure

↓

Boil water advisory

GPX

*

Community

↓

Neighbourhood cleanup recognition

Composition should occur naturally through shared events.

---

# 16. Design Principles

Summarize.

Examples:

* Capabilities extend understanding rather than replacing the core.
* The node core remains intentionally small.
* Capabilities own domain knowledge.
* Capabilities compose through shared events.
* Capabilities consume public reference services.
* Capabilities should preserve privacy.
* Capabilities should support graceful evolution.
* New forms of flourishing should require new capabilities rather than new architecture.

---

# 17. Relationship To Other Documents

Boundaries.

This document defines:

* capability architecture
* capability lifecycle
* capability composition
* capability responsibilities

Other documents define:

* place model
* reference services
* symbolic frequencies
* symbolic crafting
* node infrastructure
* recipes
* QoL

This document should become the primary architectural reference for extending Pancakes nodes. It provides the mechanism by which future domains, technologies, civic practices, and forms of flourishing can be incorporated into the ecosystem while preserving a stable, privacy-respecting, and local-first node core.
