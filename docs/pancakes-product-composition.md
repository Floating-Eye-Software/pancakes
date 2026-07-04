# Pancakes Product Composition

## Status

Foundational

Companion to:

* Pancakes Overview
* Pancakes Node Architecture
* Pancakes Node Capabilities
* Pancakes Place Model
* Pancakes Reference Services
* Pancakes Information Sources
* Pancakes Appliance Design
* Pitchfork Overview
* Pitchfork Client API

---

# Purpose

This document defines how complete Pancakes products are assembled from reusable architectural components.

Pancakes is not a collection of unrelated applications.

It is a compositional platform.

Products emerge through the composition of reusable capabilities operating within a governed node.

This document defines:

* products
* composition
* product boundaries
* composition layers
* deployment patterns
* client relationships

It does **not** define individual product behavior or user interfaces.

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

Every layer has a distinct responsibility.

Products exist to assemble those responsibilities into coherent experiences.

---

# Why Products Exist

Capabilities are intentionally small.

Each capability models a reusable area of behavior.

Users, however, interact with complete experiences.

A household does not install "Inventory."

A household installs Household Management.

A cooperative does not install "Contracts."

A cooperative installs Service Exchange.

Products provide coherent human-centered experiences by composing reusable capabilities.

---

# Canonical Definition

A Pancakes product is a coherent composition of:

* a governing node
* one or more capabilities
* optional reference services
* optional information sources
* Pitchfork services
* optional appliances
* one or more clients

Products define user-facing domains.

Nodes define governance.

Capabilities define behavior.

Clients provide interfaces.

---

# Composition Layers

Products occupy a specific position within the architecture.

```text
Clients

↓

Products

↓

Capabilities

↓

Pitchfork

↓

Node

↓

Infrastructure
```

Each layer should remain independent.

Changes at one layer should rarely require redesign of another.

---

# Architectural Building Blocks

Products are composed from reusable architectural elements.

---

## Nodes

Every product operates within a node.

The node provides:

* identity
* permissions
* storage
* retention
* audit
* synchronization
* governance
* policy

The node owns governance.

Products never replace it.

---

## Capabilities

Capabilities provide reusable behavior.

Examples include:

* Household
* Inventory
* Calendar
* Recipes
* Contracts
* Questing
* Notifications
* Stewardship
* Journals
* Memory Archive

Products compose capabilities.

Capabilities remain reusable.

---

## Pitchfork

Pitchfork provides shared accounting.

Products may use:

* events
* settlement
* recipes
* contracts
* symbolic resources
* projections

Products should avoid creating independent accounting systems.

---

## Reference Services

Reference services provide public knowledge.

Examples include:

* places
* products
* species
* civic infrastructure
* repair knowledge
* ecological information

Products consume reference knowledge when appropriate.

Reference services remain application-independent.

---

## Information Sources

Information sources provide observations.

Examples include:

* weather
* astronomy
* sensors
* public data feeds
* environmental monitoring
* wearable devices

Products consume observations through capabilities.

Observations remain distinct from meaning.

---

## Appliances

Appliances are optional deployment units.

Examples include:

* household node appliance
* Speakers' Corner
* workshop station
* garden station
* BLE loop sensor
* community display

Products may support appliances.

Products are not appliances.

---

## Clients

Clients provide user interfaces.

Examples include:

* mobile applications
* desktop applications
* dashboards
* web interfaces
* ambient displays
* command-line tools
* voice interfaces

Multiple clients may expose the same product.

---

# Product Composition

Products are primarily compositions of capabilities.

Example:

```text
Household Management

Household
Inventory
Recipes
Calendar
Notifications
Quality of Life
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

Example:

```text
Pitchfork RPG

Questing
Crafting
Inventory
Recipes
Projection
Pitchfork
```

The product owns the composition.

The capabilities remain reusable.

---

# Product Lifecycle

Products typically initialize using the following sequence.

```text
Resolve Node

↓

Establish Identity

↓

Load Node Policy

↓

Discover Capabilities

↓

Discover Reference Services

↓

Discover Information Sources

↓

Obtain Permissions

↓

Begin Operation
```

Products should adapt to the capabilities available on the active node.

---

# Product Patterns

Several common composition patterns exist.

---

## Standalone Product

A lightweight composition.

Usually:

* few capabilities
* one client
* limited projections

---

## Composite Product

The most common pattern.

Several reusable capabilities cooperate to create one experience.

Examples include:

* Household Management
* Service Exchange

---

## Community Product

Designed for cooperatives and communities.

Typically includes:

* shared governance
* shared appliances
* community projections
* stewardship capabilities

---

## Institutional Product

Designed for clinics, schools, libraries, and organizations.

Often emphasizes:

* permissions
* audit
* retention
* governance
* reporting

The underlying capability model remains unchanged.

---

# Multiple Clients

A product may expose multiple interfaces.

Example:

```text
Household Management

├── Mobile App
├── Kitchen Display
├── Desktop Dashboard
├── Ambient Display
└── Administration Console
```

These remain one product.

They consume the same capabilities.

---

# Capability Discovery

Products should discover capabilities rather than assuming every node provides identical functionality.

Some capabilities may be required.

Others may be optional.

Example:

```text
Household Management

Required

Household
Calendar

Optional

Weather
Notifications
GIS
```

Graceful degradation should be preferred whenever possible.

---

# Composition Manifest

Products should describe themselves declaratively.

Example:

```yaml
product: household-management

requires:

  capabilities:
    - household
    - inventory
    - recipes
    - calendar

optional:

  capabilities:
    - notifications
    - qol

reference_services:
  - place
  - products

information_sources:
  - weather

clients:
  - mobile
  - dashboard

projections:
  - wellness
  - symbolic
```

The composition manifest allows nodes to determine whether a product can operate.

---

# Deployment Is Not Composition

Deployment and composition should remain separate concepts.

For example:

```text
Woodland Commons

↓

Household Node
Commons Node

↓

Products

↓

Clients

↓

Appliances
```

Woodland Commons is not a product.

It is a deployment containing many products.

Similarly, a clinic may deploy:

* Service Exchange
* Wellness
* Memory Archive
* Governance

The deployment contains products.

The products remain independently composable.

---

# Product Boundaries

Products should not duplicate:

* node governance
* identity
* permissions
* storage
* settlement
* reference services
* information sources

Those responsibilities belong elsewhere.

Products assemble.

They do not redefine.

---

# Design Principles

Products should be:

* compositional
* capability-oriented
* node-governed
* Pitchfork-compatible
* reusable
* discoverable
* modular
* independently deployable
* gracefully degradable

Products should express human purposes rather than technical layers.

---

# The Sneeds Test

Suppose society discovers a completely new domain.

The preferred solution should be:

```text
New capability

↓

Existing product composition
```

or

```text
New capability

↓

New product
```

The architecture should rarely require redesigning the node.

Products should evolve through composition.

---

# Relationship To Other Documents

**Pancakes Node Architecture** defines governance boundaries.

**Pancakes Node Capabilities** defines reusable behavioral services.

**Pancakes Reference Services** defines reusable public knowledge.

**Pancakes Information Sources** defines observations.

**Pancakes Appliance Design** defines deployment hardware and virtual infrastructure.

**Pitchfork** defines settlement, contracts, resources, recipes, and projections.

This document explains how those architectural components become complete Pancakes products.

---

# Open Questions

* Should products themselves be installable packages?
* Can products declare optional feature profiles?
* How should products advertise compatible clients?
* Should products expose standard health and readiness endpoints?
* Should products be versioned independently of capabilities?
* How should community-developed product bundles be distributed?
* What is the canonical product manifest format?

---

# Final Principle

Pancakes grows by composition.

Nodes provide governance.

Capabilities provide reusable behavior.

Pitchfork provides shared accounting.

Reference services provide public knowledge.

Information sources provide observations.

Appliances provide deployment infrastructure.

Clients provide interfaces.

Products bring these elements together to support coherent areas of human life.

As new needs emerge, the ecosystem should grow by creating new capabilities and new product compositions rather than continually expanding the responsibilities of the node itself.
