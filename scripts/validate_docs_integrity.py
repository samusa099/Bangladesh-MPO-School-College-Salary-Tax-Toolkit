from __future__ import annotations

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
WIKI = ROOT / "wiki"

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


def publishing_entries(path: Path) -> set[str]:
    """Return normalized Markdown filenames from a publishing section."""
    if not path.exists():
        errors.append(f"Missing required index: {path.relative_to(ROOT)}")
        return set()

    text = path.read_text(encoding="utf-8")
    heading = re.search(
        r"^##\s+(?:[^\w\s]+\s*)?Publishing(?:\s+and\s+Releases|\s+pages)?\s*$",
        text,
        re.MULTILINE | re.IGNORECASE,
    )
    if not heading:
        errors.append(f"{path.name}: missing Publishing section")
        return set()

    next_heading = re.search(r"^##\s+", text[heading.end() :], re.MULTILINE)
    section_end = heading.end() + next_heading.start() if next_heading else len(text)
    section = text[heading.end() : section_end]

    entries: set[str] = set()
    for line in section.splitlines():
        line = line.strip()
        if not line.startswith("-"):
            continue

        link = re.search(r"\[[^\]]+\]\(([^)]+\.md)\)", line)
        code = re.search(r"`([^`]+\.md)`", line)
        target = link.group(1) if link else code.group(1) if code else None
        if not target:
            continue

        name = Path(target).name.removesuffix(".md").replace("-", " ").casefold()
        entries.add(name)

    return entries


# Navigation and final index must expose the same publishing pages.
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
