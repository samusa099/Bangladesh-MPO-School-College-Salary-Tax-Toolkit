# Source Register

The workbook uses source IDs to keep salary and tax rules auditable.

## Core source register sheet

```text
SOURCE_REGISTER
```

## Required source fields

| Field | Meaning |
|---|---|
| Source ID | Stable reference ID inside the workbook |
| Authority | Issuing authority |
| Document or page | Source title |
| Published date | Publication date where available |
| Effective date | Date the rule applies from |
| Applicable area | Salary, tax, allowance or deduction area |
| Rule extracted | Short extracted rule note |
| Verification | Research, Beta or Verified status |
| Last checked | Review date |
| URL | Public source location where available |

## Current extracted evidence

| Source ID | Authority | Document / page | Applicable area | Rule extracted | Evidence status | Last checked |
|---|---|---|---|---|---|---|
| `NBR-BUDGET-2026-APP-B` | National Board of Revenue | Budget Speech 2026, Appendix B, Table 1 | TY 2026–27 taxpayer thresholds | General BDT 375,000; female/65+ BDT 425,000; third gender/disability BDT 500,000; eligible gazetted special category BDT 525,000; eligible dependent with disability +BDT 50,000 | **Primary source verified; workbook pending** | 2026-08-23 |
| `SHED-MPO-POLICY-2025` | Secondary and Higher Education Division | School & College Manpower Structure and MPO Policy 2025 | School/College controlling policy catalogue | Current School & College MPO policy catalogue; rule-by-rule extraction still required | **Primary source identified; extraction in progress** | 2026-08-23 |
| `SHED-BAISHAKHI-2018` | Secondary and Higher Education Division | 2018 order on 5% increment and 20% Baishakhi allowance | Baishakhi allowance | MPO School/College teachers and employees: Baishakhi allowance at 20% under the cited order | **Primary rate source; supersession check pending** | 2026-08-23 |
| `DSHE-BAISHAKHI-2026` | Directorate of Secondary and Higher Education | Baishakhi Allowance 2026 bill-submission notice | Baishakhi allowance workflow | Confirms the allowance remained an active MPO School/College billing workflow in April 2026 | **Primary current-workflow corroboration; rate not stated** | 2026-08-23 |
| `TERBB-RETIREMENT-6PCT` | Non-Government Teachers' and Employees' Retirement Benefit Board | Board site / 6% deduction gazette catalogue | Retirement Benefit deduction | 6% is deducted/saved from MPO for retirement benefits | **Primary authority verified; workbook pending** | 2026-08-23 |
| `WELFARE-TRUST-4PCT` | Non-Government Educational Institution Teachers and Employees Welfare Trust | Regulations page / 4% contribution notification | Welfare Trust deduction | Authority publishes the 4% contribution-deduction notification | **Primary authority identified; workbook pending** | 2026-08-23 |
| `FIN-FESTIVAL-2025-LEAD` | Finance Division order, corroborated by government news-clipping archive and contemporary reports | May 2025 festival-allowance increase | Festival allowance | Reports quote Finance Division order increasing MPO teachers from 25% to 50% of one month's government-share basic salary; employees remained at 50% | **Secondary-corroborated lead; original primary order still required in register** | 2026-08-23 |
| `DSHE-FESTIVAL-2026` | Directorate of Secondary and Higher Education | Eid-ul-Fitr / Eid-ul-Azha 2026 bill-submission notices | Festival allowance workflow | Confirms festival/bonus billing remained active for MPO School/College personnel in 2026 | **Primary current-workflow corroboration; rate not stated** | 2026-08-23 |

### Public source locations

- `NBR-BUDGET-2026-APP-B`: <https://nbr.gov.bd/uploads/budget/Budget_Speech_English.pdf>
- `SHED-MPO-POLICY-2025`: <https://shed.gov.bd/pages/moedu-policies/%E0%A6%AC%E0%A7%87%E0%A6%B8%E0%A6%B0%E0%A6%95%E0%A6%BE%E0%A6%B0%E0%A6%BF-%E0%A6%B6%E0%A6%BF%E0%A6%95%E0%A7%8D%E0%A6%B7%E0%A6%BE-%E0%A6%AA%E0%A7%8D%E0%A6%B0%E0%A6%A4%E0%A6%BF%E0%A6%B7%E0%A7%8D%E0%A6%A0%E0%A6%BE%E0%A6%A8-%E0%A6%B8%E0%A7%8D%E0%A6%95%E0%A7%81%E0%A6%B2-%E0%A6%93-%E0%A6%95%E0%A6%B2%E0%A7%87%E0%A6%9C-%E0%A6%8F%E0%A6%B0-%E0%A6%9C%E0%A6%A8%E0%A6%AC%E0%A6%B2-%E0%A6%95%E0%A6%BE%E0%A6%A0%E0%A6%BE%E0%A6%AE%E0%A7%8B-%E0%A6%93-%E0%A6%8F%E0%A6%AE-%E0%A6%AA%E0%A6%BF-%E0%A6%93-cc6ff9-69414656c4774958d7b551b7>
- `SHED-BAISHAKHI-2018`: <https://shed.gov.bd/pages/notices/6941463da31054345f0fc6c3>
- `DSHE-BAISHAKHI-2026`: <https://dshe.gov.bd/pages/notices/69ce29296f69908fa2e1b4b5>
- `TERBB-RETIREMENT-6PCT`: <https://terbb.gov.bd/>
- `TERBB-RETIREMENT-6PCT` gazette catalogue: <https://terbb.gov.bd/site/page/ed5675a3-1c33-427c-b644-a1b8b1066de3/%E0%A6%97%E0%A7%87%E0%A6%9C%E0%A7%87%E0%A6%9F>
- `WELFARE-TRUST-4PCT`: <https://ngte-welfaretrust.gov.bd/pages/static-pages/6922dfcf933eb65569e2418d>
- `DSHE-FESTIVAL-2026`: <https://dshe.gov.bd/pages/notices/%E0%A6%8F%E0%A6%AE%E0%A6%AA%E0%A6%BF%E0%A6%93%E0%A6%AD%E0%A7%81%E0%A6%95%E0%A7%8D%E0%A6%A4-%E0%A6%B6%E0%A6%BF%E0%A6%95%E0%A7%8D%E0%A6%B7%E0%A6%95-%E0%A6%95%E0%A6%B0%E0%A7%8D%E0%A6%AE%E0%A6%9A%E0%A6%BE%E0%A6%B0%E0%A7%80%E0%A6%A6%E0%A7%87%E0%A6%B0-%E0%A6%88%E0%A6%A6-%E0%A6%89%E0%A6%B2-%E0%A6%AB%E0%A7%87%E0%A6%A4%E0%A6%B0-%E0%A7%A8%E0%A7%A6%E0%A7%A8%E0%A7%AC-%E0%A6%8F%E0%A6%B0-%E0%A6%89%E0%A7%8E%E0%A6%B8%E0%A6%AC-%E0%A6%AD%E0%A6%BE%E0%A6%A4%E0%A6%BE%E0%A6%B0-%E0%A6%85%E0%A6%B0%E0%A7%8D%E0%A6%A5-eft-%E0%A6%A4%E0%A7%87-%E0%A6%AA%E0%A7%8D%E0%A6%B0%E0%A7%87%E0%A6%B0%E0%A6%A3%E0%A7%87%E0%A6%B0-%E0%A6%B2%E0%A6%95%E0%A7%8D%E0%A6%B7%E0%A7%8D%E0%A6%AF%E0%A7%87-%E0%A6%AC%E0%A6%BF%E0%A6%B2-%E0%A6%B8%E0%A6%BE%E0%A6%AC%E0%A6%AE%E0%A6%BF%E0%A6%9F-%E0%A6%B8%E0%A6%82%E0%A6%95%E0%A7%8D%E0%A6%B0%E0%A6%BE%E0%A6%A8%E0%A7%8D%E0%A6%A4-08xij0-69a57feea2028309cc744343>

## Verification rule

A formula should not be marked **Verified** merely because a source exists. The source must be tied to the correct effective period and employee scope, mapped to the workbook field/formula, and tested against the actual workbook implementation. Secondary reporting may be retained as a research lead, but it must not replace an available primary order/gazette.
