#!/usr/bin/env python3
"""Conservative release checks for private data accidentally bundled in a skill."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


TEXT_SUFFIXES = {".md", ".py", ".yaml", ".yml", ".json", ".toml", ".txt"}
PRIVATE_DIRS = {"Career-OS", "vault", "private", "outputs", "attachments", ".history", "99_Raw"}
SCAN_RULES = (
    ("fixed personal home path", re.compile(r"(?:[A-Za-z]:[\\/](?:Users|xwechat_files)[\\/][^\s]|/(?:Users|home)/[^\s/]+)")),
    ("email address", re.compile(r"[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}", re.I)),
    ("mobile phone candidate", re.compile(r"(?<!\d)(?:\+?86[- ]?)?1[3-9]\d{9}(?!\d)")),
    ("credential candidate", re.compile(r"(?:gh[pousr]_[A-Za-z0-9]{20,}|sk-[A-Za-z0-9_-]{24,})")),
    ("private key", re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----")),
    ("embedded image", re.compile(r"data:image/[a-z0-9.+-]+;base64,", re.I)),
)


def audit(root: Path) -> list[str]:
    root = root.resolve()
    errors: list[str] = []
    for path in sorted(root.rglob("*")):
        relative = path.relative_to(root)
        if ".git" in relative.parts or "__pycache__" in relative.parts:
            continue
        if path.is_symlink():
            errors.append(f"{relative}: symlink may escape the release boundary")
            continue
        if not path.is_file():
            continue
        if set(relative.parts) & PRIVATE_DIRS:
            errors.append(f"{relative}: private runtime directory")
            continue
        if path.suffix not in TEXT_SUFFIXES and path.name not in {".gitignore", "LICENSE"}:
            errors.append(f"{relative}: non-allowlisted release file")
            continue
        if path.name.startswith(".env") or ".local." in path.name:
            errors.append(f"{relative}: private local configuration")
            continue
        if path.stat().st_size > 512_000:
            errors.append(f"{relative}: unexpectedly large release file")
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            errors.append(f"{relative}: not UTF-8 text")
            continue
        for category, pattern in SCAN_RULES:
            for match in pattern.finditer(text):
                line = text.count("\n", 0, match.start()) + 1
                errors.append(f"{relative}:{line}: {category}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    errors = audit(args.root)
    for error in errors:
        print(f"ERROR: {error}")
    if errors:
        return 1
    print("Public-package privacy checks passed (text allowlist, paths, contacts, credentials, media)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
