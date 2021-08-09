
from typing import Text
from docx import Document
file = Document('D:/Desktop/明御®运维审计与风险控制系统V2.0.8.3.1.2应用发布手册.docx')
para = file.paragraphs[1]
#print(para.text)
blo = para.runs
for text_text in blo:
    print(text_text.text)

