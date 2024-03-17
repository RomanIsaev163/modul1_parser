import os, fitz 
import re
from docs_readers import read_pdf_file
import pytesseract
from PIL import Image

filePath = 'data_dir/hacka-aka-embedika-2/docs/4a5707e447271a188a1211606b158a94.pdf'
  # get filename from command line
doc = fitz.open(filePath)  # open document
path, fileName = os.path.split(filePath)
fileBaseName, fileExtension = os.path.splitext(fileName)
dir_to_save='data_dir/pdf_image'
print(fileBaseName)
print(f'{os.path.join(dir_to_save, fileBaseName)}-1.png')
for page in doc:  # iterate through the pages
    pix = page.get_pixmap()  # render page to an image
    pix.save(f'{os.path.join(dir_to_save, fileBaseName)}-page-{page.number}.jpg')

imgae_path = '/Users/romanisaev/VS code projects/html_parser/data_dir/pdf_image/4a5707e447271a188a1211606b158a94-page-0.jpg'
with Image.open(imgae_path) as image:
  txt = pytesseract.image_to_string(image).encode("utf-8")
  print(txt)
