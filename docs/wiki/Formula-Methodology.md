# 🧮 Formula Methodology

This page documents the workbook’s calculation architecture, salary flow, tax flow, and validation principles.

## Architecture

```text
Shared calculation engine
        ↓
Sector-specific rule pack
        ↓
Institution and employee inputs
        ↓
Salary, tax, reporting and validation outputs
```

> [!IMPORTANT]
> Rules are separated from calculation logic wherever practical. This allows a verified rule to be updated without rebuilding the entire workbook.

## Monthly Salary Flow

```text
Basic Salary
+ House Rent
+ Medical Allowance
+ Other Allowance
+ Special Facility
+ Festival Bonus
+ Baishakhi Allowance
+ Arrear
= Gross Pay

Gross Pay
- Welfare Deduction
- Retirement Deduction
- Other Deduction
- TDS
= Net Pay
```

## MVP Rules

### House Rent

```excel
=MAX(Basic_Salary*15%,2000)
```

| Element | Rule |
|:--|:--|
| Percentage | 15% of basic salary |
| Minimum | BDT 2,000 |
| Status | Current TY 2026–27 working assumption |

### Special Facility

```text
Grades 1–9:  Basic Salary × 10%
Grades 10–20: MAX(Basic Salary × 15%, BDT 1,500)
```

## Annual Tax Flow

```text
Annual Gross Salary
- Verified Salary Exemptions
+ Other Annual Taxable Income
= Total Taxable Income

Total Taxable Income
- Applicable Category Threshold
= Income Above Threshold

Progressive Slab Tax
- Eligible Rebate
= Tax After Rebate

MAX(Tax After Rebate, Applicable Minimum Tax)
- Tax Deducted at Source
= Estimated Tax Payable or Refund Position
```

## Formula Design Principles

1. **Traceability:** every verified rule links to a source ID.
2. **Separation:** inputs, rules, calculations, and outputs remain distinct.
3. **Transparency:** no hidden VBA or opaque calculation layer in v1.
4. **Compatibility:** core formulas target Excel 2019 or later.
5. **Determinism:** the same inputs must return the same outputs.
6. **Boundary testing:** thresholds, grade changes, and minimum values require edge-case tests.
7. **No silent errors:** missing or invalid inputs should produce visible warnings.

## Beta Assumptions

Medical allowance, festival allowance, Baishakhi allowance, deductions, exemptions, rebate, and minimum-tax interpretation remain editable until source extraction and review are complete.

> [!CAUTION]
> A configurable input is not automatically a verified legal default. Its source and effective date must be documented before Verified release.

---

**Related pages:** [Taxpayer Categories](Taxpayer-Categories.md) · [Validation and Release Gates](Validation-and-Release-Gates.md)
