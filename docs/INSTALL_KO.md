# 한국어 패치 설치 안내

## 1. 준비물

- `moon: Remix RPG Adventure` PlayStation 일본판 Rev 1의 BIN/CUE
- [Python 3](https://www.python.org/downloads/)
- [xdelta3 3.1.0](https://github.com/jmacd/xdelta-gpl/releases/tag/v3.1.0)
- GitHub Releases에서 받은 `Moon_PS1_Korean_Patch_v1.0.zip`

이 패치는 다른 리비전, ISO 변환본, CHD, PBP 또는 이미 수정된 BIN에는
직접 적용할 수 없습니다. 먼저 정확한 Rev 1 BIN/CUE를 준비해야 합니다.

## 2. 원본 확인

지원 원본 BIN의 조건은 다음과 같습니다.

- 권장 파일명:
  `Moon - Remix RPG Adventure (Japan) (Rev 1).bin`
- 크기: `640,491,936 bytes`
- SHA-256:
  `828189dd7cba0211585c9e06a99936924f0fb883da428525f1fc73790fb403f2`

원본 CUE:

- 권장 파일명:
  `Moon - Remix RPG Adventure (Japan) (Rev 1).cue`
- 크기: `108 bytes`
- SHA-256:
  `031a35316b96460c474e3a6a99bd2dfb98e6408dedd8ceadffc49faf20d77482`
- 구조: 단일 `TRACK 01 MODE2/2352`, `INDEX 01 00:00:00`

릴리스 폴더에서 다음 명령으로 BIN 종류를 확인할 수도 있습니다.

```text
python3 verify_image.py "/경로/원본.bin" --cue "/경로/원본.cue"
```

Windows에서 `python3`가 없다면 `py -3`을 사용하세요.

## 3. xdelta3 배치

xdelta3 실행 파일을 다음 중 한 곳에 둡니다.

1. 패치 압축을 푼 최상위 폴더
2. 그 안의 `tools` 폴더
3. 운영체제의 PATH

Windows 파일은 필요하면 `xdelta3.exe`로 이름을 정리합니다. 이 프로젝트는
xdelta3 실행 파일을 직접 동봉하지 않으며, 공식 프로젝트의 배포 파일을
사용합니다.

## 4. 간단 적용

### Windows

`apply_patch_windows.bat`을 실행합니다. 원본 BIN과 CUE 경로를 차례로
요청하면 파일을 창에 끌어 놓고 Enter를 누릅니다.

### macOS

`apply_patch_macos.command`를 실행합니다. 실행 권한이 없다면 터미널에서
릴리스 폴더로 이동한 뒤 다음을 실행합니다.

```text
python3 apply_patch.py
```

### Linux

`apply_patch_linux.sh`를 실행하거나 다음 명령을 사용합니다.

```text
python3 apply_patch.py
```

## 5. 명령행 적용

모든 경로를 직접 지정할 수 있습니다.

```text
python3 apply_patch.py \
  --bin "/경로/Moon - Remix RPG Adventure (Japan) (Rev 1).bin" \
  --cue "/경로/Moon - Remix RPG Adventure (Japan) (Rev 1).cue" \
  --output-dir "/경로/Moon_Korean_v1.0"
```

적용기는 다음 순서로 동작합니다.

1. 원본 BIN 크기와 SHA-256 확인
2. 원본 CUE 크기와 SHA-256 확인
3. xdelta 패치 자체의 크기와 SHA-256 확인
4. 기존 파일을 덮지 않는 임시 폴더에 패치 적용
5. 완성 BIN/CUE의 SHA-256 재검사
6. 모든 검사가 통과한 경우에만 최종 폴더로 이동

원본 BIN/CUE는 수정되지 않습니다. 출력 폴더가 이미 있으면 안전을 위해
중단하므로, 기존 출력 폴더를 다른 곳으로 옮기거나 새 이름을 지정하세요.

## 6. 완성 결과

완성 폴더 안에는 같은 이름의 BIN/CUE가 있습니다.

- 완성 BIN SHA-256:
  `70a8a7d27ff38e0dba186fd88e9040d44c06221086d7d44dba633b6deeb661b3`
- 완성 CUE SHA-256:
  `031a35316b96460c474e3a6a99bd2dfb98e6408dedd8ceadffc49faf20d77482`

에뮬레이터에는 BIN이 아니라 CUE를 여는 것을 권장합니다.

## 7. PSP EBOOT.PBP로 변환하려는 경우

먼저 BIN/CUE 단계에서 한국어 패치 적용과 `70a8…61b3` 검증을 모두
끝냅니다. 그다음 이용자가 선택한 변환 도구로 패치된 BIN/CUE를
EBOOT.PBP로 변환하세요.

PBP는 별도 컨테이너이므로 변환 뒤 SHA-256이 위 BIN 값과 다른 것이
정상입니다. v1.0에서는 PSP POPS/EBOOT.PBP가 아직 공식 검증 범위가
아니므로, 성공·실패 보고 시 PSP 모델, 펌웨어/POPS 환경, 변환 도구와
설정을 함께 적어 주세요.

## 8. 저장 데이터

- 일반 PlayStation 메모리카드 저장은 호환 확인됨
- 원본 또는 이전 패치에서 만든 일반 저장은 사용할 수 있음
- 에뮬레이터 savestate는 BIN의 정확한 코드·RAM 상태에 묶이므로 다른
  패치 버전 사이에서 사용하지 말 것
- 새 패치 버전으로 바꿀 때는 게임 안에서 저장한 뒤 에뮬레이터를 완전히
  종료하고 새 CUE로 다시 부팅할 것
