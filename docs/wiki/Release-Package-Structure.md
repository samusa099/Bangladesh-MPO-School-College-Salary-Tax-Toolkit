# Release Package Structure

## GitHub repository package

```text
assets/
data/
docs/
excel/
notebooks/
release/
tests/
README.md
LICENSE
CITATION.cff
```

## Kaggle distribution package

```text
BD_MPO_Salary_Tax_Excel_Package/
├── dataset-metadata.json
├── README.md
├── 01_REFERENCE_TABLES/
├── 02_EXCEL_TOOLS/
├── 03_VALIDATION_CASES/
├── 04_NOTEBOOK/
├── 05_USER_GUIDES/
└── 06_PREVIEWS/
```

## Rule

GitHub may contain engineering files. Kaggle should contain only clean user-facing files.
