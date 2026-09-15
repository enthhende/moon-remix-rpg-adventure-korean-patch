# 합동 배포·재현 계약

이 저장소는 네 플랫폼의 배포 창구입니다. 개발 저장소를 합치거나 플랫폼별 검증을
서로 승계하지 않습니다. 합동 공개 버전은 v2.0이며 플랫폼 자산의 검증된 바이트를 유지합니다.

## 기존 PS1 ZIP 보존

PS1 v2.0 두 ZIP과 독립 xdelta, `SHA256SUMS.txt`는 검증된 바이트 그대로 사용합니다.
통합 checksum은 `JOINT_SHA256SUMS.txt`로 따로 생성하며 PS1 checksum을 덮어쓰지 않습니다.
Windows ZIP도 변경할 이유가 없으면 재생성하거나 내부 파일명을 바꾸지 않습니다.

PS1 ZIP의 빌드 소스는 커밋 `7ed58079145a8ddd0236d338ad3e0a4e765d8558`입니다.
이후 합동 README는 PS1 ZIP 안의 README와 다릅니다. 그러므로 PS1 ZIP 재현은 **그 커밋의
별도 깨끗한 복제본**에서 기존 builder와 검증된 외부 xdelta 입력으로 수행합니다.
합동 트리의 PS1 builder는 재생성을 거부합니다. 적용기 자체는 기존 PS1 기능을 유지합니다.
태그를 새 합동 커밋에 붙여도 PS1 asset의 생성 커밋은 바꾸어 기록하지 않습니다.

## 게시 전 체크

- 플랫폼별 정확한 지원 원본·출력·ZIP 해시, 테스트 범위와 미검증 항목을 공개 원장에 결속
- Switch IPS32+2 pack 배포 경로, moon 전용 언어 설정과 macOS exact 새 설치 경로의 근거 보존
- 새 패키지의 A/B 결정성·독립 적용·라이선스·경로 및 금지 파일 검사
- ZIP 다운로드 링크는 실제 게시 후 검증; 준비 중 파일을 공개 완료로 표현하지 않음
- 기존 v1.0/v1.1 태그·릴리스와 PS1 이력 보존
- 전체 게임 파일·개인 경로·저장 데이터·디버그 로그는 Git과 Release 자산에서 제외

배포 대상은 동결된 플랫폼 자산 7개와 `joint_release_manifest.json`,
`JOINT_SHA256SUMS.txt`의 총 9개입니다. Switch 실기, macOS R9 남단 화면, Windows 물리
controller·대학 칠판 화면은 각각 별도 미관찰 제한이며 다른 정적·에뮬레이터·플랫폼 PASS로
바꾸지 않습니다.

public manifest의 `RELEASE_ARTIFACTS_APPROVED`는 배포 파일의 검증과 공개 승인을 뜻합니다.
실제 게시 상태는 [v2.0 Release](https://github.com/enthhende/moon-remix-rpg-adventure-korean-patch/releases/tag/v2.0)가
소유합니다. 따라서 게시 전후에 같은 manifest와 checksum으로 배포 파일을 검사할 수 있습니다.

현재 루트 `LICENSE`, `LEGAL.md`, `LICENSING.md`, `CREDITS.md`와
`release_manifest.json`은 PS1 범위입니다. 다른 플랫폼의 크레딧·라이선스는 각 배포
패키지에 포함된 문서를 확인하세요.

## v2.0 Eden 추가 배포

Eden 전용 ZIP과 `EDEN_SHA256SUMS.txt`를 기존 v2.0 Release에 추가합니다.
위의 최초 9개 자산과 `joint_release_manifest.json`은 당시 검증값을 보존하며,
추가 자산은 `platforms/switch/eden_release_manifest.json`이 소유합니다.
기존 태그를 이동하지 않고 현재 main의 안내·builder·원장을 커밋합니다.

재현: 공개 v2.0 `0100E1800EFCE000.zip`을 받아 다음 명령을 실행합니다.

```sh
python3 scripts/build_eden_bundle.py --switch-zip 0100E1800EFCE000.zip --out-dir dist
```

builder는 원본 ZIP과 payload 해시를 검증하고 IPS32·pack·크레딧·OFL을 원본 그대로
Eden 폴더에 배치합니다. 설치 안내와 내부 체크섬을 함께 넣으며 실행 파일·게임·키·세이브는
입력받지 않습니다. 파일 순서·시간·권한과 무압축 ZIP 저장을 고정해 재현성을 확보합니다.
Git에는 builder·문서·원장을, Release에는 ZIP·외부 checksum을 게시합니다.
새 ZIP의 정적 무결성 검증과 기존 macOS Eden 실행 증거는 Android 설치·실행의 검증과 구분합니다.
