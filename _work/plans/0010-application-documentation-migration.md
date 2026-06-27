# 0010 Application Documentation Migration

## Status

Ready

## Purpose

Update existing application and implementation documentation to adopt the
completed Pancakes and Pitchfork foundation.

This plan applies the canonical foundation documents to user-facing,
client-facing, gameplay, economic, and service documents.

It does **not** create new architectural primitives or reorganize the
architecture itself. Those concerns are tracked separately in
`0012-architecture-reconciliation.md`.

Application documents should consume the canonical foundation rather than
redefining it.

---

# Scope

## Pitchfork

Update:

```text
docs/pitchfork-frequencies.md
docs/pitchfork_economics.md
docs/pitchfork_rpg_client.md
```

## Pancakes

Update:

```text
docs/pancakes_service_exchange.md
docs/pancakes-goods-and-services-model.md
```

## Lone Honk

Update:

```text
docs/lone-honk-observation.md
docs/lone-honk-ecology.md
```

## New Infrastructure Documents

Create:

```text
docs/pancakes-open-gis.md
docs/pancakes-open-barcodes.md
```

---

# Goals

## Pitchfork Frequencies

Reduce the document to an application-oriented overview.

Reference the canonical symbolic architecture rather than redefining it.

Focus on:

* gameplay interpretation
* user understanding
* examples
* symbolic discovery
* links to canonical symbolic frequencies

---

## Pitchfork Economics

Update the economic model to consume the completed symbolic architecture.

Incorporate:

* symbolic conservation
* provenance
* symbolic commodities
* regional production
* recipes
* settlement
* contracts
* cooperative economics

The document should explain how economics behaves rather than redefining
foundational concepts.

---

## Pitchfork RPG Client

Update the RPG client specification to reflect the current architecture.

Describe:

* projections
* inventories
* symbolic materials
* recipes
* quests
* provenance
* symbolic inspection
* client rendering
* multiplayer considerations

The RPG should be described as one interpretation client over Pitchfork rather
than as the platform itself.

---

## Pancakes Service Exchange

Update the service exchange model to consume:

* contracts
* commonwealth
* goods and services
* node capabilities
* stewardship

Expand examples involving:

* community services
* mutual aid
* capability-generated services
* local exchange

The document should focus on service behavior rather than governance or
architecture.

---

## Pancakes Goods and Services

Update the model to align with the new economic foundation.

Expand:

* product identity
* commodity metadata
* provenance
* symbolic materials
* reference services
* repairability
* sustainability

Avoid duplicating reference-service architecture.

---

## Pancakes Open GIS

Create a canonical document describing an open geographic reference service.

Topics include:

* place identity
* ecological layers
* stewardship
* civic infrastructure
* service discovery
* privacy
* interoperability

This document consumes the Place Model and Reference Services foundation.

---

## Pancakes Open Barcodes

Create a canonical document describing an open product identity reference
service.

Topics include:

* barcode registry
* product metadata
* repairability
* sustainability
* provenance
* interoperability
* community stewardship

This document consumes the Reference Services foundation.

---

## Lone Honk Observation

Update observation to align with the completed symbolic architecture.

Connect:

* observation
* place
* symbolic interpretation
* ecological discovery
* knowledge progression

The document should remain grounded in ecology rather than becoming a symbolic
systems document.

---

## Lone Honk Ecology

Update the ecological model to reference:

* Pancakes Place Model
* symbolic frequencies
* stewardship
* ecological relationships

The document should explain how ecological systems participate in the broader
ecosystem without redefining its foundations.

---

# Migration Principles

Application documents should reference rather than redefine:

* symbolic frequencies
* symbolic crafting
* contracts
* projections
* place
* reference services
* node capabilities
* commonwealth
* governance

Application documents should emphasize:

* behavior
* implementation
* examples
* user experience
* gameplay
* services

rather than architectural foundations.

---

# Success Criteria

The plan is ready for closure when:

* application documents consistently reference canonical foundation documents;
* duplicate conceptual explanations have been removed;
* gameplay, economics, services, and ecology all use consistent terminology;
* new GIS and barcode documents exist as application-level reference-service examples;
* the application layer clearly builds upon the completed architecture without redefining it.
