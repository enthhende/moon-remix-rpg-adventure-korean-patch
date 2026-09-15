# moon 한국어 패치 합동 v2.0 릴리스 노트

## Eden PC·Android용 간편 설치 ZIP 추가

[moon-korean-eden-v2.0.zip](https://github.com/enthhende/moon-remix-rpg-adventure-korean-patch/releases/download/v2.0/moon-korean-eden-v2.0.zip)을 추가했습니다.
Switch판 **업데이트 1.1.2**가 필요하며, 패치 데이터는 기존 Switch ZIP의 v146과 동일합니다.

- **Android / Eden 환경**: ZIP 풀기 → moon 길게 누르기 → 추가 콘텐츠 → 설치 → 모드/치트 →
  `exefs`와 `romfs`가 바로 보이는 `moon-korean` 폴더 선택.
- **PC**: moon 우클릭 → Open Mod Data Location → ZIP의 `moon-korean` 폴더 넣기.
- 공통: 업데이트와 모드 활성화, 게임 시스템 언어 **Japanese**, 게임 완전 종료 후 재실행.
- **Switch 실기 / Atmosphère**: 기존 `0100E1800EFCE000.zip`을 사용합니다.

[Eden 설치 안내](https://github.com/enthhende/moon-remix-rpg-adventure-korean-patch/blob/main/platforms/switch/EDEN_INSTALL_KO.md) ·
[Switch 실기 설치 안내](https://github.com/enthhende/moon-remix-rpg-adventure-korean-patch/blob/main/platforms/switch/README.md)

추가 ZIP: 2,745,832 bytes / SHA-256
`a04c63b3ffb450048d140321c084cc5f5a9a8af713f424fb8aedbef5b296777e`.
추가 자산은 `EDEN_SHA256SUMS.txt`와 main의 `platforms/switch/eden_release_manifest.json`으로 확인합니다.
아래 최초 합동 배포 manifest·checksum의 7개 자산 범위는 그대로 유지됩니다.
크레딧·OFL 동봉과 3개 패치 데이터 동일성, ZIP 재현성을 검증했습니다.
기존 macOS Eden의 v146 실행 확인과 별개로 새 ZIP의 Android 설치·실행은 미검증입니다.

이번 합동 릴리스는 PS1의 v1.1 후속인 v2.0과 Nintendo Switch, Steam macOS, Steam Windows 패치를
한 저장소의 플랫폼별 안내와 GitHub Release 자산으로 제공합니다. 각 패치는 서로 다른 정품
원본 전용이며 다른 플랫폼의 파일을 섞어 적용할 수 없습니다.

## Switch 배포 수정

본체 언어가 한국어인 환경에서도 별도 언어 변경 없이 한국어 패치를 표시하도록 moon 전용
`config.ini`를 Switch ZIP에 포함했습니다. 이 설정은 moon만 일본어 언어 슬롯으로 실행하며
본체 전체 언어는 바꾸지 않습니다. 기존 moon용 `config.ini`가 있다면 덮어쓰기 전에 백업하고
ZIP 내부 설치 안내에 따라 `override_language=ja`를 병합하세요. IPS32와 두 자료 pack은
기존 v146 공개본과 byte-identical합니다.

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
- Switch: `0100E1800EFCE000.zip`의 `atmosphere` 폴더를 SD 카드 루트에 합칩니다.
  moon용 `config.ini`가 이미 있다면 ZIP 내부 설치 안내에 따라 설정을 병합합니다.
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
| Switch | `0100E1800EFCE000.zip` | 958,838 | `21a8ea11d74a9af4f2be9e29c7258932e8e46d24168d0d29c2c723b321656c32` |
| Steam macOS | `moon-steam-macos-korean-rc-001.zip` | 950,528 | `8d50e01c759fd0078bc9da95e801888e2c7a26bd3e4db2cd70b4cde9e68c250f` |
| Steam Windows | `moon-windows-korean-final-rc-003-release.zip` | 1,589,924 | `c0e25acef9a5a156a309205b4878549a05ac1f2b221ecf577081859e4d3c0f09` |

`joint_release_manifest.json`은 위 자산의 플랫폼·크기·SHA-256과 검증 한계를 기록합니다.
`JOINT_SHA256SUMS.txt`는 위 7개 자산과 public manifest를 검사하며 자기 자신은 포함하지
않습니다. `SHA256SUMS.txt`는 PS1 전용 체크섬입니다.

## 플랫폼별 핵심

- PS1 v2.0: 숨은 메뉴, 48면 자료관, 용의꼬리, 소년과 할머니, 이름·조사·MD·문구 교정을
  포함합니다. v2.0 추가 콘텐츠는 Mednafen PSX에서 확인했습니다. DuckStation·PS2 POPS는
  v1.1 당시 기록이며 v2.0 추가 콘텐츠는 별도 미검증입니다. 원본 PS1·PSP POPS도 미검증입니다.
- Switch: 업데이트 1.1.2의 IPS32 1개, pack 2개와 moon 전용 언어 설정을 배포합니다.
  본체 언어가 한국어여도 moon이 한국어 패치가 들어 있는 언어 슬롯을 선택합니다. 기존
  게임 payload의 Eden 배포 형태 실행은 확인했으며, 이번 설정 포함 수정본의 Atmosphère
  실기 직접 검증은 별도입니다.
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
