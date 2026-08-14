# Release Notes — v0.1.4 Kaggle Safe Workbook

## Summary

Rebuilt the workbook as a Kaggle-safe Excel package so Kaggle Data Explorer displays worksheets in the correct workflow order.

## Why this release exists

Kaggle Data Explorer sorts Excel sheets alphabetically/Unicode-style instead of following the workbook tab order. Bengali-only sheet names such as `আয়কর`, `ইনপুট`, and `১. শুরু` appeared out of the intended workflow order.

## Main fix

The workbook now uses ASCII-numbered sheet names:

```text
01_Start
02_Dashboard
03_NBR_Form
04_Return_History
05_Salary_2026
06_Income_TDS_Expense
07_Assets
08_Next_Year
09_Input
10_Taxpayer_Categories
11_Tax_Calculation
12_Annual_Salary
13_Payslip
14_Tax_Summary
15_Source_Register
16_Data_Dictionary
17_Test_Cases
18_Project_Charter
19_Sector_Rules
```

## Included workbook areas

- Start/navigation sheet
- Dashboard
- NBR return mapping
- Return history
- Monthly salary calculation
- Income, TDS and expense summary
- Asset and investment planning
- Next-year carry-forward tracking
- User input sheet
- Taxpayer category comparison
- Tax calculation
- Annual salary statement
- Payslip
- Tax summary
- Source register
- Data dictionary
- Validation cases
- Project charter
- Sector rules

## Validation

Formula error scan completed with no detected:

```text
#REF!
#DIV/0!
#VALUE!
#NAME?
#N/A
```

## Status

Beta. This workbook is for planning, learning and portfolio demonstration. It must be reviewed against official sources and professional advice before payroll submission, tax filing or financial decision-making.
