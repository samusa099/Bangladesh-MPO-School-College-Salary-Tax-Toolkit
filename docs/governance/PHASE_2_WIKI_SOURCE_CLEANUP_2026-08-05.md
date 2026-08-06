# Phase 2 Wiki Source Cleanup — 2026-08-05

## Purpose

This cleanup removes generated, temporary, or status-only pages from the duplicate `docs/wiki/` area and confirms that the project uses root-level `wiki/` as the authoritative GitHub Wiki source.

## Why this was needed

The repository had two wiki-like locations:

```text
docs/wiki/
wiki/
```

The current repository structure and publishing workflow use:

```text
wiki/
```

Therefore, `docs/wiki/` must not be treated as a second source of truth.

## Files removed in this phase

The following generated/status pages were removed from `docs/wiki/`:

- `Docs-Ready.md`
- `Wiki-Status.md`
- `Project-Wiki.md`
- `Wiki-Generated.md`
- `Wiki-Merge-Note.md`
- `Wiki-PR-Summary.md`
- `Branch-Summary.md`
- `Current-Status.md`
- `Prepared-Files.md`
- `Documentation-Only-Notice.md`
- `Review-Summary.md`

These pages were operational notes from earlier generation or PR work. They are not durable project documentation.

## Authoritative source rule

Use only:

```text
wiki/
```

for GitHub Wiki source pages.

Use:

```text
docs/governance/
docs/research/
docs/user-guides/
```

for normal repository documentation.

## Remaining check

If any `docs/wiki/` files remain, they should either be:

1. moved to root `wiki/`, if they are real user-facing wiki pages; or
2. moved to `docs/governance/`, `docs/research/`, or `docs/user-guides/`, if they are not wiki pages; or
3. deleted, if they are generated/noise files.

## Preventive rule

Future generated wiki packages must not be committed into `docs/wiki/`. They must target root `wiki/` only.
