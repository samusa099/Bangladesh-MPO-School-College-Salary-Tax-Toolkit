# Source Register

The workbook uses source IDs to keep salary and tax rules auditable.

## Core source register sheet

```text
SOURCE_REGISTER
```

## Required source fields

| Field | Meaning |
|---|---|
| Source ID | Stable reference ID inside the workbook |
| Authority | Issuing authority |
| Document or page | Source title |
| Published date | Publication date where available |
| Effective date | Date the rule applies from |
| Applicable area | Salary, tax, allowance or deduction area |
| Rule extracted | Short extracted rule note |
| Verification | Research, Beta or Verified status |
| Last checked | Review date |
| URL | Public source location where available |

## Rule

A formula should not be marked Verified unless it is tied to a source ID and effective date.
