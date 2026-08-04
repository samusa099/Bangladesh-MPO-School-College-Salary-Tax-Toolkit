from __future__ import annotations

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
WIKI = ROOT / "docs" / "wiki"

errors: list[str] = []

# Validate every backtick-quoted local Markdown filename in navigation documents.
for index_name in ("Navigation.md", "_Sidebar.md"):
    path = WIKI / index_name
    if not path.exists():
        continue
    text = path.read_text(encoding="utf-8")
    for filename in re.findall(r"`([^`]+\.md)`", text):
        candidate = WIKI / filename
        if not candidate.is_file():
            errors.append(f"{index_name}: missing wiki page {filename}")

# Navigation and final index must expose the same publishing pages.
def publishing_entries(path: Path) -> set[str]:
    if not path.exists():
        errors.append(f"Missing required index: {path.relative_to(ROOT)}")
        return set()
    text = path.read_text(encoding="utf-8")
    match = re.search(r"^## Publishing(?: pages)?\s*$([\s\S]*?)(?=^## |\Z)", text, re.MULTILINE)
    if not match:
        errors.append(f"{path.name}: missing Publishing section")
        return set()
    entries: set[str] = set()
    for line in match.group(1).splitlines():
        line = line.strip()
        if not line.startswith("-"):
            continue
        value = line[1:].strip().strip("`")
        value = value.removesuffix(".md").replace("-", " ").casefold()
        entries.add(value)
    return entries

navigation = publishing_entries(WIKI / "Navigation.md")
final_index = publishing_entries(WIKI / "Final-Wiki-Index.md")
if navigation != final_index:
    errors.append(
        "Publishing index mismatch: "
        f"only in Navigation={sorted(navigation - final_index)}; "
        f"only in Final-Wiki-Index={sorted(final_index - navigation)}"
    )

# Prevent the exact dead path detected during PR #3 review.
publishing = WIKI / "GitHub-and-Kaggle-Publishing.md"
if publishing.exists() and "docs/formula_methodology/" in publishing.read_text(encoding="utf-8"):
    errors.append("GitHub-and-Kaggle-Publishing.md: obsolete docs/formula_methodology/ path")

# Keep the workbook's canonical filename stable across documentation.
canonical = "MPO_School_College_Salary_Tax_BD_TY2026_27.xlsx"
prepared = WIKI / "Prepared-Files.md"
if prepared.exists():
    text = prepared.read_text(encoding="utf-8")
    if canonical not in text:
        errors.append(f"Prepared-Files.md: canonical workbook filename missing: {canonical}")
    if re.search(r"MPO_School_College_Salary_Tax_BD_TY2026_27_v[^\s`]+\.xlsx", text):
        errors.append("Prepared-Files.md: versioned workbook filename conflicts with canonical path")

if errors:
    print("Documentation integrity validation failed:")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print("Documentation integrity validation passed.")
