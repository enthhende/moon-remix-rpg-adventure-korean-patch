# moon: Remix RPG Adventure PS1 한국어 패치

PlayStation 일본판 `moon: Remix RPG Adventure` Rev 1을 대상으로 하는
비공식 한국어 번역 패치입니다.

이 저장소와 릴리스에는 원본 또는 패치된 전체 게임 이미지가 포함되지
않습니다. 패치를 사용하려면 이용자가 직접 준비한 정확한 일본판 Rev 1
BIN/CUE가 필요합니다.

> v2.0 추가 콘텐츠는 Mednafen에서 검증했습니다. DuckStation과 PS2 POPS는
> v1.1 당시의 사용자 확인 기록이며, 원본 PlayStation 본체는 미검증입니다.

## v2.0 주요 내용

v2.0은 v1.1의 단순 문구 수정판이 아닙니다.

- Game Start/Continue 화면에서 `SELECT`로 진입하는 숨겨진
  `미사용 개발 자료` 메뉴
- 이미지 16장과 한국어 해설을 합친 총 48화면의 `보너스 자료관`
- 남아 있던 미사용 장면을 안전하게 감상할 수 있도록 재구성한
  `용의꼬리(미사용 엔딩)`과 `소년과 할머니`
- 이름 끝에 `@♥` 같은 특수문자가 있어도 마지막 한글을 찾아 조사와
  호격을 고르는 주인공 이름 전용 처리
- 일반 대화의 `♥`·`@` 치환, 데이터 삭제 문구 겹침, 호칭·번역·줄바꿈
  수정
- Galmuri9/Galmuri14 기반 영문·특수문자 조정과 MD 문장 전체
  실제 폭 기준 가운데 정렬

추가 콘텐츠에는 본편 결말과 설정에 관한 강한 스포일러가 있습니다.
가능하면 본편 엔딩을 본 뒤 열람해 주세요.

## 다운로드

GitHub 사용에 익숙하지 않다면 저장소의 초록색 `Code` 버튼이 아니라
[Releases](https://github.com/enthhende/moon-remix-rpg-adventure-korean-patch/releases/latest)에서
운영체제에 맞는 파일을 받으세요.

- Windows 10/11 64비트:
  `Moon_PS1_Korean_Patch_v2.0_Windows_Portable.zip`
  - 권장 패키지입니다. Python이나 xdelta를 따로 설치할 필요가 없습니다.
- macOS/Linux 또는 고급 사용자:
  `Moon_PS1_Korean_Patch_v2.0.zip`
- 직접 명령행으로 적용할 사용자:
  `moon_ps1_kr_v2.0_rev1_c5e58d0b.xdelta`

압축을 푼 뒤 `README_FIRST_KO.txt` 또는
[한국어 설치 안내](docs/INSTALL_KO.md)를 따르면 됩니다.

## 빠른 적용

Windows에서는 Portable ZIP을 완전히 푼 뒤
`apply_patch_windows.bat`을 실행합니다. macOS에서는 일반 패키지의
`apply_patch_macos.command`, Linux에서는 `apply_patch_linux.sh`를
실행합니다.

적용기는 원본 BIN/CUE와 패치 파일의 크기·SHA-256을 먼저 검사합니다.
성공하면 원본 옆의 별도 `Moon_Korean_v2.0` 폴더에 결과를 만들며 원본을
수정하거나 덮어쓰지 않습니다. 에뮬레이터에서는 새 폴더의 CUE 파일을
여세요.

v1.0이나 v1.1 결과에 덧붙이는 패치가 아닙니다. 반드시 깨끗한 일본판
Rev 1 원본에서 시작해야 합니다.

## 숨겨진 메뉴 빠른 안내

1. `PUSH START` 화면에서 `START`를 누릅니다.
2. 원래 Game Start/Continue 화면이 나오면 `SELECT`를 누릅니다.
3. 노란색 `*미사용 개발 자료`를 `○` 버튼으로 고릅니다.
4. 스포일러 확인에서 `예`를 선택합니다.

자료관에서는 `○`·`→`·`↓`로 다음 화면, `←`·`↑`로 이전 화면,
`×`로 목록에 돌아갑니다. 자세한 조작과 콘텐츠 성격은
[숨겨진 콘텐츠 안내](docs/HIDDEN_CONTENT_GUIDE_KO.md)를 확인하세요.

## 지원 원본과 결과

| 구분 | 크기 | SHA-256 |
|---|---:|---|
| 지원 원본 Rev 1 BIN | 640,491,936 bytes | `828189dd7cba0211585c9e06a99936924f0fb883da428525f1fc73790fb403f2` |
| 한국어 패치 v2.0 BIN | 640,491,936 bytes | `c5e58d0b9030a0f8683126f2866b633c70e6ea5e12c699524dfece1c67fcc43d` |
| 원본·결과 CUE | 108 bytes | `031a35316b96460c474e3a6a99bd2dfb98e6408dedd8ceadffc49faf20d77482` |

트랙 구조는 단일 `TRACK 01 MODE2/2352`,
`INDEX 01 00:00:00`입니다. 파일 이름보다 위 크기와 SHA-256이 판정
기준입니다.

## 호환성과 검증 범위

- Mednafen PSX 빌드 `013d057`: 본편과 v2.0 추가 콘텐츠·최종 수정 검증
- DuckStation: v1.1 사용자 구동·플레이 확인
- PS2 실기 POPS 환경: v1.1 외부 사용자 구동 확인
- 일반 메모리카드 저장: 호환 확인, 사용 전 백업 권장
- 원본 PlayStation 본체, PSP POPS/EBOOT.PBP, 그 밖의 실행 환경:
  v2.0 미검증
- 서로 다른 패치 BIN에서 만든 에뮬레이터 savestate: 지원하지 않음

이전 버전의 외부 확인 기록을 v2.0 추가 콘텐츠까지 검증한 것으로
확대하지 않습니다. 자세한 범위는
[호환성 문서](docs/COMPATIBILITY.md)를 참고하세요.

## 주의사항

- 원본 BIN/CUE와 메모리카드 저장은 반드시 별도로 보관하세요.
- 다른 패치 버전의 savestate를 불러오지 말고, 게임 내 저장 뒤
  에뮬레이터를 완전히 종료해 새 CUE로 콜드 부팅하세요.
- 숨겨진 자료 메뉴에서는 일반 게임 저장을 진행하지 않도록 보호했지만,
  중요한 저장 데이터의 백업을 대체하지는 않습니다.
- `용의꼬리(미사용 엔딩)`은 완성 이벤트 하나의 잠금을 푼 것이 아니라,
  디스크에 남은 여러 장면을 조사해 연결한 재구성판입니다.
- 음성만 존재하는 일부 오프닝·엔딩 대사 자막은 별도 연구 범위입니다.

## 더 읽기

- [v2.0 릴리스 노트](RELEASE_NOTES_v2.0.md)
- [숨겨진 콘텐츠 안내](docs/HIDDEN_CONTENT_GUIDE_KO.md)
- [v2.0 작업기](docs/V2_0_WORKLOG_KO.md)
- [설치 안내](docs/INSTALL_KO.md)
- [자주 묻는 질문](docs/FAQ_KO.md)

## 오류 제보

[Issues](https://github.com/enthhende/moon-remix-rpg-adventure-korean-patch/issues)에
다음 정보를 적어 주세요.

- 패치 버전과 완성 BIN SHA-256
- 에뮬레이터 이름·버전 또는 실기 본체 모델
- 재현 위치, 직전 행동, 메모리카드/새 게임 여부
- 가능하다면 화면과 로그

원본·패치된 BIN/CUE, BIOS, 메모리카드 전체 덤프와 savestate는
업로드하지 마세요.

## 저작권과 라이선스

이 프로젝트는 원작 개발사·배급사·현재 권리자와 무관한 비공식 팬 번역
프로젝트입니다. 게임명, 캐릭터, 시나리오, 그래픽, 음원과 그 밖의 원작
권리는 각 권리자에게 있습니다. 자세한 내용은 [법적 고지](LEGAL.md)와
[라이선스 범위](LICENSING.md)를 확인하세요.

사용 글꼴의 원저작권과 OFL-1.1 고지는 [크레딧](CREDITS.md)과
`LICENSES/OFL-1.1.txt`에 보존합니다.
