# 0006 Node Ambience Event Plan

## Status

Blocked on:

* `pitchfork:0003-core-foundation`
* `0007-node-foundation`

## Purpose

Build the first Pancakes/Pitchfork node service capable of receiving bounded client events, settling them through Pitchfork accounting rules, maintaining resource state, deriving symbolic projections, and returning ambient projections to clients such as Lone Honk and Resonance.

This plan belongs operationally in `pancakes` because the node is the human-facing governance, permissions, identity, and deployment boundary.

It belongs conceptually in `pitchfork` because events, settlement, resource-state management, caps, permissions, and projection derivation are Pitchfork concepts.

Until repository ownership is fully stabilized, implementation should preserve the following boundary:

```text
pancakes
  owns node application
  owns sessions
  owns identity context
  owns permissions
  owns governance
  owns node APIs

pitchfork
  owns event schemas
  owns settlement rules
  owns resource-state models
  owns projection derivation
  owns accounting logic
```

---

# Design Goal

The objective is not merely to store events.

The objective is to establish the first complete Pitchfork chain:

```text
client activity
→ event
→ settlement
→ resource state
→ projection derivation
→ ambient client response
```

This chain becomes the foundation for:

* Lone Honk
* Resonance
* future ambient clients
* future household clients
* future RPG clients
* future symbolic interfaces

---

# Core Architectural Principle

Events do not directly create projections.

Instead:

```text
events
→ affect resource state

resource state
→ derives projections
```

This distinction is fundamental.

It allows:

```text
same event stream
→ multiple resource models
→ multiple client projections
```

Example:

```text
lone_honk.zone_completed
```

may settle:

```text
exploration +1
migration +1
```

Then:

```text
Lone Honk
→ red_moon

Resonance
→ dream_birds

Future RPG
→ migration reputation

Future Household Client
→ exploration journal unlock
```

all from the same settled state.

---

# Canonical Flow

Architecturally:

```text
Client
→ Node Resolver
→ Active Node Context
→ Session
→ Permission Check
→ Event Validation
→ Event Storage
→ Settlement
→ Resource State Update
→ Projection Derivation
→ Projection Response
```

---

# Node Resolver

The node resolver exists architecturally but is deferred.

Future architecture:

```text
client
→ resolver
→ node
```

Initial implementation:

```text
client
→ www.pancakes.ca node
```

No resolver service is required for the first implementation.

---

# First Hello World

The first integration should prove:

```text
Lone Honk starts
→ client sends lone_honk.client_ping
→ node stores event
→ settlement updates migration state
→ projection derivation creates red_moon
→ client requests projections
→ node returns red_moon
→ Unity renders red moon
```

The projection must be derived from resource state rather than directly attached to the originating event.

---

# Initial Clients

```text
lone_honk
resonance
```

Future clients:

```text
mobile ambient clients
web ambient clients
guild tools
household tools
rpg interfaces
```

The node should not assume any particular client implementation.

---

# Initial Event Types

```text
client_ping
session_started
session_ended
zone_completed
migration_leg_completed
projection_requested
```

Namespaced examples:

```text
lone_honk.client_ping
lone_honk.zone_completed

resonance.projection_requested
```

Namespaces prevent collisions between client ecosystems.

---

# Initial Resource State Types

Initial resource-state types should remain intentionally small.

Examples:

```text
attention
exploration
migration
sanctuary
dreaming
wildlife_affinity
```

Resource state is produced by settlement.

Clients never write resource state directly.

---

# Initial Projection Types

Examples:

```text
red_moon
fog_level
wildlife_affinity
dream_birds
sanctuary_warmth
zone_unlocked
migration_progress
```

Projections are derived outputs.

Projection derivation should remain deterministic.

---

# Projection Derivation

Projection derivation converts resource state into client-visible symbolic state.

Example:

```text
resource state

dreaming = high
```

becomes:

```text
projection

dream_birds = enabled
```

Example:

```text
resource state

migration = threshold reached
```

becomes:

```text
projection

red_moon = enabled
```

Multiple projections may be derived from the same resource state.

Multiple clients may derive different projections from the same resource state.

---

# Projection Rules

Projection derivation should be data-driven.

Introduce:

```text
projection_rules
```

Examples:

```text
client_id
projection_type
resource_type
rule_json
version
```

This allows:

```text
migration = 17
```

to produce different projections for:

```text
Lone Honk
Resonance
Future RPG
```

without changing settlement logic.

---

# First API Shape

## Infrastructure

```text
GET /health
```

---

## Sessions

```text
POST /api/node/v1/sessions/start
POST /api/node/v1/sessions/end
```

---

## Events

```text
POST /api/pitchfork/v1/events
```

---

## Resource State

```text
GET /api/pitchfork/v1/resource-state/{actor_id}
```

---

## Projections

```text
GET /api/pitchfork/v1/projections/{actor_id}
```

Projection terminology should be used consistently.

Avoid:

```text
world-state
ambient-state
```

as primary API concepts.

---

# Session Model

Use logical sessions.

```text
client starts session
→ receives session_id

events reference session_id

session expires after inactivity
```

No WebSockets are required initially.

Ordinary HTTPS requests are sufficient.

---

# Minimum Data Model

```text
nodes
clients
actors
sessions

permission_grants
node_policies

events
settlements

resource_states
projection_rules
projections

audit_events
```

Keep the initial model intentionally small.

---

# Node Policies

The node governs.

Pitchfork accounts.

Introduce:

```text
node_policies
```

even if initially minimal.

Examples:

```text
policy_version
projection_visibility
retention_period
resource_caps
```

Future governance decisions belong here.

---

# Event Record

```text
id

node_id
client_id
actor_id
session_id

event_type

occurred_at

data_class
permission_scope

attestation_method

client_record_ref

measures_json
projection_intent_json

idempotency_key

created_at
```

---

# Data Classification

Initial classifications:

```text
public
shared
private
sensitive
restricted
```

These classifications guide:

* storage
* permissions
* transmission
* auditing

---

# Permission Scopes

Examples:

```text
self
household
guild
node
public
```

Permission validation occurs before settlement.

---

# Settlement Record

```text
id

node_id
actor_id

event_id

resource_type

delta_json

settled_at
```

Settlement should be reproducible and auditable.

---

# Resource State Record

```text
id

node_id
actor_id

resource_type

state_json

updated_at
```

This record stores current settled actor state.

Examples:

```text
migration = 17
exploration = 42
dreaming = elevated
```

These are accumulated states rather than collectible resources.

---

# Projection Record

```text
id

node_id
actor_id
client_id

projection_type

state_json

visibility

source_resource_state_ref

created_at
updated_at
expires_at
```

Note:

```text
source_resource_state_ref
```

rather than:

```text
source_event_id
```

to reinforce resource-state-derived projections.

---

# Idempotency

Events must be replay-safe.

Constraint:

```text
(node_id,
 client_id,
 idempotency_key)
```

must be unique.

Duplicate submissions should return the original result.

Duplicate settlement must not occur.

---

# Privacy Rules

Do not transmit raw sensitive client records into Pitchfork.

Allowed examples:

```text
zone_completed
movement_band
session_started
projection_requested
red_moon_enabled
```

Forbidden by default:

```text
raw journal text
cycle details
symptom logs
mood journals
gps traces
household conflict records
identity documents
secrets
```

Prefer symbolic measures whenever possible.

---

# Audit Rules

Audit events should record:

```text
who
did what
when
under which permission
```

without unnecessarily storing private payloads.

Auditability should not become surveillance.

---

# Repository Boundary

Preferred architecture:

```text
pitchfork
  accounting engine
  settlement engine
  resource-state engine
  projection derivation

pancakes
  node
  identity
  permissions
  governance
  deployment

site-ops
  infrastructure
```

Example:

```python
from pitchfork import settlement
from pitchfork import projections
```

The Flask node lives in Pancakes.

The business logic lives in Pitchfork.

The infrastructure lives elsewhere.

Avoid introducing network boundaries until a demonstrated need exists.

---

# Prerequisites

This plan begins only after:

* Pitchfork plan `pitchfork:0003-core-foundation` supplies the installable
  domain package, deterministic engine, and persistence interfaces; and
* Pancakes plan `0007-node-foundation` supplies the Flask application,
  SQLAlchemy adapters, Alembic migrations, transactions, configuration,
  health checks, and verified SQLite/PostgreSQL support.

PostgreSQL is canonical for hosted nodes. SQLite remains supported for personal
or local nodes and lightweight tests. PostgreSQL integration tests must pass
before hosted deployment.

Pancakes owns the physical database, migrations, and transaction boundary.
Pitchfork owns accounting semantics and persistence interfaces and does not open
its own database directly.

---

# Integration Phases

## Phase 1 — Ambience Hello World

Accept:

```text
lone_honk.client_ping
```

Then:

```text
store event
settle migration state
derive red_moon projection
return projection
```

Validate with:

```text
curl
```

before integrating Unity.

---

## Phase 2 — Client Registration

Create:

```text
known_clients
allowed_event_types
allowed_projection_types
```

Register:

```text
lone_honk
resonance
```

Reject unsupported event types.

---

## Phase 3 — Permission Grants

Implement:

```text
development grant
explicit grants
permission validation
scope enforcement
```

Reject:

```text
unauthorized events
unsupported permissions
invalid data classes
```

before settlement occurs.

---

## Phase 4 — Governance Foundation

Implement:

```text
node policies
resource caps
projection visibility
retention rules
```

The node becomes the governance authority.

---

# Success Criteria

The plan succeeds when:

```text
curl submits event
```

and:

```text
event stored
```

and:

```text
resource state updated
```

and:

```text
projection derived
```

and:

```text
client fetches projection
```

and:

```text
duplicate event
does not duplicate settlement
```

and:

```text
no raw sensitive payloads stored
```

and:

```text
same architecture supports

Lone Honk
Resonance
```

---

# Closure Condition

The plan is complete when the first end-to-end ambient projection flow exists:

```text
client
→ event
→ settlement
→ resource state
→ projection derivation
→ projection response
```

and a simple client visibly responds to that projection.

At that point the Pancakes node becomes the first functioning Pitchfork ambient-state service.
