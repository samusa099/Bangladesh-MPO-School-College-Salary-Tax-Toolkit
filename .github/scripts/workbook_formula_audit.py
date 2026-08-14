#!/usr/bin/env python3
"""Audit saved XLSX archive, formulas, cached errors, and external links.

Dependency-free by design. This validates the saved OOXML package and formula /
reference integrity. It does not recalculate formulas or prove business rules.
"""

from __future__ import annotations

import re
import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

MAIN_NS = "http://schemas.openxmlformats.org/spreadsheetml/2006/main"
REL_NS = "http://schemas.openxmlformats.org/package/2006/relationships"
ERROR_TOKENS = ("#REF!", "#VALUE!", "#DIV/0!", "#NAME?", "#N/A", "#NUM!", "#NULL!")
EXTERNAL_FORMULA_REF = re.compile(r"\[[^\]]+\.(?:xlsx|xlsm|xlsb|xls)\]", re.IGNORECASE)


def qname(namespace: str, tag: str) -> str:
    return f"{{{namespace}}}{tag}"


def parse_xml(archive: zipfile.ZipFile, member: str) -> ET.Element:
    return ET.fromstring(archive.read(member))


def invalid_member_offsets(archive: zipfile.ZipFile, archive_size: int) -> list[str]:
    findings: list[str] = []
    for info in archive.infolist():
        # A local file header must begin inside the physical archive. A negative
        # offset is strong evidence that the leading bytes of the ZIP/XLSX were
        # truncated while the trailing central directory survived.
        if info.header_offset < 0 or info.header_offset >= archive_size:
            findings.append(
                "Invalid XLSX ZIP local-header offset: "
                f"member={info.filename!r}; header_offset={info.header_offset}; "
                f"archive_size={archive_size}; file_size={info.file_size}; "
                f"compress_size={info.compress_size}. The XLSX package is truncated or corrupt."
            )
    return findings


def audit_workbook(path: Path) -> list[str]:
    findings: list[str] = []
    formula_count = 0
    cached_error_count = 0

    if not path.exists():
        return [f"Missing workbook: {path}"]

    try:
        archive_size = path.stat().st_size
        with zipfile.ZipFile(path) as archive:
            names = set(archive.namelist())

            if "xl/workbook.xml" not in names:
                return [f"Invalid XLSX (missing xl/workbook.xml): {path}"]

            offset_findings = invalid_member_offsets(archive, archive_size)
            if offset_findings:
                # Do not attempt XML/formula analysis on a physically inconsistent
                # package; member reads can fail or return misleading results.
                return offset_findings

            external_parts = sorted(name for name in names if name.startswith("xl/externalLinks/"))
            if external_parts:
                findings.append(
                    f"External workbook link parts found in {path}: {', '.join(external_parts)}"
                )

            rels_name = "xl/_rels/workbook.xml.rels"
            if rels_name in names:
                rels_root = parse_xml(archive, rels_name)
                for rel in rels_root.findall(qname(REL_NS, "Relationship")):
                    target_mode = rel.attrib.get("TargetMode", "")
                    rel_type = rel.attrib.get("Type", "")
                    target = rel.attrib.get("Target", "")
                    if target_mode.lower() == "external" or "externalLink" in rel_type:
                        findings.append(
                            f"External workbook relationship in {path}: {target or rel_type}"
                        )

            workbook_root = parse_xml(archive, "xl/workbook.xml")
            for defined_name in workbook_root.findall(f".//{qname(MAIN_NS, 'definedName')}"):
                text = defined_name.text or ""
                for token in ERROR_TOKENS:
                    if token in text:
                        name = defined_name.attrib.get("name", "<unnamed>")
                        findings.append(
                            f"Broken defined name {name!r} in {path}: contains {token}"
                        )
                if EXTERNAL_FORMULA_REF.search(text):
                    name = defined_name.attrib.get("name", "<unnamed>")
                    findings.append(
                        f"External workbook reference in defined name {name!r} in {path}"
                    )

            worksheet_members = sorted(
                name
                for name in names
                if name.startswith("xl/worksheets/") and name.endswith(".xml")
            )

            for member in worksheet_members:
                root = parse_xml(archive, member)
                for cell in root.findall(f".//{qname(MAIN_NS, 'c')}"):
                    address = cell.attrib.get("r", "?")
                    formula = cell.find(qname(MAIN_NS, "f"))
                    value = cell.find(qname(MAIN_NS, "v"))

                    if formula is not None:
                        formula_count += 1
                        formula_text = formula.text or ""
                        for token in ERROR_TOKENS:
                            if token in formula_text:
                                findings.append(
                                    f"Broken formula in {path}:{member}:{address}: contains {token}"
                                )
                        if EXTERNAL_FORMULA_REF.search(formula_text):
                            findings.append(
                                f"External workbook formula reference in {path}:{member}:{address}"
                            )

                    if cell.attrib.get("t") == "e":
                        cached_error_count += 1
                        cached_value = (value.text if value is not None else "") or "<empty>"
                        findings.append(
                            f"Saved Excel error in {path}:{member}:{address}: {cached_value}"
                        )

    except zipfile.BadZipFile as exc:
        return [f"Unreadable XLSX ZIP container: {path}: {exc}"]
    except ET.ParseError as exc:
        return [f"Invalid XLSX XML in {path}: {exc}"]
    except (OSError, RuntimeError, NotImplementedError) as exc:
        return [f"Unable to inspect workbook {path}: {type(exc).__name__}: {exc}"]

    print(
        f"AUDIT: {path} | formulas={formula_count} | "
        f"saved_error_cells={cached_error_count} | findings={len(findings)}"
    )
    return findings


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print("Usage: workbook_formula_audit.py <workbook.xlsx> [more.xlsx ...]", file=sys.stderr)
        return 2

    findings: list[str] = []
    for raw_path in argv[1:]:
        findings.extend(audit_workbook(Path(raw_path)))

    if findings:
        for finding in findings:
            print(f"::error::{finding}")
        print(f"FAILED: {len(findings)} workbook archive/formula/reference finding(s).")
        return 1

    print("PASS: XLSX package and saved workbook formulas/references passed the automated audit.")
    print("NOTE: this check does not recalculate formulas or prove business-rule correctness.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
