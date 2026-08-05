# moon: Remix RPG Adventure PS1 한국어 패치

PlayStation 일본판 `moon: Remix RPG Adventure` Rev 1을 대상으로 하는
비공식 한국어 번역 패치입니다.

이 저장소와 릴리스에는 원본 또는 패치된 전체 게임 이미지가 포함되지
않습니다. 패치를 사용하려면 이용자가 직접 준비한 정확한 일본판 Rev 1
BIN/CUE가 필요합니다.

> 현재 호환성 표기: **에뮬레이션 검증 완료 / 실기 미검증**

## 다운로드

GitHub 사용에 익숙하지 않다면 저장소의 초록색 `Code` 버튼이 아니라
[Releases](https://github.com/enthhende/moon-remix-rpg-adventure-korean-patch/releases/latest)에서
`Moon_PS1_Korean_Patch_v1.0.zip`을 받으세요.

압축을 푼 뒤 `README_FIRST_KO.txt` 또는 [한국어 설치 안내](docs/INSTALL_KO.md)를
따르면 됩니다.

## 빠른 적용

필요한 것:

- 합법적으로 준비한 일본판 Rev 1 BIN/CUE
- Python 3
- xdelta3 3.1.0 실행 파일
- 이 프로젝트의 v1.0 Release 압축 파일

Windows에서는 `apply_patch_windows.bat`, macOS에서는
`apply_patch_macos.command`, Linux에서는 `apply_patch_linux.sh`를 실행합니다.
적용기는 입력 파일의 크기와 SHA-256을 먼저 검사하고, 다른 리비전이나
이미 패치된 파일이면 쓰기 전에 중단합니다.

성공하면 별도 `Moon_Korean_v1.0` 폴더에 BIN/CUE가 만들어집니다. 원본은
수정하거나 덮어쓰지 않습니다. 에뮬레이터에서는 새 폴더의 CUE 파일을
여세요.

## 지원 원본과 결과

| 구분 | 크기 | SHA-256 |
|---|---:|---|
| 지원 원본 Rev 1 BIN | 640,491,936 bytes | `828189dd7cba0211585c9e06a99936924f0fb883da428525f1fc73790fb403f2` |
| 한국어 패치 v1.0 BIN | 640,491,936 bytes | `70a8a7d27ff38e0dba186fd88e9040d44c06221086d7d44dba633b6deeb661b3` |
| 원본·결과 CUE | 108 bytes | `031a35316b96460c474e3a6a99bd2dfb98e6408dedd8ceadffc49faf20d77482` |

트랙 구조는 단일 `TRACK 01 MODE2/2352`, `INDEX 01 00:00:00`입니다.
파일 이름보다 위 크기와 SHA-256이 판정 기준입니다.

## 호환성

- Mednafen PSX 빌드 `013d057`: 장편 자연 플레이와 진엔딩까지 검증
- 일반 메모리카드 저장: 호환 확인
- 실제 PlayStation 본체: 미검증
- PSP POPS용 EBOOT.PBP 변환: 미검증
- 그 밖의 PS1 에뮬레이터: 미검증
- 서로 다른 패치 BIN에서 만든 에뮬레이터 savestate: 지원하지 않음

PSP나 다른 에뮬레이터로 옮길 때는 먼저 패치 직후 BIN이 위의
`70a8…61b3`인지 확인하세요. EBOOT.PBP 등으로 변환한 뒤에는 파일 형식이
달라지므로 이 SHA-256과 더 이상 같지 않은 것이 정상입니다. 자세한 범위는
[호환성 문서](docs/COMPATIBILITY.md)를 참고하세요.

## 주의사항

- 원본 BIN/CUE는 반드시 별도로 보관하세요.
- 일반 메모리카드 저장은 사용할 수 있지만, 다른 BIN에서 만든 savestate는
  불러오지 마세요.
- 엔딩의 지연된 숨은 메시지는 마지막 상태입니다. 그 뒤 타이틀로 자동
  복귀하지 않는 현상은 v1.0 진행 불가 문제로 분류하지 않았습니다.
- 음성만 존재하는 일부 오프닝·엔딩 대사와 엔딩의 일부 일본어 이미지
  한국어화는 후속 연구 범위입니다.

## 오류 제보

[Issues](https://github.com/enthhende/moon-remix-rpg-adventure-korean-patch/issues)에
다음 정보를 적어 주세요.

- 패치 버전과 완성 BIN SHA-256
- 에뮬레이터 이름·버전 또는 실기 본체 모델
- PSP라면 EBOOT.PBP 변환 도구와 설정
- 재현 위치, 직전 행동, 메모리카드/새 게임 여부
- 가능하다면 화면과 로그

원본·패치된 BIN/CUE, BIOS, 메모리카드 전체 덤프는 업로드하지 마세요.

## 저작권과 라이선스

이 프로젝트는 원작 개발사·배급사·현재 권리자와 무관한 비공식 팬 번역
프로젝트입니다. 게임명, 캐릭터, 시나리오, 그래픽, 음원과 그 밖의 원작
권리는 각 권리자에게 있습니다. 자세한 내용은 [법적 고지](LEGAL.md)와
[라이선스 범위](LICENSING.md)를 확인하세요.

사용 글꼴의 원저작권과 OFL-1.1 고지는 [크레딧](CREDITS.md)과
`LICENSES/OFL-1.1.txt`에 보존합니다.
