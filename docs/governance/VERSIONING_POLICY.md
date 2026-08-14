# Versioning Policy

## Canonical release identifier

The toolkit uses one public product release identifier across GitHub, Wiki, release notes, manifests and distribution metadata.

For the current public release:

- **Canonical product release:** `v0.1.3`
- **Release status:** Beta
- **Tax Year:** 2026–27
- **Expected Git tag:** `v0.1.3`
- **Expected GitHub Release title:** `Bangladesh MPO School & College Salary Tax Toolkit v0.1.3 Beta`

## Semantic versioning rule

Public releases use semantic-style versions:

`vMAJOR.MINOR.PATCH`

Examples:

`v0.1.3` → `v0.1.4` → `v0.2.0` → `v1.0.0`

Use:

- **PATCH** for backward-compatible fixes, packaging corrections and small workbook refinements;
- **MINOR** for backward-compatible feature additions or meaningful workbook capability expansion;
- **MAJOR** for stable-release breaking changes or a major product contract change.

## Documentation and design revisions

A README, cover, badge, documentation or visual-layout revision is **not** a product release unless the full release process is completed.

The existing `v4.0` identifier is therefore treated only as a **README/design revision**. It must never replace the canonical product release number in the release badge, current-release table, Git tag, GitHub Release, Wiki or Kaggle release metadata.

Recommended wording:

- `Product release: v0.1.3`
- `README design revision: v4.0`

## Git tag and GitHub Release rule

For every published product release:

1. Git tag must exactly equal the canonical version, for example `v0.1.3`.
2. GitHub Release title must contain the same version.
3. Root `README.md`, root `RELEASE_NOTES.md`, `CHANGELOG.md`, root `wiki/`, and release manifests must agree.
4. A release must not use an unrelated ordinal tag such as `v2`.

## Protected legacy tag exception

The historical tag `v2` predates this policy and points to the same commit as `v0.1.3`. The live GitHub Release is no longer attached to `v2`; it is attached to the canonical `v0.1.3` tag.

Repository ruleset **Protect version tags** currently blocks deletion of every `refs/tags/v*` reference and provides no bypass actor. Because of that protection, `v2` is retained only as a **deprecated protected legacy alias** until repository administrators intentionally change the tag-deletion rule.

Rules for this alias:

- it must not be used as a current release identifier;
- it must not be used in README, Wiki, Kaggle or release metadata;
- no GitHub Release should be attached to it;
- future releases must use semantic tags only;
- if tag-protection policy is later changed, `v2` may be removed after confirming `v0.1.3` still points to the same historical release commit.

## Unreleased candidate rule

Files may be prepared for a future version before publication, but they must be explicitly marked **Unreleased** or **Release candidate**.

At the time of this policy, `v0.1.4` material is preparatory and does not supersede the current public release `v0.1.3` until a matching tag and GitHub Release are published.

## Kaggle and archive metadata

GitHub is the engineering source of truth; Kaggle is a curated distribution package. Distribution metadata must record the same canonical product release as GitHub.

A package should include a small JSON metadata file with fields such as:

- `project_release`
- `tax_year`
- `status`
- `canonical_workbook`
- `source_repository`

For the current package, `project_release` must be `v0.1.3`.

## Release gate

Do not mark a release **Verified** while active public surfaces disagree on the release number or while the Git tag used by the GitHub Release differs from the canonical product release.

A documented protected legacy alias does not become the current release merely because the tag still exists; the active GitHub Release, README, Wiki and distribution metadata remain authoritative for current-release identification.

## Pre-release checklist

- [ ] README product-release badge matches the canonical version.
- [ ] README current-release table matches.
- [ ] Root Wiki Home and Project Status match.
- [ ] `CHANGELOG.md` matches.
- [ ] `RELEASE_NOTES.md` and version-specific notes match.
- [ ] Release metadata JSON matches.
- [ ] Kaggle/archive metadata matches.
- [ ] GitHub Release uses the exact canonical Git tag.
- [ ] GitHub Release title matches exactly.
- [ ] Any retained legacy tag is documented as deprecated and is not attached to a current release.
- [ ] Future-version files are clearly marked Unreleased until publication.
