# Nintendo Switch 한국어 패치

## 사용할 기기에 맞는 파일 선택

- **Switch 실기 / Atmosphère**: [0100E1800EFCE000.zip](https://github.com/enthhende/moon-remix-rpg-adventure-korean-patch/releases/download/v2.0/0100E1800EFCE000.zip). 아래 안내를 따르세요.
- **Eden PC / Android 환경**: [moon-korean-eden-v2.0.zip](https://github.com/enthhende/moon-remix-rpg-adventure-korean-patch/releases/download/v2.0/moon-korean-eden-v2.0.zip). [Eden 전용 설치 안내](EDEN_INSTALL_KO.md)를 따르세요.

두 ZIP의 한글 패치 데이터는 동일하며 설치 경로와 언어 설정 방법이 다릅니다.

## Switch 실기 설치 — Atmosphère

Atmosphère가 이미 작동하는 본체에서 사용합니다. 순정 본체의 일반 SD 카드에 복사하는 것만으로는
적용되지 않습니다. 아래 ZIP은 게임 본편·업데이트 설치 파일이 아닙니다.

1. moon의 **업데이트 1.1.2**를 준비하고 게임을 완전히 종료합니다.
2. `0100E1800EFCE000.zip`을 풉니다.
3. 아래 `config.ini` 주의사항을 확인한 뒤 **`atmosphere` 폴더를 SD 카드 최상위에 합칩니다.**
   최상위의 기존 `atmosphere` 폴더 안에 다시 `atmosphere`를 넣으면 안 됩니다.
4. SD 카드를 본체에 돌려놓고 Atmosphère 환경에서 moon을 새로 실행합니다.

본체 언어가 한국어여도 동봉 설정으로 moon의 한국어 패치를 표시합니다.
설정 파일 병합이 필요한 경우는 아래 설명을 따르세요.

## 지원 대상과 파일

대상: 일본판 moon, Title ID `0100E1800EFCE000`, 업데이트 `1.1.2`,
Build ID `18D3CEE96E3A274AAD0CA5A140079A45`.
내부 후보 v146은 합동 공개 버전 번호와 별개입니다.

배포 파일 `0100E1800EFCE000.zip`은 IPS32 1개와 자료 pack 2개, moon 전용 언어 설정,
사용자 문서 및 Galmuri14의 OFL 1.1 전문으로 구성합니다. ROM·전체 main·NSP/XCI·키·
펌웨어는 포함하지 않습니다.

본체 언어가 한국어인 경우도 패키지를 그대로 설치하면 됩니다. 포함된 다음 설정이 moon만
일본어 언어 슬롯으로 실행해 그 슬롯의 한국어 패치를 표시합니다. Switch 본체의 전체 언어
설정은 바뀌지 않습니다.

```ini
[override_config]
override_language=ja
```

설치할 때 ZIP 안의 `atmosphere` 폴더를 SD 카드 루트에 합치세요. 단,
`atmosphere/contents/0100E1800EFCE000/config.ini`가 이미 있다면 먼저 백업하고 파일 전체를
덮어쓰지 마세요. 기존 `[override_config]` 섹션에 `override_language=ja`를 한 번만 넣거나
같은 키의 값을 `ja`로 바꾸면 됩니다. 자세한 설치·제거법은 ZIP 내부 `INSTALL_KO.md`에
있습니다.

v146의 **IPS32+pack만 설치한 배포 경로**를 Eden에서 확인했습니다. 한국어 타이틀·세이브,
숨은 메뉴, 자료관 진입·표시·복귀, 용의꼬리 진입과 Plus+Minus 복귀가 정상이고 crash·비정상
대기는 없었습니다. Atmosphère 실기 직접 검증은 별도 `NOT_RUN`이며 Eden 결과로 대신하지
않습니다.

숨겨진 `미사용 개발 자료` 메뉴는 최초 `PUSH START` 화면이 아니라,
`GAME START / CONTINUE` 선택 화면에서 `-`를 누르면 열립니다.

ZIP: 958,838 bytes. SHA-256:
`21a8ea11d74a9af4f2be9e29c7258932e8e46d24168d0d29c2c723b321656c32`.
Releases의 checksum과
ZIP 내부 설치 안내를 함께 확인하세요.

## 제거

게임을 종료하고 이 패치의 IPS 1개와 pack 2개만 제거합니다.
`config.ini`를 기존 설정과 합쳤다면 `override_language=ja` 줄만 제거하거나 백업본으로 복원합니다.
다른 모드가 함께 있는 타이틀 폴더 전체를 지우지 마세요. 일반 세이브는 제거 대상이 아닙니다.
