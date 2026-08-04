<div align="center">

# 📘 Research Pack 01

## MPO School & College Salary and Tax

**Bangladesh Salary, Tax & Personal Finance Excel Toolkit**

![Status](https://img.shields.io/badge/Status-Beta-orange)
![Tax Year](https://img.shields.io/badge/Tax%20Year-2026%E2%80%9327-blue)
![Sector](https://img.shields.io/badge/Sector-MPO%20School%20%26%20College-green)
![Platform](https://img.shields.io/badge/Platform-Microsoft%20Excel-217346)

</div>

---

## 🏗️ Confirmed Architecture

The project uses a **shared Excel calculation engine** for common salary, tax, validation, and reporting functions.

However, each education authority and sector will maintain its own:

* Rule pack
* Policy source register
* Designation and grade mapping
* Salary-component configuration
* Validation scenarios
* Sector-specific workbook

> [!IMPORTANT]
> School and College, Madrasa, Ebtedayi, and Technical or Vocational institutions will not use a single combined rule table. Each sector will be implemented and validated separately.

---

## ✅ Verified Findings Used in the MVP

### 🏠 House Rent Allowance

For eligible MPO teachers and employees, the current workbook applies the following formula:

```excel
=MAX(Basic_Salary*15%,2000)
```

Or, expressed as a rule:

> **House Rent Allowance = Higher of 15% of Basic Salary or BDT 2,000**

| Component          | Applied Rule                      |
| :----------------- | :-------------------------------- |
| Percentage rate    | 15% of basic salary               |
| Minimum amount     | BDT 2,000                         |
| Workbook treatment | Automatically calculated          |
| Current status     | Working assumption for TY 2026–27 |

> [!NOTE]
> This represents the current School and College MPO package working assumption following source review. It remains subject to final source-by-source legal and policy validation.

---

### 💰 Special Facility

The workbook uses the employee’s comparable national pay-grade input to determine the applicable special-facility rule.

| Comparable Pay Grade     | Special Facility Rule |
| :----------------------- | :-------------------- |
| Grades 1–9               | 10% of basic salary   |
| Grades 10–20             | 15% of basic salary   |
| Minimum for Grades 10–20 | BDT 1,500             |

#### Calculation Logic

```text
Grades 1–9:
Special Facility = Basic Salary × 10%

Grades 10–20:
Special Facility = MAX(Basic Salary × 15%, BDT 1,500)
```

> [!TIP]
> The calculation is grade-driven so that the applicable rate is selected automatically from the employee’s input profile.

---

## 🟡 Confirmed Components with Rate Extraction Pending

The following workflows and policy areas have been confirmed, but their complete rates or calculation rules have not yet been extracted into the final rule table.

| Policy Area                        | Current Research Status                          |
| :--------------------------------- | :----------------------------------------------- |
| Festival allowance                 | Workflow confirmed in DSHE EFT billing           |
| Baishakhi allowance                | Workflow confirmed in DSHE EFT billing           |
| School and College MPO policy      | Identified as the controlling policy catalogue   |
| Madrasa education                  | Separate authority and source documents required |
| Technical and vocational education | Separate authority and source documents required |

### Controlling Policy Catalogue

The **School/College Manpower Structure and MPO Policy 2025** is being treated as the primary policy catalogue for this package.

> [!WARNING]
> Madrasa and technical education institutions operate under separate authorities and policy documents. Their rules must not be copied into the School and College workbook without independent verification.

---

## 🧪 Beta Configuration Items

The following inputs remain deliberately editable during the Beta stage:

| Beta Item                  | Workbook Treatment           |
| :------------------------- | :--------------------------- |
| Medical allowance          | User-editable rate or amount |
| Festival bonus rate        | User-editable                |
| Festival bonus months      | User-editable                |
| Baishakhi allowance rate   | User-editable                |
| Welfare deduction          | User-editable                |
| Retirement deduction       | User-editable                |
| Salary exemptions          | Configurable                 |
| Tax rebate                 | Configurable                 |
| Minimum-tax interpretation | Configurable                 |

> [!CAUTION]
> Editable Beta fields should not be treated as legally verified defaults unless their supporting source is recorded in the workbook’s `SOURCE_REGISTER` sheet.

---

## 🧾 Tax Engine

The workbook includes the project’s current **Tax Year 2026–27** calculation framework, including:

* Taxpayer-category thresholds
* Progressive tax slabs
* Taxable salary calculation
* Exempt-income adjustments
* Investment rebate inputs
* Minimum-tax handling
* Estimated annual tax liability
* Monthly tax allocation
* Validation and warning checks

### Current Status

| Area                         | Status   |
| :--------------------------- | :------- |
| Progressive tax schedule     | Included |
| Taxpayer-category thresholds | Included |
| Salary-income calculation    | Included |
| Exemption mapping            | Beta     |
| Investment rebate            | Beta     |
| Minimum-tax logic            | Beta     |
| Professional tax review      | Pending  |
| Line-by-line legal review    | Pending  |

> [!IMPORTANT]
> The tax engine remains **Beta** until all formulas, thresholds, exemptions, rebates, and minimum-tax provisions have completed line-by-line legal and professional review.

---

## 🔬 Validation Standard

A rule should only be promoted from **Beta** to **Verified** when it has:

1. A traceable primary source.
2. A clearly documented effective date.
3. A defined employee or institution scope.
4. A reproducible Excel formula.
5. At least one positive test case.
6. At least one boundary or exception test.
7. No unresolved conflict with another controlling source.

---

## 🗺️ Next Research Actions

### Priority 1 — Policy Mapping

* [ ] Extract the complete designation catalogue.
* [ ] Map each designation to the applicable pay grade.
* [ ] Extract the corresponding pay-scale information.
* [ ] Identify institution-type and staffing-condition variations.
* [ ] Record policy-page references for every mapping.

### Priority 2 — Salary Components

* [ ] Extract the current medical-allowance rule.
* [ ] Verify welfare-fund deductions.
* [ ] Verify retirement-benefit deductions.
* [ ] Confirm any grade-specific or employee-type exceptions.
* [ ] Reconcile the extracted rules with current EFT and MPO documents.

### Priority 3 — Festival and Baishakhi Allowances

* [ ] Confirm the festival-allowance rate for teachers.
* [ ] Confirm the festival-allowance rate for non-teaching employees.
* [ ] Confirm the number of payable festival months.
* [ ] Extract the current Baishakhi allowance rate.
* [ ] Document eligibility and exclusion conditions.

### Priority 4 — Tax Treatment

* [ ] Map each salary component to the applicable tax-exemption provision.
* [ ] Separate fully taxable, partially exempt, and non-taxable components.
* [ ] Validate the investment-rebate calculation.
* [ ] Confirm minimum-tax applicability by taxpayer category and location.
* [ ] Document all legal references in the source register.

### Priority 5 — Real-World Reconciliation

* [ ] Collect at least ten anonymized official salary rows.
* [ ] Compare workbook-calculated gross salary with official records.
* [ ] Compare deductions and net salary.
* [ ] Investigate all unexplained differences.
* [ ] Record expected-versus-actual results in `TEST_CASES`.

---

## 📊 Minimum Reconciliation Dataset

Each anonymized validation row should contain, where available:

| Required Field       | Purpose                     |
| :------------------- | :-------------------------- |
| Institution type     | Confirms workbook scope     |
| Designation          | Supports grade mapping      |
| Comparable pay grade | Selects rate rules          |
| Basic salary         | Core calculation input      |
| House rent           | Formula validation          |
| Medical allowance    | Rate validation             |
| Special facility     | Grade-rule validation       |
| Festival allowance   | Bonus validation            |
| Baishakhi allowance  | Allowance validation        |
| Welfare deduction    | Deduction validation        |
| Retirement deduction | Deduction validation        |
| Gross salary         | Total reconciliation        |
| Net salary           | Final-output reconciliation |

---

## 🚦Research Status Summary

| Research Area                       |           Status           |
| :---------------------------------- | :------------------------: |
| Shared workbook architecture        |         ✅ Confirmed        |
| Sector-specific rule packs          |         ✅ Confirmed        |
| House-rent working rule             |        ✅ Implemented       |
| Special-facility calculation        |        ✅ Implemented       |
| Festival allowance workflow         | 🟡 Confirmed; rate pending |
| Baishakhi allowance workflow        | 🟡 Confirmed; rate pending |
| Medical allowance                   |           🧪 Beta          |
| Welfare and retirement deductions   |           🧪 Beta          |
| Tax exemption mapping               |           🧪 Beta          |
| Official salary reconciliation      |          ⏳ Pending         |
| Final legal and professional review |          ⏳ Pending         |

---

## ⚠️ Beta Disclaimer

This research pack and its associated workbook are intended for:

* Research
* Education
* Formula testing
* Salary estimation
* Policy reconciliation
* Workbook development

They should not yet be treated as a substitute for:

* Official MPO salary statements
* DSHE or government instructions
* Professional tax advice
* Legal interpretation
* Certified payroll processing

> [!NOTE]
> All verified releases must retain source references, effective dates, validation evidence, and a documented change history.

---

<div align="center">

### 📌 Research Pack 01 Status

**Architecture Confirmed · Core MVP Rules Implemented · Policy Extraction and Validation Ongoing**

</div>
