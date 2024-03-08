
import traceback
import PyPDF2
from PyPDF2 import PdfReader

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