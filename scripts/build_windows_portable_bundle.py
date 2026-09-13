#!/usr/bin/env python3
"""Build the deterministic, Python-free Windows Portable release ZIP."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from release_lib import ReleaseError, load_manifest, validate_file  # noqa: E402
from scripts.audit_public_repo import audit  # noqa: E402
from scripts.build_release_bundle import add_bytes  # noqa: E402


BASE_FILES = (
    "LICENSE",
    "README_FIRST_KO.txt",
    "README.md",
    "apply_patch_windows.bat",
    "apply_patch_windows.ps1",
    "release_manifest.json",
    "CHANGELOG.md",
    "CREDITS.md",
    "LEGAL.md",
    "LICENSING.md",
    "docs/INSTALL_KO.md",
    "docs/COMPATIBILITY.md",
    "docs/FAQ_KO.md",
    "docs/HIDDEN_CONTENT_GUIDE_KO.md",
    "RELEASE_NOTES_v2.0.md",
)
POWERSHELL_UTF8_BOM = b"\xef\xbb\xbf"


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_path(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(8 * 1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def exact_bytes(path: Path, spec: dict, label: str) -> bytes:
    if not path.is_file():
        raise ReleaseError(f"{label} 파일이 없습니다: {path}")
    data = path.read_bytes()
    if len(data) != spec["size"]:
        raise ReleaseError(
            f"{label} 크기가 다릅니다: expected={spec['size']} actual={len(data)}"
        )
    actual = sha256_bytes(data)
    if actual != spec["sha256"]:
        raise ReleaseError(
            f"{label} SHA-256이 다릅니다: expected={spec['sha256']} actual={actual}"
        )
    return data


def extract_xdelta_exe(archive_path: Path, manifest: dict) -> bytes:
    xdelta = manifest["windows_portable"]["xdelta"]
    archive_spec = {
        "size": xdelta["archive_size"],
        "sha256": xdelta["archive_sha256"],
    }
    exact_bytes(archive_path, archive_spec, "공식 xdelta Windows ZIP")
    try:
        with zipfile.ZipFile(archive_path) as archive:
            members = set(archive.namelist())
            if xdelta["archive_member"] not in members:
                raise ReleaseError(
                    "공식 xdelta Windows ZIP 내부 경로가 예상과 다릅니다: "
                    f"{xdelta['archive_member']}"
                )
            data = archive.read(xdelta["archive_member"])
    except zipfile.BadZipFile as exc:
        raise ReleaseError(f"공식 xdelta Windows ZIP이 손상되었습니다: {exc}") from exc
    exe_spec = {"size": xdelta["exe_size"], "sha256": xdelta["exe_sha256"]}
    if len(data) != exe_spec["size"] or sha256_bytes(data) != exe_spec["sha256"]:
        raise ReleaseError("xdelta3.exe 크기 또는 SHA-256이 매니페스트와 다릅니다.")
    return data


def build(args: argparse.Namespace) -> tuple[Path, Path]:
    if (ROOT / "JOINT_RELEASE_CONTRACT.md").exists():
        raise ReleaseError("Frozen PS1 ZIP: rebuild from commit 7ed58079145a8ddd0236d338ad3e0a4e765d8558, not the joint tree.")
    manifest = load_manifest(args.manifest)
    if manifest["release"]["version"] != "2.0":
        raise ReleaseError("릴리스 버전이 v2.0이 아닙니다.")
    if manifest["licensing"]["status"] != "approved":
        raise ReleaseError("라이선스 범위가 승인되지 않았습니다.")
    findings = audit(ROOT)
    if findings:
        raise ReleaseError("공개 저장소 감사 실패:\n- " + "\n- ".join(findings))

    patch = args.patch.expanduser().resolve()
    validate_file(patch, manifest["patch"], "xdelta 패치")
    xdelta_exe = extract_xdelta_exe(
        args.xdelta_windows_zip.expanduser().resolve(), manifest
    )

    required = [ROOT / relative for relative in BASE_FILES]
    required.extend(sorted((ROOT / "LICENSES").glob("*")))
    missing = [str(path) for path in required if not path.is_file()]
    if missing:
        raise ReleaseError("릴리스 구성 파일 누락:\n- " + "\n- ".join(missing))

    version = manifest["release"]["version"]
    prefix = f"Moon_PS1_Korean_Patch_v{version}_Windows_Portable"
    out_dir = args.out_dir.expanduser().resolve()
    out_dir.mkdir(parents=True, exist_ok=True)
    zip_path = out_dir / f"{prefix}.zip"
    sums_path = out_dir / "SHA256SUMS_WINDOWS.txt"
    if zip_path.exists() or sums_path.exists():
        raise ReleaseError(f"기존 릴리스 파일이 있습니다: {zip_path} 또는 {sums_path}")

    xdelta = manifest["windows_portable"]["xdelta"]
    internal_sums = [
        f"patch_sha256  {manifest['patch']['sha256']}  patches/{manifest['patch']['filename']}",
        f"xdelta3_exe_sha256  {xdelta['exe_sha256']}  xdelta3.exe",
        f"supported_original_bin_sha256  {manifest['supported_input']['bin']['sha256']}",
        f"output_bin_sha256  {manifest['output']['bin']['sha256']}",
        f"cue_sha256  {manifest['output']['cue']['sha256']}",
    ]
    with zipfile.ZipFile(zip_path, "w", allowZip64=True) as archive:
        for path in required:
            relative = path.relative_to(ROOT).as_posix()
            data = path.read_bytes()
            if relative == "apply_patch_windows.ps1":
                data = POWERSHELL_UTF8_BOM + data
            add_bytes(archive, f"{prefix}/{relative}", data)
        add_bytes(
            archive,
            f"{prefix}/patches/{manifest['patch']['filename']}",
            patch.read_bytes(),
        )
        add_bytes(archive, f"{prefix}/xdelta3.exe", xdelta_exe, executable=True)
        add_bytes(
            archive,
            f"{prefix}/CHECKSUMS.txt",
            ("\n".join(internal_sums) + "\n").encode("utf-8"),
        )

    zip_sha = sha256_path(zip_path)
    sums_path.write_text(
        f"{zip_sha}  {zip_path.name}\n"
        f"{manifest['patch']['sha256']}  {manifest['patch']['filename']}\n"
        f"{xdelta['exe_sha256']}  xdelta3.exe\n"
        f"{xdelta['archive_sha256']}  {xdelta['archive_filename']}\n",
        encoding="utf-8",
    )
    print(
        json.dumps(
            {
                "zip": str(zip_path),
                "zip_size": zip_path.stat().st_size,
                "zip_sha256": zip_sha,
                "xdelta3_exe_sha256": xdelta["exe_sha256"],
                "checksums": str(sums_path),
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return zip_path, sums_path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--patch", type=Path, required=True)
    parser.add_argument("--xdelta-windows-zip", type=Path, required=True)
    parser.add_argument("--out-dir", type=Path, default=ROOT / "dist-windows")
    parser.add_argument("--manifest", type=Path)
    args = parser.parse_args()
    try:
        build(args)
    except (ReleaseError, OSError, zipfile.BadZipFile) as exc:
        print(f"오류: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
