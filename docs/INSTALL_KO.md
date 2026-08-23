# 한국어 패치 설치 안내

## 1. Windows 10/11 64비트 권장 방법

준비물은 다음 두 가지입니다.

- `moon: Remix RPG Adventure` PlayStation 일본판 Rev 1의 BIN/CUE
- `Moon_PS1_Korean_Patch_v2.0_Windows_Portable.zip`

Portable 패키지를 완전히 푼 뒤 `apply_patch_windows.bat`을 실행합니다.
Python이나 xdelta를 따로 설치할 필요가 없습니다. 동봉된 공식 xdelta3
3.2.0 Windows x64 실행 파일은 사용 전에 크기와 SHA-256이 검사됩니다.

원본 BIN과 CUE 경로를 차례로 요청하면 파일을 창에 끌어 놓고 Enter를
누릅니다. 성공하면 원본 옆에 `Moon_Korean_v2.0` 폴더가 만들어집니다.

## 2. macOS/Linux 및 고급 사용자 준비물

- `moon: Remix RPG Adventure` PlayStation 일본판 Rev 1의 BIN/CUE
- [Python 3](https://www.python.org/downloads/)
- [xdelta3 3.2.0](https://github.com/jmacd/xdelta/releases/tag/v3.2.0)
- `Moon_PS1_Korean_Patch_v2.0.zip`

이 패치는 다른 리비전, ISO 변환본, CHD, PBP 또는 이미 수정된 BIN에는
직접 적용할 수 없습니다. v1.0/v1.1 결과에 덧붙이는 방식도 아닙니다.
반드시 정확한 깨끗한 Rev 1 BIN/CUE에서 시작하세요.

## 3. 원본 확인

지원 원본 BIN:

- 권장 파일명:
  `Moon - Remix RPG Adventure (Japan) (Rev 1).bin`
- 크기: `640,491,936 bytes`
- SHA-256:
  `828189dd7cba0211585c9e06a99936924f0fb883da428525f1fc73790fb403f2`

지원 원본 CUE:

- 권장 파일명:
  `Moon - Remix RPG Adventure (Japan) (Rev 1).cue`
- 크기: `108 bytes`
- SHA-256:
  `031a35316b96460c474e3a6a99bd2dfb98e6408dedd8ceadffc49faf20d77482`
- 구조: 단일 `TRACK 01 MODE2/2352`, `INDEX 01 00:00:00`

파일 이름보다 크기와 SHA-256이 기준입니다. 일반 패키지에서는 다음
명령으로 원본을 미리 확인할 수 있습니다.

```text
python3 verify_image.py "/경로/원본.bin" --cue "/경로/원본.cue"
```

Windows Portable 이용자는 적용기가 같은 검사를 자동 수행하므로 이 명령을
따로 실행하지 않아도 됩니다.

## 4. xdelta3 배치(일반 패키지만 해당)

xdelta3 실행 파일을 다음 중 한 곳에 둡니다.

1. 패치 압축을 푼 최상위 폴더
2. 그 안의 `tools` 폴더
3. 운영체제의 PATH

Windows Portable에는 검증된 `xdelta3.exe`가 이미 들어 있습니다.

## 5. 간단 적용

### Windows

Windows Portable에서 `apply_patch_windows.bat`을 실행합니다.

### macOS

`apply_patch_macos.command`를 실행합니다. 실행 권한 문제로 열리지 않으면
터미널에서 패키지 폴더로 이동한 뒤 다음을 실행할 수 있습니다.

```text
python3 apply_patch.py
```

### Linux

`apply_patch_linux.sh`를 실행하거나 다음 명령을 사용합니다.

```text
python3 apply_patch.py
```

## 6. 명령행 적용

모든 경로를 직접 지정할 수 있습니다.

```text
python3 apply_patch.py \
  --bin "/경로/Moon - Remix RPG Adventure (Japan) (Rev 1).bin" \
  --cue "/경로/Moon - Remix RPG Adventure (Japan) (Rev 1).cue" \
  --output-dir "/경로/Moon_Korean_v2.0"
```

적용기는 다음 순서로 동작합니다.

1. 원본 BIN 크기와 SHA-256 확인
2. 원본 CUE 크기와 SHA-256 확인
3. xdelta 패치 자체의 크기와 SHA-256 확인
4. 기존 파일을 덮지 않는 임시 폴더에 패치 적용
5. 완성 BIN/CUE의 크기와 SHA-256 재검사
6. 모든 검사가 통과한 경우에만 최종 폴더로 이동

원본 BIN/CUE는 수정되지 않습니다. 출력 폴더가 이미 있으면 안전을 위해
중단하므로 기존 폴더를 옮기거나 다른 출력 경로를 지정하세요.

## 7. 완성 결과

- 완성 BIN 크기: `640,491,936 bytes`
- 완성 BIN SHA-256:
  `c5e58d0b9030a0f8683126f2866b633c70e6ea5e12c699524dfece1c67fcc43d`
- 완성 CUE SHA-256:
  `031a35316b96460c474e3a6a99bd2dfb98e6408dedd8ceadffc49faf20d77482`

에뮬레이터에는 BIN이 아니라 CUE를 여는 것을 권장합니다.

## 8. 저장 데이터

- 패치 적용 전에 원본 BIN/CUE와 메모리카드를 백업하세요.
- 일반 PlayStation 메모리카드 저장은 호환 확인됐지만 백업을 대체하지
  않습니다.
- 원본 또는 이전 패치에서 만든 게임 내 저장을 사용할 때는 먼저
  에뮬레이터를 완전히 종료하고 v2.0 CUE로 콜드 부팅하세요.
- 다른 패치 버전에서 만든 에뮬레이터 savestate는 사용하지 마세요.

## 9. PSP EBOOT.PBP로 변환하려는 경우

먼저 BIN/CUE 단계에서 패치를 적용하고 완성 BIN이 정확히
`c5e58d0b…fcc43d`인지 확인합니다. 그다음 이용자가 선택한 도구로
EBOOT.PBP로 변환하세요.

PBP는 별도 컨테이너라 변환 뒤 SHA-256이 위 BIN 값과 달라지는 것이
정상입니다. PSP POPS/EBOOT.PBP는 v2.0의 공식 검증 범위가 아닙니다.

## 10. 숨겨진 메뉴

적용 확인 뒤 `PUSH START`에서 `START`를 누르고, 원래
Game Start/Continue 화면에서 `SELECT`를 누릅니다. 자세한 내용은
[숨겨진 콘텐츠 안내](HIDDEN_CONTENT_GUIDE_KO.md)를 확인하세요.
