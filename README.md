<p align="center">
  <img src="assets/brand/github-cover.svg" alt="Bangladesh MPO Salary and Tax Toolkit cover" width="100%">
</p>

# Bangladesh MPO School & College Salary Tax Toolkit

[![Excel Toolkit](https://img.shields.io/badge/Excel-Toolkit-107C41?style=for-the-badge&logo=microsoft-excel&logoColor=white)](#)
[![Bangladesh MPO](https://img.shields.io/badge/Bangladesh-MPO-0F766E?style=for-the-badge)](#)
[![Tax Year](https://img.shields.io/badge/Tax%20Year-2026--27-2563EB?style=for-the-badge)](#)
[![Status](https://img.shields.io/badge/Status-Beta-B7791F?style=for-the-badge)](#)
[![Portfolio Security](https://img.shields.io/github/actions/workflow/status/samusa099/Bangladesh-MPO-School-College-Salary-Tax-Toolkit/portfolio-security.yml?branch=main&style=for-the-badge&label=Portfolio%20Security)](../../actions/workflows/portfolio-security.yml)
[![Issues](https://img.shields.io/github/issues/samusa099/Bangladesh-MPO-School-College-Salary-Tax-Toolkit?style=for-the-badge)](../../issues)

<p align="center">
  <a href="#-project-overview">Overview</a> ·
  <a href="#-workbook-modules">Workbook</a> ·
  <a href="#-repository-structure">Structure</a> ·
  <a href="data/csv/README.md">CSV Layer</a> ·
  <a href="docs/wiki/Home.md">Wiki Source</a> ·
  <a href="packages/kaggle/README.md">Kaggle Package</a>
</p>

An open-source, Excel-based toolkit for **MPO-listed School & College employees in Bangladesh** to prepare salary statements, tax estimates, payslips and personal-finance dashboards.

> **Project flow:** verified rules → structured inputs → Excel calculation engine → formula tests → reporting outputs → release package.

## ✨ Project overview

This repository turns Bangladesh MPO payroll and individual-tax rules into a structured, auditable Excel product.

| Capability | Included |
|---|---|
| 🧮 Salary calculation | Monthly basic salary, allowances, deductions and net pay |
| 🧾 Tax planning | Tax Year 2026–27 thresholds, slabs, minimum tax and TDS inputs |
| 👥 Taxpayer categories | Male, female, age 65+, third gender, disability and gazetted categories |
| 📊 Reporting | Annual statement, tax summary, dashboard and printable payslip |
| ✅ Validation | Deterministic formula scenarios, source register and verification status |
| 📁 Open data support | Reviewable CSV reference exports for Python, SQL and BI tools |
| 📚 Documentation | Version-controlled Wiki source under `docs/wiki/` |
| 📦 Distribution | Separate Kaggle-ready package design under `packages/kaggle/` |

## 🧰 Repository tools and governance

| Tool | Purpose | Open |
|---|---|---|
| Portfolio Security | Validates repository files, XLSX archives, CSV safety, immutable Actions and committed secrets | [Workflow](.github/workflows/portfolio-security.yml) |
| Repository policy | Workbook-focused validation script used by GitHub Actions | [Validator](.github/scripts/repository_policy.py) |
| Wiki Publisher | Synchronizes the authoritative `docs/wiki/` source to the separate GitHub Wiki repository | [Workflow](.github/workflows/publish-wiki.yml) |
| Dependabot | Maintains GitHub Actions dependencies on an Asia/Dhaka schedule | [Configuration](.github/dependabot.yml) |
| Workbook bug report | Structured form for formula, layout, source and compatibility defects | [Open a bug report](../../issues/new?template=workbook-bug.yml) |
| Pull-request checklist | Requires workbook, source, privacy and security validation | [Template](.github/pull_request_template.md) |
| Security policy | Defines private reporting, restricted data and workbook security controls | [Policy](SECURITY.md) |

## 📌 Current release

| Item | Value |
|---|---|
| Product | Bangladesh MPO Salary & Tax Excel Toolkit |
| First package | MPO School & College Salary and Tax |
| Workbook | `MPO_School_College_Salary_Tax_BD_TY2026_27.xlsx` |
| Version | `v0.1.2-taxpayer-categories` |
| Status | Beta |
| Macro policy | No VBA in v1 |
| Compatibility target | Excel 2019 core formulas |

## 📊 Workbook modules

| Sheet | Purpose |
|---|---|
| `START_HERE` | User instructions and scope note |
| `PROJECT_CHARTER` | Finalized project scope and release rules |
| `USER_INPUT` | Salary, allowance, deduction and taxpayer inputs |
| `TAXPAYER_CATEGORIES` | Male, female, 65+, disabled and special-category tax variation |
| `MONTHLY_SALARY` | Month-by-month salary calculation |
| `ANNUAL_SALARY` | Annual salary statement |
| `TAX_CALCULATION` | Progressive tax estimate and minimum tax |
| `INCOME_EXPENSE` | Expense allocation and surplus or deficit check |
| `DASHBOARD` | KPI cards and charts |
| `PAYSLIP` | Printable monthly payslip |
| `TAX_SUMMARY` | Annual tax planning summary |
| `SOURCE_REGISTER` | Rule evidence and verification status |
| `DATA_DICTIONARY` | Field definitions and formula logic |
| `TEST_CASES` | Deterministic formula-validation cases |

## 👥 Taxpayer category coverage

For Tax Year 2026–27, the workbook compares:

| Category | Tax-free threshold |
|---|---:|
| General male below 65 | BDT 400,000 |
| Female taxpayer or taxpayer aged 65+ | BDT 450,000 |
| Third-gender taxpayer or disabled individual | BDT 525,000 |
| Eligible gazetted wounded freedom fighter or July fighter | BDT 550,000 |
| Eligible disabled child or dependent | Additional BDT 50,000 |

Female status and age 65+ are not added together. The workbook treats them as the same higher-threshold class.

## 🧱 Repository architecture

```text
Verified sources and structured reference records
                    ↓
        Shared calculation-engine design
                    ↓
           School and College rule pack
                    ↓
       Institution-specific Excel workbook
                    ↓
     CSV exports, validation and reporting
                    ↓
      GitHub release and Kaggle package
```

GitHub is the **engineering workspace**. Kaggle is the **curated distribution workspace**. The GitHub Wiki is a **published copy** of the authoritative Markdown under `docs/wiki/`.

## 🗂️ Repository structure

```text
Bangladesh-MPO-School-College-Salary-Tax-Toolkit/
├── .github/                    # Workflows, policies and contribution templates
├── assets/
│   ├── brand/                  # Repository identity assets
│   └── previews/               # Stable workbook and release previews
├── data/
│   ├── csv/                    # Diff-friendly project reference exports
│   └── reference/              # Structured source and rule metadata
├── docs/
│   ├── governance/             # Release, security and maintenance guidance
│   ├── research/               # Project-specific rule research
│   ├── user-guides/            # Workbook usage guidance
│   └── wiki/                   # Authoritative GitHub Wiki source
├── excel/
│   ├── shared_engine/          # Reusable calculation-engine notes
│   └── school_college/         # School and College workbook package
├── notebooks/                  # Reproducible validation work
├── packages/
│   └── kaggle/                 # Curated distribution workspace
├── release/                    # Release notes and manifests
├── tests/                      # Formula-validation scenarios
├── CHANGELOG.md
├── CITATION.cff
├── CONTRIBUTING.md
├── LICENSE
├── README.md
└── SECURITY.md
```

See the complete responsibility map in **[Repository Structure](docs/REPOSITORY_STRUCTURE.md)**.

## 📁 CSV data layer

The `data/csv/` folder contains project-specific companion exports only. These files improve pull-request review and make selected tables usable in Python, SQL, Power BI, Tableau and similar tools without replacing the Excel workbook.

Current catalog:

- `01_taxpayer_categories_ty2026_27.csv`
- `02_salary_component_dictionary_ty2026_27.csv`
- `03_workbook_sheet_catalog_ty2026_27.csv`
- `04_validation_scenarios_ty2026_27.csv`
- `05_release_asset_manifest_ty2026_27.csv`

No employee-identifiable payroll, bank, national-ID or tax-return data belongs in this layer.

## 📚 Documentation and Wiki publishing

```text
Main repository
└── docs/wiki/                    authoritative, reviewable source

GitHub Wiki repository
└── *.md                          published copy
```

A root-level `/wiki/` folder is intentionally not used. The GitHub Wiki tab is backed by the separate `.wiki.git` repository. The controlled publishing workflow requires a repository secret named `WIKI_TOKEN` with suitable contents-write access.

## ✅ Verification status

This project remains **Beta** until:

- 20–30 deterministic formula tests pass;
- at least 10 anonymized official salary rows reconcile;
- every verified rule has a source ID and effective date;
- formula cells are protected for public release;
- MPO payroll and tax practitioners review the workbook.

## 🚧 Scope boundary

This repository does **not** mix in:

- Madrasa or Ebtedayi payroll;
- Technical or Vocational payroll;
- government or autonomous salary;
- private or NGO salary;
- VAT, TDS, import-export, LC or company-tax packages;
- HR analytics datasets, employee records or files from other projects.

Those subjects require separate packages and independently verified rule sets.

## ⚠️ Disclaimer

This workbook is an educational planning tool. It is not an official MPO bill, tax assessment, legal opinion or substitute for professional review.

## 👤 Author

Maintained by **Musa** as a data analytics and Excel automation portfolio project for Bangladesh payroll and tax workflows.
