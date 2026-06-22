# 0008 Pancakes Public Repository, Documentation, And Boundary Transition

## Status

Ready.

## Goal

Make `pancakes` a safe public product and node repository, establish
`docs.pancakes.ca` as its GitHub Pages documentation surface, implement the
decided Pancakes/Pitchfork/client repository boundaries, and coordinate the
related GitHub ownership, DNS, and existing-site changes through their
authoritative repositories.

This plan complements Pancakes Plan `0001-public-surfaces`; it does not
supersede it. Plan 0001 owns the distinction and static content for
`www.pancakes.ca` and `pancakes.love`, plus the `pancakes.ca` apex redirect
decision. This plan owns the repository boundary, public-repository transition,
GitHub Pages documentation, document migration, and cross-repository
coordination.

Pitchfork Plan `0001-pancakes-governance-and-architecture-roadmap` is a
different, repository-local Plan 0001. It contains the earlier candidate
repository model and the unresolved `repo-boundaries.md` initiative that this
plan must reconcile. This Pancakes plan does not change the Pitchfork plan's
workflow status; Pitchfork must update, replace, or close its own plan.

## Decision Baseline

The working repository model is:

```text
pancakes
  Pancakes node application and physical persistence
  ecosystem and product governance
  Pancakes architecture and public documentation
  no standalone product clients

pitchfork
  reusable node-runtime substrate
  phone-capable virtual-node substrate
  domain contracts, accounting, settlement, resource state, and projections
  database-independent persistence interfaces

clients
  separate repositories for Red Witch, Wellness Notebook, Honk, and future apps

limited exceptions
  small test, demonstration, or diagnostic clients may live with the component
  they exercise, such as a Flask mood-ring ambience tester
```

An exception must remain subordinate to the host repository's purpose. It must
not become a standalone product application by incremental expansion.

The intended public web estate is:

```text
www.redwitch.ca    static product site
redwitch.ca        redirect to www.redwitch.ca
docs.redwitch.ca   GitHub Pages documentation
www.pancakes.ca    NFS-hosted static product site
pancakes.ca        redirect to www.pancakes.ca
docs.pancakes.ca   GitHub Pages documentation from pancakes/docs
pancakes.love      static experimental site
```

## Authority And Cross-Repository Work

Pancakes owns its product identity, node architecture, governance, public
documentation source, and repository-local file organization.

Related work must be routed rather than duplicated:

- `pitchfork` owns Pitchfork code, contracts, accounting and settlement
  semantics, resource-state transitions, projection derivation, and its own
  document dispositions;
- `site-ops` owns GitHub organization operations, repository transfers, Pages
  platform configuration, DNS, TLS, deployment, redirects, and live-site
  verification;
- `fley-org` owns repository topology, organization-level authority records,
  project relationships, and public-surface governance;
- `fley-qms` owns controlled privacy, health, safety, compliance, regulatory,
  and formal change-control review when applicable.

Relevant existing plans include Pitchfork `0001-pancakes-governance-and-
architecture-roadmap`, Site Ops `0010-github-organization-presence` and
`0011-product-site-deployment`, and Fley Org `0004-peer-project-content-
migration` and `0009-public-surface-governance`.

## Publication Decisions

### Pancakes

The intended outcome is a public `pancakes` repository. Publication is not
authorized until the public-readiness gate in this plan passes. A public Git
repository exposes every reachable committed object and its history, not only
the files rendered by GitHub Pages.

### Pitchfork

Pitchfork does not need to become public for Pancakes or
`docs.pancakes.ca` to launch. Keep Pitchfork private during this transition
unless a separate Pitchfork public-readiness review establishes:

- a clear public purpose and audience;
- acceptable licensing, contribution, support, and security policies;
- no secrets, private data, unsuitable historical content, or third-party
  licensing conflicts in its tree or history;
- stable enough public contracts that publication will not misrepresent the
  implementation;
- explicit approval to change visibility.

This is a decision gate, not a presumption that Pitchfork should remain private
indefinitely.

## GitHub Ownership Transfer Decision

The target owner for active FLEY product repositories is
`Floating-Eye-Software`, subject to organization-level classification and
explicit approval for each transfer.

For `pancakes`, the preferred sequence is:

1. stabilize the repository boundary and complete the public-readiness audit;
2. prepare organization teams, administrator access, repository metadata,
   licensing, security policy, branch protection, Actions permissions, and
   required secrets or environments without copying private values into the
   repository;
3. approve the visibility change and ownership transfer as explicit external
   actions;
4. transfer `mlehotay/pancakes` to `Floating-Eye-Software/pancakes` before the
   final Pages custom-domain and DNS cutover;
5. update local remotes, badges, source links, API integrations, webhooks,
   deploy keys, Pages settings, and organization presentation;
6. configure and verify `docs.pancakes.ca` against the final organization-owned
   repository;
7. verify GitHub redirects from the former repository URL and retain them as a
   compatibility aid rather than the canonical address.

Transferring before the final Pages/DNS cutover avoids building the permanent
documentation configuration around a temporary personal-owner URL. If
organization permissions or policy are not ready, publication may be delayed;
the plan should not create a temporary public Pages surface that must be
immediately reworked.

Red Witch is already organization-owned and should remain the reference case
for `docs.redwitch.ca`. Pitchfork transfer and visibility are separate gates:
ownership may be transferred while private, but only after its authority,
administrative access, integrations, and repository classification are ready.

## Scope

In scope for Pancakes:

- publish a controlling repository-boundaries document;
- inventory Pancakes and Pitchfork documents and record a disposition for each
  boundary-relevant candidate;
- perform Pancakes-owned moves, splits, link repairs, and archival decisions;
- route Pitchfork-owned moves to a Pitchfork plan or todo;
- organize `docs/` as the GitHub Pages source for `docs.pancakes.ca`;
- move the approved public playlist material from `playlist/` into the Pages
  documentation tree;
- move approved Pancakes Corner material from `pancakes-corner/` into the
  Pages documentation tree, with provenance and data-dictionary context;
- add navigation, metadata, accessibility, canonical URL, and custom-domain
  source files needed by the Pages site;
- prepare updated content and links for `www.pancakes.ca`, `pancakes.love`, and
  the relevant Red Witch static surface;
- route replacement of the current `pancakes.ca` content deployment with a
  permanent redirect to `https://www.pancakes.ca/`;
- prepare handoffs for repository visibility, transfer, Pages, DNS, TLS, and
  live verification;
- reconcile organization registries and public-surface records through
  `fley-org`.

Out of scope for Pancakes-local execution:

- changing GitHub visibility or transferring repositories without explicit
  approval;
- changing DNS, Pages repository settings, TLS, or production hosting;
- directly editing Pitchfork, Site Ops, Fley Org, or Red Witch under this
  repository's dashboard;
- publishing private working notes, raw personal records, credentials, local
  media, unlicensed material, or unsupported public claims;
- treating a file move as sufficient removal when sensitive material remains
  in Git history.

## Work Plan

### 1. Baseline The Boundary

Create the controlling repository-boundaries document and reconcile it with
Pancakes plans `0006` and `0007`, Pitchfork plans `0001` and `0003`, repository
instructions, and organization registries. Define the limited embedded-client
exception and criteria for extracting an exception into a separate repository.

### 2. Audit Pancakes For Public Release

Audit the tracked tree, reachable Git history, branches and tags, large files,
ignored-file assumptions, commit metadata, licenses, third-party assets,
copyright, private or health-adjacent records, credentials, operational data,
generated files, and obsolete application material.

Record each finding and its disposition. Rotate exposed credentials regardless
of whether history is rewritten. If history rewriting is necessary, plan it as
a separately approved coordinated operation before transfer or publication.

The audit must explicitly review `apps/legacy-auth-webapp/`, `_work/`, PDFs,
images, datasets, playlist artifacts, and any file whose harmlessness depends
only on `.gitignore`.

### 3. Inventory And Reconcile Documents

Build a manifest with `retain`, `move`, `split`, `archive`, or `retire` for
boundary-relevant documents in both repositories.

The initial high-confidence moves placed Pitchfork contract documents in
Pitchfork; placed Pancakes recipes, grimoires, charter, node architecture, node
infrastructure, service exchange, and non-exploitative-infrastructure documents
in Pancakes; and placed the embodied-AI draft in Pancakes design inputs. The
Pancakes roadmap and exploratory ecosystem design are also design inputs, while
the Wellness Notebook proposal is an organization-level nursery artifact.
Pancakes also owns the top-level mentor and guide materials and the former
Pitchfork reference inputs used for Pancakes design.

Pitchfork and Pancakes draft archives, the export inventory, legacy
carry-forward notes, RPG and roguelike documents, and documents requiring a
split or further review remain in place pending later decisions.

Do not move a file solely because of its filename. Classify the decisions and
semantics it governs, preserve useful history, repair inbound and outbound
links, and leave a pointer when readers are likely to use the old path.

### 4. Build The GitHub Pages Source

Define `pancakes/docs/` as the intended Pages source. Add a clear landing page
and navigation that distinguishes product documentation, governance,
architecture, cultural material, and public datasets.

Relocate approved material to stable paths such as:

```text
docs/
  index.md
  CNAME
  architecture/
  governance/
  playlist/
  pancakes-corner/
```

The final taxonomy may differ after the document inventory. Preserve relative
links or replace them systematically, and verify every published route. The
Pancakes Corner dataset needs a public-purpose statement, schema/data
dictionary, provenance, license, and privacy review before publication.

### 5. Prepare Existing-Site Updates

Update the Pancakes-owned static sources so:

- `www.pancakes.ca` is the stable product landing page and links prominently to
  `docs.pancakes.ca`;
- `pancakes.ca` is a redirect-only apex that permanently redirects to
  `https://www.pancakes.ca/`;
- `pancakes.love` remains the experimental and cultural surface and points to
  the canonical playlist documentation;
- repository and client descriptions reflect the decided boundary;
- no site implies that planned clients or node capabilities are released.

Prepare a content handoff for the Red Witch static site so it uses the same
ecosystem language and links consistently to its own documentation and, where
appropriate, Pancakes documentation. Red Witch source changes belong in its
own repository and deployment belongs in Site Ops.

### 6. Route Platform And Organization Work

Provide Site Ops with an actionable handoff covering:

- current and target GitHub owners;
- visibility and transfer approval gates;
- final Pages source branch and directory;
- `docs.pancakes.ca` custom-domain configuration and DNS record;
- the `www.pancakes.ca` NFS static-site target and canonical URL;
- migration of the current `pancakes.ca` NFS content root to a separate
  apex-to-`www` redirect root, with backup and rollback;
- HTTPS enforcement, certificate readiness, redirects, rollback, and live
  verification;
- repository descriptions, topics, homepage URLs, organization profile, and
  pinning decisions;
- updates required for the three existing static sites.

Provide Fley Org with repository-topology, project-relationship, portfolio, and
public-surface changes. Provide Pitchfork with its document-migration actions
and separate transfer/publication decisions.

### 7. Execute Only After Gates Pass

After explicit approval, the owning repositories may execute file moves,
visibility changes, transfers, GitHub settings, DNS, and deployments in the
dependency order defined here. External mutations are not implied merely by
approval of this planning document.

### 8. Verify The Transition

Verify local document links, Pages build output, custom-domain source,
copyright and data notices, repository URLs, GitHub redirects, organization
access, branch protection, Actions, static-site links, DNS, HTTPS, canonical
URLs, robots behavior, and mobile/desktop accessibility.

## Execution Gates

### Gate A — Boundary Approved

- controlling boundary document agrees with active implementation plans;
- every candidate document has an owner and disposition;
- cross-repository tasks exist in their owning workflow surfaces.

### Gate B — Pancakes Public-Ready

- tree and history audit is complete with no unresolved high-risk findings;
- licensing and third-party content are suitable for publication;
- private data, secrets, and unsupported claims are absent or remediated;
- public README, license, security/contact information, and repository metadata
  are ready;
- the user explicitly approves the visibility change.

### Gate C — Organization Transfer-Ready

- `Floating-Eye-Software` teams and administrator continuity are confirmed;
- integrations, Pages behavior, Actions permissions, secrets, environments,
  branch protection, and rollback steps are inventoried;
- organization and Site Ops records identify the repository as a transfer;
- the user explicitly approves the transfer.

### Gate D — Pages And DNS Ready

- the Pages source builds successfully at the final repository location;
- the custom-domain file and DNS target agree;
- DNS and TLS changes have rollback and verification instructions;
- existing static sites are ready to link to the new canonical docs surface.
- `www.pancakes.ca` is ready as the canonical NFS-hosted homepage and the
  `pancakes.ca` apex redirect has a verified rollback plan.

### Gate E — Pitchfork Publication Decision

- Pitchfork completes its own public-readiness and licensing review;
- its public purpose and maturity are accurately represented;
- transfer and visibility decisions are independently approved.

Gate E does not block Pancakes publication.

## Acceptance Criteria

- the controlling repository-boundaries document reflects the decided model;
- Pancakes and Pitchfork document candidates have recorded dispositions and
  approved moves are completed in the owning repositories;
- Pancakes has passed its full-tree and Git-history public-readiness audit;
- the repository is transferred and made public only after explicit approvals;
- `docs.pancakes.ca` serves the verified GitHub Pages source from the final
  organization-owned Pancakes repository;
- `www.pancakes.ca` serves the canonical NFS-hosted Pancakes homepage and
  `pancakes.ca` permanently redirects to it without serving separate content;
- approved playlist and Pancakes Corner material is navigable, licensed,
  provenance-aware, and free of private material;
- `www.pancakes.ca`, `pancakes.love`, and relevant Red Witch content link to
  the correct canonical documentation and use consistent ecosystem language;
- Site Ops verifies DNS, HTTPS, redirects, repository settings, Pages, and
  live-site behavior;
- Fley Org topology and public-surface records match the resulting state;
- Pitchfork visibility remains unchanged unless its independent gate and
  explicit approval are satisfied.

## Verification Of Effectiveness

Use this section near closure.

Objectives achieved:

- TBD

Evidence:

- TBD

Residual risks:

- TBD

Follow-on actions:

- TBD

Lessons learned:

- TBD
