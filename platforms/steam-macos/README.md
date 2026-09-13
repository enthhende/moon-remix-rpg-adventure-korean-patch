# Steam macOS 한국어 패치

대상 관찰 원본은 Steam App ID `1714580`, Build ID `23044446`의 macOS판입니다.
실행 경로는 x86_64이며 Apple Silicon 원생 arm64 지원을 의미하지 않습니다.

배포 파일 `moon-steam-macos-korean-rc-001.zip`은 950,528 bytes입니다.
SHA-256: `8d50e01c759fd0078bc9da95e801888e2c7a26bd3e4db2cd70b4cde9e68c250f`.
기존 XINGISKAN 자동주행 보조 ZIP은 한글패치 본체가 아닙니다.

배포 적용기는 사용자가 소유한 정확한 원본의 **새 복사본**에만 적용합니다.
Steam 설치 원본·세이브·Cloud 설정은 건드리지 않습니다. exact 설치 결과의 x86_64 실행,
Steam API 오류 없음, 대표 한국어 자료관·진입 문구, 정상 종료·무크래시를 확인했습니다.
R9 남단 복귀 화면은 별도 관찰하지 않았으므로 runtime PASS로 주장하지 않습니다.

Finder의 app 더블클릭, Steam 원본 Play 버튼으로 별도 복사본 실행, Gatekeeper/notarization,
arm64 원생 실행은 지원 주장 범위가 아닙니다. 게임 전체 앱이나 개발용 디버거·배속 도구는
배포하지 않습니다. ZIP 안의 설치 안내와 제공된 command 실행 경로를 따르세요.
