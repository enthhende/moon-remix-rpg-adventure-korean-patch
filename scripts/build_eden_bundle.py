#!/usr/bin/env python3
"""Repackage the frozen public Switch patch for Eden; never accepts game images."""
import argparse
import hashlib
import io
import json
from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SOURCE_SHA256 = '21a8ea11d74a9af4f2be9e29c7258932e8e46d24168d0d29c2c723b321656c32'
BUILD_ID = '18D3CEE96E3A274AAD0CA5A140079A45'
ROMFS = 'atmosphere/contents/0100E1800EFCE000/romfs/'
PAYLOADS = {
    f'exefs/{BUILD_ID}.ips': (
        f'atmosphere/exefs_patches/moon-remix-rpg-adventure-korean/{BUILD_ID}.ips',
        'ad17aee1ad5b0421f388822bc9565f66f37fdd7d807b4ab5bbf1f7015ada60c3'),
    'romfs/Data/StreamingAssets/moon_bonus_gallery.pack': (
        ROMFS + 'Data/StreamingAssets/moon_bonus_gallery.pack',
        'efac73730ca9bbc40206ee66577acf2587e719c90aec503b01f39a5fc0daf982'),
    'romfs/moon_bonus_notice.pack': (
        ROMFS + 'moon_bonus_notice.pack',
        'a4c94bf1a3f92f9116aa0deef6e526a1292437098675d0c3d080d066b598fdf3'),
}


def sha(data):
    return hashlib.sha256(data).hexdigest()


def assemble(source_zip, guide):
    source = source_zip.read_bytes()
    if sha(source) != SOURCE_SHA256:
        raise ValueError('Input must be the exact public v2.0 Switch ZIP (locale R1).')
    files = {}
    with zipfile.ZipFile(io.BytesIO(source)) as archive:
        for target, (original, expected) in PAYLOADS.items():
            data = archive.read(original)
            if sha(data) != expected:
                raise ValueError(f'Payload mismatch: {original}')
            files[target] = data
        for name in ['CREDITS_AND_LEGAL_KO.md', 'LICENSES/OFL-1.1.txt']:
            files[name] = archive.read('moon-korean-patch/' + name)
    files['INSTALL_KO.md'] = guide.read_bytes()
    files['SHA256SUMS.txt'] = ''.join(
        f'{sha(data)}  {name}\n' for name, data in sorted(files.items())
    ).encode('utf-8')
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, 'w') as archive:
        for name, data in sorted(files.items()):
            info = zipfile.ZipInfo('moon-korean/' + name, (2026, 9, 15, 0, 0, 0))
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            # Stored entries make output byte-stable across zlib versions.
            info.compress_type = zipfile.ZIP_STORED
            archive.writestr(info, data)
    result = buffer.getvalue()
    with zipfile.ZipFile(io.BytesIO(result)) as archive:
        expected_names = {'moon-korean/' + name for name in files}
        if set(archive.namelist()) != expected_names or archive.testzip() is not None:
            raise ValueError('Output ZIP layout or CRC failure')
        for name, data in files.items():
            if archive.read('moon-korean/' + name) != data:
                raise ValueError(f'Output mismatch: {name}')
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--switch-zip', type=Path, required=True)
    parser.add_argument('--out-dir', type=Path, default=ROOT / 'dist')
    args = parser.parse_args()
    result = assemble(args.switch_zip, ROOT / 'platforms/switch/EDEN_INSTALL_KO.md')
    args.out_dir.mkdir(parents=True, exist_ok=True)
    output = args.out_dir / 'moon-korean-eden-v2.0.zip'
    checksum = args.out_dir / 'EDEN_SHA256SUMS.txt'
    if output.exists() or checksum.exists():
        raise FileExistsError('Output already exists; use an empty output directory.')
    with output.open('xb') as stream:
        stream.write(result)
    checksum.write_text(f'{sha(result)}  {output.name}\n', encoding='utf-8')
    print(json.dumps({'filename': output.name, 'bytes': len(result), 'sha256': sha(result)}))


if __name__ == '__main__':
    main()
