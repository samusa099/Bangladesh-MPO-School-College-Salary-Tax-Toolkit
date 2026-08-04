# Formula Methodology

## Architecture

```text
Shared calculation engine
        ↓
Sector rule pack
        ↓
Institution-specific workbook
```

## Salary flow

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

## Verified formulas in the MVP

### House rent

```text
MAX(Basic × 15%, BDT 2,000)
```

### Special facility

```text
Grade 1-9: Basic × 10%
Grade 10-20: MAX(Basic × 15%, BDT 1,500)
```

## Tax flow

```text
Annual Gross Salary
- Verified Salary Exemption
+ Other Annual Taxable Income
= Total Taxable Income

Total Taxable Income
- Applicable Category Threshold
= Income Above Threshold
```

The income above threshold is then passed through progressive tax slabs and minimum-tax comparison.
