# Wellness Notebook

## Final Unified Product & Architecture Design Proposal

### Pancakes / Pitchfork Native Behavioral Wellness Client

This document consolidates and supersedes all prior Wellness Notebook proposals, revisions, and Pitchfork assessments. It serves as the authoritative build baseline for the first implementation.

Sources incorporated:

* Original MVP proposal
* Pitchfork-native revision
* Build baseline addendum
* Final implementation clarifications

---

# 1. Executive Summary

Wellness Notebook is a local-first behavioral wellness client for the Pancakes / Pitchfork ecosystem.

The product is inspired by late-2000s wellness software such as Nintendo DS wellness applications that emphasized:

* finite daily participation,
* gentle accountability,
* behavioral continuity,
* emotionally sustainable interaction.

The system intentionally rejects:

* quantified-self obsession,
* punitive optimization,
* addictive engagement loops,
* surveillance-oriented wellness design,
* public comparison pressure.

The core product thesis:

> A lightweight wellness system consistently used is more valuable than a precise system abandoned.

Wellness Notebook is not:

* a standalone wellness SaaS,
* a medical platform,
* a calorie optimizer,
* a productivity surveillance system,
* a centralized health-data warehouse.

It is:

* a behavioral wellness notebook,
* a daily ritual interface,
* a private reflection environment,
* a Pancakes client,
* a producer of permissioned Pitchfork events.

---

# 2. Governing Architectural Principle

Wellness Notebook is not the ecosystem source of truth.

The architecture is:

```text
private client records
→ node identity + permission checks
→ minimal Pitchfork events
→ capped settlement
→ derived symbolic projections
→ client-specific presentation
```

Pitchfork accounts.

Clients interpret.

Nodes govern.

Identity authorizes.

Pancakes humanizes.

---

# 3. Product Philosophy

## 3.1 Core UX Goals

The application should feel like:

* a notebook,
* a companion,
* a daily ritual,
* a lightweight coach.

It should not feel like:

* enterprise analytics software,
* quantified-self telemetry,
* fitness surveillance,
* competitive productivity software.

---

## 3.2 Finite Daily Closure

Every session should feel:

* achievable,
* emotionally complete,
* bounded,
* non-overwhelming.

The product must avoid:

* infinite dashboards,
* endless optimization,
* permanent failure states,
* compulsive tracking pressure.

---

## 3.3 Low Psychic Friction

The system minimizes:

* shame,
* guilt,
* overwhelm,
* perfectionism,
* self-monitoring fatigue.

This is a first-class engineering and QA requirement.

---

## 3.4 Approximate Logging

The system intentionally favors:

* broad categories,
* coarse measures,
* behavioral summaries,
* qualitative participation.

The MVP avoids:

* calorie precision,
* macro optimization,
* barcode scanning,
* biometric surveillance,
* GPS tracking.

---

## 3.5 Gentle Coaching

Approved coaching behavior:

* encouragement,
* participation reinforcement,
* recovery framing,
* lightweight reflection.

Approved examples:

* “You checked in today.”
* “One healthy action still counts.”
* “Missing a day happens.”

Prohibited examples:

* “You failed.”
* “Your discipline is slipping.”
* “You missed your streak.”

---

# 4. System Context

## 4.1 Pancakes Node

The node governs:

* identity,
* policy,
* permissions,
* audit,
* export/import,
* retention.

## 4.2 Pitchfork

Pitchfork:

* records permissioned events,
* applies caps,
* settles symbolic resources,
* creates projections,
* preserves auditability.

Pitchfork should generally receive:

* coarse,
* derived,
* bounded,
* permissioned events.

Pitchfork should not receive:

* raw intimate records,
* detailed reflections,
* sensitive wellness context.

## 4.3 Wellness Notebook Client

Wellness Notebook:

* owns private UX records,
* stores local wellness history,
* manages ritual interaction,
* emits minimal Pitchfork events,
* preserves emotional safety.

---

# 5. MVP Product Scope

## 5.1 Daily Session

The Daily Session is the central interaction loop.

It includes:

* objectives,
* movement summary,
* food balance summary,
* activity summary,
* challenge,
* coaching message,
* completion state,
* optional reflection.

Important separation:

```text
DailySession = ordinary personal metadata
SensitiveReflection = sensitive local/private content
```

Mood and reflection text must never live directly on ordinary session records.

---

## 5.2 Movement Tracking

MVP movement tracking is:

* manual,
* coarse,
* local-first.

Features:

* manual step entry,
* movement summaries,
* adaptive participation goals.

Out of MVP:

* Apple Health,
* Google Fit,
* smartwatch sync,
* GPS,
* route traces,
* live movement telemetry.

Exact step counts remain client-private.

Pitchfork receives only:

* step bands,
* movement bands,
* completion signals.

---

## 5.3 Food Balance Logging

Food tracking models:

> behavioral balance

rather than:

> nutritional optimization.

MVP food categories:

* fruits/vegetables,
* protein,
* grains,
* sweets,
* beverages,
* snacks.

Meal types:

* breakfast,
* lunch,
* dinner,
* snack.

No:

* calorie counting,
* macros,
* barcode scanning,
* nutrition databases.

---

## 5.4 Activity Logging

Activity logging supports:

* quick mode,
* detailed mode.

Quick mode:

```text
light
moderate
intense
```

Detailed mode:

```text
activity_family
duration_band
intensity
```

Examples:

* walking,
* stretching,
* yoga,
* gardening,
* cleaning,
* cycling.

The system intentionally validates ordinary movement as meaningful participation.

---

## 5.5 Challenges

Challenges provide:

* novelty,
* small nudges,
* behavioral continuity,
* gentle engagement.

Approved categories:

```text
movement
hydration
food_balance
mindfulness_general
rest_general
environment
routine
```

Sensitive challenge categories must never be projected into Pitchfork measures.

---

## 5.6 Coaching

MVP coaching is:

* lightweight,
* rule-based,
* deterministic,
* non-medical.

Not allowed:

* diagnosis,
* therapy simulation,
* AI ingestion of reflections,
* mental-health inference,
* behavioral scoring.

---

# 6. Technical Architecture

## 6.1 Runtime Philosophy

Primary architecture:

```text
single local Pancakes node
→ local database
→ local users
→ local Pitchfork module
→ export/import
→ optional hosted deployment
```

Hosted deployment must not become the privileged architecture.

---

## 6.2 Technical Stack

### Backend

* Python 3.12+
* Flask
* Gunicorn
* SQLAlchemy
* Alembic

### Database

* PostgreSQL or SQLite depending on node profile

### Frontend

* Jinja2
* HTMX
* minimal Alpine.js

### Infrastructure

* Docker
* Nginx
* GitHub Actions

### Cache / Operational State

* Redis (restricted operational use only)

---

## 6.3 Redis Rules

Redis may store:

* session IDs,
* CSRF/session metadata,
* rate-limit counters,
* idempotency locks,
* short-lived job IDs.

Redis must never store:

* reflections,
* moods,
* symptoms,
* food notes,
* raw EventRequests,
* full client records,
* exact GPS,
* secrets.

Background jobs must pass IDs only.

---

# 7. Data Classification

Every record must include `data_class`.

Allowed values:

```text
public
node_shared
household
group
personal
sensitive
regulated_high_risk
economic
cryptographic_secret
```

---

## 7.1 Personal Data

Examples:

* daily session completion,
* movement bands,
* challenge completion,
* food categories,
* activity summaries.

---

## 7.2 Sensitive Data

Examples:

* reflections,
* moods,
* symptoms,
* sleep notes,
* disorder-adjacent notes,
* pregnancy-related wellness notes,
* household conflict.

---

## 7.3 Regulated High Risk

Out of MVP:

* GPS traces,
* medical records,
* raw wearable telemetry.

---

# 8. Permission Scopes

Allowed values:

```text
private
local_client
node_local
household
guild
trusted_participants
public_symbolic
economic_settlement
```

MVP defaults:

```text
private
local_client
```

---

# 9. Identity Model

Pitchfork-facing identity primitives:

```text
actor_id
node_id
```

`local_user_id` may exist for Flask internals only.

Every projectable record must resolve to:

* actor_id,
* node_id,
* permission grant.

---

# 10. Core Data Model

## 10.1 NodeRef

```text
NodeRef
- node_id
- node_type
- policy_version
```

---

## 10.2 ActorRef

```text
ActorRef
- actor_id
- node_id
- identity_claim_id
- assurance_level
```

---

## 10.3 DailySession

```text
DailySession
- id
- node_id
- actor_id
- local_user_id
- session_date
- completion_state
- data_class = personal
- permission_scope
- retention_policy_id
- retention_policy_version
- created_at
- updated_at
- deleted_at
```

---

## 10.4 SensitiveReflection

```text
SensitiveReflection
- id
- node_id
- actor_id
- session_id
- encrypted_body
- mood_label optional
- data_class = sensitive
- permission_scope
- retention_policy_id
- retention_policy_version
- encrypted_at
- export_inclusion_default = false
- last_sensitive_access_audit_id
- created_at
- updated_at
- deleted_at
```

Defaults:

* not AI-readable,
* not projectable,
* not included in analytics,
* not logged.

---

## 10.5 MovementLog

```text
MovementLog
- id
- node_id
- actor_id
- local_user_id
- session_id
- exact_step_count
- source_type = manual
- data_class = personal
- permission_scope = local_client

- pitchfork_permission_grant_id
- pitchfork_event_id
- pitchfork_idempotency_key
- pitchfork_event_status
- pitchfork_last_error_code
- pitchfork_last_attempt_at

- retention_policy_id
- retention_policy_version

- created_at
- updated_at
- deleted_at
```

---

## 10.6 FoodBalanceLog

```text
FoodBalanceLog
- id
- node_id
- actor_id
- session_id
- meal_type
- food_category
- quantity_estimate
- data_class
- permission_scope

- pitchfork_permission_grant_id
- pitchfork_event_id
- pitchfork_idempotency_key
- pitchfork_event_status

- retention_policy_id
- retention_policy_version

- created_at
- updated_at
- deleted_at
```

Food records escalate to `sensitive` if they include:

* medical diet context,
* eating-disorder-adjacent content,
* dependent records,
* symptoms,
* pregnancy context,
* free-text notes.

MVP recommendation:

* no free-text food notes.

---

## 10.7 ActivityLog

```text
ActivityLog
- id
- node_id
- actor_id
- session_id
- activity_family
- duration_band
- intensity
- data_class
- permission_scope

- pitchfork_permission_grant_id
- pitchfork_event_id
- pitchfork_idempotency_key
- pitchfork_event_status

- retention_policy_id
- retention_policy_version

- created_at
- updated_at
- deleted_at
```

---

## 10.8 ChallengeAttempt

```text
ChallengeAttempt
- id
- node_id
- actor_id
- session_id
- challenge_category
- completion_state
- data_class
- permission_scope

- pitchfork_permission_grant_id
- pitchfork_event_id
- pitchfork_idempotency_key
- pitchfork_event_status

- retention_policy_id
- retention_policy_version

- created_at
- updated_at
- deleted_at
```

---

# 11. Retention Model

Required fields:

```text
retention_policy_id
retention_policy_version
deleted_at
```

Allowed MVP policy IDs:

```text
user_controlled
sensitive_user_controlled
audit_minimal
backup_limited
node_policy
```

Future fields:

```text
purged_at
projection_deleted_at
backup_delete_after
```

Soft-deleted records must not appear in:

* exports,
* dashboards,
* projections,
* event builders.

---

# 12. Permission Grants

Separate grants are required.

## Personal Participation Grant

```text
grant_private_participation
```

Allowed event types:

* movement_logged,
* activity_logged,
* food_balance_logged,
* daily_session_completed,
* challenge_completed.

---

## Sensitive Completion Grant

```text
grant_sensitive_reflection_completion
```

Allowed event types:

* reflection_completed,
* rest_logged.

Sensitive grants must:

* be narrower,
* separately auditable,
* completion-only.

---

# 13. Pitchfork Event Flow

Canonical flow:

```text
private client record
→ permission grant lookup
→ EventRequest builder
→ PitchforkAdapter
→ record_event()
→ settlement persistence
→ audit hook
```

---

# 14. Event Types

MVP supported types:

```text
movement_logged
activity_logged
food_balance_logged
daily_session_completed
challenge_completed
reflection_completed
rest_logged
```

---

# 15. Measures

## Movement

Pitchfork receives:

```json
{
  "movement_band": "light",
  "step_band": "2500_4999"
}
```

Never:

```json
{
  "exact_steps": 4327
}
```

---

## Food

```json
{
  "meal_type": "lunch",
  "balance_categories": ["fruits_vegetables", "protein"],
  "quantity_estimate": "some"
}
```

---

## Activity

```json
{
  "activity_family": "walking",
  "duration_band": "10_29_minutes",
  "intensity": "light"
}
```

---

## Reflection

```json
{
  "reflection_completed": true
}
```

No raw reflections.

---

# 16. Projection Registry

Projection types must come from a registry.

Initial registry:

```text
pitchfork_rpg_private
wellness_notebook_local_summary
nexus_private_summary
ambient_private_symbolic
```

MVP-active:

```text
pitchfork_rpg_private
wellness_notebook_local_summary
```

---

# 17. Settlement and Caps

Pitchfork settlement is authoritative.

Clients must not create uncapped reward systems.

Example:

```text
daily_wellness_participation:
  event_type: daily_session_completed
  period: day
  max_private_resource_grants: 1
```

Participation should yield:

```text
baseline access
```

not:

```text
optimization pressure
```

---

# 18. Pitchfork Event Status

Allowed transitions:

```text
not_submitted -> pending
pending -> accepted
pending -> rejected
pending -> retryable_error
pending -> permission_revoked
retryable_error -> pending
retryable_error -> rejected
permission_revoked -> pending only after new permission_grant_id
accepted -> terminal
rejected -> terminal unless manually reclassified
```

---

# 19. Failure Behavior

If Pitchfork write fails:

```text
1. Preserve private record.
2. Persist failure state.
3. Retry safely if retryable.
4. Never shame the user.
```

Approved copy:

```text
Your notebook entry was saved.
```

Avoid:

```text
Your activity did not count.
```

---

# 20. Security Requirements

Required:

* Argon2 password hashing,
* CSRF protection,
* HTTPS,
* secure cookies,
* SQL injection prevention,
* dependency scanning.

Sensitive content must never appear in:

* logs,
* analytics,
* Redis,
* AI context,
* error payloads.

---

# 21. Audit Requirements

Audit required for:

* event writes,
* sensitive access,
* permission changes,
* exports,
* imports,
* projections,
* admin override,
* AI processing.

Audit records must not contain raw sensitive payloads.

---

# 22. Export / Import

Exports are first-class features.

Pitchfork exports:

* events,
* settlements,
* projections,
* audit metadata,
* permission grants.

Client exports:

* private records,
* sensitive records only with explicit inclusion.

Sensitive exports should support encryption.

---

# 23. Hard Lines

Never send to Pitchfork by default:

* raw journal text,
* detailed moods,
* symptoms,
* cycle/fertility data,
* trauma reflections,
* household conflict,
* dependent records,
* GPS traces,
* secrets,
* wallet keys.

Never use Pitchfork for:

* public wellness scoring,
* insurance scoring,
* employment scoring,
* productivity ranking,
* covert AI ingestion,
* pay-per-step economics.

---

# 24. QA Requirements

## 24.1 Behavioral QA

Release-blocking questions:

* Does this induce shame?
* Does this imply punishment?
* Does this encourage obsession?
* Does this create emotional exhaustion?

---

## 24.2 Security QA

Required tests:

* permission enforcement,
* grant revocation,
* sensitive log redaction,
* Redis payload validation,
* export authorization,
* adapter idempotency.

---

## 24.3 Required Contract Test

Before broader implementation:

```text
MovementLog exact steps saved privately
→ EventRequest contains only step_band
→ permission grant checked
→ record_event called with idempotency key
→ settlement accepted
→ event_id/status persisted
→ exact steps absent from logs/Redis/Pitchfork payload
```

This becomes the template for all event builders.

---

# 25. Thin Integration Layer

Highest-risk module:

```text
PitchforkAdapter / PitchforkEventBuilder
```

Responsibilities:

* resolve actor/node,
* classify data,
* coarsen measures,
* validate projection types,
* select grants,
* generate idempotency keys,
* redact logs,
* persist settlement safely.

This module requires the highest test coverage.

---

# 26. Recommended First Build Slice

```text
1. Shared enums/constants
2. Projectable model fields
3. PitchforkAdapter
4. Movement EventRequest builder
5. Challenge EventRequest builder
6. Redaction/idempotency tests
7. End-to-end movement contract test
8. Expand to food/activity/session/reflection
```

Movement is the preferred first implementation because:

* private exact data maps naturally to coarse Pitchfork measures,
* it exercises the full permission + settlement flow,
* it validates the adapter architecture early.

---

# 27. Final Architecture Definition

Wellness Notebook is:

```text
a local-first Pancakes wellness client
with private behavioral records
that emits minimal, permissioned Pitchfork events
for capped symbolic settlement and private projections
without exposing raw intimate life data
while preserving psychologically safe daily participation.
```
