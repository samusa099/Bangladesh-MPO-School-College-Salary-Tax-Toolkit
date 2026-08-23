# ❓ Frequently Asked Questions

## Is this an official MPO salary bill?

No. This is an open-source Excel planning, research, and validation toolkit. Official salary statements and authority instructions remain controlling.

## Can the workbook file a tax return?

No. It prepares a working estimate and summary only. A taxpayer must verify the applicable law, evidence, exemptions, rebates, minimum tax, and filing requirements.

## Why does the package cover only School and College?

School and College, Madrasa, Ebtedayi, and Technical or Vocational education operate under different authorities and source documents. Their rule tables must remain separate.

## Why are some values editable?

Some rates and interpretations still require complete source extraction or professional review. These fields remain visibly marked as Beta or user-configurable.

## Which cells should users edit?

Only highlighted or explicitly designated input cells. Formula, lookup, validation, and output cells should not be overwritten.

## Why is there no VBA?

Version 1 avoids VBA to improve transparency, compatibility, auditability, and user safety.

## What Excel version is supported?

Core formulas target Microsoft Excel 2019 or later. Compatibility should be checked before every public release.

## Why are GitHub and Kaggle packages different?

GitHub contains engineering, research, validation, governance, and release history. Kaggle contains a curated public download package.

## How should the workbook be named?

```text
MPO_School_College_Salary_Tax_BD_TY2026_27.xlsx
```

Do not add `final`, `new`, `copy`, `latest`, or `updated`.

## What is required before a Verified release?

- Source-linked rules with effective dates
- 20–30 deterministic test cases
- At least 10 anonymized official salary reconciliations
- Formula protection
- Excel compatibility checks
- MPO or payroll practitioner review
- Tax practitioner review
- Complete release notes and naming compliance

## What should I do when a result looks wrong?

1. Recheck `USER_INPUT`.
2. Confirm the applicable grade and taxpayer category.
3. Trace the result through `SECTOR_RULES` and the calculation sheets.
4. Review the source ID in `SOURCE_REGISTER`.
5. Reproduce the case in `TEST_CASES`.
6. Report the issue with anonymized inputs, expected result, actual result, and workbook version.

## Can a previous tax-year workbook be overwritten?

No. Each tax year must remain a separate, traceable asset.

---

**Need a guided workflow?** Start with [Getting Started](Getting-Started.md) or review [Validation and Release Gates](Validation-and-Release-Gates.md).
