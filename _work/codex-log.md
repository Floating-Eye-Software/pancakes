# Pancakes Codex Log

Concise append-only summaries for Codex sessions.

---

# codex-001 - Design And Governance Documentation Wrapup

**Plan:** repository workflow adoption and documentation capture
**Priority:** P1
**Status:** recorded
**Timestamp:** 2026-06-10 EDT

## Changes

- Captured new flourishing, ecosystem, ethics, and network design documents.
- Captured LifeMaxing design analysis and its source PDFs.
- Added public-surface and ethics-governance plans with executable dashboard
  entries.
- Organized Daily Session design screens under `design-inputs/ds-screens/`.
- Removed obsolete generated inventory and Pitchfork client API input files.
- Adopted the canonical FLEY repository workflow and local validation targets.

---

# codex-002 - User Profiles And Pancakes Corner Capture

**Plan:** user archetypes, node appliance research, Pancakes Corner source data,
and node ambience planning
**Priority:** P1
**Status:** recorded
**Timestamp:** 2026-06-17 EDT

## Changes

- Captured Pancakes user profiles, fictional user-study artifacts, and related
  profile images under `users/`.
- Captured Pancakes Corner taxonomy data, fact-checked dataset material, and
  data dictionary under `_work/pancakes-corner/`.
- Captured source notes for pancake-cultural-history and governance-tree
  context under `_work/notes/`.
- Added the node ambience event plan and dashboard row for future Pancakes node
  event settlement, resource-state, and projection work.

---

# codex-003 - Commons Governance And Playlist Capture

**Plan:** commons governance documentation, political characterization notes,
and playlist artifact capture
**Priority:** P1
**Status:** recorded
**Timestamp:** 2026-06-17 EDT

## Changes

- Captured Pancakes/Pitchfork political characterization, commons-problem, and
  Ostrom alignment notes under `_work/politics/`.
- Added the Pancakes Ostrom Governance Model as a foundational governance
  guidance document.
- Captured Fatima's glowing brooch wearable-node idea under `_work/notes/`.
- Added a cleaned top-level `playlist/` artifact with MP3 files, M3U ordering,
  and Billy Bragg transcript/analysis notes.
- Updated the local workflow copy to point at the current `fley-org/process/`
  canonical workflow paths.

---

# codex-004 - Persona Deck And Copyright-Safe Playlist

**Plan:** persona artifact organization and playlist rights hygiene
**Priority:** P1
**Status:** recorded
**Timestamp:** 2026-06-18 EDT

## Changes

- Moved Pancakes persona imagery and profile documents from `users/` into the
  `personas/` structure, including non-canon assets.
- Added the Pancakes character canon and persona deck as committed persona
  reference material.
- Converted the playlist reference into a copyright-compliant committed
  playlist with listening and lyrics lookup links instead of committed lyrics.
- Added playlist ignore rules so local MP3 files and the private lyrics working
  file stay out of version control.
- Removed previously tracked playlist MP3 files from the repository while
  keeping the local playlist ordering in `playlist/pancakes.m3u`.

---

# codex-005 - Playlist Good Girls Removal

**Plan:** playlist maintenance
**Priority:** P2
**Status:** recorded
**Timestamp:** 2026-06-18 EDT

## Changes

- Removed Josie Edwards "Good Girls" from the committed playlist reference,
  liner notes, and M3U ordering.
- Renumbered the remaining playlist entries 11-13 across committed references.
- Renumbered the local ignored audio filenames and private lyrics working file
  so `playlist/` remains internally consistent.

---

# codex-006 - YouTube Playlist Sync

**Plan:** playlist maintenance
**Priority:** P2
**Status:** recorded
**Timestamp:** 2026-06-18 EDT

## Changes

- Synced the committed playlist reference to the public YouTube playlist order.
- Added Cake "I Will Survive" at track 09 using the official HD video entry.
- Renumbered downstream liner notes, M3U entries, local ignored audio filenames,
  and the Neath the Grove analysis filename to keep playlist numbering aligned.

---

# codex-007 - Rehab Playlist Insertion

**Plan:** playlist maintenance
**Priority:** P2
**Status:** recorded
**Timestamp:** 2026-06-18 EDT

## Changes

- Synced the playlist order to the public YouTube playlist after Amy Winehouse
  "Rehab" was inserted after "Institutionalized."
- Added Rehab as track 07 in the committed playlist reference and liner notes.
- Renumbered downstream M3U entries, local ignored audio filenames, and
  playlist analysis filenames to keep track numbering aligned.

---

# codex-008 - Playlist Presentation And Persona Causes

**Plan:** playlist and persona reference development
**Priority:** P2
**Status:** recorded
**Timestamp:** 2026-06-18 EDT

## Changes

- Added the Pancakes playlist cover, track dates, navigation links, canonical
  M3U filename, and links between the playlist, liner notes, and song analyses.
- Expanded the Billy Bragg transcript formatting and the Deceptacon analysis,
  including interpretive context and source links.
- Added the Pancakes Persona Causes document, assigning every current playlist
  track to one primary persona as a motivating cause and developing concrete
  persona priorities without creating another mentor or advocate role.
- Added a repository whitespace checker that excludes ignored local artifacts
  while retaining checks for tracked and untracked worktree changes.

---

# codex-009 - Playlist Commercial And Cultural Histories

**Plan:** playlist reference development
**Priority:** P2
**Status:** recorded
**Timestamp:** 2026-06-18 EDT

## Changes

- Added a complete commercial and cultural history companion for all 15 songs
  in the Pancakes playlist.
- Linked every liner-note entry to a stable track anchor in the histories
  document and linked every history section back to its liner notes.
- Added the histories document to the main playlist navigation.

---

# codex-010 - Bread Playlist Coda

**Plan:** playlist maintenance
**Priority:** P2
**Status:** recorded
**Timestamp:** 2026-06-18 EDT

## Changes

- Added Anya Nami "Bread" as official track 16 in the committed playlist
  reference and M3U ordering, linked through the public YouTube playlist.
- Added liner notes and commercial and cultural history framing the song as a
  coda about food, rest, comfort, and ordinary embodied life.
- Updated the preceding tracks' sequence language and assigned Jun as the
  primary user advocate for the "Bread" cause.

---

# codex-011 - Legacy Web App Isolation And Pitchfork Contracts

**Plan:** repository structure and architecture documentation
**Priority:** P2
**Status:** recorded
**Timestamp:** 2026-06-20 EDT

## Changes

- Moved the original Flask authentication and user-profile skeleton into
  `apps/legacy-auth-webapp/` so it remains available without implying that it
  is the current Pancakes node implementation.
- Preserved the legacy deployment staging target, updated the ignored SQLite
  path, and documented how to run the archived application locally.
- Added the proposed Pitchfork contract architecture draft covering contract
  principles, models, lifecycle, governance, settlement, and client boundaries.

---

# codex-012 - Pancakes Node Foundation Split

**Plan:** `0006-node-ambience-event-plan`, `0007-node-foundation`
**Priority:** P1
**Status:** recorded
**Timestamp:** 2026-06-21 02:00 EDT

## Changes

- Added Plan 0007 for the Pancakes-owned Flask, SQLAlchemy, Alembic,
  configuration, transaction, health-check, and SQLite/PostgreSQL foundation.
- Reframed Plan 0006 as product integration work blocked on both the Pitchfork
  Core Foundation and Pancakes Node Foundation.
- Documented the boundary between Pitchfork accounting contracts and
  Pancakes-owned physical persistence and node operations.
- Added an explanatory reader for the draft Pitchfork contract model.

## Verification

- `make check-work`
- `git diff --check`

## Follow-on Work

- Begin Plan 0007 after `pitchfork:0003-core-foundation` supplies stable domain
  and persistence contracts.
- Begin Plan 0006 only after both declared foundations are complete.

---

# codex-013 - Public Repository And Documentation Transition Plan

**Plan:** `0008-public-repository-docs-and-boundary-transition`
**Priority:** P1
**Status:** recorded
**Timestamp:** 2026-06-21 EDT

## Changes

- Added Plan 0008 to coordinate the Pancakes/Pitchfork repository boundary,
  Pancakes public-readiness review, `docs.pancakes.ca`, document migrations,
  existing static-site updates, and authoritative cross-repository handoffs.
- Kept Pancakes Plan 0001 as the distinct `pancakes.ca` and `pancakes.love`
  public-surfaces plan, while adding an ordered set of architecture, security,
  documentation, publication, GitHub, governance, and verification tasks under
  Plan 0008.
- Defined the preferred GitHub transition order: stabilize and audit Pancakes,
  prepare organization access, transfer it to `Floating-Eye-Software`, approve
  public visibility, and configure the final Pages custom domain and DNS.
- Kept Pitchfork publication behind an independent readiness and approval gate;
  it does not block publication of Pancakes or `docs.pancakes.ca`.
- Preserved the Pancakes/Pitchfork planning discussion in
  `_work/pancakes-pitchfork.txt` as a design input for the transition.
- Added a playlist reader, a copyright-conscious social-demands interpretation,
  and navigation from the canonical playlist into the new material.

## Plan-ID Clarification

Pancakes `0001-public-surfaces` and Pitchfork
`0001-pancakes-governance-and-architecture-roadmap` are unrelated plans with
repository-local numeric identifiers. The Pitchfork plan contains the earlier
candidate repository model. Plan 0008 complements the Pancakes public-surfaces
plan and reconciles the boundary initiative from the Pitchfork roadmap; it does
not supersede Pancakes Plan 0001 or alter Pitchfork workflow state.

## Verification

- `make check-work`
- `git diff --check`

## Follow-on Work

- Begin with todo-003 to baseline the controlling repository boundary.
- Do not change repository visibility, ownership, Pages settings, DNS, or
  Pitchfork visibility until the applicable plan gates and explicit approvals
  are satisfied.

---

# codex-014 - Economic And Network Theory Document Migration

**Plan:** `0008-public-repository-docs-and-boundary-transition`
**Priority:** P1
**Status:** recorded
**Timestamp:** 2026-06-21 EDT

## Changes

- Moved the Pancakes/Pitchfork economic-theory synthesis from Pitchfork into
  Pancakes because it governs ecosystem philosophy, co-production, and
  institutional design rather than Pitchfork contract semantics.
- Added the Pancakes Srinivasan Network Model as a companion to the Ostrom
  Governance Model, adapting network-state formation ideas without adopting
  diplomatic sovereignty, token governance, public life ledgers, or
  exit-only remedies.
- Added a Pancakes documentation index and repaired the migrated documents'
  links to authoritative Pancakes-owned material.
- Included `_work/why-do-you-forget.png` at the user's explicit request.

## Verification

- `make check-work`
- `git diff --check`
- internal Markdown link check for the new and migrated documents

---

# codex-015 - Pancakes And Pitchfork Content Boundary Cleanup

**Plan:** `0008-public-repository-docs-and-boundary-transition`
**Priority:** P1
**Status:** recorded
**Timestamp:** 2026-06-21 EDT

## Changes

- Moved Pancakes-owned recipes, grimoires, charter, node architecture, node
  infrastructure, service exchange, and non-exploitative-infrastructure
  documents from Pitchfork into the Pancakes documentation tree.
- Moved Pitchfork contract architecture and its reader from Pancakes into
  Pitchfork, and repaired affected documentation indexes and links.
- Moved the Pancakes roadmap, exploratory ecosystem design, embodied-AI input,
  and former Pitchfork reference PDFs into Pancakes design inputs.
- Moved HRV, sensor, and medical-device guidance PDFs out of public docs into
  `_work/notes/hrv/`, and routed the Wellness Notebook proposal to the Fley Org
  project nursery.
- Moved the complete mentor and guide trees from Pitchfork to Pancakes while
  retaining their top-level layouts.
- Moved Pancakes Corner from `_work/` to the repository top level for later
  public-documentation preparation.
- Moved the legacy remote-server staging tree under
  `apps/legacy-auth-webapp/remote-server/`, updated deployment helpers and
  ignore rules, and moved the unexplained governance bundle under `_work/`.
- Included the maintainer-directed removal or relocation of obsolete political
  notes and prior planning transcripts already present in the worktree.

## Verification

- `make check-work`
- `git diff --check`
- moved-file and stale-reference review across Pancakes and Pitchfork

## Follow-on Work

- Complete the remaining document disposition review under Plan 0008.
- Audit public documentation, imagery, datasets, and Git history before making
  the Pancakes repository public.

---

# codex-016 - Pages Content Relocation And Hosting Topology

**Plan:** `0001-public-surfaces`,
`0008-public-repository-docs-and-boundary-transition`
**Priority:** P1
**Status:** recorded
**Timestamp:** 2026-06-21 EDT

## Changes

- Moved the tracked Pancakes playlist and Pancakes Corner trees under
  `docs/playlist/` and `docs/pancakes-corner/` for the planned GitHub Pages
  documentation source.
- Moved the complete local playlist directory, including ignored MP3 files,
  private lyrics, and thumbnails. Those ignored artifacts remain local and
  excluded from Git; only the public-safe tracked playlist material is part of
  the repository transition.
- Corrected the playlist's private-lyrics path after the move.
- Aligned Pancakes Plans 0001 and 0008 with the established Red Witch hosting
  pattern: `www.pancakes.ca` is the canonical NFS-hosted static homepage,
  `pancakes.ca` redirects to `www`, and `docs.pancakes.ca` is published from
  `pancakes/docs/` through GitHub Pages.
- Updated the plan and todo dashboards to preserve the hosting decision and
  route the required NFS, DNS, redirect, Pages, and live-site work to Site Ops.

## Verification

- `make check-work`
- `git diff --check`
- verified that the ignored MP3, lyrics, and thumbnail artifacts remain
  ignored at their new local paths

## Follow-on Work

- Migrate the repository to its approved new location before configuring the
  final GitHub Pages custom domain.
- Complete the public-readiness and document-disposition gates before making
  the new repository public.
- Update the Site Ops public-surface registry and Plan 0011 so
  `sites/pancakes.ca/` deploys to `/home/public/www.pancakes.ca/`, the apex
  becomes a redirect-only root, and `docs.pancakes.ca` is configured and
  verified separately.

---

# codex-017 - Clean Public Git Baseline

**Plan:** `0008-public-repository-docs-and-boundary-transition`
**Priority:** P1
**Status:** recorded
**Timestamp:** 2026-06-21 EDT

## Changes

- Established a new Git history for the organization-owned public repository.
- Kept MP3 files and raw UUID-named conversation exports outside the public
  baseline through repository-level ignore rules.
- Preserved the existing playlist-specific exclusions for private lyrics and
  thumbnails.

## Verification

- `make check-work`
- staged-tree secret-pattern and ignored-file review

## Follow-on Work

- Complete the broader licensing, document-disposition, and public-readiness
  review tracked by Plan 0008 and todo-004.

---

# codex-018 - Canonical Organization Repository Reconciliation

**Plan:** `0008-public-repository-docs-and-boundary-transition`
**Priority:** P1
**Status:** recorded
**Timestamp:** 2026-06-21 EDT

## Changes

- Recorded `https://github.com/Floating-Eye-Software/pancakes` as the canonical
  public repository on `main`.
- Replaced the obsolete personal-repository transfer sequence with the actual
  clean-history replacement outcome.
- Kept the tree, licensing, metadata, document-disposition, Pages, and DNS
  reviews open rather than treating repository creation as plan completion.
- Confirmed the local `origin` already points to the organization repository.

---

# codex-019 - Docs Pages And DNS Cutover

**Plan:** `0008-public-repository-docs-and-boundary-transition`
**Priority:** P1
**Status:** recorded
**Timestamp:** 2026-06-21 EDT

## Changes

Recorded the live `docs.pancakes.ca` GitHub Pages cutover for the public
`Floating-Eye-Software/pancakes` repository. Updated the local todo list so the
Pages source task is marked done; the remaining work stays focused on the
`www.pancakes.ca` and apex redirect path.

---

# codex-020 - Public Static Site Refresh

**Plan:** `0001-public-surfaces`
**Priority:** P1
**Status:** recorded
**Timestamp:** 2026-06-21 EDT

## Changes

- Reworked `sites/pancakes.ca/index.html` into the canonical public home for
  `www.pancakes.ca` with explicit links to `docs.pancakes.ca`, the playlist
  page, the public repository, and the apex redirect note.
- Reworked `sites/pancakes.love/index.html` into a clearly experimental and
  cultural surface that points to the playlist docs and the canonical home.
- Rebuilt both site stylesheets so the pages render as self-contained, distinct
  static sites, and fixed the `pancakes.love` theme class wiring.

---

# codex-021 - Documentation Landing Pages

**Plan:** `0008-public-repository-docs-and-boundary-transition`
**Priority:** P1
**Status:** recorded
**Timestamp:** 2026-06-22 EDT

## Changes

- Added `docs/index.md` as the public documentation root with links to the
  main product, architecture, governance, and human-flourishing material.
- Added `docs/playlist/index.md` as the playlist landing page for the
  overview, commentary, histories, and supporting materials.
- Added `docs/pancakes-corner/index.md` as the dataset landing page for the
  data dictionary and CSV artifacts.

---

# codex-022 - Split-Root Canonical Comment Update

**Plan:** `ad hoc`
**Priority:** P2
**Status:** recorded
**Timestamp:** 2026-06-22 EDT

## Changes

Added a small explanatory comment to the apex redirect root and canonical
`www` page so the Pancakes split-root layout is explicit in source:

- `sites/pancakes.ca/.htaccess` is redirect-only
- `sites/www.pancakes.ca/index.html` is the canonical content page

This documents the server-side topology without changing the page content.

---

# codex-023 - Commonwealth And Goods Model Capture

**Plan:** `0008-public-repository-docs-and-boundary-transition`
**Priority:** P1
**Status:** recorded
**Timestamp:** 2026-06-23 EDT

## Changes

- Added the Pancakes Commonwealth Model as a constitutional synthesis for the
  ecosystem.
- Added the Pancakes Goods and Services Model to frame goods, services, and
  transformations within the humane economy.
- Updated the public docs navigation so the root docs page, playlist page, and
  Pancakes Corner page all link back to the site entry points.

---

# codex-024 - Repository Workflow Sync

**Plan:** `0008-public-repository-docs-and-boundary-transition`
**Priority:** P1
**Status:** recorded
**Timestamp:** 2026-06-26 EDT

## Changes

- Synced `../pancakes/_work/repo-workflow.md` to the current canonical
  `fley-org/process/repo-workflow.md` workflow.
- Verified the local copy with `make -C ../fley-org check-repo-workflow
  REPO_WORKFLOW=../pancakes/_work/repo-workflow.md`.

---

# codex-025 - Pancakes Foundation Documentation

**Plan:** `0009-symbolic-architecture-foundations`
**Priority:** P1
**Status:** review
**Timestamp:** 2026-06-26 EDT

## Changes

- Finalized `docs/pancakes-place-model.md` as the canonical Pancakes place and
  homeland foundation.
- Finalized `docs/pancakes-reference-services.md` as the canonical public
  reference service architecture.
- Finalized `docs/pancakes-node-capabilities.md` as the canonical node
  capability extension model.
- Added `_work/plans/plans.csv` rows for Plan 0009 and downstream Plan 0010,
  with Plan 0010 blocked on Plan 0009 review.
- Kept the Pitchfork symbolic frequency and crafting foundations in the
  Pitchfork repository.

## Verification

- `make check-work`
- `git diff --check`

## Follow-on Work

- Review Plan 0009 before closure.
- Start Plan 0010 application documentation migration after the foundation
  plan is accepted.

---

# codex-026 - Appliance And Place Architecture Expansion

**Plan:** `0009-symbolic-architecture-foundations`
**Priority:** P1
**Status:** review
**Timestamp:** 2026-06-26 EDT

## Changes

- Expanded the node capability, place, and reference-service foundations to
  clarify transformations, place memory, symbolic contribution, public facts,
  privacy, governance, and client boundaries.
- Added `docs/pancakes-appliance-design.md` as a broad architecture proposal
  for node, capture, sensor, memory, projection, and resilience appliances.
- Added `_work/notes/woodland-commons.md` as a reference deployment concept.
- Added `_work/notes/jekyll-notes.md` as troubleshooting notes for the docs
  site.

Changed files:

- `docs/pancakes-node-capabilities.md`
- `docs/pancakes-place-model.md`
- `docs/pancakes-reference-services.md`
- `docs/pancakes-appliance-design.md`
- `_work/notes/woodland-commons.md`
- `_work/notes/jekyll-notes.md`

Plan 0009 remains in review; this entry does not close it.

---

# codex-027 - Cross-Repository Context Composites

**Plan:** `0011-cross-repository-chatgpt-context-composites`
**Priority:** P1
**Status:** done
**Timestamp:** 2026-06-26 EDT

## Changes

- Added a reviewed source inventory and declarative registry for Pancakes,
  Pitchfork, Honk, and Red Witch context.
- Added deterministic multi-repository composite generation with repository
  revisions, dirty-state provenance, path-containment checks, tracked-file
  enforcement, disclosure classifications, size limits, and a 25-file budget.
- Added Make targets for generation, checking, listing, cleanup, and tests.
- Added operating instructions for regeneration, disclosure review, upload
  order, and coherent replacement.
- Ignored generated context snapshots so only the registry, inventory, tooling,
  tests, and documentation are committed.
- Generated a five-file local upload set consisting of one index and four
  repository composites.

## Verification

- `make test-composites` — 17 tests passed.
- `make composites` — five files generated.
- `make check-composites` — generated snapshot current.
- `python3 -m py_compile scripts/assemble_context_composites.py
  tests/test_context_composites.py` — passed.
- Credential-pattern scan found no credential-shaped content.
- `make check-work` — passed.
- `git diff --check` — passed.

## Closure

The user approved Plan 0011 for closure. External upload remains manual.
Regenerate the ignored snapshot after commits that change a source repository
revision, and review every `private-review-required` source before upload.

---

# codex-028 - Context Composite Source Expansion

**Plan:** `0011-cross-repository-chatgpt-context-composites`
**Priority:** P1
**Status:** done
**Timestamp:** 2026-06-26 EDT

## Changes

- Expanded the Pancakes composite from 17 to 23 sources with the common-good,
  stewardship, commonwealth, recipes, grimoires, and goods-and-services
  models. The node-capabilities document was already included.
- Expanded the Pitchfork composite from 16 to 19 sources with recipes and
  grimoires, questing, and the Sneeds extensibility test.
- Updated the reviewed source inventory and context operating documentation.
- Updated the Pancakes documentation README to link the selected economic,
  constitutional, and node-capability documents.
- Coordinated the Pitchfork documentation README update in its authoritative
  repository.

## Verification

- `make test-composites` — 17 tests passed.
- `make composites` — five files generated.
- `make check-composites` — generated snapshot current.
- `make check-work` — passed.
- `make -C ../pitchfork check-work` — passed.
- Credential-pattern scan found no credential-shaped content.
- `git diff --check` passed in Pancakes and Pitchfork.

## Follow-on Work

Replace all five external project files together after reviewing every
`private-review-required` source. The three assessed Red Witch additions remain
excluded pending source curation or a separate external-evidence context.
