from run_workbook_simulation import run_workbook_simulation
import os

# 현재 실행 중인 파일의 절대 경로 기준으로 경로 설정
base_dir = os.path.dirname(os.path.abspath(__file__))

# CSV 파일 경로 설정
ocr_paragraphs_path = os.path.join(base_dir, "../data/ocr_paragraphs.csv")

# 워크북 시뮬레이션 실행
# 예: 나를 아는 부모 주차 실행
activities = run_workbook_simulation(ocr_paragraphs_path, "나를 아는 부모", "u004")