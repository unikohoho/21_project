# 21_project

EWHA CAPSTONE TEAM 21 투애니원의 프로젝트 I:ON 육아 가이드 서비스입니다.<br>

21_project/ <br>
├── HomeCam/ # 대화 감정 분석 및 리포트 생성 시스템 <br>
├── chatbot/ # GPT 기반 육아 전문 상담 챗봇 <br>
├── workbook/ # 육아 준비용 워크북 <br>
├── data/ # 샘플 오디오 및 리포트 저장 경로 <br>
├── data_extraction/ # 데이터 전처리용 스크립트 <br>
├── requirements.txt # 기본 패키지 목록 <br>
└── README.md # 실행 안내 파일 <br>

-------------------------------------------------------------------------

📁 1. 워크북 (workbook)<br>

실행 전 keys 폴더 생성 후  openai_key.txt 파일에 api key 입력 <br>

실행 경로<br>
workbook/main.py<br>

워크북 생성 기능 실행 코드 예시<br>
python3 workbook/main.py<br>


-------------------------------------------------------------------------

💬 2. 챗봇 (chatbot)<br>

실행 전 keys 폴더 생성 후  openai_key.txt 파일에 api key 입력 <br>

실행 경로<br>
chatbot/main.py<br>

챗봇 응답 실행 코드 예시<br>
python3 chatbot/main.py<br>
(챗봇에 입력 할 질문 수정을 위해선 main.py의 question 변수 값을 조정하면 됩니다)<br>

-------------------------------------------------------------------------

🏠 3. 홈캠 대화 분석 시스템 (HomeCam)<br>

실행 전 keys 폴더 생성 후  claude_key.txt, Huggingface_token 파일에 api key, Huggingface token 입력 <br>

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
