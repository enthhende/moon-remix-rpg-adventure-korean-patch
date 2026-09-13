"""Joint documentation and PS1 frozen-build boundary tests (no game files)."""
import argparse
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

    def test_draft_does_not_claim_all_platforms_released(self):
        self.assertIn("합동 릴리스 준비 초안", (ROOT / "README.md").read_text())
        self.assertIn("NOT_RUN", (ROOT / "platforms/steam-windows/README.md").read_text())
        self.assertIn("실행 확인", (ROOT / "platforms/switch/README.md").read_text())


if __name__ == "__main__":
    unittest.main()
