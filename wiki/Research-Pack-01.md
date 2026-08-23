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

## 🧮 Implemented Working Rules — Source Mapping Still Required

The workbook currently implements the following rules, but they must not be described as legally **Verified** until an authoritative effective-period source is mapped to the actual workbook formula and tested.

### 🏠 House Rent Allowance

```excel
=MAX(Basic_Salary*15%,2000)
```

**Current workbook rule:** the higher of 15% of basic salary or BDT 2,000.  
**Evidence status:** source mapping for the applicable School/College period remains pending.

### 💰 Special Facility

| Comparable pay grade | Current workbook rule | Evidence status |
|:--|:--|:--|
| Grades 1–9 | 10% of basic salary | Source mapping pending |
| Grades 10–20 | 15% of basic salary, minimum BDT 1,500 | Source mapping pending |

```text
Grades 1–9: Basic Salary × 10%
Grades 10–20: MAX(Basic Salary × 15%, BDT 1,500)
```

## 📚 Source Extraction Progress

### ✅ Primary authority identified or rate source extracted

- **Taxpayer thresholds:** current NBR source targets for TY 2026–27 have been reconciled in `Taxpayer-Categories.md` and `docs/research/TAX_THRESHOLD_RECONCILIATION_2026-08-23.md`; workbook implementation remains pending restoration/QA.
- **Baishakhi allowance:** SHED's 2018 order states a **20%** Baishakhi allowance for MPO School/College teachers and employees. A DSHE April 2026 notice independently confirms the allowance remained an active MPO billing workflow. A supersession check is still required before public formula verification.
- **Retirement Benefit deduction:** the Retirement Benefit Board states that **6%** is deducted/saved from MPO for retirement benefits and exposes the 6% deduction gazette in its official law/rules catalogue.
- **Welfare Trust deduction:** the Welfare Trust's official regulations page publishes the **4% contribution-deduction notification**.
- **School/College policy catalogue:** SHED's School & College Manpower Structure and MPO Policy 2025 is the current controlling policy catalogue identified for this package; rule-by-rule extraction and 2026 amendment mapping remain in progress.

### 🟡 Corroborated but primary order still to archive

- **Festival allowance:** May 2025 reporting consistently quotes the Finance Division decision increasing MPO teachers' festival allowance from 25% to **50%** of one month's government-share basic salary while employees remain at **50%**. DSHE's 2026 Eid bill-submission notices confirm the workflow remains active. The original Finance Division/administrative ministry order still needs to be archived as the primary source before this rate is promoted to Verified in the workbook.

### ⏳ Still pending

- Current medical-allowance authority and amount.
- Authoritative source mapping for the workbook's house-rent rule.
- MPO-specific authoritative source mapping for the workbook's special-facility rules.
- Festival payable-month/eligibility details from the primary order.
- Complete salary-component tax-treatment mapping.
- Any 2025 policy / 2026 amendment exceptions affecting employee class, grade, institution type, or effective date.

## 🧪 Editable / Unverified Workbook Items

Until the restored workbook is mapped and tested, these items must remain Beta or explicitly source-pending rather than being treated as final legal defaults:

- Medical allowance
- Festival bonus rate and payable months
- Baishakhi allowance implementation
- Welfare and retirement deduction implementation/base
- House-rent implementation
- Special-facility implementation
- Salary exemptions
- Tax rebate
- Minimum-tax interpretation

> [!CAUTION]
> A source can verify that a rule exists without proving that the current workbook binary implements the rule correctly. Workbook verification requires source mapping plus formula and boundary testing.

## 🧾 Tax Engine

The workbook contains the project's current Tax Year 2026–27 calculation framework. The public/reference threshold layer was corrected against current NBR evidence in PR #54, but the canonical workbook binary is still pending restoration and formula QA.

> [!IMPORTANT]
> The tax engine remains Beta until formulas, thresholds, exemptions, rebates, and minimum-tax provisions complete workbook testing plus line-by-line legal and professional review.

## 🔬 Verification Standard

A rule may be promoted from Beta to Verified only when it has:

1. A traceable primary source and effective date.
2. A defined employee or institution scope.
3. A documented mapping to the workbook field/formula.
4. A reproducible Excel formula.
5. Positive, boundary, and exception tests.
6. No unresolved conflict with another controlling source.
7. Reconciliation evidence where official rows are available.

## 🗺️ Next Research Actions

- [ ] Extract complete designation, grade, pay-scale, and exception mappings from the 2025 School/College MPO policy and its 2026 amendments.
- [ ] Extract the current medical-allowance authority and amount.
- [ ] Find/archive the primary effective-period authority for the current house-rent workbook formula.
- [ ] Find/archive the MPO-specific authority for the special-facility grade rules.
- [ ] Archive the original 2025 Finance Division/administrative order for the festival-allowance increase and confirm payable-month/eligibility details.
- [ ] Check for any later source superseding the 2018 20% Baishakhi rate.
- [ ] Map the 6% Retirement Benefit and 4% Welfare Trust authorities to the restored workbook's exact deduction base/formulas.
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
