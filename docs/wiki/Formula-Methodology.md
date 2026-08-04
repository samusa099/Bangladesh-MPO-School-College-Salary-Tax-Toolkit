# Formula Methodology

## Architecture

The project follows this calculation architecture:

```text
Shared calculation engine
        ↓
Sector rule pack
        ↓
Institution-specific workbook
```

## Current sector

The current workbook covers only:

```text
MPO School & College
```

Madrasa, Ebtedayi, Technical/Vocational, government, private and business-tax domains must not be mixed into this workbook.

## Salary calculation flow

```text
Basic Salary
+ House Rent
+ Medical Allowance
+ Other Allowance
+ Special Facility
+ Festival Bonus
+ Baishakhi Allowance
+ Arrear
= Gross Pay

Gross Pay
- Welfare Deduction
- Retirement Deduction
- Other Deduction
- TDS
= Net Pay
```

## Verified formulas in this MVP

### House rent

```text
MAX(Basic × 15%, BDT 2,000)
```

### Special facility

```text
Grade 1–9: Basic × 10%
Grade 10–20: MAX(Basic × 15%, BDT 1,500)
```

## Tax calculation flow

```text
Annual Gross Salary
- Verified Salary Exemption
+ Other Annual Taxable Income
= Total Taxable Income

Total Taxable Income
- Applicable Category Threshold
- Disabled Dependent Adjustment
= Income Above Threshold

Income Above Threshold
→ Progressive slab calculation
→ Tax before rebate
→ Tax after verified rebate
→ Minimum tax comparison
→ Estimated tax liability
```

## Beta assumptions

These values are intentionally editable until fully verified:

- medical allowance;
- festival bonus rate;
- Baishakhi allowance rate;
- welfare deduction;
- retirement deduction;
- salary exemptions;
- tax rebate;
- institution-specific deduction variations.

## Source rule

A formula can be marked `Verified` only when it has:

1. authority;
2. document title;
3. extracted rule;
4. effective date;
5. source ID;
6. workbook mapping.
