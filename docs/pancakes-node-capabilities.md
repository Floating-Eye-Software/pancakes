# Pancakes Node Capabilities

## Purpose

Capabilities are the primary extension mechanism for Pancakes nodes.

They let the ecosystem add new domains of life, public knowledge, civic
practice, quality-of-life interpretation, and symbolic meaning without
redesigning the node core each time. This document defines the canonical
capability model.

## Canonical Definition

A capability is a coherent domain extension for a node.

Capabilities are not merely software plugins. A plugin usually extends a
program. A Pancakes capability extends the node's understanding of a domain of
life.

That is why a capability may contribute data models, event types, permissions,
recipes, quality-of-life indicators, reports, user interface surfaces,
reference service integrations, symbolic frequency context, and governance
hooks at the same time. The unit of modularity is not a code package. It is a
meaningful area of human activity or knowledge.

## Node Core And Capability Boundary

The node core should remain intentionally small.

The core owns identity, local storage, synchronization, permissions, event
transport, capability management, basic governance, and common safety
constraints.

Capabilities own domain knowledge.

Examples include inventory, GPX, GIS, barcode lookup, pantry, civic
infrastructure, community quests, pollinator stewardship, repair, recipes,
education, and accessibility.

This boundary lets the core stay stable while communities add new forms of
flourishing through capabilities.

## Capability Interface

A capability should define its identity, version, configuration, permissions,
data schema, event types, reference service dependencies, recipes,
quality-of-life indicators, reports, user interface surfaces, migration
behaviour, synchronization expectations, and governance requirements.

Not every capability needs every feature. A small capability may only add event
types and a report. A larger one may add reference lookups, recipes, UI,
quality-of-life indicators, and symbolic interpretation.

The interface should make dependencies explicit so nodes can decide whether a
capability is trusted, enabled, disabled, upgraded, or removed.

## Lifecycle

Capabilities have a lifecycle.

They may be installed, configured, enabled, disabled, upgraded, migrated, or
removed. Optional capabilities should fail gracefully. A node should remain
usable when a nonessential capability is absent or temporarily unavailable.

Capabilities should declare migration expectations before changing stored
data. They should avoid trapping private node records in opaque formats.

## Events

Capabilities extend the node event vocabulary.

Examples include `walk.completed`, `product.scanned`,
`place.relationship.discovered`, `cleanup.completed`, `bee.observed`,
`pantry.item.added`, `repair.completed`, and `advisory.received`.

Capability events should compose through shared node infrastructure. They
should not require unrelated capabilities to know each other's private
schemas.

## Data Models

Capabilities may define persistent data.

Examples include barcode inventory, species observations, stewardship records,
GPX tracks, pantry contents, infrastructure relationships, repair histories,
and community participation records.

Capabilities should avoid coupling unrelated domains. Shared concepts should
flow through events, reference identifiers, and documented interfaces rather
than hidden data dependencies.

## Reference Service Integration

Capabilities consume public reference services.

A GIS capability can use open GIS data. A barcode capability can use an open
barcode database. A civic infrastructure capability can use water, transit, and
public alert registries. A pollinator capability can use species and habitat
reference services.

Reference services provide public facts. Capabilities interpret those facts
for the node.

## Quality Of Life

Capabilities may contribute quality-of-life indicators.

Examples include food security, transit access, park access, water reliability,
repair capacity, volunteer participation, pollinator habitat, learning access,
and household resilience.

Quality-of-life indicators should support local decisions. They should not
become centralized scoring or profiling systems.

## Recipes

Capabilities may define recipes.

Examples include a pantry audit, community cleanup, pollinator survey, repair
workflow, household garden, accessibility review, or neighbourhood mutual aid
practice.

Recipes let capabilities describe structured domain actions without changing
the core recipe architecture.

## Symbolic Interpretation

Capabilities may contribute context used by symbolic frequencies.

A GIS capability can contribute wetland, watershed, forest, trail, and civic
place context. A barcode capability can contribute commodity, packaging, and
repairability context. A community quest capability can contribute stewardship,
cooperation, and civic participation context.

Capabilities do not directly create magic or lore. They expose domain context
that Pitchfork projections may interpret.

## Governance And Trust

Nodes decide which capabilities they trust.

Governance concerns include permissions, data access, reference service
sources, community adoption, policy configuration, safety constraints, upgrade
review, and removal behaviour.

Some capabilities may be personal. Others may be adopted by a household,
school, cooperative, clinic, or community organization. The capability model
must support local governance rather than assuming one central authority.

## Privacy

Capabilities should minimize data collection, prefer local computation, use
reference services instead of centralized private storage, expose meaningful
user controls, support graceful degradation, and avoid surveillance.

Capabilities are often the place where sensitive domain data appears. That
makes privacy part of capability design, not a separate afterthought.

## Capability Composition

Capabilities should compose through shared events and reference concepts.

GPX plus GIS can support place-aware walking records. Barcode plus recipes can
support pantry planning. GIS plus civic infrastructure can support local public
alerts. Community quests plus pollinator stewardship can support habitat
restoration. Inventory plus repair can support household resilience.

Composition should not require a large central application to know every
domain. The node core provides the common substrate.

## Non-Goals

Capabilities are not a license to put every feature into the node core. They
are also not an app store, advertising channel, hidden data broker, or
centralized policy engine.

The capability model does not define detailed UI conventions, storage formats,
or business rules for every domain. It defines the extension boundary that
those domain documents should use.

## Examples

An inventory capability tracks household goods, consumables, tools, and
storage locations. It may use barcode reference data and contribute pantry or
resilience indicators.

A GPX capability records walking, cycling, routes, and activity history. When
combined with GIS, it can discover place relationships while keeping raw route
history local.

A civic infrastructure capability tracks relationships to water, wastewater,
electricity, transit, waste collection, and public alerts. It can notify a
household about relevant advisories without centralizing household records.

A community quest capability represents volunteer opportunities, stewardship
events, neighbourhood participation, and shared recognition. It can contribute
cooperation and stewardship frequencies.

A pollinator stewardship capability supports species observations, native
plants, habitat work, and community science. It may consume species reference
services and contribute ecological quality-of-life indicators.

## What Later Documents Should Reference

Later documents should reference this article when they need canonical language
for capability architecture, capability lifecycle, node core boundaries,
events, data models, reference service integration, recipes, quality-of-life
indicators, symbolic context, privacy, governance, and capability composition.

Application documents should define specific capabilities. They should not
redefine the capability model.
