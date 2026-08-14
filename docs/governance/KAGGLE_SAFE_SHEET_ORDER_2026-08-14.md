# Kaggle-Safe Sheet Order — 2026-08-14

## Problem

Kaggle Data Explorer displays Excel worksheet names in an alphabetic/Unicode order rather than the visual tab order saved inside the workbook. Bengali-only sheet names caused the workflow tabs to appear out of sequence.

## Decision

Use ASCII numeric prefixes for all public workbook sheet names in the Kaggle-distributed workbook.

## Final v0.1.4 sheet sequence

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

## Rule going forward

For Kaggle-facing Excel workbooks, use sortable sheet names with numeric prefixes. Bengali guidance can remain inside the sheets, but the sheet names themselves should start with ASCII numbers to keep Data Explorer navigation clean.

## Scope

This change is a usability and publishing fix. It does not change salary rules, tax slabs, taxpayer thresholds, source-register values or project verification status.
