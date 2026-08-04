<p align="center">
  <img src="assets/brand/github-cover.svg" alt="Bangladesh MPO Salary and Tax Toolkit cover" width="100%">
</p>

# Bangladesh MPO School & College Salary Tax Toolkit

[![Excel Toolkit](https://img.shields.io/badge/Excel-Toolkit-107C41?style=for-the-badge&logo=microsoft-excel&logoColor=white)](#)
[![Bangladesh MPO](https://img.shields.io/badge/Bangladesh-MPO-0F766E?style=for-the-badge)](#)
[![Tax Year](https://img.shields.io/badge/Tax%20Year-2026--27-2563EB?style=for-the-badge)](#)
[![Status](https://img.shields.io/badge/Status-Beta-B7791F?style=for-the-badge)](#)

An open-source, Excel-based toolkit for **MPO-listed School & College employees in Bangladesh** to prepare salary statements, tax estimates, payslips, and personal finance dashboards.

## What this project does

This repository turns Bangladesh MPO payroll and individual tax rules into a structured, auditable Excel workbook.

The first release focuses only on:

- MPO School & College monthly salary calculation
- Annual salary statement
- Tax Year 2026–27 tax estimate
- Male/female/special taxpayer category comparison
- Payslip view
- Income–expense allocation
- Dashboard and validation cases

## Current release

| Item | Value |
|---|---|
| Product | Bangladesh MPO Salary & Tax Excel Toolkit |
| First package | MPO School & College Salary and Tax |
| Workbook | `MPO_School_College_Salary_Tax_BD_TY2026_27.xlsx` |
| Version | `v0.1.2-taxpayer-categories` |
| Status | Beta |
| Macro policy | No VBA in v1 |
| Compatibility target | Excel 2019 core formulas |

## Workbook modules

| Sheet | Purpose |
|---|---|
| `START_HERE` | User instructions and scope note |
| `PROJECT_CHARTER` | Finalized project scope and release rules |
| `USER_INPUT` | Salary, allowance, deduction and taxpayer inputs |
| `TAXPAYER_CATEGORIES` | Male, female, 65+, disabled and special category tax variation |
| `MONTHLY_SALARY` | Month-by-month salary calculation |
| `ANNUAL_SALARY` | Annual salary statement |
| `TAX_CALCULATION` | Progressive tax estimate and minimum tax |
| `INCOME_EXPENSE` | Expense allocation and surplus/deficit check |
| `DASHBOARD` | KPI cards and charts |
| `PAYSLIP` | Printable monthly payslip |
| `SOURCE_REGISTER` | Rule evidence and verification status |
| `DATA_DICTIONARY` | Field definitions and formula logic |
| `TEST_CASES` | Deterministic formula validation cases |

## Taxpayer category coverage

For Tax Year 2026–27, the workbook compares:

| Category | Tax-free threshold |
|---|---:|
| General male below 65 | BDT 400,000 |
| Female taxpayer or taxpayer aged 65+ | BDT 450,000 |
| Third-gender taxpayer or disabled individual | BDT 525,000 |
| Eligible gazetted wounded freedom fighter or July fighter | BDT 550,000 |
| Eligible disabled child/dependent | Additional BDT 50,000 |

Female status and age 65+ are not added together. The workbook treats them as the same higher-threshold class.

## Repository architecture

```text
Shared calculation engine
        ↓
Sector rule packs
        ↓
Institution-specific workbook
```

GitHub is the **engineering workspace**. Kaggle is the **clean distribution package**.

```text
assets/                 Brand and preview images
data/reference/         Metadata and structured reference records
docs/                   Research, source methodology, user guides and governance
excel/                  Workbook files and shared-engine notes
notebooks/              Reproducible validation notebook
release/                Release notes and manifest
tests/                  Formula validation cases
```

## Verification status

This project is still **Beta**. It becomes Verified only after:

- 20–30 deterministic formula tests pass;
- at least 10 anonymized official salary rows reconcile;
- every verified rule has source ID and effective date;
- formula cells are protected for public release;
- MPO/payroll and tax practitioners review the workbook.

## Scope boundary

This repository does **not** mix in:

- Madrasa payroll
- Ebtedayi payroll
- Technical/Vocational payroll
- Government/autonomous salary
- Private/NGO salary
- VAT/TDS
- Import-export/LC
- Company tax

Those will become separate future packages.

## Disclaimer

This workbook is an educational planning tool. It is not an official MPO bill, tax assessment, legal opinion, or substitute for professional review.

## Author

Maintained by **Musa** as a data analytics and Excel automation portfolio project for Bangladesh payroll and tax workflows.
