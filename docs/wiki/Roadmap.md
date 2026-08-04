# 🗺️ Product Roadmap

The roadmap prioritizes rule accuracy, reconciliation, release quality, and sector separation before broader expansion.

## Current Release Line — `v0.1.x` Beta

- [x] School and College workbook MVP
- [x] Taxpayer-category comparison sheet
- [x] Dashboard and payslip views
- [x] Source register and data dictionary
- [x] Initial validation cases
- [x] GitHub and Kaggle structure
- [x] Wiki documentation
- [ ] Complete all Beta rule extraction

## `v0.2.0` — Formula Hardening

- [ ] Complete designation, grade, and pay-scale mapping
- [ ] Confirm medical allowance rules
- [ ] Confirm welfare and retirement deductions
- [ ] Confirm festival and Baishakhi allowance rates
- [ ] Map salary components to tax treatment
- [ ] Expand boundary and exception testing
- [ ] Protect formula cells

## `v0.3.0` — Reconciliation Release

- [ ] Reconcile at least 10 anonymized official salary rows
- [ ] Publish a reconciliation report
- [ ] Resolve unexplained gross and net salary variances
- [ ] Add workbook QA checklist
- [ ] Improve dashboard accessibility and print layout

## `v1.0.0` — Verified Release

Release only after all gates are complete:

| Gate | Target |
|:--|:--|
| Source-linked rule table | Complete |
| Deterministic tests | 20–30 passing |
| Official reconciliations | At least 10 |
| MPO/payroll review | Complete |
| Tax practitioner review | Complete |
| VBA | None |
| Core formula compatibility | Excel 2019 or later |
| Formula protection | Enabled |

> [!IMPORTANT]
> The project will not label a release Verified solely because the workbook opens or produces outputs. Verification requires source, test, reconciliation, and review evidence.

## Future Sector Packages

Each package will use a separate authority-specific rule pack and workbook:

- MPO Madrasa salary and tax toolkit
- Independent Ebtedayi salary and tax toolkit
- Technical or Vocational MPO salary and tax toolkit
- Government and autonomous salary toolkit
- Private and NGO salary toolkit
- Individual tax and personal finance toolkit
- Small-business income and tax toolkit
- VAT and TDS toolkit
- Import-export and LC toolkit
- Company tax toolkit

## Long-Term Platform Direction

```text
Shared calculation standards
        +
Authority-specific rule packs
        +
Tax-year-specific workbooks
        +
Automated validation and release controls
```

---

**Related pages:** [Validation and Release Gates](Validation-and-Release-Gates.md) · [GitHub and Kaggle Publishing](GitHub-and-Kaggle-Publishing.md)
