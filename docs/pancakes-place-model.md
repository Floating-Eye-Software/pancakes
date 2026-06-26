# Pancakes Place Model

## Purpose

Place is a first-class concept in Pancakes.

Nodes, households, recipes, services, stewardship, quality-of-life indicators,
and symbolic projections all occur somewhere. The place model provides shared
language for ecological, civic, historical, cultural, and infrastructure
relationships without turning location into surveillance.

This document defines place, homeland, stewardship, and place relationships. It
does not define GIS implementation details, reference service APIs, or
symbolic crafting rules.

## Canonical Definition

A place is a meaningful relationship, not merely a coordinate.

Coordinates can identify a location, but Pancakes cares about the relationships
around that location: watershed, aquifer, neighbourhood, park, library,
conservation authority, transit route, food system, local history, stewardship
group, public alert, and community practice.

Places have identities independent of a particular user. A household node may
relate to a place, but it does not own the place's meaning.

## Homelands

A node may optionally define a homeland.

A homeland is a durable relationship between a node and a place. It says, "this
node belongs here" or "this node is responsible here" in a limited,
privacy-preserving sense.

Homeland is not continuous location tracking. A node can have a homeland
without reporting movement, storing travel history, or exposing a household's
address to external services.

Homelands may apply to households, schools, cooperatives, neighbourhood groups,
community organizations, farms, clinics, libraries, or other local nodes.

Homeland is optional. Mobile households, privacy-sensitive deployments,
travelling users, and abstract service nodes must remain functional without a
homeland.

## Place Relationships

A node may relate to many places.

Examples include home, favourite park, walking trail, creek, community garden,
school, library, transit station, market, clinic, watershed, conservation
area, volunteer organization, and public service area.

These relationships are not just bookmarks. They tell the node which public
facts, local practices, stewardship opportunities, and quality-of-life signals
may be relevant.

Relationships should be explicit, reviewable, and locally governed. A node
should be able to forget, hide, or summarize place relationships when privacy
or safety requires it.

## Layers Of Place

Places are layered.

Ecological layers include watershed, aquifer, biome, forest, wetland, coastline,
pollinator habitat, migration route, and conservation area.

Geological layers include escarpment, bedrock, soil, floodplain, river valley,
and erosion risk.

Civic layers include municipality, ward, conservation authority, transit
agency, school board, library system, water utility, waste collection zone, and
public health area.

Historical layers include neighbourhood history, industrial history, settlement
history, archaeology, heritage buildings, and prior land uses.

Cultural layers include public art, languages, festivals, markets, local
traditions, and community institutions.

Indigenous context includes traditional territories, treaties, Indigenous
place names, language, stewardship knowledge, and governance relationships.
This context must be treated respectfully. It is contextual knowledge, not a
game resource, reward system, or identity mechanic.

## Stewardship

Stewardship is care for a place.

A node may choose to care about a park, creek, garden, street, trail, wetland,
library, or neighbourhood. Stewardship can include cleanup, restoration,
maintenance, monitoring, education, mutual aid, community gardening, species
observation, accessibility work, and civic participation.

Stewardship is not ownership. It is a relationship of responsibility and
attention.

The place model should make stewardship visible without pressuring households
into public disclosure. Local contribution can remain local unless a node
chooses to share it.

## Place And Quality Of Life

Place helps a node understand conditions that affect flourishing.

Examples include nearby parks, transit access, food access, library access,
water quality, flood risk, heat risk, air quality, walkability, repair access,
community services, and boil water advisories.

Quality-of-life indicators should support household and community decisions.
They should not become centralized profiling tools.

## Place And Symbolic Meaning

Place contributes symbolic context to Pitchfork projections.

A wetland can contribute wetland frequencies. A library can contribute learning
and civic knowledge frequencies. A market can contribute exchange and food
frequencies. A conservation area can contribute stewardship and ecological
frequencies.

Place enriches interpretation. It does not replace activity. Walking through a
wetland is still walking; the place adds context to the event's frequency
vector.

## Place And Infrastructure

Nodes also relate to civic and ecological infrastructure.

Examples include drinking water source, wastewater destination, electrical
grid, waste collection area, recycling system, transit system, public health
unit, conservation authority, food distribution system, and emergency alert
area.

These relationships help a node understand local conditions. A boil water
advisory can be relevant because the node knows its water system, not because a
central service tracks the household.

## Relationship To Reference Services

Reference services provide public place knowledge. Examples include GIS,
species databases, civic infrastructure registries, open barcode registries,
and public datasets.

Nodes combine that public knowledge with private local context. The reference
service may know the watershed boundary. The node knows whether that watershed
matters to its household, activities, and stewardship.

## Non-Goals

The place model does not define live tracking, geofencing surveillance,
advertising profiles, location brokerage, or centralized household registries.

It also does not define Indigenous identity, political authority, treaty
interpretation, land claims, or controlled cultural knowledge. Those require
appropriate community authority and governance outside this engineering
foundation.

## Examples

A household node declares a homeland. Locally, it can associate that homeland
with a watershed, aquifer, conservation authority, library system, transit
agency, and community garden. None of that requires publishing the household's
address.

A stewardship capability records participation in a park cleanup. The node can
associate the activity with place, stewardship, cooperation, and ecological
frequencies. A shared community artifact can preserve cleanup context without
exposing private participant histories.

A Lone Honk activity near Duffins Creek can discover a place relationship.
Pitchfork may interpret the activity with wetland or creek frequencies while
the node retains control over what location details are stored or shared.

A boil water advisory reference service identifies affected water systems. A
node that knows its own water relationship can determine local relevance
without sending private household records to the service.

## What Later Documents Should Reference

Later documents should reference this article when they need canonical language
for place, homeland, stewardship, locality, layered place relationships,
infrastructure relationships, Indigenous context boundaries, and privacy
principles for place-aware systems.

Application documents should describe how a specific client or capability uses
place. They should not redefine what place means in Pancakes.
