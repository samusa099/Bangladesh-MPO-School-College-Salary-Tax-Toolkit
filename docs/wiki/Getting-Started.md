# Getting Started

## 1. Download the workbook

Use the workbook stored at:

```text
excel/school_college/MPO_School_College_Salary_Tax_BD_TY2026_27.xlsx
```

For Kaggle distribution, use the clean package version under:

```text
kaggle_distribution/BD_MPO_Salary_Tax_Excel_Package/
```

## 2. Open in Excel

Recommended target: **Microsoft Excel 2019 or later**.

The project avoids VBA in v1, so normal Excel formulas and charts should work without enabling macros.

## 3. Start from `START_HERE`

Read the scope, status and warning notes first.

## 4. Enter data in `USER_INPUT`

Only edit the highlighted input cells. Typical inputs include:

- tax year;
- institution name;
- employee name;
- designation;
- national pay grade;
- taxpayer category;
- monthly basic salary;
- increment settings;
- allowance and deduction assumptions;
- TDS and other tax inputs.

## 5. Review results

Use these sheets for outputs:

| Sheet | Output |
|---|---|
| `MONTHLY_SALARY` | Month-by-month salary calculation |
| `ANNUAL_SALARY` | Annual salary statement |
| `TAX_CALCULATION` | Estimated tax liability |
| `TAXPAYER_CATEGORIES` | Category-wise tax variation |
| `INCOME_EXPENSE` | Personal finance allocation |
| `DASHBOARD` | KPI and chart summary |
| `PAYSLIP` | Printable payslip view |
| `TAX_SUMMARY` | Tax-return working summary |

## 6. Check source and status

Before relying on any result, check:

- `SOURCE_REGISTER`
- `DATA_DICTIONARY`
- `TEST_CASES`

## 7. Beta warning

The workbook is still Beta. Verified public release requires formula tests, official-row reconciliation and practitioner review.
