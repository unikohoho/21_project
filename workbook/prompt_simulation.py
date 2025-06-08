import pandas as pd
from openai import OpenAI
from utils import load_openai_api_key
import os

api_key = load_openai_api_key()  # OpenAI API 키 불러오기
client = OpenAI(api_key = api_key )  # OpenAI API 클라이언트 생성

# 유저 정보 CSV 불러오기
# df_users = pd.read_csv("../data/user_profiles.csv")
base_dir = os.path.dirname(os.path.abspath(__file__))  # 현재 파이썬 파일의 절대 경로
csv_path = os.path.join(base_dir, "../data/user_profiles.csv")
df_users = pd.read_csv(os.path.normpath(csv_path))

# GPT 프롬프트 생성
def generate_prompt(text_chunk, topic, user_id):

    # 유저 정보 불러오기
    user_info = df_users[df_users["user_id"] == user_id].iloc[0]

    # 유저 맞춤형 정보 추출
    child_age = user_info["child_age"]
    parenting_style = user_info["parenting_style"]
    parenting_goal = user_info["parenting_goal"]
    child_traits = user_info["child_traits"]
    health_issues = user_info["allergies_or_health_issues"]
    preferred_tone = user_info["preferred_tone"]

    return f"""
다음은 부모 교육 워크북을 위한 참고 이론입니다:

\"\"\"{text_chunk}\"\"\"

유저 정보:
- 아이 나이: {child_age}세
- 부모 육아 성향: {parenting_style}
- 육아 목표: {parenting_goal}
- 아이 특성: {child_traits}
- 건강/알러지 관련 사항: {health_issues}
- 선호 말투: {preferred_tone}

위 이론과 유저 정보를 기반으로, '{topic}' 주제에 대해 다음과 같이 구성된 워크북 액티비티 하나를 JSON 형식으로 생성하세요:

1. 활동 제목 (activity_title) — 학습자가 자기 인식을 할 수 있는 제목
2. activities: 각 액티비티는 아래 3가지 형식으로 구성됩니다.

---

- 첫 번째 활동: 작성형
  - instruction: 학습자가 자신의 경험을 돌아보며 서술하게 하세요.
  - example_answer: 작성 예시

- 두 번째 활동: 선택형
  - instruction: 학습자의 기존 반응을 보기 중에서 선택하도록 하세요.
  - options: 최소 4개의 반응 보기
  - optimal_option: 가장 이상적인 보기 1개

- 세 번째 활동: 시뮬레이션
  - instruction: 주어진 상황에서 학습자의 반응을 써보고 AI의 최적 반응과 비교할 수 있도록 하세요.
  - situation: 현실적인 부모-아이 간 갈등 상황
  - your_response: “___” 형태로 빈칸
  - ai_optimal_response: 부모와 아이 간의 대화 예시 (2~3턴)

---

출력은 반드시 다음과 같은 JSON 구조를 따르세요:
{{
  "activity_title": "...",
  "activities": [
    {{
      "type": "작성형",
      "instruction": "...",
      "example_answer": "..."
    }},
    {{
      "type": "선택형",
      "instruction": "...",
      "options": [...],
      "optimal_option": "..."
    }},
    {{
      "type": "시뮬레이션",
      "instruction": "...",
      "situation": "...",
      "your_response": "___",
      "ai_optimal_response": "부모: ...\\n아이: ..."
    }}
  ]
}}
반드시 JSON 형식으로만 응답하세요.
"""

# GPT 호출 함수
def generate_simulation(prompt):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "너는 부모교육 코치야. 실제 상황에서 아이와 일어날 만하거나, 부모로서 자신을 알아갈 시뮬레이션을 만들어줘."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )
    return response.choices[0].message.content
