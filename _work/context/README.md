# Cross-Repository Context Composites

This directory defines local, generated context snapshots for a shared
Pancakes/Pitchfork/Honk/Red Witch ChatGPT project.

## Authority

`composites.yml` is the Pancakes-owned packaging allowlist. It does not make
Pancakes authoritative for sibling-repository content. Each source remains
authoritative in the repository named in its source marker. Generated
composites are non-authoritative and are ignored by Git.

## Commands

```sh
make list-composites
make composites
make check-composites
make clean-composites
make test-composites
```

Repository roots default to the sibling layout declared in the registry. To
override one or more roots:

```sh
make composites \
  COMPOSITE_ROOT_ARGS='--repo-root pitchfork=/path/to/pitchfork --repo-root honk=/path/to/honk'
```

The generated upload set is:

```text
_work/context/generated/context-index.md
_work/context/generated/pancakes-context.md
_work/context/generated/pitchfork-context.md
_work/context/generated/honk-context.md
_work/context/generated/redwitch-context.md
```

The Pancakes composite includes the human-facing recipes, grimoires, goods,
services, common-good, stewardship, and commonwealth models. The Pitchfork
composite includes their substrate counterparts: recipes and grimoires,
questing, and the Sneeds extensibility test. Draft labels from source documents
remain visible and do not gain authority through inclusion.

## Update Procedure

1. Change only reviewed entries in `composites.yml`.
2. Update `source-inventory.csv` with the inclusion or omission rationale.
3. Run `make test-composites`.
4. Run `make composites`.
5. Run `make check-composites` and `make check-work`.
6. Read `context-index.md`, including repository revisions, dirty-state
   warnings, sizes, and review flags.
7. Inspect all generated files for secrets, private user data, raw private
   records, and inappropriate health-related disclosure.
8. Replace all five ChatGPT project files as one snapshot, in index order.

Never upload only part of a newly generated snapshot. A dirty repository is
recorded in the output and requires deliberate review before upload.

## Selection Policy

Membership is explicit. The assembler never scans for additional files.
Sources must be tracked regular UTF-8 files, remain inside their declared
repository after symlink resolution, and carry `reviewed: true`.

`public` means the source is intended for public disclosure.
`private-review-required` means inclusion is intentional but the generated
content still requires manual disclosure review before external upload.

Archived drafts, transcripts, workflow logs, operational notes, databases,
media, ignored files, and untracked files are excluded by default.
