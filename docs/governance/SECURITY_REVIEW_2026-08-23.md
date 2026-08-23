# Security Review — 2026-08-23

## Scope

This review covers repository-level controls for public data handling, GitHub Actions supply-chain safety, committed-secret detection, dependency changes, workbook/archive validation, and contributor-facing security guidance.

## Result

**Assessment:** no unresolved critical or high-severity repository-configuration finding was identified in this review. The project remains **Beta** for workbook/legal verification reasons; this security review does not promote the workbook to Verified status.

## Controls verified

| Control | Evidence | Status |
|---|---|---|
| Least-privilege workflow baseline | `Portfolio Security` defaults to `contents: read`; elevated permissions are scoped to jobs/workflows that require them | ✅ |
| Immutable third-party Actions | `.github/scripts/repository_policy.py` rejects non-40-character action refs | ✅ |
| Committed-secret scanning | `Portfolio Security` downloads a pinned Gitleaks release, verifies its SHA-256, and scans Git history with redaction | ✅ |
| Dependency change review | `actions/dependency-review-action` runs on pull requests and fails on high-severity dependency findings | ✅ |
| Sensitive/private file controls | Repository policy blocks common credential/private-key filenames and unsafe binary suffixes | ✅ |
| XLSX/archive safety | Repository policy checks XLSX structure, path traversal and oversized archive members | ✅ |
| CSV formula-injection controls | Repository policy rejects spreadsheet-formula injection prefixes in CSV data | ✅ |
| Security reporting policy | `SECURITY.md` defines restricted data and private vulnerability-reporting expectations | ✅ |
| Dependabot maintenance | GitHub Actions dependency updates are configured through `.github/dependabot.yml` | ✅ |

## Platform-side secret protection

The connected repository API used for this review does not expose a trustworthy read of GitHub's account/repository **Secret scanning / Push protection** toggle state. Therefore this review does **not** claim that GitHub-hosted push protection is enabled.

The repository does have an equivalent committed-secret detection gate through Gitleaks in `Portfolio Security`. That control detects committed secrets in CI, but it is not a substitute for true pre-push blocking. If GitHub Secret Scanning and Push Protection are available for this repository, they should remain enabled in repository security settings.

## Known non-security release blocker

The canonical v0.1.3 workbook currently requires restoration from an intact source asset before the stronger workbook audit in PR #51 can pass. That is tracked separately as release/QA work and is intentionally not hidden or downgraded by this security review.

## Decision

Repository security/hygiene review for issue #33 is complete at the code-and-workflow level. Future security changes should preserve full-SHA action pinning, least-privilege permissions, dependency review, Gitleaks scanning, and public-data restrictions.
