from __future__ import annotations
import os
import PyPDF2
from PyPDF2 import PdfReader
import docx
import pandas as pd
import numpy as np
import json
import aspose.words as aw
import traceback
import re
from download_data import download
from utility import get_docs_paths, init_file_paths
from docs_readers import read_document, create_df
from convert_djvu2pdf import convert_djvu2pdf
from pdf_image import read_pdf_image

download()
data_dir = 'data_dir/hacka-aka-embedika-2/docs'
json_path = 'data_dir/hacka-aka-embedika-2/classes.json'

converted_docx_dir = 'converted_docx'
filenames = os.listdir(data_dir)

with open(json_path) as json_file:
    label_dict = json.load(json_file)

doc_file_paths, docx_file_paths, pdf_file_paths, rtf_file_paths = init_file_paths(data_dir)

# create_df(doc_file_paths).to_csv('docs_data.csv')
create_df(doc_file_paths).to_csv('docx_file_paths.csv')
pdf_image_path_file = '' # подойдет любой pdf документ
text = read_pdf_image(pdf_image_path_file)
