import os
import numpy as np
from sklearn.preprocessing import normalize
from sentence_transformers import SentenceTransformer
import faiss

def retrieve_relevant_context(question: str, k: int = 2):
    with open("../data/ocr_paragraphs.txt", "r", encoding="utf-8") as f:
        raw_paragraphs = [line.strip().split(": ", 1)[1] for line in f if ": " in line]

    model = SentenceTransformer('snunlp/KR-SBERT-V40K-klueNLI-augSTS')
    corpus_embeddings = model.encode(raw_paragraphs)
    corpus_embeddings = normalize(corpus_embeddings, norm='l2')

    question_embedding = model.encode([question])
    question_embedding = normalize(question_embedding, norm='l2')

    index = faiss.IndexFlatIP(corpus_embeddings.shape[1])
    index.add(corpus_embeddings)

    _, I = index.search(question_embedding, k)
    top_paragraphs = [raw_paragraphs[i] for i in I[0]]

    return "\n".join(top_paragraphs)
