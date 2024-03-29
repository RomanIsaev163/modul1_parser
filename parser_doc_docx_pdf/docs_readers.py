import docx
import traceback
import PyPDF2
from PyPDF2 import PdfReader
import re
import aspose.words as aw
import pandas as pd
from convert_djvu2pdf import convert_djvu2pdf
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
            full_doc_text = full_doc_text + para.text
        return full_doc_text.replace('Evaluation Only. Created with Aspose.Words. Copyright 2003-2024 Aspose Pty Ltd.', '')
    except:
        print(f'Ошибка: Не удалось открыть файл: {docx_file_path}')
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
            # print(f'num_pages: {num_pages}')
            for num in range(num_pages):
                page = pdf.pages[num]
                # print(f'page.extract_text(): {len(page.extract_text())}')
                full_pdf_text = full_pdf_text + page.extract_text().strip()
        return full_pdf_text.strip() # костыль чтобы убрать первый пробельный символ
    except:
        print(f'Ошибка: Не удалось открыть файл: {pdf_file_path}')
        return None
    
def read_document(document_file_full_path: str, save_dir_path: str = '') -> str:
    '''
        Читаем текст документа с расширениями doc docx pdf rtf
        Для чтения doc и rtf конвертируем их в формат docx и сохраняем в директорию save_dir_path
        Если save_dir_path не указано, то сохраняется в изначальную директорию
    '''
    re_file_extension = re.compile(r'\.\w+')
    file_name = re.search(r'\/([\w\d]+)\.', document_file_full_path).group(1)
    dir_path = re.search(r'.+\/', document_file_full_path).group(0)
    file_extension = re_file_extension.findall(document_file_full_path)

    if save_dir_path == '':
        save_dir_path = dir_path
    
    if file_extension[0] == '.docx':
        return read_docx_file(document_file_full_path)
    
    elif file_extension[0] == '.doc' or file_extension[0] == '.rtf':
        # print('исправляем документ')
        new_docx_path = convert_doc_docx([[document_file_full_path, file_name]], save_dir_path)[0][0]
        return read_docx_file(new_docx_path)

    elif file_extension[0] == '.pdf':
        return read_pdf_file(document_file_full_path)
    # не работает 
    elif file_extension[0] == '.djvu':
        convert_djvu2pdf([document_file_full_path])
        new_pdf_path = f'{dir_path}{file_name}.pdf'
        # print(f'new_pdf_path: {new_pdf_path}')
        return read_pdf_file(new_pdf_path)
    
def create_df(documents_files_paths: list[str]):
    '''
        Читаем список файлов и сохраняем их текст и имя файла в df
    '''
    text_filename = []
    for document_path, filename in documents_files_paths:
        text = read_document(document_path)
        text_filename.append([text, filename])

    
    df = pd.DataFrame(data=text_filename, columns=['text', 'doc_file_name'])
    return df