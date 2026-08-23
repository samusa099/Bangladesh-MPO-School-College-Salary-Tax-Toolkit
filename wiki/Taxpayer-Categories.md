# 🧾 Taxpayer Categories

The workbook uses `TAXPAYER_CATEGORIES` to compare tax-free thresholds and select the correct base threshold for the annual tax calculation.

> [!IMPORTANT]
> The values below reflect the project’s current **Tax Year 2026–27 working rule table** and remain subject to final source-by-source legal and professional review.

## Threshold Comparison

| Category | Tax-free threshold |
|:--|--:|
| General male below 65 | **BDT 400,000** |
| Female taxpayer | **BDT 450,000** |
| Male taxpayer aged 65 or above | **BDT 450,000** |
| Female taxpayer aged 65 or above | **BDT 450,000** |
| Third-gender taxpayer | **BDT 525,000** |
| Person with disability | **BDT 525,000** |
| Gazetted wounded freedom fighter | **BDT 550,000** |
| Gazetted July fighter | **BDT 550,000** |

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
> Female status and age 65 or above use the same BDT 450,000 threshold. These conditions are not added together.

## Validation Checks

- [ ] The selected category matches the taxpayer’s legal status.
- [ ] Age-based eligibility is assessed for the relevant tax year.
- [ ] Only one base threshold is applied.
- [ ] Disability or special-category evidence is available where required.
- [ ] Boundary values immediately below, at, and above each threshold are tested.

## Beta Limitation

The workbook provides a planning estimate. Final tax treatment may depend on effective legislation, taxpayer evidence, location-based minimum tax, exemptions, rebate eligibility, and professional interpretation.

---

**Related pages:** [Formula Methodology](Formula-Methodology.md) · [Validation and Release Gates](Validation-and-Release-Gates.md)
