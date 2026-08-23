# moon PS1 한국어 패치 v2.0

v2.0은 숨겨진 미사용 자료 감상 기능과 두 재구성 이벤트를 추가하고,
실제 플레이에서 발견한 이름·문구·번역·글리프·MD 정렬 문제를 함께 다듬은
대규모 업데이트입니다.

## v1.1에서 새로 추가된 것

- Game Start/Continue 화면에서 `SELECT`로 진입하는 숨겨진
  `미사용 개발 자료` 메뉴
- 이미지 16장과 한국어 해설을 합친 총 48화면 `보너스 자료관`
- 미사용 장면을 안전한 흐름으로 재구성한
  `용의꼬리(미사용 엔딩)`
- 집 밖과 집 안 장면을 하나로 연결한 `소년과 할머니`
- 숨겨진 모드 저장 방지, 안전 출구와 타이틀 복귀

## 수정과 개선

- 이름의 `♥`와 `@`가 일반 대화에서 다른 문자로 바뀌던 문제 수정
- 이름 뒤 특수문자를 건너뛰어 마지막 한글로 조사·호격을 고르는
  주인공 이름 전용 역방향 스캐너 추가
- `이 데이터를 삭제하시겠습니까?` 문구 겹침 수정
- 무츠지로 호칭을 `〔이름〕씨~`로 교정
- `타마야 공방`, `어이, 우타코!`와 다수의 본편·엔딩 번역 및
  줄바꿈 교정
- 최대 7자 이름을 고려한 엔딩 3행·15코드 경계 보강
- Galmuri9/Galmuri14 기반 영문·특수문자 글리프 조정
- MD 제목·설명의 실제 4/8/16px 폭 기준 문장 전체 가운데 정렬
- 검수 도구의 일반 대사 3행 초과 필터와 승인 이력 반영 개선

## 다운로드

- Windows 10/11 64비트:
  `Moon_PS1_Korean_Patch_v2.0_Windows_Portable.zip`
- macOS/Linux:
  `Moon_PS1_Korean_Patch_v2.0.zip`
- 직접 적용:
  `moon_ps1_kr_v2.0_rev1_c5e58d0b.xdelta`

Windows Portable은 Python 설치가 필요 없으며 공식 xdelta3 3.2.0 Windows
x64 실행 파일과 Apache-2.0 고지를 포함합니다.

## 적용

1. 정확한 일본판 Rev 1 원본 BIN/CUE를 준비합니다.
2. Windows에서는 Portable ZIP을 완전히 푼 뒤
   `apply_patch_windows.bat`을 실행합니다.
3. 성공 후 `Moon_Korean_v2.0` 폴더에 생성된 CUE를 에뮬레이터에서
   엽니다.

v1.0이나 v1.1 결과에 덧붙이지 말고 깨끗한 일본판 Rev 1 원본에 직접
적용하세요.

## 고정 식별자

- 지원 원본 BIN SHA-256:
  `828189dd7cba0211585c9e06a99936924f0fb883da428525f1fc73790fb403f2`
- 완성 v2.0 BIN SHA-256:
  `c5e58d0b9030a0f8683126f2866b633c70e6ea5e12c699524dfece1c67fcc43d`
- v2.0 xdelta SHA-256:
  `2fa620c700d7b21adb2a35709a67a0bc166da34f3dffbcd04d6036bb5be97b16`

배포 ZIP의 체크섬은 릴리스에 함께 올린 `SHA256SUMS.txt`에서 확인할 수
있습니다.

## 숨겨진 메뉴

`PUSH START`에서 `START`를 누른 뒤 원래 Game Start/Continue 화면에서
`SELECT`를 누릅니다. 노란색 `*미사용 개발 자료`를 `○` 버튼으로
선택하세요.

강한 결말 스포일러가 있습니다. 자세한 조작은
`docs/HIDDEN_CONTENT_GUIDE_KO.md`, 개발 과정은
`docs/V2_0_WORKLOG_KO.md`를 확인하세요.

## 호환성 주의

v2.0의 추가 콘텐츠와 최종 수정은 Mednafen PSX에서 확인했습니다.
DuckStation과 PS2 POPS는 v1.1 당시의 사용자 확인 기록이며 v2.0 추가
콘텐츠는 별도 검증되지 않았습니다. 원본 PlayStation 본체와 PSP
POPS/EBOOT.PBP도 미검증입니다.

다른 패치 버전의 savestate는 사용하지 말고, 적용 전에 메모리카드와 원본을
백업하세요.

원본 또는 패치된 전체 게임 이미지와 내부 검증용 역패치는 배포하지
않습니다.
