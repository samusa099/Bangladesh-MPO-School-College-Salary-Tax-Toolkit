# Validation and Release Gates

The workbook is currently **Beta**.

## Status labels

| Status | Meaning |
|---|---|
| Research | Source collection and interpretation are incomplete |
| Draft | Structure exists but formulas are not ready |
| Beta | Usable for planning and review |
| Verified | Source-linked, tested, reconciled and reviewed |
| Deprecated | Replaced by a newer tax year or policy version |

## Required gates before Verified release

| Gate | Requirement |
|---|---|
| Formula tests | 20-30 deterministic cases |
| Official reconciliation | At least 10 anonymized official salary rows |
| Source linkage | Every verified rule has source ID and effective date |
| Formula protection | Formula cells protected before public release |
| Excel compatibility | Excel 2019-compatible core formulas |
| Macro policy | No VBA in v1 |
| Practitioner review | MPO/payroll review and tax review |
| Tax-year integrity | Previous tax-year files are not overwritten |

## Validation areas

- salary component addition;
- gross pay and net pay reconciliation;
- allowance calculations;
- deduction calculations;
- tax slab boundary cases;
- taxpayer category thresholds;
- minimum tax;
- TDS comparison;
- annual and monthly consistency.
