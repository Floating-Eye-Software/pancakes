# 0007 Pancakes Node Foundation

## Status

Blocked on `pitchfork:0003-core-foundation`.

## Purpose

Build the application and persistence foundation required to operate a Pancakes
node before product-specific event and projection integration begins.

This plan is a prerequisite for `0006-node-ambience-event-plan`. It consumes
Pitchfork's accounting contracts but does not define Pitchfork settlement or
projection semantics.

## Ownership Boundary

Pancakes owns:

* the Flask application and application factory,
* runtime configuration and environment validation,
* SQLAlchemy persistence adapters,
* Alembic migrations and the physical database schema,
* transaction and concurrency boundaries,
* node health and readiness checks,
* PostgreSQL and SQLite compatibility,
* database integration tests.

Pitchfork owns domain models, settlement semantics, resource-state transition
semantics, projection derivation, and database-independent repository
interfaces. Pitchfork must not open a database connection directly.

## Database Policy

PostgreSQL is the canonical database for hosted nodes. SQLite remains supported
for personal and local nodes and for lightweight tests.

The application must use one migration history and one persistence contract for
both databases. Database-specific behavior must be isolated and documented;
SQLite passing is not sufficient evidence for hosted deployment.

PostgreSQL integration tests are mandatory before a hosted release or
deployment. They may run against an ephemeral local service or CI service.

## Application Foundation

Create:

* a packaged Flask application with an application factory,
* configuration profiles for development, testing, personal SQLite nodes, and
  hosted PostgreSQL nodes,
* strict startup validation for required settings,
* structured logging without private event payloads,
* `/health` for process liveness,
* `/ready` for dependency readiness.

Importing the package must not connect to a database or mutate external state.

## Persistence Foundation

Implement SQLAlchemy models and Pitchfork repository adapters for:

* clients and allowed namespaces,
* sessions,
* events and idempotency identities,
* settlements and settlement entries,
* resource state,
* projections,
* audit metadata required by the initial node contract.

Schema constraints must enforce the scoping and uniqueness assumptions exposed
by Pitchfork's interfaces. Raw sensitive payloads must not be introduced merely
to support debugging or auditing.

## Transactions and Concurrency

Define one node-owned unit of work that atomically performs:

```text
event record
→ settlement record
→ resource-state update
→ projection update
```

Specify rollback behavior and duplicate-event behavior. PostgreSQL tests must
exercise concurrent processing of the same event identity. Correctness must not
depend on SQLite's locking behavior.

## Migrations

Establish Alembic with:

* an initial schema migration,
* upgrade tests from an empty database,
* downgrade policy documented explicitly,
* schema creation performed only through migrations outside isolated unit
  tests,
* verification on both SQLite and PostgreSQL.

Pancakes owns all physical schema evolution, including migrations needed when a
Pitchfork persistence contract changes.

## Implementation Phases

### Phase 1 — Application Skeleton

Create packaging, the Flask application factory, configuration, logging, and
liveness/readiness endpoints.

### Phase 2 — Schema and Migrations

Define SQLAlchemy models, establish Alembic, and verify clean upgrades on both
supported databases.

### Phase 3 — Persistence Adapters

Implement Pitchfork repository and unit-of-work interfaces with atomic,
idempotent transaction behavior.

### Phase 4 — Database Verification

Add SQLite tests for fast feedback and PostgreSQL integration and concurrency
tests as a required hosted-deployment gate.

## Verification

Automated tests must cover:

* application creation under each supported configuration,
* startup rejection of invalid configuration,
* health and readiness behavior,
* migration upgrade on empty SQLite and PostgreSQL databases,
* repository contract behavior on both databases,
* atomic rollback across all persistence operations,
* duplicate and concurrent event handling,
* node and actor scope isolation,
* absence of database connections during package import.

## Acceptance Criteria

This plan is complete when:

* the Flask application starts with either SQLite or PostgreSQL configuration;
* Alembic creates the complete initial schema on both databases;
* Pancakes implements the Pitchfork repository and unit-of-work contracts;
* transaction rollback and idempotency tests pass;
* `/health` and `/ready` accurately distinguish process and dependency state;
* PostgreSQL integration tests pass before hosted deployment;
* Pitchfork code is not responsible for database connections, SQLAlchemy
  sessions, or migrations.

## Dependencies

Completion of Pitchfork plan `pitchfork:0003-core-foundation`.

## Follow-on Work

When this plan and `pitchfork:0003-core-foundation` are complete, unblock
`0006-node-ambience-event-plan` for Lone Honk and Resonance integration.
