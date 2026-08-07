#!/usr/bin/env python3
"""Identify and verify a Moon PS1 original or Korean-patched BIN/CUE pair."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from release_lib import ReleaseError, classify_bin, load_manifest, validate_file


LABELS = {
    "supported_original": "지원 원본: Japan Rev 1",
    "unsupported": "지원하지 않는 이미지",
}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("bin", type=Path, help="확인할 BIN 파일")
    parser.add_argument("--cue", type=Path, help="함께 확인할 CUE 파일")
    parser.add_argument("--manifest", type=Path, help="릴리스 매니페스트")
    parser.add_argument("--json", action="store_true", help="JSON으로 출력")
    args = parser.parse_args()
    try:
        manifest = load_manifest(args.manifest)
        labels = dict(LABELS)
        labels["patched_release"] = (
            f"한국어 패치 v{manifest['release']['version']}"
        )
        bin_path = args.bin.expanduser().resolve()
        state, digest = classify_bin(bin_path, manifest)
        cue_state = "not_checked"
        if args.cue:
            cue_path = args.cue.expanduser().resolve()
            validate_file(cue_path, manifest["output"]["cue"], "CUE")
            cue_state = "valid"
        report = {
            "state": state,
            "label": labels[state],
            "bin": str(bin_path),
            "bin_size": bin_path.stat().st_size,
            "bin_sha256": digest,
            "cue": cue_state,
        }
    except (ReleaseError, OSError) as exc:
        print(f"오류: {exc}", file=sys.stderr)
        return 2

    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print(report["label"])
        print(f"크기: {report['bin_size']:,} bytes")
        print(f"SHA-256: {report['bin_sha256']}")
        if args.cue:
            print("CUE: 정상")
    return 0 if state != "unsupported" else 2


if __name__ == "__main__":
    raise SystemExit(main())
