# 0012 Architecture Reconciliation

## Status

Review

## Purpose

Reconcile the Pancakes and Pitchfork architecture documentation after completion
of the symbolic architecture foundation work.

The symbolic foundation documents now define the canonical concepts of place,
reference services, node capabilities, symbolic frequencies, symbolic
crafting, contracts, projections, and the commonwealth.

This plan updates the remaining architecture documents so that each has a
clear responsibility, references canonical concepts instead of redefining
them, and together forms a coherent architectural narrative for the
ecosystem.

This plan does **not** introduce new architectural primitives.

It reorganizes existing architecture around the completed foundation.

---

# Scope

This plan owns the following documents.

## New

```text
docs/pancakes-ecosystem-layers.md
```

## Update

```text
docs/pancakes-commonwealth-model.md
docs/pancakes_node_infrastructure.md
docs/pancakes_client_node_architecture.md
docs/pancakes-network-architecture.md

pitchfork/docs/pitchfork_client_api_spec.md
```

---

# Goals

## Ecosystem Layers

Create a concise architectural overview describing the major layers of the
Pancakes ecosystem and the responsibility of each.

The document should explain:

* ecosystem principles
* architectural layering
* document ownership
* dependency relationships
* canonical references

without redefining lower-level concepts.

---

## Commonwealth Model

Reduce architectural duplication.

The Commonwealth model should focus on:

* stewardship
* institutions
* participation
* governance
* civic relationships
* social organization

It should reference node architecture and ecosystem layers instead of
describing implementation details.

---

## Node Infrastructure

Refocus the document around a single question:

> What is a Pancakes node?

Topics should include:

* deployment boundary
* governance boundary
* identity boundary
* permission boundary
* capability hosting
* storage
* export/import
* appliance deployment
* federation readiness

Future research markets and networking concepts should remain out of scope.

---

## Client and Node Architecture

Refocus the document on runtime architecture.

Describe the interaction among:

* clients
* node interface
* capabilities
* reference services
* identity
* permissions
* Pitchfork
* settlement
* projections
* synchronization

This document should become the primary implementation-oriented architecture
reference.

---

## Pitchfork Client API

Reduce architectural discussion and increase implementation precision.

Update the API specification to incorporate:

* capability-aware requests
* reference-service integration
* projection requests
* symbolic projection families
* stable client integration patterns

The API should consume architectural concepts rather than defining them.

---

## Networks

Refocus the networking document on long-term ecosystem relationships.

Topics include:

* federation
* capability exchange
* knowledge exchange
* computation exchange
* service exchange
* resilience
* multi-author knowledge
* future value exchange

The networking document should describe relationships between nodes rather
than internal node implementation.

---

# Architectural Responsibilities

After completion:

`pancakes-ecosystem-layers.md`

: Defines the overall architectural map.

`pancakes-commonwealth-model.md`

: Defines social and institutional organization.

`pancakes_node_infrastructure.md`

: Defines nodes as deployment and governance units.

`pancakes_client_node_architecture.md`

: Defines runtime architecture and client interaction.

`pitchfork_client_api_spec.md`

: Defines the programming interface for clients.

`pancakes-network-architecture.md`

: Defines long-term relationships among nodes.

---

# Success Criteria

The plan is ready for closure when:

* each document has a clearly defined responsibility;
* architectural concepts have one canonical home;
* duplicate architectural explanations have been removed;
* documents reference canonical foundation documents instead of redefining them;
* the architectural progression from ecosystem to implementation is coherent;
* readers can identify where each architectural concept is defined without ambiguity.

---

# Expected Architectural Progression

The completed documentation should naturally guide readers through the
ecosystem.

```text
Ecosystem Layers
        ↓
Commonwealth
        ↓
Node Infrastructure
        ↓
Client and Node Architecture
        ↓
Pitchfork Client API
        ↓
Networks
```

Each document should narrow its focus while building on the preceding
documents.

Together they should describe a layered architecture rather than a collection
of partially overlapping design papers.
