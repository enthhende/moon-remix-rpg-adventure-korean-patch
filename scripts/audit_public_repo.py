#!/usr/bin/env python3
"""Fail closed if the public source repository contains private/game assets."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
IGNORED_DIRS = {".git", "dist", "release-assets", "__pycache__", ".venv"}
FORBIDDEN_SUFFIXES = {
    ".7z",
    ".bin",
    ".ccd",
    ".chd",
    ".cue",
    ".img",
    ".iso",
    ".mcd",
    ".mcr",
    ".pbp",
    ".rar",
    ".sav",
    ".srm",
    ".state",
    ".sub",
    ".vcdiff",
    ".xdelta",
    ".zip",
}
FORBIDDEN_TEXT = {
    "/" + "Users/": "local user path",
    "/" + "Volumes/": "local volume path",
    "github_" + "pat_": "GitHub token",
    "gh" + "p_": "GitHub token",
    "BEGIN OPENSSH" + " PRIVATE KEY": "private key",
    ".emu" + "cap/": "runtime-private path",
}
MAX_SOURCE_FILE_SIZE = 2 * 1024 * 1024


def source_files(root: Path):
    for path in sorted(root.rglob("*")):
        if not path.is_file():
            continue
        relative = path.relative_to(root)
        if any(part in IGNORED_DIRS for part in relative.parts):
            continue
        yield path, relative


def audit(root: Path) -> list[str]:
    findings: list[str] = []
    for path, relative in source_files(root):
        suffix = path.suffix.lower()
        if suffix in FORBIDDEN_SUFFIXES:
            findings.append(f"forbidden extension: {relative}")
        size = path.stat().st_size
        if size > MAX_SOURCE_FILE_SIZE:
            findings.append(f"oversized source file ({size} bytes): {relative}")
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        for needle, label in FORBIDDEN_TEXT.items():
            if needle in text:
                findings.append(f"{label}: {relative}: {needle!r}")
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args()
    root = args.root.resolve()
    findings = audit(root)
    if findings:
        print("PUBLIC REPOSITORY AUDIT: FAIL", file=sys.stderr)
        for finding in findings:
            print(f"- {finding}", file=sys.stderr)
        return 1
    count = sum(1 for _ in source_files(root))
    print(f"PUBLIC REPOSITORY AUDIT: PASS ({count} files)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
