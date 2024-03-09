import docx
import traceback
import PyPDF2
from PyPDF2 import PdfReader
import re
import aspose.words as aw
import pandas as pd

from utility import convert_doc_docx

def read_docx_file(docx_file_path: str) -> str:
    '''
        Открываем .docx файл и, соединяя все абзацы,
        возращем полный текст документа
        или None если не удалось открыть файл
    '''
    try:
        doc = docx.Document(docx_file_path)
        all_paras = doc.paragraphs
        full_doc_text = ''
        for para in all_paras:
            full_doc_text = full_doc_text + '\n' + para.text
        return full_doc_text.replace('Evaluation Only. Created with Aspose.Words. Copyright 2003-2022 Aspose Pty Ltd.', '')
    except:
        print(f'Ошибка: Не удалось открыть файл: {docx_file_path}\n {traceback.format_exc()}')
        return None
    
def read_pdf_file(pdf_file_path: str) -> str:
    '''
        Открываем .pdf файл и, соединяя все страницы,
        возращем полный текст документа
        или None если не удалось открыть файл
    '''
    try:
        full_pdf_text = ''
        with open(pdf_file_path, "rb") as filehandle:
            pdf = PdfReader(filehandle)
            num_pages = len(pdf.pages)
            for num in range(num_pages):
                page = pdf.pages[num]
                full_pdf_text = full_pdf_text + '\n' + page.extract_text()
        return full_pdf_text
    except:
        print(f'Ошибка: Не удалось открыть файл: {pdf_file_path}\n {traceback.format_exc()}')
        return None
    
def read_document(document_file_full_path: str, save_dir_path: str = '') -> str:
    re_file_extension = re.compile(r'\.\w+')
    file_name = re.search(r'\/([\w\d]+)\.', document_file_full_path).group(1)
    dir_path = re.search(r'.+\/', document_file_full_path).group(0)
    file_extension = re_file_extension.findall(document_file_full_path)

    if save_dir_path == '':
        save_dir_path = dir_path
    
    if file_extension[0] == '.docx':
        return read_docx_file(document_file_full_path)
    
    elif file_extension[0] == '.doc' or file_extension[0] == '.rtf':
        print('исправляем документ')
        new_docx_path = convert_doc_docx([[document_file_full_path, file_name]], save_dir_path)[0][0]
        return read_docx_file(new_docx_path)

    elif file_extension[0] == '.pdf':
        return read_pdf_file(document_file_full_path)
    
def create_df(documents_files_paths: list[str]):
    text_filename = []
    for document_path, filename in documents_files_paths:
        text = read_document(document_path)
        text_filename.append([text, filename])

    
    df = pd.DataFrame(data=text_filename, columns=['text', 'doc_file_name'])
    return df