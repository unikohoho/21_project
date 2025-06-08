# 21_project

-------------------------------------------------------------------------

📁 1. 워크북 (Workbook)
실행 경로: Workbook/main.py

OpenAI Key 입력 후 실행 가능

-------------------------------------------------------------------------

💬 2. 챗봇 (ChatBot)
실행 경로: ChatBot/main.py 

OpenAI Key 입력 후 실행 가능

-------------------------------------------------------------------------

🏠 3. 홈캠 대화 분석 시스템 (HomeCam)

- 별도의 가상환경 설정 및 패키지 설치가 필요합니다.

실행 경로
python -m venv py39_homecam #가상 환경 설치\n
py39_homecam\Scripts\activate #가상 환경 실행\N
python -m pip install --upgrade pip #pip upgrade
pip install -r requirements.txt #requirements.txt 설치 (HomeCam 내부)
python main.py

<필수 확인 사항>
1. pip 업그레이드_python -m pip install --upgrade pip
2. ffmpeg 설치
   https://ffmpeg.org/download.html 에서 플랫폼에 맞게 다운로드
   설치 후 실행파일 경로를 환경변수(PATH) 에 추가하거나, 프로젝트 내에 직접 지정
3. Python 버전_3.9 사용 권장 (Whisper 및 Pyannote 호환성 이슈 대비)
   
Claude API Key, Hugging Face Token 입력 후 실행 가능

-------------------------------------------------------------------------

시연 영상 url: https://youtu.be/Xx3EVTTmDR0
