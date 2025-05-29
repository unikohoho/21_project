from preprocess_data import load_and_clean_text
from preprocess_data import split_text
from prompt_simulation import generate_prompt
from prompt_simulation import generate_simulation
import json

def run_workbook_simulation(csv_path, topic, user_id):
    text = load_and_clean_text(csv_path)
    chunks = split_text(text, max_tokens=1200)
    workbook_activities = []

    for i, chunk in enumerate(chunks[:3]):  # 일부만 사용 (속도 고려)
        # 프롬프트 생성
        prompt = generate_prompt(chunk, topic, user_id)
        try:
          # 생성한 프롬프트(prompt)로 gpt 호출
            raw_output = generate_simulation(prompt)
            gpt_json = json.loads(raw_output)

          # 응답(output)을 워크북 액티비티 형식으로 포맷
            activity = {
                "activity_title": gpt_json["activity_title"],
                "activities": gpt_json["activities"]
            }

            workbook_activities.append(activity)

            # 프린트 확인용
            print(f"\n Activity {i+1} — {activity['activity_title']}")
            for j, act in enumerate(activity["activities"]):
                print(f"\n{j+1}. [{act['type']}] {act['instruction']}")
                if act['type'] == "작성형":
                    print(f"예시 답변: {act['example_answer']}")
                elif act['type'] == "선택형":
                    for k, opt in enumerate(act['options']):
                        print(f"  {k+1}) {opt}")
                    print(f"★ AI가 추천하는 선택: {act['optimal_option']}")
                elif act['type'] == "시뮬레이션":
                    print(f"상황: {act['situation']}")
                    print("AI 추천 반응:\n" + act['ai_optimal_response'])

        except Exception as e:
            print(f" GPT 처리 실패 (chunk {i}): {e}")

    return workbook_activities