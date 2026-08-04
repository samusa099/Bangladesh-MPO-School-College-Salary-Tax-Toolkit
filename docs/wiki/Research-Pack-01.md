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

The project uses a shared Excel calculation engine for common salary, tax, validation, and reporting functions. Each education authority and sector maintains a separate rule pack, source register, designation mapping, validation set, and workbook.

> [!IMPORTANT]
> School and College, Madrasa, Ebtedayi, and Technical or Vocational institutions must not share one combined rule table without independent source verification.

## ✅ Verified MVP Findings

### 🏠 House Rent Allowance

```excel
=MAX(Basic_Salary*15%,2000)
```

**Applied rule:** the higher of 15% of basic salary or BDT 2,000.

### 💰 Special Facility

| Comparable pay grade | Applied rule |
|:--|:--|
| Grades 1–9 | 10% of basic salary |
| Grades 10–20 | 15% of basic salary, minimum BDT 1,500 |

```text
Grades 1–9: Basic Salary × 10%
Grades 10–20: MAX(Basic Salary × 15%, BDT 1,500)
```

## 🟡 Confirmed, Rate Extraction Pending

- Festival allowance workflow exists in DSHE EFT billing.
- Baishakhi allowance workflow exists in DSHE EFT billing.
- The School/College Manpower Structure and MPO Policy 2025 is the controlling policy catalogue for this package.
- Madrasa and technical education require separate authority documents and rule tables.

## 🧪 Editable Beta Items

- Medical allowance
- Festival bonus rate and payable months
- Baishakhi allowance rate
- Welfare and retirement deductions
- Salary exemptions
- Tax rebate
- Minimum-tax interpretation

> [!CAUTION]
> Editable Beta fields are not legally verified defaults unless their supporting source is recorded in `SOURCE_REGISTER`.

## 🧾 Tax Engine

The workbook contains the project’s current Tax Year 2026–27 progressive schedule and category thresholds, including taxable salary, exemptions, rebate inputs, minimum-tax handling, estimated annual liability, and monthly allocation.

> [!IMPORTANT]
> The tax engine remains Beta until formulas, thresholds, exemptions, rebates, and minimum-tax provisions complete line-by-line legal and professional review.

## 🔬 Verification Standard

A rule may be promoted from Beta to Verified only when it has:

1. A traceable primary source and effective date.
2. A defined employee or institution scope.
3. A reproducible Excel formula.
4. Positive, boundary, and exception tests.
5. No unresolved conflict with another controlling source.
6. Reconciliation evidence where official rows are available.

## 🗺️ Next Research Actions

- [ ] Extract complete designation, grade, and pay-scale mappings from the 2025 School/College MPO policy.
- [ ] Extract current medical allowance, welfare, and retirement deduction rules.
- [ ] Confirm teacher and employee festival allowance rates and payable months.
- [ ] Confirm the Baishakhi allowance rate and eligibility conditions.
- [ ] Map every salary component to the applicable tax-exemption provision.
- [ ] Validate investment rebate and minimum-tax treatment.
- [ ] Reconcile at least ten anonymized official salary rows.
- [ ] Record expected-versus-actual results in `TEST_CASES`.

## 📊 Minimum Reconciliation Fields

| Field | Validation purpose |
|:--|:--|
| Institution type and designation | Confirms scope and grade mapping |
| Comparable pay grade and basic salary | Selects and tests calculation rules |
| House rent, medical and special facility | Validates allowance formulas |
| Festival and Baishakhi allowances | Validates bonus rules |
| Welfare and retirement deductions | Validates deductions |
| Gross and net salary | Completes end-to-end reconciliation |

## ⚠️ Beta Disclaimer

This research pack supports research, education, formula testing, salary estimation, policy reconciliation, and workbook development. It is not a substitute for official MPO statements, government instructions, professional tax advice, legal interpretation, or certified payroll processing.

---

## 🧭 Wiki Navigation

[🏠 Home](Home.md) · [📚 Full Wiki Index](Final-Wiki-Index.md) · [🧮 Formula Methodology](Formula-Methodology.md) · [✅ Validation Gates](Validation-and-Release-Gates.md)
