# Security and Privacy Policy

This repository contains salary, tax, and personal-finance workbook tooling. Public examples must be synthetic or properly anonymized.

## Data restrictions

Do not commit:

- NID, TIN, bank account, EFT, tax-portal, or payroll credentials;
- identifiable employee, taxpayer, medical, banking, or salary records;
- private keys, API tokens, environment files, or service-account files;
- VBA macros, ActiveX controls, embedded executables, or undocumented external links.

No VBA macros are permitted in v1. External links must point only to documented public sources.

## Report a vulnerability privately

Use GitHub private vulnerability reporting from the repository **Security** tab when available. Do not publish credentials, personal data, or exploit details in a public issue.

## Security scope

Please report:

- exposed credentials, tokens, or private keys;
- real employee, taxpayer, payroll, health, or banking data;
- malicious formulas, macros, embedded objects, or unsafe external links;
- path traversal or unsafe XLSX/archive handling;
- CSV spreadsheet-formula injection;
- vulnerable GitHub Actions or excessive workflow permissions;
- dependency or release-supply-chain risks.

## Existing controls

- read-only workflow permissions by default;
- immutable GitHub Action references;
- automated secret scanning;
- passive XLSX structure and archive validation;
- CSV formula-injection checks;
- Dependabot maintenance for GitHub Actions;
- pull-request dependency review.

Formula, workbook, archive, and source-link validation are required before release. Security and privacy fixes are applied to the latest version on `main`.
