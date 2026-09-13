"""Joint documentation and PS1 frozen-build boundary tests (no game files)."""
import argparse
import json
from pathlib import Path
import re
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from release_lib import ReleaseError
from scripts.build_release_bundle import build as general_build
from scripts.build_windows_portable_bundle import build as portable_build


class JointContractTest(unittest.TestCase):
    def test_both_ps1_builders_refuse_joint_tree(self):
        for build in [general_build, portable_build]:
            with self.assertRaisesRegex(ReleaseError, "Frozen PS1 ZIP"):
                build(argparse.Namespace())

    def test_platform_pages_and_local_links(self):
        paths = [ROOT / "README.md", ROOT / "JOINT_RELEASE_CONTRACT.md"]
        for platform in ["ps1", "switch", "steam-macos", "steam-windows"]:
            paths.append(ROOT / "platforms" / platform / "README.md")
        for path in paths:
            self.assertTrue(path.is_file())
            for target in re.findall(r"\]\(([^)]+)\)", path.read_text()):
                if "://" not in target and not target.startswith("#"):
                    self.assertTrue((path.parent / target.split("#")[0]).is_file(), (path, target))

    def test_legacy_ps1_readme_preserved(self):
        self.assertTrue((ROOT / "README_PS1_v2.0.md").read_text().startswith(
            "# moon: Remix RPG Adventure PS1 한국어 패치"))

    def test_release_keeps_platform_verification_limits(self):
        self.assertIn("NOT_RUN", (ROOT / "platforms/steam-windows/README.md").read_text())
        self.assertIn("실기 직접 검증", (ROOT / "platforms/switch/README.md").read_text())
        self.assertIn("남단", (ROOT / "platforms/steam-macos/README.md").read_text())

    def test_joint_release_manifest_is_approved_and_exact(self):
        manifest = json.loads((ROOT / "joint_release_manifest.json").read_text())
        self.assertEqual(manifest["schema"], "moon.joint-public-release-manifest.v1")
        self.assertEqual(manifest["release"]["status"], "RELEASE_ARTIFACTS_APPROVED")
        self.assertIs(manifest["release"]["publication_authorized"], True)
        self.assertEqual(manifest["release"]["tag"], "v2.0")
        self.assertEqual(len(manifest["assets"]), 7)
        self.assertEqual(len({row["filename"] for row in manifest["assets"]}), 7)
        self.assertFalse(any("/" in row["filename"] or "\\" in row["filename"]
                             for row in manifest["assets"]))
        notes = (ROOT / "RELEASE_NOTES_JOINT_v2.0.md").read_text()
        for row in manifest["assets"]:
            self.assertIn(row["filename"], notes)
            self.assertIn(row["sha256"], notes)


if __name__ == "__main__":
    unittest.main()
