#!/usr/bin/env python3
"""Shared, standard-library-only helpers for the Moon Korean patch release."""

from __future__ import annotations

import hashlib
import json
import shutil
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
DEFAULT_MANIFEST = ROOT / "release_manifest.json"


class ReleaseError(RuntimeError):
    """A user-facing release validation error."""


def load_manifest(path: Path | None = None) -> dict[str, Any]:
    manifest_path = (path or DEFAULT_MANIFEST).resolve()
    try:
        data = json.loads(manifest_path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ReleaseError(f"릴리스 매니페스트가 없습니다: {manifest_path}") from exc
    except json.JSONDecodeError as exc:
        raise ReleaseError(f"릴리스 매니페스트가 손상되었습니다: {exc}") from exc
    if data.get("schema") != "moon.ps1.kr_patch.release_manifest.v1":
        raise ReleaseError("지원하지 않는 릴리스 매니페스트입니다.")
    return data


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(8 * 1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def clean_user_path(value: str) -> Path:
    value = value.strip().strip('"').strip("'")
    return Path(value).expanduser().resolve()


def validate_file(path: Path, spec: dict[str, Any], label: str) -> str:
    if not path.is_file():
        raise ReleaseError(f"{label} 파일을 찾을 수 없습니다: {path}")
    size = path.stat().st_size
    expected_size = int(spec["size"])
    if size != expected_size:
        raise ReleaseError(
            f"{label} 크기가 다릅니다: {size:,} bytes "
            f"(필요: {expected_size:,} bytes)"
        )
    actual = sha256_file(path)
    expected = str(spec["sha256"]).lower()
    if actual != expected:
        raise ReleaseError(
            f"{label} SHA-256이 다릅니다.\n"
            f"  실제: {actual}\n"
            f"  필요: {expected}\n"
            "다른 리비전, 변환된 이미지 또는 이미 패치된 파일일 수 있습니다."
        )
    return actual


def classify_bin(path: Path, manifest: dict[str, Any]) -> tuple[str, str]:
    if not path.is_file():
        raise ReleaseError(f"BIN 파일을 찾을 수 없습니다: {path}")
    size = path.stat().st_size
    digest = sha256_file(path)
    for state, spec in (
        ("supported_original", manifest["supported_input"]["bin"]),
        ("patched_release", manifest["output"]["bin"]),
    ):
        if size == int(spec["size"]) and digest == str(spec["sha256"]):
            return state, digest
    return "unsupported", digest


def find_xdelta(explicit: Path | None = None) -> Path:
    candidates: list[Path] = []
    if explicit is not None:
        candidates.append(explicit.expanduser())
    candidates.extend(
        [
            ROOT / "xdelta3",
            ROOT / "xdelta3.exe",
            ROOT / "tools" / "xdelta3",
            ROOT / "tools" / "xdelta3.exe",
        ]
    )
    from_path = shutil.which("xdelta3")
    if from_path:
        candidates.append(Path(from_path))
    for candidate in candidates:
        resolved = candidate.resolve()
        if resolved.is_file():
            return resolved
    raise ReleaseError(
        "xdelta3를 찾을 수 없습니다. xdelta3 3.1.0 실행 파일을 이 폴더나 "
        "tools 폴더에 넣거나 PATH에 등록해 주세요."
    )


def default_patch_path(manifest: dict[str, Any]) -> Path:
    filename = manifest["patch"]["filename"]
    candidates = [ROOT / "patches" / filename, ROOT / filename]
    for candidate in candidates:
        if candidate.is_file():
            return candidate
    return candidates[0]
