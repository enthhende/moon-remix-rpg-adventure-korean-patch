# moon: Remix RPG Adventure 한국어 패치

PS1·Nintendo Switch·Steam macOS·Steam Windows용 비공식 한국어 패치를 안내하는
합동 배포 저장소입니다. 게임 본체·ROM·BIOS·키·세이브는 제공하지 않습니다.
각 플랫폼에 맞는 정품 원본이 필요하며, 다른 플랫폼의 패치를 섞어서 적용할 수 없습니다.

합동 v2.0은 PS1 v2.0과 Switch·Steam macOS·Steam Windows 패치를 함께 제공합니다.
[v2.0 다운로드](https://github.com/enthhende/moon-remix-rpg-adventure-korean-patch/releases/tag/v2.0)에서
사용할 플랫폼의 파일 하나를 선택하세요. 기존 v1.0/v1.1은 PS1 전용 릴리스입니다.

## 플랫폼을 먼저 고르세요

| 플레이할 게임 | 설치 안내 | 다운로드할 파일 |
|---|---|---|
| PlayStation 일본판 Rev 1 | [PS1](platforms/ps1/README.md) | `Moon_PS1_Korean_Patch_v2.0_Windows_Portable.zip` (Windows 적용기) / `Moon_PS1_Korean_Patch_v2.0.zip` (macOS·Linux 적용기) |
| Nintendo Switch 업데이트 1.1.2 | [Switch](platforms/switch/README.md) | `0100E1800EFCE000.zip` |
| Steam macOS | [macOS](platforms/steam-macos/README.md) | `moon-steam-macos-korean-rc-001.zip` |
| Steam Windows | [Windows](platforms/steam-windows/README.md) | `moon-windows-korean-final-rc-003-release.zip` |

`PS1 Windows Portable`은 **PS1 게임에 패치를 적용하는 Windows용 도구**입니다.
Steam Windows판 패치와 다릅니다. 다운로드는 `Code → Download ZIP`이 아닌
[Releases](https://github.com/enthhende/moon-remix-rpg-adventure-korean-patch/releases)에서
선택하세요. Steam 파일명의 `rc`와 Switch 내부 번호 `v146`은 검증된 패키지 식별자입니다.
합동 공개 버전은 v2.0이며 파일명을 바꾸거나 다른 후보로 재패키징하지 않았습니다.

## 원본과 저장 데이터

파일 이름만 같아도 지원 원본이라는 뜻은 아닙니다. 각 적용기의 크기·SHA-256 검사를 따르세요.
원본에 직접 덮어쓰거나 이전 한글패치 위에 누적하지 마세요. Steam 두 운영체제는 원본과
패키지가 각각 다릅니다. 저장 데이터·Cloud 동기화는 패치 설치와 별개이며 적용기가 기존
세이브를 자동 복원하거나 Cloud 설정을 변경해서는 안 됩니다.

## 오류 제보와 이용 안내

Issues의 공통 양식에 플랫폼, 패키지 이름·버전, 검사 결과, 재현 순서를 적어 주세요.
전체 게임 파일·세이브·개인정보가 든 로그는 공개 첨부하지 마세요.
미사용 개발 자료에는 본편 결말 스포일러가 포함됩니다.

기존 루트의 `apply_patch.*`, `release_manifest.json`, `docs/INSTALL_KO.md`는 **PS1 전용**입니다.
[기존 PS1 설명](README_PS1_v2.0.md)과 라이선스 문서는 보존합니다.
플랫폼별 크레딧·라이선스는 각 배포 패키지에서 확인할 수 있습니다. [배포·재현 계약](JOINT_RELEASE_CONTRACT.md)과
[합동 v2.0 릴리스 노트](RELEASE_NOTES_JOINT_v2.0.md)를 참고하세요.
