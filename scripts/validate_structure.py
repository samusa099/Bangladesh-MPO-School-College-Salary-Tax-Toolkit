from pathlib import Path

REQUIRED_ROOT_FILES = {
    ".editorconfig",
    ".gitattributes",
    ".gitignore",
    "CITATION.cff",
    "CODE_OF_CONDUCT.md",
    "CONTRIBUTING.md",
    "LICENSE",
    "LICENSE-CODE",
    "README.md",
    "RELEASE_NOTES.md",
    "SECURITY.md",
    "pyproject.toml",
    "requirements.txt",
}

REQUIRED_DIRECTORIES = {
    "data",
    "docs",
    "excel",
    "metadata",
    "notebooks",
    "release",
    "scripts",
    "tests",
    "wiki",
}


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    missing = [name for name in sorted(REQUIRED_ROOT_FILES) if not (root / name).is_file()]
    missing += [name + "/" for name in sorted(REQUIRED_DIRECTORIES) if not (root / name).is_dir()]
    if missing:
        print("Missing required repository items:")
        for item in missing:
            print(f"- {item}")
        return 1
    print("Repository structure validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
