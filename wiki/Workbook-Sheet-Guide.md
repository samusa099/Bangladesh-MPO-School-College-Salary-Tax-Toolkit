# 📊 Workbook Sheet Guide

This page explains the purpose, user interaction, and control role of each worksheet in the School and College MPO workbook.

## 🧭 Workbook Flow

```text
START_HERE → USER_INPUT → Salary Calculations → Tax Calculation
                         ↓
              Reports, Dashboard and Payslip
                         ↓
          Source Register, Dictionary and Tests
```

## Core Worksheets

| Sheet | Type | Purpose |
|:--|:--:|:--|
| `START_HERE` | Guide | Entry point, scope, version, warnings, and usage instructions |
| `PROJECT_CHARTER` | Governance | Project architecture, boundaries, and release principles |
| `USER_INPUT` | Input | Employee, salary, allowance, deduction, and tax inputs |
| `SECTOR_RULES` | Rules | School and College MPO calculation assumptions |
| `TAXPAYER_CATEGORIES` | Rules | Category thresholds and comparison logic |
| `MONTHLY_SALARY` | Calculation | Month-by-month earnings, deductions, and net pay |
| `ANNUAL_SALARY` | Calculation | Annual salary statement and component totals |
| `TAX_CALCULATION` | Calculation | Taxable income, slabs, rebate, TDS, and tax estimate |
| `INCOME_EXPENSE` | Analysis | Annual expense allocation and savings analysis |
| `DASHBOARD` | Report | KPI cards, charts, and summary indicators |
| `PAYSLIP` | Report | Printable payslip for the selected month |
| `TAX_SUMMARY` | Report | Consolidated annual tax working summary |
| `SOURCE_REGISTER` | Audit | Source IDs, links, dates, and extracted rule notes |
| `DATA_DICTIONARY` | Audit | Field names, definitions, formats, and ownership |
| `TEST_CASES` | Validation | Deterministic formula and boundary tests |

## ✍️ Editing Rules

> [!IMPORTANT]
> Edit only cells intentionally marked as user inputs. Calculation, lookup, and control cells should remain protected in verified releases.

| Cell category | User action |
|:--|:--|
| Highlighted input | Enter or select a value |
| Formula cell | Do not overwrite |
| Reference table | Edit only during controlled rule-pack maintenance |
| Output cell | Review; do not manually replace |
| Test result | Investigate failures before release |

## 🔍 Review Sequence

1. Confirm the workbook tax year and release status in `START_HERE`.
2. Complete `USER_INPUT`.
3. Review `MONTHLY_SALARY` and `ANNUAL_SALARY`.
4. Check `TAX_CALCULATION` and `TAX_SUMMARY`.
5. Review `DASHBOARD` and `PAYSLIP`.
6. Confirm sources and test results before distribution.

## 🗂️ Workbook Naming

```text
MPO_School_College_Salary_Tax_BD_TY2026_27.xlsx
```

> [!WARNING]
> This workbook is sector-specific. Madrasa, Ebtedayi, and Technical or Vocational education must use separate future rule packs and workbooks.

---

**Related pages:** [Getting Started](Getting-Started.md) · [Formula Methodology](Formula-Methodology.md) · [Validation and Release Gates](Validation-and-Release-Gates.md)
