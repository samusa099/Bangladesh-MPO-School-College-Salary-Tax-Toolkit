# Taxpayer Categories

The v0.1.2 workbook adds a dedicated `TAXPAYER_CATEGORIES` sheet for male, female and special taxpayer category variation.

## Category table

| Category | Tax-free threshold |
|---|---:|
| General male below 65 | BDT 400,000 |
| Female taxpayer | BDT 450,000 |
| Male taxpayer aged 65+ | BDT 450,000 |
| Female taxpayer aged 65+ | BDT 450,000 |
| Third-gender taxpayer | BDT 525,000 |
| Person with disability | BDT 525,000 |
| Gazetted wounded freedom fighter | BDT 550,000 |
| Gazetted July fighter | BDT 550,000 |

## Important rule

Female status and age 65+ do **not** combine into a doubled threshold. A female taxpayer aged 65+ still uses the BDT 450,000 threshold unless another higher special category applies.

## Disabled dependent adjustment

A taxpayer may receive an additional threshold for an eligible child or dependent person with disability.

Workbook input:

```text
USER_INPUT!B45
```

Important condition: where both parents are taxpayers, the same dependent should not be claimed by both taxpayers.

## Minimum tax

When taxable income exceeds the applicable threshold:

| Taxpayer type | Minimum tax |
|---|---:|
| Regular taxpayer | BDT 5,000 |
| New taxpayer | BDT 1,000 |

## Workbook mapping

The selected taxpayer category is entered in:

```text
USER_INPUT!B13
```

The tax engine uses that selection to calculate:

- base tax-free threshold;
- additional dependent threshold;
- slab tax;
- minimum tax;
- estimated tax liability.

## Status

The category structure is source-linked in `SOURCE_REGISTER` as `SRC-001`. The workbook remains Beta until final professional review.
