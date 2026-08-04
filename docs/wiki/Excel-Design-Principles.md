# Excel Design Principles

## Workbook design goals

- easy input;
- clear outputs;
- visible source status;
- separated formulas and assumptions;
- dashboard-ready structure;
- printable payslip;
- annual summary for tax planning.

## Input design

- Keep user inputs in `USER_INPUT`.
- Use highlighted cells for editable values.
- Avoid asking users to edit formula sheets.

## Formula design

- Keep verified rules source-linked.
- Keep uncertain rules editable.
- Avoid VBA in version 1.
- Use Excel 2019-compatible core formulas.

## Output design

- Monthly salary sheet for detail.
- Annual salary sheet for summary.
- Dashboard for quick review.
- Payslip for printable output.
