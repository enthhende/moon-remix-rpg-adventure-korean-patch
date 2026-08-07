# moon PS1 한국어 패치 v1.1

v1.1은 공개 v1.0의 본편 번역과 검증 결과를 유지하면서, 사용자가 승인한
엔딩 이미지 5개를 한국어 그래픽으로 교체한 안정 업데이트입니다.

## 주요 변경

- `C07` 2개 페이지, `C14`, `C18`, `C22` 엔딩 이미지 한국어화
- 원래 고정 BPE 슬롯을 그대로 사용하며 포인터와 팔레트 변경 없음
- 승인하지 않은 엔딩 이미지와 원작 자산은 변경하지 않음
- C22 `~사과문~` 위에 남았던 희미한 원문 흔적 제거

## 검증

- 최종 BIN SHA-256:
  `4dcea06e752afabab4d525903815fc21f681718e1ff59952ff95da6f2992fb9c`
- 엔딩 이미지 5개 고정 슬롯 디코드·읽기 검증
- 다른 엔딩 이미지 77개와 엔딩 팔레트 54개 바이트 보존
- 포인터 변경 0개, 소유 범위 밖 변경 0바이트
- 수정된 31개 Mode2/Form1 섹터의 EDC/P/Q ECC 검증
- 진엔딩 사진 흐름, 인접 장면, 크레딧, `THANKS FOR PLAYING`, 숨은 메시지 확인
- Mednafen과 DuckStation 호환 확인
- 외부 사용자의 PS2 실기 POPS 구동 확인

PS2 POPS 확인은 원본 PlayStation 본체의 광학 실행 경로까지 검증한다는
뜻은 아닙니다. 원본 PS1 본체와 PSP EBOOT.PBP는 계속 미검증으로 구분합니다.

## 설치

정확한 일본판 Rev 1 원본 BIN/CUE에 v1.1 패치를 직접 적용합니다. v1.0에
덧붙이는 패치가 아니므로, 별도로 보관한 깨끗한 원본에서 시작하세요.

- Windows 권장: `Moon_PS1_Korean_Patch_v1.1_Windows_Portable.zip`
- macOS/Linux: `Moon_PS1_Korean_Patch_v1.1.zip`
- 단독 패치: `moon_ps1_kr_v1.1_rev1_4dcea06e.xdelta`

원본 또는 패치된 전체 게임 이미지와 역패치는 배포하지 않습니다.
