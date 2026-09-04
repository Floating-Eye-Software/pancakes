# Pancakes Identity Model

**Status:** Draft architecture model  
**Date:** 2026-09-01  
**Authority:** Pancakes product architecture  

## Purpose

This document defines identity as a shared Pancakes node capability.

Pancakes needs a stable way to represent a person across personal, household,
guild, cooperative, institutional, hosted, virtual, and offline nodes. A
person must be representable without first proving a legal name, address,
citizenship, health-card number, banking relationship, or other
institutionally recognized identity.

When a Pancakes node interacts with an external service, it may need to
establish that a Pancakes person corresponds to an identity recognized by that
service. That correspondence is an external identity binding. It does not
replace the Pancakes identity or make the external authority the source of the
person's existence within Pancakes.

## Architectural Decision

Each person known to Pancakes has a permanent, opaque **Pancakes Person ID**.
The Person ID is the canonical subject identifier inside the Pancakes
ecosystem.

External identifiers are connected to a Person ID through explicit,
provenanced **External Identity Bindings**. A binding records the narrower
claim that an external authority's subject or account corresponds to a
Pancakes person according to a stated method and level of assurance.

Identity is a capability layer implemented by Pancakes nodes. It is not a
central Pancakes identity service and does not require a global registry of
people.

```text
Pancakes Person ID
├── node-local records
├── Ontario service binding
├── financial-service binding
├── social-service binding
└── school binding
```

## Design Principles

### A person precedes institutional identity

A Pancakes Person ID may be created without external documentation. A person
without a stable address, government identification, banking access, or health
card remains fully representable within Pancakes.

### Pancakes identity is sufficient inside Pancakes

Pancakes nodes do not need to verify a person's legal or institutional identity
merely to represent that person, relate records to them, or recognize them
across Pancakes activities. External verification is introduced only where an
external interaction requires it.

### External identities are bindings, not foundations

An Ontario account, bank customer record, social-service client number, or
school account does not become the Pancakes primary key. Each remains an
authority-specific identity connected to the Pancakes person through a
binding.

### Equivalence is contextual and provenanced

A binding means:

> According to this binding process, this external authority's subject
> corresponds to this Pancakes person.

It does not assert that two identifiers are universally interchangeable. The
binding retains who established it, how it was established, what the external
system actually proved, and whether that conclusion remains current.

### Nodes receive the minimum identity information they need

Most nodes need only a Person ID. They must not receive a person's government,
financial, school, or social-service identifiers merely because another node
has established those bindings.

### Identity must not create a universal correlation key

The canonical Person ID is an internal Pancakes identifier. External services
should receive service-specific opaque identifiers where possible rather than
the canonical Person ID. This prevents external authorities from correlating a
person's activity across unrelated services.

### Identity must remain compatible with local-first operation

A personal, household, virtual, or offline node must be able to create and use
Person IDs without a connection to a central service. Federation,
synchronization, duplicate reconciliation, and external verification may occur
later.

## Terminology

### Pancakes Person ID

A permanent, opaque, non-semantic identifier for a person within Pancakes.

Example:

```text
urn:pancakes:person:7b1998a6-4d20-4cca-9f7f-79a85f369384
```

The identifier must not encode a name, birth date, location, node, authority,
or other personal attribute.

### Person Reference

The portable representation of a Person ID used in node records and
node-to-node messages. A Person Reference may carry routing or version metadata
without changing the underlying Person ID.

### External Authority

An organization or service that maintains its own identity namespace, such as
a government program, financial institution, school, employer, or social
service.

### External Subject

The authority-specific account or subject identifier recognized by an
external authority. It may represent an account, client, student, customer, or
legally identified person. Its meaning is defined by the external authority.

### External Identity Binding

A record connecting a Person ID to an External Subject, together with the
method, provenance, assurance, lifecycle state, and evidence needed to
interpret the connection.

### Authentication

Evidence that the present actor controls a credential, account, device, or
Pancakes identity. Authentication does not necessarily establish legal
identity.

### Assurance

A description of what a binding process established and how confidently a
consumer may rely on it. Assurance is not a single universal score.

## Node Capability Profiles

Identity is a layered capability. Nodes implement only the profiles required
for their responsibilities.

| Profile | Responsibility | Expected adoption |
| --- | --- | --- |
| Identity-aware | Store, accept, and exchange Person References | Required for nodes that represent people or person-related activity |
| Identity-resolving | Associate a local actor, session, or record with a Person ID | Expected for most interactive nodes |
| Identity-hosting | Create Person IDs and maintain canonical person records | Required only where people are enrolled or managed |
| Identity-authenticating | Establish that the current actor controls a Pancakes identity | Required where actions need authorization or accountability |
| Identity-binding | Establish and maintain External Identity Bindings | Required only for nodes that integrate with external identity systems |
| Identity-reconciling | Detect, review, merge, split, or supersede duplicate and conflicting person records | Required for federation and multi-node reconciliation |

A node that records household activity may be identity-aware and
identity-resolving without becoming identity-binding. A school integration node
may implement identity-binding while exposing only the resulting Person ID to
other Pancakes nodes.

## Conceptual Capability Interface

An identity-aware node needs operations equivalent to:

```text
accept_person_ref(person_ref)
resolve_person(person_ref) -> local_person_view
associate_record(record_ref, person_ref)
describe_identity_context(person_ref) -> identity_context
```

An interactive node may also provide:

```text
identify_actor(session_context) -> person_ref
authenticate_actor(authentication_request) -> authentication_result
```

An identity-binding node additionally needs operations equivalent to:

```text
begin_binding(person_ref, external_authority)
complete_binding(binding_session) -> external_identity_binding
verify_binding(binding_ref) -> binding_status
refresh_binding(binding_ref) -> binding_status
revoke_binding(binding_ref, reason)
list_bindings(person_ref, requesting_context)
```

These are conceptual contracts rather than a commitment to a particular API,
protocol, or programming language.

## Core Data Model

### Person

```yaml
person_id: urn:pancakes:person:7b1998a6-4d20-4cca-9f7f-79a85f369384
status: active
created_at: 2026-09-01T12:00:00Z
```

The Person entity contains only Pancakes identity lifecycle information.
Names, contact methods, addresses, household memberships, jobs, health
information, and external identifiers belong in other records.

### External Identity Binding

```yaml
binding_id: urn:pancakes:identity-binding:0f05e568-0707-43a9-9204-d5eaf556eceb
person_id: urn:pancakes:person:7b1998a6-4d20-4cca-9f7f-79a85f369384
authority: ontario.ca
namespace: ontario-ca-login
external_subject: protected-authority-specific-value
binding_method: oidc-authentication
assurance:
  kind: account-control
  claims:
    - controls_external_account
status: active
established_at: 2026-09-01T12:30:00Z
last_checked_at: 2026-09-01T12:30:00Z
expires_at: null
evidence_reference: protected:identity-evidence:example
```

The external subject and evidence reference are sensitive. They must not be
included in ordinary node messages or logs.

### Node-local records

Nodes relate domain records to a Person ID rather than copying external
identity data.

```text
household_member(person_id, household_id, membership_state)
worker(person_id, workplace_id, relationship_state)
student(person_id, learning_record_id)
care_event(person_id, event_id)
```

These relationships describe the node's domain. They do not redefine the
person's identity.

## Binding Semantics

Different external interactions establish different facts. A binding must
record what was actually established rather than promoting every successful
login to verified legal identity.

| Binding event | Permitted conclusion |
| --- | --- |
| Email login | The actor controls the authenticated email account |
| Ontario.ca Login | The actor controls the corresponding Ontario login |
| Social-service account connection | The external service associates the account with its client record |
| School portal connection | The school recognizes the external subject as a student or participant according to its rules |
| Bank or identity-verification result | The provider verified the returned attributes using its stated process |
| Manual identifier entry | The actor asserted an external identifier; no external verification has occurred |

The assurance record should use named conclusions and claims, not labels such
as `high`, `medium`, or `low` without definitions.

## Binding Lifecycle

An External Identity Binding may pass through these states:

```text
asserted
→ pending-verification
→ active
→ stale
→ revoked or superseded
```

- **Asserted:** A person or operator supplied the association, but the external
  authority has not confirmed it.
- **Pending verification:** A verification flow has started but has not
  completed.
- **Active:** The required binding process completed successfully.
- **Stale:** The binding was previously active but requires refresh or can no
  longer be checked.
- **Revoked:** The binding must no longer be relied upon.
- **Superseded:** A newer binding replaces the record while preserving history.

Deletion of an external account does not delete the Pancakes person. Loss of a
binding does not invalidate node-local records associated with the Person ID.

## Multiplicity, Conflict, and Reconciliation

The model must permit:

- one person to have several identifiers at one authority;
- an authority to replace or migrate identifiers;
- duplicate external records for one person;
- a mistaken binding to be disputed and revoked;
- two Pancakes Person IDs to be discovered as duplicates;
- one incorrectly merged person record to be separated again;
- historical bindings to remain auditable without remaining active.

Consequently, an External Identity Binding must not be represented as an
unqualified unique equality such as `pancakes_id == external_id`. It is a
lifecycle-managed association with provenance.

Merge and split operations are consequential identity actions. They require
explicit authorization, retained history, affected-node review, and a
reversible or compensating procedure.

## Privacy and Security Boundaries

### Data minimization

Nodes should request only the external claims needed for the immediate service.
If an external authority can return a verified conclusion, Pancakes should not
retain identity-document images or the underlying evidence.

### Compartmentalization

External identifiers and verification evidence remain at the binding-capable
node or protected identity component. Other nodes receive a Person Reference
and, where necessary, a narrowly scoped assurance result.

### Pairwise external references

Where an external protocol allows it, each external relationship should use a
different opaque subject identifier. The internal Person ID must not become a
tracking identifier shared among external organizations.

### Logging

Logs must not contain identity documents, authentication credentials, access
tokens, complete external identifiers, or unnecessary personal attributes.
Audit records should refer to protected binding records by Pancakes-controlled
identifiers.

### Authorization

Possession of a Person ID is not authentication. Knowing a person's GUID does
not authorize an actor to view records, create bindings, or act for that
person. Authentication and authorization controls are separate capabilities.

## Federation and Offline Operation

The first implementation may operate within one node, but the model must not
assume a permanent central Pancakes service.

An offline or virtual node may create a Person ID and use it immediately.
Later federation may discover that another node represents the same person.
That discovery creates a reconciliation problem, not a reason to postpone
identity creation.

Federated design must eventually define:

- which node may authoritatively change identity lifecycle state;
- how a person moves between nodes without changing Person ID;
- how nodes authenticate identity messages;
- how duplicate Person IDs are reconciled;
- how revocation, merge, and split events propagate;
- how an offline node detects stale identity or binding state;
- which metadata may be disclosed during resolution.

These questions remain open and do not block a single-node implementation.

## Minimum Viable Identity Capability

The first implementation should prove the internal model without requiring an
Ontario, banking, or other production integration.

Minimum scope:

1. Generate an opaque Person ID.
2. Store a minimal Person record.
3. Use the Person ID as the foreign key for node-local person relationships.
4. Create manual external-binding records in `asserted` state.
5. Record authority, namespace, binding method, assurance claims, provenance,
   and lifecycle state.
6. Prevent ordinary node queries from exposing protected external subjects.
7. Revoke or supersede a binding without deleting the person.
8. Demonstrate that records from two Pancakes capabilities refer to the same
   person using only the Person ID.

A later integration slice can replace a manual asserted binding with a sandbox
OpenID Connect flow and an active, externally confirmed binding.

## Requirements Summary

- Every Pancakes node that represents people or person-related activity must
  implement the identity-aware profile.
- Every person represented in Pancakes must have an opaque Pancakes Person ID.
- Pancakes Person IDs must not depend on external identification.
- Node-local person records must use the Person ID rather than an external
  identifier as their canonical subject key.
- External identities must be represented as lifecycle-managed bindings.
- Every binding must identify its authority, namespace, method, assurance,
  provenance, and status.
- External authentication must not be interpreted as legal identity
  verification unless the provider explicitly supplies that assurance.
- Nodes must not disclose protected external identifiers merely to resolve a
  Person ID.
- Possession or knowledge of a Person ID must not confer authentication or
  authorization.
- The model must support local-first creation and later reconciliation.

## Open Questions

1. Should the canonical identifier use UUIDv4, another UUID profile, or a
   Pancakes-specific opaque identifier format?
2. Which node or component issues Person IDs in household and hosted
   deployments?
3. How are Person IDs recovered or transferred when a person changes their
   primary node?
4. What protocol represents Person References between federated nodes?
5. How are duplicate people merged and incorrectly merged people split?
6. Which binding evidence must be retained, and for how long?
7. Which assurance vocabulary should Pancakes standardize?
8. How should consent be represented when a node requests an external binding
   or assurance result?
9. Which identity operations require Pitchfork permissions, covenants, or
   auditable settlement?
10. Which minimum identity capabilities belong in the Pancakes node foundation
    and which should be delivered as optional modules?

## Relationship to Other Pancakes Layers

The identity layer identifies the person or actor to whom an action,
permission, record, or relationship applies. It does not replace node
governance, Pitchfork accounting, application-specific interpretation, or
human-facing Pancakes interfaces.

```text
Clients interpret.
Pitchfork accounts.
Nodes govern.
Identity authorizes.
Pancakes humanizes.
```

Within that architecture, this model supplies the stable person reference and
the controlled boundary between Pancakes identity and external identity
authorities.
