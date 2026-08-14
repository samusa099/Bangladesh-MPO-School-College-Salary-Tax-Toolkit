# Kaggle Publish Package

**Release line:** `v0.1.3`  
**Status:** Beta  
**Tax Year:** 2026–27

This directory is the curated, download-friendly distribution package for the Bangladesh MPO School & College Salary Tax Toolkit. GitHub remains the engineering source of truth; this package intentionally excludes workflows, development-only files, private records and unrelated repository content.

## Package contents

```text
publish/
├── MPO_School_College_Salary_Tax_BD_TY2026_27.xlsx
├── README.md
├── USER_GUIDE.md
├── RELEASE_NOTES.md
├── LICENSE
├── dataset-metadata.json
├── package-manifest.json
├── data/
│   └── csv/
├── metadata/
│   ├── project.yml
│   └── release-metadata.json
├── notebooks/
│   └── bd_mpo_salary_tax_toolkit_kaggle_demo.py
└── previews/
```

## Start here

1. Download/open `MPO_School_College_Salary_Tax_BD_TY2026_27.xlsx` in Excel 2019 or newer.
2. Read `USER_GUIDE.md` before changing inputs.
3. Use the CSV files for review, Python, SQL or BI exploration.
4. Use the notebook script on Kaggle for programmatic inspection.
5. Treat the workbook as a **Beta planning tool** until the repository's verification gates are complete.

## Verification status

This package does **not** claim a Verified release. The repository still tracks deterministic formula execution, official salary-row reconciliation, source extraction and independent practitioner/legal review as open release gates.

## Privacy and safety

This distribution must contain no real TIN, NID, bank-account information, personal tax returns, identifiable employee payroll records, tokens, credentials or secrets. Demo/example data must remain synthetic or otherwise privacy-safe.

## Disclaimer

This project is an educational and planning toolkit. It is not an official MPO payroll system, tax assessment, tax-filing service or legal opinion.
