# Automation Notes

## Future automation ideas

- workbook formula validation workflow;
- archive structure validation workflow;
- notebook validation workflow;
- CSV and Excel safety checks;
- release manifest generation;
- Kaggle package build workflow.

## First safe automation target

Start with validation only. Do not publish to Kaggle automatically until the release package structure is stable.

## Required checks

- file path containment;
- no temporary files;
- workbook exists;
- documentation exists;
- validation cases exist;
- release notes exist.
