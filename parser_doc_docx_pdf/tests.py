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


      data_dir = './parser_doc_docx_pdf/test_files'
      self.all_symbols = ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'

      doc_file_paths, docx_file_paths, pdf_file_paths, rtf_file_paths = init_file_paths(data_dir)

      self.doc_content_df = create_df(doc_file_paths)
      self.empty_doc_file_name = 'empty.doc'
      self.all_doc_file_name = 'all.doc'

      self.docx_content_df = create_df(docx_file_paths)
      self.empty_docx_file_name = 'empty.docx'
      self.all_docx_file_name = 'all.docx'

      self.pdf_content_df = create_df(pdf_file_paths)
      self.empty_pdf_file_name = 'empty.pdf'
      self.all_pdf_file_name = 'all.pdf'

      self.rtf_content_df = create_df(rtf_file_paths)
      self.empty_rtf_file_name = 'empty.rtf'
      self.all_rtf_file_name = 'all.rtf'
      
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
         
   # CONTENT TEST CASE
   def test_content_doc_empty(self):
      content = self.doc_content_df[self.doc_content_df['doc_file_name'] == self.empty_doc_file_name]['text'].values[0]
      self.assertEqual('\n', content)

   def test_content_docx_empty(self):
      content = self.doc_content_df[self.docx_content_df['doc_file_name'] == self.empty_docx_file_name]['text'].values[0]
      self.assertEqual('\n', content)

   def test_content_pdf_empty(self):
      content = self.doc_content_df[self.pdf_content_df['doc_file_name'] == self.empty_pdf_file_name]['text'].values[0]
      self.assertEqual('\n', content)

   def test_content_rtf_empty(self):
      content = self.doc_content_df[self.rtf_content_df['doc_file_name'] == self.empty_rtf_file_name]['text'].values[0]
      self.assertEqual('\n', content)


   def test_content_doc_all(self):
      content = self.doc_content_df[self.doc_content_df['doc_file_name'] == self.all_doc_file_name]['text'].values[0]
      self.assertEqual(self.all_symbols, content)

   def test_content_docx_all(self):
      content = self.doc_content_df[self.docx_content_df['doc_file_name'] == self.all_docx_file_name]['text'].values[0]
      self.assertEqual(self.all_symbols, content)

   def test_content_pdf_all(self):
      content = self.doc_content_df[self.pdf_content_df['doc_file_name'] == self.all_pdf_file_name]['text'].values[0]
      self.assertEqual(self.all_symbols, content)

   def test_content_rtf_all(self):
      content = self.doc_content_df[self.rtf_content_df['doc_file_name'] == self.all_rtf_file_name]['text'].values[0]
      self.assertEqual(self.all_symbols, content)



unittest.main()