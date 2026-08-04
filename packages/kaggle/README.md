# Kaggle Distribution Package

This directory defines the download-friendly Kaggle package for the Bangladesh MPO School & College Salary and Tax Toolkit.

## Role

GitHub remains the engineering source of truth. The Kaggle package is a curated distribution layer containing only the files required for end users, reviewers and learners.

## Recommended package structure

```text
packages/kaggle/
├── publish/
│   ├── MPO_School_College_Salary_Tax_BD_TY2026_27.xlsx
│   ├── README.md
│   ├── RELEASE_NOTES.md
│   ├── LICENSE
│   ├── data/
│   │   └── csv/
│   └── previews/
└── README.md
```

## Inclusion rules

Include:

- the verified release-candidate workbook;
- project-specific CSV reference exports;
- release notes and licence;
- stable preview assets;
- concise usage and disclaimer documentation.

Exclude:

- `.git/` and `.github/` engineering files;
- development branches and temporary workbooks;
- files named `final`, `new`, `copy`, `latest` or `updated`;
- source documents that cannot legally be redistributed;
- personal payroll, tax-return or institutional records;
- unrelated files from other repositories.

## Source relationship

The Kaggle package must be built from maintained files in this repository. It is not an independent source of rules or calculations.
