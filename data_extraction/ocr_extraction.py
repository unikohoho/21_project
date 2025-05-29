import os
from google.cloud import vision_v1
from google.cloud import storage

# GCP account key file 
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "owner_key.json"

def extract_text_from_gcs(bucket_name, pdf_file, output_txt):
    # OCR 클라이언트 설정
    client = vision_v1.ImageAnnotatorClient()

    gcs_source_uri = f"gs://{bucket_name}/{pdf_file}"
    gcs_output_uri = f"gs://{bucket_name}/ocr_output/"

    mime_type = "application/pdf"
    batch_size = 5

    feature = vision_v1.Feature(type_=vision_v1.Feature.Type.DOCUMENT_TEXT_DETECTION)
    gcs_source = vision_v1.GcsSource(uri=gcs_source_uri)
    input_config = vision_v1.InputConfig(gcs_source=gcs_source, mime_type=mime_type)

    gcs_destination = vision_v1.GcsDestination(uri=gcs_output_uri)
    output_config = vision_v1.OutputConfig(gcs_destination=gcs_destination, batch_size=batch_size)

    async_request = vision_v1.AsyncAnnotateFileRequest(
        features=[feature],
        input_config=input_config,
        output_config=output_config,
    )

    operation = client.async_annotate_file(request=async_request)
    print("OCR 요청 완료, 대기 중 . . . ")
    operation.result(timeout=300)
    print("OCR 완료!")

    # OCR 결과 저장된 위치에서 JSON 결과 다운로드
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob_list = list(bucket.list_blobs(prefix="ocr_output"))
    json_blobs = [b for b in blob_list if b.name.endswith(".json")]

    import json
    paragraphs = []
    for blob in json_blobs:
        result = json.loads(blob.download_as_bytes())
        responses = result["responses"]
        for idx, response in enumerate(responses):
            text = response.get("fullTextAnnotation", {}).get("text", "")
            for i, para in enumerate(text.split("\n\n")):
                clean = para.strip().replace("\n", " ")
                if len(clean) > 50:
                    paragraphs.append(f"{blob.name}_{idx+1}_{i+1}: {clean}")

    with open(output_txt, "w", encoding="utf-8") as f:
        f.write("\n".join(paragraphs))
    print(f"저장 완료: {output_txt}")
