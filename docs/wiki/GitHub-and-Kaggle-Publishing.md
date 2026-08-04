# 🚀 GitHub and Kaggle Publishing

The project separates **engineering and governance** from **public distribution**.

## GitHub Role

GitHub is the authoritative engineering workspace for:

- Workbook source files
- Research documents and source registers
- Formula methodology
- Validation cases and reconciliation evidence
- Governance and contribution documents
- Issues, pull requests, CI, and release notes
- Tax-year history and version traceability

## Kaggle Role

Kaggle is the clean public distribution package for:

- Usable workbook
- Concise README and user guide
- Dataset metadata
- Validation sample
- Lightweight notebook
- Stable preview assets

> [!IMPORTANT]
> Kaggle should contain a curated release package, not the entire engineering repository.

## Recommended Repository Paths

```text
excel/school_college/MPO_School_College_Salary_Tax_BD_TY2026_27.xlsx
assets/previews/cover-banner.jpg
assets/previews/project-icon.jpg
assets/previews/social-preview.jpg
assets/previews/dashboard-preview.jpg
docs/wiki/
docs/research/
notebooks/
tests/
release/
```

## Release Package Checklist

| Item | GitHub | Kaggle |
|:--|:--:|:--:|
| Main workbook | ✅ | ✅ |
| Full source register | ✅ | Optional summary |
| Research notes | ✅ | ❌ |
| Test suite | ✅ | Selected evidence |
| Contribution workflow | ✅ | ❌ |
| Concise user guide | ✅ | ✅ |
| Preview images | ✅ | ✅ |
| Release notes | ✅ | Summary |

## Recommended Kaggle Metadata

```text
Title: Bangladesh MPO School & College Salary Tax Toolkit
Tax Year: 2026–27
Sector: MPO School & College
Status: Beta
Format: Microsoft Excel Workbook
Country: Bangladesh
```

## Publishing Sequence

1. Complete source and formula review.
2. Run validation and reconciliation checks.
3. Confirm naming compliance.
4. Update README, Wiki, and release notes.
5. Create a versioned GitHub Release.
6. Publish the curated Kaggle package.
7. Verify download links, previews, and workbook integrity.

## Asset Rules

Stable previews:

```text
cover-banner.jpg
project-icon.jpg
social-preview.jpg
dashboard-preview.jpg
```

Tax-year-specific workbook:

```text
MPO_School_College_Salary_Tax_BD_TY2026_27.xlsx
```

Do not publish release assets containing `final`, `new`, `copy`, `latest`, or `updated`.

---

**Related pages:** [Asset Naming Convention](Asset-Naming-Convention.md) · [Validation and Release Gates](Validation-and-Release-Gates.md)
