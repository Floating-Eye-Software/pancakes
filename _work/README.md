# Pancakes Work Area

This directory contains maintainer-facing plans, design inputs, workflow
dashboards, and Codex session records for Pancakes.

## Authority

Pancakes owns its product identity, architecture, design documents, public
messaging, and implementation. Deployment operations belong in `site-ops`;
organization-level coordination belongs in `fley-org`; controlled procedures
and reviews belong in `fley-qms`.

## Workflow Files

- `repo-workflow.md` is the point-of-work copy of the canonical FLEY workflow.
- `plans/plans.csv` tracks multi-step Pancakes work fronts.
- `plans/*.md` contains plan scope, constraints, and acceptance criteria.
- `todo.csv` tracks executable tasks.
- `todo.md` provides expanded task context when needed.
- `codex-log.md` records concise, durable Codex session findings.
- `design-inputs/` contains research and source material used during design.

## Verification

Run:

```sh
make check-work
```

This validates the workflow dashboards, workflow-copy drift, and document
whitespace.
