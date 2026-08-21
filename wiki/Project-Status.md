# 🚦 Project Status

**Last reviewed:** 2026-08-21  
**Release line:** v0.1.3  
**Overall status:** Beta  
**Review cadence:** Weekly

## Release identity

- **Canonical public product release:** `v0.1.3`
- **README/design revision:** `v4.0` — documentation/design only, not a product release
- **Prepared future candidate:** `v0.1.4` — Unreleased until matching Git tag and GitHub Release are published
- **Release-number consistency gate:** Complete. The live GitHub Release uses the canonical `v0.1.3` tag. Historical `v2` remains only as a deprecated protected legacy alias and is not attached to the active release.

## Current release gates

| Area | Status | Evidence / remaining gate |
|---|---|---|
| Workbook architecture | ✅ Implemented | Shared engine and School & College workbook structure are present. |
| Core salary flow | ✅ Implemented | Monthly and annual salary calculation workflow is present. |
| Taxpayer categories | ✅ Implemented | Taxpayer-category comparison is included. |
| Workbook UX / v0.1.3 package | ✅ Implemented | v0.1.3 workbook and visual previews were merged; tab-layout changes were documented. |
| Release identifier consistency | ✅ Complete | Repository metadata is aligned to v0.1.3; the live GitHub Release uses the canonical tag, while `v2` is retained only as a documented deprecated protected alias. |
| Source extraction | 🟡 In progress | Issue #39 remains open; several allowance, deduction and tax-treatment rules still require authoritative source-by-source extraction. |
| Official salary reconciliation | 🟡 In progress | Issue #40 remains open; the 10-row anonymized reconciliation gate is not yet met. |
| Deterministic formula validation | 🟡 In progress | Validation assets and formula-error scans exist, but the full 20–30 executed deterministic scenario gate is not yet demonstrated. |
| Legal and practitioner review | ⏳ Pending | Line-by-line legal/policy review and practitioner sign-off remain outstanding. |
| Verified release | ⏳ Pending | Requires completion of every remaining verification gate above. |

## Progress since the previous checkpoint

- Release/version reconciliation was completed: issue #43 is closed and the live GitHub Release now uses the canonical `v0.1.3` tag.
- The historical `v2` tag is documented as a deprecated protected legacy alias rather than an active release identifier.
- A clean, curated v0.1.3 Kaggle/archive publish package was materialized in PR #50 without changing salary/tax formulas or verification status.
- GitHub Actions and governance tooling were strengthened, including repository-maintenance orchestration and an API-key-free GitHub Models PR reviewer.
- No new evidence was found that completes source extraction, the 10-row salary reconciliation gate, the 20–30 deterministic validation gate, or legal/practitioner review.
- No repository commits were found after 2026-08-14 before this weekly review, so the core research/validation status has not advanced since those release-governance changes.

## Research work still blocking Verified status

- Complete authoritative source extraction for festival allowance, Baishakhi allowance, medical allowance, welfare and retirement deductions, salary-component tax treatment, and any other workbook rule still pending evidence.
- Reconcile at least 10 anonymized official salary rows against workbook output and explain every material difference.
- Complete and record 20–30 deterministic formula scenarios, including boundary and exception cases.
- Resolve all unexplained salary differences and any formula/reference defects found during QA.
- Complete line-by-line legal/policy review and practitioner review.
- Complete final workbook/release-asset QA and the release Definition of Done after the evidence gates above are satisfied.

## Weekly update rule

Each weekly review should:

1. Compare repository changes and project evidence with the previous status.
2. Promote a status only when evidence supports the change.
3. Update `wiki/Home.md` and this page with the review date.
4. Keep **Verified release** pending until every published release gate is satisfied.
5. Record “no material status change” when work occurred but no release gate advanced.
6. Confirm README, Wiki, changelog, release notes, Git tag and distribution metadata still use one canonical product release identifier.

**Next scheduled review:** 2026-08-28
