# Pancakes Node Capabilities

## Purpose

Capabilities extend the Pancakes node with new domains of knowledge and behaviour.

The node core provides identity, storage, permissions, events, accounting, and local governance.

Capabilities introduce domain-specific concepts without requiring the core node to understand every area of life.

This document defines:

* capabilities
* capability lifecycle
* events
* domain data
* reference service integration
* capability composition
* symbolic contribution

It does **not** define symbolic meaning, projection behaviour, application interfaces, or individual capability specifications.

---

# Canonical Definition

A capability is a modular extension that teaches a Pancakes node about a particular domain.

Examples include:

* inventory
* GIS
* barcode
* repair
* pollinator stewardship
* civic infrastructure
* GPX activities
* weather
* pantry
* household maintenance

Capabilities extend the node.

They do not redefine it.

---

# Design Goals

Capabilities allow Pancakes to grow horizontally.

New domains should be introduced without:

* modifying the node core
* tightly coupling unrelated domains
* creating central application dependencies
* forcing every deployment to support every feature

A household should install only the capabilities it finds useful.

---

# Capability Responsibilities

Capabilities may define:

* events
* persistent data
* domain models
* reference service integrations
* quality-of-life indicators
* transformations
* automation
* exports
* interoperability

Capabilities should avoid owning concepts that belong elsewhere in the architecture.

---

# Lifecycle

Capabilities possess a lifecycle.

They may be:

* installed
* configured
* enabled
* disabled
* upgraded
* migrated
* removed

Nodes should remain usable when optional capabilities are absent.

Capabilities should support graceful degradation.

Stored data should remain exportable whenever practical.

---

# Events

Capabilities extend the shared event vocabulary.

Examples include:

```text
walk.completed

repair.completed

cleanup.completed

species.observed

pantry.item.added

barcode.scanned

advisory.received

story.recorded
```

Events should describe what happened.

They should not directly encode symbolic interpretation.

Events form the common language through which capabilities cooperate.

---

# Domain Models

Capabilities may define persistent domain information.

Examples include:

* inventories
* GPX tracks
* pantry contents
* repair history
* species observations
* stewardship records
* weather history
* infrastructure relationships

Domain models should remain modular.

Shared concepts should flow through events and documented interfaces rather than hidden coupling.

---

# Reference Service Integration

Capabilities consume public reference services.

Examples include:

* GIS
* barcode databases
* species databases
* civic infrastructure registries
* weather services

Reference services provide public knowledge.

Capabilities translate that knowledge into useful domain behaviour.

Private interpretation always remains inside the node.

---

# Transformations

Capabilities define transformations relevant to their domains.

Examples include:

* pantry updates
* repairs
* stewardship activities
* inventory adjustments
* educational activities
* maintenance
* observations
* household routines

Capabilities describe transformations.

Pitchfork later interprets their symbolic meaning.

This separation keeps symbolic systems independent of individual domains.

---

# Quality Of Life

Capabilities may contribute quality-of-life indicators.

Examples include:

* household resilience
* food security
* repair capacity
* learning opportunities
* park access
* transit access
* volunteer participation
* ecological stewardship

Indicators should support reflection and local decision making.

They should not become centralized scoring systems.

---

# Symbolic Contribution

Capabilities contribute context.

They do not define symbolic meaning.

For example:

A GIS capability contributes:

* watershed
* wetland
* trail
* municipality

A repair capability contributes:

* repair completed
* maintenance history

A stewardship capability contributes:

* habitat restoration
* cleanup
* monitoring

Pitchfork combines these transformations with symbolic frequencies.

Different clients later project that symbolic spectrum in different ways.

Capabilities expose domains.

They do not own symbolic interpretation.

---

# Capability Composition

Capabilities should compose naturally.

Examples include:

GPX

*

GIS

↓

Place-aware walking

Inventory

*

Barcode

↓

Pantry management

Repair

*

Inventory

↓

Household maintenance

Pollinator stewardship

*

GIS

↓

Habitat restoration

Inventory

*

Repair

*

Service Exchange

↓

Community repair services

Composition should emerge through shared events and documented interfaces rather than direct dependencies.

---

# Privacy

Capabilities are often where sensitive information first appears.

They should:

* minimize collection
* prefer local computation
* support user review
* expose meaningful permissions
* avoid unnecessary sharing
* degrade gracefully

Capabilities should preserve user agency.

---

# Governance

Nodes determine which capabilities they trust.

Governance includes:

* installation
* permissions
* upgrades
* policy
* reference sources
* removal
* migration

Capabilities may be adopted by:

* households
* schools
* cooperatives
* clinics
* guilds
* neighbourhoods
* community organizations

The architecture assumes plural local governance rather than centralized control.

---

# Relationship To Symbolic Systems

Capabilities expose domains of life.

Symbolic systems interpret those domains.

Example:

```text id="kb5k5z"
Repair capability

↓

repair.completed

↓

Pitchfork

repair
craftsmanship
continuity

↓

Projection

Commerce
Wellness
RPG
Ambient world
```

Capabilities should never hard-code magical resources, symbolic frequencies, or projection-specific behaviour.

Those belong to Pitchfork.

---

# Relationship To Applications

Applications combine capabilities into coherent user experiences.

Examples include:

* Red Witch
* Lone Honk
* household dashboards
* service exchange
* Woodland Commons
* future educational clients

Applications determine user experience.

Capabilities provide reusable domain foundations.

---

# Design Principles

Capabilities extend rather than replace the node.

Domains should remain modular.

Composition should occur through shared events.

Public knowledge should remain separate from private interpretation.

Symbolic systems should remain independent of domain implementations.

Capabilities should preserve user agency, privacy, and local governance.

---

# Non-Goals

Capabilities are not:

* application stores
* advertising platforms
* centralized business logic
* symbolic interpreters
* projection engines
* governance authorities
* payment systems
* mandatory components

The node core should remain small.

Capabilities should not become excuses to move every feature into the core architecture.

---

# Examples

An inventory capability manages household goods and pantry items.

A GIS capability understands watersheds, trails, parks, and conservation areas.

A repair capability records maintenance and completed repairs.

A stewardship capability records restoration, monitoring, cleanup, and habitat work.

A pollinator capability supports species observations and ecological knowledge.

A service exchange capability coordinates community services without redefining accounting or symbolic systems.

Each capability contributes transformations and domain knowledge.

Shared symbolic interpretation occurs later through Pitchfork.

---

# What Later Documents Should Reference

Later documents should reference this article whenever they require canonical language for:

* capabilities
* capability lifecycle
* events
* domain models
* capability composition
* reference service integration
* quality-of-life indicators
* privacy
* governance
* the boundary between capabilities and symbolic systems

Application documents should define individual capabilities and user experiences.

They should not redefine the capability architecture.
