# 편집과 파일 전달

## 최소 Hyperframes 계약

호환 기준은 실제 제작에 사용한 CLI 0.8.35다. 설치된 CLI의 `--help`와 `docs`를 먼저 확인한다. 기존 편집 파일이 있으면 새 도구나 추상 구조를 만들지 말고 그것을 수정한다.

- 루트에 `data-composition-id`, `data-width="1080"`, `data-height="1920"`, `data-duration`를 선언한다.
- `class="clip"`, 고유 `id`, `data-start`, `data-duration`, `data-track-index`로 장면을 배치한다.
- GSAP을 사용한다면 paused timeline 하나를 `window.__timelines[compositionId]`에 등록한다. 시간·난수에 따라 매번 달라지는 애니메이션을 쓰지 않는다.
- `<video>`는 `muted playsinline`. 소리는 별도 `<audio id="...">`로 배치한다. 음성 id가 없으면 믹스에서 빠질 수 있다.
- 일반 `data-start` 래퍼 안에 다시 `data-start`가 있는 video를 넣지 않는다. 타이밍은 한 계층에만 둔다. 영상 전환은 시간 속성이 없는 래퍼를 움직인다.
- HTML에서 media의 play/pause/currentTime을 직접 제어하지 않는다. 엔진이 재생·추출을 소유한다.
- video/audio에 불필요한 `crossorigin`을 붙이지 않는다.
- 생성 원본보다 긴 슬롯을 만들지 않는다. 지원되는 재생 속도 또는 FFmpeg 전처리를 사용하고 시간을 다시 확인한다.
- 음악은 말보다 작게, 환경음은 대사를 가리지 않게 섞는다. atempo 사용 시 실제 출력 길이를 다시 측정한다.

## 기존 자막 기준

1080×1920 기준: 폭 970px, left 55px, top 약 1640px, 글자 약 62px, 검은 테두리 약 7px, `paint-order: stroke fill`, 굵은 Pretendard. 긴 문구는 분할하여 화면 밖으로 나가지 않게 한다. 기준 영상이나 플랫폼 UI 안전 영역에 맞춰 조정한다. 폰트는 설치된 파일 또는 사용 가능한 라이선스의 파일을 구해 프로젝트에 저장한다.

전환은 비시간 래퍼에 scale 약 1.12 → 1, blur 약 15px → 0, 약 0.32초. 첫 장면은 즉시 선명하게 보여 준다. 연구 설명 장면에는 간단한 출처와 `AI 재구성 · 원리 설명용`을 넣는다.

## 실행 명령

프로젝트 자체 엔진이 있으면 그 엔진을 사용한다. 설치 스크립트의 기본 엔진은 아래 위치에 있다.

```bash
HF="$HOME/.local/share/hyperframes/runtime/node_modules/.bin/hyperframes"
PROJECT="$HOME/Projects/Youtube/영상 제목"
"$HF" check "$PROJECT" --json
"$HF" render "$PROJECT" --quality high --fps 30 --workers 4 --output "$PROJECT/영상 제목.mp4"
ffprobe -v error -show_entries stream=codec_name,width,height,r_frame_rate:format=duration -of json "$PROJECT/영상 제목.mp4"
ffmpeg -v error -i "$PROJECT/영상 제목.mp4" -f null -
```

필요할 때 로컬 미리보기 서버를 사용한다. 사용 중인 포트를 종료하지 말고 빈 포트를 선택한다. 브라우저 파일 재생이 지원되면 서버는 필요 없다.

## 웹 서비스에서 저장

생성 완료 후 서비스의 공식 다운로드 버튼을 사용한다. 저장 대화상자는 웹 DOM에 안 보일 수 있으므로 네이티브 앱 상태를 확인한다. 원하는 제목 폴더의 assets 경로와 파일명을 지정하고 실제 파일 생성·미디어 정보를 확인한다. 다운로드 클릭만으로 저장 완료라고 말하지 않는다. 컴퓨터 사용 도구의 허용 범위를 따른다.

## 제작정보에 남길 내용

실제 제공 서비스·모델·해상도·원본 길이, 사용 목소리, 장면별 소스 파일, 출처와 과학 주장 범위, 생성 이미지의 한계, 자막 정렬 방식, 최종 출력 규격을 간단히 기록한다. 토큰·쿠키·서명 URL·사용자 계정 정보는 기록하지 않는다.
