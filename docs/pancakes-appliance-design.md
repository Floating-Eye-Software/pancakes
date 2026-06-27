# Pancakes Appliance Design

## Purpose

This document defines the design direction for Pancakes appliances.

A Pancakes appliance is a physical or virtual device that runs, extends, or feeds a Pancakes node.

The purpose of the appliance model is to make Pancakes infrastructure tangible, local, understandable, and governable.

Pancakes should not exist only as a cloud app or a collection of client interfaces. It should also be able to exist as physical infrastructure in homes, clinics, schools, communities, workshops, gardens, commons, and institutions.

The appliance model gives Pancakes a concrete deployment pattern:

```text
Pancakes Node Software
+
Pitchfork Accounting Substrate
+
Physical or Virtual Appliances
+
Client Applications
```

This document distinguishes node software, client applications, and appliances.

---

# Core Thesis

Pancakes appliances are local infrastructure for humane life computing.

They should support:

* Local ownership.
* Node governance.
* Explicit consent.
* Privacy-preserving data collection.
* Community memory.
* Cooperative operation.
* Offline resilience.
* Sensor and event capture.
* Local AI under clear boundaries.
* Pitchfork-compatible accounting where appropriate.

They should not become:

* Surveillance devices.
* Behavioral control systems.
* Productivity monitors.
* Black-box institutional scoring systems.
* Hidden AI inference engines.
* Cloud-first data extraction endpoints.
* Automated punishment or restriction systems.

The appliance model exists to make Pancakes more local, not more invasive.

---

# Architectural Position

Pancakes is organized around the distinction between:

```text
Nodes
Clients
Appliances
```

## Nodes

A Pancakes node is the governance, identity, permission, storage, and policy boundary.

A node may be:

* Personal.
* Household.
* Guild.
* Cooperative.
* Clinic.
* School.
* Institutional.
* Hosted.
* Self-hosted.
* Mobile-local.
* Virtual.

Nodes govern records, permissions, retention, exports, audits, and local policy.

## Clients

A client is an interface.

Examples:

* Wellness Notebook.
* Redwitch.
* Pitchfork RPG.
* Nexus.
* Memory Explorer.
* Governance Console.
* Household Dashboard.
* Clinic Dashboard.
* Ambient World Client.

Clients interpret node state.

They do not own the whole system.

## Appliances

An appliance is a physical or virtual deployment unit that either:

1. Runs a node.
2. Extends a node.
3. Captures events for a node.
4. Displays node state.
5. Provides local AI or sensor processing under node policy.

Examples:

* Household node appliance.
* Clinic node appliance.
* Speakers' Corner memory booth.
* BLE lap timing mat.
* Workshop station.
* Garden station.
* Community display.
* Ambient projection device.
* Local backup vault.
* Offline mobile virtual node.

Appliances are not necessarily user-facing apps.

They are infrastructure.

---

# One-Sentence Summary

A Pancakes appliance is a local, governable hardware or virtual device that runs or extends a Pancakes node by capturing, storing, processing, projecting, or displaying consented life, community, and stewardship records.

---

# Design Principles

## 1. Node First

Every appliance must belong to a node.

An appliance must declare:

```text
node_id
appliance_id
appliance_type
owner
custodian
policy_version
data_classes
permission_scopes
retention_policy
audit_policy
```

No appliance should operate as an ungoverned data collector.

---

## 2. Human Control Before Automation

Appliances may observe.

Appliances may remember.

Appliances may infer.

Appliances may recommend.

Appliances must not make significant decisions about people by themselves.

This is the Bacon Computer Rule:

```text
Sensors may observe.
Nodes may remember.
AI may recommend.
Humans govern.
```

Forbidden pattern:

```text
sensor
→ inference
→ automatic restriction
```

Allowed pattern:

```text
sensor
→ node record
→ visible interpretation
→ human or governance decision
```

---

## 3. No Secret Second Database of Meanings

Raw records and AI inferences must both be governed.

The system must not treat summaries, classifications, risk scores, relationship estimates, mood estimates, or social graphs as harmless metadata.

If an inference is about an identifiable person, it is governed personal information.

Every generated inference must have:

```text
inference_id
source_record_refs
subject_refs
purpose
model_or_rule_version
confidence
created_at
retention_policy
visibility_scope
challenge_status
deleted_at
```

---

## 4. Explicit Purpose

Every appliance must state what it is for.

Acceptable purposes:

* Household coordination.
* Community memory.
* Oral history.
* Wellness reflection.
* Workshop inventory.
* Tool checkout.
* Movement ritual capture.
* Clinic-local records.
* Institutional archive.
* Governance feedback.
* Ambient symbolic projection.
* Local backup.

Unacceptable purposes:

* General surveillance.
* Unspecified future analysis.
* Behavioral prediction for discipline.
* Hidden productivity scoring.
* Secret institutional profiling.
* Real-time social ranking.
* Coercive health enforcement.

---

## 5. Local Processing Where Practical

Appliances should process data locally where possible.

Preferred pattern:

```text
sensor input
→ local processing
→ minimized node record
→ optional projection
```

Avoid:

```text
sensor input
→ cloud upload
→ remote AI processing
→ opaque result
```

Local processing is especially important for:

* Audio.
* Video.
* Biometrics.
* Health-adjacent data.
* Children or dependent data.
* Household conflict.
* Clinic or institutional data.
* Sensitive community records.

---

## 6. Visible Capture

People should know when an appliance is recording or sensing.

Visible signals may include:

* Physical lights.
* Screen notices.
* Audible start/stop cues.
* Printed signage.
* Node registry listing.
* Public appliance map.
* Session consent screen.
* Local status display.

Hidden capture is prohibited except for narrow, explicitly governed safety cases.

---

## 7. Access, Correction, Challenge, and Deletion

A person should be able to ask:

```text
What does this node know about me?
What records came from this appliance?
What inferences were generated about me?
Who accessed them?
Can I correct this?
Can I challenge this?
Can I delete or suppress this?
```

Appliances must support node-level workflows for:

* Access.
* Export.
* Correction.
* Annotation.
* Challenge.
* Suppression.
* Deletion.
* Retention expiry.
* Audit review.

---

## 8. Privacy By Boundary

Different appliances should know different things.

A BLE lap mat does not need audio.

A workshop station does not need health records.

A memory booth does not need background surveillance.

A clinic appliance does not need RPG projections.

Capability separation is a core design requirement.

---

## 9. Client Interpretation Is Optional

Appliances feed records into nodes.

Clients decide how to interpret those records.

Example:

```text
BLE lap timing mat
→ loop_completed event
→ Pitchfork movement settlement
→ Wellness Notebook: "You completed a loop."
→ RPG: "You gathered Ember Moss."
→ Ambient client: "The woodland paths are well traveled."
```

The appliance does not own all meanings of the event.

---

## 10. Graceful Non-Participation

People must be able to live near or around Pancakes appliances without being forced into full participation.

For example:

* A resident can walk the 400 m loop without carrying a tag.
* A visitor can enter a commons without recording a memory.
* A workshop can allow manual checkout.
* A household can disable optional sensors.
* A clinic can provide non-digital alternatives where appropriate.

Participation must not become coercion.

---

# Appliance Categories

## 1. Node Appliances

Node appliances run the Pancakes node itself.

They are the core local infrastructure.

Examples:

* Household Node Appliance.
* Clinic Node Appliance.
* School Node Appliance.
* Guild Node Appliance.
* Cooperative Node Appliance.
* Institutional Node Appliance.

They provide:

* Local storage.
* Identity.
* Permissions.
* Audit logs.
* Exports.
* Backups.
* Pitchfork accounting.
* Client access.
* Appliance registry.
* Local AI services where enabled.

---

## 2. Capture Appliances

Capture appliances produce records or events.

Examples:

* Speakers' Corner booth.
* BLE lap timing mat.
* Workshop checkout station.
* Garden contribution station.
* Community meal kiosk.
* Tool library station.
* Pantry inventory station.
* Studio recording station.

They should minimize what they collect.

They should produce structured records with clear purpose and scope.

---

## 3. Sensor Appliances

Sensor appliances observe environmental, spatial, or activity signals.

Examples:

* Stream flow sensor.
* Room occupancy counter.
* Air quality monitor.
* Temperature sensor.
* Door sensor.
* Lap timing sensor.
* Garden moisture sensor.
* Energy usage monitor.

Sensor appliances must distinguish between:

```text
place-level state
```

and:

```text
person-level state
```

Place-level state is generally safer.

Person-level state requires stronger consent and governance.

---

## 4. Memory Appliances

Memory appliances collect narrative artifacts.

Examples:

* Speakers' Corner booth.
* Oral history station.
* Video diary booth.
* Community interview kit.
* Story archive kiosk.
* Elder memory station.
* Festival recording booth.

They produce records such as:

* Audio.
* Video.
* Transcript.
* Summary.
* Tags.
* Consent grants.
* Publication scope.
* Source references.
* AI-generated themes.

Memory appliances are not surveillance cameras.

They are voluntary contribution devices.

---

## 5. Projection Appliances

Projection appliances display or spatialize node state.

Examples:

* Community dashboard.
* Ambient wall.
* Workshop display.
* Garden display.
* Commons screen.
* Household hearth display.
* Clinic waiting-room display.
* Ambient lighting device.
* Minecraft-like local world server.
* Nexus projection terminal.

Projection appliances must obey visibility scopes.

They should prefer aggregate, symbolic, or place-level projections over personal exposure.

---

## 6. Backup and Resilience Appliances

Backup appliances preserve node continuity.

Examples:

* Encrypted local backup vault.
* Offline archive drive.
* Household cold-storage box.
* Cooperative backup peer.
* Emergency restore kit.

They should support:

* Encrypted backups.
* Key recovery.
* Export packages.
* Retention policies.
* Disaster recovery.
* Custodian handoff.
* Node migration.

---

# Reference Appliance Types

## Household Node Appliance

The household node appliance is the basic Pancakes home server.

It may run on:

* Mini PC.
* Raspberry Pi-class hardware.
* NAS.
* Router-like appliance.
* Repurposed local computer.
* Hosted virtual appliance for non-technical households.

Primary functions:

* Household records.
* Personal records.
* Wellness Notebook.
* Redwitch, if enabled.
* Pitchfork RPG local state.
* Household rituals.
* Shared calendar.
* Service exchange.
* Family archive.
* Local backups.
* Device registry.
* Permission grants.
* Export/import.

Default posture:

```text
private by default
household sharing by explicit scope
sensitive records local-first
AI disabled unless enabled by purpose
```

---

## Clinic Node Appliance

The clinic node appliance is an institutional node for sensitive health-adjacent or clinical environments.

Primary functions:

* Local patient/member records.
* Role-based access.
* Strong audit logs.
* Strict data separation.
* Local consent management.
* Export workflows.
* Retention policy.
* Secure backup.
* Appliance registry.
* Optional research data products under explicit governance.

Default posture:

```text
least privilege
role-based access
sensitive by default
audited access
no casual browsing
no secondary use without consent
```

The clinic node should not expose sensitive data to game, ambient, or public clients unless a separate, explicit, minimized projection is approved.

---

## Speakers' Corner Memory Booth

The Speakers' Corner booth is a memory capture appliance.

It is inspired by public-access video booths, oral history stations, and civic feedback kiosks.

Primary functions:

* Voluntary recording.
* Audio/video capture.
* Consent screen.
* Session metadata.
* Transcript generation.
* Optional AI summary.
* Topic tagging.
* Publication scope selection.
* Personal archive contribution.
* Community archive contribution.
* Civic feedback contribution.

Possible modes:

```text
private
household
node_local
trusted_participants
public_symbolic
public_record
```

Example session flow:

```text
person enters booth
→ booth displays purpose and privacy options
→ person chooses scope
→ recording starts visibly
→ person records story or feedback
→ local transcript generated
→ person reviews transcript and summary
→ person accepts, edits, or deletes
→ record enters node archive
```

Forbidden uses:

* Passive surveillance.
* Covert recording.
* Relationship analysis without consent.
* Emotion scoring for institutional decisions.
* Political profiling.
* Public release without clear consent.

---

## BLE Lap Timing Mat

The BLE lap timing mat is a movement ritual appliance.

In Woodland Commons, it may sit on or near the 400 m loop trail.

Primary functions:

* Detect voluntary pass-by tags.
* Record loop completion events.
* Support walking and jogging rituals.
* Generate local movement events.
* Feed Pitchfork movement accounting.
* Support aggregate trail stewardship.

Preferred event:

```text
loop_completed
loop_id
timestamp
actor_id optional
tag_id
attestation_method = device_observed
```

Privacy posture:

* No camera required.
* No continuous location trace.
* No speed ranking by default.
* No public leaderboard by default.
* Anonymous aggregate counting allowed if configured.
* Individual tracking opt-in only.

Client projections:

```text
Wellness Notebook: "You completed a woodland loop."
Pitchfork RPG: "You gathered Ember Moss."
Nexus: "Ley Road activity increased."
Ambient World: "Paths have grown clearer."
Community Dashboard: "The loop was used 312 times this week."
```

---

## Workshop Station

The workshop station is a tool, project, and craft-memory appliance.

Primary functions:

* Tool checkout.
* Tool return.
* Maintenance logs.
* Project records.
* Safety notes.
* Material inventory.
* Optional project photo capture.
* Skill-sharing records.
* Workshop stewardship events.

Preferred records:

```text
tool_checked_out
tool_returned
tool_maintenance_logged
project_created
project_completed
material_used
workshop_stewardship_event
```

Forbidden uses:

* Worker productivity ranking.
* Secret skill scoring.
* Surveillance of informal work.
* Automatic discipline for tool use patterns.

---

## Garden Station

The garden station is a stewardship appliance.

Primary functions:

* Planting records.
* Harvest records.
* Watering logs.
* Compost logs.
* Volunteer contribution.
* Seasonal observations.
* Environmental sensors.
* Community food distribution.

Preferred posture:

* Contribution-oriented.
* Place-level memory.
* Optional personal attribution.
* Strong support for anonymous or group records.

Example projection:

```text
Garden bed 4 has been watered.
Tomatoes harvested this week: 12 kg.
Three residents contributed to the herb garden.
```

Avoid:

```text
Resident A failed to water plants.
Resident B is less committed than Resident C.
```

---

## Community Display

A community display is a projection appliance.

It may appear in:

* Household kitchen.
* Woodland Commons great hall.
* Clinic waiting area.
* Workshop.
* School lobby.
* Cooperative office.

Allowed outputs:

* Aggregates.
* Announcements.
* Consentful memories.
* Public events.
* Place-level trends.
* Symbolic projections.
* Governance notices.
* Service exchange listings.

Forbidden outputs:

* Sensitive personal records.
* Private wellness state.
* Individual rankings.
* Covert inferences.
* Relationship maps.
* Health predictions.
* Reproductive or cycle information.
* Children's private records.

---

# Data Model

## Appliance

```text
Appliance
- appliance_id
- node_id
- appliance_type
- display_name
- physical_location
- owner_ref
- custodian_ref
- firmware_version
- software_version
- policy_version
- status
- created_at
- updated_at
- retired_at
```

## Appliance Capability

```text
ApplianceCapability
- capability_id
- appliance_id
- capability_type
- data_classes_allowed
- event_types_allowed
- projection_types_allowed
- sensors_enabled
- ai_enabled
- network_required
- offline_supported
- created_at
- revoked_at
```

## Appliance Event

```text
ApplianceEvent
- event_id
- appliance_id
- node_id
- actor_id optional
- event_type
- occurred_at
- data_class
- permission_scope
- attestation_method
- source_sensor
- client_record_ref
- measures
- idempotency_key
- retention_policy_id
- created_at
```

## Memory Artifact

```text
MemoryArtifact
- artifact_id
- node_id
- appliance_id
- contributor_actor_id
- artifact_type
- title optional
- recording_ref optional
- transcript_ref optional
- summary_ref optional
- data_class
- permission_scope
- consent_grant_id
- publication_scope
- retention_policy_id
- created_at
- updated_at
- deleted_at
```

## Inference Record

```text
InferenceRecord
- inference_id
- node_id
- appliance_id optional
- subject_actor_id optional
- subject_group_id optional
- source_record_refs
- inference_type
- inference_body
- confidence
- model_or_rule_version
- purpose
- data_class
- permission_scope
- retention_policy_id
- challenge_status
- created_at
- updated_at
- deleted_at
```

## Appliance Audit Log

```text
ApplianceAuditLog
- audit_id
- node_id
- appliance_id
- actor_id optional
- action_type
- target_record_ref optional
- data_class
- permission_grant_id optional
- occurred_at
- result
- admin_override
- reason
```

---

# Consent and Permission Model

Every appliance operation should resolve to one of these patterns:

## No Personal Data

Example:

```text
stream_flow_sensor
```

No actor identity required.

Still requires node governance.

## Anonymous Aggregate

Example:

```text
trail_counter incremented
```

No direct actor identity.

Must avoid re-identification.

## Voluntary Identified Event

Example:

```text
resident used BLE tag to record loop completion
```

Requires consent or active participation.

## Contributed Artifact

Example:

```text
resident records a Speakers' Corner story
```

Requires explicit consent and publication scope.

## Sensitive Personal Record

Example:

```text
health-adjacent clinic record
```

Requires elevated safeguards, purpose limitation, and stricter access control.

## Inference About a Person

Example:

```text
AI summary identifies recurring theme in a person's recordings
```

Requires discoverability, challenge rights, retention policy, and purpose binding.

---

# PIPEDA and GDPR Design Conformance

Pancakes appliances should be designed to support Canadian PIPEDA and EU GDPR-style privacy obligations.

This document is not legal advice, but it defines product requirements aligned with those regimes.

## PIPEDA-Aligned Requirements

Appliances must support:

* Accountability.
* Identified purposes.
* Meaningful consent.
* Limiting collection.
* Limiting use, disclosure, and retention.
* Accuracy.
* Safeguards.
* Openness.
* Individual access.
* Challenge and complaint workflows.

Product implication:

```text
An appliance cannot collect data first and invent a purpose later.
```

## GDPR-Aligned Requirements

Appliances must support:

* Lawfulness, fairness, and transparency.
* Purpose limitation.
* Data minimization.
* Accuracy.
* Storage limitation.
* Integrity and confidentiality.
* Accountability.
* Access rights.
* Rectification.
* Erasure where applicable.
* Restriction of processing.
* Portability.
* Objection.
* Safeguards around automated decision-making and profiling.
* Strong protections for special category data.

Product implication:

```text
AI inference and profiling are governed processing activities.
```

## Special Category and Sensitive Inferences

The following require elevated protection:

* Health.
* Fertility.
* Menstrual cycles.
* Disability.
* Sexuality.
* Religion.
* Ethnicity.
* Political views.
* Union membership.
* Biometric identification.
* Children or dependent records.
* Household conflict.
* Financial vulnerability.

Appliances must not infer or expose these casually.

---

# AI Boundary

AI may be useful in appliances, especially for:

* Transcription.
* Summarization.
* Topic extraction.
* Oral history search.
* Accessibility.
* Translation.
* Duplicate detection.
* Archive organization.
* Stewardship suggestions.
* Aggregate trend analysis.

AI must not become ambient surveillance.

Do not build:

* A system that silently analyzes everyone nearby.
* A universal life summarizer.
* A hidden social graph.
* An institutional risk score.
* An automatic discipline engine.
* A health inference system without explicit consent.
* A system that makes significant decisions solely from AI inference.

Approved AI pattern:

```text
explicit record
→ scoped AI processing
→ visible output
→ user or steward review
→ correction/challenge path
```

Forbidden AI pattern:

```text
ambient capture
→ hidden analysis
→ secret profile
→ automated consequence
```

---

# The Bacon Computer Rule

The Bacon Computer Rule is named after the dystopian pattern in which a biosensor detects a bodily condition and an institution automatically restricts a person's food choice.

Pancakes appliances must not reproduce that pattern.

## Forbidden

```text
urinalysis
→ sodium inference
→ automatic cafeteria restriction
```

```text
mood inference
→ automatic meeting exclusion
```

```text
relationship inference
→ automatic housing decision
```

```text
movement score
→ automatic benefit reduction
```

## Allowed

```text
health signal
→ private note
→ user-visible recommendation
→ user decision
```

```text
aggregate concern themes
→ steward review
→ community governance process
```

```text
movement event
→ private ritual reward
→ optional symbolic projection
```

---

# Security Requirements

Appliances should support:

* Secure boot where practical.
* Signed updates.
* Encrypted storage.
* Encrypted transport.
* Local firewalling.
* Device identity.
* Node registration.
* Least-privilege service accounts.
* Role-based administration.
* Tamper-evident logs.
* Backup and restore.
* Rotation of keys and credentials.
* Physical reset procedure.
* Secure retirement and wipe.

For capture appliances:

* Visible recording indicator.
* Local buffer limits.
* Clear upload/sync state.
* Consent checkpoint.
* Fail-closed privacy mode.

For institutional appliances:

* Stronger access control.
* Admin audit.
* Separation of duties.
* Export approval.
* Incident response workflow.
* Retention enforcement.

---

# Offline and Sync

Appliances should tolerate network interruptions.

Preferred pattern:

```text
local capture
→ local queue
→ node sync
→ idempotent settlement
→ audit record
```

Events must include idempotency keys.

Offline devices must preserve:

* Consent context.
* Timestamps.
* Data class.
* Permission scope.
* Source appliance.
* Sync status.
* Deletion requests where feasible.

If consent cannot be verified, sensitive capture should not proceed.

---

# Physical Design Principles

Pancakes appliances should feel understandable and trustworthy.

Physical design should prefer:

* Visible state.
* Manual controls.
* Clear start/stop affordances.
* Local status lights.
* Repairability.
* Durable materials.
* Replaceable parts.
* Low noise.
* Non-institutional warmth where appropriate.
* Accessible placement.
* Plain-language labels.

Avoid:

* Black-box surveillance aesthetics.
* Hidden cameras.
* Unclear microphones.
* Dark-pattern interfaces.
* Always-on capture without signage.
* Devices that feel disciplinary.

A household appliance should feel like a domestic commons device.

A clinic appliance should feel professional and safe.

A memory booth should feel voluntary and ceremonial.

A workshop station should feel practical and durable.

---

# Repository Implications

The appliance model suggests separating repositories by responsibility.

Possible repository structure:

```text
pitchfork-core
pancakes-node
pancakes-appliance-sdk
pancakes-clients
pancakes-hardware-kits
pancakes-docs
```

## pitchfork-core

Contains:

* Event model.
* Accounting.
* Settlement.
* Caps.
* Ledgers.
* Resources.
* Covenants.
* Projection primitives.

## pancakes-node

Contains:

* Node runtime.
* Identity.
* Permissions.
* Appliance registry.
* Audit.
* Retention.
* Export/import.
* Local API.
* Admin UI.
* Backup.
* Policy engine.

## pancakes-appliance-sdk

Contains:

* Appliance registration.
* Event submission.
* Local queue.
* Consent UI helpers.
* Sensor adapters.
* Audit hooks.
* Firmware integration patterns.
* Test harnesses.

## pancakes-clients

Contains:

* Wellness Notebook.
* Redwitch.
* RPG.
* Nexus.
* Governance UI.
* Memory Explorer.
* Household Dashboard.

## pancakes-hardware-kits

Contains hardware reference designs for:

* Household node appliance.
* Speakers' Corner booth.
* BLE lap timing mat.
* Workshop station.
* Garden station.
* Community display.

## pancakes-docs

Contains:

* Architecture.
* Privacy and inference framework.
* Appliance design.
* Ethics framework.
* Deployment guides.
* Governance templates.
* Safety cases.

---

# Implementation Phases

## Phase 0: Paper Architecture

Deliverables:

* Appliance taxonomy.
* Node registry model.
* Appliance event model.
* Privacy and inference framework.
* Reference threat model.
* Consent and audit requirements.

## Phase 1: Virtual Appliance SDK

Build a software-only appliance simulator.

Capabilities:

* Register with node.
* Emit events.
* Queue offline events.
* Submit consented memory artifacts.
* Generate test audit logs.
* Test permission enforcement.

This proves the appliance contract before hardware.

## Phase 2: Household Node Appliance Prototype

Build a local node appliance using commodity hardware.

Minimum capabilities:

* Node runtime.
* Local web admin.
* Identity.
* Permission grants.
* Local database.
* Appliance registry.
* Export/import.
* Backup.
* Pitchfork event recording.

## Phase 3: BLE Lap Timing Prototype

Build the simplest physical event appliance.

Minimum capabilities:

* BLE tag detection.
* Loop completion event.
* Local queue.
* Node sync.
* User opt-in.
* Aggregate trail counts.
* RPG/Wellness projection.

## Phase 4: Speakers' Corner Booth Prototype

Build a memory capture appliance.

Minimum capabilities:

* Consent screen.
* Video/audio capture.
* Local transcript.
* Review before save.
* Scope selection.
* Node archive storage.
* Search and summary client.
* Access/correction/deletion workflow.

## Phase 5: Institutional Node Profile

Adapt the node appliance for clinics, schools, co-ops, and community institutions.

Minimum capabilities:

* Role-based access.
* Strong audit logs.
* Retention policies.
* Export approval.
* Data classification enforcement.
* Sensitive data safeguards.
* Governance templates.

---

# Woodland Commons Reference Deployment

Woodland Commons can serve as a conceptual reference deployment.

Possible appliance set:

```text
Household Node Appliances
- One per residence or household cluster.

Commons Node
- Shared node for community-level records.

BLE Loop Timing Mat
- 400 m woodland loop movement events.

Speakers' Corner Booth
- Oral history and community memory.

Workshop Station
- Tool checkout and project archive.

Garden Station
- Planting, harvest, and stewardship records.

Community Display
- Aggregate commons state and announcements.

Ambient Projection System
- Symbolic environmental or Nexus-style projections.

Backup Vault
- Encrypted local backups and continuity.
```

The key principle:

```text
The technology supports the commons.
It does not dominate the commons.
```

Visitors should notice:

* Trees.
* Stream.
* Trails.
* Homes.
* Workshop.
* Great hall.
* Community life.

Only later should they discover the node infrastructure beneath the surface.

---

# Open Questions

* What is the minimum appliance contract?
* Should appliances communicate over HTTP, MQTT, local message bus, or all three?
* How should appliance identity be provisioned?
* What hardware platform should be the first reference household node?
* Should the Speakers' Corner booth use local-only transcription by default?
* How should consent be represented for public memory artifacts?
* How should inferences be deleted when source artifacts remain?
* Should appliances support anonymous mode?
* What is the boundary between a client and an appliance?
* Which appliances are safe for children or dependent contexts?
* What is the first safety case?
* What belongs in `pancakes-node` vs `pancakes-appliance-sdk`?
* How should offline appliances handle revoked consent?
* How should a node publish an appliance registry to members?
* What should the physical design language be?

---

# Working Rule

Before adding any Pancakes appliance, answer:

```text
What node owns it?
What purpose does it serve?
What data does it collect?
What inferences can it generate?
Who can access the records?
Who can challenge or delete them?
What happens offline?
What happens if the appliance is stolen?
What happens when the appliance is retired?
Can people opt out?
Can this work with less data?
Can this work without identifying people?
Can this be symbolic or aggregate instead?
Can this ever make decisions about people?
```

If the appliance cannot answer these questions, it is not ready for implementation.

---

# Final Principle

Pancakes appliances should make communities more capable of remembering, caring, coordinating, and governing themselves.

They should not make communities more capable of surveilling, ranking, controlling, or extracting from their members.

The appliance model is successful only if it makes local life more humane.
