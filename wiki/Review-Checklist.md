# Review Checklist

Use this checklist before merging a release PR.

## Documentation

- README explains project scope.
- Wiki pages are present.
- Source register is available.
- Changelog is updated.
- Release notes are updated.

## Workbook

- Workbook opens in Excel.
- Input cells are clear.
- Formula cells are not accidentally overwritten.
- `TAXPAYER_CATEGORIES` exists.
- `TEST_CASES` exists.

## Validation

- Formula tests pass.
- Tax category thresholds are checked.
- Gross and net salary totals reconcile.
- No temporary files are committed.

## Release

- Version number is correct.
- Binary assets are placed in the correct folders.
- Kaggle package is clean.
