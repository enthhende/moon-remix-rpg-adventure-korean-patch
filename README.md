# moon: Remix RPG Adventure 한국어 패치

PS1·Nintendo Switch·Steam macOS·Steam Windows용 비공식 한국어 패치를 안내하는
합동 배포 저장소입니다. 게임 본체·ROM·BIOS·키·세이브는 제공하지 않습니다.
각 플랫폼에 맞는 정품 원본이 필요하며, 다른 플랫폼의 패치를 섞어서 적용할 수 없습니다.

> 합동 릴리스 준비 초안입니다. 아래 준비 상태를 게시 완료로 해석하지 마세요.
> 기존 공개 v1.0/v1.1은 PS1판입니다. 새 네 플랫폼 릴리스의 공개 버전과 게시일은 미확정입니다.

## 플랫폼을 먼저 고르세요

| 플레이할 게임 | 설치 안내 | 준비 상태 |
|---|---|---|
| PlayStation 일본판 Rev 1 | [PS1](platforms/ps1/README.md) | v2.0 일반·Windows Portable 패키지 준비 |
| Nintendo Switch 업데이트 1.1.2 | [Switch](platforms/switch/README.md) | v146 배포 경로 확인·canonical ZIP 준비 |
| Steam macOS | [macOS](platforms/steam-macos/README.md) | 적용기·exact 설치 결과 실행 확인·ZIP 준비 |
| Steam Windows | [Windows](platforms/steam-windows/README.md) | RC002 패키지 준비, 알려진 미검증 항목 명시 |

`PS1 Windows Portable`은 **PS1 게임에 패치를 적용하는 Windows용 도구**입니다.
Steam Windows판 패치와 다릅니다. 다운로드는 `Code → Download ZIP`이 아닌
[Releases](https://github.com/enthhende/moon-remix-rpg-adventure-korean-patch/releases)에서
해당 릴리스가 실제 게시된 것을 확인한 후 선택하세요.

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
플랫폼별 크레딧·라이선스는 각 배포 패키지를 따르며 PS1 승인 범위를 다른 플랫폼에
자동으로 확대하지 않습니다. [배포·재현 계약](JOINT_RELEASE_CONTRACT.md)과
[합동 v2.0 릴리스 노트](RELEASE_NOTES_JOINT_v2.0.md)를 참고하세요.
