# Pancakes Ecosystem Layers

## Purpose

The Pancakes ecosystem is intentionally organized into architectural layers.

Each layer has a distinct responsibility.

This separation helps keep concepts cohesive, avoids duplicate definitions, and
allows individual projects to evolve without redefining the entire ecosystem.

This document provides a high-level architectural map of the ecosystem and
identifies the canonical home for major concepts.

---

# Design Philosophy

The Pancakes ecosystem is not a single application.

It is a collection of interoperable systems built around a shared philosophy of
human flourishing, stewardship, local autonomy, and non-exploitative
infrastructure.

Rather than organizing documentation by software component, the architecture is
organized by responsibility.

Each layer builds upon the one below it.

Each concept should have one canonical home.

---

# Architectural Overview

```text
Human Flourishing
        │
        ▼
Commonwealth
        │
        ▼
Nodes
        │
        ▼
Capabilities
Reference Services
        │
        ▼
Identity & Permissions
        │
        ▼
Pitchfork
        │
        ▼
Settlement
Contracts
Recipes
Projections
        │
        ▼
Clients
        │
        ▼
Networks
```

Information generally flows downward.

Experience generally flows upward.

---

# Layer 1 — Human Flourishing

The highest layer defines why the ecosystem exists.

It answers questions such as:

* What is a flourishing life?
* What should technology encourage?
* What values guide design?
* What ethical boundaries exist?
* What forms of participation deserve recognition?

Representative documents include:

* Human Flourishing Framework
* Ethics Framework
* Stewardship Model
* Meaning
* Lifecraft

This layer defines principles rather than implementation.

---

# Layer 2 — Commonwealth

The Commonwealth layer defines how people organize together.

Topics include:

* stewardship
* participation
* institutions
* governance
* mutual aid
* civic relationships
* shared responsibilities
* common goods

Representative documents include:

* Pancakes Commonwealth Model
* Common Good Model
* Charter of Rights
* Ostrom Governance Model

This layer explains social organization independently of technical
implementation.

---

# Layer 3 — Nodes

Nodes are the operational units of the ecosystem.

A node is simultaneously:

* a deployment boundary;
* a governance boundary;
* an identity boundary;
* a permission boundary;
* a stewardship boundary.

Nodes may represent:

* individuals;
* households;
* guilds;
* cooperatives;
* institutions;
* communities;
* official hosted deployments.

Representative document:

* Pancakes Node Infrastructure

---

# Layer 4 — Runtime Services

Nodes host reusable runtime services that support every client.

These include:

* identity
* permissions
* capabilities
* reference services
* storage
* synchronization
* export and import

Representative documents include:

* Pancakes Client and Node Architecture
* Place Model
* Reference Services
* Node Capabilities

These services provide shared infrastructure without imposing application
behavior.

---

# Layer 5 — Pitchfork

Pitchfork is the ecosystem's shared symbolic and accounting substrate.

Pitchfork is responsible for:

* events;
* settlement;
* contracts;
* recipes;
* symbolic interpretation;
* provenance;
* projections.

Pitchfork deliberately avoids becoming a general-purpose application platform.

Representative documents include:

* Pitchfork Overview
* Contracts
* Symbolic Frequencies
* Symbolic Crafting
* Symbolic Projections
* Client API Specification

---

# Layer 6 — Clients

Clients present different interpretations of the same underlying activity.

Examples include:

* Pancakes Wellness Notebook
* Pitchfork RPG
* Red Witch
* Nexus
* future educational clients
* future ambient clients

Clients own:

* user experience;
* visualization;
* workflows;
* domain-specific behavior.

Clients do not redefine accounting or governance.

They interpret them.

---

# Layer 7 — Networks

Networks describe relationships between nodes.

Networking is not required for a useful Pancakes deployment.

Instead, networking allows independent communities to cooperate while retaining
local autonomy.

Topics include:

* federation;
* capability exchange;
* service exchange;
* knowledge publication;
* computation exchange;
* resilience;
* future economic coordination.

Representative document:

* Pancakes Network Architecture, Knowledge, and Value Infrastructure

Networking extends local systems.

It does not replace them.

---

# Cross-Cutting Concerns

Several concerns intentionally span multiple layers.

## Privacy

Privacy begins with human dignity.

It continues through governance, permissions, accounting, networking, and user
interfaces.

Privacy is therefore a design principle rather than a single subsystem.

---

## Stewardship

Stewardship appears at every level.

People steward households.

Communities steward common resources.

Nodes steward data.

Capabilities steward services.

Applications steward user experience.

The ecosystem treats stewardship as a recurring pattern rather than a single
feature.

---

## Local First

Every layer should support meaningful local operation.

Networking, federation, and hosted infrastructure expand local capability
rather than replacing it.

A single person running a single node should still possess a complete and
coherent system.

---

## Canonical Ownership

Every significant architectural concept should have one canonical definition.

Other documents should reference that definition rather than creating
alternative versions.

This keeps the ecosystem internally consistent as it grows.

---

# Reading Order

Readers unfamiliar with the ecosystem should generally progress in the following
order:

1. Ecosystem Overview
2. Human Flourishing and Ethics
3. Commonwealth Model
4. Node Infrastructure
5. Client and Node Architecture
6. Pitchfork Overview
7. Pitchfork Foundation Documents
8. Client-Specific Documents
9. Networking Documents

This sequence moves from purpose to implementation while preserving the
relationships between layers.

---

# Guiding Principle

The Pancakes ecosystem should feel like a collection of well-defined layers,
each with a clear responsibility.

The purpose of layering is not abstraction for its own sake.

It is to ensure that:

* principles remain stable;
* architecture remains understandable;
* implementations remain interchangeable;
* communities retain autonomy;
* and future projects can build upon the ecosystem without redefining its
  foundations.
