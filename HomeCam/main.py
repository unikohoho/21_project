import os
from datetime import datetime
from load_user import load_user_profile
from stt import run_stt
from diarization import run_diarization
from mapping import map_speaker_segments
from claude_request import build_prompt, request_claude
from pdf_report import generate_pdf_report

# 사용자 정보 로드
csv_path = "data/user_profiles.csv"
user_id = "u004"
user_info = load_user_profile(csv_path, user_id)

# 오디오 파일 경로 
audio_path = "data/HomeCam_Sample.wav"

# STT + 화자 분리
segments = run_stt(audio_path)
diarization = run_diarization(audio_path)
speaker_turns = map_speaker_segments(segments, diarization)

# 대화문 정리
dialogue = ""
for speaker, text in speaker_turns:
    dialogue += f"{speaker}: {text}\n"

# Claude API 호출
API_KEY = "MY_API" 
prompt = build_prompt(dialogue, user_info)
claude_response = request_claude(prompt, API_KEY)

# PDF 저장
output_dir = "outputs"
os.makedirs(output_dir, exist_ok=True)
filename = f"HomeCam_Emotion_Report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
output_path = os.path.join(output_dir, filename)
generate_pdf_report(output_path, claude_response)

print(f"PDF 저장 완료: {output_path}")
