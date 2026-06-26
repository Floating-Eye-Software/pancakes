# Pancakes Reference Services

## Purpose

Reference services provide shared public knowledge that Pancakes nodes can use
without centralizing private household or user data.

They answer questions about the world, not questions about people. This
document defines the canonical reference service pattern and its relationship
to nodes, capabilities, place, privacy, and symbolic interpretation.

## Canonical Definition

A reference service is an open or community-governed source of stable public
facts.

Examples include:

* this coordinate is inside this watershed
* this barcode identifies this product
* this plant is native to this region
* this water system has an active advisory
* this trail is managed by this public authority

Reference services do not store private node activity. They do not own
household inventories, walks, journals, habits, health records, or local
governance decisions.

## Public Knowledge And Private Knowledge

Pancakes separates public facts from private interpretation.

Public knowledge includes geography, species, products, public infrastructure,
standards, recipes, administrative boundaries, and civic alerts.

Private knowledge includes household activity, inventories, routes, journals,
preferences, health information, local histories, and node-specific decisions.

The node combines both locally:

```text
private node event
+ public reference fact
= local meaning
```

A walk can be enriched by GIS reference data. A pantry update can be enriched
by barcode reference data. A household alert can be enriched by civic
infrastructure reference data. In each case, the node remains the place where
private meaning is formed.

## Service Families

Reference services can be grouped into service families.

Geographic reference services provide boundaries, watersheds, aquifers, parks,
trails, ecological regions, public routes, and civic areas.

Goods reference services provide barcodes, commodities, ingredients, packaging,
repairability, recycling guidance, product categories, and standards.

Civic infrastructure services provide drinking water systems, wastewater
systems, electricity, waste collection, transit, libraries, schools, clinics,
public health areas, and public alerts.

Ecological reference services provide species, habitats, native plants,
pollinators, migration routes, invasive species, conservation areas, and
restoration practices.

Knowledge reference services provide recipes, educational materials, standards,
public datasets, safety guidance, and community-maintained instructions.

Future service families can cover astronomy, weather, geology, accessibility,
heritage, repair, or other public knowledge domains.

## Relationship To Nodes

Reference services are passive. Nodes are active.

A reference service can answer a query, publish a dataset, provide a versioned
download, or expose a public API. It should not decide what a household cares
about, monitor user behaviour, or assemble profiles.

Nodes decide what to query, what to cache, what to store, what to ignore, and
what to interpret. Nodes should prefer local caches or downloaded reference
sets when that reduces privacy exposure and improves resilience.

## Relationship To Capabilities

Capabilities consume reference services.

A GIS capability may use an open GIS service. A barcode capability may use an
open barcode database. A civic infrastructure capability may use a public water
or transit registry. A pollinator stewardship capability may use a species
reference service.

The capability translates public facts into domain behaviour for the node. The
reference service remains application-independent.

## Relationship To Place

Reference services enrich the place model.

GIS can identify a watershed, aquifer, park boundary, trail, municipality, or
conservation authority. Civic registries can identify water systems, waste
zones, transit service, and public alert areas. Ecological services can
identify species ranges and restoration contexts.

The reference service provides context. The node decides whether that context
matters to its homeland, stewardship, quality of life, or symbolic projection.

## Relationship To Symbolic Systems

Reference services do not perform symbolic interpretation.

They may provide facts that later contribute to symbolic frequencies. For
example, GIS may say that an activity occurred in a wetland. Pitchfork may
derive or project a wetland frequency. The reference service should not decide
that a user's walk produced a particular magical resource.

This boundary keeps public knowledge reusable and keeps private interpretation
inside the node.

## Privacy Principles

Reference services should minimize personal information exposure.

They should avoid user profiling, advertising identifiers, behavioural
tracking, household registries, and unnecessary query logging. Where practical,
they should support dataset downloads, regional mirrors, anonymous queries,
versioned snapshots, and local caches.

Nodes should avoid sending raw private records when a local lookup, coarse
query, or cached reference set is sufficient.

## Governance

Reference services should support open, plural, and accountable governance.

Important properties include clear data provenance, versioning, correction
processes, regional extensions, open formats, multiple implementations, public
documentation, and community review.

Avoid central monopolies. A reference service pattern should allow multiple
trusted providers, local mirrors, and community-maintained datasets.

## Non-Goals

Reference services are not social networks, advertising systems, household
data stores, identity providers, payment processors, or central node
registries.

They also do not replace community authority. Public Indigenous, ecological,
or civic data may still require careful governance, attribution, and respect
for knowledge that is not appropriate to publish.

## Examples

Open GIS provides watersheds, aquifers, parks, trails, ecological regions,
municipalities, and public boundaries. A node can use those facts to understand
place relationships.

An open barcode database provides product identity, ingredients, packaging,
categories, repairability, recycling guidance, and commodity relationships. A
node can use those facts to update an inventory or pantry without sharing the
household's full inventory externally.

A civic infrastructure registry provides water systems, wastewater systems,
electricity regions, transit service, public health regions, and alerts. A
node can determine whether a boil water advisory matters locally.

A species database provides native plants, birds, insects, invasive species,
pollinators, and habitat information. A pollinator stewardship capability can
use it to support community science and habitat work.

A recipe registry provides public recipes for food, repair, services,
education, and community practices. Nodes remain responsible for local
execution and private records.

## What Later Documents Should Reference

Later documents should reference this article when they need canonical language
for public knowledge, private node interpretation, reference service families,
privacy-preserving reference lookups, and the boundary between reference
services and capabilities.

Application documents should describe concrete reference datasets, APIs, and
client behaviours. They should not redefine the reference service pattern.
