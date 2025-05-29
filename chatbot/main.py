from embedding_retrieval import retrieve_relevant_context
from user_context import load_user_profile
from generate_response import generate_chat_response

# 사용자 질문
question = '아이가 친구랑 자주 다투어요. 어떻게 사회성을 길러줄 수 있을까요?'
# 사용자 ID
user_id = "u004"

# ID를 통해 사용자 정보 불러오기
user_info = load_user_profile(user_id)

# 문서에서 관련 문맥 검색
combined_context = retrieve_relevant_context(question)

# 챗봇 응답 생성
response = generate_chat_response(question, combined_context, user_info)

print("\n 사용자 질문:\n")
print(question)
print("\n 챗봇 답변:\n")
print(response)
