# 0001 - Pancakes Public Surfaces

## Goal

Define and prepare accurate public surfaces for `www.pancakes.ca`,
`docs.pancakes.ca`, and `pancakes.love`, with `pancakes.ca` reserved as a
redirect to the canonical `www` homepage. Each content-bearing host must
clearly communicate its distinct role in the Pancakes ecosystem.

## Authority And Related Work

The `pancakes` repository is authoritative for Pancakes product identity,
architecture, public messaging, and website content.

Related execution plan:

- `site-ops/_work/plans/0011-product-site-deployment.md`

`site-ops` is authoritative for domain, hosting, deployment, redirect, backup,
TLS, and live-site verification. Claims requiring controlled privacy, health,
safety, compliance, or regulatory review must be routed into the applicable
`fley-qms` workflow before publication.

## Product-Surface Decision

Current Pancakes architecture assigns distinct roles:

- `www.pancakes.ca`: NFS-hosted static deployment and primary public
  explanation of Pancakes
- `pancakes.ca`: redirect only, with a permanent HTTPS redirect to
  `https://www.pancakes.ca/`
- `docs.pancakes.ca`: GitHub Pages documentation published from `pancakes/docs/`
- `pancakes.love`: experimental, cooperative, and future
  blockchain-connected environment

This follows the established Red Witch hosting pattern: the `www` hostname is
the NFS-hosted homepage, the bare apex redirects to `www`, and the `docs`
hostname is served separately by GitHub Pages. `www.pancakes.ca` and
`pancakes.love` should not be treated as interchangeable placeholders or
redirected to one another. Initial sites may be small, but they must explain
the distinction and avoid promising unavailable functionality.

## Scope

In scope:

- define the audience and purpose of each domain
- establish public-safe product messaging
- create source-controlled static site content for both domains
- define navigation and links between the two domains and relevant repositories
- define `pancakes.ca` as an apex redirect rather than a content source
- link the static sites to the canonical `docs.pancakes.ca` documentation
- clearly label current, experimental, and future capabilities
- route public claims requiring controlled review
- provide deployment-ready source to `site-ops`

Out of scope:

- production deployment, DNS, TLS, redirects, or live-root backups
- launching a stable hosted application before it is ready
- presenting experimental concepts as released functionality
- publishing private design inputs, user data, or operational details
- bypassing QMS review where required

## Proposed Source Shape

```text
sites/
    pancakes.ca/
        index.html
        styles.css
        robots.txt
    pancakes.love/
        index.html
        styles.css
        robots.txt
```

The existing `sites/pancakes.ca/` directory remains the product-owned source
name; Site Ops must deploy it to `/home/public/www.pancakes.ca/`. The source
directory name does not make the apex hostname canonical.

Shared assets may be introduced only when they reduce meaningful duplication
without coupling the sites so tightly that their distinct roles become unclear.

## Work Plan

1. Define the public story.

   Extract a concise, accurate product explanation from current Pancakes
   product documents. Define what is current, incubating, experimental, or
   future.

2. Define `www.pancakes.ca` and the apex redirect.

   Prepare the stable public landing page: what Pancakes is, its humane and
   local-first principles, current project state, documentation routes, and
   links to related FLEY work. Specify `www.pancakes.ca` as its canonical URL
   and route replacement of the current `pancakes.ca` content deployment with
   a permanent redirect to `https://www.pancakes.ca/` through `site-ops`.

3. Define `pancakes.love`.

   Prepare a distinct experimental/cooperative landing page that explains its
   relationship to Pancakes and avoids implying that speculative or
   blockchain-connected capabilities are already available.

4. Review sensitive claims.

   Identify public claims involving wellness, health, privacy, safety,
   governance, financial/accounting behavior, or compliance. Route controlled
   review needs to `fley-qms` before publication.

5. Build deployment-ready static sources.

   Create minimal, accessible, responsive static sites with intentional
   metadata, links, and robots behavior.

6. Hand off deployment requirements.

   Provide `site-ops` with the source path, the
   `/home/public/www.pancakes.ca/` NFS target, the separate apex redirect root,
   expected canonical hostnames, DNS changes, rollback requirements, and a
   verification checklist.

7. Verify public distinction.

   Confirm that a visitor can understand the purpose and maturity of each
   domain without reading internal product documents.

## Acceptance Criteria

- `www.pancakes.ca` and `pancakes.love` have explicitly distinct public roles
- `pancakes.ca` permanently redirects to `https://www.pancakes.ca/` and does
  not serve an independent homepage
- `docs.pancakes.ca` publishes documentation from `pancakes/docs/`
- both sites have source-controlled deployment-ready content
- current, experimental, and future capabilities are clearly distinguished
- public claims are reviewed or routed appropriately
- the sites link to the correct product and organization sources
- `site-ops` has the information required to deploy and verify both domains
- neither domain remains a meaningless placeholder after deployment

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

## Status

Ready.

Plan `0008-public-repository-docs-and-boundary-transition` is related but does
not supersede this plan. This plan owns the distinct product roles and static
content for `www.pancakes.ca` and `pancakes.love`, plus the required
`pancakes.ca` redirect; Plan 0008 owns the repository boundary,
public-repository transition, and `docs.pancakes.ca` coordination.
