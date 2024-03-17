import re
import aspose.words as aw
import os 
import pandas as pd

def init_file_paths(data_dir_path: str) -> tuple[list[tuple[str,str]],
                                                 list[tuple[str,str]],
                                                 list[tuple[str,str]],
                                                 list[tuple[str,str]]]:
    '''
        Создаем списоки кортежей (полный путь, имя файла) для каждого расширения файла
    '''
    doc_file_paths = []
    docx_file_paths = []
    pdf_file_paths = []
    rtf_file_paths = []
    for filename in os.listdir(data_dir_path):
        try:
            if filename.endswith('.docx', -5):
                docx_file_paths.append((os.path.join(data_dir_path,filename), filename))
            elif filename.endswith('.pdf', -5):
                pdf_file_paths.append((os.path.join(data_dir_path,filename), filename))
            elif filename.endswith('.rtf', -5):
                rtf_file_paths.append((os.path.join(data_dir_path,filename), filename))
            elif filename.endswith('.doc', -5):
                doc_file_paths.append((os.path.join(data_dir_path,filename), filename))
        except:
            continue
    
    # print(f'Количество pdf-файлов: {len(pdf_file_paths)}')
    # print(f'Количество doc-файлов: {len(doc_file_paths)}')
    # print(f'Количество docx-файлов: {len(docx_file_paths)}')
    # print(f'Количество rtf-файлов: {len(rtf_file_paths)}')

    return doc_file_paths, docx_file_paths, pdf_file_paths, rtf_file_paths


def get_docs_paths(data_dir: str, converted_docx_dir: str):
    doc_file_paths, docx_file_paths, pdf_file_paths, rtf_file_paths = init_file_paths(data_dir)
    files_paths_to_docx = []
    files_paths_to_docx += doc_file_paths
    files_paths_to_docx += rtf_file_paths
    docx_file_paths += convert_doc_docx(files_paths_to_docx, converted_docx_dir)
    return doc_file_paths, docx_file_paths, pdf_file_paths, rtf_file_paths

def convert_doc_docx(doc_file_paths: list[list[str, str]], converted_files_dir_path: str)->list[tuple[str,str]]:
    '''
        Конвертируем .doc файлы в .docx, так как python не открывает файлы .doc
        Возвращаемые кортежи содержат правилльный полный путь к файлу, но старое расширение в имени файла
        Новые файлы содержат в начале Evaluation Only. Created with Aspose.Words. Copyright 2003-2022 Aspose Pty Ltd.
    '''

    new_docx_paths = []
    file_extension = re.compile(r'\..*')
    
    for doc_file_path, doc_file_name in doc_file_paths:
        try:
            doc = aw.Document(doc_file_path)
            new_docx_path = os.path.join(converted_files_dir_path, file_extension.sub("", doc_file_name) + '.docx')
            doc.save(new_docx_path)
            new_docx_paths.append((new_docx_path, doc_file_name))
        except:
            continue

    return new_docx_paths
