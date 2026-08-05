from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from release_lib import ReleaseError, load_manifest, sha256_file, validate_file  # noqa: E402
from scripts.audit_public_repo import audit  # noqa: E402


class ReleaseToolsTest(unittest.TestCase):
    def test_manifest_pins_v1_0_identities(self) -> None:
        manifest = load_manifest()
        self.assertEqual(manifest["release"]["version"], "1.0")
        self.assertEqual(manifest["supported_input"]["bin"]["size"], 640491936)
        self.assertEqual(
            manifest["supported_input"]["bin"]["sha256"],
            "828189dd7cba0211585c9e06a99936924f0fb883da428525f1fc73790fb403f2",
        )
        self.assertEqual(
            manifest["output"]["bin"]["sha256"],
            "70a8a7d27ff38e0dba186fd88e9040d44c06221086d7d44dba633b6deeb661b3",
        )
        self.assertEqual(
            manifest["patch"]["sha256"],
            "1c4c54c63e944ed0b5baabc0d8bc759568e2d7ab400554945b16f81e0257de10",
        )
        self.assertFalse(manifest["verification"]["reverse_patch_distributed"])

    def test_validate_file_accepts_only_exact_size_and_hash(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "fixture.dat"
            path.write_bytes(b"moon-release-test")
            spec = {"size": path.stat().st_size, "sha256": sha256_file(path)}
            self.assertEqual(validate_file(path, spec, "fixture"), spec["sha256"])
            path.write_bytes(b"changed")
            with self.assertRaises(ReleaseError):
                validate_file(path, spec, "fixture")

    def test_wrong_input_is_rejected_before_output(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            temp_path = Path(temp)
            wrong_bin = temp_path / "wrong.bin"
            wrong_cue = temp_path / "wrong.cue"
            output = temp_path / "output"
            wrong_bin.write_bytes(b"not a disc image")
            wrong_cue.write_text("not a cue", encoding="utf-8")
            result = subprocess.run(
                [
                    sys.executable,
                    str(ROOT / "apply_patch.py"),
                    "--bin",
                    str(wrong_bin),
                    "--cue",
                    str(wrong_cue),
                    "--output-dir",
                    str(output),
                    "--non-interactive",
                ],
                text=True,
                capture_output=True,
                check=False,
            )
            self.assertEqual(result.returncode, 2)
            self.assertIn("크기가 다릅니다", result.stderr)
            self.assertFalse(output.exists())

    def test_public_repository_has_no_forbidden_assets_or_paths(self) -> None:
        self.assertEqual(audit(ROOT), [])


if __name__ == "__main__":
    unittest.main()
