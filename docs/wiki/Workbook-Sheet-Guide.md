# Workbook Sheet Guide

This guide explains the workbook modules in `MPO_School_College_Salary_Tax_BD_TY2026_27.xlsx`.

| Sheet | Purpose | User action |
|---|---|---|
| `START_HERE` | Entry point, workbook scope, status and warnings | Read first |
| `PROJECT_CHARTER` | Finalized project scope, architecture and release rules | Read for project governance |
| `USER_INPUT` | All employee, salary, allowance, deduction and tax inputs | Edit highlighted input cells only |
| `SECTOR_RULES` | School/College rule pack for salary components | Review source-linked rules |
| `TAXPAYER_CATEGORIES` | Male/female/special taxpayer category comparison | Review category impact |
| `MONTHLY_SALARY` | July–June salary calculation | Review monthly gross, deductions and net pay |
| `ANNUAL_SALARY` | Annual salary aggregation | Use for salary statement |
| `TAX_CALCULATION` | Progressive tax and minimum-tax estimate | Use for planning only |
| `INCOME_EXPENSE` | Annual expense allocation and surplus/deficit | Enter personal expense values |
| `DASHBOARD` | KPI cards and charts | Use for quick insight |
| `PAYSLIP` | Month-specific payslip output | Select month from input sheet |
| `TAX_SUMMARY` | Tax-return working summary | Use while preparing return information |
| `SOURCE_REGISTER` | Source ID, authority, extracted rule and status | Audit every verified rule |
| `DATA_DICTIONARY` | Field definitions and calculation meaning | Use for formula review |
| `TEST_CASES` | Deterministic test cases | Use before release |

## Workbook protection rule

Formula cells should be protected before a verified public release. Users should only edit input cells.

## Naming convention

The workbook follows this format:

```text
MPO_School_College_Salary_Tax_BD_TY2026_27.xlsx
```

Format logic:

```text
Sector_Subsector_Product_Country_TaxYear.xlsx
```
