# moon 한국어 패치 v2.0 — Eden 설치 안내

받을 파일: **moon-korean-eden-v2.0.zip**

준비물은 Eden에서 실행되는 moon 본편과 **업데이트 1.1.2**입니다.
이 ZIP에는 한글 패치만 들어 있습니다. 게임을 다시 합치거나 리팩할 필요가 없습니다.

## Android / Eden 환경

1. ZIP을 다운로드하고 파일 앱에서 압축을 풉니다.
2. Eden 게임 목록에서 **moon을 길게 누르고 → 추가 콘텐츠(Add-ons) → 설치 → 모드/치트**를 선택합니다.
   메뉴 이름은 Eden 버전과 표시 언어에 따라 조금 다를 수 있습니다.
3. 폴더 선택 화면에서 압축을 푼 **`moon-korean` 폴더 안으로 들어가 → 이 폴더 사용**을 누릅니다.
   바로 안에 `exefs`와 `romfs`가 함께 보여야 합니다. `exefs` 하나만 선택하면 안 됩니다.
4. 추가 콘텐츠 목록에서 **업데이트 1.1.2와 moon-korean**이 모두 활성화됐는지 확인합니다.
5. 아래의 **게임 언어 설정**을 마친 뒤 게임을 완전히 종료하고 다시 실행합니다.

Android에서는 이 폴더 설치 방식으로 Eden이 필요한 위치에 파일을 복사합니다.
`Android/data`에 직접 접근할 필요가 없습니다. ZIP 파일을 고를 수 없는 화면이라면
먼저 압축을 풀고 위 방법대로 폴더를 선택하세요.

## PC · Windows / macOS / Linux

1. Eden에서 moon을 우클릭하고 **Open Mod Data Location**을 누릅니다.
2. ZIP을 풀어 나온 **`moon-korean` 폴더 전체**를 열린 위치에 넣습니다.
3. **Configure Game → Add-Ons**에서 **업데이트 1.1.2와 moon-korean**을 모두 켭니다.
4. 아래의 **게임 언어 설정**을 마친 뒤 게임을 완전히 종료하고 다시 실행합니다.

ZIP/폴더 모드 가져오기 버튼이 있는 Eden 버전은 그 기능을 이용해도 됩니다.
설치 후 아래 폴더 구조인지 확인하세요.

## 게임 언어 설정 — 꼭 확인하세요

이 패치는 **일본어 슬롯에 한국어를 표시**합니다. Eden이 게임에 전달하는
**시스템 언어(System → Language)를 Japanese / 日本語**로 맞추세요.

- 게임별 설정에 System → Language가 있으면 **moon에만** Japanese를 지정합니다.
- 해당 항목이 없는 버전은 Eden 전체 설정의 **System → Language**에서 변경합니다.
  PC에서는 보통 **Emulation → Configure → System → Language**입니다.
  전체 설정을 바꾸면 다른 게임에도 영향을 줄 수 있으므로 필요하면 플레이 후 원래대로 돌리세요.

Eden 앱의 메뉴 표시 언어(App Language)나 Android 기기 언어를 바꾸는 것이 아닙니다.
실기 패키지에 있는 Atmosphère용 `config.ini`는 이 ZIP에 포함하지 않으며,
그 파일을 통한 자동 언어 설정을 Eden 설치 조건으로 삼지 않습니다.

## 정상 설치 구조

Eden의 moon 모드 위치는 `load/0100E1800EFCE000/`이며, 그 안이 다음과 같아야 합니다.

```text
moon-korean/
├─ exefs/
│  └─ 18D3CEE96E3A274AAD0CA5A140079A45.ips
├─ romfs/
│  ├─ Data/StreamingAssets/moon_bonus_gallery.pack
│  └─ moon_bonus_notice.pack
├─ INSTALL_KO.md
├─ CREDITS_AND_LEGAL_KO.md
├─ LICENSES/OFL-1.1.txt
└─ SHA256SUMS.txt
```

`moon-korean/moon-korean/exefs`처럼 폴더가 두 번 겹치면 안 됩니다.
IPS 파일의 이름·대소문자·`.ips` 확장자를 바꾸지 마세요.
이전 moon 한글 모드를 다른 이름으로 설치했다면 그 모드를 끄고 이번 모드 하나만 켭니다.

## 한국어가 안 나오면

먼저 **1.1.2 활성화 → moon-korean 활성화 → 게임 언어 Japanese → 완전 종료 후 재실행**을 확인하세요.

그래도 해결되지 않으면 Eden 로그에서 확인합니다. 로그 문구는 버전에 따라 달라질 수 있습니다.

| 확인 항목 | 해석과 조치 |
|---|---|
| `Querying NSO patch existence for build_id=...` | moon의 main Build ID가 `18D3CEE96E3A274AAD0CA5A140079A45`로 시작하는지 확인합니다. 다른 모듈의 Build ID 줄과 혼동하지 마세요. |
| main Build ID가 다름 | 지원 업데이트가 실제로 적용됐는지 확인합니다. 파일명만 1.1.2인 것으로는 부족합니다. |
| `Applying IPS patch from mod "moon-korean"`가 없음 | 모드 활성화 상태, exefs 경로와 IPS 파일명을 확인합니다. |
| IPS 적용은 확인됐는데 영어가 나옴 | 게임에 전달되는 시스템 언어와 게임별 덮어쓰기 설정을 확인합니다. |
| 본편은 한글인데 자료관에 문제가 있음 | 두 pack의 경로와 파일 누락을 확인합니다. |

제보할 때는 Eden 버전, PC/Android 구분, 게임 업데이트, 패키지 파일명과 해당 로그 줄을 알려주세요.
키·전체 게임·세이브·개인정보가 포함된 전체 로그는 공개 첨부하지 마세요.

## 제거 · 숨겨진 메뉴

Eden의 추가 콘텐츠에서 `moon-korean`을 끄면 비활성화됩니다. 제거하려면 게임을 종료한 뒤
추가 콘텐츠의 제거 기능 또는 PC의 Mod Data Location에서 `moon-korean` 폴더만 삭제합니다.
모드를 제거해도 일반 세이브를 삭제할 필요는 없습니다.

숨겨진 자료는 최초 PUSH START가 아닌 **GAME START / CONTINUE 화면에서 `-`**를 눌러 엽니다.
본편 결말 스포일러가 있으므로 엔딩 후 감상을 권합니다.

## 검증 범위 · 출처

패치 데이터 3개는 공개 v2.0 Switch ZIP의 v146 IPS32·pack과 바이트 단위로 같습니다.
기존 macOS Eden에서 이 3개 파일을 설치한 배포 경로의 한국어 타이틀·세이브·숨겨진 메뉴·
자료관·용의꼬리 진입과 복귀를 확인했습니다. 이번 ZIP은 경로와 문서를 정리한 패키지입니다.
새 ZIP의 Android / Eden 환경 설치 UI 및 실제 게임 실행은 별도로 미검증이며,
모든 Eden 버전이나 Switch 실기에서의 실행을 보증하는 것은 아닙니다.

- [공개 v2.0 다운로드](https://github.com/enthhende/moon-remix-rpg-adventure-korean-patch/releases/tag/v2.0)
- [Eden 공식 모드 안내](https://github.com/eden-emulator/mirror/blob/master/docs/user/Mods.md)
- [Eden 공식 Atmosphère 모드 재배치 안내](https://github.com/eden-emulator/mirror/blob/master/docs/user/InstallingAtmosphereMods.md)
- [Android 폴더 설치 구현](https://github.com/eden-emulator/mirror/blob/master/src/android/app/src/main/java/org/yuzu/yuzu_emu/fragments/AddonsFragment.kt)
