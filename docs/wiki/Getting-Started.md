# 🚀 Getting Started

Use this guide to open the workbook, enter data safely, review outputs, and complete the minimum validation checks.

> [!CAUTION]
> The workbook is currently **Beta**. Keep a backup before editing and use it for planning, review, and research—not as an official payroll or tax filing document.

## 1. Open the Workbook

```text
excel/school_college/MPO_School_College_Salary_Tax_BD_TY2026_27.xlsx
```

Recommended environment:

| Requirement | Recommendation |
|:--|:--|
| Application | Microsoft Excel |
| Compatibility target | Excel 2019 or later |
| Macros | Not required |
| Editing method | Use highlighted input cells only |

## 2. Begin at `START_HERE`

Review the workbook scope, release status, tax year, user instructions, and limitations before entering information.

## 3. Complete `USER_INPUT`

Enter only the intended input fields:

- Employee and institution information
- Designation and comparable pay grade
- Monthly basic salary
- Allowance assumptions
- Deduction assumptions
- Taxpayer category
- TDS and other annual tax inputs

> [!IMPORTANT]
> Do not overwrite formula cells. Beta assumptions should remain visibly identified and supported by notes in `SOURCE_REGISTER`.

## 4. Review the Main Outputs

| Sheet | Primary output |
|:--|:--|
| `MONTHLY_SALARY` | Monthly gross pay, deductions, and net pay |
| `ANNUAL_SALARY` | Annual salary statement |
| `TAX_CALCULATION` | Progressive annual tax estimate |
| `TAXPAYER_CATEGORIES` | Category-wise threshold comparison |
| `INCOME_EXPENSE` | Expense allocation and savings view |
| `DASHBOARD` | KPI cards and charts |
| `PAYSLIP` | Printable selected-month payslip |
| `TAX_SUMMARY` | Consolidated tax working summary |

## 5. Check the Audit Sheets

| Support sheet | Check |
|:--|:--|
| `SOURCE_REGISTER` | Every verified rule has a source ID and effective date |
| `DATA_DICTIONARY` | Inputs and outputs have clear definitions |
| `TEST_CASES` | Formula tests pass without unexplained differences |

## 6. Perform a Quick Reasonableness Check

Confirm that:

- [ ] Basic salary matches the intended employee profile.
- [ ] Grade-dependent allowances use the correct rule.
- [ ] Gross pay equals total earnings.
- [ ] Net pay equals gross pay minus deductions and TDS.
- [ ] Annual totals reconcile with monthly values.
- [ ] The selected taxpayer category is correct.
- [ ] No formula error is visible.

## 7. Save the File Correctly

Use the approved workbook name:

```text
MPO_School_College_Salary_Tax_BD_TY2026_27.xlsx
```

Do not add words such as `final`, `new`, `copy`, `latest`, or `updated`. See [Asset Naming Convention](Asset-Naming-Convention.md).

---

**Next:** [Workbook Sheet Guide](Workbook-Sheet-Guide.md) · [Formula Methodology](Formula-Methodology.md)
