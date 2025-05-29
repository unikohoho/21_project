import os
import json
import pandas as pd
from google.cloud import vision_v1
from google.cloud import storage
from langchain.text_splitter import RecursiveCharacterTextSplitter

# GCP 키 파일
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "keys/owner_key.json"

def extract_text_from_gcs(bucket_name: str, pdf_file: str, output_csv: str):
    # Vision OCR 클라이언트
    client = vision_v1.ImageAnnotatorClient()

    # GCS 경로 설정
    gcs_source_uri = f"gs://{bucket_name}/{pdf_file}"
    gcs_output_uri = f"gs://{bucket_name}/ocr_output/"

    # OCR 요청 설정
    feature = vision_v1.Feature(type_=vision_v1.Feature.Type.DOCUMENT_TEXT_DETECTION)
    gcs_source = vision_v1.GcsSource(uri=gcs_source_uri)
    input_config = vision_v1.InputConfig(gcs_source=gcs_source, mime_type="application/pdf")

    gcs_destination = vision_v1.GcsDestination(uri=gcs_output_uri)
    output_config = vision_v1.OutputConfig(gcs_destination=gcs_destination, batch_size=5)

    async_request = {
        "requests": [
            {
                "input_config": input_config,
                "features": [feature],
                "output_config": output_config,
            }
        ]
    }

    operation = client.async_batch_annotate_files(request=async_request)

    print("OCR 요청 완료, GCP 처리 중...")
    operation.result(timeout=300)
    print("OCR 완료!")

    # 결과 JSON 다운로드 및 파싱
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob_list = list(bucket.list_blobs(prefix="ocr_output"))
    json_blobs = [b for b in blob_list if b.name.endswith(".json")]

    all_text = ""
    for blob in json_blobs:
        result = json.loads(blob.download_as_bytes())
        responses = result.get("responses", [])
        for response in responses:
            text = response.get("fullTextAnnotation", {}).get("text", "")
            all_text += text + "\n"

    # LangChain으로 문맥 단위 분리
    splitter = RecursiveCharacterTextSplitter(            
        chunk_size=500,
        chunk_overlap=50,
        separators=["\n\n", "\n", ". ", " "]
    )
    chunks = splitter.split_text(all_text)

    # Tabular 데이터로 저장 (id, content 컬럼)
    paragraphs = [{"id": i + 1, "content": chunk.strip()} for i, chunk in enumerate(chunks)]
    df = pd.DataFrame(paragraphs)

    os.makedirs(os.path.dirname(output_csv), exist_ok=True)
    df.to_csv(output_csv, index=False, encoding="utf-8")

    print(f"OCR 결과 CSV 저장 완료: {output_csv}")