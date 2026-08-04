#!/usr/bin/env python3
"""Validate repository safety, workbook integrity, and immutable Actions refs."""

from __future__ import annotations

import csv
import re
import sys
import zipfile
from pathlib import Path

ROOT = Path(".").resolve()
WORKFLOWS = Path(".github/workflows")
DEPENDABOT = Path(".github/dependabot.yml")
FULL_SHA = re.compile(r"^[0-9a-fA-F]{40}$")
ACTION_REF = re.compile(
    r"^\s*(?:-\s*)?uses:\s*([^\s@]+)@([^\s#]+)",
    re.MULTILINE,
)

BLOCKED_NAMES = {
    ".env",
    "credentials.json",
    "id_dsa",
    "id_ed25519",
    "id_rsa",
    "kaggle.json",
    "service-account.json",
}
BLOCKED_BINARY_SUFFIXES = {
    ".apk",
    ".com",
    ".dll",
    ".dmg",
    ".exe",
    ".iso",
    ".jar",
    ".msi",
    ".scr",
}
MAX_ARCHIVE_MEMBER_BYTES = 200_000_000
MAX_ARCHIVE_TOTAL_BYTES = 500_000_000

errors: list[str] = []


def fail(message: str) -> None:
    errors.append(message)


def validate_paths_and_files() -> None:
    for path in Path(".").rglob("*"):
        if ".git" in path.parts:
            continue

        if path.is_symlink():
            try:
                path.resolve(strict=True).relative_to(ROOT)
            except Exception:
                fail(f"Unsafe symlink: {path}")
            continue

        if not path.is_file():
            continue

        try:
            path.resolve().relative_to(ROOT)
        except ValueError:
            fail(f"Path escapes repository: {path}")

        if path.name.lower() in BLOCKED_NAMES:
            fail(f"Blocked credential or private file: {path}")
        if path.suffix.lower() in BLOCKED_BINARY_SUFFIXES:
            fail(f"Blocked executable/binary file: {path}")

    for path in Path(".").rglob("*.xlsx"):
        if ".git" in path.parts:
            continue
        try:
            with zipfile.ZipFile(path) as archive:
                names = archive.namelist()
                if "[Content_Types].xml" not in names or "xl/workbook.xml" not in names:
                    fail(f"Invalid XLSX: {path}")
                total_size = 0
                for member in names:
                    info = archive.getinfo(member)
                    total_size += info.file_size
                    if member.startswith(("/", "\\")) or ".." in Path(member).parts:
                        fail(f"XLSX path traversal: {path}:{member}")
                    if info.file_size > MAX_ARCHIVE_MEMBER_BYTES:
                        fail(f"Oversized XLSX member: {path}:{member}")
                if total_size > MAX_ARCHIVE_TOTAL_BYTES:
                    fail(f"Oversized XLSX expansion: {path}")
        except Exception as exc:
            fail(f"Unreadable XLSX {path}: {type(exc).__name__}")

    for path in Path(".").rglob("*.csv"):
        if ".git" in path.parts:
            continue
        try:
            with path.open(encoding="utf-8-sig", newline="", errors="replace") as handle:
                for row_number, row in enumerate(csv.reader(handle), 1):
                    for column_number, value in enumerate(row, 1):
                        if value.lstrip().startswith(("=", "+", "@", "\t", "\r")):
                            fail(
                                "CSV formula injection risk: "
                                f"{path}:{row_number}:{column_number}"
                            )
        except OSError as exc:
            fail(f"Unreadable CSV {path}: {type(exc).__name__}")


def validate_actions() -> None:
    for workflow in sorted(WORKFLOWS.glob("*.y*ml")):
        text = workflow.read_text(encoding="utf-8")
        for action, ref in ACTION_REF.findall(text):
            if action.startswith("docker://"):
                continue
            if not FULL_SHA.fullmatch(ref):
                fail(f"Non-immutable action reference in {workflow}: {action}@{ref}")


def validate_dependabot() -> None:
    if not DEPENDABOT.exists():
        fail("Missing .github/dependabot.yml")
        return
    text = DEPENDABOT.read_text(encoding="utf-8")
    if not re.search(
        r"package-ecosystem:\s*[\"']?github-actions[\"']?",
        text,
    ):
        fail("Dependabot does not configure the github-actions ecosystem")


def main() -> int:
    validate_paths_and_files()
    validate_actions()
    validate_dependabot()

    if errors:
        for message in errors:
            print(f"::error::{message}")
        print(f"FAILED: {len(errors)} repository policy violation(s).")
        return 1

    print("PASS: repository, workbook, and GitHub Actions policy validated.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
