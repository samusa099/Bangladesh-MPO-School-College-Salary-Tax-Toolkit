# 🚦 Project Status

**Last reviewed:** 2026-09-04  
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
| Core salary flow | ✅ Implemented | Monthly and annual salary calculation workflow is present, but final binary verification remains part of workbook QA. |
| Taxpayer categories | 🟡 Source-corrected; workbook pending | PR #54 corrected the canonical TY 2026–27 reference targets to BDT 375k / 425k / 500k / 525k (+50k eligible dependent). The current corrupt workbook cannot yet be inspected to confirm its formulas implement those corrected targets. |
| Workbook UX / v0.1.3 package | ✅ Implemented | v0.1.3 workbook and visual previews were merged; tab-layout changes were documented. |
| Release identifier consistency | ✅ Complete | Repository metadata is aligned to v0.1.3; the live GitHub Release uses the canonical tag, while `v2` is retained only as a documented deprecated protected alias. |
| Source extraction | 🟡 In progress | PR #55 materially strengthened evidence for Baishakhi allowance, Welfare Trust and Retirement Benefit deductions, and corrected evidence maturity labels. Issue #39 remains open because festival allowance still lacks archived primary authority and other workbook rules still require complete source-to-formula mapping. |
| Workbook integrity / formula-reference QA | 🔴 Blocked | Issue #30 / draft PR #51 confirmed the canonical and Kaggle-mirror XLSX are the same truncated 12,545-byte corrupt blob. An intact source workbook must be restored before formula/reference, recalculation and behavior checks can run. |
| Official salary reconciliation | 🟡 In progress | Issue #40 remains open; the 10-row anonymized reconciliation gate is not yet met. Workbook corruption also prevents reliable execution against reference rows. |
| Deterministic formula validation | 🟡 Specification complete; execution blocked | PR #56 expanded and source-aligned the deterministic suite to 30 cases. Issue #41 remains open because the cases have not been executed against an intact workbook and therefore cannot be marked pass/fail. |
| Legal and practitioner review | ⏳ Pending | Issue #42 remains outstanding; line-by-line legal/policy review and practitioner sign-off have not completed. |
| Verified release | ⏳ Pending | Requires completion of every remaining verification gate above. |

## Progress since the previous checkpoint

- No new commit was merged to `main` after the 2026-08-28 weekly status commit before this review, so no published release gate has advanced.
- Draft PR #51 was refreshed on 2026-08-29 onto current `main` and now includes stronger regression coverage plus auditing of both canonical and Kaggle workbook copies; it remains intentionally blocked because both copies are still the same corrupt 12,545-byte workbook.
- No new evidence was found that completes source extraction, the 10-row official salary reconciliation gate, execution of the 30 deterministic scenarios, or legal/practitioner review.
- Release identity remains consistent on canonical `v0.1.3`; no status promotion is justified.

## Research work still blocking Verified status

- Restore an intact canonical School & College workbook and replace both the repository workbook and Kaggle publish mirror.
- Rerun PR #51's XLSX package/formula/reference audit; open the workbook without repair warnings; recalculate; and complete cross-sheet/manual behavior checks.
- Confirm the restored workbook implements the corrected TY 2026–27 taxpayer thresholds and every source-corrected rule.
- Complete authoritative source extraction and source-to-formula mapping for festival allowance, medical allowance, salary-component tax treatment, house-rent/special-facility assumptions and any other rule still marked pending or interpretation-required.
- Execute all 30 deterministic scenarios, record expected versus actual results, and resolve or explicitly block every failure.
- Reconcile at least 10 anonymized official salary rows against workbook output and explain every material difference.
- Complete line-by-line legal/policy review and practitioner review.
- Complete final workbook/release-asset QA and the release Definition of Done after the evidence gates above are satisfied.

## Weekly update rule

Each weekly review should:

1. Compare repository changes and project evidence with the previous status.
2. Promote or downgrade a status only when evidence supports the change.
3. Update `wiki/Home.md` and this page with the review date.
4. Keep **Verified release** pending until every published release gate is satisfied.
5. Record “no material status change” when work occurred but no release gate advanced.
6. Confirm README, Wiki, changelog, release notes, Git tag and distribution metadata still use one canonical product release identifier.

**Next scheduled review:** 2026-09-11
