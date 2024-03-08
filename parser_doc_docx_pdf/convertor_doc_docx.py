import re
import aspose.words as aw
import os

def convert_doc_docx(doc_file_paths: str, converted_files_dir_path: str)->list[tuple[str,str]]:
    '''
        Конвертируем .doc файлы в .docx, так как python не открывает файлы .doc
        Возвращаемые кортежи содержат правилльный полный путь к файлу, но старое расширение в имени файла
        Новые файлы содержат в начале Evaluation Only. Created with Aspose.Words. Copyright 2003-2022 Aspose Pty Ltd.
    '''
    new_docx_paths = []
    file_extension = re.compile(r'\..*')
    for doc_file_path, doc_file_name in doc_file_paths:
        doc = aw.Document(doc_file_path)
        new_docx_path = os.path.join(converted_files_dir_path, file_extension.sub("", doc_file_name) + '.docx')
        doc.save(new_docx_path)
        new_docx_paths.append((new_docx_path, doc_file_name))
    return new_docx_paths