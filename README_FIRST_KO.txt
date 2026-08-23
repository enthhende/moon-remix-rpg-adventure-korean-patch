moon: Remix RPG Adventure PS1 한국어 패치 v2.0
================================================

이 패키지는 게임 전체가 아니라 xdelta 방식의 비공식 한국어 패치입니다.
합법적으로 준비한 일본판 Rev 1 BIN/CUE가 필요합니다.

Windows 10/11 64비트 권장 방법
-----------------------------

1. Moon_PS1_Korean_Patch_v2.0_Windows_Portable.zip을 완전히 풉니다.

2. apply_patch_windows.bat을 실행합니다.
   Python이나 xdelta를 따로 설치할 필요가 없습니다.

3. 요청이 나오면 원본 Rev 1 BIN과 CUE를 지정합니다.

4. 성공하면 원본 옆의 Moon_Korean_v2.0 폴더가 만들어집니다.
   에뮬레이터에서는 그 폴더의 CUE 파일을 여세요.

macOS / Linux
-------------

Moon_PS1_Korean_Patch_v2.0.zip을 받고 Python 3과 xdelta3 3.2.0을
준비한 뒤 다음 파일을 실행합니다.

macOS   : apply_patch_macos.command
Linux   : apply_patch_linux.sh

xdelta3 공식 배포: https://github.com/jmacd/xdelta/releases/tag/v3.2.0

지원 원본 BIN SHA-256
828189dd7cba0211585c9e06a99936924f0fb883da428525f1fc73790fb403f2

완성 BIN SHA-256
c5e58d0b9030a0f8683126f2866b633c70e6ea5e12c699524dfece1c67fcc43d

숨겨진 자료 메뉴
----------------

PUSH START에서 START를 누른 뒤 원래 Game Start/Continue 화면에서
SELECT를 누릅니다. 노란색 *미사용 개발 자료를 ○ 버튼으로 선택하세요.
강한 결말 스포일러가 있으므로 본편 엔딩 뒤 열람을 권장합니다.

중요:
- v1.0/v1.1 결과에 덧붙이지 말고 깨끗한 Rev 1 원본에 적용하세요.
- 원본 BIN/CUE와 메모리카드 저장은 별도로 보관하세요.
- 다른 패치 BIN에서 만든 savestate는 사용하지 마세요.
- 일반 메모리카드 저장은 호환되지만 사용 전 백업을 권장합니다.
- v2.0 추가 콘텐츠는 Mednafen에서 확인했습니다. DuckStation·PS2 POPS는
  v1.1 당시의 사용자 확인이며, 원본 PlayStation 본체는 미검증입니다.
- 원본 또는 패치된 게임 이미지는 이 패키지에 포함되지 않습니다.

자세한 설치: docs/INSTALL_KO.md
숨겨진 메뉴: docs/HIDDEN_CONTENT_GUIDE_KO.md
v2.0 작업기: docs/V2_0_WORKLOG_KO.md
