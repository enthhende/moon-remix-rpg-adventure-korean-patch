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
- Switch IPS32+2 pack 배포 경로와 macOS exact 새 설치 경로의 확인 근거 보존
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
`release_manifest.json`은 보존된 PS1 범위입니다. 새 플랫폼의 권리·동의 상태가 자동으로
승인되는 것은 아니며 각 패키지의 라이선스 문서를 개별 검수합니다.
