from ocr_extraction import extract_text_from_gcs

# 원본 pdf 파일이 올라가 있는 gcp의 bucket 
bucket_name = "uni_s_first_bucket_gcp"
# bucket 안에 있는 OCR 진행 할 raw pdf 파일명
pdf_filename = "감정코칭.pdf"
# OCR 결과 저장할 경로와 파일명
ocr_csv_path = "data/ocr_paragraphs.csv"

# OCR 수행
extract_text_from_gcs(bucket_name, pdf_filename, ocr_csv_path)
print("OCR 텍스트 추출 및 저장 완료!")