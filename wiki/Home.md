<div align="center">

# 📘 Bangladesh MPO School & College Salary Tax Toolkit

**Tax Year 2026–27 · Microsoft Excel · School & College MPO · Beta · v0.1.3**

[Project Status](Project-Status.md) · [Getting Started](Getting-Started.md) · [Workbook Guide](Workbook-Sheet-Guide.md) · [Formula Methodology](Formula-Methodology.md) · [Validation](Validation-and-Release-Gates.md)

</div>

---

> [!IMPORTANT]
> Open-source planning and research toolkit. It is not an official MPO salary bill or a substitute for professional review.

## 🎯 Project Purpose

The toolkit converts Bangladesh School & College MPO salary and individual-tax rules into a transparent Excel workflow that can be reviewed, tested and improved.

## 📦 Current Package

| Item | Current value |
|:--|:--|
| Scope | MPO School & College |
| Tax year | **2026–27** |
| Release line | **v0.1.3** |
| Status | **Beta** |
| Main workbook | `excel/school_college/MPO_School_College_Salary_Tax_BD_TY2026_27.xlsx` |
| Formula policy | Excel 2019-compatible core formulas |
| Macro policy | No VBA in v1 |
| Last status review | **2026-08-14** |

## 🏷️ Release Identity

The canonical public product release is **`v0.1.3`**.

- `v4.0` refers only to the README/design revision; it is not the product release version.
- Prepared `v0.1.4` Kaggle-safe material remains **Unreleased** until a matching Git tag and GitHub Release are published.
- The product must not be marked Verified while public release identifiers conflict.

## ✅ Current Capabilities

- Monthly and annual salary calculations
- Taxpayer-category comparison
- Progressive annual tax estimate
- Income, expense and savings analysis
- Dashboard and printable payslip views
- Source register, data dictionary and validation assets
- GitHub and Kaggle publishing structure
- v0.1.3 workbook visual-experience package

## 🚦 Release Status

| Area | Status |
|:--|:--:|
| Workbook architecture | ✅ Implemented |
| Core salary flow | ✅ Implemented |
| Taxpayer categories | ✅ Implemented |
| Workbook UX / v0.1.3 package | ✅ Implemented |
| Source extraction | 🟡 In progress |
| Official salary reconciliation | 🟡 In progress |
| Deterministic formula validation | 🟡 In progress |
| Legal and practitioner review | ⏳ Pending |
| Verified release | ⏳ Pending |

> [!NOTE]
> Official salary reconciliation has moved from **Pending** to **In progress** because pilot comparison work has started. The release gate remains open until at least 10 anonymized official salary rows reconcile and unresolved differences are documented.

See **[Project Status](Project-Status.md)** for dated evidence, remaining release gates and the weekly review rule.

## 🏗️ Architecture

```text
Verified sources
      ↓
School & College rule pack
      ↓
Excel calculation engine
      ↓
Validation and reconciliation
      ↓
Beta / Verified release
```

> [!NOTE]
> Madrasa, Ebtedayi, and Technical or Vocational education require separate rule packs and verification. Experimental sector work does not change the School & College release status.

---

<div align="center">

**Next weekly status review: 2026-08-21**

</div>
