# moon 한국어 패치 합동 v2.0 릴리스 노트

이번 합동 릴리스는 PS1의 v1.1 후속인 v2.0과 Nintendo Switch, Steam macOS, Steam Windows 패치를
한 저장소의 플랫폼별 안내와 GitHub Release 자산으로 제공합니다. 각 패치는 서로 다른 정품
원본 전용이며 다른 플랫폼의 파일을 섞어 적용할 수 없습니다.

## PS1 — 공개 v1.1 이후 변경점

- Game Start/Continue 화면에서 `SELECT`로 여는 `미사용 개발 자료` 메뉴를 추가했습니다.
- 이미지 16장과 한국어 해설을 합친 총 48화면의 `보너스 자료관`을 추가했습니다.
- 미사용 장면을 재구성한 `용의꼬리(미사용 엔딩)`과 `소년과 할머니`를 추가했습니다.
  숨겨진 모드에서는 저장을 막고 안전 출구와 타이틀 복귀를 제공합니다.
- 일반 대화에서 이름의 `♥`·`@`가 다른 기호로 바뀌던 문제를 수정했습니다.
  이름 끝의 특수문자를 건너뛰고 마지막 한글의 받침에 맞춰 조사·호격을 선택합니다.
- 데이터 삭제 질문의 글자 겹침, 무츠지로 호칭(`〔이름〕씨~`), `타마야 공방`,
  `어이, 우타코!` 등 본편·엔딩 문구와 줄바꿈을 교정했습니다.
- 최대 7자 이름을 고려해 엔딩의 3행 표시와 줄 경계를 보강했습니다.
- 영문·특수문자 글리프를 조정하고 MD 제목·설명을 실제 글자 폭에 맞춰 가운데 정렬했습니다.

상세 내용은 [PS1 v2.0 릴리스 노트](https://github.com/enthhende/moon-remix-rpg-adventure-korean-patch/blob/v2.0/RELEASE_NOTES_v2.0.md)를
참고하세요.
v1.0/v1.1 패치 결과에 덧붙이지 말고 깨끗한 일본판 Rev 1 원본에 직접 적용하세요.

## 숨겨진 메뉴 진입 방법

숨겨진 메뉴는 최초 `PUSH START` 화면에서 바로 열리지 않습니다. 먼저 일반 입력으로
`GAME START / CONTINUE` 선택 화면까지 이동한 뒤 다음 키를 누르세요.

- PS1: `SELECT`
- Switch: `-`
- Steam macOS/Windows: 키보드 `N`

주의 안내를 확인하면 `미사용 개발 자료` 메뉴로 들어갑니다. 추가 자료에는 본편 결말
스포일러가 있으므로 본편을 끝낸 뒤 감상하는 것을 권합니다.

## 다운로드와 적용

- PS1: Windows에서는 `Moon_PS1_Korean_Patch_v2.0_Windows_Portable.zip`을 풀고
  `apply_patch_windows.bat`을 실행합니다. macOS·Linux는 일반 ZIP을 선택합니다.
- Switch: `0100E1800EFCE000.zip` 안의 설치 안내에 따라 IPS32와 pack 2개를 함께 설치합니다.
- Steam macOS: macOS ZIP 안의 적용기로 원본의 새 복사본을 만들고 제공된 command로 실행합니다.
- Steam Windows: Windows ZIP을 게임의 로컬 파일 폴더에 풀고 생성된 폴더 안의
  `INSTALL_KO.bat`을 더블클릭합니다. 제거는 게임 종료 후 `UNINSTALL_KO.bat`입니다.

[플랫폼별 설치 안내](https://github.com/enthhende/moon-remix-rpg-adventure-korean-patch/tree/main/platforms)를
먼저 확인하세요. 아래 Assets에서 받으며 `Source code (zip/tar.gz)`는 패치 패키지가 아닙니다.
파일명의 `rc`와 Switch 내부 `v146`은 동결된 패키지 식별자이며 합동 공개 버전은 v2.0입니다.

## 릴리스 자산

| 플랫폼 | 파일 | bytes | SHA-256 |
|---|---|---:|---|
| PS1 | `Moon_PS1_Korean_Patch_v2.0.zip` | 1,154,582 | `f8a75d10c19a7914c82763136b8e990e4741201bec11ac21ba24286c0a3f0d7e` |
| PS1/Windows 적용기 | `Moon_PS1_Korean_Patch_v2.0_Windows_Portable.zip` | 1,304,674 | `68fbb6b87d8613485c5208d43d202897b39f377f2231a6e18e74508f769237c3` |
| PS1 직접 적용 | `moon_ps1_kr_v2.0_rev1_c5e58d0b.xdelta` | 1,117,444 | `2fa620c700d7b21adb2a35709a67a0bc166da34f3dffbcd04d6036bb5be97b16` |
| PS1 checksum | `SHA256SUMS.txt` | 315 | `9f563db4b9c6e7b4d78b1398e310c58a827caa08c029e87966d477cb0c2df3d0` |
| Switch | `0100E1800EFCE000.zip` | 958,467 | `c62aad4320a74748007ef1faf6c4f08ccfe1a25f48ff4d19edfe51886ce8d8d0` |
| Steam macOS | `moon-steam-macos-korean-rc-001.zip` | 950,528 | `8d50e01c759fd0078bc9da95e801888e2c7a26bd3e4db2cd70b4cde9e68c250f` |
| Steam Windows | `moon-windows-korean-final-rc-003-release.zip` | 1,589,924 | `c0e25acef9a5a156a309205b4878549a05ac1f2b221ecf577081859e4d3c0f09` |

`joint_release_manifest.json`은 위 자산의 플랫폼·크기·SHA-256과 검증 한계를 기록합니다.
`JOINT_SHA256SUMS.txt`는 위 7개 자산과 public manifest를 검사하며 자기 자신은 포함하지
않습니다. `SHA256SUMS.txt`는 PS1 전용 체크섬입니다.

## 플랫폼별 핵심

- PS1 v2.0: 숨은 메뉴, 48면 자료관, 용의꼬리, 소년과 할머니, 이름·조사·MD·문구 교정을
  포함합니다. v2.0 추가 콘텐츠는 Mednafen PSX에서 확인했습니다. DuckStation·PS2 POPS는
  v1.1 당시 기록이며 v2.0 추가 콘텐츠는 별도 미검증입니다. 원본 PS1·PSP POPS도 미검증입니다.
- Switch: 업데이트 1.1.2의 IPS32 1개와 pack 2개만 배포합니다. Eden의 실제 배포 형태
  실행을 확인했습니다. Atmosphère 실기에서는 직접 검증하지 않았습니다.
- Steam macOS: Build ID 23044446의 정확한 원본으로 새 복사본을 만드는 patch-only
  적용기입니다. x86_64 전용 command 실행만 지원하며, `소년과 할머니`의 남쪽 출구에서
  타이틀로 복귀하는 화면은 별도로 확인하지 않았습니다.
- Steam Windows: Build ID 23044446용 patch-only RC003입니다. `INSTALL_KO.bat`과
  `UNINSTALL_KO.bat`을 더블클릭해 적용·제거하며 PowerShell 명령을 직접 입력하지 않습니다.
  배치파일을 통한 설치·제거·재설치를 확인했습니다. 실제 컨트롤러 조작과 대학 칠판
  화면은 검증하지 않았습니다.

세이브와 Cloud는 패치 설치 대상이 아닙니다. 게임 본체·ROM·전체 실행 파일·키·세이브는
어느 자산에도 포함하지 않습니다. Windows↔macOS 세이브 로드·재저장 확인은 모든 Cloud
충돌 상황의 자동 해결 보증이 아닙니다. 미사용 개발 자료에는 본편 결말 스포일러가 있습니다.
