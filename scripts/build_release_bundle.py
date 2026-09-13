#!/usr/bin/env python3
"""Build a deterministic, game-image-free GitHub Release ZIP."""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import sys
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from release_lib import ReleaseError, load_manifest, validate_file  # noqa: E402
from scripts.audit_public_repo import audit  # noqa: E402


FIXED_ZIP_TIME = (2026, 8, 23, 0, 0, 0)
BASE_FILES = (
    "LICENSE",
    "README_FIRST_KO.txt",
    "README.md",
    "apply_patch.py",
    "apply_patch_windows.bat",
    "apply_patch_windows.ps1",
    "apply_patch_macos.command",
    "apply_patch_linux.sh",
    "verify_image.py",
    "release_lib.py",
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
EXECUTABLES = {
    "apply_patch.py",
    "apply_patch_macos.command",
    "apply_patch_linux.sh",
    "verify_image.py",
}


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_path(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(8 * 1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def add_bytes(
    archive: zipfile.ZipFile,
    archive_name: str,
    data: bytes,
    executable: bool = False,
) -> None:
    info = zipfile.ZipInfo(archive_name, FIXED_ZIP_TIME)
    info.compress_type = zipfile.ZIP_DEFLATED
    info.create_system = 3
    mode = 0o755 if executable else 0o644
    info.external_attr = mode << 16
    archive.writestr(info, data, compresslevel=9)


def build(args: argparse.Namespace) -> tuple[Path, Path]:
    if (ROOT / "JOINT_RELEASE_CONTRACT.md").exists():
        raise ReleaseError("Frozen PS1 ZIP: rebuild from commit 7ed58079145a8ddd0236d338ad3e0a4e765d8558, not the joint tree.")
    manifest = load_manifest(args.manifest)
    if manifest["release"]["version"] != "2.0":
        raise ReleaseError("릴리스 버전이 v2.0이 아닙니다.")
    if manifest["licensing"]["status"] != "approved":
        raise ReleaseError(
            "라이선스 범위가 아직 최종 승인되지 않았습니다. "
            "공개 릴리스 ZIP 생성을 중단합니다."
        )
    findings = audit(ROOT)
    if findings:
        raise ReleaseError("공개 저장소 감사 실패:\n- " + "\n- ".join(findings))

    patch = args.patch.expanduser().resolve()
    validate_file(patch, manifest["patch"], "xdelta 패치")
    required = [ROOT / relative for relative in BASE_FILES]
    required.extend(sorted((ROOT / "LICENSES").glob("*")))
    missing = [str(path) for path in required if not path.is_file()]
    if missing:
        raise ReleaseError("릴리스 구성 파일 누락:\n- " + "\n- ".join(missing))

    version = manifest["release"]["version"]
    prefix = f"Moon_PS1_Korean_Patch_v{version}"
    out_dir = args.out_dir.expanduser().resolve()
    out_dir.mkdir(parents=True, exist_ok=True)
    zip_path = out_dir / f"{prefix}.zip"
    standalone_patch = out_dir / manifest["patch"]["filename"]
    sums_path = out_dir / "SHA256SUMS.txt"
    if zip_path.exists() or standalone_patch.exists() or sums_path.exists():
        raise ReleaseError(
            "기존 릴리스 파일이 있습니다: "
            f"{zip_path}, {standalone_patch} 또는 {sums_path}"
        )

    internal_sums = [
        f"patch_sha256  {manifest['patch']['sha256']}  patches/{manifest['patch']['filename']}",
        f"supported_original_bin_sha256  {manifest['supported_input']['bin']['sha256']}",
        f"output_bin_sha256  {manifest['output']['bin']['sha256']}",
        f"cue_sha256  {manifest['output']['cue']['sha256']}",
    ]
    with zipfile.ZipFile(zip_path, "w", allowZip64=True) as archive:
        for path in required:
            relative = path.relative_to(ROOT).as_posix()
            add_bytes(
                archive,
                f"{prefix}/{relative}",
                path.read_bytes(),
                executable=relative in EXECUTABLES,
            )
        add_bytes(
            archive,
            f"{prefix}/patches/{manifest['patch']['filename']}",
            patch.read_bytes(),
        )
        add_bytes(
            archive,
            f"{prefix}/CHECKSUMS.txt",
            ("\n".join(internal_sums) + "\n").encode("utf-8"),
        )

    zip_sha = sha256_path(zip_path)
    shutil.copyfile(patch, standalone_patch)
    validate_file(standalone_patch, manifest["patch"], "독립 xdelta 패치")
    sums_path.write_text(
        f"{zip_sha}  {zip_path.name}\n"
        f"{manifest['patch']['sha256']}  {manifest['patch']['filename']}\n",
        encoding="utf-8",
    )
    print(json.dumps({
        "zip": str(zip_path),
        "zip_size": zip_path.stat().st_size,
        "zip_sha256": zip_sha,
        "standalone_patch": str(standalone_patch),
        "checksums": str(sums_path),
    }, ensure_ascii=False, indent=2))
    return zip_path, sums_path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--patch", type=Path, required=True)
    parser.add_argument("--out-dir", type=Path, default=ROOT / "dist")
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
