# Tax Threshold Reconciliation — 2026-08-23

## Finding

A source-year mismatch was found while reviewing issue #39.

The repository's previous Tax Year 2026–27 working table used:

- General taxpayer: BDT 400,000
- Female taxpayer / taxpayer aged 65+: BDT 450,000
- Third-gender taxpayer / taxpayer with disability: BDT 525,000
- Gazette-listed wounded freedom fighter / July fighter: BDT 550,000

The National Board of Revenue's **2026 Budget Speech**, Appendix B, Table 1, instead identifies the following thresholds for **Tax Years 2026–27 and 2027–28**:

- General taxpayer: **BDT 375,000**
- Female taxpayer / taxpayer aged 65+: **BDT 425,000**
- Third-gender taxpayer / taxpayer with disability: **BDT 500,000**
- Gazette-listed wounded freedom fighter / Gazette-listed injured July Warrior: **BDT 525,000**
- Eligible parent/legal guardian of a dependent with disability: **additional BDT 50,000**

The same current budget material places the BDT 400,000 / 450,000 / 525,000 / 550,000 sequence in later tax years. This strongly indicates that the repository's prior TY 2026–27 table was shifted forward by tax year.

## Primary evidence

1. National Board of Revenue — **Budget Speech 2026**, Appendix B, Table 1:  
   <https://nbr.gov.bd/uploads/budget/Budget_Speech_English.pdf>
2. National Board of Revenue — **Finance Acts** catalogue; Finance Act, 2026 is listed with date 06 July 2026:  
   <https://nbr.gov.bd/regulations/acts/finance-acts>
3. NBR budget annex published with the prior budget cycle, independently showing the same BDT 375,000 / 425,000 / 500,000 / 525,000 thresholds for the corresponding 2026–27/2027–28 period:  
   <https://nbr.gov.bd/uploads/budget/English.pdf>

## Repository action taken

- `wiki/Taxpayer-Categories.md` now records the NBR source-target values and explicitly states that workbook reconciliation remains pending.
- `data/csv/01_taxpayer_categories_ty2026_27.csv` now uses the same source-target values and no longer labels the workbook mapping simply `Verified`; its status is `Source-verified / workbook-pending`.
- The workbook binary is **not** modified by this change because the canonical workbook currently requires restoration under issue #30 / PR #51 before reliable formula editing or verification can occur.
- The Kaggle/release distribution snapshot is not silently rewritten. It must be regenerated from the corrected canonical workbook after restoration and QA.

## Remaining release work

Before the tax threshold rule can be considered implemented and release-verified:

1. restore an intact canonical workbook;
2. inspect the actual `TAXPAYER_CATEGORIES` and tax formula cells;
3. replace any year-shifted values in the workbook;
4. run boundary scenarios at each threshold;
5. confirm progressive slab and minimum-tax behavior against current law;
6. regenerate the curated distribution package; and
7. obtain the legal/practitioner review required by issue #42.

## Status

**Source discrepancy: confirmed.**  
**Documentation/reference layer: corrected.**  
**Workbook implementation: pending restoration and validation.**

This note advances issue #39 but does not close it because other allowance, deduction, tax-treatment, and source-mapping items remain incomplete.
