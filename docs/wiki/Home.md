<div align="center">

# 📘 Bangladesh MPO School & College Salary Tax Toolkit

### Wiki and implementation guide

**Tax Year 2026–27 · Microsoft Excel · School & College MPO · Beta**

[Getting Started](Getting-Started.md) · [Workbook Guide](Workbook-Sheet-Guide.md) · [Formula Methodology](Formula-Methodology.md) · [Validation](Validation-and-Release-Gates.md)

</div>

---

> [!IMPORTANT]
> This is an open-source planning and research toolkit. It is not an official MPO salary bill, certified payroll system, tax-return filing service, or substitute for legal and professional advice.

## 🎯 Project Purpose

The toolkit converts School and College MPO salary rules, taxpayer-category thresholds, deductions, allowances, and annual tax logic into a transparent Excel workflow that can be reviewed, tested, and improved.

## 📦 Current Package

| Item | Current value |
|:--|:--|
| Scope | MPO School & College |
| Tax year | **2026–27** |
| Release line | `v0.1.x` |
| Status | **Beta** |
| Main workbook | `excel/school_college/MPO_School_College_Salary_Tax_BD_TY2026_27.xlsx` |
| Formula policy | Excel 2019-compatible core formulas |
| Macro policy | No VBA in v1 |

## 🧭 Wiki Navigation

| Area | Page | Use it for |
|:--|:--|:--|
| Start | [Getting Started](Getting-Started.md) | Open the workbook and enter data safely |
| Workbook | [Workbook Sheet Guide](Workbook-Sheet-Guide.md) | Understand every worksheet |
| Tax | [Taxpayer Categories](Taxpayer-Categories.md) | Review category thresholds and selection logic |
| Calculations | [Formula Methodology](Formula-Methodology.md) | Trace salary and tax formulas |
| Quality | [Validation and Release Gates](Validation-and-Release-Gates.md) | Understand Beta and Verified criteria |
| Publishing | [GitHub and Kaggle Publishing](GitHub-and-Kaggle-Publishing.md) | Prepare engineering and distribution packages |
| Assets | [Asset Naming Convention](Asset-Naming-Convention.md) | Apply stable release filenames |
| Planning | [Roadmap](Roadmap.md) | Review planned releases and sector expansion |
| Help | [FAQ](FAQ.md) | Resolve common questions |

## 🏗️ Architecture

```text
Shared calculation engine
        ↓
School & College rule pack
        ↓
Tax-year-specific workbook
        ↓
Validation, reporting and release package
```

> [!NOTE]
> Madrasa, Ebtedayi, and Technical or Vocational education require separate authority documents, rule packs, and workbooks.

## ✅ Current Capabilities

- Monthly and annual salary calculations
- Taxpayer-category comparison
- Progressive annual tax estimate
- Income, expense, and savings analysis
- Dashboard and printable payslip views
- Source register, data dictionary, and test cases
- GitHub and Kaggle publishing structure

## 🚦Release Status

| Area | Status |
|:--|:--:|
| Workbook architecture | ✅ Implemented |
| Core salary flow | ✅ Implemented |
| Taxpayer categories | ✅ Implemented |
| Source extraction | 🟡 In progress |
| Official salary reconciliation | ⏳ Pending |
| Legal and practitioner review | ⏳ Pending |
| Verified release | ⏳ Pending |

---

<div align="center">

**Start with → [Getting Started](Getting-Started.md)**

</div>
