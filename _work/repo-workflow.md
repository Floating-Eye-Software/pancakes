# FLEY Repository Workflow

This document defines the common operational workflow for Floating Eye Software
(FLEY) execution repositories.

It establishes the shared engineering execution model used across FLEY projects
while remaining independent of any particular programming language, framework,
or regulatory domain.

Repository workflows are the top-level operational authority for how FLEY
repository work is performed. Higher-level organizational governance, including
the FLEY Quality Management System (QMS), applies to repository work through
the interfaces defined by this workflow.

This workflow is intentionally technology-neutral. It defines common engineering
behavior rather than prescribing particular programming languages, build
systems, test runners, or development tools.

---

# Purpose

The repository workflow provides a common way to organize engineering work
across FLEY repositories.

It governs:

* planning and execution within a repository;
* repository-local work tracking;
* engineering documentation;
* engineering verification activities;
* coordination between repositories;
* contributor expectations;
* session management for human and AI contributors.

The workflow intentionally defines the complete operational execution model for
repository work. It does not replace QMS authority over governed obligations,
approvals, or controlled records; it provides the operational path through
which those obligations are exercised.

It does not define:

* organizational strategy;
* Management Review;
* controlled document approval;
* Design Control;
* CAPA;
* formal verification or validation;
* other QMS-governed activities.

Those responsibilities remain authoritative in the applicable higher governance
layers, while this workflow must provide and maintain the repository interfaces
needed to execute them.

The repository workflow should remain stable even as repository technologies,
organizational structure, and QMS processes evolve. Changes to it must be
reviewed for continued coverage of applicable QMS requirements.

---

# Capabilities and Obligations

The FLEY architecture intentionally separates **engineering capability** from
**governance obligations**.

Repository workflows define the required operational capabilities and
interfaces through which repository work is controlled.

The QMS determines which obligations, approvals, records, and evidence are
required. The workflow must maintain the execution paths, ownership rules,
review points, and evidence surfaces needed to satisfy those requirements.

Repository workflows answer:

> How is engineering work performed?

The QMS answers:

> Which engineering activities are required, reviewed, approved, recorded, and
> retained?

This distinction allows the workflow to remain the operational authority while
QMS requirements evolve under controlled governance.

For example:

| Repository Capability  | Governance Responsibility                                            |
| ---------------------- | -------------------------------------------------------------------- |
| `make test`            | determine whether execution constitutes formal verification evidence |
| Pull Request           | determine approval requirements                                      |
| Git tag                | determine whether it represents an approved release baseline         |
| Markdown documentation | determine whether the document is controlled                         |
| Repository plans       | determine whether they satisfy Quality Planning activities           |
| Repository tasks       | determine whether they satisfy controlled planning activities        |
| Risk records           | determine whether they become controlled organizational risks        |

**The workflow controls operational execution. The QMS controls governed
obligations.**

Governance should use the workflow's defined interfaces rather than bypassing
or silently redefining repository execution.

---

# Relationship to the FLEY QMS

The repository workflow forms the operational execution layer of the FLEY
architecture.

Repository execution continuously produces engineering outputs, including:

* source code;
* documentation;
* engineering tests;
* design discussions;
* repository workstream summaries;
* implementation plans;
* repository tasks;
* repository status information.

Higher-level governance processes may consume these outputs.

For example:

* Design Control may designate repository tests as formal verification
  activities.
* Document Control may designate selected Markdown files as controlled
  documents.
* Management Review may use repository status information as organizational
  input.
* Quality Planning may reference repository plans.
* Risk Management may promote repository observations into controlled risk
  records.

Repository workflows intentionally define stable engineering interfaces that
higher-level governance may invoke. Examples include repository test commands,
planning artifacts, pull requests, engineering documentation, release
procedures, and status reports.

Higher-level governance should state its requirements and use these interfaces
rather than bypassing or silently redefining repository execution. The
workflow must be reviewed whenever those interfaces or their QMS coverage
change.

The repository workflow therefore provides engineering capabilities.

The QMS imposes governance obligations through the workflow interface.

Neither replaces the other.

---

# Relationship to Organizational Governance

This workflow is paired with:

`fley-org/process/org-process.md`

which governs organization-level reconciliation, cross-repository routing,
organizational wrap-up, and enterprise coordination.

Repository workflows own engineering execution.

Organization workflows own organizational coordination.

The QMS owns controlled governance processes.

Together they form a layered architecture:

```text
Engineering Execution
        ↓
Organizational Coordination
        ↓
Governance
```

Each layer builds upon the previous one without replacing it.

---

# Work Surfaces

Repository work is organized around three levels of durable engineering
artifacts:

```text
Workstream
    ↓
Plan
    ↓
Task
```

**Workstreams** describe the repository's durable top-level priorities and
responsibilities.

**Plans** describe bounded multi-step change efforts within one or more
workstreams.

**Tasks** describe concrete, verifiable engineering work that can be completed,
reviewed, and tracked independently.

Workstreams are intentionally broader and longer-lived than plans. A workstream
may contain many plans over time, and the set of active plans may change
without changing the repository's workstream structure.

Plans should be created when work involves:

* multiple implementation steps;
* uncertainty;
* dependencies;
* acceptance criteria;
* architectural decisions.

Tasks should describe executable engineering work.

Stable plan and task identifiers shall not be reused.

`_work/quick-status.md` is authoritative for the repository's current
workstream names and top-level priority summary. Plan and task dashboards remain
authoritative for execution state, dependencies, and detailed scheduling.

Workstreams, plans, and tasks track repository-owned work.

They do not replace organization registries or controlled QMS records.

Creating a plan, task, note, or other authoritative repository artifact
constitutes successful transfer of responsibility from conversation into the
repository.

Conversation history should not remain the authoritative engineering record.

Repository work surfaces should remain:

* durable;
* version controlled where practical;
* reviewable;
* independently understandable;
* suitable for future contributors.

---

# Repository Authority

Execution repositories own:

* engineering implementation;
* local workstreams and priority summaries;
* local planning;
* engineering tasks;
* engineering documentation;
* local testing;
* engineering acceptance criteria;
* repository architecture;
* repository-local risks;
* local release readiness.

Repository workflows intentionally avoid governing organization-wide concerns.

Those belong to their respective authoritative processes.

---

# Organization Authority

Organization-level authority resides within `fley-org`.

Examples include:

* repository topology;
* portfolio management;
* publication registry;
* organizational coordination;
* enterprise initiatives.

Organization registries describe organizational state rather than executable
repository work.

---

# QMS Authority

Controlled governance resides within `fley-qms`.

Examples include:

* SOPs;
* Work Instructions;
* Design Control;
* Change Control;
* CAPA;
* Management Review;
* Document Control;
* Risk and Opportunity Management;
* Quality Planning.

These processes may reference repository artifacts while remaining
authoritative for governance decisions.

---

# Work Tracking

Workstreams, plans, and tasks remain repository-owned engineering artifacts.

Workstreams:

* define the repository's current top-level priorities and responsibilities;
* are broader and more durable than individual plans;
* provide a compact situational view for maintainers, contributors, and
  organization-wide tooling;
* may remain active across many plans and implementation cycles;
* should not be created merely to represent every directory, component, or
  possible future activity.

Plans:

* describe bounded engineering objectives within a workstream;
* identify dependencies;
* define acceptance criteria;
* coordinate multi-step work.

Tasks:

* identify concrete executable engineering work;
* reference plans where applicable;
* record execution state;
* should be independently reviewable whenever practical.

Repository dashboards describe detailed engineering execution. Quick status
describes the repository-level workstream view.

Higher-level governance may reference repository workstreams, plans, and tasks
but should not duplicate repository execution state.

---

# Quick Status

Every FLEY workflow repository shall maintain:

```text
_work/quick-status.md
```

The quick-status file is the repository's compact workstream summary. It exists
so a maintainer, contributor, or organization-wide tool can understand the
repository's major priorities without reconstructing them from plans, tasks,
Git history, or conversation context.

The file should remain **under 40 lines** unless a repository documents a
specific reason for a different limit.

A normal quick-status file has:

```markdown
# Quick Status

Last update: YYYY-MM-DD

### <workstream>
* current state or objective
* major next direction

### <workstream>
* current state or objective
* major next direction

[//]: # "keep this file under 40 lines; history belongs in reports/"
```

Each level-three Markdown heading (`###`) defines one current **workstream**.

Workstream names should be:

* stable enough to remain useful across multiple plans;
* broad enough to describe a major repository responsibility;
* specific enough for organization-wide scripts and agents to distinguish;
* few enough that the file remains an actual prioritization surface.

Each workstream should normally contain one to four bullets describing:

* current state;
* current objective;
* major next direction;
* a significant blocker or constraint, when one materially affects the
  workstream.

Do not copy detailed task lists, dependency graphs, acceptance criteria, or
historical narrative into quick status.

History belongs in reports, plans, Git history, or other durable records.

A repository with no substantial active work should say so concisely rather
than manufacture workstreams or plans.

Quick status has a deliberately narrow authority boundary:

* `_work/quick-status.md` is authoritative for current workstream names and the
  repository's condensed top-level priority summary;
* `_work/plans/plans.csv` is authoritative for plan execution state;
* `_work/tasks.csv` is authoritative for task execution state;
* organization registries remain authoritative for portfolio, project,
  repository, and publication state;
* controlled QMS records remain authoritative for governed decisions and
  obligations.

When quick status disagrees with the underlying engineering state, reconcile it
promptly. A workstream summary must not claim that a plan or task is complete
when its authoritative dashboard says otherwise.

Organization-wide telemetry may parse `###` headings and their bullets to
produce cross-repository situational summaries. The format should therefore
remain simple Markdown and should not depend on custom front matter, embedded
JSON, or repository-specific syntax.

Do not create a separate `workstreams.csv` merely to duplicate quick status.
If future automation requires stronger workstream metadata, extend this
workflow deliberately rather than introducing parallel state informally.


# CSV Surface Types

CSV files used for coordination in Floating Eye repositories fall into two
governed categories.

## Workflow Dashboards

Workflow dashboards describe executable engineering work owned by the
repository.

Accepted dashboard labels include:

* `tasks`
* repository-specific task dashboards
* other engineering dashboards defined by the local workflow

Workflow dashboards:

* belong to the repository that owns the work;
* track execution state;
* do not replace organizational registries.

## Organization Registries

Organization registries belong to `fley-org`.

They describe organization-level state such as:

* repository topology;
* project lifecycle;
* portfolio membership;
* publication governance.

Registries should have:

* a documented schema;
* a clear authority boundary;
* sufficient evidence or notes to justify each record.

Registries do not track executable engineering work.

Repository engineering work belongs in repository plans and task dashboards.

Do not treat arbitrary CSV data files as governance artifacts merely because
they use CSV format.

Analysis datasets, exports, fixtures, and other engineering data remain
repository-local unless a documented workflow explicitly governs them.

---

# Plan Closure

Plans should remain open until:

* acceptance criteria are satisfied;
* verification is complete;
* residual follow-up work is identified;
* the user explicitly approves closure.

Plans requiring outcome review should include a Verification of Effectiveness
(VoE) section summarizing:

* objectives achieved;
* supporting evidence;
* residual risks;
* follow-up work;
* lessons learned.

Codex should identify plans that appear to satisfy their acceptance criteria.

Closure review should occur after verification but before marking a plan
`done`.

The closure prompt should summarize:

* the completed objectives;
* supporting evidence;
* residual risks;
* remaining follow-up work.

If the user confirms closure:

* update the plan status;
* update dashboard state;
* record the closure in the Codex log if applicable.

If the user does not approve closure, leave the plan open and record remaining
work as appropriate.

---

# Dashboard Schema

Repository dashboards provide the authoritative execution state for engineering
work.

## Plans

`_work/plans/plans.csv`

```csv
id,status,track,priority,depends_on,notes
```

## Tasks

`_work/tasks.csv`

```csv
id,status,plan,track,priority,depends_on,notes
```

Task notes that do not belong in the dashboard may be recorded in:

```text
_work/tasks.md
```

---

## Status Values

Supported workflow states are:

* `todo`
* `ready`
* `doing`
* `review`
* `blocked`
* `parked`
* `done`
* `dropped`

Definitions:

* **todo** — work exists but has not yet been evaluated for execution.
* **ready** — all declared dependencies are complete and the work may begin.
* **doing** — engineering work is actively underway.
* **review** — implementation is complete and awaiting review or verification.
* **blocked** — execution cannot continue because a dependency or external
  condition remains unresolved.
* **parked** — intentionally deferred without cancellation.
* **done** — completed.
* **dropped** — intentionally abandoned.

Rows in `ready` must not have unfinished dependencies.

Rows in `blocked` should identify the dependency or external condition
preventing execution.

---

## Dependency Rules

Dependency relationships should form an acyclic graph.

Separate multiple dependencies using:

```text
|
```

Dependencies should identify engineering prerequisites rather than merely
describing preferred sequencing.

---

## Dashboard Consistency

Repository dashboards should remain internally consistent.

Validation should ensure:

* valid statuses;
* valid priorities;
* valid references;
* valid dependency syntax;
* acyclic dependency graphs;
* plans and associated plan files remain synchronized;
* active tasks reference existing plans where applicable;
* `ready` rows have no unfinished declared dependencies;
* `doing` and `review` rows have no unfinished declared dependencies;
* tasks attached to plans in `doing` should have a parent plan also in
  `doing`.

---

## Priority Values

Priority values are:

* `P0` — urgent or blocking.
* `P1` — milestone-critical.
* `P2` — useful soon.
* `P3` — later or housekeeping.

Repositories may define additional scheduling practices while preserving the
common priority vocabulary.

---

## Repository Validation

Repositories should provide narrow validation appropriate to their workflow.

Typical checks include:

```text
make check-plans
make check-tasks
make check-registries
```

Repository-specific validation commands may extend these checks while preserving
the common workflow semantics.

---

# Codex Sessions

Codex sessions should preserve repository integrity while minimizing unnecessary
changes.

The repository remains the authoritative engineering record.

Conversation is transient.

Repository artifacts are durable.

---

## Session Start

Before making changes:

* inspect `git status`;
* inspect `_work/quick-status.md`;
* identify the relevant workstream;
* inspect relevant plans;
* inspect relevant tasks;
* inspect relevant repository documentation when needed;
* identify the intended files before editing;
* understand the current engineering state before proposing changes.

Unexpected repository state should be acknowledged before proceeding.

---

## During Execution

Engineering work should remain focused.

Codex should:

* keep changes narrowly scoped to the requested work;
* maintain plans and task dashboards when execution state changes;
* record durable engineering findings in repository artifacts;
* avoid unrelated modifications;
* preserve existing repository conventions whenever practical;
* prefer durable repository-local processes over ephemeral experiments in
  `/tmp` or other transient environments whenever practical;
* prefer reusable tests, scripts, fixtures, documentation, or `make` targets
  over one-off verification commands whenever practical;
* avoid introducing temporary engineering debt merely to complete a task;
* do not install software, modify the development environment, or make
  persistent environment changes unless explicitly requested by the user.

Repository-local engineering processes should generally be preferred over
session-specific workarounds.

---

## Verification

Where practical, verify engineering work before declaring completion.

Verification should use repository-owned engineering processes.

Prefer documented repository commands such as:

```text
make test
make lint
make check-plans
make check-tasks
```

or their documented repository equivalents.

When verification cannot be completed, clearly identify:

* what was verified;
* what was not verified;
* why verification could not be completed.

Repository testing remains governed by the repository testing process.

---

## Wrap-Up

Before concluding a session:

* update `_work/quick-status.md` when repository-level workstreams or top-level
  priorities materially change;
* update plans when objectives change;
* update task status when execution changes;
* record durable engineering notes where appropriate;
* identify remaining follow-up work;
* identify plans that may be ready for closure.

Wrap-up should leave the repository in a state that another contributor can
understand without relying upon conversation history.

---

## Plan Completion

When a plan appears complete:

* summarize completed objectives;
* summarize supporting evidence;
* summarize remaining follow-up work;
* identify residual risks if known;
* ask whether the user wishes to close the plan.

Codex should recommend plan closure when appropriate.

Codex should never close plans without explicit user approval.

---

## Repository State

Repository modifications should be intentional.

Avoid:

* partially updated dashboards;
* orphaned tasks;
* stale execution state;
* undocumented engineering changes;
* incomplete engineering notes when they materially affect future work.

Repository consistency is preferred over conversational convenience.

---

# Routing Boundaries

Routing selects the authoritative owner for engineering and governance
information.

Every durable artifact should have one authoritative owner.

Higher governance layers should reference repository artifacts rather than
duplicate them whenever practical.

---

## Execution Repositories

Execution repositories own:

* implementation;
* engineering workstreams;
* engineering plans;
* engineering tasks;
* repository documentation;
* engineering architecture;
* engineering testing;
* engineering verification;
* engineering release readiness;
* repository-local risks.

Execution repositories remain authoritative for engineering execution.

A workspace may reuse this workflow without joining the FLEY organizational
surface. When a top-level sibling workspace contains `.fleyignore`, broad FLEY
workspace discovery must treat it as outside the observation boundary: do not
inventory it, report its name or state, count it as drift, or route its work.
The marker does not prevent access by an explicitly targeted command; such
access requires separate authorization from the workspace owner.

---

## Organization

`fley-org` owns:

* organization topology;
* portfolio coordination;
* publication registries;
* organizational planning;
* organizational reconciliation;
* enterprise coordination;
* cross-repository governance.

Organization processes coordinate repositories.

They do not replace repository execution.

---

## Quality Management

`fley-qms` owns controlled governance including:

* SOPs;
* Work Instructions;
* Design Control;
* Change Control;
* CAPA;
* Management Review;
* Document Control;
* Risk and Opportunity Management;
* Quality Planning;
* controlled records.

The QMS should impose governance obligations through the repository workflow
rather than redefine repository engineering execution outside that workflow.

---

## Authority Principle

Repository execution should remain authoritative for engineering work.

Organization workflows should remain authoritative for organizational
coordination.

The QMS should remain authoritative for controlled governance.

Engineering capability should exist independently of governance obligations.

Higher governance layers should compose engineering capabilities rather than
replace them.

---

## Layered Architecture

The FLEY workflow intentionally separates engineering execution,
organizational coordination, and governance.

```text
Engineering Execution
        ↓
Operational Telemetry
        ↓
Organizational Coordination
        ↓
Management Review
        ↓
Governance Decisions
        ↓
Engineering Execution
```

Engineering work continuously informs governance.

Governance continuously improves engineering.

Neither layer duplicates the responsibilities of another.

---

# Guiding Principles

Repository workflows should be:

* durable;
* repeatable;
* deterministic where practical;
* reviewable;
* repository-owned;
* technology-neutral;
* automation-friendly;
* minimally prescriptive;
* suitable for long-term maintenance.

Engineering knowledge should accumulate in repository artifacts rather than
conversation history whenever practical.

Repository workflows define engineering capability.

Governance defines engineering obligations.

The workflow controls operational execution.

The QMS controls governed obligations and approvals through the workflow.
