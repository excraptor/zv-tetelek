import os
import markdown 
import pdfkit
from pathlib import Path

text = '<meta charset="utf-8">\n'

def add_to_pdf(directory):
    global text
    with os.scandir(directory) as targyak:
        for targy in targyak:
            with os.scandir(targy) as tetelek:
                for tetel in tetelek:
                    if ".md" in tetel.name:
                        with open(tetel, 'r', encoding="utf-8") as f:
                            content = f.read()
                            text += content


add_to_pdf('TORZSTARGYAK-I')
add_to_pdf('TORZSTARGYAK-II')

html = markdown.markdown(text)
pdfkit.from_string(html, 'kidolgozas.pdf')

