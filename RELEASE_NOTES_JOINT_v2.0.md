# moon 한국어 패치 합동 v2.0 릴리스 노트 (게시 전 후보)

이번 합동 릴리스는 기존 PS1 v2.0과 Nintendo Switch, Steam macOS, Steam Windows 패치를
한 저장소의 플랫폼별 안내와 GitHub Release 자산으로 제공합니다. 각 패치는 서로 다른 정품
원본 전용이며 다른 플랫폼의 파일을 섞어 적용할 수 없습니다.

## 릴리스 자산

| 플랫폼 | 파일 | bytes | SHA-256 |
|---|---|---:|---|
| PS1 | `Moon_PS1_Korean_Patch_v2.0.zip` | 1,154,582 | `f8a75d10c19a7914c82763136b8e990e4741201bec11ac21ba24286c0a3f0d7e` |
| PS1/Windows 적용기 | `Moon_PS1_Korean_Patch_v2.0_Windows_Portable.zip` | 1,304,674 | `68fbb6b87d8613485c5208d43d202897b39f377f2231a6e18e74508f769237c3` |
| PS1 직접 적용 | `moon_ps1_kr_v2.0_rev1_c5e58d0b.xdelta` | 1,117,444 | `2fa620c700d7b21adb2a35709a67a0bc166da34f3dffbcd04d6036bb5be97b16` |
| PS1 checksum | `SHA256SUMS.txt` | 315 | `9f563db4b9c6e7b4d78b1398e310c58a827caa08c029e87966d477cb0c2df3d0` |
| Switch | `0100E1800EFCE000.zip` | 956,335 | `a0b650c72f7a3f6f11b81f6826dc8aba857a55fe85e9aeaeeeaeaaecb835fc30` |
| Steam macOS | `moon-steam-macos-korean-rc-001.zip` | 950,528 | `8d50e01c759fd0078bc9da95e801888e2c7a26bd3e4db2cd70b4cde9e68c250f` |
| Steam Windows | `moon-windows-korean-final-rc-002-release.zip` | 1,587,997 | `77dbf8aeae794581d0b12c084d6dedadfec26afae30179dbefcad5120afbb25a` |

`joint_release_manifest.json`은 위 자산의 플랫폼·크기·SHA-256과 검증 한계를 기록합니다.
`JOINT_SHA256SUMS.txt`는 위 7개 자산과 public manifest를 검사하며 자기 자신은 포함하지
않습니다. 기존 `SHA256SUMS.txt`는 PS1 전용 파일로 그대로 보존됩니다.

## 플랫폼별 핵심

- PS1 v2.0: 숨은 메뉴, 48면 자료관, 용의꼬리, 소년과 할머니, 이름·조사·MD·문구 교정을
  포함합니다. 상세 변경은 기존 `RELEASE_NOTES_v2.0.md`를 따릅니다.
- Switch: 업데이트 1.1.2의 IPS32 1개와 pack 2개만 배포합니다. Eden의 실제 배포 형태
  runtime은 통과했지만 Atmosphère 실기 직접 검증은 `NOT_RUN`입니다.
- Steam macOS: Build ID 23044446의 정확한 원본으로 새 복사본을 만드는 patch-only
  적용기입니다. x86_64 전용 command 실행만 지원하며 R9 남단 복귀 화면은 별도 미관찰입니다.
- Steam Windows: Build ID 23044446용 patch-only RC002입니다. 실제 controller 경로와 대학
  칠판 화면은 공개된 `NOT_RUN` 제한입니다.

세이브와 Cloud는 패치 설치 대상이 아닙니다. 게임 본체·ROM·전체 실행 파일·키·세이브는
어느 자산에도 포함하지 않습니다. 이 문서는 게시 전 후보이며 실제 다운로드는 GitHub
Releases에 동일 자산과 checksum이 게시된 뒤에만 유효합니다.
