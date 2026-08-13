# 🚦 Project Status

**Last reviewed:** 2026-08-14  
**Release line:** v0.1.3  
**Overall status:** Beta  
**Review cadence:** Weekly

## Current release gates

| Area | Status | Evidence / remaining gate |
|---|---|---|
| Workbook architecture | ✅ Implemented | Shared engine and School & College workbook structure are present. |
| Core salary flow | ✅ Implemented | Monthly and annual salary calculation workflow is present. |
| Taxpayer categories | ✅ Implemented | Taxpayer-category comparison is included. |
| Workbook UX / v0.1.3 package | ✅ Implemented | v0.1.3 workbook and visual previews were merged; tab-layout changes were documented. |
| Source extraction | 🟡 In progress | Core working rules are documented, while several allowance, deduction and tax-treatment rates still require source-by-source extraction. |
| Official salary reconciliation | 🟡 In progress | Pilot reconciliation work has started; the 10-row anonymized validation gate is not yet met. |
| Deterministic formula validation | 🟡 In progress | Validation assets exist and formula-error scanning has been performed; the full 20–30 deterministic scenario gate is not yet demonstrated. |
| Legal and practitioner review | ⏳ Pending | Line-by-line legal/policy review and practitioner sign-off remain outstanding. |
| Verified release | ⏳ Pending | Requires completion of all verification gates above. |

## Progress since the previous checkpoint

- v0.1.3 School & College workbook and visual-preview assets were merged.
- A separate synthetic Fazil/Madrasa calculator was added without changing the School & College verification status.
- Repository maintenance tooling was stabilized under Python orchestration.
- v0.1.3 tab-layout refinements were documented.
- Repository cover branding was refreshed.
- Official salary reconciliation has moved from **Pending** to **In progress**, but it is not yet complete.

## Research work still blocking Verified status

- Complete source extraction for festival allowance, Baishakhi allowance, medical allowance, welfare and retirement deductions, and tax-treatment mapping.
- Reconcile at least 10 anonymized official salary rows against workbook output.
- Complete 20–30 deterministic formula scenarios, including boundary and exception cases.
- Resolve all unexplained salary differences.
- Complete legal/policy review and practitioner review.

## Weekly update rule

Each weekly review should:

1. Compare repository changes and project evidence with the previous status.
2. Promote a status only when evidence supports the change.
3. Update `wiki/Home.md` and this page with the review date.
4. Keep **Verified release** pending until every published release gate is satisfied.
5. Record “no material status change” when work occurred but no release gate advanced.

**Next scheduled review:** 2026-08-21
