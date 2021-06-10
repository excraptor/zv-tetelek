import os
import markdown 
import pdfkit
from pathlib import Path

text = '<meta charset="utf-8">\n\n'

with os.scandir('TORZSTARGYAK-I/') as targyak:
    for targy in targyak:
        with os.scandir(targy) as tetelek:
            for tetel in tetelek:
                if ".md" in tetel.name:
                    with open('TORZSTARGYAK-I/' + targy.name + "/" + tetel.name, 'r', encoding="utf-8") as f:
                        content = f.read()
                        text += content
                        text += '\n'

with os.scandir('TORZSTARGYAK-II/') as targyak:
    for targy in targyak:
        with os.scandir(targy) as tetelek:
            for tetel in tetelek:
                if ".md" in tetel.name:
                    with open('TORZSTARGYAK-II/' + targy.name + "/" + tetel.name, 'r', encoding="utf-8") as f:
                        content = f.read()
                        text += content
                        text += '\n'

with open("kidolgozas.md", "w", encoding="utf-8") as f:
    f.write(text)

