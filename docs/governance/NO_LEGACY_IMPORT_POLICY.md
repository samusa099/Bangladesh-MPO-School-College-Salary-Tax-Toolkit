# No Legacy Import Policy

## Purpose

This policy prevents accidental carryover from older portfolio repositories into the Bangladesh MPO School & College Salary Tax Toolkit.

## Allowed reuse

The project may reuse general organization patterns, such as:

- clear folder structure;
- source register discipline;
- validation cases;
- release notes;
- branch and pull-request governance;
- privacy and security checks;
- GitHub engineering vs Kaggle distribution separation.

## Not allowed

Do not import or preserve content from unrelated projects, including:

- HR turnover analytics datasets;
- ecommerce project content;
- Power BI assessment project content;
- unrelated organization names;
- employee records;
- applicant or HR analytics records;
- unrelated screenshots or previews;
- unrelated CSV dictionaries;
- unrelated README text.

## Required rewrite rule

Every file in this repository must answer this question:

> Does this file directly support the MPO School & College salary, tax, payslip, dashboard, validation, release or documentation workflow?

If the answer is no, the file does not belong here.

## Review checklist

Before merging any future import or generated package:

- Search for old repository names.
- Search for unrelated business domains.
- Check screenshots and preview assets.
- Check CSV headers and dictionaries.
- Check README, wiki and release notes.
- Confirm paths match the repository structure.
- Confirm no personal or real payroll data is included.

## Correct location rule

| Content | Correct location |
|---|---|
| Main workbook | `excel/school_college/` |
| Wiki source | `wiki/` |
| Governance docs | `docs/governance/` |
| Research docs | `docs/research/` |
| User guides | `docs/user-guides/` |
| Kaggle package | `packages/kaggle/` |
| Validation cases | `tests/` |
| Preview assets | `assets/previews/` |
| Brand assets | `assets/brand/` |
