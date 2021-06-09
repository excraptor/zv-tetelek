import os
import markdown 
import pdfkit
from pathlib import Path

text = '<meta charset="utf-8">\n'

with os.scandir('TORZSTARGYAK-I/') as targyak:
    for targy in targyak:
        with os.scandir(targy) as tetelek:
            for tetel in tetelek:
                if ".md" in tetel.name:
                    with open('TORZSTARGYAK-I/' + targy.name + "/" + tetel.name, 'r', encoding="ISO-8859-1") as f:
                        content = f.read()
                        text += content

with os.scandir('TORZSTARGYAK-II/') as targyak:
    for targy in targyak:
        with os.scandir(targy) as tetelek:
            for tetel in tetelek:
                if ".md" in tetel.name:
                    with open('TORZSTARGYAK-II/' + targy.name + "/" + tetel.name, 'r', encoding="ISO-8859-1") as f:
                        content = f.read()
                        text += content

html = markdown.markdown(text)
pdfkit.from_string(html, 'kidolgozas.pdf')

