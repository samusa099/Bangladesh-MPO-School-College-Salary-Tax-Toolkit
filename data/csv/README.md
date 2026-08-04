# CSV Data Layer

This directory contains reviewable, UTF-8 CSV exports derived from the maintained MPO School & College workbook and its documented rule pack.

## Purpose

- make key workbook reference tables easy to inspect without opening Excel;
- support Python, SQL, Power BI, Tableau and other analytics tools;
- provide diff-friendly records for pull-request review;
- keep release metadata separate from workbook binaries.

## Files

| File | Purpose |
|---|---|
| `01_taxpayer_categories_ty2026_27.csv` | Taxpayer categories, thresholds and workbook mappings |
| `02_salary_component_dictionary_ty2026_27.csv` | Salary and deduction component definitions |
| `03_workbook_sheet_catalog_ty2026_27.csv` | Workbook sheet inventory and usage classification |
| `04_validation_scenarios_ty2026_27.csv` | Deterministic formula and boundary-test catalogue |
| `05_release_asset_manifest_ty2026_27.csv` | Stable release asset names and roles |

## Governance

The Excel workbook remains the calculation product. CSV files are structured companion exports, not an independent legal or payroll authority.

When a workbook rule changes, update the relevant CSV in the same pull request and preserve the applicable source ID, effective date and verification status where available.

Do not commit employee-identifiable payroll records, national identifiers, bank details, tax-return data or unredacted institutional records.
