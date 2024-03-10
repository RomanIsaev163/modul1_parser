import unittest
from utility import *
from docs_readers import *
from utility import *

class TestParser(unittest.TestCase):
    def setUp(self):
        self.good_path_doc = './parser_doc_docx_pdf/test_files/test.doc'
        self.good_path_docx = './parser_doc_docx_pdf/test_files/test.docx'
        self.good_path_pdf = './parser_doc_docx_pdf/test_files/test.pdf'
        self.broken_path = 'XXXXXXXX'
        self.null_path = None
        self.empty_path = ''
        
    def test1_read_docx_file_docx(self):
       self.assertRaises(Exception, read_docx_file(self.good_path_docx))

    def test2_read_pdf_file_pdf(self):
       self.assertRaises(Exception, read_pdf_file(self.good_path_pdf))

    def test3_read_docx_file_pdf(self):
       self.assertRaises(Exception, read_docx_file(self.good_path_pdf))

    def test4_read_pdf_file_doc(self):
       self.assertRaises(Exception, read_pdf_file(self.good_path_docx))

    def test5_read_docx_file_doc(self):
       self.assertRaises(Exception, read_docx_file(self.good_path_doc))

    def test6_read_pdf_file_doc(self):
       self.assertRaises(Exception, read_pdf_file(self.good_path_doc))


    def test7_read_pdf_broken_path(self):
       self.assertRaises(Exception, read_pdf_file(self.broken_path))

    def test8_read_pdf_broken_path(self):
       self.assertRaises(Exception, read_pdf_file(self.null_path))

    def test8_read_pdf_broken_path(self):
       self.assertRaises(Exception, read_pdf_file(self.empty_path))


    def test9_read_docx_broken_path(self):
       self.assertRaises(Exception, read_docx_file(self.broken_path))

    def test10_read_docx_broken_path(self):
       self.assertRaises(Exception, read_docx_file(self.null_path))

    def test11_read_docx_broken_path(self):
       self.assertRaises(Exception, read_docx_file(self.empty_path))


    def test13_convert_doc_docx(self):
       self.assertRaises(Exception, convert_doc_docx([[self.broken_path, 'TEST']], 'test_files'))

    def test14_convert_doc_docx(self):
       self.assertRaises(Exception, convert_doc_docx([[self.empty_path, 'TEST']], 'test_files'))

    def test15_convert_doc_docx(self):
       self.assertRaises(Exception, convert_doc_docx([[self.null_path, 'TEST']], 'test_files'))


    def test16_convert_doc_docx(self):
       self.assertRaises(Exception, convert_doc_docx([[self.good_path_pdf, 'TEST']], 'test_files'))

    def test17_convert_doc_docx(self):
       self.assertRaises(Exception, convert_doc_docx([[self.good_path_doc, 'TEST']], 'test_files'))

    def test18_convert_doc_docx(self):
       self.assertRaises(Exception, convert_doc_docx([[self.good_path_docx, 'TEST']], 'test_files'))
            
unittest.main()