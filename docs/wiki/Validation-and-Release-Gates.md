# Validation and Release Gates

The workbook is currently **Beta**.

A workbook should not be marked `Verified` until it passes the project release gates.

## Release status labels

| Status | Meaning |
|---|---|
| Research | Source collection and interpretation are still incomplete |
| Draft | Structure exists, but formulas are not ready for public use |
| Beta | Usable for planning, but review and reconciliation remain incomplete |
| Verified | Source-linked, tested, reconciled and practitioner-reviewed |
| Deprecated | Superseded by a newer tax year or policy version |

## Required gates before Verified release

| Gate | Requirement |
|---|---|
| Formula tests | 20–30 deterministic cases |
| Official reconciliation | At least 10 anonymized official salary rows |
| Source linkage | Every verified rule must have source ID and effective date |
| Formula protection | Formula cells protected before public release |
| Excel compatibility | Excel 2019-compatible core formulas |
| Macro policy | No VBA in v1 |
| Practitioner review | MPO/payroll practitioner + tax practitioner review |
| Tax-year integrity | Previous tax-year releases must not be overwritten |

## Validation areas

- salary component addition;
- gross pay and net pay reconciliation;
- allowance calculations;
- deduction calculations;
- tax slab boundary cases;
- taxpayer category thresholds;
- minimum tax;
- TDS comparison;
- zero/blank/invalid input handling;
- annual summary and monthly sheet consistency.

## Public disclaimer

The workbook provides education and planning estimates. It is not an official salary bill, tax assessment, legal opinion or professional filing tool.
