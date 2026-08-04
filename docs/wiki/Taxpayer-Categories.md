# Taxpayer Categories

The v0.1.2 workbook includes a `TAXPAYER_CATEGORIES` sheet.

## Threshold comparison

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

## Key note

Female status and age 65+ use the same BDT 450,000 threshold. They are not added together.

## Workbook input

The category is selected in:

```text
USER_INPUT!B13
```

The tax calculation uses that category to calculate the base threshold, income above threshold, slab tax and estimated tax.
