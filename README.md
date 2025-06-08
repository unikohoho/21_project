# 21_project

-------------------------------------------------------------------------

📁 1. 워크북 (Workbook)<br>

실행 경로<br>
workbook/main.py<br>

keys 폴더 생성 후  openai_key.txt 파일에 api key 입력 <br>

-------------------------------------------------------------------------

💬 2. 챗봇 (ChatBot)<br>

실행 경로<br>
chatBot/main.py<br>

keys 폴더 생성 후  openai_key.txt 파일에 api key 입력 <br>

-------------------------------------------------------------------------

🏠 3. 홈캠 대화 분석 시스템 (HomeCam)<br>

- 별도의 가상환경 설정 및 패키지 설치가 필요합니다.<br>

실행 경로<br>
#폴더 이동<br>
cd "HomeCam FILE"<br>
#가상 환경 설치<br>
python -m venv py39_homecam<br>
#가상 환경 실행<br>
py39_homecam\Scripts\activate<br>
#pip upgrade<br>
python -m pip install --upgrade pip<br>
#requirements.txt 설치 (HomeCam 내부)<br>
pip install -r requirements.txt<br>
python main.py<br><br>

<필수 확인 사항>
1. pip 업그레이드_python -m pip install --upgrade pip<br>
2. ffmpeg 설치<br>
   https://ffmpeg.org/download.html 에서 플랫폼에 맞게 다운로드<br>
   설치 후 실행파일 경로를 환경변수(PATH) 에 추가하거나, 프로젝트 내에 직접 지정<br>
3. Python 버전_3.9 사용 권장 (Whisper 및 Pyannote 호환성 이슈 대비)<br><br>
   
Claude API Key, Hugging Face Token 입력 후 실행 가능<br>

-------------------------------------------------------------------------

시연 영상 url: https://youtu.be/Xx3EVTTmDR0<br>
