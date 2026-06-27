# 0011 Cross-Repository ChatGPT Context Composites

## Status

Done.

## Goal

Create a deterministic, reviewable workflow that packages the important
Pancakes, Pitchfork, Honk, and Red Witch source documents into a small set of
generated Markdown composites suitable for a shared ChatGPT project.

The initial packaging budget is at most 25 uploaded files. The workflow should
normally emit one composite per repository plus a short index, leaving room for
selected standalone files when their independent identity is useful.

## Motivation

The relevant context spans more source files than are practical to maintain as
individual ChatGPT project uploads. Manual copy-and-paste bundles would obscure
provenance, drift as the repositories change, and risk mixing authoritative
source with generated packaging.

`../halfbaked` already implements the useful core pattern:

- `assets/composites.yml` is the declarative membership registry;
- `make composites` performs ordered, concatenation-only assembly;
- generated files identify their source documents and carry a non-authoritative
  notice;
- `make check-composites` detects stale outputs;
- list, clean, and ad hoc operations are separate;
- writes are atomic and missing, duplicate, non-UTF-8, or invalid inputs fail
  before successful completion.

Pancakes should adapt that pattern rather than copy it unchanged. Halfbaked's
assembler deliberately accepts only paths below one repository root, while
this workflow needs four named sibling repositories and stronger provenance
and disclosure controls.

## Authority And Ownership

This plan governs only Pancakes-local context packaging and its generated
artifacts. It does not transfer or redefine authority:

- `pancakes` owns Pancakes product identity, node architecture, governance,
  public documentation, and this assembly workflow;
- `pitchfork` owns shared contracts, projection semantics, accounting,
  settlement, resource state, and reusable runtime architecture;
- `honk` owns Honk client behavior and documentation;
- `redwitch` owns Red Witch client behavior, product identity, and
  documentation.

Each included source remains authoritative in its owning repository. A
composite is a convenience snapshot, never a new canonical source. Changes
needed in a sibling repository must be planned and made there.

## Scope

In scope:

- inventorying the important context sources in the four repositories;
- defining stable, ordered, allowlisted composite membership;
- implementing deterministic multi-repository Markdown assembly;
- recording source repository, path, and Git revision in generated outputs;
- generating an upload index and a compact set of repository composites;
- checking generated outputs for drift and enforcing the upload-file budget;
- documenting review, regeneration, and ChatGPT project replacement steps.

Out of scope:

- changing source content in Pitchfork, Honk, or Red Witch;
- uploading files to ChatGPT automatically;
- treating generated context as authoritative;
- including credentials, private user data, raw private records, local
  environment files, databases, media, or ignored files;
- using semantic summarization or model-generated rewriting during assembly;
- automatically discovering and including every Markdown file.

## Proposed Design

### Registry

Add a committed Pancakes-owned registry, provisionally:

```text
_work/context/composites.yml
```

It should declare:

- a schema version;
- the generated output directory;
- the upload-file budget;
- named repository roots for `pancakes`, `pitchfork`, `honk`, and `redwitch`;
- composites with stable IDs, output names, notes, and ordered source entries;
- each source as a repository ID plus a path relative to that repository;
- optional classification such as `public`, `private-review-required`, or
  `generated-excluded`.

Repository root locations are local configuration, not portable facts. The
registry may declare expected sibling directory names, while Make variables or
command-line options provide overrides. Absolute workstation paths must not be
committed.

### Outputs

Generate local artifacts under a dedicated directory such as:

```text
_work/context/generated/
  context-index.md
  pancakes-context.md
  pitchfork-context.md
  honk-context.md
  redwitch-context.md
```

The directory must be excluded from Git unless a later review establishes a
specific reason to version generated snapshots. The index should state the
generation time, registry version, repository revisions, dirty-worktree
warnings, output sizes, source counts, and upload order.

Each repository composite should contain:

- a generated/non-authoritative notice;
- repository name and captured Git revision;
- an ordered source manifest;
- explicit begin and end markers around each source;
- the complete source text, normalized only for line endings and final newline.

Source paths in headers should remain repository-qualified, for example
`pitchfork:docs/contracts.md`, so similarly named files cannot be confused.

### Commands

Add Make targets consistent with Halfbaked's interface:

```text
make composites
make check-composites
make list-composites
make clean-composites
```

Pancakes may also provide a narrower validation command for the registry, but
ad hoc cross-repository assembly is not required initially. Stable ChatGPT
project context should use registered composites.

### Safety And Validation

The assembler must:

- accept only known repository IDs and repository-relative source paths;
- reject absolute paths and `..` traversal;
- resolve symlinks and verify every source remains below its declared
  repository root;
- require regular UTF-8 text files;
- reject missing and duplicate inputs and duplicate output names;
- write only below the configured generated-output directory;
- reject outputs that collide with source files;
- avoid reading ignored or untracked files unless a source has been explicitly
  classified and approved;
- warn or fail, according to documented policy, when a repository is dirty;
- record the Git commit for every source repository;
- generate into temporary files and replace outputs atomically;
- fail `check-composites` when content, provenance, membership, or the index
  would change;
- fail when the generated upload set exceeds its configured file budget.

Selection is an explicit disclosure decision. Inventory tooling may report
candidates, but only reviewed registry entries may enter an output.

## Work Plan

### 1. Inventory And Classify Sources

Inspect repository instructions and documentation surfaces in all four
repositories. Build a candidate inventory containing repository, path,
authority, purpose, sensitivity, overlap, and proposed disposition.

Classify each candidate as:

- include in its repository composite;
- keep standalone;
- omit as redundant or operational;
- require privacy or disclosure review;
- route to another repository for correction before inclusion.

Start with orientation, architecture, contracts, domain terminology, active
plans that materially affect implementation, and client-specific behavior.
Exclude routine workflow dashboards unless they provide necessary current
state.

### 2. Define The Upload Set

Choose the smallest set that is sufficient for cross-repository work. Default
to the index and four repository composites. Keep a standalone file only when
separate updating, retrieval, or authority is materially better than embedding
it.

Document ordering rationale and intentional omissions. Set a size threshold or
warning policy so the workflow catches a technically valid but impractically
large composite.

### 3. Implement The Registry And Assembler

Adapt the proven Halfbaked structure while replacing its single-root file model
with named roots and repository-qualified sources. Keep assembly mechanical and
deterministic. Do not import Halfbaked's IER-specific headers, scope vocabulary,
or unknown-output filename convention.

Separate registry parsing, path validation, provenance capture, rendering,
checking, and cleanup so each can be tested independently.

### 4. Integrate Make And Local-Artifact Handling

Add the four Make targets, document root overrides, and exclude generated
outputs from Git. Cleaning must remove only outputs declared by the registry;
unknown files should be reported and left untouched.

### 5. Test And Verify

Cover at least:

- deterministic output across two consecutive runs;
- stale-output detection after changing a source;
- missing repository and missing source failures;
- unknown repository ID, absolute path, traversal, and symlink-escape failures;
- duplicate source and output failures;
- invalid UTF-8 rejection;
- dirty-repository provenance behavior;
- unknown generated-file reporting;
- safe, declaration-limited cleanup;
- upload budget and size-policy failures;
- source markers and repository-qualified provenance in every output.

Run `make composites`, `make check-composites`, the focused assembler tests,
and `make check-work`.

### 6. Review And Operating Procedure

Review every generated file before its first upload, with particular attention
to private repositories and health-adjacent or personal content. Document:

1. how to regenerate and check the set;
2. how to inspect revisions and dirty-state warnings;
3. which generated files to upload;
4. how to replace the prior ChatGPT project files as one coherent snapshot;
5. how to record intentional membership changes.

Do not automate external upload without a separate explicit request and review.

## Acceptance Criteria

- A committed registry defines all included sources by repository ID and
  repository-relative path.
- The generated upload set is no more than the configured 25-file budget.
- One command deterministically generates the complete reviewed upload set.
- A check command detects stale content, membership, and provenance.
- Every output identifies its source files and repository revisions and states
  that the sources remain authoritative.
- Path containment, symlink escape, missing input, duplicate input, UTF-8, dirty
  state, output collision, and cleanup behavior are tested.
- Generated composites are not committed and contain no credentials, private
  user data, raw private records, secrets, or unreviewed ignored files.
- The inventory records why important candidates were included, kept
  standalone, omitted, or routed elsewhere.
- Maintainer documentation explains regeneration, review, upload order, and
  coherent replacement of the ChatGPT project snapshot.
- `make check-composites` and `make check-work` pass.

## Risks And Controls

- **Stale external context:** revision metadata, check mode, and coherent
  replacement make staleness visible.
- **Authority confusion:** repository-qualified source markers and generated
  notices preserve ownership.
- **Sensitive disclosure:** explicit allowlists and pre-upload human review are
  mandatory; automatic discovery cannot add content.
- **Path escape across sibling repositories:** named roots, resolved-path
  containment, and symlink tests prevent arbitrary reads.
- **Oversized context:** file-count and size policies fail before upload
  packaging is accepted.
- **Cross-repository drift:** the index captures all four revisions in one
  snapshot and warns about dirty worktrees.
- **Generated-file churn:** only the registry, tooling, tests, and
  documentation are versioned by default.

## Implementation Outcome

Implemented on 2026-06-26:

- `_work/context/composites.yml` defines four repository composites using 54
  reviewed, repository-qualified source entries;
- `_work/context/source-inventory.csv` records inclusion and omission
  rationale;
- `scripts/assemble_context_composites.py` provides deterministic generation,
  checking, listing, and declaration-limited cleanup;
- the Makefile exposes `composites`, `check-composites`, `list-composites`,
  `clean-composites`, and `test-composites`;
- `_work/context/generated/` is ignored and contains the five-file local upload
  set;
- `tests/test_context_composites.py` covers the required safety, drift, budget,
  collision, and cleanup behavior with 17 tests;
- `_work/context/README.md` documents regeneration, review, overrides, upload
  order, and coherent replacement.

The generated set is 652,621 bytes: one index and four composites, within the
25-file and configured size budgets. The Pancakes revision is marked dirty
because implementation changes are uncommitted. Pitchfork, Honk, and Red Witch
were clean during generation. No sibling repository was modified.

## Verification Of Effectiveness

Automated verification changed a tracked fixture source after generation,
confirmed that check mode failed, regenerated the snapshot, and confirmed that
check mode then passed with dirty-state provenance recorded.

Verification completed:

- `make test-composites` — 17 tests passed;
- `make composites` — five files generated;
- `make check-composites` — generated snapshot current;
- `python3 -m py_compile scripts/assemble_context_composites.py
  tests/test_context_composites.py` — passed;
- credential-pattern scan of generated outputs — no credential-shaped content
  found;
- `make check-work` — passed;
- `git diff --check` — passed.

Residual review:

- inspect the generated Red Witch and other `private-review-required` material
  before external upload;
- regenerate after committing because the Pancakes revision and dirty marker
  will change;
- upload or replace all five generated files as one coherent snapshot.

The user approved closure on 2026-06-26. The plan is complete.
