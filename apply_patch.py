#!/usr/bin/env python3
"""Safely apply the Moon PS1 Korean v1.0 xdelta patch."""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

from release_lib import (
    ReleaseError,
    clean_user_path,
    default_patch_path,
    find_xdelta,
    load_manifest,
    validate_file,
)


def ask_path(prompt: str) -> Path:
    return clean_user_path(input(prompt).strip())


def resolve_inputs(args: argparse.Namespace, manifest: dict) -> tuple[Path, Path]:
    bin_name = manifest["supported_input"]["bin"]["filename"]
    cue_name = manifest["supported_input"]["cue"]["filename"]
    source_bin = args.bin
    if source_bin is None:
        source_bin = ask_path("원본 Rev 1 BIN 파일을 끌어놓고 Enter를 누르세요:\n> ")
    else:
        source_bin = source_bin.expanduser().resolve()
    if source_bin.is_dir():
        source_bin = source_bin / bin_name

    source_cue = args.cue
    if source_cue is None:
        sibling = source_bin.with_name(cue_name)
        if sibling.is_file():
            source_cue = sibling
        elif args.non_interactive:
            raise ReleaseError(f"원본 CUE 파일을 찾을 수 없습니다: {sibling}")
        else:
            source_cue = ask_path("원본 Rev 1 CUE 파일을 끌어놓고 Enter를 누르세요:\n> ")
    else:
        source_cue = source_cue.expanduser().resolve()
    return source_bin.resolve(), source_cue.resolve()


def apply(args: argparse.Namespace) -> Path:
    manifest = load_manifest(args.manifest)
    source_bin, source_cue = resolve_inputs(args, manifest)
    validate_file(source_bin, manifest["supported_input"]["bin"], "원본 BIN")
    validate_file(source_cue, manifest["supported_input"]["cue"], "원본 CUE")

    patch = (args.patch or default_patch_path(manifest)).expanduser().resolve()
    validate_file(patch, manifest["patch"], "xdelta 패치")
    xdelta = find_xdelta(args.xdelta)

    output_dir = args.output_dir
    if output_dir is None:
        output_dir = source_bin.parent / "Moon_Korean_v1.0"
    output_dir = output_dir.expanduser().resolve()
    if output_dir.exists():
        raise ReleaseError(
            f"출력 폴더가 이미 존재합니다: {output_dir}\n"
            "기존 파일 보호를 위해 덮어쓰지 않습니다. 폴더 이름을 바꾸거나 옮겨 주세요."
        )
    output_dir.parent.mkdir(parents=True, exist_ok=True)

    temp_root = Path(
        tempfile.mkdtemp(prefix=f".{output_dir.name}.tmp-", dir=output_dir.parent)
    )
    output_bin = temp_root / manifest["output"]["bin"]["filename"]
    output_cue = temp_root / manifest["output"]["cue"]["filename"]
    try:
        print("원본과 패치 파일 검증 완료")
        print("xdelta 패치를 적용합니다. 잠시 기다려 주세요…")
        result = subprocess.run(
            [
                str(xdelta),
                "-d",
                "-s",
                str(source_bin),
                str(patch),
                str(output_bin),
            ],
            text=True,
            capture_output=True,
            check=False,
        )
        if result.returncode != 0:
            detail = (result.stderr or result.stdout).strip()
            raise ReleaseError(f"xdelta 적용에 실패했습니다.\n{detail}")
        validate_file(output_bin, manifest["output"]["bin"], "완성 BIN")
        shutil.copyfile(source_cue, output_cue)
        validate_file(output_cue, manifest["output"]["cue"], "완성 CUE")
        temp_root.rename(output_dir)
    except Exception:
        shutil.rmtree(temp_root, ignore_errors=True)
        raise

    print("\n한국어 패치 적용이 완료되었습니다.")
    print(f"출력 폴더: {output_dir}")
    print(f"BIN SHA-256: {manifest['output']['bin']['sha256']}")
    print("에뮬레이터에서는 출력 폴더의 CUE 파일을 여세요.")
    print("다른 빌드에서 만든 savestate는 사용하지 마세요.")
    return output_dir


def parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser(description=__doc__)
    result.add_argument("--bin", type=Path, help="지원 원본 Rev 1 BIN")
    result.add_argument("--cue", type=Path, help="지원 원본 Rev 1 CUE")
    result.add_argument("--patch", type=Path, help="v1.0 xdelta 패치")
    result.add_argument("--output-dir", type=Path, help="새 출력 폴더")
    result.add_argument("--xdelta", type=Path, help="xdelta3 실행 파일")
    result.add_argument("--manifest", type=Path, help="릴리스 매니페스트")
    result.add_argument(
        "--non-interactive", action="store_true", help="누락 경로를 묻지 않고 실패"
    )
    return result


def main() -> int:
    try:
        apply(parser().parse_args())
    except (ReleaseError, OSError) as exc:
        print(f"\n오류: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
