import aspose.imaging as im
from aspose.imaging import *
from aspose.imaging.imageoptions import *
import re
from docs_readers import read_pdf_file
import pytesseract
from PIL import Image
from pdf2image import convert_from_path
import os

filePath = '/Users/romanisaev/VS code projects/html_parser/data_dir/hacka-aka-embedika-2/docs/4a5707e447271a188a1211606b158a94.pdf'
doc = convert_from_path(filePath)
path, fileName = os.path.split(filePath)
fileBaseName, fileExtension = os.path.splitext(fileName)

for page_number, page_data in enumerate(doc):
    txt = pytesseract.image_to_string(Image.fromarray(page_data)).encode("utf-8")
    print("Page # {} - {}".format(str(page_number),txt))
