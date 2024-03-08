import docx
import traceback

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