# 🗂️ Asset Naming Convention

This convention defines the required filenames for repository previews, workbook releases, and related distribution assets.

Consistent filenames improve:

* Repository organization
* GitHub link stability
* Release automation
* Searchability
* Documentation maintenance
* Kaggle and external-platform compatibility

---

## 🖼️ Preview Assets

Use stable, permanent filenames for repository and promotional images.

```text
cover-banner.jpg
project-icon.jpg
social-preview.jpg
dashboard-preview.jpg
```

| Asset                   | Purpose                                      |
| :---------------------- | :------------------------------------------- |
| `cover-banner.jpg`      | Main repository, Wiki, or project banner     |
| `project-icon.jpg`      | Square project icon or avatar                |
| `social-preview.jpg`    | GitHub social preview and link-sharing image |
| `dashboard-preview.jpg` | Workbook dashboard screenshot or preview     |

> [!IMPORTANT]
> Preview filenames must remain stable when an image is redesigned or replaced. Update the existing file instead of creating versioned duplicates.

---

## 📊 Workbook Assets

Workbook filenames must clearly identify:

* Sector or workbook scope
* Primary function
* Country
* Applicable tax year
* File format

### Required Pattern

```text
MPO_School_College_Salary_Tax_BD_TY2026_27.xlsx
```

### Filename Structure

```text
[Sector]_[Institution]_[Purpose]_[Country]_[TaxYear].[Extension]
```

| Filename Element  | Example          |
| :---------------- | :--------------- |
| Sector            | `MPO`            |
| Institution scope | `School_College` |
| Purpose           | `Salary_Tax`     |
| Country           | `BD`             |
| Tax year          | `TY2026_27`      |
| Extension         | `.xlsx`          |

> [!NOTE]
> Use underscores between filename components. Avoid spaces, unnecessary punctuation, and ambiguous abbreviations.

---

## 🚫 Prohibited Filename Terms

Do not use temporary or subjective labels in published, distributed, or release assets.

Prohibited examples include:

```text
final
new
copy
latest
updated
```

### Incorrect Examples

```text
MPO_Salary_Tax_final.xlsx
MPO_Salary_Tax_latest.xlsx
MPO_Salary_Tax_updated.xlsx
MPO_Salary_Tax_copy.xlsx
cover-banner-new.jpg
social-preview-final.jpg
```

### Correct Examples

```text
MPO_School_College_Salary_Tax_BD_TY2026_27.xlsx
cover-banner.jpg
social-preview.jpg
```

> [!WARNING]
> Terms such as `final`, `latest`, and `updated` become inaccurate as soon as another revision is released. They also create duplicate files, broken references, and uncertainty about which asset is authoritative.

---

## 🔢 Versioning Rule

Use semantic release versions, tax years, dates, or Git tags when version identification is required.

Preferred version identifiers include:

```text
v0.1.0
v0.2.0-beta
v1.0.0
TY2026_27
2026-08-04
```

### Recommended Release Practice

Keep the workbook filename stable within its tax-year package:

```text
MPO_School_College_Salary_Tax_BD_TY2026_27.xlsx
```

Track release versions through:

* Git tags
* GitHub Releases
* Release notes
* Checksums
* Changelog entries
* Package or archive filenames

Example release archive:

```text
bd-mpo-salary-tax-toolkit_v0.1.2_TY2026_27.zip
```

---

## ✅ Naming Rules

All repository assets must follow these requirements:

1. Use descriptive and predictable names.
2. Use underscores for structured workbook filenames.
3. Use lowercase kebab-case for stable preview-image filenames.
4. Include the applicable tax year in workbook filenames.
5. Preserve stable preview filenames when replacing images.
6. Use release tags instead of words such as `final` or `latest`.
7. Avoid spaces, duplicate suffixes, and operating-system-generated names.
8. Ensure documentation references the exact filename and letter case.

---

## 📋 Naming Compliance Checklist

Before publishing a release, confirm that:

* [ ] All preview assets use stable filenames.
* [ ] The workbook name includes the correct tax year.
* [ ] No filename contains `final`, `new`, `copy`, `latest`, or `updated`.
* [ ] No duplicate suffixes such as `(1)` or `- Copy` remain.
* [ ] Documentation links use the correct filename.
* [ ] GitHub Release assets match the documented naming convention.
* [ ] Archive filenames include a proper release version.
* [ ] Previous release assets remain traceable through Git tags or releases.

---

## 📌 Approved Asset Names

```text
cover-banner.jpg
project-icon.jpg
social-preview.jpg
dashboard-preview.jpg
MPO_School_College_Salary_Tax_BD_TY2026_27.xlsx
```

> [!TIP]
> A filename should describe what the asset is—not its temporary editing status.
