# Tests and Verification Evidence

This folder is the home for reproducible test execution and verification evidence.

## Current scenario catalog

The repository already contains `data/csv/04_validation_scenarios_ty2026_27.csv`. That file is a **scenario catalog**, not proof that every scenario has been executed successfully.

## Release gate

A Verified release requires evidence for at least 20–30 deterministic scenarios covering salary calculations, annual aggregation, taxpayer categories, tax boundaries, minimum-tax interactions and formula/reference integrity.

Each executed case should record:

- scenario ID;
- fixed inputs;
- independently derived expected result;
- workbook result;
- difference;
- pass/fail status;
- evidence/source reference.

Official salary reconciliation evidence should remain anonymized and must not expose personal identifiers or banking data.
