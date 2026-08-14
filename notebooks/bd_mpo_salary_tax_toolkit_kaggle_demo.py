# %% [markdown]
# Bangladesh MPO School & College Salary Tax Toolkit — Python Starter Notebook

This notebook shows how to explore the **Bangladesh MPO School & College Salary Tax Toolkit** dataset on Kaggle.

It is designed for first-time users who want to quickly inspect the workbook, read key sheets, create a small summary, and generate basic charts from the Excel toolkit.

## What this notebook does

1. Finds the Excel workbook automatically under `/kaggle/input`.
2. Lists available files and sheets.
3. Loads taxpayer-category, monthly salary, tax calculation, asset, and next-year planning sheets when available.
4. Creates quick summaries and simple charts.
5. Exports clean preview CSV files to `/kaggle/working`.

> Note: This is an educational and planning notebook. It does not replace official payroll, tax, legal, or professional review.


# %%
from pathlib import Path
import os
import re
import json
import warnings

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

warnings.filterwarnings("ignore")

pd.set_option("display.max_columns", 80)
pd.set_option("display.max_rows", 80)
pd.set_option("display.width", 160)

INPUT_ROOT = Path("/kaggle/input")
WORKING_ROOT = Path("/kaggle/working")

print("Input root:", INPUT_ROOT)
print("Working root:", WORKING_ROOT)


# %%
def show_input_tree(root=INPUT_ROOT, max_files=80):
    """Print a compact tree of files available to this notebook."""
    if not root.exists():
        print("No /kaggle/input folder found. Are you running outside Kaggle?")
        return []

    all_files = []
    for path in sorted(root.rglob("*")):
        if path.is_file():
            all_files.append(path)

    print(f"Found {len(all_files)} files under {root}")
    for path in all_files[:max_files]:
        rel = path.relative_to(root)
        size_kb = path.stat().st_size / 1024
        print(f"- {rel} ({size_kb:,.1f} KB)")

    if len(all_files) > max_files:
        print(f"... showing first {max_files} files only")
    return all_files

all_files = show_input_tree()


# %%
def find_workbook(root=INPUT_ROOT):
    """Find the MPO Salary Tax workbook, even when the dataset is nested."""
    candidates = sorted(root.rglob("*.xlsx")) if root.exists() else []

    if not candidates:
        raise FileNotFoundError(
            "No .xlsx workbook found under /kaggle/input. "
            "Attach the Kaggle dataset to this notebook first."
        )

    preferred = [
        p for p in candidates 
        if "MPO_School_College_Salary_Tax_BD_TY2026_27" in p.name
    ]

    workbook_path = preferred[0] if preferred else candidates[0]
    print("Selected workbook:")
    print(workbook_path)
    return workbook_path

workbook_path = find_workbook()


# %%
xls = pd.ExcelFile(workbook_path)
sheet_names = xls.sheet_names

sheet_catalog = pd.DataFrame({
    "sheet_no": range(1, len(sheet_names) + 1),
    "sheet_name": sheet_names
})

sheet_catalog


# %%
def get_sheet_by_alias(aliases, header=None):
    """
    Read the first sheet that exists from a list of possible names.
    Handles both Bengali v0.1.3 sheet names and earlier English sheet names.
    """
    for name in aliases:
        if name in sheet_names:
            print(f"Loaded sheet: {name}")
            return pd.read_excel(workbook_path, sheet_name=name, header=header), name

    print("None of these sheets were found:", aliases)
    return None, None


def clean_table(df):
    """Drop fully empty rows and columns and reset index."""
    if df is None:
        return None
    out = df.copy()
    out = out.dropna(how="all").dropna(axis=1, how="all")
    out = out.reset_index(drop=True)
    return out


def safe_display(df, rows=12):
    if df is None:
        print("No data to display.")
    else:
        display(df.head(rows))


# %%
sheet_aliases = {
    "start": ["১. শুরু", "START_HERE"],
    "summary": ["২. সারাংশ", "DASHBOARD"],
    "nbr_form": ["৩. NBR ফর্ম"],
    "return_history": ["৪. রিটার্ন"],
    "monthly_salary": ["৫. বেতন ২০২৬", "MONTHLY_SALARY"],
    "income_expense": ["৬. আয়-TDS-ব্যয়", "INCOME_EXPENSE"],
    "assets": ["৭. সম্পদ"],
    "next_year": ["৮. পরের বছর"],
    "user_input": ["ইনপুট", "USER_INPUT"],
    "taxpayer_categories": ["করদাতা", "TAXPAYER_CATEGORIES"],
    "tax_calculation": ["আয়কর", "TAX_CALCULATION"],
    "annual_salary": ["বার্ষিক বেতন", "ANNUAL_SALARY"],
    "source_register": ["উৎস", "SOURCE_REGISTER"],
    "data_dictionary": ["ডিকশনারি", "DATA_DICTIONARY"],
    "test_cases": ["টেস্ট", "TEST_CASES"],
}

loaded = {}
for key, aliases in sheet_aliases.items():
    df, used_name = get_sheet_by_alias(aliases, header=None)
    loaded[key] = {
        "sheet_name": used_name,
        "data": clean_table(df)
    }

print("Loaded sheets:")
for key, item in loaded.items():
    if item["data"] is not None:
        print(f"- {key}: {item['sheet_name']} -> {item['data'].shape}")


# %%
print("Workbook front/navigation preview")
safe_display(loaded["start"]["data"], 15)

print("\nTaxpayer category preview")
safe_display(loaded["taxpayer_categories"]["data"], 15)

print("\nTax calculation preview")
safe_display(loaded["tax_calculation"]["data"], 20)


# %%
def extract_taxpayer_category_table(raw):
    """
    Extract the taxpayer category table from the workbook.
    Expected header row contains 'Dropdown Category' and 'Tax-free Threshold'.
    """
    if raw is None:
        return pd.DataFrame()

    df = raw.copy()
    header_idx = None
    for i in range(len(df)):
        row_values = df.iloc[i].astype(str).str.strip().tolist()
        if "Dropdown Category" in row_values and "Tax-free Threshold" in row_values:
            header_idx = i
            break

    if header_idx is None:
        return pd.DataFrame()

    table = df.iloc[header_idx + 1:].copy()
    table.columns = df.iloc[header_idx].tolist()
    table = table.dropna(how="all")

    if "Dropdown Category" in table.columns:
        table = table[table["Dropdown Category"].notna()]

    if "Tax-free Threshold" in table.columns:
        table["Tax-free Threshold"] = pd.to_numeric(table["Tax-free Threshold"], errors="coerce")

    return table.reset_index(drop=True)

taxpayer_table = extract_taxpayer_category_table(loaded["taxpayer_categories"]["data"])
taxpayer_table


# %%
if not taxpayer_table.empty and "Tax-free Threshold" in taxpayer_table.columns:
    chart_df = taxpayer_table.dropna(subset=["Tax-free Threshold"]).copy()
    chart_df = chart_df.sort_values("Tax-free Threshold")

    plt.figure(figsize=(10, 5))
    plt.barh(chart_df["Dropdown Category"], chart_df["Tax-free Threshold"])
    plt.title("Tax-free Threshold by Taxpayer Category — TY 2026–27")
    plt.xlabel("Threshold (BDT)")
    plt.ylabel("Category")
    plt.tight_layout()
    plt.show()
else:
    print("Taxpayer category table was not available for charting.")


# %%
def extract_metric_table(raw):
    """Extract simple two-column metric tables from sheets such as tax calculation."""
    if raw is None:
        return pd.DataFrame(columns=["metric", "value"])

    df = raw.copy()
    rows = []
    for _, row in df.iterrows():
        values = row.tolist()
        if len(values) >= 2 and pd.notna(values[0]) and pd.notna(values[1]):
            metric = str(values[0]).strip()
            value = values[1]
            if metric and metric.lower() not in ["metric", "input", "field"]:
                rows.append({"metric": metric, "value": value})

    return pd.DataFrame(rows)

tax_metrics = extract_metric_table(loaded["tax_calculation"]["data"])
tax_metrics.head(30)


# %%
def extract_monthly_salary(raw):
    """
    Extract a usable monthly salary table from the workbook.
    The expected table has a 'Month' header somewhere in the sheet.
    """
    if raw is None:
        return pd.DataFrame()

    df = raw.copy()
    header_idx = None
    for i in range(len(df)):
        row_values = df.iloc[i].astype(str).str.strip().tolist()
        if "Month" in row_values:
            header_idx = i
            break

    if header_idx is None:
        return pd.DataFrame()

    table = df.iloc[header_idx + 1:].copy()
    table.columns = df.iloc[header_idx].tolist()
    table = table.dropna(how="all").reset_index(drop=True)

    for col in table.columns:
        if col != "Month":
            table[col] = pd.to_numeric(table[col], errors="ignore")

    return table

monthly_salary = extract_monthly_salary(loaded["monthly_salary"]["data"])
monthly_salary.head()


# %%
if not monthly_salary.empty:
    possible_net_cols = [
        c for c in monthly_salary.columns 
        if isinstance(c, str) and ("net" in c.lower() or "Net" in c)
    ]

    if possible_net_cols and "Month" in monthly_salary.columns:
        net_col = possible_net_cols[-1]
        plot_df = monthly_salary[["Month", net_col]].dropna()

        plt.figure(figsize=(11, 5))
        plt.plot(plot_df["Month"], plot_df[net_col], marker="o")
        plt.title(f"Monthly Net Salary Trend — {net_col}")
        plt.xlabel("Month")
        plt.ylabel("Amount (BDT)")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    else:
        print("Monthly salary table loaded, but no clear net salary column was detected.")
        display(monthly_salary.head(12))
else:
    print("Monthly salary table was not available.")


# %%
print("Assets and investment planning sheet")
safe_display(loaded["assets"]["data"], 15)

print("\nNext-year carry-forward planning sheet")
safe_display(loaded["next_year"]["data"], 15)


# %%
exports = {
    "sheet_catalog.csv": sheet_catalog,
    "taxpayer_categories_preview.csv": taxpayer_table,
    "tax_metrics_preview.csv": tax_metrics,
    "monthly_salary_preview.csv": monthly_salary,
}

for filename, df in exports.items():
    if df is not None and not df.empty:
        out_path = WORKING_ROOT / filename
        df.to_csv(out_path, index=False)
        print("Saved:", out_path)

print("\nGenerated output files:")
for p in sorted(WORKING_ROOT.glob("*.csv")):
    print("-", p.name)


# %% [markdown]
## Conclusion

This starter notebook demonstrates how to programmatically inspect the Excel toolkit, extract key sheets, and produce quick exploratory summaries.

Suggested next improvements:

- Add official salary-row reconciliation cases.
- Expand source-register parsing.
- Compare multiple taxpayer categories at the same taxable income.
- Build a cleaner salary dashboard from exported CSV tables.
- Publish an updated notebook when the workbook moves from Beta to Verified.
