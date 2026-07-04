# Pancakes Node Capabilities

## Status

Foundational

Companion to:

* Pancakes Overview
* Pancakes Node Architecture
* Pancakes Product Composition
* Pancakes Place Model
* Pancakes Reference Services
* Pancakes Information Sources
* Pancakes Appliance Design
* Pitchfork Overview
* Pitchfork Client API

---

# Purpose

This document defines the capability model used throughout the Pancakes ecosystem.

Capabilities are the primary mechanism by which Pancakes nodes acquire new behavior.

Rather than continually expanding the responsibilities of the node itself, Pancakes grows by composing reusable capabilities that model human activities, institutions, services, and integrations.

This document defines:

* capabilities
* capability categories
* capability discovery
* capability composition
* capability dependencies
* capability lifecycle

It does **not** define individual products, user interfaces, deployment models, or application-specific behavior.

---

# Core Principle

```text
Nodes govern.

Capabilities provide behavior.

Reference services describe the world.

Information sources observe the world.

Pitchfork accounts.

Products compose capabilities.

Clients present experiences.
```

The node should remain stable while capabilities evolve.

---

# Why Capabilities Exist

Human life continuously develops new needs.

Communities invent new institutions.

Technology introduces new possibilities.

Future generations will almost certainly discover new forms of flourishing that cannot be anticipated today.

Rather than redesigning Pancakes whenever this occurs, new domains should normally appear as new capabilities.

Capabilities are therefore the primary extension mechanism for the ecosystem.

The architecture should require:

```text
new capability
```

rather than:

```text
new node architecture
```

when new domains emerge.

This is the architectural motivation behind the Sneeds principle.

---

# Canonical Definition

A capability is a reusable, discoverable service that extends the behavior of a Pancakes node.

Capabilities may:

* expose APIs
* consume node infrastructure
* consume Pitchfork services
* consume reference services
* consume information sources
* produce events
* expose projections
* participate in product compositions

Capabilities are reusable.

They are not complete applications.

---

# Relationship To Nodes

Nodes provide governance.

Nodes determine:

* identity
* permissions
* storage
* retention
* audit
* synchronization
* policy
* exports
* capability installation

Capabilities operate within those boundaries.

Capabilities do not replace node governance.

They extend node behavior.

---

# Relationship To Products

Products are compositions of capabilities.

For example:

```text
Household Management

↓

Household
Recipes
Calendar
Inventory
Notifications
Pitchfork
```

Another product may reuse many of the same capabilities.

Capabilities are intended to be shared across products whenever practical.

---

# Relationship To Clients

Clients provide interfaces.

Capabilities provide behavior.

Multiple clients may consume the same capability.

Examples include:

* desktop clients
* mobile applications
* web interfaces
* ambient displays
* dashboards
* command-line tools
* voice interfaces

Clients should avoid duplicating capability logic.

---

# Relationship To Pitchfork

Pitchfork provides settlement, contracts, symbolic accounting, recipes, projections, and economic infrastructure.

Capabilities may submit events to Pitchfork.

Capabilities may consume projections.

Capabilities should not create independent accounting systems.

Pitchfork remains the shared accounting substrate.

---

# Capability Categories

Capabilities fall into three broad architectural categories.

These categories describe responsibility rather than implementation.

---

## Infrastructure Capabilities

Infrastructure capabilities provide reusable platform services.

They make the node itself useful.

Examples include:

* Identity
* Permissions
* Storage
* Search
* Notifications
* Scheduler
* Synchronization
* Audit
* Export
* Media Storage
* Projection Engine
* Policy Engine
* Appliance Registry

Infrastructure capabilities generally do not model human activities.

They provide services used by other capabilities.

Example:

```text
Identity

↓

Permission Check

↓

Storage

↓

Audit
```

Most nodes require many infrastructure capabilities regardless of which products they host.

---

## Domain Capabilities

Domain capabilities model human activities, institutions, and forms of stewardship.

Most Pancakes functionality belongs here.

Examples include:

* Household
* Journal
* Recipes
* Inventory
* Calendar
* Service Exchange
* Contracts
* Questing
* Gardening
* Stewardship
* Governance
* Wellness
* Red Witch
* Memory Archive
* Quality of Life Signals
* Symbolic Crafting

Domain capabilities represent meaningful areas of human life.

They should remain reusable across products.

Example:

```text
Garden

plant()

harvest()

water()

observe()

maintain()
```

---

## Integration Capabilities

Integration capabilities connect Pancakes nodes to external systems.

Examples include:

* Weather
* Astronomy
* Email
* Bitcoin
* Lightning
* Google Calendar
* Barcode Lookup
* GIS
* Environmental Sensors
* Resonance
* Mastodon
* Public Data Feeds

Integration capabilities translate between Pancakes and external systems.

They should avoid embedding external assumptions into the core architecture.

External technologies should remain replaceable.

---

# Capability Relationships

The three capability categories naturally depend upon one another.

```text
Infrastructure

↓

Domain

↓

Integration
```

Infrastructure capabilities provide reusable services.

Domain capabilities model human activities.

Integration capabilities connect those activities to the outside world.

The preferred dependency direction is downward.

Infrastructure capabilities should not depend upon domain-specific behavior.

---

# Capability Discovery

Capabilities should be discoverable.

Nodes should advertise:

* capability identity
* version
* category
* supported operations
* required permissions
* supported data classes
* dependencies
* operational status

Clients should discover capabilities rather than assuming every node provides identical functionality.

This allows different nodes to expose different feature sets while preserving compatibility.

---

# Capability APIs

Capabilities expose reusable domain APIs.

Example:

```text
Inventory

record_item()

consume_item()

transfer_item()

search_items()
```

Example:

```text
Calendar

create_event()

cancel_event()

schedule_recurring()

list_events()
```

Example:

```text
Garden

plant()

harvest()

water()

record_observation()
```

Products consume these APIs rather than reimplementing them.

---

# Capability Dependencies

Capabilities may depend upon:

* infrastructure capabilities
* other capabilities
* Pitchfork
* reference services
* information sources

Dependencies should be explicit.

A capability should declare:

Required capabilities.

Optional capabilities.

Required reference services.

Required information sources.

Required permission scopes.

This allows graceful degradation when optional services are unavailable.

---

# Capability Composition

Capabilities are intended to be composed.

Example:

```text
Household Management

Household
Recipes
Inventory
Calendar
Notifications
Quality of Life
Pitchfork
```

Example:

```text
Pitchfork RPG

Questing
Inventory
Crafting
Recipes
Projection
Pitchfork
```

Example:

```text
Service Exchange

Contracts
Scheduling
Messaging
Payments
Pitchfork
```

Products compose capabilities.

Capabilities remain reusable.

---

# Relationship To Reference Services

Reference services provide public knowledge.

Capabilities consume that knowledge.

Examples include:

* place information
* species databases
* barcode registries
* civic infrastructure
* ecological data

Capabilities interpret reference information within their own domains.

Reference services remain application-independent.

---

# Relationship To Information Sources

Information sources produce observations.

Capabilities consume observations.

Examples include:

* weather
* environmental sensors
* astronomical calculations
* wearable devices
* public data feeds

Capabilities determine whether observations are relevant to their domain.

Observations do not automatically become meaningful events.

---

# Capability Events

Capabilities often produce events.

Examples include:

```text
meal_prepared

loop_completed

garden_watered

tool_checked_out

service_completed

story_recorded
```

Events may later be submitted to Pitchfork for settlement.

Not every internal operation requires a Pitchfork event.

---

# Capability Permissions

Capabilities operate within node governance.

Capabilities should declare:

* required permission scopes
* supported data classes
* projection permissions
* administrative requirements

Nodes determine whether those permissions are granted.

Capabilities should never bypass node governance.

---

# Capability Lifecycle

Capabilities normally progress through the following lifecycle.

```text
Design

↓

Installation

↓

Discovery

↓

Configuration

↓

Permission

↓

Operation

↓

Upgrade

↓

Deprecation

↓

Removal
```

Nodes should support capability evolution without disrupting unrelated capabilities.

---

# Capability Versioning

Capabilities evolve independently.

Nodes should support:

* installation
* upgrades
* migration
* deprecation
* compatibility information

Products should discover capability versions rather than assuming a particular implementation.

---

# Capability Manifest

Every capability should expose a declarative description of its requirements and behavior.

Example:

```yaml
capability: garden

category: domain

depends_on:
  - identity
  - permissions
  - storage
  - pitchfork

optional:
  - notifications
  - place

reference_services:
  - species
  - weather

information_sources:
  - rainfall
  - soil_moisture

events:
  - plant_seeded
  - harvest_completed

projections:
  - stewardship
```

The manifest allows nodes to validate compatibility before installation.

---

# Design Principles

Capabilities should be:

* reusable
* composable
* discoverable
* permission-aware
* event-oriented
* API-first
* independently versioned
* replaceable
* gracefully degradable

Capabilities should prefer cooperation over duplication.

---

# The Sneeds Test

The capability architecture should remain adaptable.

When a new domain emerges, the preferred response should be:

```text
Add a new Domain capability.
```

When a new external system appears:

```text
Add a new Integration capability.
```

When new reusable platform services become necessary:

```text
Add a new Infrastructure capability.
```

The architecture should rarely require changes to the node itself.

A healthy architecture grows through capabilities rather than structural redesign.

---

# Non-Goals

Capabilities are not:

* complete products
* user interfaces
* deployment environments
* governance authorities
* reference services
* information sources
* appliances
* accounting systems

Those concepts remain separate architectural responsibilities.

---

# Relationship To Other Documents

**Pancakes Node Architecture** defines governance and runtime boundaries.

**Pancakes Product Composition** explains how capabilities are assembled into complete products.

**Pancakes Reference Services** defines shared public knowledge consumed by capabilities.

**Pancakes Information Sources** defines observations consumed by capabilities.

**Pancakes Appliance Design** defines physical and virtual deployment units that host or extend nodes.

**Pitchfork** provides settlement, contracts, recipes, resources, and projections used by capabilities.

---

# Open Questions

* Which infrastructure capabilities are mandatory for every node?
* Should capabilities be installable packages?
* Can nodes publish capability profiles for households, clinics, schools, and cooperatives?
* How should capabilities declare compatibility across versions?
* Should third parties publish community capability repositories?
* How should capabilities express optional versus required dependencies?
* Which capabilities should be considered canonical for every Pancakes deployment?

---

# Final Principle

A Pancakes node should remain small, stable, and governable.

Everything that changes rapidly—new domains, new institutions, new services, new integrations, and new forms of flourishing—should emerge through reusable capabilities.

The ecosystem should grow by composition rather than by continually expanding the responsibilities of the node itself.
