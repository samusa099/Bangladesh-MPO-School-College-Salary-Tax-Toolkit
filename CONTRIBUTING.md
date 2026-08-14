# Contributing

Thank you for improving the Bangladesh MPO School & College Salary Tax Toolkit.

## Scope

Contributions should stay inside this repository's School & College MPO salary/tax scope. Do not import unrelated HR analytics, personal-finance workbooks, private tax-return data or files from other projects.

## Before changing formulas or rules

- identify the affected workbook component;
- cite the competent official source or documented evidence;
- record the effective date / Tax Year;
- explain any interpretation or unresolved ambiguity;
- add or update a deterministic regression scenario.

## Data and privacy

Never commit real TIN/NID values, bank-account information, credentials, private salary statements, identifiable employee records or completed personal tax returns. Use synthetic/anonymized examples where evidence is required.

## File discipline

Use stable professional filenames. Avoid temporary names such as `final`, `copy`, `latest`, `new`, `(1)` or ad-hoc backups. Keep engineering material in GitHub workspace folders and curated distribution files under `packages/kaggle/`.

## Pull requests

1. Create a focused branch.
2. Keep each PR limited to one coherent change set.
3. Update documentation and evidence when behavior changes.
4. Run applicable repository/workbook validation.
5. Do not mark Beta gates complete without reproducible evidence.

## Release changes

Public version identifiers must follow `docs/governance/RELEASE_VERSION_POLICY.md`. The Git tag, GitHub Release, README, Wiki and distribution metadata should agree before publication.
