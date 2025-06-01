import requests


def build_prompt(dialogue, user_info):
    return f"""당신은 초보 부모를 위한 감정 분석 상담 AI입니다.

다음은 실제 홈캠에서 수집된 부모와 아이 간의 대화입니다. 화자는 SPEAKER_00과 SPEAKER_01로 구분되어 있으며, 이 대화를 바탕으로 말투, 감정, 상호작용을 분석해 주세요.

분석 시, 아래 사용자 특성을 꼭 반영해 **사용자에게 맞춤형 피드백과 공감 어린 조언**을 제공해 주세요:

사용자 정보:
- 자녀 나이: {user_info['child_age']}
- 양육 스타일: {user_info['parenting_style']}
- 양육 목표: {user_info['parenting_goal']}
- 자녀 성향: {user_info['child_traits']}
- 선호하는 말투: {user_info['preferred_tone']}
- 사용하는 언어: {user_info['language']}
- 알레르기나 건강 이슈: {user_info['health_issues']}

아래 항목에 대해 분석해 주세요:
1. 각 화자가 어떤 역할(부모 / 아이)인지 자연스럽게 추론해 주세요.
2. 부모는 어떤 말투나 감정을 표현하고 있나요? 아이에게 긍정적인 영향을 줄 수 있는 표현과, 더 나은 표현 방식이 있다면 함께 알려주세요.
3. 아이는 어떤 감정 상태를 보이고 있나요? 대사 속에 드러난 감정, 욕구, 요구를 설명해 주세요.
4. 부모와 아이의 상호작용이 아이의 정서 발달에 어떤 영향을 줄 수 있을지, 사용자 정보에 맞추어 분석해 주세요.
5. 초보 부모에게 도움이 될 만한 따뜻하고 공감 가는 조언을 제공해 주세요. 단정적인 표현은 피하고, 필요 시 전문가 상담을 권유하는 방식으로 안내해 주세요.

[대화 내용]
{dialogue}

모든 응답은 한국어로, 친절하고 이해하기 쉬운 말투로 작성해 주세요.
"""


def load_claude_key_from_file(path="../keys/claude_key.txt"):
    with open(path, "r") as f:
        return f.read().strip()


def request_claude(prompt):
    api_key = load_claude_key_from_file()
    api_url = "https://api.anthropic.com/v1/messages"
    headers = {
        "x-api-key": api_key,
        "anthropic-version": "2023-06-01",
        "Content-Type": "application/json"
    }
    data = {
        "model": "claude-3-haiku-20240307",
        "max_tokens": 1000,
        "messages": [{"role": "user", "content": prompt}]
    }
    response = requests.post(api_url=api_url, headers=headers, json=data)
    if response.status_code == 200:
        raw = response.json()["content"]
        return "\n\n".join(block["text"] for block in raw if "text" in block).strip() if isinstance(raw, list) else raw.strip()
    else:
        raise Exception(f"Claude API 호출 실패: {response.status_code}")
