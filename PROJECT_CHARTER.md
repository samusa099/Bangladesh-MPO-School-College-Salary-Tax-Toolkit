# Finalized Project Charter

## Umbrella brand
**Bangladesh Salary, Tax & Personal Finance Excel Toolkit**

## First repository
`Bangladesh-MPO-School-College-Salary-Tax-Toolkit`

## First deliverable
**Research Pack 01 — MPO School & College Salary and Tax**

## First workbook
`MPO_School_College_Salary_Tax_BD_TY2026_27.xlsx`

## Architecture
`Shared calculation engine → Sector rule packs → Institution-specific workbook`

The project uses one workbook per sector/package. Designation and grade differences are handled through structured reference tables and dropdowns, not by creating a separate file for every designation.

## Current strict scope
This repository currently covers **MPO School & College salary and tax only**.

The following are excluded from this repository and will be handled as separate future packages:
- Government/autonomous salary
- Private/NGO salary
- Individual tax and personal finance
- Small business
- VAT/TDS
- Import-export and LC
- Company tax

## Platform roles
### GitHub
Engineering workspace containing research, formula methodology, source mapping, workbooks, validation, tests, notebooks, governance and releases.

### Kaggle
Compact distribution package containing the usable workbook, concise metadata, user guides, validation cases, notebook and previews.

## Release controls
- Excel 2019-compatible core formulas
- No VBA in v1
- 20–30 deterministic formula tests
- At least 10 anonymized official salary-row reconciliations before Verified status
- Source-linked rules with effective dates
- Protected formula cells before v1.0
- MPO/payroll practitioner and tax practitioner review before Verified status
- Previous tax-year releases are never overwritten
