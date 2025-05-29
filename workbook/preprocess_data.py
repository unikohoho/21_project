import pandas as pd
import tiktoken

## 문서 데이터 준비
# CSV에서 텍스트 불러오기 + 전처리
def load_and_clean_text(filepath):
    df = pd.read_csv(filepath)
    raw_text = " ".join(df.iloc[:, 1].astype(str))  # 두 번째 컬럼이 본문이라고 가정
    cleaned_text = raw_text.replace("\n", " ").replace("\xa0", " ").strip()
    return cleaned_text

# 텍스트 토큰 단위로 나누기 위한 함수 (gpt-4 기준)
def split_text(text, max_tokens=1500):
    enc = tiktoken.encoding_for_model("gpt-4")
    tokens = enc.encode(text)
    chunks = []
    while tokens:
        chunk = tokens[:max_tokens]
        tokens = tokens[max_tokens:]
        chunks.append(enc.decode(chunk))
    return chunks