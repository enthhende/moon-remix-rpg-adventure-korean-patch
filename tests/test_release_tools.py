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
    def test_manifest_pins_v1_1_identities(self) -> None:
        manifest = load_manifest()
        self.assertEqual(manifest["release"]["version"], "1.1")
        self.assertEqual(manifest["supported_input"]["bin"]["size"], 640491936)
        self.assertEqual(
            manifest["supported_input"]["bin"]["sha256"],
            "828189dd7cba0211585c9e06a99936924f0fb883da428525f1fc73790fb403f2",
        )
        self.assertEqual(
            manifest["output"]["bin"]["sha256"],
            "4dcea06e752afabab4d525903815fc21f681718e1ff59952ff95da6f2992fb9c",
        )
        self.assertEqual(
            manifest["patch"]["sha256"],
            "48e5cc30f88dbe7858f4096d9fb7c1942a4c1344dc16f702460e53b88379208e",
        )
        self.assertFalse(manifest["verification"]["reverse_patch_distributed"])

    def test_windows_portable_pins_official_xdelta(self) -> None:
        manifest = load_manifest()
        portable = manifest["windows_portable"]
        xdelta = portable["xdelta"]
        self.assertFalse(portable["python_required"])
        self.assertEqual(xdelta["version"], "3.2.0")
        self.assertEqual(xdelta["license"], "Apache-2.0")
        self.assertEqual(xdelta["archive_size"], 184374)
        self.assertEqual(
            xdelta["archive_sha256"],
            "af8ef036cb077a48df080c9a8ac1be4a6e7511c32d11f8bec89b6803a9e52576",
        )
        self.assertEqual(xdelta["exe_size"], 336896)
        self.assertEqual(
            xdelta["exe_sha256"],
            "53d90226615f217d3380c39892833311b4e24acd863e1ca01f14b5e772e2e6d0",
        )

    def test_windows_wrapper_is_python_free_and_pins_all_inputs(self) -> None:
        manifest = load_manifest()
        batch = (ROOT / "apply_patch_windows.bat").read_text(encoding="utf-8")
        powershell = (ROOT / "apply_patch_windows.ps1").read_text(encoding="utf-8")
        self.assertNotIn("python", batch.lower())
        self.assertIn("powershell.exe", batch.lower())
        self.assertIn("-NoProfile", batch)
        self.assertIn("-ExecutionPolicy Bypass", batch)
        self.assertNotIn("apply_patch.py", powershell.lower())
        self.assertNotIn("python.exe", powershell.lower())
        self.assertNotIn("python3", powershell.lower())
        self.assertIn("$ExpectedInputSize = 640491936", powershell)
        self.assertIn(manifest["supported_input"]["bin"]["sha256"], powershell)
        self.assertIn(manifest["supported_input"]["cue"]["sha256"], powershell)
        self.assertIn(manifest["patch"]["sha256"], powershell)
        self.assertIn(manifest["output"]["bin"]["sha256"], powershell)
        self.assertIn(manifest["windows_portable"]["xdelta"]["exe_sha256"], powershell)
        self.assertIn("Output folder already exists", powershell)
        self.assertIn("Move-Item", powershell)

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
