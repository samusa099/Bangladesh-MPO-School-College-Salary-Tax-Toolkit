#!/usr/bin/env python3
"""Regression tests for workbook_formula_audit.py using synthetic XLSX fixtures."""

from __future__ import annotations

import importlib.util
import tempfile
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

SCRIPT = Path(__file__).with_name("workbook_formula_audit.py")
spec = importlib.util.spec_from_file_location("workbook_formula_audit", SCRIPT)
assert spec and spec.loader
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

MAIN_NS = module.MAIN_NS


def qname(tag: str) -> str:
    return f"{{{MAIN_NS}}}{tag}"


def build_workbook(
    path: Path,
    *,
    formula: str | None = None,
    cell_type: str | None = None,
    value: str | None = None,
) -> None:
    workbook = ET.Element(qname("workbook"))
    worksheet = ET.Element(qname("worksheet"))
    sheet_data = ET.SubElement(worksheet, qname("sheetData"))
    row = ET.SubElement(sheet_data, qname("row"), {"r": "1"})
    cell_attrs = {"r": "A1"}
    if cell_type:
        cell_attrs["t"] = cell_type
    cell = ET.SubElement(row, qname("c"), cell_attrs)
    if formula is not None:
        ET.SubElement(cell, qname("f")).text = formula
    if value is not None:
        ET.SubElement(cell, qname("v")).text = value

    with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        archive.writestr("xl/workbook.xml", ET.tostring(workbook, encoding="utf-8", xml_declaration=True))
        archive.writestr(
            "xl/worksheets/sheet1.xml",
            ET.tostring(worksheet, encoding="utf-8", xml_declaration=True),
        )


def assert_contains(findings: list[str], text: str) -> None:
    assert any(text in finding for finding in findings), findings


def main() -> int:
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)

        valid = root / "valid.xlsx"
        build_workbook(valid, formula='CONCATENATE("#N/A","foo")', value="0")
        assert module.audit_workbook(valid) == []

        broken = root / "broken.xlsx"
        build_workbook(broken, formula="1+#REF!", value="0")
        assert_contains(module.audit_workbook(broken), "Broken formula")

        external = root / "external.xlsx"
        build_workbook(external, formula="'[book.xlsx]Sheet1'!A1", value="0")
        assert_contains(module.audit_workbook(external), "External workbook formula reference")

        saved_error = root / "saved-error.xlsx"
        build_workbook(saved_error, cell_type="e", value="#DIV/0!")
        assert_contains(module.audit_workbook(saved_error), "Saved Excel error")

        truncated = root / "truncated.xlsx"
        build_workbook(truncated, formula="1+1", value="2")
        data = truncated.read_bytes()
        truncated.write_bytes(data[64:])
        findings = module.audit_workbook(truncated)
        assert findings, "Truncated XLSX must fail the audit"
        assert any(
            "offset" in finding.lower() or "unreadable" in finding.lower()
            for finding in findings
        ), findings

    print("PASS: workbook audit regression fixtures behaved as expected.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
