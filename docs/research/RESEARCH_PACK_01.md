# Research Pack 01 — MPO School & College Salary and Tax

## Confirmed architecture
A shared Excel calculation engine will be reused, but every authority/sector will have a separate rule pack and workbook.

## Verified findings used in the MVP

### House rent
For eligible MPO teachers and employees, the workbook applies:

`MAX(Basic × 15%, BDT 2,000)`

This reflects the School/College MPO package’s current TY 2026–27 working assumption after source review.

### Special facility
The workbook uses the employee’s pay-grade input to select the correct rule:

- Comparable national pay grades 1–9: 10% of basic salary
- Grades 10–20: 15% of basic salary, but not less than BDT 1,500

## Confirmed but rate extraction pending
- Festival allowance workflow exists in DSHE EFT billing.
- Baishakhi allowance workflow exists in DSHE EFT billing.
- School/College Manpower Structure and MPO Policy 2025 is the controlling policy catalogue for this package.
- Madrasa and technical education use separate authorities and documents; they will not share this workbook’s rule table.

## Beta items
The following are deliberately editable:

- Medical allowance
- Festival bonus rate and months
- Baishakhi rate
- Welfare and retirement deductions
- Salary exemptions
- Tax rebate
- Minimum-tax interpretation

## Tax engine
The workbook contains the project’s current 2026–27 progressive tax schedule and category thresholds. The workbook remains Beta until a line-by-line legal and professional review is completed.

## Next research actions
1. Extract complete designation, grade and pay-scale mapping from the 2025 School/College MPO policy.
2. Extract medical allowance and deduction rules from current EFT/MPO source documents.
3. Confirm teacher vs employee festival allowance rates.
4. Map salary components to tax exemption provisions.
5. Reconcile at least ten anonymized official salary rows.
