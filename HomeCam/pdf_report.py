from fpdf import FPDF
import os
import re
from datetime import datetime
import requests


def download_font(font_name, url):
    if not os.path.exists(font_name):
        r = requests.get(url)
        if r.status_code == 200:
            with open(font_name, "wb") as f:
                f.write(r.content)
        else:
            raise Exception(f"{font_name} 다운로드 실패 (상태 코드: {r.status_code})")


class ReportPDF(FPDF):
    def header(self):
        self.set_font("Nanum", '', 14)
        self.cell(0, 10, "부모-아이 대화 감정 분석 리포트", ln=True, align="C")
        self.set_font("Nanum", '', 11)
        self.cell(0, 10, f"분석 날짜: {datetime.now().strftime('%Y-%m-%d')}", ln=True, align="C")
        self.ln(10)

    def chapter_title(self, title):
        self.set_font("Nanum", 'B', 12)
        self.cell(0, 10, title, ln=True)
        self.ln(2)

    def chapter_body(self, body):
        self.set_font("Nanum", '', 11)
        self.multi_cell(0, 8, body)
        self.ln()


def clean_text(text):
    return re.sub(r"[^\uAC00-\uD7A3\u3131-\u318E\u1100-\u11FF\u0020-\u007E\n.,?!\"'()\-:]", "", text)


def generate_pdf_report(output_path, claude_response):
    download_font("NanumGothic.ttf", "https://github.com/google/fonts/raw/main/ofl/nanumgothic/NanumGothic-Regular.ttf")
    download_font("NanumGothicBold.ttf", "https://github.com/google/fonts/raw/main/ofl/nanumgothic/NanumGothic-Bold.ttf")

    pdf = ReportPDF()
    pdf.add_font('Nanum', '', 'NanumGothic.ttf', uni=True)
    pdf.add_font('Nanum', 'B', 'NanumGothicBold.ttf', uni=True)
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.chapter_title("HomeCam Emotion Analysis Report")
    pdf.chapter_body(clean_text(claude_response))
    pdf.output(output_path)
