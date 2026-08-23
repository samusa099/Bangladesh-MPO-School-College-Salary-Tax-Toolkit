# ✅ Validation and Release Gates

The workbook is currently **Beta**. This page defines the evidence required to promote a release to **Verified**.

## Status Model

| Status | Meaning |
|:--|:--|
| 🔎 Research | Source collection or interpretation is incomplete |
| 📝 Draft | Structure exists, but formulas or rules are not ready |
| 🧪 Beta | Usable for controlled planning, testing, and review |
| ✅ Verified | Source-linked, tested, reconciled, and professionally reviewed |
| 🗄️ Deprecated | Replaced by a newer tax year or controlling policy |

## Mandatory Verified-Release Gates

| Gate | Minimum requirement |
|:--|:--|
| Formula tests | 20–30 deterministic cases pass |
| Official reconciliation | At least 10 anonymized official salary rows reconcile |
| Source linkage | Every verified rule has source ID, authority, and effective date |
| Formula protection | Calculation cells are protected before public release |
| Compatibility | Excel 2019-compatible core formulas |
| Macro policy | No VBA in v1 |
| Practitioner review | MPO/payroll and tax review completed |
| Tax-year integrity | Previous tax-year files remain unchanged and traceable |
| Naming compliance | Release assets follow the approved naming convention |

## Validation Coverage

- Salary-component addition
- Gross-pay and net-pay reconciliation
- Grade-dependent allowance calculations
- Minimum allowance floors
- Deduction calculations
- Annual and monthly consistency
- Tax-slab boundaries
- Taxpayer-category thresholds
- Minimum-tax handling
- Rebate and TDS comparison
- Missing, zero, negative, and invalid input handling

## Test Case Structure

Each test should record:

| Field | Purpose |
|:--|:--|
| Test ID | Stable reference |
| Rule under test | Formula or business rule |
| Inputs | Reproducible values |
| Expected result | Independently calculated answer |
| Actual result | Workbook output |
| Variance | Difference between expected and actual |
| Status | Pass, fail, or review |
| Source ID | Supporting authority |

## Release Decision

> [!IMPORTANT]
> A release must remain **Beta** whenever a material salary or tax rule lacks a primary source, reproducible formula, test evidence, or required professional review.

## Pre-Release Checklist

- [ ] All tests pass or have documented accepted exceptions.
- [ ] No unexplained reconciliation difference remains.
- [ ] Formula cells are protected.
- [ ] Source links and effective dates are complete.
- [ ] Workbook, archive, and preview filenames comply with policy.
- [ ] Release notes explain assumptions, limitations, and changes.
- [ ] The previous tax-year package has not been overwritten.

---

**Related pages:** [Formula Methodology](Formula-Methodology.md) · [Asset Naming Convention](Asset-Naming-Convention.md) · [Roadmap](Roadmap.md)
