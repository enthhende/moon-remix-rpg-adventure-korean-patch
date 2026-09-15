"""Package boundary tests with synthetic data; no ROM or real patch needed."""
import hashlib
import io
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import zipfile

from scripts import build_eden_bundle as builder


class EdenBundleTest(unittest.TestCase):
    def test_wrong_source_is_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            source = Path(temp) / 'wrong.zip'
            source.write_bytes(b'not the approved source')
            with self.assertRaisesRegex(ValueError, 'exact public'):
                builder.assemble(source, Path(temp) / 'missing-guide.md')

    def test_layout_identity_and_locale_exclusion(self):
        with tempfile.TemporaryDirectory() as temp:
            source = Path(temp) / 'fixture.zip'
            guide = Path(temp) / 'guide.md'
            guide.write_bytes(b'Japanese system language required.\n')
            data = b'fixture IPS32 payload'
            with zipfile.ZipFile(source, 'w') as archive:
                archive.writestr('original/payload', data)
                archive.writestr('moon-korean-patch/CREDITS_AND_LEGAL_KO.md', b'credits')
                archive.writestr('moon-korean-patch/LICENSES/OFL-1.1.txt', b'license')
                archive.writestr('atmosphere/contents/title/config.ini', b'locale')
            payloads = {'exefs/test.ips': ('original/payload', hashlib.sha256(data).hexdigest())}
            with patch.object(builder, 'SOURCE_SHA256', hashlib.sha256(source.read_bytes()).hexdigest()), patch.object(builder, 'PAYLOADS', payloads):
                result = builder.assemble(source, guide)
                self.assertEqual(result, builder.assemble(source, guide))
                with zipfile.ZipFile(io.BytesIO(result)) as archive:
                    self.assertEqual(set(archive.namelist()), {
                        'moon-korean/exefs/test.ips', 'moon-korean/INSTALL_KO.md',
                        'moon-korean/CREDITS_AND_LEGAL_KO.md',
                        'moon-korean/LICENSES/OFL-1.1.txt', 'moon-korean/SHA256SUMS.txt'})
                    self.assertEqual(archive.read('moon-korean/exefs/test.ips'), data)
                    for line in archive.read('moon-korean/SHA256SUMS.txt').decode().splitlines():
                        digest, name = line.split('  ', 1)
                        self.assertEqual(digest, hashlib.sha256(archive.read('moon-korean/' + name)).hexdigest())
                payloads['exefs/test.ips'] = ('original/payload', '0' * 64)
                with self.assertRaisesRegex(ValueError, 'Payload mismatch'):
                    builder.assemble(source, guide)


if __name__ == '__main__':
    unittest.main()
