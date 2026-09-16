#!/usr/bin/env python3
"""Create only missing, blank Career OS files; never overwrite existing data."""

from __future__ import annotations

import argparse
from pathlib import Path


DIRECTORIES = (
    "00_Home", "01_My_Evidence", "02_Roles", "03_Companies",
    "04_Applications", "05_Career_Experiments", "06_Templates",
    "07_Resumes", "99_Raw",
)


def home_documents() -> dict[str, str]:
    documents = {
        "Career Dashboard.md": "# Career Dashboard\n\nPrivate Vault. No personal evidence has been added yet.\n",
        "My Profile.md": (
            "# My Profile\n\nAll personal fields begin as NEED_CONFIRMATION. "
            "Enter only the current user's supported facts or direct confirmations.\n\n"
            "| Field | Status | Value |\n| --- | --- | --- |\n"
            "| Name | NEED_CONFIRMATION | |\n"
            "| Phone | NEED_CONFIRMATION | |\n"
            "| Email | NEED_CONFIRMATION | |\n"
            "| Location | NEED_CONFIRMATION | |\n"
            "| Education | NEED_CONFIRMATION | |\n"
            "| Graduation date | NEED_CONFIRMATION | |\n"
            "| Language certificate | NEED_CONFIRMATION | |\n"
        ),
        "Personal Evidence Intake.md": (
            "# Personal Evidence Intake\n\nAdd the current user's resumes, work/project materials, "
            "metrics definitions, education, skills, and direct confirmations. "
            "Preserve source links and ownership boundaries; record conflicts rather than choosing a version.\n"
        ),
        "Career Map.md": "# Career Map\n\nNo roles or experiments recorded yet.\n",
    }
    for name, header in (
        ("Evidence Index.md", "ID | Status | Title | Source"),
        ("Role Index.md", "ID | Role | Updated | Note"),
        ("Company Index.md", "ID | Company | Updated | Note"),
        ("Application Index.md", "ID | Company | Role | Status | Folder"),
    ):
        columns = header.count("|") + 1
        documents[name] = (
            f"# {name.removesuffix('.md')}\n\n"
            f"| {header} |\n| " + " | ".join(["---"] * columns) + " |\n"
        )
    return documents


def initialize(vault: Path) -> list[Path]:
    vault = vault.expanduser().resolve()
    if vault.parent == vault or vault == Path.home().resolve():
        raise ValueError("Choose a dedicated Vault directory, not a filesystem root or home directory")
    for name in DIRECTORIES:
        (vault / name).mkdir(parents=True, exist_ok=True)
    written: list[Path] = []
    files = {vault / "00_Home" / name: content for name, content in home_documents().items()}
    template_root = Path(__file__).resolve().parents[1] / "templates"
    for template in template_root.glob("*.md"):
        files[vault / "06_Templates" / template.name] = template.read_text(encoding="utf-8")
    for path, content in files.items():
        if path.exists():
            continue
        try:
            with path.open("x", encoding="utf-8", newline="\n") as stream:
                stream.write(content)
        except FileExistsError:
            continue
        written.append(path)
    return written


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--vault", type=Path, required=True)
    args = parser.parse_args()
    created = initialize(args.vault)
    print(f"Created {len(created)} blank files; existing files were preserved")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
