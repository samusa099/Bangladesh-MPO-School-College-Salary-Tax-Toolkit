# Project Alignment Audit — 2026-08-05

## Repository

`samusa099/Bangladesh-MPO-School-College-Salary-Tax-Toolkit`

## Audit purpose

This audit records the project-specific cleanup required after importing structure and governance patterns from earlier portfolio repositories. The goal is to keep this repository focused on the Bangladesh MPO School & College Salary Tax Toolkit and prevent unrelated project content or conflicting documentation paths from returning.

## Current confirmed scope

- Product: Bangladesh MPO School & College Salary Tax Toolkit
- Tax year: 2026–27
- Current status: Beta
- Main workbook path: `excel/school_college/MPO_School_College_Salary_Tax_BD_TY2026_27.xlsx`
- Wiki source of truth: `wiki/`
- Kaggle package workspace: `packages/kaggle/`

## Findings

### 1. Wiki source path mismatch

The repository had conflicting documentation about the authoritative Wiki source.

- `README.md` pointed readers to `docs/wiki/`.
- `docs/REPOSITORY_STRUCTURE.md` defines root-level `wiki/` as the authoritative version-controlled Wiki source.
- `.github/workflows/publish-wiki.yml` validates and publishes `wiki/**`.

### Action taken

`README.md` has been corrected to consistently use `wiki/` as the authoritative Wiki source.

### 2. Imported-pattern risk

The repository uses organizational ideas from earlier analytics repositories. That is acceptable only when the actual files, names, datasets and business context are fully rewritten for this MPO salary-tax project.

### Control

No unrelated HR analytics, employee-turnover, ecommerce, BI-assessment or legacy organization content should be committed. Structural ideas may be reused; subject-matter content must not be reused.

### 3. Duplicate documentation risk

A duplicate Wiki source under `docs/wiki/` can confuse contributors and automation.

### Control

Use only root-level `wiki/` for GitHub Wiki source. Keep `docs/` for governance, research and user guides.

### 4. Binary asset status

Workbook and image assets should be committed only under stable project paths.

Allowed paths:

```text
excel/school_college/MPO_School_College_Salary_Tax_BD_TY2026_27.xlsx
assets/brand/github-cover.svg
assets/previews/cover-banner.jpg
assets/previews/project-icon.jpg
assets/previews/social-preview.jpg
assets/previews/dashboard-preview.jpg
```

Avoid temporary names such as `final`, `copy`, `new`, `latest`, or `updated`.

## Preventive rules

1. Keep School/College MPO scope strict in this repository.
2. Keep Madrasa, Ebtedayi and Technical/Vocational payroll in future separate packages.
3. Keep VAT, TDS, LC, import-export and company tax outside this repository.
4. Do not add real payroll, bank, tax or NID data.
5. Every verified formula must link to a source ID and effective date.
6. Every new workbook release must update changelog, wiki, validation cases and release notes.
7. Use `wiki/` as the single Wiki source path.
8. Use `packages/kaggle/` only as distribution workspace, not the engineering source of truth.

## Next recommended cleanup

- Remove or archive any remaining duplicate `docs/wiki/` content if present.
- Ensure all README links point to existing files.
- Run repository policy validation after binary workbook upload.
- Confirm Wiki publisher skips gracefully when `WIKI_TOKEN` is unavailable.
- Open a follow-up issue for the workbook binary and preview asset upload if they are not present.
