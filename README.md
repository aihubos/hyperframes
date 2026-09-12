# hyperframes

**Omni Flash 360p → 기존 목소리 → 동영상·이미지 혼합 편집 → 쇼츠와 썸네일 저장**을 이어 주는 한국어 AI 에이전트 스킬입니다.

이 저장소는 사용자 제작 워크플로입니다. [HeyGen Hyperframes](https://github.com/heygen-com/hyperframes) 공식 엔진과 별개이며 렌더링에 그 엔진을 사용합니다. 모델 생성 서비스나 유료 계정을 포함하지 않습니다.

## AI에게 설치와 적용을 맡기기

아래 내용을 Codex 또는 Claude Code에 붙여 넣으세요.

```text
https://github.com/aihubos/hyperframes 저장소를 확인하고 README.md에 따라 설치해줘.
Git, Python 3, Node.js 22 이상, FFmpeg가 없으면 내 운영체제에 맞는 설치 방법으로 준비하고,
기존 파일은 백업한 뒤 install.py를 실행해줘. 계정 로그인이나 관리자 권한이 필요한 단계는 알려줘.
설치 후 SKILL.md를 직접 읽어 지금 요청부터 적용해줘.
동영상 생성은 Omni Flash 360p로 하고 장면별 길이는 직접 정해줘.
이미지·썸네일·영상은 ~/Projects/Youtube/영상 제목/에 저장해줘.
```

## 직접 설치

필수 도구: Git, Python 3, **Node.js 22 이상**, FFmpeg/ffprobe. GitHub 계정이나 GitHub CLI(`gh`)는 공개 저장소 설치에 필요하지 않습니다.

macOS에서 Homebrew가 이미 설치되어 있다면:

```bash
brew install git python node ffmpeg
```

Homebrew가 없다면 [공식 설치 안내](https://brew.sh/)를 따르세요. Windows/Linux는 [Git](https://git-scm.com/downloads), [Python](https://www.python.org/downloads/), [Node.js](https://nodejs.org/en/download), [FFmpeg](https://ffmpeg.org/download.html)의 운영체제별 설치 안내를 사용하세요. 이 설치 스크립트의 실제 검증 환경은 macOS입니다.

```bash
mkdir -p "$HOME/Projects"
git clone https://github.com/aihubos/hyperframes.git "$HOME/Projects/hyperframes-skill"
cd "$HOME/Projects/hyperframes-skill"
python3 install.py
```

이미 같은 경로에 이 저장소를 복제했다면 새로 clone하지 않고 변경 사항을 보존한 뒤 해당 폴더에서 업데이트하세요.

설치 스크립트는 다음을 수행합니다.

- 호환 엔진 Hyperframes 0.8.35를 `~/.local/share/hyperframes/runtime`에 설치하고 렌더링용 Chrome을 확인/준비합니다. 기존 엔진이 있으면 재사용합니다.
- Codex(`$CODEX_HOME/skills` 또는 `~/.codex/skills`), Claude(`~/.claude/skills`), 공용 에이전트(`~/.agents/skills`)에 `hyperframes` 스킬을 설치합니다.
- 기존 동명 스킬과 심볼릭 링크를 `~/.local/share/hyperframes/backups/`에 백업합니다. `restore.json`에 원래 경로를 남깁니다.

Codex만 설치하거나 엔진 설치를 생략할 수도 있습니다.

```bash
python3 install.py --skills-dir "$HOME/.codex/skills"
python3 install.py --skip-runtime
```

이미 엔진이 있는 프로젝트를 재사용하려면:

```bash
python3 install.py --runtime-dir "/absolute/path/to/existing/project"
```

설치 직후 AI에게 설치된 `SKILL.md`를 읽게 하면 현재 요청에 적용할 수 있습니다. 자동 스킬 목록은 앱을 재시작한 뒤 확인하세요. **설치가 곧 Omni·ElevenLabs 로그인이나 영상 생성 완료를 뜻하지는 않습니다.**

## 사용

```text
$hyperframes로 딱따구리를 주제로 45초 쇼츠를 만들어줘.
동영상과 이미지를 적절히 섞고, 기존 목소리·자막 스타일을 적용해줘.
썸네일과 유튜브 제목·설명도 함께 만들어줘.
```

기본값은 Omni Flash 360p, 45초 세로 쇼츠, Viraj 목소리, 흰색·검은 테두리의 짧은 자막, 빠른 줌·블러 전환입니다. 실제 생성 서비스에서 Omni Flash 360p를 지원하는지 확인하며, Google Flow/Veo로 임의 대체하지 않습니다. 기존에 사용하는 다른 목소리나 별도 요청이 있으면 그 지시를 우선합니다.

생성 원본과 결과는 `~/Projects/Youtube/영상 제목/` 안에 모입니다. 원본이 360p여도 최종 1080×1920 출력은 가능하며, 생성 원본과 출력 해상도를 구분해 기록합니다. 유튜브 업로드는 별도 요청 때만 진행합니다.

완성 영상 전달 시 **최종 채팅 답변에 유튜브 제목과 설명을 각각 복사 가능한 코드 블록으로 제공**하고, 동일한 내용을 `유튜브_제목과설명.txt`에도 저장합니다. 파일 링크만으로 제목·설명 전달을 대신하지 않습니다.

장면은 넓은 환경, 전신 동작, 부위 근접, 다양한 각도, 구조·비교 이미지를 내용에 맞게 섞습니다. 같은 옆모습을 반복하거나 동일 원본의 확대·반전만으로 채우지 않도록 생성 전 구도를 설계하고 결과 프레임을 비교합니다.

## 업데이트와 충돌

공식 Hyperframes의 `skills update` 명령이 같은 이름의 공식 스킬을 다시 설치할 수 있습니다. 이 사용자 워크플로를 복원하려면 이 저장소에서 `python3 install.py --skip-runtime`을 실행하세요. 기존 프로젝트의 엔진 버전은 임의로 변경하지 않습니다.

이 저장소에는 사용자 생성 영상·이미지·음성·쿠키·API 키를 포함하지 않습니다. 로그인은 각자의 계정으로 진행합니다.
