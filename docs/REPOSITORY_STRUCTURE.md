# Repository Structure

This repository follows a layered structure inspired by strong analytics-project organization, while remaining specific to the Bangladesh MPO School & College Salary and Tax Toolkit.

> No data, report, code, CSV, documentation or project content is imported from another repository. Only organizational principles such as clear folder boundaries, naming discipline, reviewable metadata and release packaging are adopted.

## Architecture principles

1. `excel/` contains the calculation product and workbook-engine material.
2. `data/` contains structured reference and companion exports derived from this project only.
3. `docs/` contains research, governance and user guidance.
4. `wiki/` is the root-level, authoritative, version-controlled Wiki source.
5. `tests/` contains deterministic formula-validation material.
6. `notebooks/` contains reproducible validation and analysis notebooks.
7. `assets/` contains repository and release visuals.
8. `release/` contains release notes, manifests and version-specific packaging metadata.
9. `packages/` contains distribution-ready workspaces, never the engineering source of truth.

## Target structure

```text
Bangladesh-MPO-School-College-Salary-Tax-Toolkit/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   ├── scripts/
│   └── workflows/
├── assets/
│   ├── brand/
│   └── previews/
├── data/
│   ├── csv/
│   └── reference/
├── docs/
│   ├── governance/
│   ├── research/
│   └── user-guides/
├── excel/
│   ├── shared_engine/
│   └── school_college/
├── notebooks/
├── packages/
│   └── kaggle/
├── release/
├── tests/
├── wiki/                       # Authoritative Wiki source
│   ├── Home.md
│   ├── _Sidebar.md
│   └── ...
├── CHANGELOG.md
├── CITATION.cff
├── CONTRIBUTING.md
├── LICENSE
├── README.md
└── SECURITY.md
```

## Folder responsibilities

| Folder | Responsibility | Source of truth? |
|---|---|---|
| `.github/` | CI, repository policy, issue forms and contribution automation | Yes |
| `assets/` | Brand files and stable preview assets | Yes |
| `data/csv/` | Diff-friendly project reference exports | Companion layer |
| `data/reference/` | Source metadata and structured rule records | Yes |
| `docs/` | Research, methodology, governance and user documentation | Yes |
| `wiki/` | Authoritative version-controlled Wiki Markdown | Yes |
| `excel/` | Workbook binaries and calculation-engine documentation | Yes |
| `notebooks/` | Reproducible formula and data checks | Yes |
| `packages/kaggle/` | Download-friendly publication package | No; generated distribution layer |
| `release/` | Release notes, manifests and packaging records | Yes |
| `tests/` | Formula scenarios and validation fixtures | Yes |

## CSV policy

CSV files are project-specific structured exports. They make key reference tables reviewable and reusable in Python, SQL and BI tools without replacing the workbook.

Required characteristics:

- UTF-8 encoding;
- stable snake_case filenames;
- tax-year suffix where rules are period-specific;
- clear column headers;
- no formulas hidden inside CSV values;
- no personally identifiable payroll or tax-return data;
- source ID and verification status where applicable.

## Wiki architecture

```text
Main repository
└── wiki/                    authoritative and reviewable source

GitHub Wiki repository
└── *.md                     published copy
```

The Wiki source must remain outside `docs/`. The root-level `wiki/` directory is reviewed through normal pull requests and synchronized to the separate `.wiki.git` repository for the GitHub Wiki tab.

## Separation from other projects

This repository must remain independent from all HR analytics, employee datasets and unrelated portfolio projects. Structural ideas may be studied, but files and subject-matter content must never be merged across projects.
