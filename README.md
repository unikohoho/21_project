# 🍼 21\_project

EWHA CAPSTONE TEAM 21 투애니원의 프로젝트 **I\:ON 육아 가이드 서비스**입니다.

---

## 📁 1. 워크북 (workbook)

실행 전 `keys` 폴더를 생성한 후, `openai_key.txt` 파일에 **OpenAI API Key**를 입력합니다.

**실행 경로**
`workbook/main.py`

**실행 예시**

```bash
python3 workbook/main.py
```

---

## 💬 2. 챗봇 (chatbot)

실행 전 `keys` 폴더를 생성한 후, `openai_key.txt` 파일에 **OpenAI API Key**를 입력합니다.

**실행 경로**
`chatbot/main.py`

**실행 예시**

```bash
python3 chatbot/main.py
```

> 💡 챗봇에 입력할 질문을 수정하려면 `main.py`의 `question` 변수 값을 조정하세요.

---

## 🏠 3. 홈캠 대화 분석 시스템 (HomeCam)

실행 전 `keys` 폴더를 생성한 후, 다음 두 파일에 각각 내용을 입력합니다.

* `claude_key.txt`: Claude API Key
* `Huggingface_token.txt`: Hugging Face Access Token

**가상환경 설정 및 실행 방법**

```bash
# 폴더 이동
cd "HomeCam FILE"

# 가상 환경 생성
python -m venv py39_homecam

# 가상 환경 실행
py39_homecam\Scripts\activate

# pip 업그레이드
python -m pip install --upgrade pip

# requirements.txt 설치 (HomeCam 폴더 내부)
pip install -r requirements.txt

# 실행
python main.py
```

### ✅ 필수 확인 사항

1. `pip` 업그레이드

```bash
python -m pip install --upgrade pip
```

2. `ffmpeg` 설치 필요

* [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html) 에서 플랫폼에 맞는 버전 다운로드 후 설치
* 설치 후 실행파일 경로를 환경변수(PATH)에 추가하거나 프로젝트 내부에서 직접 경로 지정

3. **Python 3.9 사용 권장**

* Whisper 및 Pyannote 호환성 문제 방지

---

## 🎬 시연 영상

[https://youtu.be/Xx3EVTTmDR0](https://youtu.be/Xx3EVTTmDR0)
