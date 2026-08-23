# 🧾 Taxpayer Categories

The workbook uses `TAXPAYER_CATEGORIES` to compare tax-free thresholds and select the correct base threshold for the annual tax calculation.

> [!IMPORTANT]
> The source-target values below are taken from the National Board of Revenue's 2026 Budget Speech, Appendix B, Table 1, for **Tax Years 2026–27 and 2027–28**. The canonical v0.1.3 workbook is still under restoration/QA in issue #30 and PR #51, so these source-verified values must be reconciled against the workbook before the workbook can be treated as Verified.

## Threshold Comparison

| Category | Tax-free threshold |
|:--|--:|
| General male below 65 | **BDT 375,000** |
| Female taxpayer | **BDT 425,000** |
| Male taxpayer aged 65 or above | **BDT 425,000** |
| Female taxpayer aged 65 or above | **BDT 425,000** |
| Third-gender taxpayer | **BDT 500,000** |
| Person with disability | **BDT 500,000** |
| Gazetted wounded freedom fighter | **BDT 525,000** |
| Gazetted July fighter | **BDT 525,000** |
| Parent/legal guardian of eligible dependent with disability | **Additional BDT 50,000** |

### Authoritative source

- National Board of Revenue, **Budget Speech 2026**, Appendix B, Table 1: <https://nbr.gov.bd/uploads/budget/Budget_Speech_English.pdf>
- NBR Finance Acts catalogue, which lists **Finance Act, 2026** dated 06 July 2026: <https://nbr.gov.bd/regulations/acts/finance-acts>

The same NBR budget material shows the **BDT 400,000 / 450,000 / 525,000 / 550,000** sequence for later tax years, not for Tax Years 2026–27 and 2027–28. See the dated reconciliation note in `docs/research/TAX_THRESHOLD_RECONCILIATION_2026-08-23.md`.

## Selection Logic

The taxpayer category is selected in:

```text
USER_INPUT!B13
```

The tax engine then uses the selected category to calculate:

```text
Total Taxable Income
- Applicable Category Threshold
= Income Above Threshold
```

Income above the threshold is passed through the progressive tax slabs and minimum-tax comparison.

> [!NOTE]
> Female status and age 65 or above use the same BDT 425,000 threshold. These conditions are not added together.

## Validation Checks

- [ ] The selected category matches the taxpayer’s legal status.
- [ ] Age-based eligibility is assessed for the relevant tax year.
- [ ] Only one base threshold is applied.
- [ ] Disability or special-category evidence is available where required.
- [ ] Boundary values immediately below, at, and above each threshold are tested.
- [ ] Workbook outputs are reconciled against these source-target values after the canonical workbook is restored.

## Beta Limitation

The workbook provides a planning estimate. Final tax treatment may depend on effective legislation, taxpayer evidence, location-based minimum tax, exemptions, rebate eligibility, and professional interpretation. Source verification of a threshold does not by itself prove that the current workbook binary implements it correctly.

---

**Related pages:** [Formula Methodology](Formula-Methodology.md) · [Validation and Release Gates](Validation-and-Release-Gates.md)
